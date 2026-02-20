from playwright.sync_api import sync_playwright
import os

def test_skip_link():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Loading: {file_path}")
        page.goto(file_path)

        # Locator for skip link
        skip_link = page.locator(".skip-link")

        # 1. Verify existence
        print("Verifying skip link exists...")
        assert skip_link.count() > 0, "Skip link element not found"

        # 2. Verify initially hidden (off-screen)
        print("Verifying skip link is initially hidden...")
        box = skip_link.bounding_box()
        # If box is None, it's not visible at all. If it exists, check position.
        if box:
            assert box['y'] < 0, f"Skip link should be off-screen (y < 0), but found at y={box['y']}"
        else:
             # Depending on CSS, it might be hidden differently, but let's assume top: -Xpx
             # If bounding_box is None, playwright considers it not visible.
             pass

        # 3. Verify focus makes it visible
        print("Verifying skip link becomes visible on focus...")
        # Since it's the first link, one Tab should focus it.
        # But wait, does the browser focus the body first?
        # Usually, first interactive element.
        page.keyboard.press("Tab")

        # Check active element
        active_id = page.evaluate("document.activeElement.className")
        # Might contain multiple classes
        assert "skip-link" in active_id, f"Expected active element to be skip-link, but got class: {active_id}"

        # Check visibility
        # Wait for transition
        page.wait_for_timeout(500)
        box = skip_link.bounding_box()
        assert box is not None, "Skip link should have a bounding box when focused"
        assert box['y'] >= 0, f"Skip link should be on-screen (y >= 0), but found at y={box['y']}"

        # 4. Verify functionality (moves focus/scroll to main content)
        print("Verifying functionality...")
        page.keyboard.press("Enter")

        # Check URL hash
        # Wait a bit for navigation/scroll
        page.wait_for_timeout(500)
        assert "#main-content" in page.url, f"URL should contain #main-content, got {page.url}"

        # Check scroll position
        # main-content should be at the top (modulo scroll-margin-top)
        # Actually, if we have smooth scroll, it might take time.
        # We can just check if the main content is in view.
        main_content = page.locator("#main-content")
        assert main_content.is_visible(), "Main content should be visible"

        print("Skip link verification successful!")
        browser.close()

if __name__ == "__main__":
    test_skip_link()
