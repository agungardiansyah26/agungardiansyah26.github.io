from playwright.sync_api import sync_playwright
import os
import time

def test_xss_mitigation():
    cwd = os.getcwd()
    file_path = f"file://{cwd}/index.html"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        msgs = []
        page.on("console", lambda msg: msgs.append(msg.text))

        print(f"Loading: {file_path}")
        page.goto(file_path)

        print("Injecting XSS payload into translations object...")
        page.evaluate("""
            translations.id.nav.projects = "<img src='x' onerror=\\"console.log('XSS_SUCCESS')\\"> <span class='test'>Proyek</span> <script>console.log('XSS_SUCCESS_SCRIPT')</script>";
            updateContent('id');
        """)

        time.sleep(1)

        print("Verifying if XSS payload was executed...")
        if "XSS_SUCCESS" in msgs or "XSS_SUCCESS_SCRIPT" in msgs:
            print("FAIL: XSS payload executed! Console messages:", msgs)
            raise Exception("XSS payload executed!")
        else:
            print("PASS: XSS payload blocked!")

        html = page.evaluate("document.querySelector('a[data-i18n=\"nav.projects\"]').innerHTML")
        print("Sanitized HTML:", html)
        if "<img" in html or "<script" in html:
            print("FAIL: Disallowed tags found in DOM!")
            raise Exception("Disallowed tags found in DOM!")
        else:
            print("PASS: Disallowed tags stripped from DOM!")

        if "<span" in html:
            print("PASS: Allowed tags preserved in DOM!")
        else:
            print("FAIL: Allowed tags missing from DOM!")
            raise Exception("Allowed tags missing from DOM!")

        browser.close()

if __name__ == "__main__":
    test_xss_mitigation()

def test_xss_href_mitigation():
    import os, time
    from playwright.sync_api import sync_playwright
    cwd = os.getcwd()
    file_path = f"file://{cwd}/index.html"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        msgs = []
        page.on("console", lambda msg: msgs.append(msg.text))

        print(f"Loading: {file_path}")
        page.goto(file_path)

        print("Injecting XSS href payload into translations object...")
        page.evaluate("""
            translations.id.nav.projects = "<a href='javascript:console.log(\\"XSS_HREF_SUCCESS\\")'>Click Me</a>";
            updateContent('id');
        """)

        time.sleep(1)

        print("Clicking the injected link...")
        page.click("text=Click Me")

        time.sleep(1)

        print("Verifying if XSS href payload was executed...")
        if "XSS_HREF_SUCCESS" in msgs:
            print("FAIL: XSS href payload executed! Console messages:", msgs)
            raise Exception("XSS href payload executed!")
        else:
            print("PASS: XSS href payload blocked!")

        browser.close()

if __name__ == "__main__":
    test_xss_mitigation()
    test_xss_href_mitigation()
