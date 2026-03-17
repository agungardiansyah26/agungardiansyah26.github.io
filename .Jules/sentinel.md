# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2026-03-17 - DOM-based XSS Prevention in translation logic
**Vulnerability:** Translation values stored in `data-i18n` attributes were directly assigned to `innerHTML` without sanitization, exposing the application to potential DOM-based Cross-Site Scripting (XSS) if translations were compromised or tampered with.
**Learning:** Even internal static files like `translations.js` should not be blindly trusted for direct HTML rendering. When sanitizing HTML in vanilla JS, a native `DOMParser` is an effective, lightweight alternative to external libraries like `DOMPurify`, capable of successfully stripping dangerous tags (`script`, `iframe`, `object`, `embed`) and event attributes (starting with `on` or `javascript:`).
**Prevention:** Always sanitize any dynamic string before assigning it to `innerHTML`. Use a custom `DOMParser` based sanitization function if avoiding external dependencies, or default to safe assignment methods like `textContent` where applicable.
