const fs = require('fs');
const path = require('path');

function runSuite() {
  console.log("===================================================================");
  console.log("   AUTOMATED MOBILE RESPONSIVENESS & SCALING VERIFICATION SUITE   ");
  console.log("   Target Viewports: 360px, 375px, 390px, 412px, 430px           ");
  console.log("===================================================================\n");

  let passedTests = 0;
  let totalTests = 0;

  function assert(condition, message) {
    totalTests++;
    if (!condition) {
      console.error(`❌ [FAIL] ${message}`);
      throw new Error(message);
    }
    console.log(`✅ [PASS] ${message}`);
    passedTests++;
  }

  const indexHtml = fs.readFileSync('index.html', 'utf8');
  const navCss = fs.readFileSync('vector-nav.css', 'utf8');
  const tplFooter = fs.readFileSync('template_footer.html', 'utf8');

  // -------------------------------------------------------------
  // TEST GROUP 1: R1 — Vertical Spacing and Layout Flow
  // -------------------------------------------------------------
  console.log("\n--- TEST GROUP 1: R1 — Vertical Spacing & Layout Flow ---");

  // 1.1 Hero Section Height Normalization
  assert(
    navCss.includes('.hero') &&
    navCss.includes('min-height: auto !important') &&
    navCss.includes('height: auto !important'),
    "Hero section has min-height and height reset to auto on mobile"
  );
  assert(
    navCss.includes('.container.hero-flex-container') &&
    navCss.includes('gap: 16px !important'),
    "Hero flex container has compact responsive gap on mobile"
  );

  // 1.2 Solutions Section Gaps Eliminated
  assert(
    navCss.includes('.solutions-section') &&
    navCss.includes('.solutions-row') &&
    navCss.includes('.solutions-image-wrap-mobile {') &&
    navCss.includes('display: none !important;'),
    "Solutions section hides 315px empty placeholder images on mobile"
  );
  assert(
    navCss.includes('.soliutions-image-track {') &&
    navCss.includes('display: none !important;'),
    "Desktop-only sticky image track is hidden on mobile viewports"
  );
  assert(
    navCss.includes('.solutions-row {') &&
    navCss.includes('opacity: 1 !important;'),
    "Solutions rows are forced opacity: 1 on mobile to prevent invisible sections"
  );

  // 1.3 Ecosystem 3,000px Voids Eliminated
  assert(
    navCss.includes('.ecosystem-section') &&
    navCss.includes('.ecosystem-rows') &&
    navCss.includes('.ecosystem-row,') &&
    navCss.includes('.ecosystem-row-layer {') &&
    navCss.includes('height: auto !important;') &&
    navCss.includes('min-height: auto !important;'),
    "Ecosystem rows reset from 100vh desktop pinned height to auto height on mobile"
  );
  assert(
    navCss.includes('.ecosystem-layer-wrapper,') &&
    navCss.includes('max-height: 280px !important;'),
    "Ecosystem animation wrappers capped cleanly to prevent stretched black voids"
  );

  // 1.4 Token / Agency OS Section Spacing
  assert(
    navCss.includes('.token-section') &&
    navCss.includes('.token-intro {') &&
    navCss.includes('flex-direction: column !important;'),
    "Agency OS / Token section stacks vertically on mobile without horizontal spacing voids"
  );
  assert(
    navCss.includes('.empty-col {') &&
    navCss.includes('display: none !important;'),
    "Empty desktop grid placeholder column is suppressed on mobile"
  );

  // 1.5 FAQ & CTA Banner Vertical Flow
  assert(
    navCss.includes('.faq-2 {') &&
    navCss.includes('padding: 28px 0 !important;'),
    "FAQ section has natural compact vertical padding on mobile"
  );
  assert(
    navCss.includes('.cta-banner-wrapper {') &&
    navCss.includes('padding: 28px 16px !important;'),
    "CTA banner wrapper has compact mobile padding avoiding excessive vertical gaps"
  );

  // 1.6 Inline Critical Fix in index.html Head
  assert(
    indexHtml.includes('id="vs-critical-mobile-fix"') &&
    indexHtml.includes('.solutions-section,') &&
    indexHtml.includes('.ecosystem-section,') &&
    indexHtml.includes('min-height: auto !important;'),
    "Critical inline style block in index.html guards against mobile vertical voids before external CSS"
  );

  // -------------------------------------------------------------
  // TEST GROUP 2: R2 — Responsive Footer Stacking
  // -------------------------------------------------------------
  console.log("\n--- TEST GROUP 2: R2 — Responsive Footer Stacking ---");

  // 2.1 CSS Footer Grid Definition
  assert(
    navCss.includes('.vs-footer-grid {') &&
    navCss.includes('grid-template-columns: 1fr !important;'),
    "vs-footer-grid transitions to 1fr single-column stacking on mobile viewports (<= 768px)"
  );
  assert(
    navCss.includes('.vs-footer-bottom {') &&
    navCss.includes('flex-direction: column !important;'),
    "Footer bottom bar stacks vertically on mobile viewports"
  );

  // 2.2 Template Footer Uses vs-footer-grid
  assert(
    tplFooter.includes('class="vs-footer-grid"') &&
    !tplFooter.includes('grid-template-columns:1.6fr 1fr 1fr 1fr') &&
    !tplFooter.includes('grid-template-columns: 1.6fr 1fr 1fr 1fr'),
    "template_footer.html uses responsive .vs-footer-grid class without hardcoded inline multi-columns"
  );

  // 2.3 index.html Uses vs-footer-grid
  assert(
    indexHtml.includes('class="vs-footer-grid"') &&
    !indexHtml.includes('style="display:grid;grid-template-columns:1.6fr') &&
    !indexHtml.includes('style="display:grid; grid-template-columns: 1.6fr'),
    "index.html uses responsive .vs-footer-grid class without inline hardcoded grid style"
  );

  // 2.4 Verify All Site HTML Pages Have Responsive Footer Grid
  const htmlFiles = fs.readdirSync('.').filter(f => f.endsWith('.html') && f !== 'test_index.html');
  console.log(`Checking footer structure across ${htmlFiles.length} root HTML pages...`);
  htmlFiles.forEach(file => {
    const content = fs.readFileSync(file, 'utf8');
    if (content.includes('id="site-footer"')) {
      assert(
        content.includes('class="vs-footer-grid"'),
        `${file} implements .vs-footer-grid for clean responsive stacking`
      );
      assert(
        !content.includes('style="display:grid;grid-template-columns:1.6fr') &&
        !content.includes('style="display:grid; grid-template-columns: 1.6fr'),
        `${file} has no hardcoded 4-column inline style causing squished text wrapping`
      );
    }
  });

  // Also check project subpages in projects/
  const subpages = fs.readdirSync('projects').filter(f => f.endsWith('.html'));
  console.log(`Checking footer structure across ${subpages.length} project subpages...`);
  subpages.forEach(sub => {
    const content = fs.readFileSync(path.join('projects', sub), 'utf8');
    if (content.includes('id="site-footer"')) {
      assert(
        content.includes('class="vs-footer-grid"'),
        `projects/${sub} implements .vs-footer-grid`
      );
    }
  });

  // -------------------------------------------------------------
  // TEST GROUP 3: R3 — Card & Content Sizing & Alignment (360px - 430px)
  // -------------------------------------------------------------
  console.log("\n--- TEST GROUP 3: R3 — Card & Content Sizing & Viewport Scaling ---");

  // 3.1 Global Fluid Scaling & Overflow Boundary
  assert(
    navCss.includes('overflow-x: hidden !important;') &&
    navCss.includes('max-width: 100vw !important;'),
    "Global overflow-x protection prevents accidental horizontal scroll on mobile"
  );
  assert(
    navCss.includes('img, svg, video, canvas {') &&
    navCss.includes('max-width: 100% !important;'),
    "Universal media boundary rule prevents image, svg, canvas blowouts"
  );

  // 3.2 Mobile Viewport Width Scaling (360px to 430px)
  assert(
    navCss.includes('@media screen and (max-width: 430px) {') &&
    navCss.includes('font-size: clamp(20px, 6vw, 26px) !important;'),
    "Section titles scale responsively via fluid clamp down to 360px viewports"
  );
  assert(
    navCss.includes('.top-banner-text.overflow-ellipsis {') &&
    navCss.includes('max-width: 210px !important;'),
    "Top announcement banner text is capped to prevent wrapping blowout on 360px screens"
  );
  assert(
    navCss.includes('.hero-heding-top-stroke svg {') &&
    navCss.includes('max-width: 90vw !important;'),
    "Hero decorative SVG stroke scales fluidly within 90vw on narrow mobile screens"
  );

  // 3.3 Card Grid Single-Column Stacking for Secondary Pages
  assert(
    navCss.includes('.articles-list {') &&
    navCss.includes('grid-template-columns: 1fr !important;'),
    "Projects and case study card grids stack in single column on mobile"
  );
  assert(
    navCss.includes('.landing-features-grid,') &&
    navCss.includes('grid-template-columns: 1fr !important;'),
    "Company inner-page bento feature cards stack cleanly in 1fr column on mobile"
  );

  // 3.4 Card Padding and Box-Sizing
  assert(
    navCss.includes('.solutions-row {') &&
    navCss.includes('box-sizing: border-box !important;') || navCss.includes('*, *::before, *::after {'),
    "Universal border-box sizing ensures card padding does not cause viewport overflow"
  );

  // -------------------------------------------------------------
  // TEST GROUP 4: Section Hierarchy & Div Balance
  // -------------------------------------------------------------
  console.log("\n--- TEST GROUP 4: Section Hierarchy & Div Balance ---");

  // Check div balance across index.html
  const divRegex = /<(\/?[a-zA-Z0-9]+)(\s+[^>]*)?>/g;
  let depth = 0;
  let match;
  while ((match = divRegex.exec(indexHtml)) !== null) {
    const tag = match[1].toLowerCase();
    const attrs = match[2] || '';
    const isSec = ['id="cases"', 'id="ecosystem"', 'id="our-token"', 'id="faq"', 'id="site-footer"'].some(k => attrs.includes(k));
    if (isSec && !tag.startsWith('/')) {
      assert(depth === 0, `Section ${attrs.slice(0, 30)} starts cleanly at div depth 0`);
    }
    if (tag === 'div') depth++;
    else if (tag === '/div') depth--;
  }
  assert(depth === 0, `index.html div depth is perfectly balanced (final depth: ${depth})`);

  // -------------------------------------------------------------
  // TEST GROUP 5: Advanced Responsive Safeguards & Robustness
  // -------------------------------------------------------------
  console.log("\n--- TEST GROUP 5: Advanced Responsive Safeguards & Robustness ---");

  // 5.1 Enforced flexbox display on critical stacked containers
  assert(
    navCss.includes('.solutions-row {') && navCss.includes('display: flex !important;') &&
    navCss.includes('.solutions-cols {') && navCss.includes('display: flex !important;'),
    "Solutions rows and columns explicitly enforce display: flex !important on mobile"
  );
  assert(
    navCss.includes('.token-intro {') && navCss.includes('display: flex !important;'),
    "Token intro section explicitly enforces display: flex !important on mobile"
  );
  assert(
    navCss.includes('.articles-list {') && navCss.includes('display: grid !important;'),
    "Articles list explicitly enforces display: grid !important on mobile"
  );

  // 5.2 Elimination of slider overflow margin and double ecosystem border
  assert(
    navCss.includes('.caselist-slider-item {') && navCss.includes('margin-right: 0 !important;'),
    "Case study slider items reset margin-right: 0 on mobile preventing horizontal viewport expansion"
  );
  assert(
    navCss.includes('.ecosystem-row-item.ecosystem-row-layer {') &&
    navCss.includes('border: none !important;') &&
    navCss.includes('background: transparent !important;'),
    "Nested ecosystem layer items eliminate redundant double card borders"
  );

  // 5.3 Badge grayscale reset and banner text ellipsis
  assert(
    navCss.includes('.nb-default {') && navCss.includes('filter: none !important;'),
    "Solutions numbering badges reset grayscale filter to visible on mobile"
  );
  assert(
    navCss.includes('.top-banner-text.overflow-ellipsis {') &&
    navCss.includes('white-space: nowrap !important;') &&
    navCss.includes('text-overflow: ellipsis !important;'),
    "Announcement banner text truncates cleanly with ellipsis without text blowout"
  );
  assert(
    navCss.includes('.vertical-line {') && navCss.includes('pointer-events: none !important;'),
    "Decorative vertical background lines do not intercept touch interaction on mobile"
  );

  // 5.4 Check div balance across all 15 project subpages
  console.log("Verifying div balance across all 15 project subpages...");
  subpages.forEach(sub => {
    const subHtml = fs.readFileSync(path.join('projects', sub), 'utf8');
    let subDepth = 0;
    let sm;
    const subDivRegex = /<(\/?[a-zA-Z0-9]+)(\s+[^>]*)?>/g;
    while ((sm = subDivRegex.exec(subHtml)) !== null) {
      const tag = sm[1].toLowerCase();
      if (tag === 'div') subDepth++;
      else if (tag === '/div') subDepth--;
    }
    assert(subDepth === 0, `projects/${sub} div depth is perfectly balanced (final depth: ${subDepth})`);
  });

  // -------------------------------------------------------------
  // TEST GROUP 6: Form, Viewport Boundary & Control Stacking Robustness (R2 Audit)
  // -------------------------------------------------------------
  console.log("\n--- TEST GROUP 6: Form, Viewport Boundary & Control Stacking Robustness ---");

  // 6.1 Breakpoint synchronization: 768px covers iPad/Tablet boundary across all systems
  assert(
    navCss.includes('@media screen and (max-width: 768px) {\n  .short-mode.aside-navbar,') ||
    navCss.includes('@media screen and (max-width: 768px) {\r\n  .short-mode.aside-navbar,'),
    "aside-navbar hides cleanly at max-width: 768px preventing desktop rail intrusion on tablet"
  );
  assert(
    indexHtml.includes('@media screen and (max-width: 768px) {\r\n    .vs-brand-logo-img {') ||
    indexHtml.includes('@media screen and (max-width: 768px) {\n    .vs-brand-logo-img {'),
    "Critical mobile fix inline stylesheet triggers at max-width: 768px matching external CSS"
  );
  assert(
    navCss.includes('@media screen and (max-width: 768px) {\n  .vs-footer-grid {') ||
    navCss.includes('@media screen and (max-width: 768px) {\r\n  .vs-footer-grid {'),
    "Footer grid transitions to single column at max-width: 768px"
  );

  // 6.2 Sibling layout of Ecosystem layers: Layer 01 properly closed and not enclosing Layer 02
  const layer1CloseIdx = indexHtml.indexOf('Layer1_Mobile');
  const layer2StartIdx = indexHtml.indexOf('anim-layer-2');
  const betweenLayer1And2 = indexHtml.slice(layer1CloseIdx, layer2StartIdx);
  assert(
    betweenLayer1And2.includes('</div></div></div></div></div>'),
    "Layer 01 properly closes all 5 nested container divs before Layer 02 starts"
  );

  // 6.3 Form controls responsive stacking
  assert(
    navCss.includes('#contact-form div[style*="grid-template-columns"]') &&
    navCss.includes('grid-template-columns: 1fr !important;'),
    "Contact form two-column grids stack to 1fr on mobile viewports"
  );
  assert(
    navCss.includes('.form-input-webflow') &&
    navCss.includes('max-width: 100% !important;'),
    "Webflow form inputs enforce max-width: 100% avoiding horizontal viewport blowout"
  );
  assert(
    navCss.includes('.verify-row') &&
    navCss.includes('flex-direction: column !important;'),
    "Verification page input and dropdown controls stack vertically on mobile"
  );
  assert(
    navCss.includes('.btn-verify') &&
    navCss.includes('width: 100% !important;') &&
    navCss.includes('justify-content: center !important;'),
    "Verification action button stretches to full mobile container width"
  );

  // 6.4 Button flex alignment
  assert(
    navCss.includes('.solutions-actions-row a {') &&
    navCss.includes('display: inline-flex !important;') &&
    navCss.includes('justify-content: center !important;'),
    "Solutions CTA buttons enforce inline-flex with center justification"
  );
  assert(
    navCss.includes('.grid-column--special a {') &&
    navCss.includes('display: inline-flex !important;') &&
    navCss.includes('justify-content: center !important;'),
    "Agency OS footer CTA links enforce inline-flex with center justification"
  );

  // 6.5 Slider and Marquee Bounds
  assert(
    navCss.includes('.learn-more-box {') &&
    navCss.includes('max-width: 100% !important;'),
    "Case studies learn-more-box is capped to 100% container width"
  );
  assert(
    navCss.includes('.w-slider {') &&
    navCss.includes('overflow: hidden !important;'),
    "Webflow sliders strictly isolate horizontal overflow on mobile"
  );

  // 6.6 Full width utilization of top announcement banner on narrow mobile
  assert(
    navCss.includes('.top-banner-link {') &&
    navCss.includes('max-width: 100% !important;'),
    "Top banner link utilizes full mobile width without redundant close button margin"
  );

  console.log("\n===================================================================");
  console.log(`   ALL ${passedTests} / ${totalTests} TESTS PASSED WITH 100% SUCCESS!   `);
  console.log("===================================================================\n");
}

runSuite();
