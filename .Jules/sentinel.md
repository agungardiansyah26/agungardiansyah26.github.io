# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2025-03-03 - DOM-based XSS via Translation Dictionary
**Vulnerability:** XSS vulnerability in `assets/js/script.js` due to direct assignment of translation strings to `element.innerHTML` without prior sanitization.
**Learning:** Even internal or static translation dictionaries can be vectors for XSS if they process unsanitized user inputs or external data in the future. The use of `innerHTML` inherently trusts the input to be valid HTML.
**Prevention:** Implement a strict, `DOMParser`-based `sanitizeHTML` function that filters allowed tags and attributes, strips dangerous URIs (like `javascript:`), and mitigates entity bypasses. Apply this function before assigning any string to `innerHTML`.
