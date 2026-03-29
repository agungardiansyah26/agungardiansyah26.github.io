# Sentinel's Journal

## 2025-02-23 - DOM-based XSS via Translation Payloads
**Vulnerability:** The `updateContent` function assigned unsanitized translation strings directly to `element.innerHTML`, creating a DOM-based XSS vulnerability if malicious data is present in `translations.js`.
**Learning:** Even internal static files can be vectors if dynamically loaded without sanitization. Externalizing strings to `innerHTML` demands explicit validation, as simple text assignments don't strip dangerous tags (`script`, `iframe`, etc.) or attributes (`onerror`, `javascript:`).
**Prevention:** Implement a `sanitizeHTML` utility utilizing a native `DOMParser` to aggressively strip unapproved tags and attributes before any `innerHTML` assignment. Ensure values are trimmed and lowercased prior to validation to mitigate basic bypasses.

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.
