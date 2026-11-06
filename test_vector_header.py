# TDD Verification Suite for Task 1: Vector Studioz Header, Clean Menu & Rainbow CTA

import os
from bs4 import BeautifulSoup

def test_vector_header_components():
    assert os.path.exists('template_header.html'), "template_header.html missing"
    assert os.path.exists('template_footer.html'), "template_footer.html missing"
    assert os.path.exists('vector-nav.css'), "vector-nav.css missing"

    with open('template_header.html', 'r', encoding='utf-8') as f:
        header_html = f.read()
    soup_header = BeautifulSoup(header_html, 'html.parser')

    # 1. Brand Identity
    assert "CoinGPT" not in header_html, "Found leftover CoinGPT in header"
    assert "Vector Studioz" in header_html, "Missing Vector Studioz brand text in header"
    brand_elem = soup_header.find(class_='vs-brand-text') or soup_header.find(class_='vs-brand')
    assert brand_elem is not None and "Vector Studioz" in brand_elem.get_text(), "Brand element text not Vector Studioz"

    # 2. Clean Menu (No green icon containers)
    icon_boxes = soup_header.find_all(class_='vs-dropdown-icon')
    assert len(icon_boxes) == 0, f"Expected 0 .vs-dropdown-icon elements, found {len(icon_boxes)}"

    # 3. Agency Services Menu Items
    menu_text = soup_header.get_text()
    assert "Web Design" in menu_text or "UI/UX" in menu_text, "Missing Web Design in services menu"
    assert "Development" in menu_text or "Software" in menu_text, "Missing Software/Development in services menu"
    assert "AI Automation" in menu_text, "Missing AI Automation in services menu"
    assert "3D" in menu_text or "WebGL" in menu_text, "Missing 3D/WebGL in services menu"

    # 4. Zero Crypto Terms
    crypto_terms = ["Trading Assistant", "Smart Contract Auditor", "Market Alerts", "Compliance Assistant", "CoinGPT"]
    for term in crypto_terms:
        assert term not in header_html, f"Found crypto term '{term}' in header"

    # 5. Rainbow CTA Button
    btn = soup_header.find(class_='btn-primary')
    assert btn is not None, "Missing .btn-primary CTA button in header"
    btn_text = btn.find(class_='btn-primary-text')
    assert btn_text is not None, "Missing .btn-primary-text in CTA button"
    assert "SUBMIT PROJECT BRIEF" in btn_text.get_text() or "Start a Project" in btn_text.get_text() or "Book a Call" in btn_text.get_text(), f"Unexpected CTA text: {btn_text.get_text()}"

    # 6. Rainbow CSS in vector-nav.css
    with open('vector-nav.css', 'r', encoding='utf-8') as f:
        css = f.read()
    assert "#ff007a" in css or "rainbow" in css or "#ff3366" in css or "#7928ca" in css, "Missing rainbow spectrum colors in vector-nav.css"

    # 7. Vector Studioz Footer
    with open('template_footer.html', 'r', encoding='utf-8') as f:
        footer_html = f.read()
    assert "Vector Studioz" in footer_html, "Missing Vector Studioz in template_footer.html"
    assert "CoinGPT" not in footer_html, "Found leftover CoinGPT in footer"

    print("ALL VECTOR STUDIOZ HEADER & FOOTER TESTS PASSED!")

if __name__ == '__main__':
    test_vector_header_components()
