# Generator for Webflow Native careers.html

with open('template_header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

with open('template_footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

PAGE_HTML = f"""<!DOCTYPE html>
<html data-wf-domain="www.coingpt.tech" data-wf-page="6488c93b137bd37e5762ce47" data-wf-site="64354b8ce4872ad8cd1c7b04" lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Careers — CoinGPT | Build the Neural Architecture of Web3</title>
  <meta name="description" content="Explore open roles in AI research, distributed systems engineering, smart contract security, and Web3 infrastructure at CoinGPT. 100% remote-first with top-tier token compensation."/>
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
      --cyan: #28efce;
      --purple: #6a59e5;
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
      width: 750px;
      height: 450px;
      background: radial-gradient(circle, rgba(0, 255, 163, 0.15) 0%, rgba(40, 239, 206, 0.08) 45%, transparent 70%);
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
      background: linear-gradient(135deg, #00ffa3 0%, #28efce 50%, #6a59e5 100%);
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
      border-color: #00ffa3;
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
      border-color: #00ffa3;
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
      border: 1px solid rgba(0, 255, 163, 0.25);
      border-radius: 4px;
      background: rgba(0, 255, 163, 0.04);
      font-family: 'Roboto Mono', monospace;
      font-size: 12px;
      letter-spacing: 0.1em;
      color: #00ffa3;
      text-transform: uppercase;
      margin-bottom: 16px;
    }}
    .section-title-bordered::before {{
      content: '';
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #00ffa3;
      box-shadow: 0 0 8px #00ffa3;
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
      border-color: rgba(0, 255, 163, 0.4);
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
      border-color: rgba(0, 255, 163, 0.4);
      background: rgba(22, 25, 38, 0.9);
      transform: translateY(-2px);
    }}
    .role-dept {{
      font-family: 'Roboto Mono', monospace;
      font-size: 12px;
      color: #00ffa3;
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
      color: #00ffa3;
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
      border-color: rgba(0, 255, 163, 0.35);
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
      color: #00ffa3;
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
      border: 1px solid rgba(0, 255, 163, 0.3);
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
      background: radial-gradient(circle, rgba(0, 255, 163, 0.15) 0%, transparent 70%);
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
    <div class="section-title-bordered">CAREERS AT COINGPT</div>
    <h1 class="hero-title-h1">Build the Neural Architecture of <span class="gradient-text">Web3</span></h1>
    <p class="hero-desc-p">
      We are an elite, globally distributed team of AI researchers, distributed systems architects, and cryptography veterans building the autonomous cognitive infrastructure of decentralized finance.
    </p>
    <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
      <a class="btn-primary w-inline-block" href="#open-roles" scramble-link="">
        <div class="btn-primary-lines btn-primary-lines-1">
          <div class="btn-primary-lines btn-primary-lines-2">
            <div class="btn-primary-text" scramble-text="">View 6 Open Roles</div>
          </div>
        </div>
      </a>
      <a class="btn-secondary w-inline-block" href="#culture" style="padding: 12px 24px; border: 1px solid rgba(255,255,255,0.15); border-radius: 2px; color: #ffffff; text-decoration: none; font-weight: 600; font-size: 14px; display: inline-flex; align-items: center; transition: all 0.2s;">
        Our Engineering Culture
      </a>
    </div>
  </section>

  <!-- Culture & Values Bento -->
  <section id="culture" class="content-section" style="border-top: 1px solid rgba(255, 255, 255, 0.06);">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 30px;">
      <div class="section-title-bordered">CULTURE &amp; VALUES</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        How We Build, Ship, and Lead
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        We reject corporate bureaucracy in favor of technical rigor, radical candor, and asynchronous ownership.
      </p>
    </div>

    <div class="values-grid">
      <!-- Value 1 -->
      <div class="value-card">
        <div block-corners-top=""></div>
        <div class="value-title">
          <span style="color: #00ffa3;">01.</span> Extreme Autonomy
        </div>
        <div class="value-desc">
          We hire self-directed problem solvers who thrive on high trust. You own features from architectural specification to deployment on mainnet with zero micro-management.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Value 2 -->
      <div class="value-card">
        <div block-corners-top=""></div>
        <div class="value-title">
          <span style="color: #28efce;">02.</span> Decentralization First
        </div>
        <div class="value-desc">
          We build permissionless systems that run without centralized intermediaries. Our models and data execution graphs are open, verifiable, and resilient by design.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Value 3 -->
      <div class="value-card">
        <div block-corners-top=""></div>
        <div class="value-title">
          <span style="color: #6a59e5;">03.</span> Rigorous Mathematical Foundations
        </div>
        <div class="value-desc">
          Every predictive model, order-routing formula, and formal security verification circuit undergoes rigorous stress-testing against historic adversarial conditions.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Value 4 -->
      <div class="value-card">
        <div block-corners-top=""></div>
        <div class="value-title">
          <span style="color: #00ffa3;">04.</span> Radical Candor &amp; Async Speed
        </div>
        <div class="value-desc">
          We default to transparent written RFCs and documentation. Honest, constructive technical debate is celebrated; ego and office politics are never tolerated.
        </div>
        <div block-corners-bottom=""></div>
      </div>
    </div>
  </section>

  <!-- Open Roles Section -->
  <section id="open-roles" class="content-section" style="border-top: 1px solid rgba(255, 255, 255, 0.06); padding-top: 80px;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 30px;">
      <div class="section-title-bordered">OPEN OPPORTUNITIES</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        Join Our Distributed Engineering &amp; Research Clusters
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        All positions are 100% remote with competitive base salaries in USD/USDC and significant CGPT token equity.
      </p>
    </div>

    <div class="roles-list">
      <!-- Role 1 -->
      <div class="role-card">
        <div block-corners-top=""></div>
        <div>
          <div class="role-dept">Core Engineering</div>
          <div class="role-title">Senior Distributed Systems Engineer (Rust / Go)</div>
          <div class="role-meta">
            <span class="role-tag">🌍 Remote (Global)</span>
            <span class="role-tag">⚡ Full-Time</span>
            <span class="role-tag">💰 $180k - $240k + CGPT</span>
          </div>
        </div>
        <div>
          <a class="btn-primary w-inline-block" href="contact-us.html?role=distributed-systems" scramble-link="">
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
          <div class="role-dept">AI &amp; Machine Learning</div>
          <div class="role-title">Quantitative Machine Learning Researcher (PyTorch / RL)</div>
          <div class="role-meta">
            <span class="role-tag">🌍 Remote (Global)</span>
            <span class="role-tag">⚡ Full-Time</span>
            <span class="role-tag">💰 $190k - $260k + CGPT</span>
          </div>
        </div>
        <div>
          <a class="btn-primary w-inline-block" href="contact-us.html?role=ml-researcher" scramble-link="">
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
          <div class="role-dept">Security &amp; Formal Verification</div>
          <div class="role-title">Lead Smart Contract Security Auditor (Solidity / Vyper)</div>
          <div class="role-meta">
            <span class="role-tag">🌍 Remote (Global)</span>
            <span class="role-tag">⚡ Full-Time</span>
            <span class="role-tag">💰 $175k - $230k + CGPT</span>
          </div>
        </div>
        <div>
          <a class="btn-primary w-inline-block" href="contact-us.html?role=security-auditor" scramble-link="">
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
          <div class="role-dept">Frontend &amp; User Experience</div>
          <div class="role-title">Staff Web3 Frontend Engineer (React / TypeScript / WebGL)</div>
          <div class="role-meta">
            <span class="role-tag">🌍 Remote (Global)</span>
            <span class="role-tag">⚡ Full-Time</span>
            <span class="role-tag">💰 $160k - $210k + CGPT</span>
          </div>
        </div>
        <div>
          <a class="btn-primary w-inline-block" href="contact-us.html?role=frontend-engineer" scramble-link="">
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
          <div class="role-dept">Autonomous AI Systems</div>
          <div class="role-title">Autonomous Agent Infrastructure Architect (Python / Rust)</div>
          <div class="role-meta">
            <span class="role-tag">🌍 Remote (Global)</span>
            <span class="role-tag">⚡ Full-Time</span>
            <span class="role-tag">💰 $185k - $250k + CGPT</span>
          </div>
        </div>
        <div>
          <a class="btn-primary w-inline-block" href="contact-us.html?role=agent-architect" scramble-link="">
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
        <div class="step-name">Application &amp; Async Review</div>
        <div class="step-desc">
          We review your GitHub, past protocols, or research papers. No generic recruiter screenings.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Step 2 -->
      <div class="pipeline-step">
        <div block-corners-top=""></div>
        <div class="step-badge">STAGE 02 // 60 MINS</div>
        <div class="step-name">Technical Architecture Deep-Dive</div>
        <div class="step-desc">
          A peer-to-peer technical conversation with a senior engineer or research scientist on our team.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Step 3 -->
      <div class="pipeline-step">
        <div block-corners-top=""></div>
        <div class="step-badge">STAGE 03 // 3-5 DAYS</div>
        <div class="step-name">Paid Practical Assessment</div>
        <div class="step-desc">
          A real-world task mirroring our daily challenges. We compensate you fairly for your time ($1,000 stipend).
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Step 4 -->
      <div class="pipeline-step">
        <div block-corners-top=""></div>
        <div class="step-badge">STAGE 04 // 24 HOURS</div>
        <div class="step-name">Executive Offer &amp; Token Grant</div>
        <div class="step-desc">
          Clear compensation terms, upfront token vesting schedule, and official onboarding plan.
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
        Engineered for Peak Performance &amp; Flexibility
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        Everything you need to do the best work of your career from anywhere in the world.
      </p>
    </div>

    <div class="perks-grid">
      <div class="perk-card">
        <div block-corners-top=""></div>
        <div class="perk-title">🌍 100% Remote Freedom</div>
        <div class="perk-desc">Work from anywhere across the globe. We coordinate asynchronously across all time zones.</div>
        <div block-corners-bottom=""></div>
      </div>
      <div class="perk-card">
        <div block-corners-top=""></div>
        <div class="perk-title">💰 Base + CGPT Token Grants</div>
        <div class="perk-desc">Competitive USD/USDC salary paired with liquid token grants aligned with network growth.</div>
        <div block-corners-bottom=""></div>
      </div>
      <div class="perk-card">
        <div block-corners-top=""></div>
        <div class="perk-title">🏝️ Annual Global Offsites</div>
        <div class="perk-desc">Gather twice a year in destinations like Lisbon, Tokyo, and Dubai for strategy, hacking, and fun.</div>
        <div block-corners-bottom=""></div>
      </div>
      <div class="perk-card">
        <div block-corners-top=""></div>
        <div class="perk-title">💻 $4,000 Home Lab Stipend</div>
        <div class="perk-desc">Top-of-the-line Apple silicon, GPU cloud compute credits, and custom ergonomic workspace setup.</div>
        <div block-corners-bottom=""></div>
      </div>
      <div class="perk-card">
        <div block-corners-top=""></div>
        <div class="perk-title">📚 Unlimited Learning Budget</div>
        <div class="perk-desc">Company-sponsored attendance for ETHDenver, Devcon, NeurIPS, and books/courses.</div>
        <div block-corners-bottom=""></div>
      </div>
      <div class="perk-card">
        <div block-corners-top=""></div>
        <div class="perk-title">🏥 Premium Health Coverage</div>
        <div class="perk-desc">Comprehensive medical, dental, and vision insurance for you and your dependents globally.</div>
        <div block-corners-bottom=""></div>
      </div>
    </div>
  </section>

  <!-- FAQ Section (Webflow .faq-2 Accordion) -->
  <section class="content-section" style="border-top: 1px solid rgba(255, 255, 255, 0.06); padding-top: 80px;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 30px;">
      <div class="section-title-bordered">FREQUENTLY ASKED QUESTIONS</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        Careers &amp; Onboarding FAQ
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        Answers regarding remote arrangements, compensation structures, and token vesting.
      </p>
    </div>

    <div class="faq-list">
      <!-- Item 1 -->
      <div class="faq-2 open">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">Can I work from any country in the world?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Yes. CoinGPT operates as a borderless decentralized protocol. We hire engineers and researchers regardless of geographic location via international contractor agreements or local Employer of Record (EOR) entities.
        </div>
      </div>

      <!-- Item 2 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">How does the CGPT token compensation work?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Token grants are offered alongside base pay. They follow an industry-standard 4-year vesting schedule with a 1-year cliff, giving every team member direct equity in the protocol's long-term utility and adoption.
        </div>
      </div>

      <!-- Item 3 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">What is your policy on open-source contributions and publications?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          We strongly encourage open-source contributions and academic publishing. Our research team regularly presents at top AI and cryptography symposiums, and we contribute to key Ethereum/Solana tooling.
        </div>
      </div>

      <!-- Item 4 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">What if I don't see a role that matches my exact background?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          We always make room for exceptional talent. If you are an exceptional machine learning engineer, zero-knowledge cryptographer, or quantitative researcher, reach out via our contact page with your portfolio.
        </div>
      </div>
    </div>
  </section>

  <!-- Bottom CTA Banner -->
  <div class="cta-banner-wrapper">
    <div class="cta-banner">
      <div block-corners-top=""></div>
      <div class="cta-banner-glow"></div>
      <div style="position: relative; z-index: 1; max-width: 650px;">
        <div class="section-title-bordered" style="margin-bottom: 12px;">READY TO SHAPE WEB3?</div>
        <h3 style="font-size: clamp(24px, 3vw, 36px); font-weight: 800; color: #ffffff; margin: 0 0 12px;">
          Deploy Your Career at the Cutting Edge of AI &amp; Crypto
        </h3>
        <p style="color: #9ca3af; font-size: 15px; margin: 0; line-height: 1.6;">
          Join our decentralized team and build systems that protect and empower millions of Web3 transactions every day.
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
      
      // Close all faqs
      document.querySelectorAll('.faq-2').forEach(f => f.classList.remove('open'));
      
      // If was not open, open this one
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

print("Successfully generated Webflow native careers.html")
