import subprocess
import time
import sys
import os
from playwright.sync_api import sync_playwright

def run_server():
    server_process = subprocess.Popen(
        [sys.executable, "-m", "http.server", "8000"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(2)
    return server_process

def verify_scroll_screenshot():
    print("Starting server...")
    server = run_server()
    try:
        with sync_playwright() as p:
            print("Launching browser...")
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Set viewport large enough
            page.set_viewport_size({"width": 1280, "height": 800})

            url = "http://localhost:8000"
            print(f"Loading: {url}")
            page.goto(url)

            # Scroll down to trigger back-to-top button
            print("Scrolling down...")
            page.evaluate("window.scrollTo(0, 1000)")
            time.sleep(1.5) # Wait for transition

            # Verify visible
            btn = page.locator("#back-to-top")
            opacity = btn.evaluate("el => getComputedStyle(el).opacity")
            print(f"Opacity: {opacity}")

            if float(opacity) > 0.9:
                print("Button is visible.")
            else:
                print("Button NOT visible!")

            # Take screenshot
            # Ensure directory exists
            os.makedirs("verification", exist_ok=True)
            screenshot_path = "verification/scroll_screenshot.png"
            print(f"Taking screenshot to {screenshot_path}...")
            page.screenshot(path=screenshot_path)

            browser.close()
    finally:
        print("Stopping server...")
        server.terminate()
        server.wait()

if __name__ == "__main__":
    verify_scroll_screenshot()
