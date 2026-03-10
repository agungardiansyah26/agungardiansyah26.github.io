import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        file_path = f"file://{os.path.abspath('index.html')}"
        await page.goto(file_path)

        # Intercept and dismiss any unexpected dialogs to avoid browser hangs
        dialog_events = []
        page.on("dialog", lambda dialog: (dialog_events.append(dialog), asyncio.create_task(dialog.dismiss())))

        # Inject malicious HTML into translations object
        # We target the hero.title key
        malicious_payload = "I build learning experiences <img src=x onerror=alert('XSS1')> and <a href=\"jav&#x09;ascript:alert('XSS2')\">malicious link</a>"

        await page.evaluate(f"""
            translations['en']['hero']['title'] = `{malicious_payload}`;
        """)

        # Trigger language toggle to 'en'
        await page.click("#lang-en")

        # Wait a moment for translations to apply
        await page.wait_for_timeout(500)

        # Click the link to see if javascript: fires
        try:
            await page.click('.hero-title a', timeout=1000)
            await page.wait_for_timeout(500)
        except Exception:
            pass # Link might not exist if sanitized

        # Check the DOM
        hero_title_html = await page.evaluate("document.querySelector('.hero-title').innerHTML")

        print("Hero Title HTML after sanitization:")
        print(hero_title_html)
        print(f"Dialogs triggered: {len(dialog_events)}")

        if len(dialog_events) > 0:
            print("FAILED: XSS vulnerability detected! Alert dialog was fired.")
            exit(1)

        if "<img" in hero_title_html.lower():
            print("FAILED: <img> tag was not stripped out.")
            exit(1)

        if "javascript:" in hero_title_html.lower() or "jav\t" in hero_title_html.lower():
            print("FAILED: javascript URI was not stripped out.")
            exit(1)

        print("SUCCESS: XSS vulnerability mitigated. Sanitizer working as expected.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
