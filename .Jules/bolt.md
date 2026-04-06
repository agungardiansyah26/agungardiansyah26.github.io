## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-13 - [Redundant Initial DOM Updates]
**Learning:** Executing localization functions (like `updateContent`) on initial load unconditionally causes massive layout thrashing and redundant DOM mutations (e.g., 100+ innerHTML writes) if the user's language already matches the default HTML payload.
**Action:** Check `localStorage` against the default language payload before calling translation functions. If they match, skip the DOM updates entirely and only initialize interactive states (like theme toggles).
