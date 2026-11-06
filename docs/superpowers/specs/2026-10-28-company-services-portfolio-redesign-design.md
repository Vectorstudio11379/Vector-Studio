# Design Document: Company Pages HIW Fix, Service Pages Canonical Webflow Migration, Portfolio Image Fix & Resources Removal

**Date:** October 28, 2026  
**Status:** Pending Review  
**Target Architecture:** Vector Studioz Canonical Webflow Landing System  

---

## 1. Intent & Purpose
The objective of this design is to resolve structural alignment and visual inconsistencies across the Vector Studioz website:
1. **Fix the Scrambled "How It Works" (HIW) Layout**: Resolve the asymmetric Webflow CSS grid conflict where Step 4 floated beside Step 1 and Step 2 was pushed down, replacing it with a balanced, sequential **2x2 grid** (Step 1 & 2 in Row 1, Step 3 & 4 in Row 2) across all pages.
2. **Fix Broken Image Paths**: Convert absolute root `/images/case-studies/...` image paths in `projects.html`, `case-studies.html`, and all 15 project subpages in `projects/` to proper relative paths (`images/case-studies/...` and `../images/case-studies/...`), restoring all project thumbnails.
3. **Migrate All 6 Service Pages to Canonical Webflow Layout**: Transform `web-design.html`, `webgl-3d.html`, `web-development.html`, `software-engineering.html`, `ai-automation.html`, and `mobile-development.html` from legacy custom grids to the 11-section canonical Webflow layout established on the Company pages.
4. **Completely Purge the Resource Section**: Delete `blog.html`, `brand-kit.html`, and `videos.html`. Remove all "Resources" dropdown menus, links, and footer columns across every page.
5. **Strict Baseline Invariance**: Maintain `index.html` 100% frozen (SHA-256: `96e040f788d68ea79d1f28f58e7d0def11957a8d9779c8bc798b747a02fdced7`).

---

## 2. Goals, Non-Goals & Anti-Goals

### Goals
- Ensure the 4-step HIW cards render sequentially in a clean 2x2 grid on desktop viewports and stack cleanly on mobile viewports.
- Fix all thumbnail image references so every case study card displays its preview graphic without 404 errors in all environments.
- Unify all 6 service landing pages under the canonical 11-section Webflow architecture (`landing-hero-2`, `landing-why`, `landing-features`, `landing-who-for`, second `landing-why`, `landing-hiw`, `landing-comparison`, `landing-launch`, `landing-group`, `landing-faq`, `landing-cta`).
- Cleanly delete `blog.html`, `brand-kit.html`, `videos.html` and eliminate all navigation references to "Resources".
- Verify all changes with comprehensive automated test suites.

### Non-Goals
- Modifying `index.html` under any circumstances.
- Altering the core visual branding (Vector Studioz cyan/purple glow theme).

### Anti-Goals
- Do not introduce ad-hoc CSS classes or unverified inline positioning.
- Do not leave broken links or references pointing to deleted resource pages.
- Do not disrupt the catalog filtering functionality on `projects.html` and `case-studies.html`.

---

## 3. Constraints
- **Frozen Baseline**: `index.html` SHA-256 hash must remain exactly `96e040f788d68ea79d1f28f58e7d0def11957a8d9779c8bc798b747a02fdced7`.
- **CSS Architecture**: Use native Webflow classes from `chain-gpt.shared.a3558708c.min.css` augmented by scoped CSS overrides in `<style>` where Webflow's legacy 5-card rules interfere.
- **Projects Grid Spacing**: Preserve `gap: 36px 28px !important;` on `projects.html` and `case-studies.html`.

---

## 4. Approaches Considered & Selected

### "How It Works" Section Layout
- **Alternative A: 4-Column Horizontal Progression (1 → 2 → 3 → 4)**:
  - *Trade-off*: Squeezes rich descriptions and dot bullet points into narrow columns on desktop.
