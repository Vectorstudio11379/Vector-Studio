# Generator for Agency Native Webflow careers.html

with open('template_header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

with open('template_footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

PAGE_HTML = f"""<!DOCTYPE html>
<html data-wf-domain="www.vectorstudioz.com" data-wf-page="6488c93b137bd37e5762ce47" data-wf-site="64354b8ce4872ad8cd1c7b04" lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Careers — Vector Studioz | Join the Creative &amp; Engineering Vanguard</title>
  <meta name="description" content="Explore open roles in UI/UX design, full-stack software development, 3D WebGL, and AI automation at Vector Studioz. 100% remote-first with top-tier compensation."/>
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
    .careers-hero-container {{
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
      max-width: 780px;
      margin: 0 auto 32px;
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

    .content-section {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 60px 2rem;
    }}

    /* Values Bento */
    .values-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
      margin-top: 40px;
    }}
    @media (max-width: 768px) {{
      .values-grid {{ grid-template-columns: 1fr; }}
    }}
    .value-card {{
      background: rgba(18, 20, 29, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 32px 28px;
      position: relative;
      transition: all 0.3s ease;
    }}
    .value-card:hover {{
      border-color: rgba(0, 225, 255, 0.4);
      transform: translateY(-2px);
    }}
    .value-title {{
      font-size: 19px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .value-desc {{
      color: #9ca3af;
      font-size: 15px;
      line-height: 1.6;
    }}

    /* Open Roles */
    .roles-list {{
      display: flex;
      flex-direction: column;
      gap: 16px;
      margin-top: 40px;
    }}
    .role-card {{
      background: rgba(18, 20, 29, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 28px 32px;
      position: relative;
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 24px;
      transition: all 0.25s ease;
    }}
    @media (max-width: 860px) {{
      .role-card {{ flex-direction: column; align-items: flex-start; }}
    }}
    .role-card:hover {{
      border-color: rgba(0, 225, 255, 0.4);
      background: rgba(22, 25, 38, 0.9);
      transform: translateY(-2px);
    }}
    .role-dept {{
      font-family: 'Roboto Mono', monospace;
      font-size: 12px;
      color: #00e1ff;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 6px;
    }}
    .role-title {{
      font-size: 20px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 8px;
    }}
    .role-meta {{
      display: flex;
      gap: 14px;
      font-size: 13.5px;
      color: #9ca3af;
      flex-wrap: wrap;
    }}
    .role-tag {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 3px 10px;
      border-radius: 3px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }}

    /* Hiring Pipeline */
    .pipeline-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-top: 40px;
    }}
    @media (max-width: 991px) {{
      .pipeline-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
      .pipeline-grid {{ grid-template-columns: 1fr; }}
    }}
    .pipeline-step {{
      background: rgba(18, 20, 29, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 28px 24px;
      position: relative;
    }}
    .step-badge {{
      font-family: 'Roboto Mono', monospace;
      font-size: 13px;
      font-weight: 700;
      color: #00e1ff;
      margin-bottom: 12px;
    }}
    .step-name {{
      font-size: 17px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 8px;
    }}
    .step-desc {{
      font-size: 14px;
      color: #9ca3af;
      line-height: 1.5;
    }}

    /* Perks Grid */
    .perks-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-top: 40px;
    }}
    @media (max-width: 900px) {{
      .perks-grid {{ grid-template-columns: repeat(2, 1fr); }}
    }}
    @media (max-width: 600px) {{
      .perks-grid {{ grid-template-columns: 1fr; }}
    }}
    .perk-card {{
      background: rgba(18, 20, 29, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 24px;
      position: relative;
    }}
    .perk-title {{
      font-size: 16px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 6px;
    }}
    .perk-desc {{
      font-size: 13.5px;
      color: #9ca3af;
      line-height: 1.5;
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

  <!-- Careers Hero -->
  <section class="careers-hero-container" style="text-align: center;">
    <div class="hero-glow-bg"></div>
    <div class="section-title-bordered">CAREERS AT VECTOR STUDIOZ</div>
    <h1 class="hero-title-h1">Join the Creative &amp; <span class="gradient-text">Engineering Vanguard</span></h1>
    <p class="hero-desc-p">
      We are an elite, globally distributed digital product studio building category-defining web experiences, scalable software architectures, and autonomous AI automation systems. Do the best work of your career with high trust and zero bureaucracy.
    </p>
    <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
      <a class="btn-primary w-inline-block" href="#open-roles" scramble-link="">
        <div class="btn-primary-lines btn-primary-lines-1">
          <div class="btn-primary-lines btn-primary-lines-2">
            <div class="btn-primary-text" scramble-text="">View 5 Open Roles</div>
          </div>
        </div>
      </a>
      <a class="btn-secondary w-inline-block" href="#culture" style="padding: 12px 24px; border: 1px solid rgba(255,255,255,0.15); border-radius: 2px; color: #ffffff; text-decoration: none; font-weight: 600; font-size: 14px; display: inline-flex; align-items: center; transition: all 0.2s;">
        Studio Culture
      </a>
    </div>
  </section>

  <!-- Culture & Values Bento -->
  <section id="culture" class="content-section" style="border-top: 1px solid rgba(255, 255, 255, 0.06);">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 30px;">
      <div class="section-title-bordered">STUDIO VALUES</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        How We Build, Collaborate, and Ship
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        We reject corporate bureaucracy in favor of craft excellence, radical ownership, and asynchronous speed.
      </p>
    </div>

    <div class="values-grid">
      <!-- Value 1 -->
      <div class="value-card">
        <div block-corners-top=""></div>
        <div class="value-title">
          <span style="color: #00e1ff;">01.</span> Creative Autonomy
        </div>
        <div class="value-desc">
          We hire experienced craftspeople and give them full authority. You own products from initial Figma concept through to production launch with zero micro-management.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Value 2 -->
      <div class="value-card">
        <div block-corners-top=""></div>
        <div class="value-title">
          <span style="color: #ff007a;">02.</span> Craft Over Bureaucracy
        </div>
        <div class="value-desc">
          No endless status meetings or middle managers. We coordinate via Slack, async Loom walkthroughs, and clear GitHub pull requests with direct partner feedback.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Value 3 -->
      <div class="value-card">
        <div block-corners-top=""></div>
        <div class="value-title">
          <span style="color: #00ffa3;">03.</span> High-Velocity Innovation
        </div>
        <div class="value-desc">
          We constantly explore the bleeding edge: custom GLSL shaders, 3D WebGL interactions, Next.js App Router optimizations, and autonomous AI agent workflows.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Value 4 -->
      <div class="value-card">
        <div block-corners-top=""></div>
        <div class="value-title">
          <span style="color: #ffe600;">04.</span> Extreme Transparency
        </div>
        <div class="value-desc">
          Open communication, competitive formula-based salaries, and studio profit sharing. Everyone shares in the upside of the products we bring to market.
        </div>
        <div block-corners-bottom=""></div>
      </div>
    </div>
  </section>

  <!-- Open Roles Section -->
  <section id="open-roles" class="content-section" style="border-top: 1px solid rgba(255, 255, 255, 0.06); padding-top: 80px;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 30px;">
      <div class="section-title-bordered">CURRENT OPENINGS</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        Join Our Distributed Design &amp; Engineering Squads
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        All positions are 100% remote with competitive base salaries, profit sharing, and full hardware setups.
      </p>
    </div>

    <div class="roles-list">
      <!-- Role 1 -->
      <div class="role-card">
        <div block-corners-top=""></div>
        <div>
          <div class="role-dept">Design &amp; Experience</div>
          <div class="role-title">Senior Product Designer (UI/UX &amp; Design Systems)</div>
          <div class="role-meta">
            <span class="role-tag">🌍 Remote (Global)</span>
            <span class="role-tag">⚡ Full-Time</span>
            <span class="role-tag">💰 $140k - $180k + Profit Share</span>
          </div>
        </div>
        <div>
          <a class="btn-primary w-inline-block" href="contact-us.html?role=product-designer" scramble-link="">
            <div class="btn-primary-lines btn-primary-lines-1">
              <div class="btn-primary-lines btn-primary-lines-2">
                <div class="btn-primary-text" scramble-text="">Apply Now</div>
              </div>
            </div>
          </a>
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Role 2 -->
      <div class="role-card">
        <div block-corners-top=""></div>
        <div>
          <div class="role-dept">Software Engineering</div>
          <div class="role-title">Lead Full-Stack Architect (Next.js / TypeScript / Node)</div>
          <div class="role-meta">
            <span class="role-tag">🌍 Remote (Global)</span>
            <span class="role-tag">⚡ Full-Time</span>
            <span class="role-tag">💰 $160k - $210k + Profit Share</span>
          </div>
        </div>
        <div>
          <a class="btn-primary w-inline-block" href="contact-us.html?role=fullstack-lead" scramble-link="">
            <div class="btn-primary-lines btn-primary-lines-1">
              <div class="btn-primary-lines btn-primary-lines-2">
                <div class="btn-primary-text" scramble-text="">Apply Now</div>
              </div>
            </div>
          </a>
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Role 3 -->
      <div class="role-card">
        <div block-corners-top=""></div>
        <div>
          <div class="role-dept">Artificial Intelligence</div>
          <div class="role-title">AI Automation &amp; Multi-Agent Solutions Engineer</div>
          <div class="role-meta">
            <span class="role-tag">🌍 Remote (Global)</span>
            <span class="role-tag">⚡ Full-Time</span>
            <span class="role-tag">💰 $170k - $220k + Profit Share</span>
          </div>
        </div>
        <div>
          <a class="btn-primary w-inline-block" href="contact-us.html?role=ai-engineer" scramble-link="">
            <div class="btn-primary-lines btn-primary-lines-1">
              <div class="btn-primary-lines btn-primary-lines-2">
                <div class="btn-primary-text" scramble-text="">Apply Now</div>
              </div>
            </div>
          </a>
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Role 4 -->
      <div class="role-card">
        <div block-corners-top=""></div>
        <div>
          <div class="role-dept">Creative Technology</div>
          <div class="role-title">Creative WebGL &amp; 3D Interactive Developer (Three.js)</div>
          <div class="role-meta">
            <span class="role-tag">🌍 Remote (Global)</span>
            <span class="role-tag">⚡ Full-Time</span>
            <span class="role-tag">💰 $150k - $195k + Profit Share</span>
          </div>
        </div>
        <div>
          <a class="btn-primary w-inline-block" href="contact-us.html?role=webgl-developer" scramble-link="">
            <div class="btn-primary-lines btn-primary-lines-1">
              <div class="btn-primary-lines btn-primary-lines-2">
                <div class="btn-primary-text" scramble-text="">Apply Now</div>
              </div>
            </div>
          </a>
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Role 5 -->
      <div class="role-card">
        <div block-corners-top=""></div>
        <div>
          <div class="role-dept">Product Delivery</div>
          <div class="role-title">Technical Project Lead &amp; Agile Delivery Manager</div>
          <div class="role-meta">
            <span class="role-tag">🌍 Remote (Global)</span>
            <span class="role-tag">⚡ Full-Time</span>
            <span class="role-tag">💰 $135k - $175k + Profit Share</span>
          </div>
        </div>
        <div>
          <a class="btn-primary w-inline-block" href="contact-us.html?role=delivery-lead" scramble-link="">
            <div class="btn-primary-lines btn-primary-lines-1">
              <div class="btn-primary-lines btn-primary-lines-2">
                <div class="btn-primary-text" scramble-text="">Apply Now</div>
              </div>
            </div>
          </a>
        </div>
        <div block-corners-bottom=""></div>
      </div>
    </div>
  </section>

  <!-- Hiring Pipeline -->
  <section class="content-section" style="border-top: 1px solid rgba(255, 255, 255, 0.06); padding-top: 80px;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 30px;">
      <div class="section-title-bordered">TRANSPARENT PROCESS</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        A Fast, Respectful 4-Stage Interview Journey
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        We value your time. Our hiring loop finishes in under two weeks with direct feedback after every stage.
      </p>
    </div>

    <div class="pipeline-grid">
      <!-- Step 1 -->
      <div class="pipeline-step">
        <div block-corners-top=""></div>
        <div class="step-badge">STAGE 01 // 48 HOURS</div>
        <div class="step-name">Portfolio &amp; Async Review</div>
        <div class="step-desc">
          We review your actual Figma files, GitHub repositories, or live shipped products. No generic HR screenings.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Step 2 -->
      <div class="pipeline-step">
        <div block-corners-top=""></div>
        <div class="step-badge">STAGE 02 // 60 MINS</div>
        <div class="step-name">Design &amp; Architecture Deep-Dive</div>
        <div class="step-desc">
          A peer-to-peer technical conversation with one of our co-founders or senior discipline leads.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Step 3 -->
      <div class="pipeline-step">
        <div block-corners-top=""></div>
        <div class="step-badge">STAGE 03 // 3-5 DAYS</div>
        <div class="step-name">Paid Practical Project</div>
        <div class="step-desc">
          A real-world project task mirroring our daily client work. We compensate you fairly for your time ($1,000 stipend).
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Step 4 -->
      <div class="pipeline-step">
        <div block-corners-top=""></div>
        <div class="step-badge">STAGE 04 // 24 HOURS</div>
        <div class="step-name">Partner Offer &amp; Equity Grant</div>
        <div class="step-desc">
          Transparent compensation terms, annual profit-sharing agreement, and your official studio onboarding roadmap.
        </div>
        <div block-corners-bottom=""></div>
      </div>
    </div>
  </section>

  <!-- Perks & Benefits -->
  <section class="content-section" style="border-top: 1px solid rgba(255, 255, 255, 0.06); padding-top: 80px;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 30px;">
      <div class="section-title-bordered">PERKS &amp; BENEFITS</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        Engineered for High Autonomy &amp; Craft
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        Everything you need to do the best work of your career from anywhere in the world.
      </p>
    </div>

    <div class="perks-grid">
      <div class="perk-card">
        <div block-corners-top=""></div>
        <div class="perk-title">🌍 100% Global Remote</div>
        <div class="perk-desc">Work from wherever you are happiest. We coordinate asynchronously across time zones.</div>
        <div block-corners-bottom=""></div>
      </div>
      <div class="perk-card">
        <div block-corners-top=""></div>
        <div class="perk-title">💰 Base + Profit Sharing</div>
        <div class="perk-desc">Top-of-market base compensation paired with transparent quarterly studio profit distributions.</div>
        <div block-corners-bottom=""></div>
      </div>
      <div class="perk-card">
        <div block-corners-top=""></div>
        <div class="perk-title">🏝️ Annual Global Retreats</div>
        <div class="perk-desc">Twice a year we fly the entire team to destinations like Lisbon, Tokyo, and Montreal for strategy and connection.</div>
        <div block-corners-bottom=""></div>
      </div>
      <div class="perk-card">
        <div block-corners-top=""></div>
        <div class="perk-title">💻 $4,000 Workspace Stipend</div>
        <div class="perk-desc">Top-of-the-line Apple silicon MacBook Pro or workstation, Herman Miller chair, and 4K displays.</div>
        <div block-corners-bottom=""></div>
      </div>
      <div class="perk-card">
        <div block-corners-top=""></div>
        <div class="perk-title">📚 Unlimited Learning Budget</div>
        <div class="perk-desc">Company-sponsored attendance at Config, Awwwards Conference, design courses, and technical books.</div>
        <div block-corners-bottom=""></div>
      </div>
      <div class="perk-card">
        <div block-corners-top=""></div>
        <div class="perk-title">🏥 Premium Health &amp; Wellness</div>
        <div class="perk-desc">Comprehensive medical, dental, and mental health coverage for you and your dependents globally.</div>
        <div block-corners-bottom=""></div>
      </div>
    </div>
  </section>

  <!-- FAQ Section (Webflow .faq-2 Accordion) -->
  <section class="content-section" style="border-top: 1px solid rgba(255, 255, 255, 0.06); padding-top: 80px;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 30px;">
      <div class="section-title-bordered">FREQUENTLY ASKED QUESTIONS</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        Careers &amp; Life at Vector Studioz
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        Everything you need to know about remote setups, contracts, and evaluation.
      </p>
    </div>

    <div class="faq-list">
      <!-- Item 1 -->
      <div class="faq-2 open">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">Can I work from any country or time zone?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Yes. Vector Studioz is a borderless digital studio. We hire exceptional craftspeople globally via direct international contractor agreements or local Employer of Record (EOR) providers.
        </div>
      </div>

      <!-- Item 2 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">How does studio profit sharing work?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          A dedicated percentage of quarterly studio net profits is distributed directly to full-time team members based on tenure and impact, ensuring everyone shares in the agency's commercial success.
        </div>
      </div>

      <!-- Item 3 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">What if I don't see an exact opening for my skillset?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          We always create space for extraordinary creative and engineering talent. Send us your portfolio, GitHub, or case studies through our contact page with a note on what you'd love to build.
        </div>
      </div>

      <!-- Item 4 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">Do you support personal side projects and open source?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Yes. Many of our team members maintain popular open-source packages, Figma UI kits, and creative experiments. We actively sponsor and celebrate your personal creative output.
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
        <div class="section-title-bordered" style="margin-bottom: 12px;">READY TO BUILD WITH US?</div>
        <h3 style="font-size: clamp(24px, 3vw, 36px); font-weight: 800; color: #ffffff; margin: 0 0 12px;">
          Deploy Your Craft at the Cutting Edge of Digital Products
        </h3>
        <p style="color: #9ca3af; font-size: 15px; margin: 0; line-height: 1.6;">
          Join our distributed studio and build digital platforms that win awards and drive measurable business impact.
        </p>
      </div>

      <div style="position: relative; z-index: 1; display: flex; gap: 16px; flex-wrap: wrap;">
        <a class="btn-primary w-inline-block" href="contact-us.html" scramble-link="">
          <div class="btn-primary-lines btn-primary-lines-1">
            <div class="btn-primary-lines btn-primary-lines-2">
              <div class="btn-primary-text" scramble-text="">Send General Application</div>
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

with open('careers.html', 'w', encoding='utf-8') as f:
    f.write(PAGE_HTML)

print("Successfully generated Vector Studioz agency careers.html")
