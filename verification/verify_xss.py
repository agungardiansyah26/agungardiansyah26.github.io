from playwright.sync_api import sync_playwright
import os
import sys

def test_xss_prevention():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"
        page.goto(file_path)

        # Inject malicious translation
        malicious_html = 'Safe Text <img src=x onerror="window.xss_triggered=true" class="malicious"> <span class="hero-highlight">Highlight</span>'

        print("Injecting malicious translation...")
        page.evaluate(f"""
            translations['id']['hero']['title'] = '{malicious_html}';
            updateContent('id');
        """)

        # Allow some time for potential execution
        page.wait_for_timeout(1000)

        # Check for malicious tag
        img_count = page.locator('img.malicious').count()
        print(f"Malicious img count: {img_count}")

        # Check for execution
        xss_triggered = page.evaluate("window.xss_triggered === true")
        print(f"XSS Triggered: {xss_triggered}")

        if img_count > 0 or xss_triggered:
            print("FAIL: XSS Vulnerability detected!")
            sys.exit(1)
        else:
            print("PASS: Malicious HTML was sanitized.")

        browser.close()

if __name__ == "__main__":
    test_xss_prevention()
