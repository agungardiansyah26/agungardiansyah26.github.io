# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2026-03-07 - DOM-based XSS in Translation Injection
**Vulnerability:** The translation system injected unvalidated strings directly into the DOM using `element.innerHTML`, creating a DOM-based XSS vulnerability if translation data was compromised.
**Learning:** `innerHTML` should never be used with un-sanitized data. A custom `DOMParser`-based `sanitizeHTML` function is needed for complex nested structures (like mixing text with HTML tags like `<strong>`) when no external sanitization library is available.
**Prevention:** Always sanitize data before assigning to `innerHTML`. Use `DOMParser` to filter allowed tags and attributes, and explicitly strip control characters from URL attributes to prevent entity bypasses (e.g., `jav&#x09;ascript:`).
