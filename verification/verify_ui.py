from playwright.sync_api import sync_playwright
import os

def verify_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"
        page.goto(file_path)

        # Wait for translation to load
        page.wait_for_timeout(500)

        # Take a screenshot
        page.screenshot(path="verification/ui_after_fix.png")

        browser.close()

if __name__ == "__main__":
    verify_ui()
