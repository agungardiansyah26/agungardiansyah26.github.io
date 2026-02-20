from playwright.sync_api import sync_playwright, expect
import os
import time

def test_form_ux():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.on("console", lambda msg: print(f"BROWSER CONSOLE: {msg.text}"))
        page.on("pageerror", lambda err: print(f"BROWSER ERROR: {err}"))

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Loading: {file_path}")
        page.goto(file_path)

        # Mock the form submission endpoint
        def handle_route(route):
            print(f"Intercepted request to: {route.request.url}")
            # Verify loading state inside the handler (while request is pending)
            print("Verifying loading state (inside route handler)...")
            is_sending = page.evaluate("document.querySelector('button[type=\"submit\"] span[data-i18n]').textContent === 'Mengirim...'")
            is_disabled = page.evaluate("document.querySelector('button[type=\"submit\"]').disabled")

            print(f"Loading state check inside handler: Text='Mengirim...'? {is_sending}, Disabled? {is_disabled}")

            if not is_sending or not is_disabled:
                print("FAIL: Loading state incorrect during request!")
            else:
                print("PASS: Loading state correct during request!")

            # Complete the request
            route.fulfill(
                status=200,
                content_type="application/json",
                body='{"ok": true}'
            )

        # Intercept POST requests to formspree
        page.route("**/formspree.io/**", handle_route)

        # Fill the form
        print("Filling the form...")
        page.fill("#name", "Test User")
        page.fill("#email", "test@example.com")
        page.fill("#message", "This is a test message.")

        # Click submit
        submit_btn = page.locator("button[type='submit']")
        status_div = page.locator("#form-status")

        print("Submitting form...")
        submit_btn.click()

        # Verify Success State
        print("Waiting for success message...")
        try:
            expect(status_div).to_have_text("Pesan terkirim! Terima kasih.", timeout=5000)
            print("Success message verified.")
            page.screenshot(path="verification/form_success.png")
            print("Screenshot saved to verification/form_success.png")
        except Exception as e:
             print(f"Success message not found. Status content: {status_div.text_content()}")
             raise e

        # Verify Form Reset
        print("Verifying form reset...")
        expect(page.locator("#name")).to_have_value("")
        expect(page.locator("#email")).to_have_value("")
        expect(page.locator("#message")).to_have_value("")
        print("Form reset verified.")

        browser.close()

if __name__ == "__main__":
    test_form_ux()
