## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-25 - [Redundant DOM Updates on Initial Load]
**Learning:** Running an unconditionally invoked translation/content population function on initial load triggers hundreds of unnecessary `innerHTML` re-assignments if the saved language matches the default server-rendered language.
**Action:** Add an early return or condition in initialization scripts to skip DOM updates (`innerHTML`) if the requested state matches the default HTML payload, checking only necessary states (like aria attributes).
