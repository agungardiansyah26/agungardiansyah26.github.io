# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2024-05-24 - Unsanitized HTML in Translations
**Vulnerability:** The i18n system used `innerHTML` to inject translated strings containing formatting tags (like `<span>`), which could allow XSS if translations were compromised.
**Learning:** Even trusted static data sources should be treated with caution when using dangerous sinks like `innerHTML`.
**Prevention:** Implemented a lightweight `sanitizeHTML` function using `DOMParser` with a strict whitelist of allowed tags (`SPAN`, `STRONG`, `EM`, `B`, `I`, `BR`, `P`) and attributes (`class`) before injection.
