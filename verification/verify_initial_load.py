from playwright.sync_api import sync_playwright, expect
import os

def test_initial_load_mutations():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Clear storage by not persisting context
        context = browser.new_context()
        page = context.new_page()

        # Inject MutationObserver before any script runs
        page.add_init_script("""
            window.__mutationCount = 0;
            const observer = new MutationObserver((mutations) => {
                for (const m of mutations) {
                    if (m.type === 'childList') {
                        window.__mutationCount++;
                    }
                }
            });
            // We want to observe body, but init_script runs before body exists
            // So we wait for DOMContentLoaded
            window.addEventListener('DOMContentLoaded', () => {
                observer.observe(document.body, { childList: true, subtree: true });
            });
        """)

        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Loading: {file_path}")
        page.goto(file_path)

        # Wait for the page to be fully loaded
        page.wait_for_load_state("networkidle")

        # Give it a small moment for any potential script execution to finish
        page.wait_for_timeout(500)

        # Get mutation count
        mutation_count = page.evaluate("window.__mutationCount")

        print(f"Number of childList mutations on initial load: {mutation_count}")

        # We expect 0 mutations if savedLang is 'id' and we don't call updateContent
        # Wait, there might be other mutations, like reveal Elements or something?
        # The reveal elements add classes, which are attribute mutations, not childList.
        # updateContent modifies innerHTML, which creates childList mutations.

        assert mutation_count == 0, f"Expected 0 childList mutations on initial load, but found {mutation_count}."

        print("Verification passed: No redundant DOM childList mutations on initial load.")

        browser.close()

if __name__ == "__main__":
    test_initial_load_mutations()
