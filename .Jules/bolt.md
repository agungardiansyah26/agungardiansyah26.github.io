## 2026-02-20 - [Theme Toggle FOUC Prevention]
**Learning:** Static sites relying on deferred JS for theme toggling experience a Flash of Unstyled Content (FOUC) and layout shifts.
**Action:** Use an inline script in `<head>` to detect preferences and apply classes immediately to `<html>`, combined with CSS-based icon visibility logic, to ensure correct initial render.

## 2026-02-23 - [Scroll Performance Optimization]
**Learning:** Attaching scroll event listeners directly to the window without throttling causes excessive function calls and layout thrashing, especially on high-refresh-rate displays.
**Action:** Use `requestAnimationFrame` to throttle scroll handlers for visual updates, ensuring logic runs at most once per frame. Use `{ passive: true }` to allow the browser to optimize scrolling.

## 2026-03-28 - [Active Navigation Link Scroll Optimization]
**Learning:** Using an `IntersectionObserver` that iterates over a `NodeList` and updates DOM `classList` for every entry continuously leads to excessive DOM mutation, thrashing, and performance degradation during scrolling.
**Action:** Use a `Map` to cache the relation between section IDs and anchor links (`O(1)` lookups). Additionally, keep track of `currentActiveLinks` and only mutate the DOM (`classList.add/remove`) when the actual active section changes to drastically reduce redundant operations.

## 2026-04-21 - [i18n Parsing and Traversal Optimization]
**Learning:** Re-instantiating `DOMParser` and querying the DOM for translation elements on every language toggle introduces significant layout thrashing and computational overhead during continuous user interactions.
**Action:** Cache DOM queries for dynamic elements outside the update loop and reuse a single `DOMParser` instance globally to avoid redundant instantiation and tree-walking penalties.
