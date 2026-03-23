# Sentinel's Journal

## 2026-03-23 - DOM-based XSS via Translation Payloads
**Vulnerability:** The `updateContent` function used `element.innerHTML = translation` to set localized content. If translation data or another malicious payload injected code, it would be rendered without sanitization resulting in a DOM-based XSS vulnerability.
**Learning:** Assigning values to `innerHTML` directly is unsafe when the source string contains HTML.
**Prevention:** Implement a custom `sanitizeHTML` function using the native `DOMParser` to strip dangerous tags (`script`, `iframe`, `object`, `embed`) and attributes (e.g. `on*` handlers, `javascript:` URLs) before applying content to the DOM.

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.
