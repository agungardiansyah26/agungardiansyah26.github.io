# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.
## 2024-05-24 - DOMParser Mitigation for XSS in Translation System
**Vulnerability:** Translation values fetched from `translations.js` were directly injected into the DOM using `element.innerHTML`, which opened up a Cross-Site Scripting (XSS) vulnerability.
**Learning:** Even though the translations are stored locally within the application code, this mechanism represents an unsafe coding pattern, especially if a future update attempts to dynamically load translations from external sources. To adhere to strict security constraints without introducing external dependencies (like DOMPurify), an inline mitigation strategy must be used.
**Prevention:** Utilizing the native JavaScript `DOMParser`, a custom, lightweight `sanitizeHTML` function can securely parse the HTML payload. By using bottom-up recursion, stripping disallowed tags (while retaining content), and meticulously sanitizing attributes (specifically checking for and neutralizing `javascript:`, `vbscript:`, and `data:` schemes while stripping bypass control characters like tabs and spaces), XSS vectors are successfully neutralized before DOM insertion.
