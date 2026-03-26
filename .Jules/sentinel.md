# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2026-03-26 - XSS in Dynamic Translations
**Vulnerability:** DOM-based Cross-Site Scripting (XSS) due to directly assigning translation strings (from `translations.js`) to `innerHTML` without sanitization.
**Learning:** Even internal or semi-trusted data sources like translation files can become vectors for XSS if they contain unsanitized HTML structures (like `<script>` or `javascript:` URIs) and are directly parsed by the browser. The vulnerability existed because the translation update logic assumed all incoming strings were safe text.
**Prevention:** When assigning dynamic content to `innerHTML` in vanilla JS, always use a native `DOMParser` to strip dangerous tags (`script`, `iframe`, `object`, `embed`) and potentially malicious attributes (starting with `on` or `javascript:`). Always `.trim().toLowerCase()` attribute values before checking for `javascript:` to prevent basic bypasses like ` href=" javascript:alert(1)"`.
