#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Enforces HTTPS encryption and prevents SSL-stripping (HSTS).'), ('Content-Security-Policy', 'Restricts resource loading to mitigate Cross-Site Scripting (XSS).'), ('X-Frame-Options', 'Mitigates clickjacking attacks by managing frame embedding rules.'), ('X-Content-Type-Options', 'Prevents MIME-sniffing vulnerabilities in client browsers.'), ('Referrer-Policy', 'Controls referrer metadata leakage across external origins.'), ('Permissions-Policy', 'Applies least-privilege control to browser hardware interfaces.')]

def scan_target(target_url):
    print(f"\n[TAVARDT UK] Starting HTTP security headers perimeter audit for: {target_url}\n")
    try:
        req = urllib.request.Request(
            target_url,
            headers={"User-Agent": "TAVARDT-Security-Scanner/3.0 (en-GB)"}
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            headers = dict(response.headers.items())
            
            score = 0
            total = len(SECURITY_HEADERS)
            
            for header_name, desc in SECURITY_HEADERS:
                found = any(h.lower() == header_name.lower() for h in headers.keys())
                if found:
                    print(f"  [PASS] {header_name}")
                    score += 1
                else:
                    print(f"  [FAIL] {header_name}: {desc}")
                    
            print(f"\n[TAVARDT UK] Audit Score: {score}/{total}")
            print(f"\nVerificacao completa online: https://tools.tavardt.com/uk/security-headers-check/")
            print(f"Suporte corporativo e ciberdefesa: https://ag.tavardt.com/uk/cybersecurity/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT UK] Erro ao inspecionar o alvo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
