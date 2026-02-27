from playwright.sync_api import sync_playwright
import os
import sys

def test_xss_vulnerability():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Capture console messages
        page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))

        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"
        print(f"Loading: {file_path}")
        page.goto(file_path)

        print("Injecting malicious payload...")
        page.evaluate("""
            const maliciousPayload = 'Hello <img src=x onerror="document.body.setAttribute(\\'data-hacked\\', \\'true\\')" id="xss-trigger"> <b id="safe-tag">World</b>';

            try {
                if (typeof translations === 'undefined') throw new Error('translations is undefined');
                if (typeof updateContent === 'undefined') throw new Error('updateContent is undefined');
                if (typeof sanitizeHTML === 'undefined') throw new Error('sanitizeHTML is undefined');

                translations['id']['hero']['title'] = maliciousPayload;
                console.log('Payload injected. Updating content...');
                updateContent('id');
                console.log('Content updated.');
            } catch (e) {
                console.error('JS Error:', e);
                document.body.setAttribute('data-error', e.message);
                // Also log stack
                console.error(e.stack);
            }
        """)

        error = page.locator("body").get_attribute("data-error")
        if error:
             print(f"TEST ERROR: JS Error: {error}")
             sys.exit(1)

        unsafe_img = page.locator("#xss-trigger")
        safe_tag = page.locator("#safe-tag")

        # Debugging: Print counts
        print(f"Unsafe Img Count: {unsafe_img.count()}")
        print(f"Safe Tag Count: {safe_tag.count()}")

        is_unsafe_present = unsafe_img.count() > 0
        is_safe_present = safe_tag.count() > 0

        if is_unsafe_present:
            print("FAIL: Unsafe <img ...> tag found in DOM (Vulnerability Persists).")
        else:
            print("PASS: Unsafe <img ...> tag NOT found in DOM (Secure).")

        if is_safe_present:
            print("PASS: Safe <b> tag preserved (Functionality OK).")
        else:
            print("FAIL: Safe <b> tag missing (Functionality Broken).")

        browser.close()

        if is_unsafe_present or not is_safe_present:
            sys.exit(1)
        else:
            sys.exit(0)

if __name__ == "__main__":
    test_xss_vulnerability()
