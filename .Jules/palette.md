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
