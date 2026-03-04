# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.
## 2024-05-23 - XSS Prevention in Translation Updates
**Vulnerability:** The translation system updated elements' `innerHTML` with unsanitized text from `data-i18n` attributes. Although translations are currently loaded from a static `.js` file, dynamically loaded translations or maliciously modified global state could lead to XSS execution.
**Learning:** Using `innerHTML` requires explicit sanitization, especially when rendering external or potentially untrusted content.
**Prevention:** Added a `sanitizeHTML` function that uses `DOMParser` to parse HTML strings, recursively unwraps disallowed tags (leaving only safe formatting tags like `SPAN`, `STRONG`, `EM`, `B`, `I`, `BR`, `P`, `A`), and removes disallowed attributes or malicious values (like stripping control characters in `href` and `src` to prevent HTML entity bypasses). This function is called before assigning to `innerHTML`.
