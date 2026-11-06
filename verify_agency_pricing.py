# TDD Verification Suite for Task 2: Agency Native Webflow pricing.html

import os
from bs4 import BeautifulSoup

def test_agency_pricing():
    assert os.path.exists('pricing.html'), "pricing.html missing"
    
    with open('pricing.html', 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Brand & Webflow setup
    assert "Vector Studioz" in html, "Missing Vector Studioz in pricing.html"
    assert "CoinGPT" not in html, "Found leftover CoinGPT in pricing.html"
    for forbidden in ["on-chain", "token equity", "mempool", "liquidity flow"]:
        assert forbidden not in html.lower(), f"Found crypto forbidden phrase: {forbidden}"
        
    assert soup.find('link', href=lambda h: h and 'chain-gpt.shared' in h), "Missing Webflow shared CSS"
    body = soup.find('body')
    assert body and "landing-body" in body.get('class', []), "Body missing landing-body class"
    
    # 2. Hero & Agency Engagement Tiers
    h1 = soup.find('h1')
    assert h1 and ("Pricing" in h1.text or "Models" in h1.text or "Engage" in h1.text), "Missing pricing h1"
    
    tiers = soup.find_all(class_='pricing-card') or soup.find_all(class_='pricing-tier')
    assert len(tiers) >= 3, f"Expected at least 3 pricing tiers, found {len(tiers)}"
    
    tier_text = " ".join([t.get_text() for t in tiers])
    assert "Sprint" in tier_text or "Design" in tier_text, "Missing Design Sprint tier"
    assert "Dedicated" in tier_text or "Retainer" in tier_text, "Missing Dedicated Team / Retainer tier"
    assert "Enterprise" in tier_text or "Custom" in tier_text, "Missing Enterprise Custom tier"
    
    # 3. Cut corners & badges
    corners = soup.find_all(attrs={'block-corners-top': True})
    assert len(corners) >= 3, "Missing block-corners-top cut corners"
    
    badges = soup.find_all(class_='section-title-bordered')
    assert len(badges) >= 2, "Missing .section-title-bordered badges"
    
    # 4. Agency Scope FAQs
    faqs = soup.find_all(class_='faq-2')
    assert len(faqs) >= 4, f"Expected at least 4 FAQs, found {len(faqs)}"
    faq_text = " ".join([f.get_text() for f in faqs])
    assert "IP" in faq_text or "ownership" in faq_text.lower(), "Missing IP ownership FAQ"
    
    # 5. Bottom CTA Banner with .btn-primary
    banner = soup.find(class_='cta-banner-wrapper') or soup.find(class_='cta-banner')
    assert banner is not None, "Missing bottom CTA banner"
    cta_btn = banner.find(class_='btn-primary')
    assert cta_btn is not None, "Missing .btn-primary CTA in banner"
    
    print("AGENCY PRICING PAGE VERIFICATION PASSED!")

if __name__ == '__main__':
    test_agency_pricing()
