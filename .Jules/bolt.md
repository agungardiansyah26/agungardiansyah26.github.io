## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-11 - [Initial Load DOM Redundancy Prevention]
**Learning:** For static sites with multi-language support injected via JavaScript, running the translation function (`updateContent`) on the initial load unnecessarily queries and mutates the DOM if the user's preferred language matches the default HTML payload.
**Action:** Always check if the saved preference matches the default markup state before executing DOM-heavy functions. By skipping redundant updates on initial load, Total Blocking Time (TBT) and Time to Interactive (TTI) are measurably improved.
