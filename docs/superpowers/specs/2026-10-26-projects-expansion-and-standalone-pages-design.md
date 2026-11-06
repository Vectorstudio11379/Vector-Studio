# Vector Studioz — Projects Expansion & Dedicated Subpages Design Document

## 1. Intent & Purpose
Vector Studioz is evolving its client portfolio representation by transitioning all showcase sections, navigation entries, and pages from "Case Studies" to the agency standard **"Projects"**. In addition, the agency portfolio is expanding from 10 to 15 real-world production platforms, featuring newly added live client websites, each equipped with its own dedicated standalone subpage (`projects/<slug>.html`) delivering comprehensive project breakdowns, tech stack architectures, key impact metrics, and direct live website links.

---

## 2. Goals, Non-Goals & Anti-Goals

### Goals
- **Nomenclature & Page Transition**:
  - Rename "Case Studies" to **"Projects"** across the global header navigation, mobile drawer menu, footer columns, breadcrumbs, and homepage section tabs (`index.html#projects`).
  - Transition the primary catalog from `case-studies.html` to `projects.html` while maintaining `case-studies.html` as a synchronized mirror/redirect for link preservation.
- **Project Expansion (15 Client Platforms)**:
  - Add the 6 client platforms specified by the user:
    1. **Messulogic** (`https://mesuullogic.com/`) — Enterprise EdTech & Learning Management System.
    2. **ExpressTeck** (`https://expressteck.tech/`) — Tech Innovation, Interactive Courses & Digital Training Academy.
    3. **Lake Greenfield Hotel** (`https://lakegreenfieldhotel.com/`) — Luxury Boutique Hospitality & Direct Booking Platform.
    4. **icL Virtual Services** (`https://iclvirtualservices.com/`) — Operational Excellence Assistant & Remote Talent Management (replaces legacy placeholder).
    5. **Mirola Cleaning Services** (`https://mirolacleaningservices.com/`) — Commercial Janitorial & Facility Sanitization Portal.
    6. **Mirola Enterprise Nigeria** (`https://mirolanigeria.com/`) — Digital & Remote Work Skills Development Hub.
  - Retain and elevate the existing 9 active projects:
    7. **Beacon Corporate Realty** (`https://beaconcorporaterealty.com`)
    8. **Twist Studio / JumboDTG** (`https://jumbodtg.com/`)
    9. **Resilient Solutions**
    10. **Mirola Ambassador Platform**
    11. **MIRODATA**
    12. **Cleaner Spaces**
    13. **5th Element Media Group**
    14. **Aliola Global Services**
    15. **Tom Ojo Sports Academy**
- **Dedicated Standalone Subpages**:
  - Generate a full, standalone HTML page for each project under `projects/<slug>.html`.
  - Each subpage contains:
    - Global Vector Studioz header & navigation (with "Projects" marked active).
    - Hero section with title, subtitle, industry pill, launch year, and "Visit Live Website" outbound CTA.
    - Full-bleed 16:9 cinematic screenshot showcase.
    - Project Overview & Client Background.
    - Strategic Challenges & Business Objectives.
    - Architectural Solutions & Engineering Highlights.
    - Core Technologies & Stack Badges (e.g. Next.js, React, Liquid, WordPress, PHP, Tailwind CSS).
    - Quantifiable Business Results & Impact Metrics (e.g., Conversion uplift, Lighthouse scores, engagement rates).
    - Client Testimonial / Impact Quote.
    - "Next Project" / "Back to All Projects" cross-navigation.
    - Global Vector Studioz footer.
- **Homepage Slider & Catalog Grid Sync**:
  - Update `index.html` slider (`#case-slider`) to showcase all projects with 16:9 widescreen thumbnails and direct links to either their standalone project subpage or live site.
  - Update `projects.html` with an interactive 2-column widescreen card grid, filter tags (All, Web Design, SaaS & Cloud, EdTech, Operations & Enterprise, E-Commerce), and deep links to the dedicated subpages.
- **Global Header/Footer Synchronization**:
  - Update all 24 website pages to reflect "Projects" in header nav and footer columns.

### Non-Goals
- Requiring a dynamic database, server runtime, or external CMS. All pages are compiled as ultra-fast static HTML with zero runtime lag.
- Modifying core agency branding (remains strictly **Vector Studioz**).

