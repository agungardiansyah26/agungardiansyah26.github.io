## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-26 - [Redundant DOM Updates on Initial Load]
**Learning:** Calling translation or initialization functions that unconditionally overwrite `innerHTML` of numerous elements on initial load, even when the default language matches the HTML payload, causes unnecessary DOM writes (e.g. 101 `innerHTML` assignments), wasting client CPU cycles during the critical rendering path.
**Action:** Add a conditional check to initialization logic to skip redundant DOM updates if the state matches the default HTML payload. Ensure accessibility attributes (like `aria-label`) that depend on JavaScript are still explicitly updated.
