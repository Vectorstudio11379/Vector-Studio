# test_projects_data.py
import sys

def run_tests():
    from projects_data import PROJECTS_LIST

    assert len(PROJECTS_LIST) == 15, f"Expected 15 projects, got {len(PROJECTS_LIST)}"
    required_keys = ['slug', 'title', 'short_title', 'client', 'category', 'industry', 'year', 'live_url', 'thumbnail', 'tagline', 'metrics', 'overview', 'challenge', 'solution', 'tech_stack']
    for p in PROJECTS_LIST:
        for key in required_keys:
            assert key in p, f"Missing {key} in {p.get('slug')}"
            assert p[key], f"Empty value for {key} in {p.get('slug')}"
        assert p['live_url'].startswith('http'), f"Invalid live_url in {p.get('slug')}"
        assert len(p['metrics']) >= 2, f"Expected at least 2 metrics in {p.get('slug')}"

    slugs = [p['slug'] for p in PROJECTS_LIST]
    assert 'iclvirtualservices' in slugs, "iclvirtualservices missing from slugs"
    assert 'operational-excellence' not in slugs, "operational-excellence was not replaced"
    icl = next(p for p in PROJECTS_LIST if p['slug'] == 'iclvirtualservices')
    assert icl['live_url'] == 'https://iclvirtualservices.com/'

    slug_url_map = {p['slug']: p['live_url'] for p in PROJECTS_LIST}
    assert 'mesuullogic' in slug_url_map and slug_url_map['mesuullogic'] == 'https://mesuullogic.com/'
    assert 'expressteck' in slug_url_map and slug_url_map['expressteck'] == 'https://expressteck.tech/'
    assert 'lake-greenfield-hotel' in slug_url_map and slug_url_map['lake-greenfield-hotel'] == 'https://lakegreenfieldhotel.com/'
    assert 'iclvirtualservices' in slug_url_map and slug_url_map['iclvirtualservices'] == 'https://iclvirtualservices.com/'
    assert 'mirola-cleaning-services' in slug_url_map and slug_url_map['mirola-cleaning-services'] == 'https://mirolacleaningservices.com/'
    assert 'mirola-nigeria' in slug_url_map and slug_url_map['mirola-nigeria'] == 'https://mirolanigeria.com/'

    print("ALL 15 PROJECTS DATA SPECIFICATION TESTS PASSED!")

if __name__ == '__main__':
    run_tests()
