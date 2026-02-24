# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2024-05-24 - Translation System XSS Risk
**Vulnerability:** The translation system in `assets/js/script.js` used `element.innerHTML` to inject translated strings, creating a potential XSS vector if translation data were compromised or dynamically loaded from an untrusted source.
**Learning:** Even with static translation files, defense-in-depth is crucial. Relying solely on data integrity is risky. CSP (Content Security Policy) effectively mitigated execution (`script-src 'self'`) but HTML injection was still possible (defacement).
**Prevention:** Implemented a strict `sanitizeHTML` function using `DOMParser` to allow only a specific whitelist of safe tags (`SPAN`, `STRONG`, `EM`, `B`, `I`, `BR`, `P`) and attributes (`class`), ensuring that injected content cannot execute scripts or break layout unexpectedly.
