# TDD Verification Suite for Task 4: Agency Native Webflow careers.html

import os
from bs4 import BeautifulSoup

def test_agency_careers():
    assert os.path.exists('careers.html'), "careers.html missing"
    
    with open('careers.html', 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Brand & Webflow setup
    assert "Vector Studioz" in html, "Missing Vector Studioz in careers.html"
    assert "CoinGPT" not in html, "Found leftover CoinGPT in careers.html"
    for forbidden in ["on-chain", "mempool", "liquidity flow", "solidity", "validator"]:
        assert forbidden not in html.lower(), f"Found crypto forbidden phrase: {forbidden}"
        
    assert soup.find('link', href=lambda h: h and 'chain-gpt.shared' in h), "Missing Webflow shared CSS"
    body = soup.find('body')
    assert body and "landing-body" in body.get('class', []), "Body missing landing-body class"
    
    # 2. Hero & Culture
    h1 = soup.find('h1')
    assert h1 and ("Careers" in h1.text or "Vanguard" in h1.text or "Join" in h1.text), "Missing careers h1"
    
    # 3. Open Roles
    roles = soup.find_all(class_='role-card')
    assert len(roles) >= 4, f"Expected at least 4 role cards, found {len(roles)}"
    roles_text = " ".join([r.get_text() for r in roles])
    assert "Designer" in roles_text or "UI/UX" in roles_text, "Missing Designer role"
    assert "Full-Stack" in roles_text or "Engineer" in roles_text, "Missing Engineer role"
    assert "AI" in roles_text, "Missing AI role"
    
    # 4. Hiring Pipeline & Perks
    steps = soup.find_all(class_='pipeline-step') or soup.find_all(class_='stage-card')
    assert len(steps) >= 4, f"Expected at least 4 hiring process steps, found {len(steps)}"
    
    perks = soup.find_all(class_='perk-card')
    assert len(perks) >= 4, f"Expected at least 4 perk cards, found {len(perks)}"
    
    # 5. Cut Corners & FAQ
    corners = soup.find_all(attrs={'block-corners-top': True})
    assert len(corners) >= 3, "Missing block-corners-top cut corners"
    
    faqs = soup.find_all(class_='faq-2')
    assert len(faqs) >= 4, f"Expected at least 4 FAQs, found {len(faqs)}"
    
    # 6. Bottom Rainbow CTA Banner
    banner = soup.find(class_='cta-banner-wrapper') or soup.find(class_='cta-banner')
    assert banner is not None, "Missing bottom CTA banner"
    cta_btn = banner.find(class_='btn-primary')
    assert cta_btn is not None, "Missing .btn-primary CTA in banner"
    
    print("AGENCY CAREERS PAGE VERIFICATION PASSED!")

if __name__ == '__main__':
    test_agency_careers()
