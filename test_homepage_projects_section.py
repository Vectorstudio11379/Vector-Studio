# test_homepage_projects_section.py
from projects_data import PROJECTS_LIST

def run_tests():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Check tab label is Projects
    assert 'Projects</div>' in html or '>Projects<' in html, "Tab label is not Projects"
    assert 'href="projects.html"' in html or 'href="/projects.html"' in html, "Missing link to projects.html"
    
    # Check replacement of legacy operational excellence
    assert 'Operational Excellence — Digital Operations' not in html, "Legacy Operational Excellence still present in index.html"
    assert 'icL Virtual Services' in html, "icL Virtual Services not in index.html slider"

    # Check newly added sites in slider
    assert 'Messulogic' in html, "Messulogic not in index.html"
    assert 'ExpressTeck' in html, "ExpressTeck not in index.html"
    assert 'Lake Greenfield' in html, "Lake Greenfield Hotel not in index.html"
    assert 'Mirola Cleaning' in html, "Mirola Cleaning not in index.html"
    assert 'Mirola Enterprise Nigeria' in html, "Mirola Enterprise Nigeria not in index.html"

    # Check that all 15 project subpages are linked in index.html
    for p in PROJECTS_LIST:
        assert f"/projects/{p['slug']}.html" in html or f"projects/{p['slug']}.html" in html, f"Missing subpage link for {p['slug']} in index.html"

    print("ALL HOMEPAGE PROJECTS SECTION TESTS PASSED!")

if __name__ == '__main__':
    run_tests()
