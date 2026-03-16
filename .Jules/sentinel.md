# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2024-05-24 - InnerHTML XSS Vulnerability in Translation Logic
**Vulnerability:** XSS vulnerability through the use of `element.innerHTML = translation;` in `assets/js/script.js` when applying multi-language translations without sanitization.
**Learning:** Even if the translation dictionary is currently static and trusted, using direct `innerHTML` assignments is a bad practice. If translations were ever loaded dynamically from a third-party source or manipulated locally (e.g. injected into local storage or state), it could execute arbitrary JavaScript.
**Prevention:** Implement a native HTML sanitizer using `DOMParser` to parse the incoming HTML, strip out dangerous tags (`script`, `iframe`, `object`, `embed`), and remove dangerous attributes (like event handlers starting with `on` and `javascript:` URIs) before assigning to `innerHTML`.
