from playwright.sync_api import sync_playwright, expect
import os
import time

def test_focus_styles():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"
        page.goto(file_path)

        # 1. Check a nav link
        nav_link = page.locator(".nav-link").first
        nav_link.focus()
        page.wait_for_timeout(300)

        # Get computed style
        outline_width = nav_link.evaluate("el => window.getComputedStyle(el).outlineWidth")
        outline_style = nav_link.evaluate("el => window.getComputedStyle(el).outlineStyle")
        outline_offset = nav_link.evaluate("el => window.getComputedStyle(el).outlineOffset")

        print(f"Nav Link Focus: {outline_width} {outline_style} {outline_offset}")

        # Assertions
        assert outline_width == "2px", f"Expected 2px, got {outline_width}"
        assert outline_style == "solid", f"Expected solid, got {outline_style}"
        assert outline_offset == "2px", f"Expected 2px, got {outline_offset}"

        # 2. Check a project link
        project_link = page.locator(".project-link").first
        project_link.focus()
        page.wait_for_timeout(300)

        outline_width_proj = project_link.evaluate("el => window.getComputedStyle(el).outlineWidth")
        print(f"Project Link Focus: {outline_width_proj}")

        assert outline_width_proj == "2px", f"Expected 2px, got {outline_width_proj}"

        # 3. Check Input Field (should NOT have outline, but custom styles)
        input_field = page.locator("#name")
        input_field.focus()
        page.wait_for_timeout(300)

        input_outline_style = input_field.evaluate("el => window.getComputedStyle(el).outlineStyle")
        print(f"Input Field Outline Style: {input_outline_style}")

        # It should be none because .input-field:focus sets outline: none
        assert input_outline_style == "none" or input_outline_style == "0px", \
            f"Expected none/0px, got {input_outline_style}"

        print("Focus styles verified successfully!")
        browser.close()

if __name__ == "__main__":
    test_focus_styles()
