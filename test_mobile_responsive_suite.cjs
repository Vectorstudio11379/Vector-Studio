// Mobile layout guard rails.
//
// The homepage is built on the CoinGPT Webflow template, whose own CSS and
// IX2 scroll interactions already produce the correct mobile layout (compare
// https://coingpt.tech/ at 375px). Earlier "fixes" overrode that with blanket
// `height: auto !important` rules and stripped the Webflow page attributes,
// which collapsed the hero and froze every scroll animation. These checks keep
// those regressions out, plus the few targeted fixes our custom markup needs.
const fs = require('fs');
const path = require('path');

let passed = 0;
let failed = 0;
function check(condition, message) {
  if (condition) {
    passed++;
    console.log(`PASS  ${message}`);
  } else {
    failed++;
    console.error(`FAIL  ${message}`);
  }
}

const indexHtml = fs.readFileSync('index.html', 'utf8');
const navCss = fs.readFileSync('vector-nav.css', 'utf8');
const tplFooter = fs.readFileSync('template_footer.html', 'utf8');

// Strip comments so prose mentioning a selector doesn't count as a rule.
const cssNoComments = navCss.replace(/\/\*[\s\S]*?\*\//g, '');

// Every selector that appears in a rule body containing `prop: value`.
function selectorsSetting(css, propRegex) {
  const hits = [];
  const ruleRe = /([^{}]+)\{([^{}]*)\}/g;
  let m;
  while ((m = ruleRe.exec(css))) {
    if (propRegex.test(m[2])) hits.push(m[1].trim());
  }
  return hits;
}

console.log('\n-- Webflow template integrity --');
check(
  /<html[^>]*data-wf-page="6488c93b137bd37e5762ce45"[^>]*data-wf-site="64354b8ce4872ad8cd1c7b04"/.test(indexHtml),
  'index.html <html> keeps data-wf-page/data-wf-site (needed for IX2 scroll interactions)'
);

const templateSections = /(^|[\s,])\.(hero|hero-flex-container|unlimited-solutions|solutions-section|solutions-row|ecosystem-section|ecosystem-row|ecosystem-rows|token-section|token-intro|faq-2|latest-items)\b/;
const heightOverrides = selectorsSetting(cssNoComments, /(min-)?height\s*:\s*auto\s*!important/)
  .filter(sel => templateSections.test(sel));
check(
  heightOverrides.length === 0,
  `vector-nav.css does not force height:auto on template sections${heightOverrides.length ? ' (found: ' + heightOverrides.join(' | ') + ')' : ''}`
);

const inlineCss = (indexHtml.match(/<style[^>]*>[\s\S]*?<\/style>/g) || []).join('\n');
const inlineHeightOverrides = selectorsSetting(inlineCss, /(min-)?height\s*:\s*auto\s*!important/)
  .filter(sel => templateSections.test(sel));
check(
  inlineHeightOverrides.length === 0,
  `index.html inline CSS does not force height:auto on template sections${inlineHeightOverrides.length ? ' (found: ' + inlineHeightOverrides.join(' | ') + ')' : ''}`
);

check(
  !/\*\s*,\s*\*::before\s*,\s*\*::after\s*\{[^}]*box-sizing[^}]*!important/.test(cssNoComments),
  'No global !important box-sizing override (it changes template geometry)'
);

console.log('\n-- Horizontal overflow guards --');
check(
  !selectorsSetting(cssNoComments, /overflow(-x)?\s*:\s*(hidden|auto|scroll)/)
    .some(sel => sel.split(',').map(s => s.trim()).includes('body')),
  'body never gets overflow hidden/auto/scroll (it would become a scroll container and break position:sticky, e.g. the services 3D icon)'
);
check(
  /(^|\})\s*body\s*\{[^}]*overflow-x\s*:\s*clip/.test(cssNoComments),
  'body uses overflow-x: clip to block sideways scroll without creating a scroll container'
);
check(
  /\.footer\.site-footer::before\s*,\s*\.footer\.site-footer::after\s*\{[^}]*display\s*:\s*none/.test(cssNoComments),
  'Webflow .footer corner brackets are hidden (they sit 24px outside the full-bleed footer)'
);

console.log('\n-- Inner-page mobile grids --');
check(
  /\.landing-hiw-list-wrapper\.landing-hiw-list-wrapper\s*\{[^}]*grid-template-areas\s*:\s*none/.test(cssNoComments),
  '"How it works" grid resets Webflow grid-template-areas on mobile (otherwise a 2nd column survives)'
);
check(
  /\.landing-faq-wrapper\s*\{[^}]*flex-direction\s*:\s*column/.test(cssNoComments),
  'Service-page FAQ stacks title above questions on mobile'
);

