from playwright.sync_api import sync_playwright, expect
import os
import time

def test_nav_active_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()

        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"
        print(f"Loading: {file_path}")
        page.goto(file_path)

        # Helper function to check active link
        def check_active_link(expected_id):
            print(f"Checking active link for #{expected_id}...")
            # Wait a bit for intersection observer to trigger
            time.sleep(0.5)

            nav_links = page.locator(".nav-link")
            count = nav_links.count()

            for i in range(count):
                link = nav_links.nth(i)
                href = link.get_attribute("href")
                is_active = "active" in link.get_attribute("class")

                if href == f"#{expected_id}":
                    if not is_active:
                        print(f"FAIL: Link {href} should be active but is not.")
                        return False
                else:
                    if is_active:
                        print(f"FAIL: Link {href} should NOT be active but is.")
                        return False
            print(f"PASS: Only #{expected_id} is active.")
            return True

        # Initial state (might be hero or nothing depending on scroll)
        # Scroll to Projects
        print("Scrolling to #projects...")
        page.locator("#projects").scroll_into_view_if_needed()
        # Ensure we are well within the section
        page.evaluate("document.getElementById('projects').scrollIntoView()")

        if not check_active_link("projects"):
            exit(1)

        # Scroll to Contact
        print("Scrolling to #contact...")
        page.evaluate("document.getElementById('contact').scrollIntoView()")

        if not check_active_link("contact"):
            exit(1)

        # Scroll back to Teaching
        print("Scrolling to #teaching...")
        page.evaluate("document.getElementById('teaching').scrollIntoView()")

        if not check_active_link("teaching"):
            exit(1)

        print("Navigation active state verification successful!")
        browser.close()

if __name__ == "__main__":
    test_nav_active_state()
