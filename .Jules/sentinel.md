# Sentinel's Journal

## 2026-03-25 - DOM-based XSS in Translation Loader
**Vulnerability:** A DOM-based Cross-Site Scripting (XSS) vulnerability existed due to assigning raw string translations directly to `element.innerHTML`.
**Learning:** Translating content using `innerHTML` can inadvertently execute malicious scripts if the translation source is manipulated (e.g. `javascript:` links or `onerror` handlers).
**Prevention:** Use a native `DOMParser` to sanitize HTML content before using `innerHTML`. Always strip dangerous tags (`script`, `iframe`, `object`, `embed`) and attributes starting with `on` or `javascript:`, remembering to `.trim().toLowerCase()` attribute values to prevent basic bypasses.

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.
