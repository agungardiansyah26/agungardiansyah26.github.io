## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-09 - [Redundant Initial Render Updates]
**Learning:** Running JavaScript state initialization that overwrites the DOM with the same content as the initial HTML payload causes unnecessary DOM queries, layout reflows, and performance bottlenecks, especially in large translation objects.
**Action:** Check local state against the default HTML state before applying updates on initial load. If they match, skip the heavy DOM operations and only initialize necessary interactive properties (like ARIA labels).
