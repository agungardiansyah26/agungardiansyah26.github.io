## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-02-23 - [Avoid Redundant Initial DOM Updates]
**Learning:** Running a full translation function (which updates innerHTML) unconditionally on initial load causes unnecessary layout thrashing and redundant DOM queries if the saved language matches the default HTML payload.
**Action:** Always check if the saved language matches the default language before invoking translation logic, and short-circuit to only update strictly necessary dynamic attributes (like `aria-label` for theme toggles).
