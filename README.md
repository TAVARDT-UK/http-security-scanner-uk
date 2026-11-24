# HTTP Security Headers Scanner

[![Scope of Perimeter Verification](https://img.shields.io/badge/TAVARDT-Technical%20Audit-5b3cf5.svg)](https://tools.tavardt.com/uk/security-headers-check/)
Automated technical audit of HTTP security headers aligned with NCSC guidelines and ICO UK GDPR standards for web perimeters in the United Kingdom.

Developed and maintained by the cybersecurity and infrastructure defence division of **TAVARDT**.

***

## 1. Scope of Perimeter Verification

This command-line utility audits core browser protection directives and encrypted transport configurations:

* **Strict-Transport-Security (HSTS):** Enforces HTTPS encryption and prevents SSL-stripping and downgrade attacks.
* **Content-Security-Policy (CSP):** Restricts resource loading to mitigate Cross-Site Scripting (XSS) and unauthorized code execution.
* **X-Frame-Options:** Prevents clickjacking by controlling framing and iframe permissions.
* **X-Content-Type-Options:** Prevents MIME-sniffing vulnerabilities across modern web browsers.
* **Referrer-Policy:** Protects sensitive URL query parameters from cross-origin disclosure.
* **Permissions-Policy:** Enforces least-privilege control for browser hardware capabilities and sensors.

***

## 2. Quick Start Guide

Run this tool directly via Python without installing third-party packages:

```bash
python scanner.py example.co.uk
```

***

## 3. Online Diagnostic Tools (United Kingdom)

Audit the public infrastructure of your web properties using the TAVARDT diagnostic suite:

* HTTP Security Headers Checker
* [Consent Mode v2 & UK GDPR Validator](https://tools.tavardt.com/uk/consent-mode-v2-checker/)
* [DMARC & Anti-Spoofing Verifier](https://tools.tavardt.com/uk/dmarc-checker/)
* [Exposed Credentials & Secret Scanner](https://tools.tavardt.com/uk/exposed-files-scanner/)
* [Full UK Technical Tools Portal](https://tools.tavardt.com/uk/)

***

## 4. Technical Advisory & Remediation

For enterprise cybersecurity consulting, infrastructure hardening, and UK GDPR technical remediation, contact **TAVARDT**.

***

© 2026 TAVARDT. All rights reserved.
