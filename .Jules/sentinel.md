# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2025-02-18 - DOM-based XSS via Translation Data
**Vulnerability:** Cross-Site Scripting (XSS) risk via `innerHTML` injection of translation data. The translation script populated the UI without any sanitization, allowing scripts or malicious links to be executed if the translation data were ever compromised.
**Learning:** Native `DOMParser` allows for building custom, no-dependency sanitizers. However, attribute validation requires stripping HTML whitespace/entities (e.g., tabs in `jav&#x09;ascript:`) before checking prefixes, as browsers execute them anyway.
**Prevention:** A native `sanitizeHTML` function was implemented. Always pass any externally-sourced string (even local static translations to be safe) through a sanitizer before using `innerHTML`, or use `textContent` when HTML formatting isn't needed.