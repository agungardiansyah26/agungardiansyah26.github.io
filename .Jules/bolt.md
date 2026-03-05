## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-02-23 - [IntersectionObserver DOM Manipulation Optimization]
**Learning:** Iterating over all elements in an O(N) loop to update active state classes inside an IntersectionObserver callback is inefficient and can cause layout thrashing during scroll, particularly when multiple entries intersect.
**Action:** Use a `Map` for O(1) element lookups, track the current active element's state to ensure `classList.add`/`remove` are strictly called only when the target actually changes, and prioritize the last intersecting entry.
