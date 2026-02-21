# Sentinel's Journal

## 2025-02-19 - Content Security Policy Hardening
**Vulnerability:** The application used `script-src 'self' 'unsafe-inline'` in its Content Security Policy (CSP). This allows the execution of inline scripts and inline event handlers, which significantly increases the risk of Cross-Site Scripting (XSS) attacks if an attacker can inject malicious HTML.
**Learning:** Even in static sites without backend processing, DOM-based XSS is possible. Using `'unsafe-inline'` negates much of the protection CSP offers.
**Prevention:** Moved the critical inline theme initialization script to a separate file (`assets/js/theme-init.js`) and removed `'unsafe-inline'` from the `script-src` directive. This enforces that only scripts from the same origin (hosted files) can execute, blocking any injected inline scripts.
