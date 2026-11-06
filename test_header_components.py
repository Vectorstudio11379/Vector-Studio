from bs4 import BeautifulSoup
import sys

def test_header():
    with open('template_header.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Check brand text
    brand = soup.find(class_='vs-brand') or soup.find(class_='w-nav-brand')
    assert brand is not None, "Brand link not found in header"
    assert "CoinGPT" in brand.get_text(), f"Brand text does not contain CoinGPT: {brand.get_text()}"
    
    # Check logo svg gradients
    svg = brand.find('svg')
    assert svg is not None, "SVG logo not found in brand"
    svg_str = str(svg)
    assert "#00ffa3" in svg_str or "00ffa3" in svg_str, "SVG does not contain signature emerald #00ffa3"
    assert "#28efce" in svg_str or "28efce" in svg_str, "SVG does not contain signature cyan #28efce"
    
    # Check default .btn-primary CTA button
    btn = soup.find('a', class_='btn-primary')
    assert btn is not None, "Header does not contain .btn-primary CTA button"
    assert btn.find(class_='btn-primary-lines-1') is not None, "Missing .btn-primary-lines-1"
    assert btn.find(class_='btn-primary-lines-2') is not None, "Missing .btn-primary-lines-2"
    assert btn.find(class_='btn-primary-text') is not None, "Missing .btn-primary-text"
    
    # Check footer
    with open('template_footer.html', 'r', encoding='utf-8') as f:
        footer_soup = BeautifulSoup(f.read(), 'html.parser')
    assert "CoinGPT" in footer_soup.get_text(), "Footer does not contain CoinGPT branding"
    
    print("ALL HEADER & FOOTER TESTS PASSED!")

if __name__ == '__main__':
    try:
        test_header()
        sys.exit(0)
    except AssertionError as e:
        print(f"TEST FAILED (RED): {e}")
        sys.exit(1)
