# CoinGPT Native Webflow Inner-Page Templates & Header Modernization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild non-homepage pages (`pricing.html`, `about.html`, `careers.html`, `contact-us.html`) into authentic Webflow inner-page templates matching `ai-trading-assistant.html`, restore the signature default Webflow header CTA button (`.btn-primary`), and redesign the CoinGPT logo with the site's neon cyber palette.

**Architecture:** Extract the master Webflow DOM patterns from `ai-trading-assistant.html` (hero grid, cut corners `[block-corners-top/bottom]`, badge title gradients, frosted bento cards, interactive FAQ accordions, and bottom CTA banner) and inject page-specific content into this framework. Modernize `template_header.html` and `template_footer.html` with the new SVG cyber logo and `.btn-primary` CTA, then propagate across all 24 pages.

**Tech Stack:** HTML5, Vanilla CSS / Webflow styles (`chain-gpt.shared.a3558708c.min.css`), Webflow JavaScript (`Lenis`, `Webflow.js`), `vector-nav.css`, `vector-nav.js`, Python (automation & verification).

**Spec:** [`docs/coingpt-webflow-template-design.md`](file:///c:/Users/new/Documents/coingpt/docs/coingpt-webflow-template-design.md)

## Global Constraints
- Every page must render with the Webflow base layout (`<body class="landing-body">` or matching container hierarchy) and include `chain-gpt.shared.a3558708c.min.css`.
- The header must use the native `.btn-primary` CTA button structure with multi-gradient border lines and cut corners.
- Brand logo must feature the geometric Cyber Neural Hexagon mark with neon emerald (`#00ffa3`), cyan (`#28efce`), and violet (`#6a59e5`) colors, with wordmark `CoinGPT` and `.tech` accent.
- All internal navigation links must resolve to `.html` endpoints without 404s.
- Interactive FAQ accordions must be functional with CSS/JS click toggles.

## Review Focus
1. Mobile viewport responsiveness: Navbar drawer toggles cleanly without content collision on `< 768px`.
2. Button hover fidelity: `.btn-primary` renders with 45° cut corners, dot accents, and animated gradient lines.
3. FAQ accordion interactivity: Clicking questions toggles answer visibility and rotates plus/cross icons smoothly.
4. Clean HTML links: Zero extensionless URLs (e.g. `/pricing`) that trigger 404 errors on static file servers.
5. Visual parity with `ai-trading-assistant.html`: Hero 2-column layout, section title badges, and bento cards match the live Webflow aesthetic.

---

### Task 1: Redesign Brand Logo and Restore Header `.btn-primary` CTA
**Files:**
- Modify: `c:/Users/new/Documents/coingpt/template_header.html`
- Modify: `c:/Users/new/Documents/coingpt/template_footer.html`
- Modify: `c:/Users/new/Documents/coingpt/vector-nav.css`
- Test: `c:/Users/new/Documents/coingpt/test_header_components.py`

**Interfaces:**
- Produces: Updated `template_header.html` containing the new SVG cyber logo and `.btn-primary` header button; updated `template_footer.html` matching CoinGPT branding.

- [ ] **Step 1: Write verification test for logo and CTA button**
  Create test script to verify that `template_header.html` contains:
  - CoinGPT logo SVG with `#00ffa3` and `#28efce` gradients.
  - Anchor with class `btn-primary` containing `.btn-primary-lines-1`, `.btn-primary-lines-2`, and `.btn-primary-text`.
  - Footer containing CoinGPT branding and updated logo.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python test_header_components.py`
  Expected: FAIL (missing `.btn-primary` and updated CoinGPT SVG in header).

- [ ] **Step 3: Update `template_header.html`, `template_footer.html`, and `vector-nav.css`**
  - Implement the Cyber Neural Hexagon SVG emblem in the header brand block.
  - Implement the exact `.btn-primary` structure inside `.vs-nav-actions` and mobile drawer.
  - Add required `.btn-primary` border line and chamfered corner styles to `vector-nav.css` if not already present.
  - Update `template_footer.html` with the new CoinGPT brand logo and copyright text.

- [ ] **Step 4: Run test to verify it passes**
  Run: `python test_header_components.py`
  Expected: PASS.

---

### Task 2: Build Native Webflow `pricing.html`
**Files:**
- Create/Overwrite: `c:/Users/new/Documents/coingpt/pricing.html`
- Test: `c:/Users/new/Documents/coingpt/verify_pricing_page.py`

**Interfaces:**
- Consumes: `template_header.html`, `template_footer.html`, Webflow styles from `ai-trading-assistant.html`.
- Produces: Complete Webflow-styled `pricing.html`.

- [ ] **Step 1: Write verification test for `pricing.html`**
  Verify `pricing.html` contains:
  - Header with `vs-navbar` and footer with `site-footer`.
  - Hero with `.section-title-bordered--gradient` and H1 "Transparent On-Chain Pricing".
  - Pricing tier grid with 3 cards (Free, Pro Trader, Enterprise API).
  - Monthly / Annual toggle button.
  - Interactive FAQ accordion (`.faq-2`).
  - Bottom CTA banner with `.btn-primary`.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python verify_pricing_page.py`
  Expected: FAIL (current `pricing.html` does not use the Webflow DOM layout).

- [ ] **Step 3: Build Webflow-styled `pricing.html`**
  Using the layout architecture of `ai-trading-assistant.html`, build the full page structure with Webflow classes, cut-corner blocks, pricing plan cards, feature lists, interactive FAQ accordion, and bottom CTA banner.

- [ ] **Step 4: Run test to verify it passes**
  Run: `python verify_pricing_page.py`
  Expected: PASS.

---

### Task 3: Build Native Webflow `about.html`
**Files:**
- Create/Overwrite: `c:/Users/new/Documents/coingpt/about.html`
- Test: `c:/Users/new/Documents/coingpt/verify_about_page.py`

**Interfaces:**
- Consumes: `template_header.html`, `template_footer.html`, Webflow styles.
- Produces: Complete Webflow-styled `about.html`.

- [ ] **Step 1: Write verification test for `about.html`**
  Verify `about.html` contains:
  - Hero with `.section-title-bordered--gradient` and H1 "Engineering the Intelligence Layer for Web3".
  - Stats section with holographic metrics (2M+ Queries, 450K+ Active Wallets, 99.98% Uptime).
  - Mission & Technology Pillars bento grid cards.
  - Leadership & core contributor cards with cut-corner image styling.
  - Interactive FAQ accordion and bottom conversion banner.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python verify_about_page.py`
  Expected: FAIL.

- [ ] **Step 3: Build Webflow-styled `about.html`**
  Implement the full Webflow page DOM tree with narrative, metrics, bento pillars, leadership showcase, and bottom banner.

- [ ] **Step 4: Run test to verify it passes**
  Run: `python verify_about_page.py`
  Expected: PASS.

---

### Task 4: Build Native Webflow `careers.html`
**Files:**
- Create/Overwrite: `c:/Users/new/Documents/coingpt/careers.html`
- Test: `c:/Users/new/Documents/coingpt/verify_careers_page.py`

**Interfaces:**
- Consumes: `template_header.html`, `template_footer.html`, Webflow styles.
- Produces: Complete Webflow-styled `careers.html`.

- [ ] **Step 1: Write verification test for `careers.html`**
  Verify `careers.html` contains:
  - Hero with `.section-title-bordered--gradient` and H1 "Build the Future of Decentralized AI".
  - Culture and perks bento cards (Global Remote, Token Grants, Retreats, Tooling Budget).
  - Open positions listing with department tags and "Apply" buttons.
  - Hiring process timeline with 4 distinct phases.
  - Interactive FAQ accordion and bottom CTA banner.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python verify_careers_page.py`
  Expected: FAIL.

- [ ] **Step 3: Build Webflow-styled `careers.html`**
  Construct the complete Webflow inner-page layout for Careers with interactive role filters, perks bento, and application modal/link.

- [ ] **Step 4: Run test to verify it passes**
  Run: `python verify_careers_page.py`
  Expected: PASS.

---

### Task 5: Build Native Webflow `contact-us.html`
**Files:**
- Create/Overwrite: `c:/Users/new/Documents/coingpt/contact-us.html`
- Test: `c:/Users/new/Documents/coingpt/verify_contact_page.py`

**Interfaces:**
- Consumes: `template_header.html`, `template_footer.html`, Webflow styles.
- Produces: Complete Webflow-styled `contact-us.html`.

- [ ] **Step 1: Write verification test for `contact-us.html`**
  Verify `contact-us.html` contains:
  - Hero with `.section-title-bordered--gradient` and H1 "Connect With CoinGPT Engineering & Partnerships".
  - 2-column layout: Left column with office hubs, direct inquiry emails, Telegram/Discord community cards; Right column with Webflow styled contact form (`.form-field`, `.label-moved`).
  - Interactive FAQ accordion for common support inquiries.
  - Bottom conversion banner.

- [ ] **Step 2: Run test to verify it fails**
  Run: `python verify_contact_page.py`
  Expected: FAIL.

- [ ] **Step 3: Build Webflow-styled `contact-us.html`**
  Implement the Webflow contact layout with working form validation states, channel directory, and FAQ accordion.

- [ ] **Step 4: Run test to verify it passes**
  Run: `python verify_contact_page.py`
  Expected: PASS.

---

### Task 6: Synchronize Header, Footer, and Branding Across All Pages
**Files:**
- Script: `c:/Users/new/Documents/coingpt/sync_all_pages.py`
- Modify: All remaining 20 HTML files in the repository
- Test: `c:/Users/new/Documents/coingpt/verify_all_pages_sync.py`

**Interfaces:**
- Consumes: Updated `template_header.html` and `template_footer.html`.
- Produces: 100% synchronized header and footer across all 24 pages in `c:/Users/new/Documents/coingpt`.

- [ ] **Step 1: Write synchronization and validation script**
  Verify that all 24 HTML pages have:
  - Exact updated CoinGPT logo and `.btn-primary` header button.
  - Consistent footer.
  - Correct `.html` internal links.
  - Title tags containing `CoinGPT`.

- [ ] **Step 2: Run synchronization script**
  Run: `python sync_all_pages.py`

- [ ] **Step 3: Verify all 24 pages pass validation**
  Run: `python verify_all_pages_sync.py`
  Expected: PASS (24/24 pages validated).

---

### Task 7: End-to-End Verification with Browser Subagent
**Files:**
- Artifact: `task.md`

- [ ] **Step 1: Launch local web server on port 3000**
- [ ] **Step 2: Perform automated browser checks via `browser_subagent`**
  - Verify `index.html`: Header `.btn-primary` renders with cut corners and animated border lines.
  - Verify logo: Renders CoinGPT with cyber neon gradient colors.
  - Navigate to `pricing.html`: Verify Webflow hero, bento cards, and interactive FAQ accordion.
  - Navigate to `about.html`: Verify metrics, pillars bento, and leadership cards.
  - Navigate to `careers.html`: Verify role listings and perks bento.
  - Navigate to `contact-us.html`: Verify 2-column contact channels and styled form.
  - Confirm mobile responsiveness and navigation drawer behavior.
