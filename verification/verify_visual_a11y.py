from playwright.sync_api import sync_playwright
import os

def test_visual_a11y():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Loading: {file_path}")
        page.goto(file_path)

        # Locator for buttons
        lang_id = page.locator("#lang-id")
        lang_en = page.locator("#lang-en")

        # Focus ID button and take screenshot
        lang_id.focus()
        page.screenshot(path="verification/focus_id.png")
        print("Screenshot saved: verification/focus_id.png")

        # Focus EN button and take screenshot
        lang_en.focus()
        page.screenshot(path="verification/focus_en.png")
        print("Screenshot saved: verification/focus_en.png")

        browser.close()

if __name__ == "__main__":
    test_visual_a11y()
