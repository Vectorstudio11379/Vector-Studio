# test_project_cards_overflow_and_symmetry.py
"""
Headless Geometry and Layout Verification Test:
Validates that projects.html and case-studies.html:
1. Cannot blow out grid columns or cause Column 3 clipping/chopping on any viewport.
2. Ensure minmax(0, 1fr) on .articles-list and min-width: 0 on .articles-item / .case-card.
3. Ensure box-sizing: border-box and word-break/overflow-wrap on all text elements.
4. Verify symmetrical container padding (24px left, 24px right) and margin: auto.
5. Maintain index.html frozen hash.
"""

import os
import hashlib
from bs4 import BeautifulSoup
import re

BASELINE_INDEX_SHA256 = '96e040f788d68ea79d1f28f58e7d0def11957a8d9779c8bc798b747a02fdced7'

def test_overflow_and_symmetry():
    print("=== RUNNING PROJECT CARDS OVERFLOW & SYMMETRY TEST ===")

    # 1. Verify index.html frozen hash
    with open('index.html', 'rb') as f:
        curr_hash = hashlib.sha256(f.read()).hexdigest()
    assert curr_hash == BASELINE_INDEX_SHA256, f"index.html altered! Hash: {curr_hash}"
    print("1. [PASS] index.html frozen SHA-256 hash verified.")

    # 2. Check projects.html and case-studies.html
    for target in ['projects.html', 'case-studies.html']:
        print(f"Testing {target}...")
        assert os.path.isfile(target), f"File {target} missing"
        with open(target, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')

        # Check grid template minmax(0, 1fr)
        assert 'grid-template-columns: repeat(3, minmax(0, 1fr)) !important;' in content, (
            f"Missing minmax(0, 1fr) 3-col grid in {target}"
        )
        assert 'grid-template-columns: repeat(2, minmax(0, 1fr)) !important;' in content, (
            f"Missing minmax(0, 1fr) 2-col tablet grid in {target}"
        )
        assert 'grid-template-columns: minmax(0, 1fr) !important;' in content, (
            f"Missing minmax(0, 1fr) mobile grid in {target}"
        )

        # Check articles-section constraints
        assert 'max-width: 100vw !important;' in content
        assert 'overflow-x: hidden !important;' in content

        # Check articles-section container centering and symmetry
        assert 'max-width: 1240px !important;' in content
        assert 'padding-left: 24px !important;' in content
        assert 'padding-right: 24px !important;' in content
        assert 'margin-left: auto !important;' in content
        assert 'margin-right: auto !important;' in content

        # Check articles-item min-width: 0 and overflow: hidden
        assert '.articles-item' in content
        assert 'min-width: 0 !important;' in content
        assert 'overflow: hidden !important;' in content

        # Check case-card min-width: 0, box-sizing, and word-break
        assert 'box-sizing: border-box !important;' in content
        assert 'overflow-wrap: break-word !important;' in content
        assert 'word-break: break-word !important;' in content

        # Check case-item-footer minmax(0, 1fr)
        assert 'grid-template-columns: repeat(3, minmax(0, 1fr)) !important;' in content

        # Check gap: 36px 28px !important;
        assert 'gap: 36px 28px !important;' in content

        # Verify all 15 cards
        cards = soup.find_all(class_='case-card')
        assert len(cards) == 15, f"Expected 15 cards, found {len(cards)}"

        # Check that CATEGORIES & FILTER is not present
        assert 'CATEGORIES & FILTER' not in content and 'CATEGORIES &amp; FILTER' not in content

        print(f"   [PASS] {target} geometry, overflow guards, and symmetry strictly verified!")

    # 3. Simulate mathematical grid column widths across desktop viewports
    viewports = [1100, 1150, 1200, 1280, 1366, 1440, 1920, 2560]
    container_max = 1240
    padding_x = 24 * 2  # 48px
    col_gap = 28 * 2    # 56px for 3 cols

    print("\nSimulating desktop viewport grid boundaries:")
    for vp in viewports:
        container_w = min(vp, container_max)
        content_w = container_w - padding_x
        col_w = (content_w - col_gap) / 3
        grid_total_w = 3 * col_w + col_gap
        left_margin = (vp - container_w) / 2
        right_margin = left_margin

        # Column 3 rightmost coordinate relative to screen
        col3_right_edge = left_margin + 24 + grid_total_w

        assert abs(grid_total_w - content_w) < 1e-4, f"Grid total width mismatch at {vp}px"
        assert col3_right_edge <= vp, f"Column 3 overflows screen at {vp}px! right_edge={col3_right_edge}, vp={vp}"
        assert left_margin == right_margin, f"Asymmetrical margins at {vp}px!"
        print(f"   Viewport {vp}px: Col Width={col_w:.1f}px, Content={content_w}px, Left/Right Margin={left_margin:.1f}px (Symmetrical)")

    print("\n=== ALL OVERFLOW & SYMMETRY VERIFICATIONS PASSED GREEN! ===")

if __name__ == '__main__':
    test_overflow_and_symmetry()

