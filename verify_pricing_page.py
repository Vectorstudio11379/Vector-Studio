from bs4 import BeautifulSoup
import sys

def test_pricing():
    with open('pricing.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # 1. Check Webflow classes & head
    assert soup.find('link', href=lambda h: h and 'chain-gpt.shared' in h), "Missing Webflow shared CSS in head"
    assert soup.find(class_='vs-navbar') or soup.find('header'), "Missing header"
    assert soup.find(class_='site-footer') or soup.find('footer'), "Missing footer"
    
    # 2. Check Hero section badge & title
    badge = soup.find(class_='section-title-bordered')
    assert badge is not None, "Missing .section-title-bordered badge in hero"
    h1 = soup.find('h1')
    assert h1 is not None, "Missing H1 headline"
    assert "Pricing" in h1.get_text() or "Plans" in h1.get_text(), f"H1 does not mention Pricing/Plans: {h1.get_text()}"
    
    # 3. Check Webflow cut-corner blocks
    corner_blocks = soup.find_all(attrs={"block-corners-top": True}) or soup.find_all(attrs={"block-corners-bottom": True})
    assert len(corner_blocks) > 0, "Missing [block-corners-top] or [block-corners-bottom] cut-corner blocks"
    
    # 4. Check Pricing tiers
    pricing_cards = soup.find_all(class_='pricing-card') or soup.find_all(class_='pricing-tier') or soup.find_all(class_='plan-card')
    assert len(pricing_cards) >= 3, f"Expected at least 3 pricing cards, found {len(pricing_cards)}"
    
    # 5. Check FAQ accordion
    faq_items = soup.find_all(class_='faq-2') or soup.find_all(class_='miscellaneous-2') or soup.find_all(class_='faq-item')
    assert len(faq_items) >= 4, f"Expected at least 4 FAQ items, found {len(faq_items)}"
    
    # 6. Check CTA button .btn-primary
    btn_primaries = soup.find_all(class_='btn-primary')
    assert len(btn_primaries) >= 2, f"Expected multiple .btn-primary buttons, found {len(btn_primaries)}"
    
    print("PRICING PAGE VERIFICATION PASSED!")

if __name__ == '__main__':
    try:
        test_pricing()
        sys.exit(0)
    except AssertionError as e:
        print(f"TEST FAILED (RED): {e}")
        sys.exit(1)
