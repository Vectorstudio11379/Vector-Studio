# test_project_cards_layout_and_padding.py
"""
Verification script for user request:
- Remove CATEGORIES & FILTER and sidebar offset
- Properly align project cards so the right part is not cut off
- Ensure project cards content has proper padding and balanced breathing room
- Preserve index.html SHA-256 hash
- Preserve header CTA button SUBMIT PROJECT BRIEF ↓
"""

import os
import hashlib
from bs4 import BeautifulSoup

BASELINE_INDEX_SHA256 = '96e040f788d68ea79d1f28f58e7d0def11957a8d9779c8bc798b747a02fdced7'

def verify_all():
    print("=== RUNNING PROJECT CARDS LAYOUT & PADDING TEST SUITE ===")

    # 1. Verify index.html SHA-256 hash
    with open('index.html', 'rb') as f:
        curr_hash = hashlib.sha256(f.read()).hexdigest()
    assert curr_hash == BASELINE_INDEX_SHA256, f"index.html was modified! Current: {curr_hash}"
    print("1. [PASS] index.html hash matches baseline perfectly.")

    # 2. Check projects.html and case-studies.html
    for filename in ['projects.html', 'case-studies.html']:
        print(f"Checking {filename}...")
        assert os.path.isfile(filename), f"{filename} does not exist"
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()

        soup = BeautifulSoup(html, 'html.parser')

        # CATEGORIES & FILTER must be completely removed
        assert "CATEGORIES &amp; FILTER" not in html and "CATEGORIES & FILTER" not in html, (
            f"Found 'CATEGORIES & FILTER' in {filename}"
        )
        assert soup.find(class_='article-pre-labe') is None, (
            f"Found '.article-pre-labe' in {filename}"
        )

        # Container & grid centering
        assert '.articles-wrap' in html, f"Missing .articles-wrap in {filename}"
        assert 'max-width: 1240px !important' in html, f"Missing max-width 1240px container in {filename}"
        assert 'display: block !important' in html, f"Missing display: block override in {filename}"
        assert 'gap: 36px 28px !important' in html, f"Missing gap: 36px 28px in {filename}"

        # Card content padding & breathing room
        assert 'padding: 24px !important' in html, f"Missing padding: 24px in {filename}"
        assert 'box-sizing: border-box !important' in html, f"Missing box-sizing in {filename}"
        assert '.case-item-head' in html, f"Missing .case-item-head in {filename}"
        assert '.case-item-image-wrapper' in html, f"Missing .case-item-image-wrapper in {filename}"
        assert 'aspect-ratio: 16 / 9 !important' in html, f"Missing 16:9 aspect ratio in {filename}"
        assert '.case-desc-wrap' in html, f"Missing .case-desc-wrap in {filename}"
        assert '.case-item-footer' in html, f"Missing .case-item-footer in {filename}"
        assert '.case-card-actions-bar' in html, f"Missing .case-card-actions-bar in {filename}"

        # Header CTA button
        assert 'SUBMIT PROJECT BRIEF &darr;' in html or 'SUBMIT PROJECT BRIEF ↓' in html, (
            f"Missing 'SUBMIT PROJECT BRIEF' CTA button in {filename}"
        )

        # Check all 15 cards are present and well-formed
        cards = soup.find_all(class_='case-card')
        assert len(cards) == 15, f"Expected 15 case cards in {filename}, found {len(cards)}"
        for card in cards:
            assert card.find(class_='case-item-head') is not None
            assert card.find(class_='case-item-image-wrapper') is not None
            assert card.find(class_='case-desc-wrap') is not None
            assert card.find(class_='case-item-footer') is not None
            assert card.find(class_='case-card-actions-bar') is not None

        print(f"   [PASS] {filename} layout and padding strictly validated!")

    print("=== ALL PROJECT CARDS LAYOUT AND PADDING VERIFICATIONS PASSED! ===")

if __name__ == '__main__':
    verify_all()

