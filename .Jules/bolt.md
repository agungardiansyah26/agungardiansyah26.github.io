## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-01 - [Active Navigation Highlighting Optimization]
**Learning:** Updating active navigation links inside an `IntersectionObserver` callback by looping through all links via `document.querySelectorAll(".nav-link")` causes an O(N) DOM manipulation nested inside the intersection event loop. As the user scrolls, this executes repeatedly and causes unnecessary reflows/repaints, blocking the main thread.
**Action:** Use a `Map` initialized outside the observer to cache navigation link DOM nodes for O(1) lookups based on their `href` identifiers. Keep track of `currentActiveLink` to ensure we only update the DOM when the actual active target changes (at most 2 class updates per change) rather than modifying all nodes repeatedly.
