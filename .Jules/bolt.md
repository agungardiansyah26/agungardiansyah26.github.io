## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-02-26 - [Prevent Redundant Initial Load DOM Mutations]
**Learning:** Unconditional client-side translation hydration overwrites the `innerHTML` of all nodes on initial load, even when the saved preference matches the default pre-rendered HTML payload. This causes unnecessary main-thread blocking, O(n) DOM traversal, and redundant painting.
**Action:** When initializing hydration scripts, always check if the saved preference (e.g., language='id') strictly matches the default payload, and early return to preserve the critical initial render path.