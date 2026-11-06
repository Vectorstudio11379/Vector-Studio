# Verification script for careers.html Webflow native template

import os
from bs4 import BeautifulSoup

def verify_careers():
    assert os.path.exists('careers.html'), "careers.html does not exist"
    
    with open('careers.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Header & Brand Logo
    assert "CoinGPT" in html, "Missing CoinGPT brand name"
    header = soup.find('header')
    assert header is not None, "Missing header"
    logo_text = header.find(class_='vs-brand-text') or header.find(class_='brand-text')
    assert logo_text and "CoinGPT" in logo_text.text, "Header brand text not CoinGPT"
    
    # CTA in header
    btn_primary = header.find(class_='btn-primary')
    assert btn_primary is not None, "Header missing native .btn-primary CTA"
    
    # 2. Webflow stylesheet & body class
    assert "chain-gpt.shared" in html, "Missing Webflow shared stylesheet"
    body = soup.find('body')
    assert body is not None and "landing-body" in body.get('class', []), "Body missing landing-body class"
    
    # 3. Section Title Bordered & Block corners
    bordered_titles = soup.find_all(class_='section-title-bordered')
    assert len(bordered_titles) >= 3, f"Expected at least 3 .section-title-bordered, found {len(bordered_titles)}"
    
    corners = soup.find_all(attrs={'block-corners-top': True})
    assert len(corners) >= 3, f"Expected at least 3 block-corners-top cards, found {len(corners)}"
    
    # 4. Hero
    assert "Careers" in html or "Join" in html, "Missing Hero title"
    html_lower = html.lower()
    assert "autonomous web3 intelligence" in html_lower or "next-gen ai" in html_lower or "decentralized" in html_lower, "Missing hero description context"
    
    # 5. Open Roles (at least 4 open positions)
    role_cards = soup.find_all(class_='role-card')
    assert len(role_cards) >= 4, f"Expected at least 4 role cards, found {len(role_cards)}"
    
    # 6. Hiring Pipeline / Stages (at least 4 steps)
    steps = soup.find_all(class_='pipeline-step') or soup.find_all(class_='stage-card')
    assert len(steps) >= 4, f"Expected at least 4 hiring process steps, found {len(steps)}"
    
    # 7. Perks / Benefits
    assert "Perks" in html or "Benefits" in html, "Missing perks/benefits section"
    
    # 8. FAQ Accordion
    faqs = soup.find_all(class_='faq-2')
    assert len(faqs) >= 4, f"Expected at least 4 .faq-2 items, found {len(faqs)}"
    
    # 9. Bottom CTA Banner with .btn-primary
    banner = soup.find(class_='cta-banner-wrapper') or soup.find(class_='cta-wrapper')
    assert banner is not None, "Missing bottom CTA banner wrapper"
    banner_btn = banner.find(class_='btn-primary')
    assert banner_btn is not None, "Bottom CTA banner missing .btn-primary button"
    
    # 10. Footer
    footer = soup.find('footer')
    assert footer is not None, "Missing footer"
    assert "CoinGPT" in footer.text, "Footer missing CoinGPT text"
    
    print("CAREERS PAGE VERIFICATION PASSED!")

if __name__ == '__main__':
    verify_careers()
