"""
test_webflow_company_templates.py
Rigorously verifies that about.html, careers.html, and contact-us.html
contain the full 11-section canonical Webflow landing page layout template from web3-chatbot.html
(as shown in the user's reference screenshot media_1793214418187_04f368f1.png).
"""

import os
import hashlib
from bs4 import BeautifulSoup

BASELINE_INDEX_SHA256 = '96e040f788d68ea79d1f28f58e7d0def11957a8d9779c8bc798b747a02fdced7'

# All 11 Canonical Webflow landing template sections from web3-chatbot.html
REQUIRED_SECTIONS = [
    'landing-hero-2',
    'landing-why',          # Why section 1
    'landing-features',     # Features section
    'landing-who-for',      # Who for section
    'landing-hiw',          # How it works section
    'landing-comparison',   # Comparison table
    'landing-launch',       # Mid-page Launch CTA banner
    'landing-group',        # Group / Dual-card comparison section
    'landing-faq',          # F.A.Q. split accordion
    'landing-cta'           # Closing CTA banner
]

CANONICAL_WEBFLOW_CLASSES = [
    'landing-hero-2',
    'landing-hero-dots-top-left',
    'landing-dark-gradient',
    'landing-container',
    'landing-hero-wrapper',
    'landing-hero-asset-wrapper',
    'hero-assets-container',
    'landing-hero-features',
    'landing-hero-features-list',
    'landing-hero-features-item',
    'landing-why',
    'landing-why-wrapper',
    'landing-why-list',
    'landing-why-item',
    'landing-features',
    'landing-features-wrapper',
    'landing-features-list',
    'landing-features-list-item',
    'landing-who-for',
    'landing-who-for-wrapper',
    'landing-hiw',
    'landing-hiw-wrapper',
    'landing-hiw-list-wrapper',
    'landing-comparison',
    'landing-comparison-table',
    'landing-launch',
    'landing-launch-wrapper',
    'landing-group',
    'landing-group-wrapper',
    'landing-group-list',
    'landing-faq',
    'landing-faq-wrapper',
    'landing-faq-questions-list',
    'landing-faq-question-item',
    'landing-cta',
    'cta-wrapper',
    'cta-title-2',
    'btn-primary-4',
    'btn-primary-wrapper',
    'vs-navbar',
    'site-footer'
]

REJECTED_ADHOC_CLASSES = [
    'stat-holo-card',
    'stat-hero-card',
    'stat-hero-frame',
    'faq-accordion-item',
    'hero-grid-2col',
    'about-hero-container',
    'vector-glow-box'
]

def test_index_unmodified():
    print("1. Checking index.html preservation...")
    assert os.path.exists('index.html'), "index.html missing"
    with open('index.html', 'rb') as f:
        current_hash = hashlib.sha256(f.read()).hexdigest()
    assert current_hash == BASELINE_INDEX_SHA256, (
        f"CRITICAL ERROR: index.html was modified! Current: {current_hash}, Expected: {BASELINE_INDEX_SHA256}"
    )
    print("   [PASS] index.html SHA-256 is 100% identical to baseline.")

def test_company_pages_canonical_webflow_template():
    print("2. Checking Company pages for complete 11-section canonical Webflow template layouts...")
    for filename in ['about.html', 'careers.html', 'contact-us.html']:
        assert os.path.exists(filename), f"{filename} missing"
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')

        # Check all canonical Webflow classes
        for cls in CANONICAL_WEBFLOW_CLASSES:
            assert cls in content, f"Missing canonical Webflow class '{cls}' in {filename}"

        # Verify all required sections exist in the DOM
        sections = soup.find_all('section')
        section_classes = [' '.join(s.get('class', [])) for s in sections]
        
        for req_sec in REQUIRED_SECTIONS:
            found = any(req_sec in sc for sc in section_classes)
            assert found, f"Missing section '{req_sec}' in {filename}. Found sections: {section_classes}"

        # Verify there are at least two landing-why sections (matching web3-chatbot.html)
        why_count = sum(1 for sc in section_classes if 'landing-why' in sc)
        assert why_count >= 2, f"Expected at least 2 'landing-why' sections in {filename}, found {why_count}"

        # Verify native Webflow hero assets container is used
        hero_asset = soup.find('div', class_='hero-assets-container')
        assert hero_asset is not None, f"Missing native Webflow '.hero-assets-container' in {filename}"

        # Reject ad-hoc misaligned styles
        for adhoc in REJECTED_ADHOC_CLASSES:
            assert adhoc not in content, f"Found ad-hoc '.{adhoc}' in {filename}. Must use native Webflow classes."

        # Team section must NOT be present in about.html
        if filename == 'about.html':
            assert 'Faces Behind Vector Studioz' not in content, "Team section still in about.html"
            assert 'Elijah Ezekiel' not in content, "Team member card still in about.html"

        # No crypto pricing link
        assert 'pricing.html' not in content, f"pricing.html link found in {filename}"

        print(f"   [PASS] {filename} strictly conforms to the 11-section Webflow template ({len(sections)} sections).")

def test_projects_spacing_preserved():
    print("3. Checking projects.html & case-studies.html spacing...")
    for filename in ['projects.html', 'case-studies.html']:
        assert os.path.exists(filename), f"{filename} missing"
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        assert 'gap: 36px 28px' in content, f"Missing grid gap spacing in {filename}"
    print("   [PASS] Project card spacing preserved.")

if __name__ == '__main__':
    print("=== RUNNING RIGOROUS CANONICAL WEBFLOW TEMPLATE TEST SUITE ===")
    test_index_unmodified()
    test_company_pages_canonical_webflow_template()
    test_projects_spacing_preserved()
    print("=== ALL RIGOROUS CANONICAL WEBFLOW TESTS PASSED! ===")

