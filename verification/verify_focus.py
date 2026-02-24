from playwright.sync_api import sync_playwright
import os

def test_focus_styles():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use dark mode to verify variable usage
        context = browser.new_context(color_scheme="dark")
        page = context.new_page()

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Loading: {file_path}")
        page.goto(file_path)

        def check_outline(selector, name):
            locator = page.locator(selector).first
            locator.focus()
            # Wait a bit for transition
            page.wait_for_timeout(200)

            # evaluate returns the computed style property value
            outline_width = locator.evaluate("el => getComputedStyle(el).outlineWidth")
            outline_style = locator.evaluate("el => getComputedStyle(el).outlineStyle")
            outline_offset = locator.evaluate("el => getComputedStyle(el).outlineOffset")
            outline_color = locator.evaluate("el => getComputedStyle(el).outlineColor")

            print(f"[{name}] Outline: {outline_width} {outline_style} {outline_color}, Offset: {outline_offset}")

            # Check for our specific custom focus style:
            # width: 2px
            # style: solid
            # offset: 2px

            is_custom = True
            if "2px" not in outline_width: is_custom = False
            if "solid" not in outline_style: is_custom = False
            if "2px" not in outline_offset: is_custom = False

            if is_custom:
                print(f"✅ {name} has CUSTOM focus outline.")
                return True
            else:
                print(f"❌ {name} MISSING CUSTOM focus outline.")
                return False

        results = []
        # Check Nav Link first and screenshot it
        results.append(check_outline(".nav-link", "Nav Link"))

        # Take a screenshot of the focused Nav Link
        screenshot_path = "verification/focus_style.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        results.append(check_outline(".btn-primary", "Primary Button"))
        results.append(check_outline(".btn-ghost", "Ghost Button"))
        results.append(check_outline(".project-link", "Project Link"))
        results.append(check_outline(".footer-link", "Footer Link"))

        browser.close()

if __name__ == "__main__":
    test_focus_styles()
