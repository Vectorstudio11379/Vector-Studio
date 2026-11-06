# Generator for Webflow Native about.html

with open('template_header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

with open('template_footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

PAGE_HTML = f"""<!DOCTYPE html>
<html data-wf-domain="www.coingpt.tech" data-wf-page="6488c93b137bd37e5762ce46" data-wf-site="64354b8ce4872ad8cd1c7b04" lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>About Us — CoinGPT | Architecting Autonomous Web3 Intelligence</title>
  <meta name="description" content="CoinGPT is the decentralized AI infrastructure network powering autonomous DeFi trading, smart contract security audits, and institutional on-chain intelligence."/>
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
      width: 750px;
      height: 450px;
      background: radial-gradient(circle, rgba(0, 255, 163, 0.15) 0%, rgba(40, 239, 206, 0.08) 45%, transparent 70%);
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
      background: linear-gradient(135deg, #00ffa3 0%, #28efce 50%, #6a59e5 100%);
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
      padding: 22px 20px;
      border-radius: 4px;
      position: relative;
      transition: all 0.3s ease;
    }}
    .stat-holo-card:hover {{
      border-color: rgba(0, 255, 163, 0.4);
      transform: translateY(-2px);
      box-shadow: 0 10px 25px -5px rgba(0, 255, 163, 0.1);
    }}
    .stat-number {{
      font-size: 32px;
      font-weight: 800;
      font-family: 'Roboto Mono', monospace;
      color: #00ffa3;
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
      border-color: rgba(40, 239, 206, 0.4);
      background: rgba(22, 25, 38, 0.85);
      transform: translateY(-3px);
    }}
    .pillar-icon {{
      width: 48px;
      height: 48px;
      border-radius: 8px;
      background: rgba(0, 255, 163, 0.1);
      border: 1px solid rgba(0, 255, 163, 0.25);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 20px;
      color: #00ffa3;
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
      border-color: rgba(106, 89, 229, 0.45);
      transform: translateY(-3px);
    }}
    .team-avatar {{
      width: 80px;
      height: 80px;
      border-radius: 50%;
      margin: 0 auto 18px;
      background: linear-gradient(135deg, rgba(0, 255, 163, 0.2), rgba(106, 89, 229, 0.3));
      border: 2px solid rgba(0, 255, 163, 0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 28px;
      color: #00ffa3;
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
      color: #28efce;
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

  <!-- About Hero -->
  <section class="about-hero-container">
    <div class="hero-glow-bg"></div>
    <div class="hero-grid-2col">
      <div>
        <div class="section-title-bordered">ABOUT COINGPT</div>
        <h1 class="hero-title-h1">Architecting Autonomous <span class="gradient-text">Web3 Intelligence</span></h1>
        <p class="hero-desc-p">
          CoinGPT unites decentralized neural networks, on-chain execution primitives, and high-frequency predictive models to empower 850,000+ traders, institutional quants, and smart contract developers across 28+ blockchains.
        </p>
        <div style="display: flex; gap: 16px; flex-wrap: wrap;">
          <a class="btn-primary w-inline-block" href="pricing.html" scramble-link="">
            <div class="btn-primary-lines btn-primary-lines-1">
              <div class="btn-primary-lines btn-primary-lines-2">
                <div class="btn-primary-text" scramble-text="">Explore Solutions</div>
              </div>
            </div>
          </a>
          <a class="btn-secondary w-inline-block" href="contact-us.html" style="padding: 12px 24px; border: 1px solid rgba(255,255,255,0.15); border-radius: 2px; color: #ffffff; text-decoration: none; font-weight: 600; font-size: 14px; display: inline-flex; align-items: center; transition: all 0.2s;">
            Contact Research Team
          </a>
        </div>
      </div>

      <!-- Holographic Stats Grid -->
      <div class="hero-stats-grid">
        <div class="stat-holo-card">
          <div block-corners-top=""></div>
          <div class="stat-number">$4.8B+</div>
          <div class="stat-label">Volume Analyzed</div>
          <div block-corners-bottom=""></div>
        </div>
        <div class="stat-holo-card">
          <div block-corners-top=""></div>
          <div class="stat-number">120M+</div>
          <div class="stat-label">On-Chain Signals</div>
          <div block-corners-bottom=""></div>
        </div>
        <div class="stat-holo-card">
          <div block-corners-top=""></div>
          <div class="stat-number">850K+</div>
          <div class="stat-label">Community Members</div>
          <div block-corners-bottom=""></div>
        </div>
        <div class="stat-holo-card">
          <div block-corners-top=""></div>
          <div class="stat-number">99.98%</div>
          <div class="stat-label">High-Availability Uptime</div>
          <div block-corners-bottom=""></div>
        </div>
      </div>
    </div>
  </section>

  <!-- Core Mission Pillars Bento -->
  <section class="content-section">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 30px;">
      <div class="section-title-bordered">CORE PILLARS / ARCHITECTURE</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        Engineering the Cognitive Layer of Decentralized Finance
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        Our decentralized infrastructure bridges real-time on-chain telemetry with custom fine-tuned transformer models.
      </p>
    </div>

    <div class="pillars-grid">
      <!-- Pillar 1 -->
      <div class="pillar-card">
        <div block-corners-top=""></div>
        <div class="pillar-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg>
        </div>
        <div class="pillar-title">Autonomous DeFi Trading Models</div>
        <div class="pillar-desc">
          Zero-latency multi-DEX order execution, predictive liquidity flows, real-time slippage mitigation, and microsecond arbitrage across Ethereum, Solana, Arbitrum, and BNB Chain.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Pillar 2 -->
      <div class="pillar-card">
        <div block-corners-top=""></div>
        <div class="pillar-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>
        </div>
        <div class="pillar-title">Smart Contract AI Security Audits</div>
        <div class="pillar-desc">
          Automated formal verification neural networks scanning Solidity, Rust, and Vyper codebases in seconds. Detect reentrancy, price manipulation, and access-control vulnerabilities prior to deployment.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Pillar 3 -->
      <div class="pillar-card">
        <div block-corners-top=""></div>
        <div class="pillar-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 7h10"/><path d="M7 12h10"/><path d="M7 17h10"/></svg>
        </div>
        <div class="pillar-title">High-Throughput Web3 Copilot</div>
        <div class="pillar-desc">
          Semantic natural language queries for on-chain analytics, automated yield routing, wallet risk diagnostics, and smart contract transaction generation via unified chat.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Pillar 4 -->
      <div class="pillar-card">
        <div block-corners-top=""></div>
        <div class="pillar-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>
        </div>
        <div class="pillar-title">Decentralized Node Network</div>
        <div class="pillar-desc">
          Globally distributed validator and compute clusters executing private, localized LLM inference. Verifiable cryptographically with zero centralized dependencies or single points of failure.
        </div>
        <div block-corners-bottom=""></div>
      </div>
    </div>
  </section>

  <!-- Leadership / Research Team Grid -->
  <section class="content-section" style="border-top: 1px solid rgba(255, 255, 255, 0.06); padding-top: 80px;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 30px;">
      <div class="section-title-bordered">LEADERSHIP / RESEARCH TEAM</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        Led by World-Class AI Scientists &amp; Blockchain Engineers
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        Our team combines decades of deep learning research at top institutions with battle-tested decentralized security expertise.
      </p>
    </div>

    <div class="team-grid">
      <!-- Member 1 -->
      <div class="team-card">
        <div block-corners-top=""></div>
        <div class="team-avatar">AM</div>
        <div class="team-name">Dr. Alex Mercer</div>
        <div class="team-role">Founder &amp; CEO</div>
        <div class="team-bio">
          Former DeepMind research scientist. Quantitative Cryptography PhD from MIT. Pioneered predictive order flow execution in decentralized automated market makers.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Member 2 -->
      <div class="team-card">
        <div block-corners-top=""></div>
        <div class="team-avatar">EV</div>
        <div class="team-name">Dr. Elena Vance</div>
        <div class="team-role">Chief AI Scientist</div>
        <div class="team-bio">
          Machine Learning Research Fellow at Stanford. Author of 18+ papers on transformer-based time-series forecasting and real-time on-chain reinforcement learning.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Member 3 -->
      <div class="team-card">
        <div block-corners-top=""></div>
        <div class="team-avatar">MS</div>
        <div class="team-name">Marcus Sterling</div>
        <div class="team-role">Head of Smart Contract Security</div>
        <div class="team-bio">
          Former Lead Auditor at ConsenSys Diligence. Audited 450+ production protocols securing over $12B in Total Value Locked without a single exploit.
        </div>
        <div block-corners-bottom=""></div>
      </div>

      <!-- Member 4 -->
      <div class="team-card">
        <div block-corners-top=""></div>
        <div class="team-avatar">SC</div>
        <div class="team-name">Sofia Chen</div>
        <div class="team-role">Head of Product &amp; Compute</div>
        <div class="team-bio">
          Former Lead Infrastructure Architect at Polygon. Scaled distributed RPC and validator node telemetry processing 1.4B daily transactions.
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
        Everything You Need to Know About CoinGPT
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        Transparent answers regarding our decentralized model architecture, safety audits, and network governance.
      </p>
    </div>

    <div class="faq-list">
      <!-- Item 1 -->
      <div class="faq-2 open">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">How is CoinGPT different from centralized AI language models?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          CoinGPT models are explicitly fine-tuned on real-time mempool telemetry, smart contract bytecode, and multi-chain liquidity graph dynamics. Centralized models lack live on-chain execution capabilities and are limited by stale cutoff dates, whereas CoinGPT continuously ingests block-by-block data.
        </div>
      </div>

      <!-- Item 2 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">What blockchains and Layer 2 networks does CoinGPT support?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          CoinGPT supports all major EVM networks (Ethereum, Arbitrum, Optimism, Base, Polygon, Avalanche, BNB Chain), non-EVM ecosystems including Solana and Sui, and Bitcoin Layer 2 networks through unified RPC adapters.
        </div>
      </div>

      <!-- Item 3 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">How does the Smart Contract AI Audit ensure zero false negatives?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Our audit pipeline combines formal mathematical verification with deep reinforcement learning trained on a corpus of 14,000+ past exploit post-mortems and vulnerable AST patterns, providing multi-layered risk verification with proof certificates.
        </div>
      </div>

      <!-- Item 4 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">Is CoinGPT open-source and decentralized?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Yes. Core developer SDKs, verification circuits, and on-chain oracle contracts are open-source. Model inference runs across our decentralized validator node network where participants stake CGPT tokens to verify computational integrity.
        </div>
      </div>

      <!-- Item 5 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">How do developers integrate CoinGPT models into decentralized apps?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Developers can integrate via our TypeScript/Python SDKs, standard REST/WebSocket endpoints, or decentralized oracle requests directly inside Solidity smart contracts with instant response times.
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
        <div class="section-title-bordered" style="margin-bottom: 12px;">JOIN THE NETWORK</div>
        <h3 style="font-size: clamp(24px, 3vw, 36px); font-weight: 800; color: #ffffff; margin: 0 0 12px;">
          Build the Future of Autonomous Finance with CoinGPT
        </h3>
        <p style="color: #9ca3af; font-size: 15px; margin: 0; line-height: 1.6;">
          Deploy intelligent DeFi agents, access high-frequency on-chain signals, and protect your protocol with automated formal audits today.
        </p>
      </div>

      <div style="position: relative; z-index: 1; display: flex; gap: 16px; flex-wrap: wrap;">
        <a class="btn-primary w-inline-block" href="pricing.html" scramble-link="">
          <div class="btn-primary-lines btn-primary-lines-1">
            <div class="btn-primary-lines btn-primary-lines-2">
              <div class="btn-primary-text" scramble-text="">Launch App</div>
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

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(PAGE_HTML)

print("Successfully generated Webflow native about.html")
