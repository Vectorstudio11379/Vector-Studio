# Generator for Agency Native Webflow pricing.html

with open('template_header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

with open('template_footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

PAGE_HTML = f"""<!DOCTYPE html>
<html data-wf-domain="www.vectorstudioz.com" data-wf-page="6488c93b137bd37e5762ce45" data-wf-site="64354b8ce4872ad8cd1c7b04" lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Pricing &amp; Retainer Models — Vector Studioz | Elite Digital Agency</title>
  <meta name="description" content="Transparent, outcome-driven pricing for bespoke web design, full-stack product engineering, dedicated agile squads, and enterprise AI automation systems."/>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Roboto+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/css/chain-gpt.shared.a3558708c.min.css"/>
  <link rel="stylesheet" href="vector-nav.css"/>
  <style>
    :root {{
      --bg-dark: #0b0c10;
      --divider: rgba(255, 255, 255, 0.08);
      --card-bg: rgba(18, 20, 29, 0.7);
      --primary: #00ffa3;
      --cyan: #00e1ff;
      --pink: #ff007a;
      --purple: #7928ca;
    }}
    body {{
      background-color: #0b0c10;
      color: #efefe5;
      font-family: 'Inter', -apple-system, sans-serif;
      margin: 0;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }}
    .pricing-hero-container {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 90px 2rem 50px;
      position: relative;
    }}
    .hero-glow-bg {{
      position: absolute;
      top: -60px;
      left: 50%;
      transform: translateX(-50%);
      width: 800px;
      height: 450px;
      background: radial-gradient(circle, rgba(255, 0, 122, 0.12) 0%, rgba(0, 225, 255, 0.08) 50%, transparent 70%);
      filter: blur(90px);
      pointer-events: none;
      z-index: 0;
    }}
    .hero-grid-2col {{
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 50px;
      align-items: center;
      position: relative;
      z-index: 1;
    }}
    @media (max-width: 991px) {{
      .hero-grid-2col {{ grid-template-columns: 1fr; gap: 40px; }}
    }}
    .hero-title-h1 {{
      font-size: clamp(34px, 4.8vw, 56px);
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.15;
      color: #ffffff;
      margin: 16px 0 20px;
    }}
    .hero-title-h1 span.gradient-text {{
      background: linear-gradient(135deg, #ff007a 0%, #ff8a00 25%, #ffe600 50%, #00ffa3 75%, #00e1ff 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero-desc-p {{
      font-size: clamp(16px, 1.8vw, 18px);
      color: #9ca3af;
      line-height: 1.6;
      margin-bottom: 28px;
    }}
    .hero-bullets {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-bottom: 34px;
    }}
    .hero-bullet-item {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 15px;
      color: #d1d5db;
    }}
    .hero-bullet-icon {{
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: rgba(0, 225, 255, 0.1);
      border: 1px solid rgba(0, 225, 255, 0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #00e1ff;
      font-size: 11px;
      flex-shrink: 0;
    }}

    /* Webflow Native Cut Corners */
    [block-corners-top] {{
      position: absolute;
      top: 0; left: 0; right: 0; height: 1px;
    }}
    [block-corners-top]::before, [block-corners-top]::after {{
      content: '';
      position: absolute;
      width: 6px;
      height: 6px;
      border-color: #00e1ff;
      border-style: solid;
      top: -1px;
    }}
    [block-corners-top]::before {{ left: -1px; border-width: 1px 0 0 1px; }}
    [block-corners-top]::after {{ right: -1px; border-width: 1px 1px 0 0; }}

    [block-corners-bottom] {{
      position: absolute;
      bottom: 0; left: 0; right: 0; height: 1px;
    }}
    [block-corners-bottom]::before, [block-corners-bottom]::after {{
      content: '';
      position: absolute;
      width: 6px;
      height: 6px;
      border-color: #00e1ff;
      border-style: solid;
      bottom: -1px;
    }}
    [block-corners-bottom]::before {{ left: -1px; border-width: 0 0 1px 1px; }}
    [block-corners-bottom]::after {{ right: -1px; border-width: 0 1px 1px 0; }}

    /* Section Title Bordered */
    .section-title-bordered {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border: 1px solid rgba(0, 225, 255, 0.25);
      border-radius: 4px;
      background: rgba(0, 225, 255, 0.04);
      font-family: 'Roboto Mono', monospace;
      font-size: 12px;
      letter-spacing: 0.1em;
      color: #00e1ff;
      text-transform: uppercase;
      margin-bottom: 16px;
    }}
    .section-title-bordered::before {{
      content: '';
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #00e1ff;
      box-shadow: 0 0 8px #00e1ff;
    }}

    /* Pricing Section */
    .content-section {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 60px 2rem;
    }}
    .toggle-container {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      margin: 20px 0 40px;
    }}
    .toggle-btn {{
      background: rgba(18, 20, 29, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 14px;
      color: #9ca3af;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .toggle-btn.active {{
      background: rgba(0, 225, 255, 0.15);
      border-color: #00e1ff;
      color: #ffffff;
      font-weight: 600;
    }}
    .discount-badge {{
      background: linear-gradient(135deg, #ff007a, #7928ca);
      color: #ffffff;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 10px;
      margin-left: 6px;
    }}

    /* Pricing Grid */
    .pricing-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }}
    @media (max-width: 1024px) {{
      .pricing-grid {{ grid-template-columns: 1fr; }}
    }}
    .pricing-card {{
      background: rgba(18, 20, 29, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 38px 32px;
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border-radius: 4px;
      transition: all 0.3s ease;
    }}
    .pricing-card:hover {{
      border-color: rgba(0, 225, 255, 0.4);
      transform: translateY(-4px);
      box-shadow: 0 15px 35px -10px rgba(0, 225, 255, 0.15);
    }}
    .pricing-card.featured {{
      border-color: rgba(255, 0, 122, 0.5);
      background: rgba(24, 26, 38, 0.85);
      box-shadow: 0 20px 40px -10px rgba(255, 0, 122, 0.2);
    }}
    .tier-badge {{
      font-family: 'Roboto Mono', monospace;
      font-size: 12px;
      color: #00e1ff;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 8px;
    }}
    .tier-title {{
      font-size: 24px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 12px;
    }}
    .tier-desc {{
      font-size: 14.5px;
      color: #9ca3af;
      line-height: 1.5;
      margin-bottom: 24px;
      min-height: 44px;
    }}
    .tier-price {{
      font-size: 42px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 4px;
      font-family: 'Roboto Mono', monospace;
    }}
    .tier-period {{
      font-size: 13.5px;
      color: #9ca3af;
      margin-bottom: 28px;
    }}
    .tier-features {{
      list-style: none;
      padding: 0;
      margin: 0 0 32px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}
    .tier-feature-item {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      font-size: 14px;
      color: #d1d5db;
      line-height: 1.4;
    }}
    .tier-feature-item svg {{
      color: #00ffa3;
      flex-shrink: 0;
      margin-top: 2px;
    }}

    /* FAQ 2 Webflow Styling */
    .faq-list {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-top: 36px;
    }}
    .faq-2 {{
      background: rgba(18, 20, 29, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 4px;
      overflow: hidden;
      transition: all 0.3s ease;
    }}
    .faq-2.open {{
      border-color: rgba(0, 225, 255, 0.35);
      background: rgba(22, 25, 38, 0.8);
    }}
    .faq-2-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 22px 26px;
      cursor: pointer;
      user-select: none;
    }}
    .faq-2-title {{
      font-size: 17px;
      font-weight: 600;
      color: #ffffff;
      margin: 0;
    }}
    .faq-2-plus {{
      width: 24px;
      height: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      color: #00e1ff;
      transition: transform 0.3s ease;
    }}
    .faq-2.open .faq-2-plus {{
      transform: rotate(45deg);
    }}
    .faq-2-bottom {{
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.35s ease, padding 0.35s ease;
      padding: 0 26px;
      color: #9ca3af;
      font-size: 15px;
      line-height: 1.6;
    }}
    .faq-2.open .faq-2-bottom {{
      max-height: 300px;
      padding: 0 26px 22px;
    }}

    /* Bottom CTA banner */
    .cta-banner-wrapper {{
      max-width: 1400px;
      margin: 80px auto 100px;
      padding: 0 2rem;
    }}
    .cta-banner {{
      background: linear-gradient(135deg, rgba(18, 20, 29, 0.95), rgba(28, 32, 48, 0.85));
      border: 1px solid rgba(0, 225, 255, 0.3);
      padding: 60px 48px;
      position: relative;
      border-radius: 4px;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 40px;
    }}
    @media (max-width: 900px) {{
      .cta-banner {{ flex-direction: column; text-align: center; padding: 40px 24px; }}
    }}
    .cta-banner-glow {{
      position: absolute;
      top: 50%;
      right: 10%;
      transform: translateY(-50%);
      width: 350px;
      height: 350px;
      background: radial-gradient(circle, rgba(255, 0, 122, 0.15) 0%, transparent 70%);
      filter: blur(60px);
      pointer-events: none;
    }}
  </style>
</head>
<body class="landing-body">

  <!-- Header -->
  {header_html}

  <!-- Pricing Hero -->
  <section class="pricing-hero-container">
    <div class="hero-glow-bg"></div>
    <div class="hero-grid-2col">
      <div>
        <div class="section-title-bordered">TRANSPARENT ENGAGEMENT MODELS</div>
        <h1 class="hero-title-h1">Predictable Pricing for <span class="gradient-text">Ambitious Products</span></h1>
        <p class="hero-desc-p">
          From rapid 3-week design sprints to dedicated multi-disciplinary engineering squads and custom enterprise AI automations, Vector Studioz provides transparent, value-aligned engagements with zero hidden fees.
        </p>
        <div class="hero-bullets">
          <div class="hero-bullet-item">
            <div class="hero-bullet-icon">✓</div>
            <span>100% intellectual property &amp; source code transfer</span>
          </div>
          <div class="hero-bullet-item">
            <div class="hero-bullet-icon">✓</div>
            <span>Senior-only designers &amp; engineers with zero junior offshoring</span>
          </div>
          <div class="hero-bullet-item">
            <div class="hero-bullet-icon">✓</div>
            <span>Flexible agile terms with seamless weekly sprint reporting</span>
          </div>
        </div>
      </div>

      <!-- Hero Summary Card -->
      <div style="background: rgba(18, 20, 29, 0.85); border: 1px solid rgba(255, 255, 255, 0.08); padding: 36px 32px; border-radius: 4px; position: relative;">
        <div block-corners-top=""></div>
        <div class="section-title-bordered" style="margin-bottom: 12px;">CLIENT GUARANTEE</div>
        <h3 style="font-size: 20px; font-weight: 700; color: #ffffff; margin: 0 0 12px;">The Vector Studioz Standard</h3>
        <p style="font-size: 14.5px; color: #9ca3af; line-height: 1.6; margin: 0 0 20px;">
          Every project is managed directly by a founding partner and backed by rigorous QA, automated tests, and award-winning aesthetic standards.
        </p>
        <div style="display: flex; gap: 20px; border-top: 1px solid rgba(255, 255, 255, 0.06); padding-top: 16px;">
          <div>
            <div style="font-family: 'Roboto Mono', monospace; font-size: 22px; font-weight: 700; color: #00ffa3;">140+</div>
            <div style="font-size: 12px; color: #9ca3af; text-transform: uppercase;">Shipped Products</div>
          </div>
          <div>
            <div style="font-family: 'Roboto Mono', monospace; font-size: 22px; font-weight: 700; color: #00e1ff;">99.2%</div>
            <div style="font-size: 12px; color: #9ca3af; text-transform: uppercase;">Client Retention</div>
          </div>
          <div>
            <div style="font-family: 'Roboto Mono', monospace; font-size: 22px; font-weight: 700; color: #ff007a;">5.0★</div>
            <div style="font-size: 12px; color: #9ca3af; text-transform: uppercase;">Clutch Rating</div>
          </div>
        </div>
        <div block-corners-bottom=""></div>
      </div>
    </div>
  </section>

  <!-- Pricing Tiers Grid -->
  <section class="content-section">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 20px;">
      <div class="section-title-bordered">SELECT YOUR PLAN</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        Tailored for Startups &amp; Growing Enterprises
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        Choose between fixed-price product sprints, monthly dedicated squads, or custom enterprise architecture.
      </p>
    </div>

    <!-- Monthly/Annual Retainer Toggle -->
    <div class="toggle-container">
      <button class="toggle-btn active" id="btn-monthly" onclick="setBilling('monthly')">Monthly Retainer</button>
      <button class="toggle-btn" id="btn-annual" onclick="setBilling('annual')">Annual Retainer <span class="discount-badge">Save 15%</span></button>
    </div>

    <div class="pricing-grid">
      <!-- Tier 1: Design Sprint & MVP -->
      <div class="pricing-card">
        <div block-corners-top=""></div>
        <div>
          <div class="tier-badge">FIXED SCOPE SPRINT</div>
          <div class="tier-title">Design Sprint &amp; MVP</div>
          <div class="tier-desc">Ideal for early-stage founders needing a category-defining design prototype and high-speed MVP launched in 3-4 weeks.</div>
          <div class="tier-price">$8,500</div>
          <div class="tier-period">Flat project investment</div>
          <ul class="tier-features">
            <li class="tier-feature-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg>
              <span>Full Figma design system &amp; clickable prototype</span>
            </li>
            <li class="tier-feature-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg>
              <span>Production Webflow or Next.js frontend build</span>
            </li>
            <li class="tier-feature-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg>
              <span>Mobile-first responsive optimization &amp; micro-interactions</span>
            </li>
            <li class="tier-feature-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg>
              <span>Complete source code &amp; design tokens handoff</span>
            </li>
          </ul>
        </div>
        <a class="btn-primary w-inline-block" href="contact-us.html?plan=sprint" scramble-link="" style="width: 100%;">
          <div class="btn-primary-lines btn-primary-lines-1" style="width: 100%;">
            <div class="btn-primary-lines btn-primary-lines-2" style="width: 100%; justify-content: center;">
              <div class="btn-primary-text" scramble-text="" style="width: 100%; text-align: center; justify-content: center;">Start MVP Sprint</div>
            </div>
          </div>
        </a>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Tier 2: Dedicated Product Squad (Featured) -->
      <div class="pricing-card featured">
        <div block-corners-top=""></div>
        <div style="position: absolute; top: -14px; right: 24px; background: linear-gradient(135deg, #ff007a, #7928ca); color: #fff; font-size: 11px; font-weight: 700; padding: 4px 12px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.08em;">MOST POPULAR</div>
        <div>
          <div class="tier-badge" style="color: #ff007a;">MONTHLY AGILE SQUAD</div>
          <div class="tier-title">Dedicated Product Squad</div>
          <div class="tier-desc">Your autonomous product team: 1 Senior Designer + 2 Full-Stack Engineers + 1 AI Architect scaling your product continuously.</div>
          <div class="tier-price" id="squad-price">$14,500</div>
          <div class="tier-period" id="squad-period">Per month / Cancel anytime</div>
          <ul class="tier-features">
            <li class="tier-feature-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg>
              <span>1 Senior Product Designer + 2 Senior Full-Stack Engineers</span>
            </li>
            <li class="tier-feature-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg>
              <span>Weekly agile sprint cycles &amp; direct Slack integration</span>
            </li>
            <li class="tier-feature-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg>
              <span>Unlimited feature requests &amp; design revisions</span>
            </li>
            <li class="tier-feature-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg>
              <span>Automated CI/CD pipelines &amp; rigorous code reviews</span>
            </li>
          </ul>
        </div>
        <a class="btn-primary w-inline-block" href="contact-us.html?plan=squad" scramble-link="" style="width: 100%;">
          <div class="btn-primary-lines btn-primary-lines-1" style="width: 100%;">
            <div class="btn-primary-lines btn-primary-lines-2" style="width: 100%; justify-content: center;">
              <div class="btn-primary-text" scramble-text="" style="width: 100%; text-align: center; justify-content: center;">Reserve Dedicated Squad</div>
            </div>
          </div>
        </a>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Tier 3: Enterprise Custom Systems -->
      <div class="pricing-card">
        <div block-corners-top=""></div>
        <div>
          <div class="tier-badge">CUSTOM ARCHITECTURE</div>
          <div class="tier-title">Enterprise Custom Systems</div>
          <div class="tier-desc">Comprehensive bespoke software engineering, multi-agent AI automation workflows, and spatial 3D WebGL experiences.</div>
          <div class="tier-price">Custom</div>
          <div class="tier-period">Tailored to scope &amp; SLA requirements</div>
          <ul class="tier-features">
            <li class="tier-feature-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg>
              <span>Custom multi-agent AI workflows &amp; fine-tuned LLM models</span>
            </li>
            <li class="tier-feature-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg>
              <span>3D WebGL interactive experiences &amp; custom Three.js shaders</span>
            </li>
            <li class="tier-feature-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg>
              <span>Enterprise cloud infrastructure, microservices &amp; security</span>
            </li>
            <li class="tier-feature-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6 9 17l-5-5"/></svg>
              <span>Dedicated Solutions Architect &amp; guaranteed 24/7 SLA</span>
            </li>
          </ul>
        </div>
        <a class="btn-primary w-inline-block" href="contact-us.html?plan=enterprise" scramble-link="" style="width: 100%;">
          <div class="btn-primary-lines btn-primary-lines-1" style="width: 100%;">
            <div class="btn-primary-lines btn-primary-lines-2" style="width: 100%; justify-content: center;">
              <div class="btn-primary-text" scramble-text="" style="width: 100%; text-align: center; justify-content: center;">Speak with Architect</div>
            </div>
          </div>
        </a>
        <div block-corners-bottom=""></div>
      </div>
    </div>
  </section>

  <!-- Scope & Agency FAQs (.faq-2 Webflow Accordion) -->
  <section class="content-section" style="border-top: 1px solid rgba(255, 255, 255, 0.06); padding-top: 80px;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 30px;">
      <div class="section-title-bordered">FREQUENTLY ASKED QUESTIONS</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        Billing, Contracts, &amp; Engagement FAQs
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        Clear answers on how we collaborate, invoice, and transition deliverables to your internal teams.
      </p>
    </div>

    <div class="faq-list">
      <!-- Item 1 -->
      <div class="faq-2 open">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">Who owns the intellectual property and code?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          You own 100% of all intellectual property, design assets, Figma files, and custom source code. As invoices are settled, full copyright and ownership are immediately transferred to your company without licensing caveats.
        </div>
      </div>

      <!-- Item 2 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">How do revision rounds work during active design sprints?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          We operate on continuous async collaboration rather than rigid waterfall batches. You will have real-time access to our Figma files and GitHub repositories, with rapid turnarounds on feedback during your sprint cycle.
        </div>
      </div>

      <!-- Item 3 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">Can we pause, cancel, or scale our Dedicated Product Squad retainer?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Yes. Our monthly retainers operate on flexible 30-day notice terms. If your product needs change or you transition between funding rounds, you can easily pause or scale your squad size without penalties.
        </div>
      </div>

      <!-- Item 4 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">What technologies and frameworks does Vector Studioz specialize in?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Our core stack includes Figma for design systems, Webflow and Next.js / React for frontends, TypeScript, Python, and Node.js for scalable backends, Three.js / WebGL for interactive 3D, and leading open-weights / API model pipelines for AI automation.
        </div>
      </div>

      <!-- Item 5 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">How quickly can our project kick off?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Following our initial 30-minute discovery call and scope alignment, dedicated squads and sprint projects typically kick off within 5 to 7 business days.
        </div>
      </div>
    </div>
  </section>

  <!-- Bottom Rainbow CTA Banner -->
  <div class="cta-banner-wrapper">
    <div class="cta-banner">
      <div block-corners-top=""></div>
      <div class="cta-banner-glow"></div>
      <div style="position: relative; z-index: 1; max-width: 650px;">
        <div class="section-title-bordered" style="margin-bottom: 12px;">READY TO ELEVATE YOUR BRAND?</div>
        <h3 style="font-size: clamp(24px, 3vw, 36px); font-weight: 800; color: #ffffff; margin: 0 0 12px;">
          Build Something Category-Defining with Vector Studioz
        </h3>
        <p style="color: #9ca3af; font-size: 15px; margin: 0; line-height: 1.6;">
          Schedule a 30-minute discovery session with our founding partners to discuss your product vision, timeline, and goals.
        </p>
      </div>

      <div style="position: relative; z-index: 1; display: flex; gap: 16px; flex-wrap: wrap;">
        <a class="btn-primary w-inline-block" href="contact-us.html" scramble-link="">
          <div class="btn-primary-lines btn-primary-lines-1">
            <div class="btn-primary-lines btn-primary-lines-2">
              <div class="btn-primary-text" scramble-text="">Start a Project</div>
            </div>
          </div>
        </a>
      </div>
      <div block-corners-bottom=""></div>
    </div>
  </div>

  <!-- Footer -->
  {footer_html}

  <script>
    function toggleFaq(element) {{
      const card = element.closest('.faq-2');
      const wasOpen = card.classList.contains('open');
      document.querySelectorAll('.faq-2').forEach(f => f.classList.remove('open'));
      if (!wasOpen) {{
        card.classList.add('open');
      }}
    }}

    function setBilling(mode) {{
      const monthlyBtn = document.getElementById('btn-monthly');
      const annualBtn = document.getElementById('btn-annual');
      const squadPrice = document.getElementById('squad-price');
      const squadPeriod = document.getElementById('squad-period');

      if (mode === 'annual') {{
        annualBtn.classList.add('active');
        monthlyBtn.classList.remove('active');
        squadPrice.innerText = '$12,300';
        squadPeriod.innerText = 'Per month / Billed annually';
      }} else {{
        monthlyBtn.classList.add('active');
        annualBtn.classList.remove('active');
        squadPrice.innerText = '$14,500';
        squadPeriod.innerText = 'Per month / Cancel anytime';
      }}
    }}
  </script>
</body>
</html>
"""

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(PAGE_HTML)

print("Successfully generated Vector Studioz agency pricing.html")
