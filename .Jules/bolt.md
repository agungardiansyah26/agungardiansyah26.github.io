## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-15 - [Skip Redundant Initial Translation Updates]
**Learning:** Running translation scripts on initial load when the default HTML already matches the target language causes unnecessary DOM operations (e.g., redundant `innerHTML` assignments) which blocks the main thread momentarily and slows down First Contentful Paint.
**Action:** Add condition checks on initial load to skip full DOM updates if the saved language preference matches the default HTML language.
