# Generator for Agency Native Webflow about.html

with open('template_header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

with open('template_footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

PAGE_HTML = f"""<!DOCTYPE html>
<html data-wf-domain="www.vectorstudioz.com" data-wf-page="6488c93b137bd37e5762ce46" data-wf-site="64354b8ce4872ad8cd1c7b04" lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>About Studio — Vector Studioz | Elite Digital Experience &amp; AI Agency</title>
  <meta name="description" content="Vector Studioz is an elite digital product agency uniting bespoke UI/UX design, scalable full-stack software development, and autonomous AI automation."/>
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
    .about-hero-container {{
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
    .hero-stats-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
      margin-top: 24px;
    }}
    .stat-holo-card {{
      background: rgba(18, 20, 29, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 24px 20px;
      border-radius: 4px;
      position: relative;
      transition: all 0.3s ease;
    }}
    .stat-holo-card:hover {{
      border-color: rgba(0, 225, 255, 0.4);
      transform: translateY(-2px);
      box-shadow: 0 10px 25px -5px rgba(0, 225, 255, 0.15);
    }}
    .stat-number {{
      font-size: 34px;
      font-weight: 800;
      font-family: 'Roboto Mono', monospace;
      color: #00e1ff;
      margin-bottom: 6px;
    }}
    .stat-label {{
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #9ca3af;
      font-weight: 600;
    }}

    /* Bento Pillars */
    .content-section {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 60px 2rem;
    }}
    .pillars-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
      margin-top: 40px;
    }}
    @media (max-width: 768px) {{
      .pillars-grid {{ grid-template-columns: 1fr; }}
    }}
    .pillar-card {{
      background: rgba(18, 20, 29, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 36px 32px;
      position: relative;
      transition: all 0.3s ease;
      display: flex;
      flex-direction: column;
    }}
    .pillar-card:hover {{
      border-color: rgba(255, 0, 122, 0.4);
      background: rgba(22, 25, 38, 0.85);
      transform: translateY(-3px);
    }}
    .pillar-icon {{
      width: 48px;
      height: 48px;
      border-radius: 8px;
      background: rgba(0, 225, 255, 0.1);
      border: 1px solid rgba(0, 225, 255, 0.25);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 20px;
      color: #00e1ff;
    }}
    .pillar-title {{
      font-size: 20px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 12px;
    }}
    .pillar-desc {{
      font-size: 15px;
      color: #9ca3af;
      line-height: 1.6;
    }}

    /* Leadership Team Grid */
    .team-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-top: 40px;
    }}
    @media (max-width: 1100px) {{
      .team-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
      .team-grid {{ grid-template-columns: 1fr; }}
    }}
    .team-card {{
      background: rgba(18, 20, 29, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 28px 24px;
      position: relative;
      transition: all 0.3s ease;
      text-align: center;
    }}
    .team-card:hover {{
      border-color: rgba(0, 225, 255, 0.45);
      transform: translateY(-3px);
    }}
    .team-avatar {{
      width: 80px;
      height: 80px;
      border-radius: 50%;
      margin: 0 auto 18px;
      background: linear-gradient(135deg, rgba(255, 0, 122, 0.2), rgba(0, 225, 255, 0.3));
      border: 2px solid rgba(0, 225, 255, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 26px;
      color: #00e1ff;
      font-weight: 800;
      font-family: 'Roboto Mono', monospace;
    }}
    .team-name {{
      font-size: 18px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 4px;
    }}
    .team-role {{
      font-size: 13px;
      font-weight: 600;
      color: #00ffa3;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 12px;
      font-family: 'Roboto Mono', monospace;
    }}
    .team-bio {{
      font-size: 13.5px;
      color: #9ca3af;
      line-height: 1.5;
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

  <!-- About Hero -->
  <section class="about-hero-container">
    <div class="hero-glow-bg"></div>
    <div class="hero-grid-2col">
      <div>
        <div class="section-title-bordered">ABOUT VECTOR STUDIOZ</div>
        <h1 class="hero-title-h1">We Craft Digital Experiences That <span class="gradient-text">Define Categories</span></h1>
        <p class="hero-desc-p">
          Vector Studioz is an elite digital product agency uniting world-class UI/UX design, modern full-stack software development, and autonomous AI automation. We partner with ambitious founders and visionary enterprises to ship iconic digital products.
        </p>
        <div style="display: flex; gap: 16px; flex-wrap: wrap;">
          <a class="btn-primary w-inline-block" href="pricing.html" scramble-link="">
            <div class="btn-primary-lines btn-primary-lines-1">
              <div class="btn-primary-lines btn-primary-lines-2">
                <div class="btn-primary-text" scramble-text="">Explore Retainers</div>
              </div>
            </div>
          </a>
          <a class="btn-secondary w-inline-block" href="contact-us.html" style="padding: 12px 24px; border: 1px solid rgba(255,255,255,0.15); border-radius: 2px; color: #ffffff; text-decoration: none; font-weight: 600; font-size: 14px; display: inline-flex; align-items: center; transition: all 0.2s;">
            Book Discovery Call
          </a>
        </div>
      </div>

      <!-- Holographic Stats Grid -->
      <div class="hero-stats-grid">
        <div class="stat-holo-card">
          <div block-corners-top=""></div>
          <div class="stat-number">140+</div>
          <div class="stat-label">Projects Delivered</div>
          <div block-corners-bottom=""></div>
        </div>
        <div class="stat-holo-card">
          <div block-corners-top=""></div>
          <div class="stat-number">99.2%</div>
          <div class="stat-label">Client Retention</div>
          <div block-corners-bottom=""></div>
        </div>
        <div class="stat-holo-card">
          <div block-corners-top=""></div>
          <div class="stat-number">12</div>
          <div class="stat-label">International Awards</div>
          <div block-corners-bottom=""></div>
        </div>
        <div class="stat-holo-card">
          <div block-corners-top=""></div>
          <div class="stat-number">5.0★</div>
          <div class="stat-label">Clutch &amp; Client Rating</div>
          <div block-corners-bottom=""></div>
        </div>
      </div>
    </div>
  </section>

  <!-- 4 Core Craft Pillars Bento -->
  <section class="content-section">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 30px;">
      <div class="section-title-bordered">OUR CRAFT PILLARS</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        Where Radical Craft Meets Engineering Precision
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        We reject generic templates and cookie-cutter code. Every digital product we build is designed from first principles.
      </p>
    </div>

    <div class="pillars-grid">
      <!-- Pillar 1 -->
      <div class="pillar-card">
        <div block-corners-top=""></div>
        <div class="pillar-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/></svg>
        </div>
        <div class="pillar-title">Bespoke Visual Excellence</div>
        <div class="pillar-desc">
          World-class UI/UX, scalable design systems, and bespoke typography. We design category-defining experiences that captivate users and elevate brand equity.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Pillar 2 -->
      <div class="pillar-card">
        <div block-corners-top=""></div>
        <div class="pillar-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
        </div>
        <div class="pillar-title">Scalable Modern Architecture</div>
        <div class="pillar-desc">
          Production-grade codebases built with Next.js, React, TypeScript, and Node.js. Sub-second load times, flawless responsiveness, and bulletproof security.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Pillar 3 -->
      <div class="pillar-card">
        <div block-corners-top=""></div>
        <div class="pillar-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 7h10"/><path d="M7 12h10"/><path d="M7 17h10"/></svg>
        </div>
        <div class="pillar-title">Intelligent AI Workflows</div>
        <div class="pillar-desc">
          We integrate autonomous multi-agent pipelines, specialized LLM fine-tuning, and smart operational workflows that multiply team leverage and drive growth.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Pillar 4 -->
      <div class="pillar-card">
        <div block-corners-top=""></div>
        <div class="pillar-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        </div>
        <div class="pillar-title">Relentless Execution Velocity</div>
        <div class="pillar-desc">
          Zero bureaucratic delays. You work directly with senior designers and engineers inside your daily Slack channel with weekly production sprint ship dates.
        </div>
        <div block-corners-bottom=""></div>
      </div>
    </div>
  </section>

  <!-- Leadership / Creative Team Grid -->
  <section class="content-section" style="border-top: 1px solid rgba(255, 255, 255, 0.06); padding-top: 80px;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 30px;">
      <div class="section-title-bordered">LEADERSHIP &amp; PARTNERS</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        Led by Designers, Engineers, &amp; Product Builders
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        Our founders have built and scaled digital products recognized on Awwwards, Product Hunt, and TechCrunch.
      </p>
    </div>

    <div class="team-grid">
      <!-- Member 1 -->
      <div class="team-card">
        <div block-corners-top=""></div>
        <div class="team-avatar">MV</div>
        <div class="team-name">Marcus Vance</div>
        <div class="team-role">Creative Director &amp; Co-Founder</div>
        <div class="team-bio">
          Former Principal Designer at Pentagram and Fantasy. Winner of 10+ Awwwards Site of the Day honors and judged global design competitions.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Member 2 -->
      <div class="team-card">
        <div block-corners-top=""></div>
        <div class="team-avatar">SL</div>
        <div class="team-name">Sarah Lin</div>
        <div class="team-role">Head of Engineering &amp; Co-Founder</div>
        <div class="team-bio">
          Ex-Stripe infrastructure architect. Scaled distributed web systems supporting tens of millions of active users with sub-second latency.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Member 3 -->
      <div class="team-card">
        <div block-corners-top=""></div>
        <div class="team-avatar">AT</div>
        <div class="team-name">Dr. Aris Thorne</div>
        <div class="team-role">AI Solutions Architect</div>
        <div class="team-bio">
          Former Stanford AI Lab researcher specializing in autonomous multi-agent pipelines, transformer fine-tuning, and production LLM orchestration.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Member 4 -->
      <div class="team-card">
        <div block-corners-top=""></div>
        <div class="team-avatar">JM</div>
        <div class="team-name">Jessica Miller</div>
        <div class="team-role">Head of Client Experience</div>
        <div class="team-bio">
          Over a decade managing client partnerships for enterprise brands and Series A-C startups, maintaining our 99.2% client satisfaction record.
        </div>
        <div block-corners-bottom=""></div>
      </div>
    </div>
  </section>

  <!-- FAQ Section (Webflow .faq-2 Accordion) -->
  <section class="content-section" style="border-top: 1px solid rgba(255, 255, 255, 0.06); padding-top: 80px;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 30px;">
      <div class="section-title-bordered">FREQUENTLY ASKED QUESTIONS</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        Collaborating with Vector Studioz
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        How we integrate with your team, manage timelines, and guarantee deliverable quality.
      </p>
    </div>

    <div class="faq-list">
      <!-- Item 1 -->
      <div class="faq-2 open">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">What types of clients does Vector Studioz partner with?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          We partner with venture-backed technology startups, high-growth scale-ups, and established brands across SaaS, fintech, AI, and consumer tech who require world-class digital experiences and custom software systems.
        </div>
      </div>

      <!-- Item 2 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">How does Vector Studioz differ from traditional digital agencies?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Traditional agencies rely on junior staff and middle-management layers. At Vector Studioz, you work directly with senior craftspeople—no fluff, no telephone games, and direct access in Slack with daily async progress updates.
        </div>
      </div>

      <!-- Item 3 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">Can you work alongside our existing in-house team?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Absolutely. Many of our clients embed our Dedicated Product Squads directly alongside their existing product managers and engineers to accelerate roadmap velocity or build new experimental greenfield features.
        </div>
      </div>

      <!-- Item 4 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">Where are Vector Studioz teams located?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          We operate as a distributed studio headquartered in San Francisco with creative hubs in London and New York, serving clients seamlessly across North American and European time zones.
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
          Let's discuss how our design, software engineering, and AI automation capabilities can accelerate your growth.
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
  </script>
</body>
</html>
"""

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(PAGE_HTML)

print("Successfully generated Vector Studioz agency about.html")
