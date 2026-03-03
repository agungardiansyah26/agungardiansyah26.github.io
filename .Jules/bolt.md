## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-03 - [IntersectionObserver Navigation Optimization]
**Learning:** Updating all navigation link classes inside an `IntersectionObserver` callback creates an O(N) loop inside an O(M) trigger, causing unnecessary DOM reads and writes on every scroll intersection, leading to minor layout thrashing.
**Action:** Use an O(1) `Map` to look up the target navigation link based on the section ID, and maintain a `currentActiveLink` reference to only update the DOM when the active state actually changes.
