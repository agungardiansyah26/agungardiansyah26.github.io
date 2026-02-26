from playwright.sync_api import sync_playwright, expect
import os
import time

def test_nav_highlight():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Using a context can sometimes help isolate state
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Loading: {file_path}")
        page.goto(file_path)

        # Modify content to ensure clean intersection testing
        # Make each section tall and spaced out so only one intersects at a time
        print("Injecting styles to isolate sections...")
        page.evaluate("""
            const style = document.createElement('style');
            style.textContent = `
                section {
                    min-height: 100vh !important;
                    margin-bottom: 50vh !important;
                    border: 5px solid red; /* Visual debugging if headless=false */
                }
            `;
            document.head.appendChild(style);
        """)

        # Wait for layout update
        page.wait_for_timeout(500)

        # Helper to check active link
        def check_active_link(expected_href):
            nav_links = page.locator(".nav-link")
            count = nav_links.count()

            # Helper to print current active links
            def print_active():
                active_links = []
                for i in range(count):
                    link = nav_links.nth(i)
                    if "active" in link.get_attribute("class"):
                        active_links.append(link.get_attribute("href"))
                print(f"Current active links: {active_links}")

            # Wait for the expected link to become active
            target_link = page.locator(f".nav-link[href='{expected_href}']")
            try:
                expect(target_link).to_have_class("nav-link active", timeout=3000)
            except AssertionError:
                print(f"WARNING: Expected link {expected_href} did not become active within timeout.")
                print_active()

            # Then verify others are NOT active
            for i in range(count):
                link = nav_links.nth(i)
                href = link.get_attribute("href")

                if href == expected_href:
                    expect(link).to_have_class("nav-link active")
                else:
                    expect(link).not_to_have_class("nav-link active")

            # Take screenshot
            safe_href = expected_href.replace("#", "")
            page.screenshot(path=f"verification/nav_{safe_href}.png")
            print(f"Screenshot saved to verification/nav_{safe_href}.png")

        # Scroll to center to ensure good visibility
        def scroll_to(id_name):
            print(f"Scrolling to #{id_name}...")
            # Use smooth scrolling to trigger observer updates naturally
            page.evaluate(f"document.getElementById('{id_name}').scrollIntoView({{block: 'center'}})")
            # Wait for observer to fire
            page.wait_for_timeout(500)

        scroll_to("projects")
        check_active_link("#projects")

        scroll_to("games")
        check_active_link("#games")

        scroll_to("teaching")
        check_active_link("#teaching")

        scroll_to("about")
        check_active_link("#about")

        scroll_to("contact")
        check_active_link("#contact")

        print("All navigation checks passed.")
        browser.close()

if __name__ == "__main__":
    test_nav_highlight()
