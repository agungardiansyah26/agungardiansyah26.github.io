# Sentinel's Journal

## 2024-05-24 - DOM-based XSS in Translation Injection
**Vulnerability:** Translation strings were directly assigned to `element.innerHTML` without sanitization, allowing potential Cross-Site Scripting (XSS) if translation files or source inputs were compromised to include `<script>`, `javascript:` URIs, or `on*` event handlers.
**Learning:** Even static or seemingly trusted data sources like translation dictionaries can become vectors for DOM-based XSS if the data flow relies on unsanitized `innerHTML` assignments.
**Prevention:** Always sanitize dynamic content before injecting it into the DOM. Implement a native `DOMParser`-based sanitization function to strip dangerous tags (`script`, `iframe`, `object`, `embed`) and attributes (`on*`, `javascript:`) without relying on external dependencies like DOMPurify.

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.
