from playwright.sync_api import sync_playwright

def test_security_fix():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://localhost:8001/index.html')

        # Inject malicious HTML to simulate attack on translation data
        page.evaluate("""
            const t = translations['en'];
            t['hero']['title'] = 'Hacked! <img src="x" onerror="window.hacked=true" /> <a href="javascript:alert(1)">Click Me</a>';
            updateContent('en');
        """)

        # Give it a moment to render
        page.wait_for_timeout(1000)

        hacked = page.evaluate('window.hacked')
        if hacked:
            print("XSS SUCCESSFUL - FIX FAILED")
        else:
            print("XSS BLOCKED - FIX SUCCESSFUL")

        print("Hero title content:", page.locator('.hero-title').inner_html())

        page.screenshot(path="verification/security_fix.png")
        browser.close()

if __name__ == '__main__':
    test_security_fix()
