import time
from playwright.sync_api import sync_playwright

def test_nav_highlighting():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})

        print("Loading: file:///app/index.html")
        page.goto("file:///app/index.html")

        # Wait for initial load
        page.wait_for_timeout(1000)

        # Check initial active link (should be #projects or none depending on scroll)

        # Scroll to #projects
        print("Scrolling to #projects")
        page.locator("#projects").scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        projects_link = page.locator(".nav-link[href='#projects']")
        print(f"Projects link classes: {projects_link.get_attribute('class')}")
        assert "active" in projects_link.get_attribute("class")

        # Take a screenshot
        page.screenshot(path="verification/nav_projects.png")

        # Scroll to #about
        print("Scrolling to #about")
        page.locator("#about").scroll_into_view_if_needed()
        page.wait_for_timeout(1000)
        about_link = page.locator(".nav-link[href='#about']")
        print(f"About link classes: {about_link.get_attribute('class')}")
        assert "active" in about_link.get_attribute("class")

        # Check that projects is no longer active
        print(f"Projects link classes after scroll: {projects_link.get_attribute('class')}")
        assert "active" not in projects_link.get_attribute("class")

        # Take a screenshot
        page.screenshot(path="verification/nav_about.png")

        print("Nav highlighting verification successful!")
        browser.close()

if __name__ == "__main__":
    test_nav_highlighting()
