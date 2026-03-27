# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2024-05-24 - DOM-based XSS via innerHTML
**Vulnerability:** Translation strings were directly assigned to `element.innerHTML` without sanitization. This allowed execution of arbitrary JavaScript if the translation source (e.g. `translations.js`) was compromised or dynamically populated.
**Learning:** Using `innerHTML` with unsanitized input is a critical security risk. A malicious payload can include tags like `<script>`, `<iframe>`, `<embed>`, `<object>` or attributes like `onerror` and `javascript:` URIs.
**Prevention:** Implement a `sanitizeHTML` function using the native `DOMParser` to parse the string into a DOM structure, then programmatically remove dangerous tags and attributes before converting back to HTML and assigning to `innerHTML`.
