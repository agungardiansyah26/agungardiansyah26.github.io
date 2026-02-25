## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-02-23 - [IntersectionObserver Optimization]
**Learning:** Iterating over all navigation links inside an `IntersectionObserver` callback for every intersecting entry causes unnecessary DOM reflows (O(N*M)), especially when multiple sections intersect quickly.
**Action:** Use a `Map` for O(1) lookup of navigation elements and track the `currentActiveNav` state to ensure DOM updates only happen when the active section actually changes.
