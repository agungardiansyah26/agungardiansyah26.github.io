# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2024-05-24 - DOM XSS in Translation Injection
**Vulnerability:** Cross-Site Scripting (XSS) vulnerability during translation insertion where user-controlled translation JSON was inserted directly using `innerHTML` without sanitization.
**Learning:** In client-side translation systems, injecting translations directly to `innerHTML` exposes the application to DOM-based XSS if the translation source is compromised or if it reflects unsanitized user input. Using native `DOMParser` provides a way to parse and clean the HTML string before injection in vanilla JS without adding heavy external dependencies like DOMPurify.
**Prevention:** Always sanitize any dynamic content that will be injected into the DOM via `innerHTML` or similar unsafe sinks. Use a whitelist-based approach to allow only specific safe HTML tags and attributes (e.g., stripping `javascript:` URLs in `href`).
