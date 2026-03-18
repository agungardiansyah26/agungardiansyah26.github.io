# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2026-03-18 - Native DOMParser for XSS Sanitization
**Vulnerability:** `innerHTML` was used directly with data from a source (translation payload via `localStorage`), allowing for Cross-Site Scripting (XSS).
**Learning:** Relying on `innerHTML` directly is risky without sanitizing first, and introducing an external library like `DOMPurify` into vanilla JS adds unneeded overhead when it can be done natively for smaller scopes.
**Prevention:** Use a native `DOMParser` to strip dangerous tags (`script`, `iframe`, `object`, `embed`) and attributes (starting with `on` or `javascript:`) before using `innerHTML` to securely mitigate XSS vulnerabilities while keeping the app zero-dependency.
