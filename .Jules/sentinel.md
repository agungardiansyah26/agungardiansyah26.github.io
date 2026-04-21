# Sentinel's Journal

## 2025-02-23 - DOM-based XSS via Translation Payloads
**Vulnerability:** The `updateContent` function assigned unsanitized translation strings directly to `element.innerHTML`, creating a DOM-based XSS vulnerability if malicious data is present in `translations.js`.
**Learning:** Even internal static files can be vectors if dynamically loaded without sanitization. Externalizing strings to `innerHTML` demands explicit validation, as simple text assignments don't strip dangerous tags (`script`, `iframe`, etc.) or attributes (`onerror`, `javascript:`).
**Prevention:** Implement a `sanitizeHTML` utility utilizing a native `DOMParser` to aggressively strip unapproved tags and attributes before any `innerHTML` assignment. Ensure values are trimmed and lowercased prior to validation to mitigate basic bypasses.

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2026-03-19 - XSS Vulnerability in Translation System
**Vulnerability:** The translation system injected un-sanitized localized content directly into the DOM using `element.innerHTML = translation;`. This opened up potential Cross-Site Scripting (XSS) risks.
**Learning:** Using `innerHTML` with unsanitized data is dangerous. To avoid adding external dependencies like DOMPurify to a vanilla JS app, we can utilize a native `DOMParser` to manually strip dangerous HTML tags (`script`, `iframe`, `object`, `embed`) and event handler attributes (`on*`, `javascript:`).
**Prevention:** When assigning dynamic HTML strings to `innerHTML` in a vanilla setup, always pass the string through a native DOMParser-based sanitization function first to strip dangerous tags and attributes.

## 2026-04-21 - DOM-based XSS via Bypassable Blocklist
**Vulnerability:** The previous `sanitizeHTML` implementation used a blocklist for dangerous tags but allowed unhandled tags through, stripping their attributes. It failed to address bypasses like `<svg>` or deeply nested event handlers that could still execute.
**Learning:** Blocklisting specific tags (like `script` or `iframe`) is insufficient against XSS because browsers parse many edge-case vectors (e.g., `svg onload`, `data:` URIs, or unknown tags with malicious behavior). It is far more robust to define what is explicitly allowed.
**Prevention:** Transitioned `sanitizeHTML` to a strict allowlist approach. By explicitly defining permitted tags (e.g., `b`, `span`, `a`) and permitted attributes (e.g., `class`, `href`), all other content is implicitly rejected. Used child-hoisting for unauthorized tags to preserve text nodes.
