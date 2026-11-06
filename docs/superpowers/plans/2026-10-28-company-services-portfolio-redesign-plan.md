# Company Pages HIW Fix, Service Pages Migration, Portfolio Image Fix & Resources Removal Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the scrambled "How It Works" 2x2 grid across company pages, fix all broken case study thumbnail paths across portfolio pages, migrate all 6 service pages to the canonical 11-section Webflow landing layout, completely remove all resource pages and navigation references, and preserve `index.html` unchanged.

**Architecture:** Automated Python generator scripts (`build_webflow_company_pages.py`, `build_all_service_pages.py`, `build_agency_projects.py`, `build_project_subpages.py`) compile canonical Webflow HTML using shared templates (`template_header.html`, `template_footer.html`) with scoped CSS grid overrides and relative asset paths.

**Tech Stack:** Python 3, BeautifulSoup4, HTML5/CSS3 (Webflow shared CSS `chain-gpt.shared.a3558708c.min.css`), JavaScript (jQuery, accordion interaction).

**Spec:** [`docs/superpowers/specs/2026-10-28-company-services-portfolio-redesign-design.md`](file:///c:/Users/new/Documents/coingpt/docs/superpowers/specs/2026-10-28-company-services-portfolio-redesign-design.md)

## Global Constraints

- `index.html` SHA-256 hash must remain exactly `96e040f788d68ea79d1f28f58e7d0def11957a8d9779c8bc798b747a02fdced7`.
- "How It Works" section cards must render in a 2x2 grid (Step 1 & 2 in Row 1, Step 3 & 4 in Row 2) on desktop and stack on mobile.
- Zero absolute `/images/case-studies/` paths; must use `images/case-studies/` or `../images/case-studies/`.
- All 6 service pages must include all 11 canonical Webflow sections matching the company pages.
- Resource pages (`blog.html`, `brand-kit.html`, `videos.html`) must be deleted, and all "Resources" navigation items removed from headers and footers.
- Project card grid gap on `projects.html` and `case-studies.html` must preserve `gap: 36px 28px !important;`.

## Review Focus

1. **How It Works Card Ordering**: Step 1 top-left, Step 2 top-right, Step 3 bottom-left, Step 4 bottom-right on desktop; single-column stack on mobile.
2. **Thumbnail Image Resolution**: All 15 case study cards in `projects.html`, `case-studies.html`, and `projects/*.html` must load locally without 404s.
3. **Dead Resource Links**: No dangling links to `blog.html`, `brand-kit.html`, or `videos.html` in navbars, footers, or content bodies.
4. **Service Page Completeness**: Every service page has all 11 sections with domain-relevant copy and interactive accordions.
5. **Baseline Preservation**: `index.html` is strictly untouched.

---

### Task 1: Create TDD Verification Suite

**Files:**
- Create: `test_hiw_grid_and_resources.py`

**Interfaces:**
- Consumes: File system, HTML files.
- Produces: Test runner script reporting assertion passes/failures.

- [ ] **Step 1: Write the failing test in `test_hiw_grid_and_resources.py`**
  Asserts:
  - `blog.html`, `brand-kit.html`, `videos.html` do not exist.
  - No occurrences of "Resources" dropdown or links in `template_header.html` or `template_footer.html`.
  - No leading slash `/images/case-studies/` in `projects.html`, `case-studies.html`, or `projects/*.html`.
  - All company and service pages have `.landing-hiw-list-wrapper` styled with `grid-template-columns: repeat(2, 1fr)`.
  - All 6 service pages contain all 11 canonical Webflow sections.
  - `index.html` hash equals `96e040f788d68ea79d1f28f58e7d0def11957a8d9779c8bc798b747a02fdced7`.

- [ ] **Step 2: Run test to verify it fails (RED phase)**
  Run: `python test_hiw_grid_and_resources.py`
  Expected: FAIL on existing resource files, leading slash images, and missing service page sections.

---

### Task 2: Purge Resource Pages and Clean Global Navigation

**Files:**
- Modify: `template_header.html`
- Modify: `template_footer.html`
- Delete: `blog.html`, `brand-kit.html`, `videos.html`

**Interfaces:**
- Consumes: `template_header.html`, `template_footer.html`.
- Produces: Updated header without Resources dropdown; updated footer without Resources column.

- [ ] **Step 1: Remove resource files**
  Delete `blog.html`, `brand-kit.html`, `videos.html`.

- [ ] **Step 2: Update `template_header.html`**
  Remove the entire "Resources" dropdown `<li>` and the mobile drawer Resources section.

- [ ] **Step 3: Update `template_footer.html`**
  Remove the "Resources" column from the footer grid, rebalancing the grid to `grid-template-columns: 1.6fr 1fr 1fr;` (Brand, Capabilities, Studio).

- [ ] **Step 4: Verify removal**
  Run: `python -c "assert not any(__import__('os').path.exists(f) for f in ['blog.html', 'brand-kit.html', 'videos.html']); print('Resource files removed!')"`

---

### Task 3: Fix "How It Works" 2x2 Grid & Update Company Pages

**Files:**
- Modify: `build_webflow_company_pages.py`
- Modify: `about.html`
- Modify: `careers.html`
- Modify: `contact-us.html`

**Interfaces:**
- Consumes: `template_header.html`, `template_footer.html`.
- Produces: Rebuilt `about.html`, `careers.html`, `contact-us.html` with 2x2 HIW grid layout.

- [ ] **Step 1: Add 2x2 Grid CSS Override to `build_webflow_company_pages.py`**
  Add explicit CSS rules for `.landing-hiw-list-wrapper` to force `grid-template-columns: repeat(2, 1fr)` and reset asymmetric positioning classes.

- [ ] **Step 2: Simplify HIW item markup in `build_webflow_company_pages.py`**
  Remove conflicting legacy classes (`wc-item-1`..`wc-item-5`, `sca-hiw-list`) and ensure items 1, 2, 3, 4 are clean equal-height grid cells.

- [ ] **Step 3: Run generator script**
  Run: `python build_webflow_company_pages.py`
  Expected: Successfully regenerates `about.html`, `careers.html`, `contact-us.html`.

- [ ] **Step 4: Verify company template tests pass**
  Run: `python test_webflow_company_templates.py`
  Expected: PASS.

---

### Task 4: Fix Broken Image Paths Across Portfolio Catalog & Subpages

**Files:**
- Modify: `build_agency_projects.py`
- Modify: `build_project_subpages.py`
- Modify: `projects.html`
- Modify: `case-studies.html`
- Modify: `projects/*.html` (15 subpages)

**Interfaces:**
- Consumes: `template_header.html`, `template_footer.html`, `images/case-studies/`.
- Produces: Relative image paths in `projects.html`, `case-studies.html`, and `projects/*.html`.

- [ ] **Step 1: Update `build_agency_projects.py`**
  Replace all `/images/case-studies/` references with relative `images/case-studies/`.
  Re-run `python build_agency_projects.py` to regenerate `projects.html` and `case-studies.html`.

- [ ] **Step 2: Update `build_project_subpages.py`**
  Replace all `/images/case-studies/` references with relative `../images/case-studies/`.
  Re-run `python build_project_subpages.py` to regenerate all 15 subpages in `projects/`.

- [ ] **Step 3: Verify thumbnail image tests**
  Run: `python test_case_studies_thumbnails.py`
  Run: `python test_projects_catalog.py`
  Run: `python test_projects_suite.py`
  Expected: All PASS with 0 broken or absolute paths.

---

### Task 5: Migrate All 6 Service Pages to Canonical 11-Section Webflow Architecture

**Files:**
- Create/Modify: `build_all_service_pages.py`
- Modify: `web-design.html`
- Modify: `webgl-3d.html`
- Modify: `web-development.html`
- Modify: `software-engineering.html`
- Modify: `ai-automation.html`
- Modify: `mobile-development.html`

**Interfaces:**
- Consumes: `template_header.html`, `template_footer.html`.
- Produces: 6 canonical Webflow service landing pages with all 11 sections and the 2x2 HIW grid.

- [ ] **Step 1: Implement `build_all_service_pages.py`**
  Write complete page generators for:
  1. `web-design.html` (Web Design & UI/UX)
  2. `webgl-3d.html` (3D & WebGL Studio)
  3. `web-development.html` (Full-Stack Web Development)
  4. `software-engineering.html` (Custom Software Engineering)
  5. `ai-automation.html` (AI Automation & Workflows)
  6. `mobile-development.html` (Mobile App Development)
  Each page includes:
  - `landing-hero-2` with `.hero-assets-container.w-embed` video asset and features bar
  - `landing-why` (4 cards)
  - `landing-features` (feature items with banners)
  - `landing-who-for` (4 cards)
  - Second `landing-why` (4 cards)
  - `landing-hiw` (4 steps in clean 2x2 grid)
  - `landing-comparison` (3-column comparison table)
  - `landing-launch` (Launch CTA banner with button)
  - `landing-group` (2 cards: Direct Channels on left, Discovery Brief on right)
  - `landing-faq` (Interactive accordion)
  - `landing-cta` (Closing CTA banner with 3D robot aura)

- [ ] **Step 2: Run generator script**
  Run: `python build_all_service_pages.py`
  Expected: All 6 service pages generated successfully.

- [ ] **Step 3: Run service pages test**
  Run: `python test_agency_services_pages.py`
  Expected: PASS.

---

### Task 6: Full Verification Suite & Final Audit

**Files:**
- Run: `test_hiw_grid_and_resources.py`
- Run: `test_webflow_company_templates.py`
- Run: `test_task_requirements.py`
- Run: `test_webflow_replica_classes.py`
- Run: `test_projects_catalog.py`
- Run: `test_projects_suite.py`
- Run: `verify_all_pages_sync.py`

- [ ] **Step 1: Execute `test_hiw_grid_and_resources.py`**
  Run: `python test_hiw_grid_and_resources.py`
  Expected: PASS (all checks green).

- [ ] **Step 2: Execute all existing regression suites**
  Run:
  - `python test_webflow_company_templates.py`
  - `python test_task_requirements.py`
  - `python test_webflow_replica_classes.py`
  - `python test_projects_catalog.py`
  - `python test_projects_suite.py`
  - `python verify_all_pages_sync.py`
  Expected: All PASS.

- [ ] **Step 3: Verify `index.html` preservation**
  Run: `python -c "import hashlib; h = hashlib.sha256(open('index.html', 'rb').read()).hexdigest(); assert h == '96e040f788d68ea79d1f28f58e7d0def11957a8d9779c8bc798b747a02fdced7'; print('index.html SHA-256 Verified 100% Identical!')"`
  Expected: PASS.

