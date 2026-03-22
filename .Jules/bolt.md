## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-22 - [Redundant Initial DOM Updates Prevention]
**Learning:** Automatically running full innerHTML updates on page load for multi-language sites triggers excessive reflows and layout shifts, even if the payload's default language matches the user's saved preference.
**Action:** Implement conditional checks to verify whether the stored language setting requires new DOM modifications. Skip translation loops when the saved language is identical to the payload default, reducing redundant operations.
