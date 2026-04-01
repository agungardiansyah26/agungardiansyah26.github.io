## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-02-26 - [Navigation Observer Optimization]
**Learning:** Updating classes inside an IntersectionObserver loop directly iterates over DOM queries every time which leads to redundant O(N) operations and layout thrashing.
**Action:** Use a `Map` array structure to lookup elements efficiently with O(1) time and track an active links array state to mutate only when absolutely necessary.

## 2026-02-26 - [Initial Load Language Optimization]
**Learning:** If initial text payloads exist correctly without JavaScript, using JavaScript immediately to query logic that returns the same text results in massive DOM layout thrashing and paints for zero reason.
**Action:** Introduce a conditional block at the initial language load handler to completely skip query selecting and rewriting `innerHTML` unless it differs from the initially assumed state structure.