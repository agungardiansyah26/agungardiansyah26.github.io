from playwright.sync_api import sync_playwright

def verify_focus():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("file:///app/index.html")

        # Wait for nav links to be visible
        page.wait_for_selector(".nav-link")

        # Focus on the first nav link
        nav_link = page.locator(".nav-link").first
        nav_link.focus()

        # Take a screenshot of the focused element
        page.screenshot(path="verification/focus_nav_link.png")

        # Focus on the theme toggle button
        theme_toggle = page.locator("#theme-toggle")
        theme_toggle.focus()

        # Take a screenshot of the focused element
        page.screenshot(path="verification/focus_theme_toggle.png")

        # Focus on a primary button
        btn_primary = page.locator(".btn-primary").first
        btn_primary.focus()

        # Take a screenshot
        page.screenshot(path="verification/focus_btn_primary.png")

        browser.close()

if __name__ == "__main__":
    verify_focus()
