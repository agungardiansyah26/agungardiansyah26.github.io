## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-02-23 - [Optimized Script Loading and Initial Render]
**Learning:** For static sites with pre-filled content (e.g., default language HTML), blindly running update scripts on initialization (like `updateContent`) causes redundant DOM thrashing and layout calculations.
**Action:** Check if the initial state (e.g., language preference) matches the static HTML before running update logic. Also, move critical but non-blocking scripts to `<head>` with `defer` to leverage the browser's preload scanner for parallel downloading.
