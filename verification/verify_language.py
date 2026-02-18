from playwright.sync_api import sync_playwright
import os

def test_language_toggle():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Loading: {file_path}")
        page.goto(file_path)

        # 1. Verify default language (Indonesian)
        # Check Hero Title
        hero_title = page.locator(".hero-title")
        print("Checking default language...")
        content_id = hero_title.inner_text()
        print(f"Content ID: {content_id}")
        assert "Saya membangun pengalaman belajar" in content_id

        # Check active toggle
        lang_id = page.locator("#lang-id")
        lang_en = page.locator("#lang-en")

        assert "active-lang" in lang_id.get_attribute("class")
        assert "active-lang" not in lang_en.get_attribute("class")

        # Take screenshot of ID version
        page.screenshot(path="verification/1_default_id.png")
        print("Screenshot saved: verification/1_default_id.png")

        # 2. Switch to English
        print("Switching to English...")
        lang_en.click()

        # Verify content changed
        content_en = hero_title.inner_text()
        print(f"Content EN: {content_en}")
        assert "I build learning experiences" in content_en

        # Verify active toggle
        assert "active-lang" not in lang_id.get_attribute("class")
        assert "active-lang" in lang_en.get_attribute("class")

        # Take screenshot of EN version
        page.screenshot(path="verification/2_switched_en.png")
        print("Screenshot saved: verification/2_switched_en.png")

        # 3. Reload and verify persistence
        print("Reloading page...")
        page.reload()

        content_reloaded = hero_title.inner_text()
        print(f"Content Reloaded: {content_reloaded}")
        assert "I build learning experiences" in content_reloaded

        # Verify active toggle
        lang_en_reloaded = page.locator("#lang-en")
        assert "active-lang" in lang_en_reloaded.get_attribute("class")

        print("Verification successful!")
        browser.close()

if __name__ == "__main__":
    test_language_toggle()
