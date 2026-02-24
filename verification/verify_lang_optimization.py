from playwright.sync_api import sync_playwright, expect
import os

def test_lang_optimization():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # Test Case 1: Default Load (No localStorage) -> Should be ID
        print("Test 1: Default Load (No localStorage)")
        context = browser.new_context()
        page = context.new_page()

        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"
        page.goto(file_path)

        # Verify ID content matches index.html static content
        expect(page.locator("html")).to_have_attribute("lang", "id")
        expect(page.locator("#lang-id")).to_have_class("lang-option active-lang")
        expect(page.locator("[data-i18n='hero.title']")).to_contain_text("Saya membangun pengalaman belajar")

        # Verify theme label (should be localized to ID)
        # Depending on system preference, it could be light or dark.
        # But verify it has A label.
        expect(page.locator("#theme-toggle")).not_to_have_attribute("aria-label", "Toggle theme") # Should be translated

        context.close()

        # Test Case 2: localStorage = 'en'
        print("\nTest 2: localStorage = 'en'")
        context = browser.new_context()
        # Set localStorage
        context.add_init_script("localStorage.setItem('lang', 'en');")
        page = context.new_page()

        page.goto(file_path)

        # Verify EN content
        expect(page.locator("html")).to_have_attribute("lang", "en")
        expect(page.locator("#lang-en")).to_have_class("lang-option active-lang")
        expect(page.locator("[data-i18n='hero.title']")).to_contain_text("I build learning experiences")

        context.close()

        # Test Case 3: Switch Language manually
        print("\nTest 3: Switch Language manually")
        context = browser.new_context()
        page = context.new_page()
        page.goto(file_path)

        # Click EN
        page.locator("#lang-en").click()
        expect(page.locator("[data-i18n='hero.title']")).to_contain_text("I build learning experiences")

        # Click ID
        page.locator("#lang-id").click()
        expect(page.locator("[data-i18n='hero.title']")).to_contain_text("Saya membangun pengalaman belajar")

        context.close()

        browser.close()

if __name__ == "__main__":
    test_lang_optimization()
