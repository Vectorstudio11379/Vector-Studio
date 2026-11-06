const fs = require('fs');

function runTests() {
  console.log("=== RUNNING COMPLETE VERIFICATION SUITE ===");

  const indexHtml = fs.readFileSync('index.html', 'utf8');

  // 1. No pricing section
  if (indexHtml.includes('id="our-pricing"') || indexHtml.includes('Our\n Pricing') || indexHtml.includes('Our Pricing')) {
    throw new Error("Pricing section still in index.html");
  }

  // 2. No Audited by section
  if (indexHtml.includes('AUDITED BY') || indexHtml.includes('token-sub-intro') || indexHtml.includes('certik.svg') || indexHtml.includes('hacken.svg')) {
    throw new Error("Audited by section still in index.html");
  }

  // 3. Features of sprint aligned
  const forbiddenSprint = ["DAO & Voting", "retainer & Farming", "access to idos", "Liquidity Providing"];
  for (const f of forbiddenSprint) {
    if (indexHtml.includes(f)) throw new Error(`Forbidden sprint feature found: ${f}`);
  }
  if (!indexHtml.includes("Bespoke UI/UX") || !indexHtml.includes("Full-Stack Web")) {
    throw new Error("Missing Vector Studioz sprint features");
  }

  // 4. Old Explore our Projects removed (blog/vlog/spaces tab triggers)
  if (indexHtml.includes('class="text-block-140">blog') || indexHtml.includes('class="text-block-140">vlog') || indexHtml.includes('class="text-block-140">spaces')) {
    throw new Error("Old explore our projects with blog still present");
  }
  if (!indexHtml.includes('id="cases"') || !indexHtml.includes('Messulogic')) {
    throw new Error("Missing #cases or Messulogic");
  }

  // 5. Team section completely removed
  if (indexHtml.includes('id="team"') || indexHtml.includes('Faces behind Vector Studioz')) {
    throw new Error("Team section still in index.html");
  }
  const aboutHtml = fs.readFileSync('about.html', 'utf8');
  if (aboutHtml.includes('Faces Behind Vector Studioz') || aboutHtml.includes('Elijah Ezekiel')) {
    throw new Error("Team still in about.html");
  }

  // 6. Partners & projects and AS SEEN ON removed
  if (indexHtml.includes('partners & projects (184)') || indexHtml.includes('partners & projects') || indexHtml.includes('AS SEEN ON:')) {
    throw new Error("Partners or AS SEEN ON still in index.html");
  }

  // 7. Community section cleaned
  const forbiddenCommunity = ["195K+", "45K+", "t.me/chaingpt", "discord.gg/chaingpt"];
  for (const f of forbiddenCommunity) {
    if (indexHtml.includes(f)) throw new Error(`Forbidden community content found: ${f}`);
  }

  // 8. FAQ cleaned
  const forbiddenFaq = ['CGPT Credits', 'Diamond Tier', '0x9840652DC04fb9db2C43853633f0F62BE6f00f98', 'Binance smart chain', '200,000 voting power'];
  for (const f of forbiddenFaq) {
    if (indexHtml.includes(f)) throw new Error(`Forbidden FAQ content found: ${f}`);
  }

  // 9. Div nesting depth is 0 at section boundaries
  const divRegex = /<(\/?[a-zA-Z0-9]+)(\s+[^>]*)?>/g;
  let depth = 0;
  let match;
  while ((match = divRegex.exec(indexHtml)) !== null) {
    const tag = match[1].toLowerCase();
    const attrs = match[2] || '';
    const isSec = ['id="cases"', 'id="ecosystem"', 'id="our-token"', 'id="faq"', 'id="site-footer"'].some(k => attrs.includes(k));
    if (isSec && !tag.startsWith('/')) {
      if (depth !== 0) throw new Error(`Section ${attrs.slice(0, 30)} at non-zero depth ${depth}`);
    }
    if (tag === 'div') depth++;
    else if (tag === '/div') depth--;
  }
  if (depth !== 0) throw new Error(`Final div depth in index.html is ${depth}`);

  // 10. Pricing links removed from template header and footer
  const tplHeader = fs.readFileSync('template_header.html', 'utf8');
  if (tplHeader.includes('href="pricing.html"')) throw new Error("pricing.html in template_header.html");
  const tplFooter = fs.readFileSync('template_footer.html', 'utf8');
  if (tplFooter.includes('href="pricing.html"')) throw new Error("pricing.html in template_footer.html");

  // 11. Header on project page and subpages
  const prjHtml = fs.readFileSync('projects.html', 'utf8');
  if (!prjHtml.includes('vector-nav.js')) throw new Error("vector-nav.js missing from projects.html");
  if (prjHtml.includes('href="/vector-nav.css"')) throw new Error("Leading slash in vector-nav.css in projects.html");

  const subpages = fs.readdirSync('projects').filter(f => f.endsWith('.html'));
  if (subpages.length !== 15) throw new Error(`Expected 15 subpages, found ${subpages.length}`);
  for (const s of subpages) {
    const subHtml = fs.readFileSync('projects/' + s, 'utf8');
    if (subHtml.includes('vs-nav-header')) throw new Error(`Legacy vs-nav-header in projects/${s}`);
    if (!subHtml.includes('vs-navbar')) throw new Error(`vs-navbar missing in projects/${s}`);
  }

  // 12. Discount top banner
  if (!indexHtml.includes('Special Discount') || !indexHtml.includes('30% Off')) {
    throw new Error("Discount banner missing from index.html");
  }

  // 13. Official brand logo images
  if (!indexHtml.includes('images/branding/vector-studioz-logo.png')) {
    throw new Error("Branding logo missing from index.html");
  }
  if (!tplHeader.includes('images/branding/vector-studioz-logo.png')) {
    throw new Error("Branding logo missing from template_header.html");
  }
  if (!tplFooter.includes('images/branding/vector-studioz-logo.png')) {
    throw new Error("Branding logo missing from template_footer.html");
  }

  // 14. SEO & OG image
  if (!indexHtml.includes('https://vectorstudioz.uk/images/og-hero.jpg')) {
    throw new Error("OG hero image missing from index.html head");
  }
  if (!indexHtml.includes('https://vectorstudioz.uk/')) {
    throw new Error("Canonical domain missing from index.html");
  }
  if (!indexHtml.includes('href="favicon.png"')) {
    throw new Error("Favicon missing from index.html");
  }

  console.log("ALL 14 VERIFICATION CHECKS PASSED PERFECTLY!");
}

runTests();