- **Alternative B: Sequential 2x2 Grid (Selected by User)**:
  - *Details*: Step 1 & Step 2 span Row 1; Step 3 & Step 4 span Row 2.
  - *Benefits*: Provides generous reading width for each sprint stage, preserves natural reading flow (left-to-right, top-to-bottom), and stacks into a single column on mobile viewports (< 768px).

### Service Pages Migration
- **Alternative A: Minor styling tweaks to existing service pages**:
  - *Trade-off*: Leaves service pages on inconsistent custom grids (`.service-hero-container`), perpetuating visual misalignment.
- **Alternative B: Full Migration to Canonical Webflow Generator (Selected)**:
  - *Details*: Create an automated generator (`build_all_service_pages.py`) that outputs all 6 service pages using the exact 11-section Webflow template with domain-specific content, icons, and features.

---

## 5. Detailed Component Specifications

### 5.1. "How It Works" 2x2 Grid Architecture
In Webflow's stylesheet, `.landing-item-fourth` had hardcoded `grid-column: 2 / span 1; grid-row: 1 / span 2;`. We resolve this with scoped CSS applied to `.landing-hiw-list-wrapper`:
```css
.landing-hiw-list-wrapper,
.landing-hiw-list-wrapper.sca-hiw-list {
  display: grid !important;
  grid-template-columns: repeat(2, 1fr) !important;
  grid-template-rows: auto auto !important;
  gap: 24px !important;
}
.landing-hiw-item-wrapper {
  grid-column: auto !important;
  grid-row: auto !important;
  width: 100% !important;
  max-width: 100% !important;
  margin: 0 !important;
}
.landing-hiw-item {
  height: 100% !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: flex-start !important;
}
@media (max-width: 768px) {
  .landing-hiw-list-wrapper,
  .landing-hiw-list-wrapper.sca-hiw-list {
    grid-template-columns: 1fr !important;
  }
}
```
This guarantees Step 1 (top-left), Step 2 (top-right), Step 3 (bottom-left), Step 4 (bottom-right).

### 5.2. Relative Thumbnail Paths
- In `projects.html` and `case-studies.html`: Replace `/images/case-studies/` with `images/case-studies/`.
- In `projects/*.html`: Replace `/images/case-studies/` with `../images/case-studies/`.
- In all generator scripts (`build_agency_projects.py`, `build_project_subpages.py`): Update image path generators to emit clean relative paths.

### 5.3. Service Pages Migration
Update or create `build_all_service_pages.py` to regenerate the 6 service pages with all 11 canonical Webflow sections:
1. `web-design.html` (Bespoke UI/UX & Design Systems)
2. `webgl-3d.html` (3D & Spatial WebGL Studio)
3. `web-development.html` (Full-Stack Web Development)
4. `software-engineering.html` (Custom Software Engineering)
5. `ai-automation.html` (Autonomous AI Automation & Workflows)
6. `mobile-development.html` (Cross-Platform Mobile App Engineering)

### 5.4. Resources Purge & Navigation Cleanup
- Remove files: `blog.html`, `brand-kit.html`, `videos.html`.
- Remove "Resources" dropdown from `template_header.html` and mobile navigation drawer.
- Remove "Resources" column from `template_footer.html` (rebalance footer grid to 3 columns: Brand, Capabilities, Studio).
- Synchronize updated header and footer across all remaining pages.

---

## 6. Verification & Test Strategy (TDD)
1. **TDD Suite `test_hiw_grid_and_resources.py`**:
   - Assert `blog.html`, `brand-kit.html`, `videos.html` do not exist.
   - Assert "Resources" dropdown is absent in headers and footers across all pages.
   - Assert all image `src` attributes in `projects.html`, `case-studies.html`, and `projects/*.html` contain zero leading `/images/`.
   - Assert all 6 service pages and 3 company pages contain the 11 canonical Webflow sections and the 2x2 grid override.
   - Assert `index.html` hash remains identical to baseline.
2. **Execute Full Suite**:
   - Run `test_webflow_company_templates.py`.
   - Run `test_task_requirements.py`.
   - Run `test_projects_catalog.py`.
   - Run `test_projects_suite.py`.
   - Run `verify_all_pages_sync.py`.

