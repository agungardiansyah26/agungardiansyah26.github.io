from playwright.sync_api import sync_playwright
import os

def test_xss_sanitization():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Loading: {file_path}")
        page.goto(file_path)

        # Inject malicious payload: A link with javascript: URI
        print("Injecting malicious payload (javascript: link)...")
        # We inject it into a translation key that is rendered
        page.evaluate("""
            const currentLang = localStorage.getItem('lang') || 'id';
            translations[currentLang].hero.title = 'Hacked <a href="javascript:window.xss=true" id="hack-link">Click Me</a>';
        """)

        # Trigger updateContent by toggling language
        current_lang = page.evaluate("localStorage.getItem('lang') || 'id'")
        if current_lang == 'id':
            page.click('#lang-en')
            page.click('#lang-id')
        else:
            page.click('#lang-id')
            page.click('#lang-en')

        # Check if the malicious element exists in the DOM
        # Before sanitization: It should exist.
        # After sanitization: It should NOT exist (or be converted to text).

        try:
            # We expect the element to be present if vulnerability (or lack of sanitization) exists
            page.wait_for_selector('#hack-link', timeout=2000)
            print("FAIL: Malicious element found in DOM! Sanitization missing.")
            return True # Vulnerable / Not sanitized
        except:
            print("PASS: Malicious element NOT found in DOM. Sanitization working.")
            return False # Secure / Sanitized

if __name__ == "__main__":
    vulnerable = test_xss_sanitization()
    if vulnerable:
        exit(1)
    else:
        exit(0)
