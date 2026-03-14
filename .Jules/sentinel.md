# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2025-03-14 - Translation Strings XSS Mitigation
**Vulnerability:** Unsanitized translation strings were directly assigned to `element.innerHTML`, introducing an XSS vulnerability where malicious payload could be injected into the DOM.
**Learning:** Direct string assignment to `innerHTML` when rendering multi-language text is dangerous, especially when translations may contain user-defined content or come from an external untrusted source.
**Prevention:** Implement a recursive `sanitizeHTML` function utilizing `DOMParser` to parse the input string and remove disallowed tags and attributes (e.g., `<script>`, `<img onerror=...>`, `href="javascript:..."`), stripping potentially malicious control characters and spaces from `href`/`src` attributes to prevent bypasses, before appending to the DOM.
