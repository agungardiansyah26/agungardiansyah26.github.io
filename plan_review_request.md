I have reviewed the current codebase and the instructions to act as the "Palette" 🎨 UX-focused agent.

The issue requires ONE micro-UX improvement.
Upon exploring `assets/css/style.css`, I see several specific focus-visible styles but no standardized global focus states for interactable elements.

Memory explicitly instructs:
> Focus indicators for interactive elements (e.g., `a`, `button`, `input`, `textarea`, `[tabindex='0']`) are globally standardized in `assets/css/style.css` using `:focus-visible` with a `2px solid var(--accent)` outline and `2px` offset. Avoid adding redundant, component-specific focus styles and do not enforce a global `border-radius` on focus states.

Currently, we have:
1. `.skip-link:focus`
2. `.lang-option:focus-visible`
3. `.input-field:focus`
4. `.back-to-top:focus-visible`

Based on this, my plan is:
1. *Modify `assets/css/style.css` to add the global focus indicator.*
   - Add a global selector block: `a:focus-visible, button:focus-visible, input:focus-visible, textarea:focus-visible, [tabindex="0"]:focus-visible`
   - Apply `outline: 2px solid var(--accent); outline-offset: 2px;` inside it.
2. *Clean up redundant component-specific focus styles.*
   - Remove the `outline` rules from `.skip-link:focus`, `.lang-option:focus-visible`, `.input-field:focus` (while keeping `border-color` / `background` changes for `.input-field:focus`), and `.back-to-top:focus-visible`.
3. *Add a journal entry to `.Jules/palette.md`.*
   - Create a critical learning entry following the required format about standardizing focus indicators globally with `:focus-visible`.
4. *Verify changes using Playwright.*
   - Run a short verification script that navigates elements using `page.keyboard.press('Tab')` and confirms `:focus-visible` styles apply globally.
5. *Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.*
6. *Submit the UX improvement PR.*
   - Submit the PR with the title '🎨 Palette: Add standardized global focus visible styles' and description answering What, Why, Impact, and Accessibility.
