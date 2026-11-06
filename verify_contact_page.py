# Verification script for contact-us.html Webflow native template

import os
from bs4 import BeautifulSoup

def verify_contact():
    assert os.path.exists('contact-us.html'), "contact-us.html does not exist"
    
    with open('contact-us.html', 'r', encoding='utf-8') as f:
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
    assert len(bordered_titles) >= 2, f"Expected at least 2 .section-title-bordered, found {len(bordered_titles)}"
    
    corners = soup.find_all(attrs={'block-corners-top': True})
    assert len(corners) >= 2, f"Expected at least 2 block-corners-top cards, found {len(corners)}"
    
    # 4. Hero
    assert "Contact" in html or "Touch" in html or "Connect" in html, "Missing Hero title"
    
    # 5. Form & Fields
    form = soup.find('form')
    assert form is not None, "Missing contact form"
    inputs = form.find_all('input')
    textareas = form.find_all('textarea')
    assert len(inputs) >= 2, f"Expected at least 2 inputs, found {len(inputs)}"
    assert len(textareas) >= 1, "Missing textarea in form"
    
    # 6. Communication Channels / Inquiries (Emails / Discord / Telegram)
    assert "@coingpt.tech" in html or "partnerships" in html, "Missing official contact channel email"
    
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
    
    print("CONTACT PAGE VERIFICATION PASSED!")

if __name__ == '__main__':
    verify_contact()
