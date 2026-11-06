# TDD Verification Suite for Vector Studioz 6 Agency Service Pages

import os
from bs4 import BeautifulSoup

CLEAN_SERVICE_PAGES = [
    ('web-design.html', 'Web Design'),
    ('web-development.html', 'Web Development'),
    ('software-engineering.html', 'Software Engineering'),
    ('ai-automation.html', 'AI Automation'),
    ('webgl-3d.html', '3D & WebGL'),
    ('mobile-development.html', 'Mobile App Development')
]

LEGACY_SERVICE_PAGES = [
    ('ai-agents.html', 'Web Design (Legacy)'),
    ('ai-trading-assistant.html', 'Web Development (Legacy)'),
    ('smart-contract-auditor.html', 'Software Engineering (Legacy)'),
    ('crypto-ai-hub.html', 'AI Automation (Legacy)'),
    ('web3-chatbot.html', '3D & WebGL (Legacy)'),
    ('smart-contract-generator.html', 'Mobile App Development (Legacy)')
]

FORBIDDEN_CRYPTO = [
    "coingpt", "mempool", "liquidity flow", "solidity", "on-chain", 
    "smart contract audit", "trading assistant", "token equity", "validator node"
]

def test_agency_service_pages():
    # 1. Check header links in template_header.html
    assert os.path.exists('template_header.html'), "template_header.html missing"
    with open('template_header.html', 'r', encoding='utf-8') as f:
        header_html = f.read()
    
    for filename, service_name in CLEAN_SERVICE_PAGES:
        assert filename in header_html, f"template_header.html does not link to clean URL: {filename}"

    # 2. Check each clean and legacy service page
    for filename, service_name in CLEAN_SERVICE_PAGES + LEGACY_SERVICE_PAGES:
        assert os.path.exists(filename), f"Service page missing: {filename}"
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()
        soup = BeautifulSoup(html, 'html.parser')
        
        # Branding
        assert "Vector Studioz" in html, f"{filename} missing Vector Studioz branding"
        html_lower = html.lower()
        for forbidden in FORBIDDEN_CRYPTO:
            assert forbidden not in html_lower, f"{filename} contains forbidden crypto term '{forbidden}'"
            
        # Webflow structure
        assert soup.find('link', href=lambda h: h and 'chain-gpt.shared' in h), f"{filename} missing Webflow shared CSS"
        body = soup.find('body')
        assert body and "landing-body" in body.get('class', []), f"{filename} body missing landing-body class"
        
        # Features & FAQs
        pillars = soup.find_all(class_='pillar-card') or soup.find_all(class_='feature-card')
        assert len(pillars) >= 4, f"{filename} has fewer than 4 feature cards (found {len(pillars)})"
        
        faqs = soup.find_all(class_='faq-2')
        assert len(faqs) >= 4, f"{filename} has fewer than 4 FAQs (found {len(faqs)})"
        
        # Cut corners
        corners = soup.find_all(attrs={'block-corners-top': True})
        assert len(corners) >= 3, f"{filename} missing cut corners"
        
        # CTA button & banner
        banner = soup.find(class_='cta-banner-wrapper') or soup.find(class_='cta-banner')
        assert banner is not None, f"{filename} missing bottom CTA banner"
        btn = banner.find(class_='btn-primary')
        assert btn is not None, f"{filename} banner missing .btn-primary CTA button"

    print("ALL 6 VECTOR STUDIOZ SERVICE PAGES VERIFIED SUCCESSFULLY!")

if __name__ == '__main__':
    test_agency_service_pages()
