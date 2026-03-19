## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-05 - [Prevent Redundant DOM Updates on Initial Load]
**Learning:** Reassigning `innerHTML` multiple times on initial load, especially when the content matches the default HTML payload, causes unnecessary DOM operations and overhead.
**Action:** Add a check during initial load to skip the full `updateContent()` DOM manipulation if the saved language is 'id'. Only call `updateThemeLabel()` to ensure proper ARIA label state, avoiding redundant updates.
