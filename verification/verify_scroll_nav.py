from playwright.sync_api import sync_playwright

def test_scroll_nav():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the local index.html
        page.goto("file:///app/index.html")

        # Scroll down slowly to trigger intersection observers
        page.evaluate("window.scrollTo(0, document.body.scrollHeight / 4)")
        page.wait_for_timeout(500)
        page.evaluate("window.scrollTo(0, document.body.scrollHeight / 2)")
        page.wait_for_timeout(500)

        # Check active link
        active_links = page.locator(".nav-link.active").count()
        print(f"Number of active links: {active_links}")

        if active_links > 0:
            active_text = page.locator(".nav-link.active").first.text_content()
            print(f"Active link text: {active_text}")

        page.screenshot(path="/app/verification/scroll_nav.png")
        print("Screenshot saved to /app/verification/scroll_nav.png")

        browser.close()

if __name__ == "__main__":
    test_scroll_nav()
