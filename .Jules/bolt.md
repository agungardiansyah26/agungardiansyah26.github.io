## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-06 - [IntersectionObserver Navigation Performance Optimization]
**Learning:** Using `IntersectionObserver` to highlight navigation links without state tracking causes O(N) DOM writes/class manipulations per update event on all navigation links, leading to layout thrashing.
**Action:** Use a `Map` to hold navigation links mapped by their targets to achieve O(1) lookup. Track the current active link and only perform DOM modifications when a new link truly becomes active.