console.log('\n-- Footer --');
check(/\.vs-footer-grid\s*\{/.test(navCss), 'vector-nav.css defines .vs-footer-grid');
check(
  tplFooter.includes('class="vs-footer-grid"') && !/grid-template-columns:\s*1\.6fr/.test(tplFooter),
  'template_footer.html uses .vs-footer-grid instead of inline columns'
);
check(
  indexHtml.includes('class="vs-footer-grid"') && !indexHtml.includes('style="display:grid;grid-template-columns:1.6fr'),
  'index.html footer uses .vs-footer-grid instead of inline columns'
);

console.log('\n-- Ecosystem markup --');
const layer1 = indexHtml.indexOf('Layer1_Mobile');
const layer2 = indexHtml.indexOf('anim-layer-2');
check(
  layer1 > -1 && layer2 > layer1 && indexHtml.slice(layer1, layer2).includes('</div></div></div></div></div>'),
  'Ecosystem Layer 01 closes its containers before Layer 02 starts'
);

console.log('\n-- Page loader & assets --');
const navJs = fs.readFileSync('vector-nav.js', 'utf8');
const robotJs = fs.existsSync('js/robot-scene.js') ? fs.readFileSync('js/robot-scene.js', 'utf8') : '';
check(/<body class="home-page">/.test(indexHtml), 'Homepage <body> does not start as loaded/page-ready (the loader must wait for the robot)');
check(!indexHtml.includes('vs-instant-ready'), 'No script that marks the homepage loaded instantly');
check(!/\.page-loader[^{]*\{[^}]*display\s*:\s*none/.test(cssNoComments), 'vector-nav.css never hides .page-loader outright');
check(!/setTimeout\(\s*\w+\s*,\s*750\s*\)/.test(navJs), 'vector-nav.js has no 750ms forced loader dismissal');
check(/HARD_CAP_MS/.test(navJs) && /MutationObserver/.test(navJs), 'vector-nav.js waits for body.loaded with a stall fallback');
check(indexHtml.includes('src="js/robot-scene.js'), 'Robot scene script is self-hosted (not a third-party GitHub repo)');
check(robotJs.includes('chaingpt-web.s3.us-east-2.amazonaws.com/assets/3d/Cannon_Exterior.hdr'), 'Robot env map points at a host that exists');
check(/\}\), undefined, \(err =>/.test(robotJs), 'Robot model load failure still releases the loader');
check(/querySelector\("\.pupils"\);\s*if \(!t\) return;/.test(robotJs), 'Eye tracking tolerates the missing .pupils element');
check(fs.existsSync('assets/video/eyes_video-transcode.mp4') && indexHtml.includes('assets/video/eyes_video-transcode.mp4'), 'Robot eye video is self-hosted');
check(!/src="https:\/\/(web-assets\.vectorstudioz\.com|cdn\.jsdelivr\.net\/gh\/PazyukAleksey)/.test(indexHtml), 'Homepage loads nothing from dead asset hosts');
check(indexHtml.includes(".rive-animation[data-rive-src]"), 'Rive init only targets elements that have a source file');

console.log('\n-- "Trusted by" client strip --');
const awardsStart = indexHtml.indexOf('<section class="awards-section');
const awardsSection = indexHtml.slice(awardsStart, indexHtml.indexOf('</section>', awardsStart));
const clientLinks = [...awardsSection.matchAll(/class="awards-item[^"]*" href="([^"]+)"/g)].map(m => m[1]);
const clientLogos = [...awardsSection.matchAll(/src="(images\/clients\/[^"]+)"/g)].map(m => m[1]);
check(awardsSection.includes('>TRUSTED BY<'), 'Strip is titled "Trusted by"');
check(clientLinks.length === 15, `Strip lists all 15 clients (found ${clientLinks.length})`);
check(clientLinks.every(h => fs.existsSync(h)), 'Every client links to an existing project page');
check(clientLogos.length > 0 && clientLogos.every(p => fs.existsSync(p)), 'Every client logo file exists');
check(!/awards-nvidia|grant from|AWS Credits|Awwwards Site of the Day/i.test(awardsSection), 'No leftover template award claims');
check(/initClientStripReveal/.test(navJs) && /product-track-descr/.test(navJs) && /html\.vs-reveal-ready \.awards-section/.test(cssNoComments),
  'Mobile strip reveal waits for the pinned "Your Gateway" heading, then shows (no overlap, no late fade)');

console.log('\n-- Stylesheet versions --');
const pages = fs.readdirSync('.').filter(f => f.endsWith('.html') && f !== 'test_index.html')
  .concat(fs.readdirSync('projects').filter(f => f.endsWith('.html')).map(f => path.join('projects', f)));
const versions = new Set();
for (const p of pages) {
  const m = fs.readFileSync(p, 'utf8').match(/vector-nav\.css\?v=([\d.]+)/);
  if (m) versions.add(m[1]);
}
check(versions.size <= 1, `All pages reference the same vector-nav.css version (${[...versions].join(', ') || 'none'})`);

console.log(`\n${passed} passed, ${failed} failed`);
process.exit(failed ? 1 : 0);
