from playwright.sync_api import sync_playwright
import os

def test_skip_link():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Loading: {file_path}")
        page.goto(file_path)

        # Locator for skip link
        skip_link = page.locator(".skip-link")

        # 1. Verify skip link exists and is initially off-screen
        print("Verifying skip link existence and initial state...")
        assert skip_link.count() == 1, "Skip link not found"

        # Check if it is positioned off-screen (top < 0)
        # We need to wait for styles to apply
        page.wait_for_selector(".skip-link")
        box = skip_link.bounding_box()
        # Note: box.y might be negative or 0 depending on implementation details and viewport.
        # But we know CSS sets top: -100px.
        # Let's check computed style instead for robustness.
        top_value = skip_link.evaluate("el => getComputedStyle(el).top")
        print(f"Skip link top value: {top_value}")
        assert top_value == "-100px", f"Expected top: -100px, got {top_value}"

        # 2. Verify focus interaction
        print("Verifying focus interaction...")
        # Press Tab to focus the first element (should be skip link)
        page.keyboard.press("Tab")

        focused_class = page.evaluate("document.activeElement.className")
        print(f"Focused element class: {focused_class}")
        assert "skip-link" in focused_class, "Skip link did not receive focus on first tab"

        # Verify it becomes visible (top: 0)
        # Wait a bit for transition? Computed style should reflect the focus rule if applied.
        # However, transitions take time. We can check if the rule applies.
        # Let's check if the element is effectively visible in the viewport now.
        # Playwright's bounding box should now be within the viewport.

        # We can also check the computed style again, but since there is a transition, it might vary.
        # But verify focus style application:
        # We added .skip-link:focus { top: 0; }
        # Let's verify that the element is now intersecting the viewport.

        # Simply check if it is "visible" to the user now.
        # Since it was off-screen, is_visible might have been false (depending on how playwright defines it).
        # But let's check the computed top value again.
        # Note: transitions happen over time. We might need to wait.
        page.wait_for_timeout(400) # Wait for 0.3s transition

        current_top = skip_link.evaluate("el => getComputedStyle(el).top")
        print(f"Skip link top value after focus: {current_top}")
        assert current_top == "0px", f"Expected top: 0px, got {current_top}"

        # 3. Verify text content (Translation check)
        print("Verifying text content...")
        text = skip_link.inner_text()
        print(f"Skip link text: {text}")
        assert text == "Lanjut ke konten utama", f"Expected ID text, got {text}"

        # 4. Verify functionality (Skip to main)
        print("Verifying skip functionality...")
        page.keyboard.press("Enter")

        # Check if URL updated
        assert page.url.endswith("#main-content"), f"URL did not update to #main-content, got {page.url}"

        # Check if main content is the target
        # Verify that the next tab focuses something inside main or that main is the active element (if it has tabindex)
        # Default behavior: hash navigation scrolls to element. Focus might not shift unless tabindex=-1 is set on target and we call focus().
        # But simpler check: the URL hash change confirms the link works.

        print("Skip link verification successful!")
        browser.close()

if __name__ == "__main__":
    test_skip_link()
