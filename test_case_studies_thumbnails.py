import os
import re
from bs4 import BeautifulSoup

def test_case_studies_thumbnails():
    # 1. Check vector-nav.css for 16:9 widescreen rules
    assert os.path.exists('vector-nav.css'), "vector-nav.css missing"
    with open('vector-nav.css', 'r', encoding='utf-8') as f:
        css = f.read()

    assert 'case-item-image-wrapper' in css, "Missing case-item-image-wrapper in vector-nav.css"
    assert '16 / 9' in css or '16/9' in css, "Missing 16:9 aspect ratio in vector-nav.css"
    assert 'object-fit: cover' in css or 'object-fit:cover' in css, "Missing object-fit: cover in vector-nav.css"

    # 2. Check case-studies.html exists and is clean of crypto
    assert os.path.exists('case-studies.html'), "case-studies.html missing"
    with open('case-studies.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    forbidden_crypto = ['leonis ai', 'chaingpt', 'coingpt', 'unibase', 'smartsentinels', 'flipper cut']
    html_lower = html.lower()
    for f in forbidden_crypto:
        assert f not in html_lower, f"case-studies.html contains forbidden crypto term: {f}"

    # 3. Check for 10 real client case studies
    expected_projects = [
        'Beacon Corporate Realty',
        'JumboDTG',
        'Resilient Solutions',
        'Mirola Enterprises',
        'MIRODATA',
        'Cleaner Spaces',
        '5th Element Media Group',
        'Operational Excellence',
        'Aliola Global Services',
        'Tom Ojo Sports Academy'
    ]

    for p in expected_projects:
        assert p in html, f"Missing project '{p}' in case-studies.html"

    # 4. Check for 16:9 widescreen image wrappers in case-studies.html
    images = soup.find_all('img', src=lambda s: s and 'images/case-studies/' in s)
    assert len(images) >= 10, f"Expected at least 10 case study images in case-studies.html, found {len(images)}"

    # 5. Check index.html case slider
    with open('index.html', 'r', encoding='utf-8') as f:
        index_html = f.read()
    for p in expected_projects:
        assert p in index_html, f"Missing project '{p}' in index.html"

    print("ALL CASE STUDY THUMBNAIL AND PAGE TESTS PASSED!")

if __name__ == '__main__':
    test_case_studies_thumbnails()
