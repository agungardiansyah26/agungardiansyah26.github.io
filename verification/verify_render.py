from playwright.sync_api import sync_playwright
import os

def test_hero_html_rendering():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"
        print(f"Loading: {file_path}")
        page.goto(file_path)

        # Check if hero title contains the span with class hero-highlight
        # The translation is: "Saya membangun pengalaman belajar dan proyek teknis<br /><span class=\"hero-highlight\">dengan Python, web, game, dan elektronika.</span>"

        # We can check innerHTML of the h1
        hero_title = page.locator(".hero-title")
        inner_html = hero_title.inner_html()

        print(f"Hero Title HTML: {inner_html}")

        # Normalize whitespace for comparison if needed, but simple check is enough
        if '<span class="hero-highlight">' in inner_html or "<span class=\"hero-highlight\">" in inner_html:
            print("PASS: Hero title contains expected span class.")
        else:
            print("FAIL: Hero title missing expected span class!")
            return False

        # Also check if <br> is present (allowed tag)
        if '<br>' in inner_html or '<br />' in inner_html:
            print("PASS: Hero title contains expected <br>.")
        else:
            print("FAIL: Hero title missing expected <br>!")
            return False

        return True

if __name__ == "__main__":
    if test_hero_html_rendering():
        exit(0)
    else:
        exit(1)
