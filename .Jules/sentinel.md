# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2024-05-24 - Client-side Translation XSS Vulnerability
**Vulnerability:** A Cross-Site Scripting (XSS) vulnerability was identified in the `updateContent` function where unsanitized string values from `translations.js` were directly assigned to `element.innerHTML`.
**Learning:** Client-side translation payloads are commonly perceived as "safe" because they originate from within the codebase, leading to developers bypassing sanitization. However, if these translation objects can be manipulated by user input, URL parameters, or injected during a supply chain attack, it results in a critical DOM-based XSS vulnerability.
**Prevention:** Implement a recursive `DOMParser`-based `sanitizeHTML` function. Explicitly whitelist allowed tags (`SPAN`, `STRONG`, `EM`, `B`, `I`, `BR`, `P`, `A`) and attributes, while stripping control characters (`/[\x00-\x20\u00A0]/g`) from URLs to prevent bypasses like `jav&#x09;ascript:`. Wrap all `innerHTML` assignments with this sanitizer.