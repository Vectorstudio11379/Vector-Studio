# Verification script for universal header & footer synchronization across all 24 pages for Vector Studioz

import glob
from bs4 import BeautifulSoup

USER_PAGES = [
    f for f in glob.glob('*.html') 
    if f not in ['template_header.html', 'template_footer.html', 'navbar_current.html']
]

def verify_all_pages():
    print(f"Auditing {len(USER_PAGES)} pages for Vector Studioz branding...")
    assert len(USER_PAGES) >= 24, f"Expected at least 24 user-facing pages, found {len(USER_PAGES)}"
    
    failed_header = []
    failed_cta = []
    failed_footer = []
    failed_icons = []
    failed_coingpt = []
    failed_css = []
    
    for page in sorted(USER_PAGES):
        with open(page, 'r', encoding='utf-8') as f:
            html = f.read()
            soup = BeautifulSoup(html, 'html.parser')
            
        header = soup.find('header')
        if not header or "Vector Studioz" not in header.get_text():
            failed_header.append(page)
            continue
            
        if "CoinGPT" in header.get_text():
            failed_coingpt.append(page)
            
        icons = header.find_all(class_='vs-dropdown-icon')
        if len(icons) > 0:
            failed_icons.append(page)
            
        btn = header.find(class_='btn-primary')
        if not btn or not btn.find(class_='btn-primary-text'):
            failed_cta.append(page)
        elif page != 'index.html' and "SUBMIT PROJECT BRIEF" not in btn.get_text():
            failed_cta.append(page)
        elif page == 'index.html' and "SUBMIT PROJECT BRIEF" not in btn.get_text() and "Start a Project" not in btn.get_text():
            failed_cta.append(page)
            
        footer = soup.find('footer')
        if not footer or "Vector Studioz" not in footer.get_text() or "CoinGPT" in footer.get_text():
            failed_footer.append(page)
            
        head = soup.find('head')
        if not head or not head.find('link', href=lambda h: h and 'vector-nav.css' in h):
            failed_css.append(page)
            
    assert not failed_header, f"Header branding missing Vector Studioz in: {failed_header}"
    assert not failed_coingpt, f"Leftover CoinGPT found in header in: {failed_coingpt}"
    assert not failed_icons, f"Green icon containers (.vs-dropdown-icon) found in header in: {failed_icons}"
    assert not failed_cta, f"Header CTA button invalid in: {failed_cta}"
    assert not failed_footer, f"Footer missing Vector Studioz or contains CoinGPT in: {failed_footer}"
    assert not failed_css, f"Head missing vector-nav.css in: {failed_css}"
    
    print("ALL 24 PAGES SUCCESSFULLY SYNCHRONIZED AND VERIFIED FOR VECTOR STUDIOZ!")

if __name__ == '__main__':
    verify_all_pages()
