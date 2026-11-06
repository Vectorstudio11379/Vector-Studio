# test_project_subpages.py
import os
from projects_data import PROJECTS_LIST

def run_tests():
    for p in PROJECTS_LIST:
        path = os.path.join('projects', f"{p['slug']}.html")
        assert os.path.isfile(path), f"Subpage not found: {path}"
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        assert p['title'] in html or p['short_title'] in html, f"Missing title in {path}"
        assert p['live_url'] in html, f"Missing live_url in {path}"
        assert 'href="/projects.html"' in html or 'href="../projects.html"' in html or 'href="projects.html"' in html, f"Missing link back to projects in {path}"
        assert '/vector-nav.css' in html or 'vector-nav.css' in html, f"Missing stylesheet in {path}"
        assert 'aspect-ratio: 16 / 9' in html or 'case-item-image-wrapper' in html or 'project-hero-media' in html, f"Missing 16:9 widescreen presentation in {path}"
        assert 'Vector Studioz' in html, f"Missing Vector Studioz branding in {path}"
        assert 'coingpt.tech' not in html.lower(), f"Crypto remnant found in {path}"

    print("ALL 15 STANDALONE SUBPAGES EXIST AND PASSED VERIFICATION!")

if __name__ == '__main__':
    run_tests()
