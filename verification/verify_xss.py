from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load local file
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # 1. Test: Inject Malicious Script
        print("Testing XSS injection...")

        malicious_html = '<img src=x onerror="window.xss_triggered=true">Search Result'

        # Inject into translation
        # We target 'id' language and 'hero.title' key
        page.evaluate(f"""() => {{
            window.xss_triggered = false;
            if (translations && translations.id && translations.id.hero) {{
                translations.id.hero.title = '{malicious_html}';
            }}
            updateContent('id');
        }}""")

        # Check if xss_triggered is true
        is_triggered = page.evaluate("() => window.xss_triggered === true")

        if is_triggered:
            print("❌ XSS VULNERABILITY DETECTED! Script executed.")
            # We don't exit here because we want to see if the content is sanitized in the fix.
            # But for "verification" of the fix, failing here is expected BEFORE the fix.
        else:
            print("✅ XSS attempt blocked. Script did not execute.")

        # Check content
        content = page.locator(".hero-title").inner_html()
        print(f"Rendered content: {content}")

        if "<img" in content and "onerror" in content:
             print("❌ Malicious tag still present in DOM!")
             is_vulnerable = True
        else:
             print("✅ HTML seems sanitized (or tag stripped).")
             is_vulnerable = False

        # 2. Test: Preserve Valid HTML
        print("\nTesting Valid HTML preservation...")
        valid_html = 'Hello <span class="highlight">World</span>'
        page.evaluate(f"""() => {{
            translations.id.hero.title = '{valid_html}';
            updateContent('id');
        }}""")

        content_valid = page.locator(".hero-title").inner_html()
        print(f"Rendered content for valid HTML: {content_valid}")

        # We expect <span class="highlight">World</span> to be present
        # Note: browser might normalize quotes or order
        if 'Hello <span class="highlight">World</span>' in content_valid or 'Hello <span class="highlight">World</span>' in content_valid.replace("'", '"'):
             print("✅ Valid HTML preserved.")
        else:
             print("❌ Valid HTML was stripped or altered unexpectedly.")
             # If strict sanitizer strips everything, this might fail. We want to preserve spans.

        browser.close()

        if is_vulnerable:
             print("\nFINAL RESULT: VULNERABLE")
             exit(1)
        else:
             print("\nFINAL RESULT: SECURE")
             exit(0)

if __name__ == "__main__":
    run()
