# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2024-05-23 - XSS Vulnerability in Translation System
**Vulnerability:** The translation system injected unescaped user-provided/translated data directly into the DOM using `element.innerHTML = translation;`. This opened up potential for Cross-Site Scripting (XSS) if translations contained malicious payloads.
**Learning:** Even internal or semi-trusted data sources like translations can introduce XSS if directly injected into the DOM as HTML without sanitization, particularly when handling rich text formatting.
**Prevention:** Implement a `sanitizeHTML` function using `DOMParser` to sanitize input strings before injecting them into `innerHTML`. Restrict allowed tags and attributes strictly to what's necessary (e.g., formatting tags, safe links) and strip potentially dangerous URI schemes like `javascript:`.
