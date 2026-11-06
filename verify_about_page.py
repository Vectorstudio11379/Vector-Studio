# Verification script for about.html Webflow native template

import os
from bs4 import BeautifulSoup

def verify_about():
    assert os.path.exists('about.html'), "about.html does not exist"
    
    with open('about.html', 'r', encoding='utf-8') as f:
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
    
    # 4. Hero & Stats
    assert "Architecting Autonomous Web3 Intelligence" in html or "About CoinGPT" in html, "Missing Hero title"
    assert "Volume Analyzed" in html, "Missing stats in Hero"
    assert "99.98%" in html, "Missing uptime stat"
    
    # 5. Mission Pillars Bento (4 pillars)
    assert "Autonomous DeFi" in html or "DeFi Trading" in html, "Missing Mission Pillar 1"
    assert "Security Audits" in html or "Smart Contract" in html, "Missing Mission Pillar 2"
    
    # 6. Leadership / Team Section
    assert "Leadership" in html or "Core Team" in html, "Missing leadership section"
    assert "Chief AI Scientist" in html or "Head of" in html, "Missing leadership role"
    
    # 7. FAQ Accordion
    faqs = soup.find_all(class_='faq-2')
    assert len(faqs) >= 4, f"Expected at least 4 .faq-2 items, found {len(faqs)}"
    
    # 8. Bottom CTA Banner with .btn-primary
    banner = soup.find(class_='cta-banner-wrapper') or soup.find(class_='cta-wrapper')
    assert banner is not None, "Missing bottom CTA banner wrapper"
    banner_btn = banner.find(class_='btn-primary')
    assert banner_btn is not None, "Bottom CTA banner missing .btn-primary button"
    
    # 9. Footer
    footer = soup.find('footer')
    assert footer is not None, "Missing footer"
    assert "CoinGPT" in footer.text, "Footer missing CoinGPT text"
    
    print("ABOUT PAGE VERIFICATION PASSED!")

if __name__ == '__main__':
    verify_about()
