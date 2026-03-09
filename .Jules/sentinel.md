# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2024-10-24 - DOM-based XSS in Translation Updates
**Vulnerability:** XSS vulnerability in `assets/js/script.js` due to `element.innerHTML = translation;` within the `updateContent` function, allowing an attacker who manipulates the translation dictionary to inject arbitrary HTML into the DOM.
**Learning:** `innerHTML` is inherently unsafe when handling data derived from variables or objects outside of direct, hardcoded control. Double-encoding and entity bypasses (e.g., `jav&#x09;ascript:`) require careful regex or sanitization.
**Prevention:** Create a bottom-up DOM tree sanitization function (`sanitizeHTML`) using `DOMParser`, allowing only specific benign tags (`SPAN`, `STRONG`, `EM`, `B`, `I`, `BR`, `P`, `A`) and attributes (`class`, `href`, `target`, `rel`). Pass all dynamic text updates through `sanitizeHTML` before injecting into `innerHTML`.
