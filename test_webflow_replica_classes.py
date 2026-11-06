# test_webflow_replica_classes.py
"""
Automated verification test suite for Webflow Architecture Replica
Validates that secondary pages mirror coingpt.tech design, layout, styles,
and animation classes while strictly verifying index.html remains untouched.
"""

import os
import hashlib
from bs4 import BeautifulSoup
from projects_data import PROJECTS_LIST

BASELINE_INDEX_SHA256 = '96e040f788d68ea79d1f28f58e7d0def11957a8d9779c8bc798b747a02fdced7'

REQUIRED_WEBFLOW_CLASSES = [
    'articles-hero',
    'articles-section',
    'section-head-cols',
    'section-heading-dot',
    'section-title-bordered',
    'filters-panel',
    'filter-search-field',
    'articles-list',
    'articles-item',
    'article-card',
    'case-card',
    'case-item-head',
    'case-item-image-wrapper',
    'case-item-bg-gradient',
    'arrow-el-wrap',
    'arrow-el',
    'corner-elem',
    'case-item-footer',
    'caseitem-footer-text',
    'caseitem-footer-subtext'
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

def test_projects_webflow_replica():
    print("2. Checking projects.html & case-studies.html Webflow replica...")
    for filename in ['projects.html', 'case-studies.html']:
        assert os.path.exists(filename), f"{filename} missing"
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check required Webflow classes
        for cls in REQUIRED_WEBFLOW_CLASSES:
            assert cls in content, f"Missing Webflow class '{cls}' in {filename}"

        # Check card spacing
        assert 'gap: 36px 28px' in content, f"Missing grid gap spacing in {filename}"

        # Check all 15 project links and titles
        soup = BeautifulSoup(content, 'html.parser')
        cards = soup.find_all(class_='articles-item')
        assert len(cards) == 15, f"Expected 15 articles-item cards in {filename}, found {len(cards)}"

        for p in PROJECTS_LIST:
            expected_href = f"/projects/{p['slug']}.html"
            assert expected_href in content, f"Missing link {expected_href} in {filename}"

        # Check filter bar and search input
        assert soup.find(id='projects-search-input') is not None, f"Missing search input in {filename}"
        pills = soup.find_all(class_='category-filter-pill')
        assert len(pills) >= 5, f"Expected category filter pills in {filename}, found {len(pills)}"

        # Check for zero crypto pricing links
        assert 'href="pricing.html"' not in content, f"pricing.html link found in {filename}"
        assert 'href="/pricing.html"' not in content, f"/pricing.html link found in {filename}"

    print("   [PASS] projects.html & case-studies.html match coingpt.tech Webflow architecture.")

def test_company_pages_design_system():
    print("3. Checking Company pages (about.html, careers.html, contact-us.html)...")
    for filename in ['about.html', 'careers.html', 'contact-us.html']:
        assert os.path.exists(filename), f"{filename} missing"
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        assert 'chain-gpt.shared.a3558708c.min.css' in content, f"Missing Webflow shared CSS in {filename}"
        assert 'section-title-bordered' in content, f"Missing section-title-bordered in {filename}"
        assert 'block-corners-top' in content, f"Missing block-corners-top in {filename}"
        assert 'block-corners-bottom' in content, f"Missing block-corners-bottom in {filename}"
        assert 'landing-hero-2' in content, f"Missing landing-hero-2 in {filename}"
        assert 'landing-why' in content, f"Missing landing-why in {filename}"
        assert 'landing-faq' in content, f"Missing landing-faq in {filename}"
        assert 'landing-cta' in content, f"Missing landing-cta in {filename}"
        assert 'vs-navbar' in content, f"Missing vs-navbar in {filename}"
        assert 'site-footer' in content, f"Missing site-footer in {filename}"
        assert 'pricing.html' not in content, f"pricing.html found in {filename}"

        if filename == 'about.html':
            assert 'Faces Behind Vector Studioz' not in content, "Team section still in about.html"
            assert 'Elijah Ezekiel' not in content, "Team member card still in about.html"

    print("   [PASS] Company pages utilize Webflow shared styles and corner-cut frames.")

def test_all_15_subpages():
    print("4. Checking all 15 project subpages...")
    for p in PROJECTS_LIST:
        subpage_path = os.path.join('projects', f"{p['slug']}.html")
        assert os.path.exists(subpage_path), f"Missing {subpage_path}"
        with open(subpage_path, 'r', encoding='utf-8') as f:
            content = f.read()

        assert 'chain-gpt.shared.a3558708c.min.css' in content
        assert 'vector-nav.css' in content
        assert p['live_url'] in content
        assert 'Vector Studioz' in content
        assert '../projects.html' in content or 'projects.html' in content

    print("   [PASS] All 15 subpages verified green.")

if __name__ == '__main__':
    print("=== RUNNING WEBFLOW ARCHITECTURE REPLICA VERIFICATION SUITE ===")
    test_index_unmodified()
    test_projects_webflow_replica()
    test_company_pages_design_system()
    test_all_15_subpages()
    print("=== ALL REPLICA VERIFICATION TESTS PASSED SUCCESSFULLY! ===")

