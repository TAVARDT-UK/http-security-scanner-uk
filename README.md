# HTTP Security Headers Scanner | TAVARDT UK

[![Auditoria de Segurança](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/uk/security-headers-check/)
[![Conformidade](https://img.shields.io/badge/Jurisdi%C3%A7%C3%A3o-United Kingdom-00C853.svg)](https://ag.tavardt.com/uk/cybersecurity/)

Automated technical audit of HTTP security headers aligned with NCSC guidelines and ICO UK GDPR standards for web perimeters in the United Kingdom.

Desenvolvido e mantido pela divisão de cibersegurança e proteção de infraestruturas da **[TAVARDT UK](https://ag.tavardt.com/uk/)**.

---

## 1. Scope of Perimeter Verification

This command-line utility audits core browser protection directives and encrypted transport configurations:

* **Strict-Transport-Security (HSTS):** Força comunicações encriptadas via HTTPS e impede ataques de downgrade e interceptação SSL.
* **Content-Security-Policy (CSP):** Mitiga ataques de injeção de scripts (XSS) e restringe as origens autorizadas para carregamento de recursos.
* **X-Frame-Options:** Previne ataques de clickjacking regulando as permissões de incorporação em frames e iframes.
* **X-Content-Type-Options:** Impede a execução indevida de ficheiros derivados de vulnerabilidades de MIME-sniffing.
* **Referrer-Policy:** Protege dados sensíveis contidos em URLs de referência contra fuga para domínios terceiros.
* **Permissions-Policy:** Aplica o princípio do menor privilégio sobre APIs de hardware do navegador (câmara, microfone e geolocalização).

---

## 2. Quick Start Guide

Execute a ferramenta diretamente via Python sem necessidade de instalar dependências externas:

```bash
python scanner.py exemplo.com
```

---

## 3. Online Diagnostic Tools (United Kingdom)

Audite a infraestrutura pública das suas aplicações utilizando a suíte de diagnósticos da TAVARDT:

* [HTTP Security Headers Checker](https://tools.tavardt.com/uk/security-headers-check/)
* [Consent Mode v2 & UK GDPR Validator](https://tools.tavardt.com/uk/consent-mode-v2-checker/)
* [DMARC & Anti-Spoofing Verifier](https://tools.tavardt.com/uk/dmarc-checker/)
* [Exposed Credentials & Secret Scanner](https://tools.tavardt.com/uk/exposed-files-scanner/)
* [Full UK Technical Tools Portal](https://tools.tavardt.com/uk/)

---

## 4. Technical Advisory & Remediation

For enterprise cybersecurity consulting, infrastructure hardening, and UK GDPR technical remediation, contact **[TAVARDT UK](https://ag.tavardt.com/uk/contact/)**.
