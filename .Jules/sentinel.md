# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2025-03-05 - DOM XSS in Translation System
**Vulnerability:** XSS vulnerability where maliciously crafted translation strings could be injected into the DOM directly using `element.innerHTML = translation;` in `updateContent`.
**Learning:** Even though translation files are typically static assets, trusting all content rendered via `innerHTML` can introduce DOM-based XSS if the data source is compromised or if user inputs ever make their way into the translation system.
**Prevention:** Always sanitize dynamically rendered HTML using a strict allowlist of tags and attributes. Use `DOMParser` to properly parse and strip invalid nodes and protocol schemes like `javascript:`.
