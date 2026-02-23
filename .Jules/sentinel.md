# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2026-02-23 - Unsanitized HTML in Translations
**Vulnerability:** Translation strings containing HTML were inserted directly into the DOM using `innerHTML` without sanitization. While the current translation source is trusted (local file), this created a potential XSS vector if the source were compromised or replaced with a dynamic one.
**Learning:** `DOMParser` can be used to parse and sanitize HTML strings effectively in the browser without external libraries.
**Prevention:** Implemented a `sanitizeHTML` function that parses the input string and only allows a strict whitelist of tags (`SPAN`, `STRONG`, `EM`, `B`, `I`, `BR`, `P`) and attributes (`class`) before insertion.
