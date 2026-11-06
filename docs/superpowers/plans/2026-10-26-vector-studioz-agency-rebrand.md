# Vector Studioz Agency Rebrand & Webflow Template Realignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebrand the website to **Vector Studioz** (elite web design, full-stack software development, and AI automation agency), remove all green icon boxes from the menu, apply vibrant rainbow spectrum gradients to the signature Webflow `.btn-primary` CTA button, overhaul inner-page content (`pricing.html`, `about.html`, `careers.html`, `contact-us.html`), and synchronize all 24 pages.

**Architecture:** Update master components `template_header.html` (Vector Studioz emblem, clean typographic menu, rainbow `.btn-primary` CTA), `template_footer.html`, and `vector-nav.css`. Generate authentic Webflow inner-page templates using agency-specific content models and Webflow components (`landing-body`, cut-corner blocks, bento cards, `.faq-2` accordions, bottom CTA banner), then propagate universally across all 24 pages.

**Tech Stack:** HTML5, CSS3, Webflow Stylesheet (`chain-gpt.shared.a3558708c.min.css`), `vector-nav.css`, `vector-nav.js`, Python (generators & verification).

**Spec:** [`docs/superpowers/specs/2026-10-26-vector-studioz-agency-rebrand-design.md`](file:///c:/Users/new/Documents/coingpt/docs/superpowers/specs/2026-10-26-vector-studioz-agency-rebrand-design.md)

## Global Constraints
- Target brand is **Vector Studioz** across all titles, headers, wordmarks, and footers.
- Absolutely zero references to cryptocurrencies, coins, trading signals, blockchain audits, tokens, or CoinGPT.
- The navigation menu must NOT contain green icon boxes or accents; presentation must be clean, elegant agency typography.
- The `.btn-primary` CTA button must feature vibrant, animated rainbow chromatic gradients (`#ff007a`, `#ff8a00`, `#ffe600`, `#00ffa3`, `#00e1ff`, `#7928ca`) with 45° chamfered cut corners.
- All internal links must resolve cleanly to `.html` endpoints without 404 errors.

## Review Focus
1. Header CTA button rendering: The rainbow chromatic gradient lines render cleanly without visual clipping across Chrome/Edge.
2. Menu typography: Dropdown entries have removed green icon boxes while retaining readable hierarchy and smooth hover states.
3. Agency content integrity: All 4 inner pages (`pricing.html`, `about.html`, `careers.html`, `contact-us.html`) speak purely of web design, software development, and AI automation.
4. Accordion interactivity: FAQ questions expand/collapse smoothly and toggle plus/cross icons.
5. Universal sync: All 24 pages display the unified Vector Studioz header and footer with 0 broken links.

---

### Task 1: Vector Studioz Brand Logo, Clean Navigation Menu & Rainbow CTA Button
**Files:**
- Modify: `c:/Users/new/Documents/coingpt/template_header.html`
- Modify: `c:/Users/new/Documents/coingpt/template_footer.html`
- Modify: `c:/Users/new/Documents/coingpt/vector-nav.css`
- Test: `c:/Users/new/Documents/coingpt/test_vector_header.py`

**Interfaces:**
- Produces: `template_header.html` containing Vector Studioz SVG logo, clean agency menu without green icon boxes, and rainbow `.btn-primary` CTA button; `template_footer.html` with agency copyright and links.

- [ ] **Step 1: Write verification test `test_vector_header.py`**
  Verify `template_header.html` and `vector-nav.css` contain:
  - Vector Studioz brand text and custom Vector SVG logo.
  - Zero `.vs-dropdown-icon` green container elements.
  - Agency service titles (*Web Design & UI/UX*, *Full-Stack Development*, *Custom Software*, *AI Automation*, *3D & WebGL*).
  - Rainbow gradient definitions on `.btn-primary` (`#ff007a`, `#ff8a00`, `#ffe600`, `#00ffa3`, `#00e1ff`, `#7928ca`).
  - Text: "Start a Project" inside `.btn-primary-text`.
  - Vector Studioz copyright in `template_footer.html`.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python test_vector_header.py`
  Expected: FAIL (currently contains CoinGPT and green icons).

- [ ] **Step 3: Update `template_header.html`, `template_footer.html`, and `vector-nav.css`**
  - Implement dynamic geometric Vector Studioz SVG logo emblem and `Vector Studioz` wordmark.
  - Strip out all green icon boxes (`.vs-dropdown-icon`) from navigation dropdowns.
  - Restructure dropdown links around core agency services.
  - Add chromatic rainbow gradient CSS to `.btn-primary`, `.btn-primary-lines-1`, and `.btn-primary-lines-2` with ambient rainbow glow in `vector-nav.css`.
  - Update `template_footer.html` with Vector Studioz branding.

- [ ] **Step 4: Run test to verify it passes**
  Run: `python test_vector_header.py`
  Expected: PASS.

---

### Task 2: Build Agency Native Webflow `pricing.html`
**Files:**
- Modify: `c:/Users/new/Documents/coingpt/pricing.html`
- Create: `c:/Users/new/Documents/coingpt/build_agency_pricing.py`
- Test: `c:/Users/new/Documents/coingpt/verify_agency_pricing.py`

**Interfaces:**
- Consumes: `template_header.html`, `template_footer.html`, `vector-nav.css`
- Produces: Agency-focused `pricing.html` with engagement tiers, retainers, and scope FAQs.

- [ ] **Step 1: Write verification test `verify_agency_pricing.py`**
  Verify `pricing.html`:
  - Contains `Vector Studioz` branding, 0 mentions of crypto/tokens/trading.
  - Contains 3 agency engagement tiers (*Design Sprint & MVP*, *Dedicated Product Team Retainer*, *Enterprise Bespoke Systems*).
  - Contains monthly/annual retainer toggle.
  - Contains at least 4 agency scope FAQs.
  - Contains rainbow `.btn-primary` CTA buttons.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python verify_agency_pricing.py`
  Expected: FAIL.

- [ ] **Step 3: Implement `build_agency_pricing.py` and generate `pricing.html`**
  - Build 2-column hero: *"Transparent Models for Ambitious Products"*.
  - Render 3 pricing tiers with cut corners and feature checklists.
  - Include monthly/annual toggle and agency FAQ accordion.
  - Run: `python build_agency_pricing.py`

- [ ] **Step 4: Run test to verify it passes**
  Run: `python verify_agency_pricing.py`
  Expected: PASS.

---

### Task 3: Build Agency Native Webflow `about.html`
**Files:**
- Modify: `c:/Users/new/Documents/coingpt/about.html`
- Create: `c:/Users/new/Documents/coingpt/build_agency_about.py`
- Test: `c:/Users/new/Documents/coingpt/verify_agency_about.py`

**Interfaces:**
- Consumes: `template_header.html`, `template_footer.html`
- Produces: Agency-focused `about.html` with agency stats bento, 4 craft pillars, and leadership.

- [ ] **Step 1: Write verification test `verify_agency_about.py`**
  Verify `about.html`:
  - Contains `Vector Studioz` branding, 0 mentions of crypto/blockchain/nodes.
  - Contains agency stats: `140+ Projects Delivered`, `99.2% Client Retention`, `12 Design Awards`.
  - Contains 4 agency pillars (*Bespoke Visual Excellence*, *Scalable Architecture*, *Intelligent AI Workflows*, *Relentless Execution*).
  - Contains agency leadership team and agency FAQ.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python verify_agency_about.py`
  Expected: FAIL.

- [ ] **Step 3: Implement `build_agency_about.py` and generate `about.html`**
  - Build 2-column hero: *"We Craft Digital Experiences That Define Categories"*.
  - Render holographic stats bento, craft pillars, leadership grid, and interactive `.faq-2` accordion.
  - Run: `python build_agency_about.py`

- [ ] **Step 4: Run test to verify it passes**
  Run: `python verify_agency_about.py`
  Expected: PASS.

---

### Task 4: Build Agency Native Webflow `careers.html`
**Files:**
- Modify: `c:/Users/new/Documents/coingpt/careers.html`
- Create: `c:/Users/new/Documents/coingpt/build_agency_careers.py`
- Test: `c:/Users/new/Documents/coingpt/verify_agency_careers.py`

**Interfaces:**
- Consumes: `template_header.html`, `template_footer.html`
- Produces: Agency-focused `careers.html` with design & engineering open roles, culture bento, and perks.

- [ ] **Step 1: Write verification test `verify_agency_careers.py`**
  Verify `careers.html`:
  - Contains `Vector Studioz` branding, 0 mentions of crypto/blockchain.
  - Contains at least 4 open agency roles (*Senior Product Designer*, *Lead Full-Stack Architect*, *AI Solutions Engineer*, *Creative WebGL Developer*).
  - Contains 4-stage agency hiring pipeline and perks grid.
  - Contains interactive `.faq-2` accordion.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python verify_agency_careers.py`
  Expected: FAIL.

- [ ] **Step 3: Implement `build_agency_careers.py` and generate `careers.html`**
  - Build hero: *"Join the Creative & Engineering Vanguard"*.
  - Render culture bento, open role cards, hiring pipeline, perks grid, and interactive FAQ.
  - Run: `python build_agency_careers.py`

- [ ] **Step 4: Run test to verify it passes**
  Run: `python verify_agency_careers.py`
  Expected: PASS.

---

### Task 5: Build Agency Native Webflow `contact-us.html`
**Files:**
- Modify: `c:/Users/new/Documents/coingpt/contact-us.html`
- Create: `c:/Users/new/Documents/coingpt/build_agency_contact.py`
- Test: `c:/Users/new/Documents/coingpt/verify_agency_contact.py`

**Interfaces:**
- Consumes: `template_header.html`, `template_footer.html`
- Produces: Agency-focused `contact-us.html` with client project intake form and studio channels.

- [ ] **Step 1: Write verification test `verify_agency_contact.py`**
  Verify `contact-us.html`:
  - Contains `Vector Studioz` branding, 0 mentions of crypto/audits/nodes.
  - Contains direct agency contact channels (`projects@vectorstudioz.com`, `hello@vectorstudioz.com`).
  - Contains client project intake form (Name, Company, Work Email, Project Type, Estimated Budget, Timeline, Message).
  - Contains rainbow CTA submit button.
  - Contains discovery FAQ accordion.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python verify_agency_contact.py`
  Expected: FAIL.

- [ ] **Step 3: Implement `build_agency_contact.py` and generate `contact-us.html`**
  - Build 2-column layout pairing agency communication hubs with interactive intake form.
  - Run: `python build_agency_contact.py`

- [ ] **Step 4: Run test to verify it passes**
  Run: `python verify_agency_contact.py`
  Expected: PASS.

---

### Task 6: Universal Header & Footer Synchronization Across All 24 Pages
**Files:**
- Modify: all 24 `.html` files in project root
- Script: `c:/Users/new/Documents/coingpt/sync_all_pages.py`
- Test: `c:/Users/new/Documents/coingpt/verify_all_pages_sync.py`

**Interfaces:**
- Consumes: `template_header.html`, `template_footer.html`
- Produces: Synchronized pages across the entire repository.

- [ ] **Step 1: Update `verify_all_pages_sync.py` to assert Vector Studioz branding**
  Ensure test checks for `Vector Studioz` in header/footer, 0 `CoinGPT` references, rainbow CTA button, and 0 green icon containers.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python verify_all_pages_sync.py`
  Expected: FAIL.

- [ ] **Step 3: Run `sync_all_pages.py` to update all 24 pages**
  Run: `python sync_all_pages.py`

- [ ] **Step 4: Run test to verify it passes**
  Run: `python verify_all_pages_sync.py`
  Expected: PASS.

---

### Task 7: Full System Verification & Interactive Validation
**Files:**
- Test runner: `verify_all_agency_suites.py`

- [ ] **Step 1: Execute all test suites**
  Run: `python -c "import subprocess, sys; tests=['test_vector_header.py','verify_agency_pricing.py','verify_agency_about.py','verify_agency_careers.py','verify_agency_contact.py','verify_all_pages_sync.py']; sys.exit(0 if all(subprocess.run(['python',t]).returncode==0 for t in tests) else 1)"`
  Expected: ALL TEST SUITES PASS.

- [ ] **Step 2: Visual validation in browser**
  Check `http://localhost:3000/index.html`, `http://localhost:3000/pricing.html`, `http://localhost:3000/about.html`, `http://localhost:3000/careers.html`, `http://localhost:3000/contact-us.html`.
  Confirm:
  - Vector Studioz logo emblem
  - Rainbow chromatic gradient on CTA button
  - No green icon boxes in menu
  - 100% agency web design, software development, and AI automation copy.
