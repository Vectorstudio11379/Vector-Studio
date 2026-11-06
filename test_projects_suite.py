# test_projects_suite.py
import os
import glob
from projects_data import PROJECTS_LIST

def run_tests():
    # 1. Check all 15 subpages
    for p in PROJECTS_LIST:
        subpage = os.path.join('projects', f"{p['slug']}.html")
        assert os.path.isfile(subpage), f"Missing subpage {subpage}"
        with open(subpage, 'r', encoding='utf-8') as f:
            c = f.read()
        assert p['live_url'] in c, f"Missing live_url in {subpage}"
        assert '/vector-nav.css' in c or 'vector-nav.css' in c
        assert 'Vector Studioz' in c
        assert 'coingpt.tech' not in c.lower()

    # 2. Check catalog projects.html
    assert os.path.isfile('projects.html')
    with open('projects.html', 'r', encoding='utf-8') as f:
        proj_cat = f.read()
    assert 'Explore our Projects' in proj_cat or 'Client Projects' in proj_cat or 'Projects' in proj_cat
    for p in PROJECTS_LIST:
        assert f"/projects/{p['slug']}.html" in proj_cat

    # 3. Check all site pages for Projects navigation
    pages_to_check = [
        'index.html', 'projects.html', 'about.html', 'careers.html', 'contact-us.html',
        'web-design.html', 'web-development.html', 'software-engineering.html',
        'ai-automation.html', 'webgl-3d.html', 'mobile-development.html'
    ]
    for page in pages_to_check:
        assert os.path.isfile(page), f"Page {page} does not exist"
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        assert 'projects.html' in content, f"Page {page} missing projects.html link"
        assert 'Projects' in content, f"Page {page} missing Projects label in nav"

    print("ALL 15 SUBPAGES, CATALOG, AND GLOBAL PAGES VERIFIED GREEN!")

if __name__ == '__main__':
    run_tests()
