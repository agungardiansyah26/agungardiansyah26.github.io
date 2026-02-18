from playwright.sync_api import sync_playwright
import os

def test_a11y():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Loading: {file_path}")
        page.goto(file_path)

        # Locator for buttons
        lang_id = page.locator("#lang-id")
        lang_en = page.locator("#lang-en")

        # 1. Verify they are buttons
        print("Verifying elements are buttons...")
        assert lang_id.evaluate("el => el.tagName") == "BUTTON", "ID toggle is not a button"
        assert lang_en.evaluate("el => el.tagName") == "BUTTON", "EN toggle is not a button"

        # 2. Verify aria-labels
        print("Verifying aria-labels...")
        assert lang_id.get_attribute("aria-label") == "Switch to Indonesian"
        assert lang_en.get_attribute("aria-label") == "Switch to English"

        # 3. Verify initial state (ID active)
        print("Verifying initial state...")
        assert lang_id.get_attribute("aria-pressed") == "true"
        assert lang_en.get_attribute("aria-pressed") == "false"

        # 4. Switch to English and verify state update
        print("Switching to English...")
        lang_en.click()
        assert lang_id.get_attribute("aria-pressed") == "false"
        assert lang_en.get_attribute("aria-pressed") == "true"

        # 5. Switch back to ID and verify state update
        print("Switching back to Indonesian...")
        lang_id.click()
        assert lang_id.get_attribute("aria-pressed") == "true"
        assert lang_en.get_attribute("aria-pressed") == "false"

        # 6. Verify focusability (Tab key)
        print("Verifying focusability...")
        # Reload to reset focus
        page.reload()

        # Focus explicitly to test styles/accessibility properties first
        lang_id.focus()
        focused_id = page.evaluate("document.activeElement.id")
        assert focused_id == "lang-id"

        # Tab to next element (divider is span, so next should be EN button)
        page.keyboard.press("Tab")
        focused_id = page.evaluate("document.activeElement.id")
        assert focused_id == "lang-en"

        print("Accessibility verification successful!")
        browser.close()

if __name__ == "__main__":
    test_a11y()
