# Palette's Journal

## 2024-05-22 - Non-interactive span elements for toggles
**Learning:** The project uses `span` elements for interactive toggles (like language switcher) which lack keyboard accessibility and semantic meaning.
**Action:** Replace `span` with `<button type="button">` and add `aria-pressed` for toggle states, ensuring to reset button styles to match the original design.

## 2024-05-23 - Skip to content link with sticky header
**Learning:** Fixed/sticky headers obscure content when using anchor links or skip links. Standard anchor jumps land the element at the top of the viewport, under the header.
**Action:** Always add `scroll-margin-top` to the target element (e.g., `main` or section ID) equal to or slightly larger than the header height to ensure visibility.

## 2024-05-24 - Async Form Submission & CSP
**Learning:** Replacing standard form submission with `fetch` requires updating Content Security Policy (CSP) to allow external API connections (`connect-src`), not just `form-action`. Async forms significantly improve UX by avoiding page reloads.
**Action:** When implementing async forms, check CSP headers and provide clear loading/success feedback inline, ensuring screen reader announcements via `aria-live`.

## 2024-05-24 - Managing focus on hidden fixed elements
**Learning:** Elements hidden with `opacity: 0` remain in the tab order and can be focused by keyboard users, leading to confusion. `pointer-events: none` prevents mouse interaction but not keyboard focus.
**Action:** Use `visibility: hidden` (or `display: none`) alongside `opacity: 0` for transitions to ensure the element is removed from the accessibility tree and tab order when inactive.

## 2024-05-24 - Dynamic ARIA Labels for Toggles
**Learning:** Static `aria-label` ("Toggle Theme") is insufficient for state toggles. Users need to know the *current state* or the *next action* (e.g., "Switch to Light Mode").
**Action:** Use JavaScript to update `aria-label` (and `title`) dynamically based on state and current language.

## 2024-05-25 - Global focus visible styles
**Learning:** Focus rings were added individually on some components but missing on many default interactive elements (like anchor links and primary buttons), causing an inconsistent keyboard navigation experience.
**Action:** Always add a global `a:focus-visible, button:focus-visible` rule with `outline` and `outline-offset` instead of maintaining focus styles on individual components to ensure consistent keyboard accessibility.