### Anti-Goals
- No placeholder, dummy, or broken external links.
- No regression back to letterboxed, duplicate background, or low-aspect-ratio thumbnails. All imagery maintains strict `16:9` cinematic presentation.
- No leftover cryptocurrency references anywhere on the site.

---

## 3. Evaluated Approaches & Selection

### Approach 1: Structured Project Data Architecture (Selected)
- **Concept**: Define a single source of truth in Python (`projects_data.py`) modeling all 15 projects with complete copy, metadata, technology tags, metrics, and live URLs. Compile `projects.html`, `index.html` slider, and all 15 standalone `projects/<slug>.html` pages via automated SSG script.
- **Rationale**: 100% design consistency, zero risk of broken links, unified styling via `vector-nav.css`, and blazing fast load times. Chosen directly by user.

### Approach 2: Bespoke Hand-Coded Subpages (Rejected)
- **Concept**: Write 15 disconnected HTML files manually from scratch.
- **Trade-off**: High risk of styling drift, broken cross-links, and slow maintenance.

### Approach 3: Dynamic Single-Template Viewer (Rejected)
- **Concept**: One `project.html?id=slug` page loading content via client-side JavaScript.
- **Trade-off**: Poor SEO indexing, flash of unstyled content, no true static URL structure.

---

## 4. Architectural & Implementation Specifications

### 4.1 Data Schema (`projects_data.py`)
Each of the 15 projects will define:
```python
{
    'slug': 'mesuullogic',
    'title': 'Messulogic — Enterprise EdTech & Learning Management Platform',
    'short_title': 'Messulogic',
    'client': 'Messulogic Technologies',
    'category': 'EdTech & Learning Management',
    'industry': 'Education & Digital Skills',
    'year': '2025',
    'live_url': 'https://mesuullogic.com/',
    'thumbnail': '/images/case-studies/mesuullogic.jpg',
    'tagline': 'Scalable Learning Management Architecture & Student Portal',
    'metrics': [
        {'value': '10K+', 'label': 'Active Learners'},
        {'value': '99.9%', 'label': 'Platform Uptime'},
        {'value': '< 1.2s', 'label': 'Course Load Speed'}
    ],
    'overview': '...',
    'challenge': '...',
    'solution': '...',
    'tech_stack': ['WordPress', 'LMS Engine', 'WooCommerce', 'PHP', 'Tailwind CSS', 'CDN Edge'],
    'testimonial': {'quote': '...', 'author': '...', 'role': '...'}
}
```

### 4.2 File Structure & Routes
- `projects.html`: Master projects catalog with category filter tabs and 15 project cards.
- `case-studies.html`: Aliased / synchronized mirror to prevent 404s.
- `projects/`: Subdirectory containing the 15 standalone subpages:
  1. `projects/beacon-corporate-realty.html`
  2. `projects/twist-studio.html`
  3. `projects/resilient-solutions.html`
  4. `projects/mirola-ambassador.html`
  5. `projects/mirodata.html`
  6. `projects/cleaner-spaces.html`
  7. `projects/5th-element-media.html`
  8. `projects/iclvirtualservices.html` (replaces operational excellence)
  9. `projects/aliola-global-services.html`
  10. `projects/tom-ojo-sports-academy.html`
  11. `projects/mesuullogic.html`
  12. `projects/expressteck.html`
  13. `projects/lake-greenfield-hotel.html`
  14. `projects/mirola-cleaning-services.html`
  15. `projects/mirola-nigeria.html`

### 4.3 Navigation & Header Updates across 24 Pages
- Desktop Header: `Case Studies` -> `Projects` (pointing to `/projects.html`).
- Mobile Drawer: `Case Studies` -> `Projects` (pointing to `/projects.html`).
- Footer Navigation: `Case Studies` -> `Projects` (pointing to `/projects.html`).
- Homepage Tab: Tab name changed to `Projects`, heading `Explore our Projects`.

### 4.4 Automated Testing & Verification Gate
- `test_projects_suite.py`:
  - Asserts all 15 project subpages exist in `projects/` and return HTTP 200 / valid HTML.
  - Verifies each subpage has correct live URL link, 16:9 widescreen layout, and Vector Studioz navigation.
  - Verifies `projects.html` contains all 15 projects.
  - Verifies `index.html` slider references the projects and contains "Projects" labeling.
  - Verifies all 24 site pages have "Projects" navigation links.
