## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-05 - [Avoid Redundant Initial DOM Updates]
**Learning:** Initializing translations by modifying the innerHTML of elements (e.g. `101` DOM nodes) when the HTML document is already authored in the default language causes a large number of unnecessary synchronous DOM manipulation and layout recalculations.
**Action:** Always verify if the user's saved preference matches the default markup payload. If it does, skip the full content replacement (e.g., `updateContent()`) and only perform the strictly necessary logic like updating ARIA labels (e.g., `updateThemeLabel()`).
