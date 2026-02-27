from playwright.sync_api import sync_playwright
import os

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    # Set color scheme to dark to ensure consistency with existing tests or defaults
    context = browser.new_context(color_scheme='dark')
    page = context.new_page()

    # Load the local index.html file
    # Assuming the script is run from the root of the repo or we can use absolute path
    # verification/ is inside the repo.
    # We will use file:// URI.
    # Since we are running from repo root (as per instructions), we can resolve the path.

    file_path = os.path.abspath("index.html")
    page.goto(f"file://{file_path}")

    # Scroll to the contact section
    contact_section = page.locator("#contact")
    contact_section.scroll_into_view_if_needed()

    # Wait a bit for any transitions or lazy loading (though this page seems static/fast)
    page.wait_for_timeout(1000)

    # Take a screenshot of the contact form area
    # We target the .contact-container or just the form
    form_area = page.locator(".contact-container")
    if form_area.is_visible():
        form_area.screenshot(path="verification/contact_form_ux.png")
        print("Screenshot saved to verification/contact_form_ux.png")
    else:
        print("Contact form container not found or not visible.")
        page.screenshot(path="verification/full_page_debug.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
