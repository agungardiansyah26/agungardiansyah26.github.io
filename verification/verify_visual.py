from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Force dark mode for consistency
        context = browser.new_context(color_scheme="dark", viewport={"width": 1280, "height": 800})
        page = context.new_page()

        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # Take screenshot of Hero section
        page.locator(".hero").screenshot(path="verification/hero.png")

        # Scroll to projects and take screenshot
        page.locator("#projects").scroll_into_view_if_needed()
        page.locator("#projects").screenshot(path="verification/projects.png")

        # Toggle language and screenshot header
        page.locator("#lang-en").click()
        page.locator("header").screenshot(path="verification/header_en.png")

        browser.close()

if __name__ == "__main__":
    run()
