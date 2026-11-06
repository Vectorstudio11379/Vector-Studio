# TDD Verification Suite for Task 5: Agency Native Webflow contact-us.html

import os
from bs4 import BeautifulSoup

def test_agency_contact():
    assert os.path.exists('contact-us.html'), "contact-us.html missing"
    
    with open('contact-us.html', 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Brand & Webflow setup
    assert "Vector Studioz" in html, "Missing Vector Studioz in contact-us.html"
    assert "CoinGPT" not in html, "Found leftover CoinGPT in contact-us.html"
    for forbidden in ["on-chain", "mempool", "liquidity flow", "solidity", "validator"]:
        assert forbidden not in html.lower(), f"Found crypto forbidden phrase: {forbidden}"
        
    assert soup.find('link', href=lambda h: h and 'chain-gpt.shared' in h), "Missing Webflow shared CSS"
    body = soup.find('body')
    assert body and "landing-body" in body.get('class', []), "Body missing landing-body class"
    
    # 2. Hero
    h1 = soup.find('h1')
    assert h1 and ("Start a Project" in h1.text or "Connect" in h1.text or "Vector Studioz" in h1.text or "Contact" in h1.text), "Missing contact h1"
    
    # 3. Form & Fields
    form = soup.find('form')
    assert form is not None, "Missing contact form"
    inputs = form.find_all('input')
    textareas = form.find_all('textarea')
    selects = form.find_all('select')
    assert len(inputs) >= 2, f"Expected at least 2 inputs, found {len(inputs)}"
    assert len(textareas) >= 1, "Missing textarea in form"
    assert len(selects) >= 1, "Missing project type select in form"
    
    form_text = form.get_text()
    assert "Design" in form_text or "Software" in form_text or "AI" in form_text, "Missing agency service options in form"
    
    # 4. Studio Channels
    assert "@vectorstudioz.com" in html, "Missing @vectorstudioz.com contact email"
    
    # 5. Cut Corners & FAQ
    corners = soup.find_all(attrs={'block-corners-top': True})
    assert len(corners) >= 2, "Missing block-corners-top cut corners"
    
    faqs = soup.find_all(class_='faq-2')
    assert len(faqs) >= 4, f"Expected at least 4 FAQs, found {len(faqs)}"
    
    # 6. Bottom Rainbow CTA Banner
    banner = soup.find(class_='cta-banner-wrapper') or soup.find(class_='cta-banner')
    assert banner is not None, "Missing bottom CTA banner"
    cta_btn = banner.find(class_='btn-primary')
    assert cta_btn is not None, "Missing .btn-primary CTA in banner"
    
    print("AGENCY CONTACT PAGE VERIFICATION PASSED!")

if __name__ == '__main__':
    test_agency_contact()
