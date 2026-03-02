## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-02 - [IntersectionObserver Navigation Thashing]
**Learning:** IntersectionObserver callbacks can cause redundant DOM thrashing on scroll if the state is not tracked, as the observer triggers on every threshold crossing. Looping over elements to find and update class lists inside the callback is O(n) and inefficient for navigation links.
**Action:** Use an O(1) Map for quick DOM node lookups by target ID, track the `currentActiveLink` to avoid modifying `classList` unless the state actually changes, and filter `isIntersecting` entries to process only the most relevant one.
