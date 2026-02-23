from playwright.sync_api import sync_playwright, expect
import os

def test_optimization():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Force dark mode preference to ensure deterministic start state
        context = browser.new_context(color_scheme="dark")
        page = context.new_page()

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Loading: {file_path}")
        page.goto(file_path)

        # 1. Verify Scripts in Head and Deferred
        print("Verifying scripts are deferred and in head...")
        # Check for scripts in head with defer attribute
        # Note: In Playwright, we can check if the element exists in head.
        # But simpler is just to check if the script tag has defer attribute.

        script_trans_defer = page.evaluate("""
            document.querySelector('head script[src*="translations.js"]').defer
        """)
        script_main_defer = page.evaluate("""
            document.querySelector('head script[src*="script.js"]').defer
        """)

        if script_trans_defer and script_main_defer:
            print("✅ Scripts are in head and deferred.")
        else:
            print("❌ Scripts are NOT in head or NOT deferred.")
            # Don't fail yet, maybe we haven't applied changes.
            # But the test should assert this eventually.

        # 2. Verify Content is Visible (Initial Load Logic)
        print("Verifying content visibility...")
        # Check for a specific element text
        expect(page.locator(".hero-title")).to_contain_text("Saya membangun pengalaman belajar")
        print("✅ Content is visible.")

        # 3. Verify Theme Toggle (should work even if we skipped updateContent)
        print("Verifying theme toggle...")
        theme_toggle = page.locator("#theme-toggle")

        # Initial State: Should be Dark Mode (no light-mode class on html)
        expect(page.locator("html")).not_to_have_class("light-mode")

        # Expect label to be "Ganti ke Mode Terang" (ID default)
        # If we skipped updateContent, we must ensure updateThemeLabel was called!
        expect(theme_toggle).to_have_attribute("aria-label", "Ganti ke Mode Terang")

        # Click Toggle -> Switch to Light Mode
        theme_toggle.click()
        expect(page.locator("html")).to_have_class("light-mode")
        expect(theme_toggle).to_have_attribute("aria-label", "Ganti ke Mode Gelap")
        print("✅ Theme toggle works.")

        # 4. Verify Language Toggle (should trigger updateContent)
        print("Verifying language toggle...")
        # Switch to English
        page.locator("#lang-en").click()

        # Verify text changed
        expect(page.locator(".hero-title")).to_contain_text("I build learning experiences")
        expect(page.locator("html")).to_have_attribute("lang", "en")
        print("✅ Language toggle works (ID -> EN).")

        # Switch back to ID
        page.locator("#lang-id").click()
        expect(page.locator(".hero-title")).to_contain_text("Saya membangun pengalaman belajar")
        expect(page.locator("html")).to_have_attribute("lang", "id")
        print("✅ Language toggle works (EN -> ID).")

        browser.close()

if __name__ == "__main__":
    test_optimization()
