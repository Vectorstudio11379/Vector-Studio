# test_projects_catalog.py
import os
from projects_data import PROJECTS_LIST

def run_tests():
    assert os.path.isfile('projects.html'), "projects.html does not exist"
    with open('projects.html', 'r', encoding='utf-8') as f:
        content = f.read()

    assert 'Explore our Projects' in content or 'Client Projects' in content or 'Projects' in content
    for p in PROJECTS_LIST:
        assert p['short_title'] in content or p['title'] in content, f"Missing {p['short_title']} in projects.html"
        assert f"/projects/{p['slug']}.html" in content or f"projects/{p['slug']}.html" in content, f"Missing link to subpage for {p['slug']}"

    assert 'Operational Excellence Assistant & Remote Talent Platform' not in content
    assert 'icL Virtual Services' in content
    assert 'coingpt.tech' not in content.lower()

    # Backwards compatibility check
    assert os.path.isfile('case-studies.html'), "case-studies.html does not exist"
    with open('case-studies.html', 'r', encoding='utf-8') as f:
        cs_content = f.read()
    assert 'projects.html' in cs_content or 'Explore our Projects' in cs_content or 'Client Projects' in cs_content

    print("ALL PROJECTS CATALOG TESTS PASSED!")

if __name__ == '__main__':
    run_tests()
