## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-21 - [Scroll Event Throttling]
**Learning:** Legacy scroll event listeners on the main thread can cause layout thrashing and jank, especially on mobile devices, if not throttled.
**Action:** Always wrap scroll event handlers in `requestAnimationFrame` (or use `IntersectionObserver`) to ensure they run synchronized with the repaint cycle.
