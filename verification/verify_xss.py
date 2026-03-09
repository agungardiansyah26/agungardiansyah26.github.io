from playwright.sync_api import sync_playwright, expect
import os
import sys

def test_xss():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Capture console messages to detect alert execution
        console_messages = []
        page.on("console", lambda msg: console_messages.append(msg.text))

        # Handle alert dialog to prevent hanging and detect execution
        dialog_messages = []
        page.on("dialog", lambda dialog: (dialog_messages.append(dialog.message), dialog.dismiss()))

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Loading: {file_path}")
        page.goto(file_path)

        # Inject XSS payload into translation
        print("Injecting XSS payload into translation...")
        page.evaluate('''
            translations['id']['hero']['title'] = 'Testing XSS <img src=x onerror=alert("XSS_EXECUTED")>';
        ''')

        # Trigger updateContent
        print("Triggering updateContent...")
        page.evaluate('''
            updateContent('id');
        ''')

        # Wait a moment to ensure any async execution or rendering completes
        page.wait_for_timeout(1000)

        # Check if alert was executed
        if "XSS_EXECUTED" in dialog_messages:
            print("FAIL: XSS payload was executed via alert()!")
            print(f"Dialog messages: {dialog_messages}")
            sys.exit(1)
        else:
            print("PASS: No XSS alert detected.")

        # Check innerHTML to verify the payload was sanitized
        title_html = page.evaluate("document.querySelector('.hero-title').innerHTML")
        print(f"Sanitized HTML: {title_html}")

        # We expect the img tag to be removed, leaving only its text content if any or just the clean string
        if "<img" in title_html.lower() or "onerror" in title_html.lower():
             print("FAIL: XSS payload not fully sanitized!")
             sys.exit(1)
        else:
             print("PASS: XSS payload sanitized successfully in DOM.")

        page.screenshot(path="verification/xss_verification.png")

        browser.close()
        sys.exit(0)

if __name__ == "__main__":
    test_xss()