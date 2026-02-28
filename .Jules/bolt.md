## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2024-05-24 - [IntersectionObserver Navigation Highlight Optimization]
**Learning:** Iterating through all navigation links and removing the `active` class on every intersection observer entry causes unnecessary layout thrashing and redundant DOM updates, especially when scrolling past multiple sections quickly.
**Action:** Use a `Map` for O(1) lookups to directly access the corresponding link for an intersected section. Track the `currentActiveLink` to ensure DOM updates (adding/removing classes) only occur when the active link actually changes.
