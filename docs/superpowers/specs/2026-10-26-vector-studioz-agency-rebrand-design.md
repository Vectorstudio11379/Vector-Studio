# Vector Studioz Agency Rebrand & Webflow Template Realignment Design Document

**Date:** 2026-10-26  
**Status:** Pending User Approval  
**Scope:** Universal Brand, Header, Menu, CTA Button, and Inner-Page Content Overhaul  
**Target Brand:** Vector Studioz (Elite Web Design, Full-Stack Development, Software Engineering & AI Automation Agency)

---

## 1. Intent & Context
Vector Studioz is an elite digital experience agency delivering bespoke websites, high-performance web applications, custom enterprise software, and autonomous AI automation systems for high-growth brands.

During earlier template modernization, reference URLs from `coingpt.tech` (used solely to demonstrate layout patterns) led to cryptocurrency, token trading, and on-chain blockchain copy displacing Vector Studioz. This design document establishes the comprehensive plan to:
1. Restore and elevate the **Vector Studioz** brand identity across the entire site.
2. Remove all green icon boxes from the navigation menu for a clean, editorial agency aesthetic.
3. Apply a vibrant **rainbow spectrum gradient** to the signature Webflow `.btn-primary` CTA button.
4. Rewrite the 4 rebuilt Webflow inner-page templates (`pricing.html`, `about.html`, `careers.html`, `contact-us.html`) with 100% agency-focused services, deliverables, client proof, and career opportunities.
5. Synchronize the master header and footer across all 24 pages.

---

## 2. Goals, Non-Goals, and Anti-Goals

### Goals
- **Brand Identity**: Implement a modern, multi-faceted geometric Vector logo mark (SVG) alongside the `Vector Studioz` wordmark.
- **Rainbow CTA Button**: Style the native Webflow `.btn-primary` CTA button with multi-hued chromatic rainbow gradient lines (`#ff007a` $\to$ `#ff8a00` $\to$ `#ffe600` $\to$ `#00ffa3` $\to$ `#00e1ff` $\to$ `#7928ca`), chamfered 45° cut corners, glowing dot accents, and smooth hover dynamics.
- **Clean Services Dropdown**: Strip out the green icon boxes/accents in the dropdown menu. Organize services into clear agency capabilities:
  1. *Web Design & UI/UX*
  2. *Full-Stack Web Development*
  3. *Custom Software Engineering*
  4. *AI Automation & Workflow Agents*
  5. *3D & WebGL Interactive Experiences*
  6. *Mobile Applications (iOS / Android)*
- **Agency Content Overhaul**:
  - `pricing.html`: Agency engagement models (*Sprint Prototype*, *Dedicated Product Team Retainer*, *Enterprise Custom Software & AI Systems*), deliverables checklists, and agency FAQ.
  - `about.html`: Vector Studioz agency story, verified client proof metrics (140+ shipped products, 99.2% satisfaction rate, 12 international design awards), 4 craft pillars, and leadership team.
  - `careers.html`: Agency culture, remote flexibility, 5 open agency roles (*Senior Product Designer*, *Lead Full-Stack Architect*, *AI Automation Engineer*, *Creative WebGL Developer*, *Technical Project Lead*), hiring pipeline, and studio perks.
  - `contact-us.html`: Project onboarding matrix, budget and timeline selectors, direct studio contact channels (`hello@vectorstudioz.com`, `projects@vectorstudioz.com`), and discovery call FAQs.
- **Universal Synchronization**: Re-sync all 24 HTML pages with `template_header.html` and `template_footer.html`.

### Non-Goals
- Altering the underlying Webflow styling system (`chain-gpt.shared.a3558708c.min.css`) or breaking responsive grid classes.
- Adding third-party UI framework dependencies.

### Anti-Goals
- Zero remnants of crypto trading, tokens, coins, on-chain signals, mempools, or CoinGPT branding anywhere on the site.

---

## 3. Approaches Considered & Decision

| Approach | Description | Trade-offs | Verdict |
| :--- | :--- | :--- | :--- |
| **Approach 1: Comprehensive Agency Transformation** | Full brand overhaul, clean menu without green icons, rainbow CTA button, agency content on all inner pages, and universal 24-page sync. | Requires rewriting copy across 4 pages and updating templates. | **Selected (User Approved)** |
| **Approach 2: Header & Menu Re-Skin Only** | Replaces header logo and menu labels, leaving inner-page body copy unchanged. | Leaves severe contradictions where inner pages still discuss crypto coins and decentralized node networks. | **Rejected** |
| **Approach 3: Phased Overhaul** | Updates header first, then inner pages one-by-one over multiple iterations. | Slower, produces intermediate inconsistent states across the live site. | **Rejected** |

