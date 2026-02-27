from playwright.sync_api import sync_playwright, expect
import os

def test_theme_toggle():
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

        theme_toggle = page.locator("#theme-toggle")

        # Initial State: Should be Dark Mode (no light-mode class on html)
        # Because we forced color_scheme="dark", the init script should NOT add light-mode.

        print("Verifying initial state (Dark Mode, ID)...")
        expect(page.locator("html")).not_to_have_class("light-mode")

        # Expect label to be "Ganti ke Mode Terang" (Switch to Light Mode)
        # Note: Depending on the initial load state and localStorage, it might start as Light Mode if system pref is light.
        # But we forced color_scheme="dark".
        # However, the JS checks localStorage first. If "light" is stored from previous run, it might be light.
        # Ideally, we should clear localStorage or handle both cases.
        # But since we are launching a fresh browser context, localStorage should be empty.
        # BUT, the initial JS execution might have race conditions or default behavior.
        # Let's inspect the actual state if it fails.

        # Based on previous failure: Actual value: Toggle theme.
        # This means updateThemeLabel() might not have run or translations weren't ready?
        # Or it defaults to "Toggle theme" in HTML and JS didn't update it yet.
        # We should wait for the update.

        # Wait for the label to NOT be the default "Toggle theme"
        expect(theme_toggle).not_to_have_attribute("aria-label", "Toggle theme", timeout=10000)

        expect(theme_toggle).to_have_attribute("aria-label", "Ganti ke Mode Terang")
        expect(theme_toggle).to_have_attribute("title", "Ganti ke Mode Terang")
        print("Initial state verified.")

        # Click Toggle -> Switch to Light Mode
        print("Clicking theme toggle...")
        theme_toggle.click()

        print("Verifying Light Mode state (Light Mode, ID)...")
        expect(page.locator("html")).to_have_class("light-mode")
        # Expect label to be "Ganti ke Mode Gelap" (Switch to Dark Mode)
        expect(theme_toggle).to_have_attribute("aria-label", "Ganti ke Mode Gelap")
        expect(theme_toggle).to_have_attribute("title", "Ganti ke Mode Gelap")
        print("Light Mode state verified.")

        # Switch Language to English
        print("Switching language to EN...")
        page.locator("#lang-en").click()

        print("Verifying EN state (Light Mode, EN)...")
        expect(page.locator("html")).to_have_attribute("lang", "en")
        # Expect label to be "Switch to Dark Mode"
        expect(theme_toggle).to_have_attribute("aria-label", "Switch to Dark Mode")
        expect(theme_toggle).to_have_attribute("title", "Switch to Dark Mode")
        print("EN state verified.")

        # Click Toggle -> Switch to Dark Mode (EN)
        print("Clicking theme toggle (in EN)...")
        theme_toggle.click()

        print("Verifying Dark Mode state (Dark Mode, EN)...")
        expect(page.locator("html")).not_to_have_class("light-mode")
        # Expect label to be "Switch to Light Mode"
        expect(theme_toggle).to_have_attribute("aria-label", "Switch to Light Mode")
        expect(theme_toggle).to_have_attribute("title", "Switch to Light Mode")
        print("Dark Mode state (EN) verified.")

        browser.close()

if __name__ == "__main__":
    test_theme_toggle()
