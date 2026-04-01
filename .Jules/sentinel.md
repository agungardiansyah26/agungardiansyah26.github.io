# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2026-04-01 - DOM-based XSS via Translation Data
**Vulnerability:** DOM-based XSS was possible because language translation strings from `translations.js` were directly assigned to `element.innerHTML` without sanitization in `assets/js/script.js`'s `updateContent` function.
**Learning:** Even though translation data is static in the codebase, directly updating the DOM with unsanitized strings via `innerHTML` is a dangerous pattern. If translation data or other configuration objects become dynamic or influenced by user input in the future, it creates an immediate attack vector.
**Prevention:** Implement a custom `sanitizeHTML` function using the native `DOMParser` to strip dangerous tags (`script`, `iframe`, `object`, `embed`) and attributes (e.g., `on*`, `javascript:`) before inserting content via `innerHTML`, avoiding the need for external dependencies like DOMPurify.
