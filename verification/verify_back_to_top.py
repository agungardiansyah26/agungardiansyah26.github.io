from playwright.sync_api import sync_playwright
import os
import time

def test_back_to_top():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Loading: {file_path}")
        page.goto(file_path)

        # Locator for back to top button
        btn = page.locator("#back-to-top")

        # 1. Verify existence
        print("Verifying back-to-top button exists...")
        if btn.count() == 0:
            print("Button not found!")
            exit(1)

        # 2. Verify initially hidden
        print("Verifying button is initially hidden...")
        opacity = btn.evaluate("el => getComputedStyle(el).opacity")
        # Allow some float precision issues or initial render states, but should be 0
        assert float(opacity) < 0.1, f"Expected opacity ~0, got {opacity}"

        # 3. Scroll down to trigger visibility
        print("Scrolling down...")
        page.evaluate("window.scrollTo(0, 500)")
        time.sleep(1.5) # Wait for scroll event and transition (increased wait)

        # Verify visible
        print("Verifying button becomes visible...")
        opacity = btn.evaluate("el => getComputedStyle(el).opacity")
        assert float(opacity) > 0.9, f"Expected opacity ~1 after scroll, got {opacity}"

        # 4. Click to scroll up
        print("Clicking button...")
        btn.click()

        # Wait for scroll animation
        time.sleep(1.5)

        # 5. Verify scroll position is back to top
        print("Verifying scroll position...")
        scroll_y = page.evaluate("window.scrollY")
        assert scroll_y < 10, f"Expected scrollY close to 0, got {scroll_y}"

        print("Back to Top verification successful!")
        browser.close()

if __name__ == "__main__":
    test_back_to_top()
