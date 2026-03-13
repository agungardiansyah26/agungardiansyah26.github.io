# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2024-05-24 - DOM-based XSS in Translation Updates
**Vulnerability:** Translations containing malicious HTML strings were being rendered dynamically using `element.innerHTML = translation` in the translation script, resulting in a DOM-based XSS vulnerability.
**Learning:** Even though translation inputs may be internal (e.g. `translations.js`), dynamically updating HTML via `innerHTML` without sanitization creates a potential attack vector if an attacker injects malicious values or bypasses the translation source.
**Prevention:** Implement a `sanitizeHTML` function utilizing `DOMParser` to recursively filter nodes and strip unapproved tags, as well as maliciously constructed URIs containing control characters (e.g. `jav&#x09;ascript:`). Apply the sanitized value to `innerHTML`.
