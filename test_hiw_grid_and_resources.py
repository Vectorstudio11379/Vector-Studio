"""
test_hiw_grid_and_resources.py
TDD verification suite asserting:
1. Resource pages (blog.html, brand-kit.html, videos.html) are completely deleted.
2. Header and footer navigation contain zero references to 'Resources'.
3. Zero absolute '/images/case-studies/' image paths across projects catalog and subpages.
4. 'How It Works' section has 2x2 grid styling override across company and service pages.
5. All 6 service pages have complete 11-section canonical Webflow landing layouts.
6. index.html SHA-256 remains 100% frozen.
"""

import os
import glob
import hashlib
from bs4 import BeautifulSoup

BASELINE_INDEX_SHA256 = '96e040f788d68ea79d1f28f58e7d0def11957a8d9779c8bc798b747a02fdced7'

SERVICE_PAGES = [
    'web-design.html',
    'webgl-3d.html',
    'web-development.html',
    'software-engineering.html',
    'ai-automation.html',
    'mobile-development.html'
]

COMPANY_PAGES = [
    'about.html',
    'careers.html',
    'contact-us.html'
]

REQUIRED_11_SECTIONS = [
    'landing-hero-2',
    'landing-why',
    'landing-features',
    'landing-who-for',
    'landing-hiw',
    'landing-comparison',
    'landing-launch',
    'landing-group',
    'landing-faq',
    'landing-cta'
]

def test_index_unmodified():
    print("1. Checking index.html baseline preservation...")
    assert os.path.exists('index.html'), "index.html missing"
    with open('index.html', 'rb') as f:
        current_hash = hashlib.sha256(f.read()).hexdigest()
    assert current_hash == BASELINE_INDEX_SHA256, (
        f"CRITICAL: index.html modified! Hash: {current_hash}"
    )
    print("   [PASS] index.html hash matches baseline.")

def test_resource_pages_deleted():
    print("2. Checking deletion of Resource pages...")
    for f in ['blog.html', 'brand-kit.html', 'videos.html']:
        assert not os.path.exists(f), f"Resource page {f} must be deleted!"
    print("   [PASS] All Resource pages (blog.html, brand-kit.html, videos.html) deleted.")

def test_navigation_resources_removed():
    print("3. Checking header & footer for removal of Resources...")
    with open('template_header.html', 'r', encoding='utf-8') as f:
        h = f.read()
    assert 'Resources' not in h, "template_header.html still references 'Resources'"
    assert 'blog.html' not in h, "template_header.html still links to blog.html"
    assert 'brand-kit.html' not in h, "template_header.html still links to brand-kit.html"
    assert 'videos.html' not in h, "template_header.html still links to videos.html"

    with open('template_footer.html', 'r', encoding='utf-8') as f:
        foot = f.read()
    assert 'Resources' not in foot, "template_footer.html still references 'Resources'"
    assert 'blog.html' not in foot, "template_footer.html still links to blog.html"
    print("   [PASS] Navigation headers and footers contain zero references to Resources.")

def test_image_paths_relative():
    print("4. Checking for broken absolute thumbnail image paths...")
    # Check projects.html and case-studies.html
    for page in ['projects.html', 'case-studies.html']:
        assert os.path.exists(page), f"{page} missing"
        soup = BeautifulSoup(open(page, encoding='utf-8'), 'html.parser')
        for img in soup.find_all('img'):
            src = img.get('src', '')
            assert not src.startswith('/images/case-studies/'), (
                f"Absolute path '{src}' found in {page}. Must be relative 'images/case-studies/'"
            )

    # Check project subpages
    for p in glob.glob('projects/*.html'):
        soup = BeautifulSoup(open(p, encoding='utf-8'), 'html.parser')
        for img in soup.find_all('img'):
            src = img.get('src', '')
            assert not src.startswith('/images/case-studies/'), (
                f"Absolute path '{src}' found in {p}. Must be relative '../images/case-studies/'"
            )
    print("   [PASS] All case study thumbnails use correct relative paths.")

def test_hiw_2x2_grid_override():
    print("5. Checking 'How It Works' 2x2 grid styling override...")
    for page in COMPANY_PAGES + SERVICE_PAGES:
        assert os.path.exists(page), f"{page} missing"
        content = open(page, encoding='utf-8').read()
        assert 'grid-template-columns: repeat(2, 1fr)' in content or 'grid-template-columns:repeat(2,1fr)' in content, (
            f"Missing 2x2 grid override 'grid-template-columns: repeat(2, 1fr)' in {page}"
        )
    print("   [PASS] All company and service pages contain the 2x2 HIW grid override.")

def test_service_pages_canonical_11_sections():
    print("6. Checking 6 service pages for 11-section canonical Webflow layout...")
    for page in SERVICE_PAGES:
        assert os.path.exists(page), f"{page} missing"
        content = open(page, encoding='utf-8').read()
        soup = BeautifulSoup(content, 'html.parser')

        sections = soup.find_all('section')
        sec_classes = [' '.join(s.get('class', [])) for s in sections]

        for req in REQUIRED_11_SECTIONS:
            assert any(req in sc for sc in sec_classes), (
                f"Missing section '{req}' in {page}. Found: {sec_classes}"
            )

        why_count = sum(1 for sc in sec_classes if 'landing-why' in sc)
        assert why_count >= 2, f"Expected at least 2 'landing-why' sections in {page}, found {why_count}"

        assert soup.find('div', class_='hero-assets-container') is not None, (
            f"Missing native Webflow '.hero-assets-container' in {page}"
        )
        print(f"   [PASS] {page} has all 11 canonical Webflow sections.")

if __name__ == '__main__':
    print("=== RUNNING TDD VERIFICATION SUITE ===")
    test_index_unmodified()
    test_resource_pages_deleted()
    test_navigation_resources_removed()
    test_image_paths_relative()
    test_hiw_2x2_grid_override()
    test_service_pages_canonical_11_sections()
    print("=== ALL TESTS PASSED SUCCESSFULLY! ===")

