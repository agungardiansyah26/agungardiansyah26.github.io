## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-27 - [Intersection Observer DOM Thrashing]
**Learning:** Updating active navigation links inside an `IntersectionObserver` callback indiscriminately using `forEach` on all links causes unnecessary O(n) loop overhead and frequent `classList.add/remove` DOM mutations.
**Action:** Map navigation links by `id` once upfront for O(1) lookups. Track a specific array of `currentActiveLinks` to skip unnecessary DOM updates when the visible section hasn't changed, significantly reducing rendering overhead during fast scrolling.
