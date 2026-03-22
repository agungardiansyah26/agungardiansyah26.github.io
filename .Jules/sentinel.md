# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2026-03-22 - DOM-based XSS in Translation System
**Vulnerability:** The translation system assigned translated text directly to `innerHTML` without sanitization, leading to a potential DOM-based XSS via malicious input in `data-i18n`.
**Learning:** `DOMParser` can be used to construct a quick native client-side sanitizer to strip `script`/`iframe` tags and attributes starting with `on` and `javascript:` without introducing heavy external dependencies like `DOMPurify`.
**Prevention:** Always sanitize any dynamic data that is bound to the DOM directly via `innerHTML`.
