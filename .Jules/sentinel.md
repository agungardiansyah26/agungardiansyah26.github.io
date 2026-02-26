# Sentinel's Journal

## 2024-05-23 - Inline Script CSP Handling
**Vulnerability:** Content Security Policy (CSP) allowed `'unsafe-inline'` for `script-src`, enabling potential XSS attacks.
**Learning:** The inline script in `index.html` handles theme initialization to prevent Flash of Incorrect Theme (FOUC). It cannot be easily moved to an external file without impacting UX.
**Prevention:** Calculate the SHA-256 hash of the inline script and add it to the `script-src` directive in the CSP meta tag. This allows the necessary inline script while blocking all other unauthorized inline scripts.

## 2024-05-23 - DOM-based XSS in Translation System
**Vulnerability:** The translation system used `innerHTML` to inject content from `translations.js` directly into the DOM without sanitization. While the source file is local, this pattern is dangerous if the source ever becomes dynamic or untrusted.
**Learning:** Initial sanitization attempts using top-down traversal (processing parent before children) are vulnerable to bypasses. If a sanitizer strips a parent tag (like `<div>`) but "unwraps" its children (keeps them), it might inadvertently promote malicious children (like `<img onerror>`) to a level where they are no longer checked by the loop, as the loop iterator might have already passed their new position or relies on a static snapshot of nodes.
**Prevention:** Implement a `sanitizeHTML` function using **bottom-up recursion**. Recursively clean the children of a node *before* deciding whether to keep or strip the node itself. This ensures that any content promoted by unwrapping has already been sanitized.