---

## 4. Technical Architecture & Component Specifications

### 4.1. Brand Identity & Logo
- **Emblem**: Custom SVG vector mark composed of dynamic angular facets representing precision, multidimensional engineering, and agency craft.
- **Wordmark**: `Vector Studioz` set in `Inter` (weight 800, tracking -0.03em) with a subtle studio accent badge (`.studio` or `Agency`).

### 4.2. Rainbow CTA Button (`.btn-primary`)
- **Structure**:
  ```html
  <a class="btn-primary ml-auto w-inline-block" href="contact-us.html" scramble-link="">
    <div class="btn-primary-lines btn-primary-lines-1">
      <div class="btn-primary-lines btn-primary-lines-2">
        <div class="btn-primary-text" scramble-text="">Start a Project</div>
      </div>
    </div>
  </a>
  ```
- **Styling**:
  - Border gradient: `linear-gradient(135deg, #ff007a 0%, #ff8a00 20%, #ffe600 40%, #00ffa3 60%, #00e1ff 80%, #7928ca 100%)`.
  - Animated border lines and glowing corner dot accents utilizing the chromatic spectrum.
  - Hover state with ambient rainbow blur glow.

### 4.3. Navigation Menu (`template_header.html`)
- Remove all `<div class="vs-dropdown-icon">` and `<svg>` green icon boxes.
- Clean typographic presentation:
  - Title: Crisp, bold agency capability title.
  - Description: 1-line client outcome statement.
  - Subtle badge tags (`Bespoke`, `Scalable`, `Autonomous`, `Spatial`).
- Active link routing to existing agency `.html` pages.

### 4.4. Inner-Page Content Models
1. **`pricing.html`**:
   - Hero: *"Transparent Models for Ambitious Products"*.
   - 3 Tiers:
     - **Design Sprint & MVP**: Rapid 3-4 week concept, high-fidelity Figma prototype, and interactive Webflow/React build.
     - **Dedicated Product Team (Retainer)**: Ongoing monthly agile squad (Senior Designer, 2 Senior Engineers, QA) for fast-scaling startups.
     - **Enterprise Custom Systems**: End-to-end bespoke software engineering, multi-agent AI automation, and high-availability cloud architecture.
   - Interactive monthly/annual toggle with retainer savings.
   - Agency FAQs (IP ownership, revisions, billing, handoff).
2. **`about.html`**:
   - Hero: *"We Craft Digital Experiences That Define Categories"*.
   - Holographic Stats Bento: `140+ Projects Delivered`, `99.2% Client Retention`, `12 Design Awards`, `5.0★ Clutch Rating`.
   - 4 Pillars: Bespoke Visual Excellence, Scalable Modern Architecture, Intelligent AI Workflows, Relentless Execution.
   - Leadership Team: Creative Director, Head of Engineering, AI Solutions Architect, Head of Client Success.
3. **`careers.html`**:
   - Hero: *"Join the Creative & Engineering Vanguard"*.
   - Culture Bento: Creative Autonomy, Craft Over Bureaucracy, 100% Remote Flexibility, High-Trust Environment.
   - 5 Open Roles: Senior Product Designer, Lead Full-Stack Architect, AI Automation Engineer, Creative WebGL Developer, Technical Project Lead.
   - 4-Stage Hiring Process & Studio Perks ($4,000 workspace budget, profit share, global retreats).
4. **`contact-us.html`**:
   - 2-Column Matrix:
     - Left: Direct project inquiries (`projects@vectorstudioz.com`), studio partnerships (`hello@vectorstudioz.com`), office locations (San Francisco, London).
     - Right: Interactive client intake form (Name, Company, Project Type, Estimated Budget Range, Timeline, Project Goals).

---

## 5. Verification & Testing Strategy
- Automated Python test suites:
  1. `test_vector_header.py`: Verifies `Vector Studioz` branding, rainbow CTA gradients, and removal of green icon containers.
  2. `verify_agency_pricing.py`: Verifies agency engagement tiers, retainer models, and pricing FAQ.
  3. `verify_agency_about.py`: Verifies agency stats, craft pillars, and team.
  4. `verify_agency_careers.py`: Verifies open roles, culture bento, and agency benefits.
  5. `verify_agency_contact.py`: Verifies intake form, studio channels, and discovery process.
  6. `verify_all_pages_sync.py`: Verifies universal header, footer, and zero broken links across all 24 pages.
- Visual browser verification: End-to-end inspection of desktop, mobile drawer, and interactive accordions.
