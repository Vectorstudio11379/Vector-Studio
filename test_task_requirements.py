import os
import glob
from bs4 import BeautifulSoup
import re

def test_requirements():
    print("Testing Task Requirements...")
    assert os.path.exists('index.html'), "index.html must exist"
    
    with open('index.html', 'r', encoding='utf-8') as f:
        index_html = f.read()
    index_soup = BeautifulSoup(index_html, 'html.parser')

    # 1. No pricing section or page
    assert not os.path.exists('pricing.html'), "pricing.html still exists"
    assert index_soup.find(id='our-pricing') is None, "Pricing section (#our-pricing) still exists in index.html"
    assert "Our\n Pricing" not in index_html and "Our Pricing" not in index_html, "Pricing title still in index.html"

    # 2. No Audited by section in index.html
    assert "AUDITED BY" not in index_html, "'AUDITED BY' still found in index.html"
    assert index_soup.find(class_='token-sub-intro') is None, ".token-sub-intro still found in index.html"
    assert "certik.svg" not in index_html, "Certik logo still in index.html"
    assert "hacken.svg" not in index_html, "Hacken logo still in index.html"

    # 3. Features of the sprint content aligned with Vector Studioz agency
    assert "DAO & Voting" not in index_html, "'DAO & Voting' still in index.html"
    assert "retainer & Farming" not in index_html, "'retainer & Farming' still in index.html"
    assert "access to idos" not in index_html, "'access to idos' still in index.html"
    assert "Liquidity Providing" not in index_html, "'Liquidity Providing' still in index.html"
    assert "Bespoke UI/UX &amp; Design Systems" in index_html or "Bespoke UI/UX" in index_html, "Missing Vector Studioz UI/UX sprint feature"
    assert "Full-Stack Web &amp; Mobile Engineering" in index_html or "Full-Stack Web" in index_html, "Missing Vector Studioz engineering sprint feature"

    # 4. Old Explore our Projects section (blog/vlog/spaces) removed
    assert "Tab 2" not in index_html or "data-w-tab=\"Tab 2\"" not in index_html or "blog" not in [t.get_text().strip() for t in index_soup.find_all(class_='text-block-140')], "Old Explore our Projects with blog still present"
    assert index_soup.find(id='cases') is not None, "Agency projects section (#cases) missing"
    assert "Messulogic" in index_html, "Agency projects missing Messulogic"

    # 5. Team section completely removed from index.html and about.html
    assert index_soup.find(id='team') is None, "Team section (#team) still in index.html"
    assert "Faces behind Vector Studioz" not in index_html, "Team title still in index.html"
    with open('about.html', 'r', encoding='utf-8') as f:
        about_html = f.read()
    assert "Faces Behind Vector Studioz" not in about_html, "Team title still in about.html"
    assert "Elijah Ezekiel" not in about_html, "Elijah Ezekiel card still in about.html"

    # 6. Partners & projects (184) and AS SEEN ON removed
    assert "partners & projects (184)" not in index_html, "'partners & projects (184)' still in index.html"
    assert "partners & projects" not in index_html, "'partners & projects' still in index.html"
    assert "AS SEEN ON:" not in index_html, "'AS SEEN ON:' still in index.html"
    if os.path.exists('blog.html'):
        assert "AS SEEN ON:" not in open('blog.html', 'r', encoding='utf-8').read(), "'AS SEEN ON:' still in blog.html"
    if os.path.exists('videos.html'):
        assert "AS SEEN ON:" not in open('videos.html', 'r', encoding='utf-8').read(), "'AS SEEN ON:' still in videos.html"
    if os.path.exists('verify.html'):
        assert "AS SEEN ON:" not in open('verify.html', 'r', encoding='utf-8').read(), "'AS SEEN ON:' still in verify.html"

    # 7. Revolution / Community section removed per user request and image
    assert index_soup.find(id='ai-revolution') is None, "ai-revolution still in index.html"
    assert "195K+" not in index_html, "195K+ still in index.html"
    assert "45K+" not in index_html, "45K+ still in index.html"
    assert "t.me/chaingpt" not in index_html, "ChainGPT telegram still in index.html"
    assert "discord.gg/chaingpt" not in index_html, "ChainGPT discord still in index.html"

    # 8. FAQ in index.html cleaned of crypto/staking/DAO
    for forbidden in ['CGPT Credits', 'Diamond Tier', '0x9840652DC04fb9db2C43853633f0F62BE6f00f98', 'Binance smart chain', '200,000 voting power']:
        assert forbidden not in index_html, f"Lingering crypto FAQ content found: {forbidden}"

    # 9. Div nesting depth is 0 at all major section boundaries in index.html
    pattern = re.compile(r'<(/?[a-zA-Z0-9]+)(\s+[^>]*)?>')
    depth = 0
    for m in pattern.finditer(index_html):
        tag = m.group(1).lower()
        attrs = m.group(2) or ''
        is_sec = any(k in attrs for k in ['id="cases"', 'id="ecosystem"', 'id="our-token"', 'id="faq"', 'id="site-footer"'])
        if is_sec and not tag.startswith('/'):
            assert depth == 0, f"Section {attrs[:30]} at non-zero depth {depth}"
        if tag == 'div': depth += 1
        elif tag == '/div': depth -= 1
    assert depth == 0, f"Final div depth in index.html is {depth}"

    # 10. Navigation & footer pricing link removed
    with open('template_header.html', 'r', encoding='utf-8') as f:
        tpl_header = f.read()
    assert 'href="pricing.html"' not in tpl_header, "pricing.html link still in template_header.html"

    with open('template_footer.html', 'r', encoding='utf-8') as f:
        tpl_footer = f.read()
    assert 'href="pricing.html"' not in tpl_footer, "pricing.html link still in template_footer.html"

    # 11. Header on project page and subpages consistent with home page
    with open('projects.html', 'r', encoding='utf-8') as f:
        prj_html = f.read()
    assert 'vector-nav.js' in prj_html, "vector-nav.js missing from projects.html"
    assert 'href="/vector-nav.css"' not in prj_html, "Duplicate /vector-nav.css in projects.html"

    subpages = glob.glob('projects/*.html')
    assert len(subpages) == 15, f"Expected 15 subpages, found {len(subpages)}"
    for sub in subpages:
        with open(sub, 'r', encoding='utf-8') as f:
            sub_html = f.read()
        assert 'vs-nav-header' not in sub_html, f"Legacy vs-nav-header found in {sub}"
        assert 'vs-navbar' in sub_html, f"vs-navbar missing from {sub}"
        assert sub_html.count('vector-nav.js') == 1, f"Duplicate vector-nav.js in {sub}"
        assert sub_html.count('vector-nav.css') == 1, f"Duplicate vector-nav.css in {sub}"

    print("ALL 11 REQUIREMENTS VERIFICATION SUITE PASSED!")

if __name__ == '__main__':
    test_requirements()
