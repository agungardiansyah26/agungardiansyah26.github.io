## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-30 - [Redundant Initial Load DOM Mutations]
**Learning:** Unconditionally hydrating the DOM with default text on load causes excessive, redundant `innerHTML` assignments that block the main thread and can trigger forced reflows.
**Action:** When implementing multi-language hydration, check if the saved user preference matches the default HTML payload before replacing the content. Skip DOM manipulation entirely if the payloads are identical.
