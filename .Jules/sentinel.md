# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2026-03-21 - DOM-based XSS via innerHTML assignments
**Vulnerability:** DOM-based XSS vulnerability discovered in the `updateContent` function where `element.innerHTML` was directly assigned translations without sanitization.
**Learning:** Assigning dynamic user-provided or external data directly to `innerHTML` allows execution of dangerous elements and event handlers (`<script>`, `onerror`, `javascript:`).
**Prevention:** Always sanitize dynamic HTML inputs using a native `DOMParser` before assignment to `innerHTML` to strip dangerous elements and attributes, avoiding introducing heavy external dependencies like `DOMPurify` for simple sanitization.
