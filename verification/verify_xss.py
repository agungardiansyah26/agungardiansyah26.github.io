from playwright.sync_api import sync_playwright
import os

def test_xss_protection():
    html_file_path = f"file://{os.path.abspath('index.html')}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        alert_called = False
        def handle_dialog(dialog):
            nonlocal alert_called
            print(f"Dialog caught: {dialog.message}")
            alert_called = True
            dialog.dismiss()
        page.on("dialog", handle_dialog)

        # Go to the page first
        page.goto(html_file_path)

        # Inject payload by changing the translation and triggering updateContent
        page.evaluate("""
            translations['id']['hero']['title'] = 'Payload <script>alert("XSS")</script><img src="x" onerror="alert(\\'XSS\\')"><a href="javascript:alert(\\'XSS\\')">Link</a><a href="jav&#x09;ascript:alert(\\'XSS\\')">Link2</a><span class="safe">Safe</span>';
            updateContent('id');
        """)

        # Wait to see if alert triggers
        page.wait_for_timeout(1000)

        # Check DOM contents
        title_html = page.locator('h1.hero-title').inner_html()
        print(f"Sanitized Title HTML: {title_html}")

        assert "Payload" in title_html
        assert "<script>" not in title_html
        assert "onerror" not in title_html
        assert "javascript:" not in title_html
        assert "class=\"safe\"" in title_html or "class=\"safe\"" in title_html.replace("'", '"')

        # Click the bypass link to trigger the alert
        try:
            page.click("a:has-text('Link2')")
        except Exception as e:
            pass

        page.wait_for_timeout(1000)

        if alert_called:
            print("FAILED: XSS alert was executed!")
            exit(1)

        print("SUCCESS: XSS test passed, malicious HTML is sanitized properly.")

        browser.close()

if __name__ == "__main__":
    test_xss_protection()
