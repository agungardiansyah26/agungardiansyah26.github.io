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
