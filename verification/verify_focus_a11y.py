from playwright.sync_api import sync_playwright
import os
import time

def test_focus_styles():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Use local server
        file_path = "http://localhost:8000/index.html"
        print(f"Loading: {file_path}")
        page.goto(file_path)

        # Helper to get computed style of active element
        def get_active_outline():
            return page.evaluate("""() => {
                const el = document.activeElement;
                const style = window.getComputedStyle(el);
                return {
                    style: style.outlineStyle,
                    width: style.outlineWidth,
                    color: style.outlineColor,
                    offset: style.outlineOffset,
                    tagName: el.tagName,
                    className: el.className
                };
            }""")

        print("Pressing Tab to navigate...")

        # Click to ensure window is focused
        page.mouse.click(0, 0)

        # 1. Skip Link
        page.keyboard.press("Tab")
        # print(f"1. {get_active_outline()}")

        # 2. First Nav Link (Projects)
        page.keyboard.press("Tab")
        time.sleep(0.5) # Wait for potential transition
        nav_outline = get_active_outline()
        print(f"2. {nav_outline}")

        # Check if nav outline matches expectations
        # Relaxed check: solid and width > 0
        if nav_outline['style'] == 'none' or nav_outline['width'] == '0px':
            print("FAIL: Nav Link outline mismatch (expected visible outline).")
        else:
            print("PASS: Nav Link outline matches.")
            page.screenshot(path="verification/nav_link_focus.png")
            print("Screenshot saved: verification/nav_link_focus.png")

        # Tab through remaining nav links (4 more)
        for _ in range(4):
            page.keyboard.press("Tab")

        # Lang ID (6)
        page.keyboard.press("Tab")
        # Lang EN (7)
        page.keyboard.press("Tab")
        # Theme Toggle (8)
        page.keyboard.press("Tab")

        # Hero Button (9) - View Projects (.btn-primary)
        page.keyboard.press("Tab")
        time.sleep(0.5)
        hero_outline = get_active_outline()
        print(f"9. Hero Button: {hero_outline}")

        if hero_outline['style'] == 'solid' and hero_outline['width'] != '0px':
            print("PASS: Hero Button outline matches.")
        else:
             print("FAIL: Hero Button outline mismatch.")

        browser.close()

if __name__ == "__main__":
    test_focus_styles()
