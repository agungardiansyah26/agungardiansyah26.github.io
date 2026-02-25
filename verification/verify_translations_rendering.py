from playwright.sync_api import sync_playwright
import os
import sys

def test_html_preserved():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"
        page.goto(file_path)

        # Check Hero Title for span.hero-highlight
        print("Checking Hero Title structure...")
        hero_title = page.locator(".hero-title")
        highlight = hero_title.locator(".hero-highlight")

        # It should exist and be visible
        count = highlight.count()
        print(f"Highlight span count: {count}")

        if count == 1:
            print("PASS: valid HTML tags (span.hero-highlight) are preserved.")
        else:
            print("FAIL: valid HTML tags seem lost.")
            print(hero_title.inner_html())
            sys.exit(1)

        browser.close()

if __name__ == "__main__":
    test_html_preserved()
