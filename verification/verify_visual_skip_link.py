from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Set viewport size to ensure good screenshot
        page.set_viewport_size({"width": 1280, "height": 720})

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Loading: {file_path}")
        page.goto(file_path)

        # Focus the skip link
        page.keyboard.press("Tab")

        # Wait for transition
        page.wait_for_timeout(500)

        # Take screenshot
        screenshot_path = "verification/skip_link_visible.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    run()
