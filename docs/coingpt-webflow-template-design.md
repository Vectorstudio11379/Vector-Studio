# Design Document: CoinGPT Native Webflow Inner-Page Templates & Header Modernization

## 1. Overview
Transform the non-homepage custom pages (`about.html`, `pricing.html`, `careers.html`, `contact-us.html`) into authentic, pixel-accurate Webflow inner-page templates matching `ai-trading-assistant.html` and `web3-chatbot.html`. Simultaneously restore the signature default Webflow header CTA button (`.btn-primary` with multi-color gradient border lines and cut corners) and redesign the CoinGPT logo to match the site's neon cyber color palette.

---

## 2. Header Components Specification

### 2.1 Default Webflow Header CTA Button (`.btn-primary`)
- **Structure**:
  ```html
  <div class="header-side-part">
    <a class="btn-primary ml-auto w-inline-block" href="pricing.html" scramble-link="">
      <div class="btn-primary-lines btn-primary-lines-1">
        <div class="btn-primary-lines btn-primary-lines-2">
          <div class="btn-primary-text" scramble-text="">Launch App</div>
        </div>
      </div>
    </a>
  </div>
  ```
- **Visual Mechanics**:
  - 45° chamfered cut corners via pseudo-elements (`.btn-primary:before`, `.btn-primary:after`).
  - Animated multi-gradient border strokes (`.btn-primary-lines-1`, `.btn-primary-lines-2` with `#fb7454`, `#bcda68`, `#6e52e5`, `#74e79a`).
  - Dual dot indicators (`.btn-primary-text:before`, `.btn-primary-text:after`) in `#efefe5`.
  - Integrated into desktop navbar actions and mobile drawer action button.

### 2.2 Redesigned CoinGPT Logo (Website Color Palette)
- **Emblem**:
  - High-precision geometric Cyber Neural Hexagon / Quantum Node SVG icon.
  - Linear gradients using `#00ffa3` (electric emerald), `#28efce` (neon cyan), and `#6a59e5` (deep violet).
  - Glowing outer border with soft drop shadow: `drop-shadow(0 0 10px rgba(0, 255, 163, 0.4))`.
- **Wordmark**:
  - Bold Inter typography: `CoinGPT`.
  - Accent suffix: `<span style="color:#00ffa3;">.tech</span>` or electric emerald badge.
- **Header & Footer Consistency**:
  - Replaces all legacy logos in `template_header.html` and `template_footer.html` and propagates across all 24 site pages.

---

## 3. Webflow Inner-Page Template Architecture

Every non-home page will adhere to the layout established in `ai-trading-assistant.html`:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Header (CoinGPT Logo, Dropdowns, Default .btn-primary)   │
├─────────────────────────────────────────────────────────────┤
│ 2. Hero Section:                                            │
│    Left: .section-title-bordered--gradient badge            │
│          H1 Hero Headline + Gradient Highlights             │
│          Hero Description + Feature Bullet list             │
│          .btn-primary ("Launch" / "Get Started")            │
│    Right: Cyber Graphic / Interactive Product Visual Card   │
├─────────────────────────────────────────────────────────────┤
│ 3. Cut-Corner Divider [block-corners-top/bottom]           │
├─────────────────────────────────────────────────────────────┤
│ 4. Core Features / Bento Grid:                              │
│    Grid cards with Webflow frosted borders & hover glow     │
├─────────────────────────────────────────────────────────────┤
│ 5. Detailed Breakdown / Comparison or Interactive Tabs      │
├─────────────────────────────────────────────────────────────┤
│ 6. Interactive FAQ Section (.faq-2 .miscellaneous-2):       │
│    Expandable question cards with animated plus/cross icon  │
├─────────────────────────────────────────────────────────────┤
│ 7. Bottom CTA Banner (Glowing banner with .btn-primary)     │
├─────────────────────────────────────────────────────────────┤
│ 8. Standardized Site Footer                                 │
└─────────────────────────────────────────────────────────────┘
```

### 3.1 Page-Specific Implementations

1. **`pricing.html`**:
   - **Hero**: "Transparent On-Chain Pricing & API Tiers" + live billing toggle (Monthly / Annual).
   - **Visual Card**: Tier summary card with real-time token/fiat cost indicator.
   - **Tier Bento**: 3 Webflow styled cards (Free Tier, Pro Trader, Enterprise API & Institutional).
   - **Comparison Matrix**: Detailed feature comparison table with checkmarks.
   - **FAQ**: 5 expandable pricing and subscription questions.

2. **`about.html`**:
   - **Hero**: "Engineering the Intelligence Layer for Web3" + mission statement.
   - **Visual Card**: Holographic neural network node graphic with live stats metrics (2M+ queries, 450K+ users).
   - **Pillars Bento**: 4 cards highlighting Decoupled Architecture, On-chain Verifiability, Low Latency, and Security.
   - **Leadership & Backers**: Webflow avatar cards with clip-path chamfered portraits.
   - **FAQ**: 4 company and infrastructure questions.

3. **`careers.html`**:
   - **Hero**: "Build the Future of Decentralized AI" + culture highlights.
   - **Visual Card**: Interactive Remote Perks & Benefits badge cluster.
   - **Roles Bento**: Open positions categorized by Engineering, AI Research, Product & Design, and Growth with "Apply" triggers.
   - **Hiring Process**: 4-step interview pipeline diagram.
   - **FAQ**: 4 career, relocation, and equity questions.

4. **`contact-us.html`**:
   - **Hero**: "Connect With CoinGPT Engineering & Partnerships".
   - **Left Column**: Office hubs (Global Remote, Singapore, Zurich), direct email routes (support@, press@, partnerships@), Telegram & Discord handles.
   - **Right Column (Form Card)**: Webflow styled `.form-field` inputs with floating labels (`.label-moved`), category dropdown, message textarea, and submission button.
   - **FAQ**: 4 inquiry and response time questions.

---

## 4. Navigation & Link Routing
- Keep `vector-nav.css` and `vector-nav.js` active for smooth mobile drawers and link sanitization.
- Ensure all relative navigation links point cleanly to their `.html` targets.
- Retain Webflow native script bindings (`Lenis` smooth scroll, hover animations, and SVG transitions).

---

## 5. Verification Strategy
1. **Visual & Interactive Validation**: Run browser checks on desktop and mobile viewports.
2. **Component Integrity**: Test `.btn-primary` hover line animations, FAQ accordion expands/collapses, and mobile menu drawer open/close.
3. **Link Health**: Verify 100% of header and footer links resolve with HTTP 200 without broken routes.
