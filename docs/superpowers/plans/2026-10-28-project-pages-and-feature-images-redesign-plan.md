# Implementation Plan: Webflow Project Pages Migration & Bespoke Vector Studioz Feature Banners

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal**:
1. Upgrade `projects.html`, `case-studies.html`, and all 15 single project subpages (`projects/*.html`) to the canonical Webflow page template layout (Webflow Hero with video & ticker bar, Webflow card grids with corner cuts, Webflow badges, and closing Webflow CTA banner).
2. Fix broken thumbnails in the project catalog (specifically replacing the Cloudflare verification white screen for ICL Virtual Services with a bespoke dark-themed agency dashboard graphic) and purge all residual crypto/token mentions.
3. Replace the Webflow crypto chatbot screenshots (`item 1 desk.png` / `item 2 desk.png` featuring "$CGPT", "Trending Coins", "DeFi", and "Crypto Market Analysis") across all company pages (`about.html`, `careers.html`, `contact-us.html`) and all 6 service pages with bespoke dark Vector Studioz UI graphics (Design Tokens, WebGL Shaders, Full-Stack Architecture, AI Multi-Agent Swarms, Mobile Apps).
4. Maintain `index.html` SHA-256 frozen baseline (`96e040f788d68ea79d1f28f58e7d0def11957a8d9779c8bc798b747a02fdced7`).

---

### Task 1: Generate Custom Dark-Mode UI Feature Banners & Fix ICL Thumbnail

**Files:**
- Create: `images/features/vector-design-system.png`
- Create: `images/features/vector-webgl-shader.png`
- Create: `images/features/vector-fullstack-telemetry.png`
- Create: `images/features/vector-cloud-architecture.png`
- Create: `images/features/vector-ai-agents.png`
- Create: `images/features/vector-mobile-apps.png`
- Replace: `images/case-studies/iclvirtualservices.png`

- [x] **Step 1: Generate high-resolution dark mockups for Vector Studioz disciplines using Pillow/SVG rendering or `generate_image`**
- [x] **Step 2: Replace Cloudflare challenge screen for ICL Virtual Services with dark agency talent platform mockup**
- [x] **Step 3: Update `projects_data.py` to point to `images/case-studies/iclvirtualservices.png` and clean any token/contract text**

---

### Task 2: Replace Crypto Chatbot Screenshots in Company & Service Pages

**Files:**
- Modify: `build_webflow_company_pages.py`
- Modify: `build_all_service_pages.py`
- Modify: `about.html`, `careers.html`, `contact-us.html`
- Modify: 6 service pages (`web-design.html`, `webgl-3d.html`, `web-development.html`, `software-engineering.html`, `ai-automation.html`, `mobile-development.html`) and mirrors

- [x] **Step 1: Update `build_webflow_company_pages.py` to use local Vector Studioz feature graphics**
- [x] **Step 2: Update `build_all_service_pages.py` to bind tailored domain feature graphics to each service**
- [x] **Step 3: Regenerate company pages and all 6 service pages**
- [x] **Step 4: Verify with `test_webflow_company_templates.py` and `test_agency_services_pages.py`**

---

### Task 3: Migrate `projects.html` & `case-studies.html` to Canonical Webflow Template

**Files:**
- Modify: `build_agency_projects.py`
- Modify: `projects.html`
- Modify: `case-studies.html`

- [x] **Step 1: Implement canonical Webflow Hero (`landing-hero-2` with video asset, ticker bar, badge) in `build_agency_projects.py`**
- [x] **Step 2: Align 3-column project card grid with Webflow card styles, corner cuts, and preserved `gap: 36px 28px !important;`**
- [x] **Step 3: Add canonical Webflow Closing CTA banner (`landing-cta` with robot aura)**
- [x] **Step 4: Regenerate `projects.html` and `case-studies.html`**
- [x] **Step 5: Verify with `test_projects_catalog.py` and `test_case_studies_thumbnails.py`**

---

### Task 4: Migrate All 15 Single Project Subpages (`projects/*.html`) to Canonical Webflow Template

**Files:**
- Modify: `build_project_subpages.py`
- Modify: `projects/*.html` (15 files)

- [x] **Step 1: Upgrade subpage layout to Webflow section architecture (Webflow Hero with breadcrumbs, live indicators, and 16:9 preview media)**
- [x] **Step 2: Structure project narrative with Webflow `item-50` corner-cut cards and glowing KPI metric badges**
- [x] **Step 3: Add canonical Webflow Closing CTA banner to subpages**
- [x] **Step 4: Regenerate all 15 subpages via `python build_project_subpages.py`**
- [x] **Step 5: Verify with `test_projects_suite.py`**

---

### Task 5: Full Regression Testing & Baseline Audit

**Files:**
- Run: `test_hiw_grid_and_resources.py`
- Run: `test_webflow_company_templates.py`
- Run: `test_agency_services_pages.py`
- Run: `test_case_studies_thumbnails.py`
- Run: `test_projects_catalog.py`
- Run: `test_projects_suite.py`
- Run: `test_task_requirements.py`
- Run: `verify_all_pages_sync.py`

- [x] **Step 1: Run all test suites and confirm 100% green**
- [x] **Step 2: Verify `index.html` SHA-256 hash strictly equals `96e040f788d68ea79d1f28f58e7d0def11957a8d9779c8bc798b747a02fdced7`**

