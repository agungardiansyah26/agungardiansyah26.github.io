## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-02-23 - [Initial Load Redundant DOM Mutations]
**Learning:** Running translation functions unconditionally on initial load causes unnecessary DOM mutations and innerHTML assignments if the default HTML is already in the target language.
**Action:** Add an early return condition during initialization to skip redundant DOM updates and only initialize lightweight states (like ARIA labels) when the cached language matches the default.
