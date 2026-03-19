# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2026-03-19 - XSS Vulnerability in Translation System
**Vulnerability:** The translation system injected un-sanitized localized content directly into the DOM using `element.innerHTML = translation;`. This opened up potential Cross-Site Scripting (XSS) risks.
**Learning:** Using `innerHTML` with unsanitized data is dangerous. To avoid adding external dependencies like DOMPurify to a vanilla JS app, we can utilize a native `DOMParser` to manually strip dangerous HTML tags (`script`, `iframe`, `object`, `embed`) and event handler attributes (`on*`, `javascript:`).
**Prevention:** When assigning dynamic HTML strings to `innerHTML` in a vanilla setup, always pass the string through a native DOMParser-based sanitization function first to strip dangerous tags and attributes.
