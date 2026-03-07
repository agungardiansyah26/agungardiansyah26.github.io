## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-07 - [Scroll Navigation DOM Updates]
**Learning:** Continuous O(N) DOM queries and updates within an IntersectionObserver callback to highlight active navigation links cause unnecessary layout recalculations and reduce scrolling performance.
**Action:** Use a Map for O(1) link lookups and track the `currentActiveLink`. This limits DOM writes strictly to moments when the active link changes, preventing redundant layout thrashing.
