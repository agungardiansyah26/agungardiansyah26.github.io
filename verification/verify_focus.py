import time
from playwright.sync_api import sync_playwright

def verify_focus_visible():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the local HTML file
        page.goto("file:///app/index.html")

        # Wait for fonts and styles to load
        page.wait_for_load_state("networkidle")

        # Focus on the 'ID' language toggle button
        lang_id_btn = page.locator("#lang-id")
        lang_id_btn.focus()

        # Take a screenshot to verify the focus outline
        page.screenshot(path="verification/focus_visible.png")

        # Focus on the back-to-top button
        # First we need to make it visible by scrolling
        page.evaluate("window.scrollTo(0, 1000)")

        # Wait for the button to become visible (it has a transition)
        page.wait_for_timeout(500)

        back_to_top_btn = page.locator("#back-to-top")
        back_to_top_btn.focus()

        # Take another screenshot
        page.screenshot(path="verification/focus_visible_back_to_top.png")

        browser.close()
        print("Screenshots taken successfully.")

if __name__ == "__main__":
    verify_focus_visible()
