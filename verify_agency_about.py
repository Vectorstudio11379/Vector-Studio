# TDD Verification Suite for Task 3: Agency Native Webflow about.html

import os
from bs4 import BeautifulSoup

def test_agency_about():
    assert os.path.exists('about.html'), "about.html missing"
    
    with open('about.html', 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Brand & Webflow setup
    assert "Vector Studioz" in html, "Missing Vector Studioz in about.html"
    assert "CoinGPT" not in html, "Found leftover CoinGPT in about.html"
    for forbidden in ["on-chain", "mempool", "liquidity flow", "smart contract audit", "validator"]:
        assert forbidden not in html.lower(), f"Found crypto forbidden phrase: {forbidden}"
        
    assert soup.find('link', href=lambda h: h and 'chain-gpt.shared' in h), "Missing Webflow shared CSS"
    body = soup.find('body')
    assert body and "landing-body" in body.get('class', []), "Body missing landing-body class"
    
    # 2. Hero & Stats
    h1 = soup.find('h1')
    assert h1 and ("Define Categories" in h1.text or "Digital Experiences" in h1.text or "Vector Studioz" in h1.text), "Missing about h1"
    assert "140+" in html, "Missing 140+ projects delivered stat"
    assert "99.2%" in html, "Missing 99.2% retention stat"
    
    # 3. Agency Craft Pillars (4 bento cards)
    pillars = soup.find_all(class_='pillar-card')
    assert len(pillars) >= 4, f"Expected at least 4 craft pillars, found {len(pillars)}"
    pillar_text = " ".join([p.get_text() for p in pillars])
    assert "Visual Excellence" in pillar_text or "Design" in pillar_text, "Missing visual excellence pillar"
    assert "Architecture" in pillar_text or "Engineering" in pillar_text, "Missing scalable architecture pillar"
    assert "AI" in pillar_text or "Automation" in pillar_text, "Missing AI automation pillar"
    
    # 4. Leadership Team
    team = soup.find_all(class_='team-card')
    assert len(team) >= 1, f"Expected leadership card, found {len(team)}"
    team_text = " ".join([t.get_text() for t in team])
    assert "Elijah Ezekiel" in team_text, "Missing Elijah Ezekiel in leadership"
    assert "Creative" in team_text or "Founder" in team_text, "Missing agency leadership roles"
    
    # 5. FAQ Accordion & Cut Corners
    faqs = soup.find_all(class_='faq-2')
    assert len(faqs) >= 4, f"Expected at least 4 FAQs, found {len(faqs)}"
    
    corners = soup.find_all(attrs={'block-corners-top': True})
    assert len(corners) >= 3, "Missing block-corners-top cut corners"
    
    # 6. Bottom Rainbow CTA Banner
    banner = soup.find(class_='cta-banner-wrapper') or soup.find(class_='cta-banner')
    assert banner is not None, "Missing bottom CTA banner"
    cta_btn = banner.find(class_='btn-primary')
    assert cta_btn is not None, "Missing .btn-primary CTA in banner"
    
    print("AGENCY ABOUT PAGE VERIFICATION PASSED!")

if __name__ == '__main__':
    test_agency_about()
