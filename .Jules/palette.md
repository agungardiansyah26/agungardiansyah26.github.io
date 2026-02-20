# Palette's Journal

## 2024-05-22 - Non-interactive span elements for toggles
**Learning:** The project uses `span` elements for interactive toggles (like language switcher) which lack keyboard accessibility and semantic meaning.
**Action:** Replace `span` with `<button type="button">` and add `aria-pressed` for toggle states, ensuring to reset button styles to match the original design.

## 2024-05-23 - Skip to content link with sticky header
**Learning:** Fixed/sticky headers obscure content when using anchor links or skip links. Standard anchor jumps land the element at the top of the viewport, under the header.
**Action:** Always add `scroll-margin-top` to the target element (e.g., `main` or section ID) equal to or slightly larger than the header height to ensure visibility.

## 2024-05-24 - Managing focus on hidden fixed elements
**Learning:** Elements hidden with `opacity: 0` remain in the tab order and can be focused by keyboard users, leading to confusion. `pointer-events: none` prevents mouse interaction but not keyboard focus.
**Action:** Use `visibility: hidden` (or `display: none`) alongside `opacity: 0` for transitions to ensure the element is removed from the accessibility tree and tab order when inactive.
