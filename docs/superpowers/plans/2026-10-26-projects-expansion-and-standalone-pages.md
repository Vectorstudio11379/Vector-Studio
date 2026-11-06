# Projects Expansion & Standalone Subpages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the client showcase into "Projects", integrate 6 live client websites (expanding the portfolio to 15 real-world platforms), generate dedicated standalone subpages for every project, and update global navigation, the homepage slider, and the catalog grid.

**Architecture:** A centralized Python data model (`projects_data.py`) serves as the single source of truth for all 15 client projects. Automated generators compile standalone static HTML subpages in `projects/<slug>.html`, the master catalog `projects.html` (with `case-studies.html` alias), the homepage slider on `index.html`, and propagate "Projects" navigation across all 24 site pages.

**Tech Stack:** HTML5, CSS3 (`vector-nav.css`), Vanilla JavaScript (`vector-nav.js`), Python 3 static site generators, and Pytest / Python test scripts.

**Spec:** [`docs/superpowers/specs/2026-10-26-projects-expansion-and-standalone-pages-design.md`](file:///c:/Users/new/Documents/coingpt/docs/superpowers/specs/2026-10-26-projects-expansion-and-standalone-pages-design.md)

## Global Constraints
- Every case study / project thumbnail must strictly use `aspect-ratio: 16 / 9`, `width: 100%`, and `object-fit: cover`.
- All branding must remain strictly **Vector Studioz**; zero cryptocurrency terms.
- All 15 projects must feature verified live website URLs with `target="_blank" rel="noopener noreferrer"`.
- Legacy `case-studies.html` must remain active and redirect or mirror `projects.html` to prevent broken bookmarks.
- Subpage asset paths must use root-relative `/` URLs (e.g. `/vector-nav.css`, `/vector-nav.js`, `/images/...`) so they load correctly from any subfolder.

## Review Focus
1. **Broken Subpage Asset Links**: Verify that stylesheets, fonts, and scripts load cleanly on `/projects/<slug>.html` without 404 errors.
2. **Missing Live URLs**: Ensure all 15 project cards and subpage headers link to their real outbound sites with external target attributes.
3. **Thumbnail Aspect Ratio Consistency**: Ensure none of the newly added projects render letterboxed or squished images.
4. **Navigation Consistency Across 24 Pages**: Ensure every page's header nav and footer list "Projects" pointing to `projects.html`.
5. **Backwards Compatibility**: Confirm navigating to `/case-studies.html` seamlessly displays the Projects catalog without error.

---

### Task 1: Centralized Project Data Model (`projects_data.py`)

**Files:**
- Create: `projects_data.py`
- Test: `test_projects_data.py`

**Interfaces:**
- Produces: `PROJECTS_LIST` (List of 15 project dicts with slug, title, short_title, client, category, industry, year, live_url, thumbnail, tagline, metrics, overview, challenge, solution, tech_stack, testimonial).

- [ ] **Step 1: Write the failing test for the data model**

```python
# test_projects_data.py
import pytest
from projects_data import PROJECTS_LIST

def test_projects_list_count_and_keys():
    assert len(PROJECTS_LIST) == 15
    required_keys = ['slug', 'title', 'short_title', 'client', 'category', 'industry', 'year', 'live_url', 'thumbnail', 'tagline', 'metrics', 'overview', 'challenge', 'solution', 'tech_stack']
    for p in PROJECTS_LIST:
        for key in required_keys:
            assert key in p, f"Missing {key} in {p.get('slug')}"
            assert p[key], f"Empty value for {key} in {p.get('slug')}"
        assert p['live_url'].startswith('http'), f"Invalid live_url in {p.get('slug')}"
        assert len(p['metrics']) >= 2, f"Expected at least 2 metrics in {p.get('slug')}"

def test_icl_virtual_services_present_and_op_excellence_replaced():
    slugs = [p['slug'] for p in PROJECTS_LIST]
    assert 'iclvirtualservices' in slugs
    assert 'operational-excellence' not in slugs
    icl = next(p for p in PROJECTS_LIST if p['slug'] == 'iclvirtualservices')
    assert icl['live_url'] == 'https://iclvirtualservices.com/'
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest test_projects_data.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'projects_data'`

- [ ] **Step 3: Implement `projects_data.py` with all 15 project specifications**

Populate `PROJECTS_LIST` with the 6 user-specified additions/replacements and the 9 existing projects:
1. `mesuullogic`: `https://mesuullogic.com/` (EdTech & Learning Management)
2. `expressteck`: `https://expressteck.tech/` (Tech Innovation, Courses & Commerce)
3. `lake-greenfield-hotel`: `https://lakegreenfieldhotel.com/` (Luxury Hospitality & Booking Engine)
4. `iclvirtualservices`: `https://iclvirtualservices.com/` (Operational Excellence Assistant & Remote Talent)
5. `mirola-cleaning-services`: `https://mirolacleaningservices.com/` (Commercial Janitorial & Facility Sanitization)
6. `mirola-nigeria`: `https://mirolanigeria.com/` (Digital & Remote Skills Academy)
7. `beacon-corporate-realty`: `https://beaconcorporaterealty.com`
8. `twist-studio`: `https://jumbodtg.com/`
9. `resilient-solutions`: `https://timi-portfolio.onrender.com/work`
10. `mirola-ambassador`: `https://timi-portfolio.onrender.com/work`
11. `mirodata`: `https://timi-portfolio.onrender.com/work`
12. `cleaner-spaces`: `https://timi-portfolio.onrender.com/work`
13. `5th-element-media`: `https://timi-portfolio.onrender.com/work`
14. `aliola-global-services`: `https://timi-portfolio.onrender.com/work`
15. `tom-ojo-sports-academy`: `https://timi-portfolio.onrender.com/work`

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest test_projects_data.py -v`
Expected: PASS with 2 tests passing

- [ ] **Step 5: Commit**

```bash
git add projects_data.py test_projects_data.py
git commit -m "feat: add centralized projects data model for 15 platforms"
```

---

### Task 2: Standalone Subpages Generator (`build_project_subpages.py`)

**Files:**
- Create: `build_project_subpages.py`
- Create directory: `projects/`
- Test: `test_project_subpages.py`

**Interfaces:**
- Consumes: `PROJECTS_LIST` from `projects_data.py`
- Produces: 15 HTML files inside `projects/<slug>.html`

- [ ] **Step 1: Write the failing test for subpages generator**

```python
# test_project_subpages.py
import os
from projects_data import PROJECTS_LIST

def test_all_15_subpages_exist_and_render_correctly():
    for p in PROJECTS_LIST:
        path = os.path.join('projects', f"{p['slug']}.html")
        assert os.path.isfile(path), f"Subpage not found: {path}"
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        assert p['title'] in html or p['short_title'] in html
        assert p['live_url'] in html
        assert 'href="/projects.html"' in html or 'href="../projects.html"' in html
        assert '/vector-nav.css' in html
        assert 'aspect-ratio: 16 / 9' in html or 'case-item-image-wrapper' in html
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest test_project_subpages.py -v`
Expected: FAIL because subpages do not exist yet

- [ ] **Step 3: Implement `build_project_subpages.py`**

Build the subpage template containing:
- Vector Studioz `<head>` with dynamic `<title>` and `<meta name="description">`.
- Global `<header class="vs-nav-header">` with "Projects" link marked active.
- Project Hero with category tag, client name, project title, year, and "Visit Live Website ↗" button.
- 16:9 cinematic screenshot preview container.
- Two-column detail layout: Left column = Project Background, Strategic Challenge, and Architectural Solution; Right column = Tech Stack Pills, Client Info, and Impact Metric Cards.
- Outbound CTA banner to the live website.
- Pagination / Cross-navigation bar (`← Previous Project` | `All Projects` | `Next Project →`).
- Vector Studioz Global `<footer class="vs-footer">`.
- Run script to compile all 15 files into `projects/`.

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest test_project_subpages.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add build_project_subpages.py projects/ test_project_subpages.py
git commit -m "feat: generate 15 dedicated standalone project subpages"
```

---

### Task 3: Projects Catalog Page (`projects.html` & `case-studies.html`)

**Files:**
- Create: `build_agency_projects.py`
- Create: `projects.html`
- Update: `case-studies.html` (mirror / redirect)
- Test: `test_projects_catalog.py`

**Interfaces:**
- Consumes: `PROJECTS_LIST` from `projects_data.py`
- Produces: `projects.html` and synchronized `case-studies.html`

- [ ] **Step 1: Write the failing test for the catalog**

```python
# test_projects_catalog.py
import os
from projects_data import PROJECTS_LIST

def test_projects_catalog_content_and_links():
    assert os.path.isfile('projects.html')
    with open('projects.html', 'r', encoding='utf-8') as f:
        content = f.read()
    assert 'Explore our Projects' in content or 'Projects' in content
    for p in PROJECTS_LIST:
        assert p['short_title'] in content or p['title'] in content
        assert f"/projects/{p['slug']}.html" in content or f"projects/{p['slug']}.html" in content
    assert 'Operational Excellence Assistant' not in content
    assert 'icL Virtual Services' in content

def test_case_studies_alias_exists():
    assert os.path.isfile('case-studies.html')
    with open('case-studies.html', 'r', encoding='utf-8') as f:
        content = f.read()
    assert 'projects.html' in content or 'Explore our Projects' in content
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest test_projects_catalog.py -v`
Expected: FAIL with `FileNotFoundError` or missing projects in `projects.html`

- [ ] **Step 3: Implement `build_agency_projects.py`**

Generate `projects.html` using the existing dark luxury design:
- Page Header: "Vector Studioz — Client Projects & Digital Platforms".
- Hero: "Our Work & Digital Platforms — Bespoke Websites, Scalable Web Applications & Interactive Digital Experiences".
- Category Filter Navigation: All, Web Design, SaaS & Cloud, EdTech, Operations, E-Commerce.
- Responsive 2-column widescreen grid (`.cases-page-grid`) showing all 15 cards with 16:9 thumbnails, tags, metrics, and direct links to `/projects/<slug>.html`.
- Also mirror to `case-studies.html` with a meta redirect and identical catalog view.

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest test_projects_catalog.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add build_agency_projects.py projects.html case-studies.html test_projects_catalog.py
git commit -m "feat: compile master projects.html catalog and sync case-studies alias"
```

---

### Task 4: Homepage Slider & Section Transition (`index.html`)

**Files:**
- Modify: `index.html:1610-1640`
- Test: `test_homepage_projects_section.py`

**Interfaces:**
- Consumes: `PROJECTS_LIST` from `projects_data.py`
- Produces: Updated `#cases` section on `index.html` labeled "Projects" with all 15 project slides.

- [ ] **Step 1: Write the failing test for homepage slider**

```python
# test_homepage_projects_section.py
def test_homepage_projects_tab_and_slider():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    assert 'Explore our Projects' in html or 'Explore our</span>' in html
    assert 'href="projects.html"' in html
    assert 'icL Virtual Services' in html
    assert 'Operational Excellence — Digital Operations' not in html
    assert 'Messulogic' in html
    assert 'ExpressTeck' in html
    assert 'Lake Greenfield Hotel' in html
    assert 'Mirola Cleaning Services' in html
    assert 'Mirola Enterprise Nigeria' in html
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest test_homepage_projects_section.py -v`
Expected: FAIL

- [ ] **Step 3: Update `index.html` section and slider**

- Update tab heading from "Case Studies" to "Projects".
- Update link button from "CLIENT PORTFOLIO" pointing to `case-studies.html` to point to `projects.html`.
- Update `#case-slider` to include the slides for the 6 new/updated platforms (Messulogic, ExpressTeck, Lake Greenfield Hotel, icL Virtual Services, Mirola Cleaning Services, Mirola Enterprise Nigeria) with 16:9 thumbnails, metrics, and links to `/projects/<slug>.html`.
- Update the bottom "Read More" button to `href="projects.html"` with text "Explore all Client Projects & Platforms".

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest test_homepage_projects_section.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add index.html test_homepage_projects_section.py
git commit -m "feat: update homepage slider and section to Projects with 15 platforms"
```

---

### Task 5: Global Site Navigation Synchronization Across All 24 Pages

**Files:**
- Modify: `template_header.html`
- Modify: `template_footer.html`
- Modify: `navbar_current.html`
- Run: `sync_all_pages.py`
- Test: `verify_all_pages_sync.py` & `test_projects_suite.py`

**Interfaces:**
- Updates navigation links: `href="case-studies.html"` -> `href="projects.html"`, label: `Projects`.

- [ ] **Step 1: Write comprehensive verification test `test_projects_suite.py`**

```python
# test_projects_suite.py
import os
import glob
from projects_data import PROJECTS_LIST

def test_global_pages_contain_projects_nav():
    html_files = [f for f in glob.glob('*.html') if not f.endswith('.bak') and f != 'template_header.html' and f != 'template_footer.html' and f != 'navbar_current.html']
    for page in html_files:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        if 'vs-nav-header' in content or 'header-menu' in content:
            assert 'href="projects.html"' in content or 'href="/projects.html"' in content, f"Page {page} missing projects.html link"
            assert 'Projects' in content, f"Page {page} missing Projects label"

def test_all_15_subpages_have_live_links_and_styles():
    for p in PROJECTS_LIST:
        subpage = os.path.join('projects', f"{p['slug']}.html")
        assert os.path.isfile(subpage)
        with open(subpage, 'r', encoding='utf-8') as f:
            content = f.read()
        assert p['live_url'] in content
        assert '/vector-nav.css' in content
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest test_projects_suite.py -v`
Expected: FAIL

- [ ] **Step 3: Update templates and run `sync_all_pages.py`**

- Update `template_header.html` to change "Case Studies" to "Projects" linking to `projects.html`.
- Update `template_footer.html` to change "Case Studies" to "Projects" linking to `projects.html`.
- Run `python sync_all_pages.py` to synchronize all 24 website pages.

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest test_projects_suite.py -v`
Expected: PASS

- [ ] **Step 5: Visual inspection in browser**

Navigate browser subagent to `http://localhost:3000/projects.html`, `http://localhost:3000/projects/mesuullogic.html`, and `http://localhost:3000/index.html#cases`. Confirm responsive layouts, 16:9 imagery, and working live links.

- [ ] **Step 6: Commit**

```bash
git add template_header.html template_footer.html navbar_current.html *.html test_projects_suite.py
git commit -m "feat: complete global navigation synchronization for Projects across all pages"
```
