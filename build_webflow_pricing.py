# Generator for Webflow Native pricing.html

with open('template_header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

with open('template_footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

PAGE_HTML = f"""<!DOCTYPE html>
<html data-wf-domain="www.coingpt.tech" data-wf-page="6488c93b137bd37e5762ce45" data-wf-site="64354b8ce4872ad8cd1c7b04" lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Pricing &amp; Plans — CoinGPT | Decentralized Web3 AI Infrastructure</title>
  <meta name="description" content="Transparent, predictable pricing for CoinGPT decentralized AI models, real-time trading signals, smart contract audits, and institutional Web3 developer APIs."/>
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
    /* Hero layout */
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
      background: rgba(0, 255, 163, 0.12);
      border: 1px solid rgba(0, 255, 163, 0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #00ffa3;
      flex-shrink: 0;
    }}
    /* Billing toggle */
    .billing-toggle-wrap {{
      display: inline-flex;
      align-items: center;
      gap: 16px;
      background: rgba(22, 25, 36, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 6px 10px;
      border-radius: 50px;
      margin-top: 10px;
    }}
    .billing-opt-btn {{
      padding: 8px 18px;
      border-radius: 40px;
      font-family: 'Roboto Mono', monospace;
      font-size: 13px;
      font-weight: 500;
      color: #9ca3af;
      cursor: pointer;
      border: none;
      background: transparent;
      transition: all 0.2s ease;
    }}
    .billing-opt-btn.active {{
      background: #00ffa3;
      color: #0b0c10;
      font-weight: 700;
      box-shadow: 0 0 16px rgba(0, 255, 163, 0.35);
    }}
    .discount-pill {{
      font-size: 11px;
      font-weight: 700;
      color: #00ffa3;
      background: rgba(0, 255, 163, 0.15);
      border: 1px solid rgba(0, 255, 163, 0.3);
      padding: 2px 8px;
      border-radius: 999px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    /* Hero Visual Card */
    .hero-visual-card {{
      background: rgba(18, 20, 28, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 20px;
      padding: 32px;
      backdrop-filter: blur(20px);
      box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7);
      position: relative;
    }}
    .card-header-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 18px;
      margin-bottom: 24px;
    }}
    .terminal-dots {{
      display: flex;
      gap: 7px;
    }}
    .terminal-dot {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
    }}
    .terminal-dot.dot-red {{ background: #ef4444; }}
    .terminal-dot.dot-yellow {{ background: #f59e0b; }}
    .terminal-dot.dot-green {{ background: #10b981; }}
    .terminal-status {{
      font-family: 'Roboto Mono', monospace;
      font-size: 12px;
      color: #00ffa3;
    }}
    /* Cut-corner divider wrapper */
    .cut-corner-container {{
      max-width: 1400px;
      margin: 40px auto;
      padding: 0 2rem;
      position: relative;
    }}
    .divider-line {{
      height: 1px;
      background: linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.12) 20%, rgba(0,255,163,0.3) 50%, rgba(255,255,255,0.12) 80%, transparent 100%);
    }}
    /* Pricing Tier Cards Grid */
    .plans-grid {{
      max-width: 1400px;
      margin: 40px auto 90px;
      padding: 0 2rem;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
      position: relative;
      z-index: 1;
    }}
    @media (max-width: 991px) {{
      .plans-grid {{ grid-template-columns: 1fr; max-width: 550px; }}
    }}
    .pricing-card {{
      background: rgba(18, 20, 29, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 20px;
      padding: 40px 32px;
      backdrop-filter: blur(24px);
      transition: all 0.3s ease;
      display: flex;
      flex-direction: column;
      position: relative;
    }}
    .pricing-card:hover {{
      border-color: rgba(0, 255, 163, 0.4);
      transform: translateY(-5px);
      box-shadow: 0 15px 35px -10px rgba(0, 255, 163, 0.15);
    }}
    .pricing-card.featured {{
      border-color: rgba(0, 255, 163, 0.5);
      background: linear-gradient(180deg, rgba(20, 30, 35, 0.85) 0%, rgba(14, 18, 26, 0.95) 100%);
      box-shadow: 0 20px 40px -15px rgba(0, 255, 163, 0.2);
    }}
    .pricing-tier-badge {{
      display: inline-block;
      font-family: 'Roboto Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #00ffa3;
      background: rgba(0, 255, 163, 0.1);
      border: 1px solid rgba(0, 255, 163, 0.3);
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 20px;
      align-self: flex-start;
    }}
    .pricing-title {{
      font-size: 24px;
      font-weight: 700;
      color: #ffffff;
      margin: 0 0 8px;
    }}
    .pricing-subtitle {{
      font-size: 14px;
      color: #9ca3af;
      line-height: 1.5;
      min-height: 42px;
      margin-bottom: 24px;
    }}
    .pricing-price-wrap {{
      display: flex;
      align-items: baseline;
      gap: 6px;
      margin-bottom: 28px;
    }}
    .price-num {{
      font-size: 48px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: -0.03em;
    }}
    .price-period {{
      font-size: 15px;
      color: #9ca3af;
    }}
    .pricing-features-list {{
      list-style: none;
      padding: 0;
      margin: 0 0 36px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      flex-grow: 1;
    }}
    .pricing-feature-item {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      font-size: 14px;
      color: #d1d5db;
      line-height: 1.5;
    }}
    .pricing-check {{
      color: #00ffa3;
      flex-shrink: 0;
      margin-top: 2px;
    }}
    /* FAQ Section */
    .faq-section {{
      max-width: 1000px;
      margin: 40px auto 100px;
      padding: 0 2rem;
    }}
    .faq-title-wrap {{
      text-align: center;
      margin-bottom: 48px;
    }}
    .faq-item {{
      background: rgba(18, 20, 29, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      margin-bottom: 16px;
      overflow: hidden;
      transition: border-color 0.2s ease;
    }}
    .faq-item:hover {{
      border-color: rgba(0, 255, 163, 0.3);
    }}
    .faq-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 22px 28px;
      cursor: pointer;
      font-size: 17px;
      font-weight: 600;
      color: #ffffff;
    }}
    .faq-toggle-icon {{
      width: 24px;
      height: 24px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #00ffa3;
      transition: transform 0.25s ease;
      font-size: 20px;
    }}
    .faq-item.is-open .faq-toggle-icon {{
      transform: rotate(45deg);
    }}
    .faq-body {{
      display: none;
      padding: 0 28px 24px;
      font-size: 15px;
      color: #9ca3af;
      line-height: 1.6;
    }}
    .faq-item.is-open .faq-body {{
      display: block;
    }}
    /* Bottom CTA banner */
    .bottom-cta-section {{
      max-width: 1400px;
      margin: 0 auto 80px;
      padding: 0 2rem;
    }}
    .bottom-cta-card {{
      background: linear-gradient(135deg, rgba(16, 36, 44, 0.8) 0%, rgba(20, 24, 38, 0.9) 100%);
      border: 1px solid rgba(0, 255, 163, 0.3);
      border-radius: 24px;
      padding: 60px 40px;
      text-align: center;
      position: relative;
      overflow: hidden;
    }}
  </style>
</head>
<body class="landing-body">

  <!-- Universal Header -->
  {header_html}

  <!-- Main Content -->
  <main>
    <!-- Hero Section -->
    <section class="pricing-hero-container">
      <div class="hero-glow-bg"></div>
      <div class="hero-grid-2col">
        <div>
          <div class="section-title-bordered section-title-bordered--gradient">
            <div class="section-title-bordered-line-1"></div>
            <div class="section-title-bordered-line-2"></div>
            <div class="section-title-bordered-text">PRICING &amp; SUBSCRIPTION TIERS</div>
          </div>
          <h1 class="hero-title-h1">Transparent On-Chain <br/><span class="gradient-text">Pricing &amp; API Plans</span></h1>
          <p class="hero-desc-p">Predictable, high-throughput access to CoinGPT's decentralized AI models, real-time trading signals, smart contract security audits, and institutional SDKs.</p>
          
          <div class="hero-bullets">
            <div class="hero-bullet-item">
              <div class="hero-bullet-icon"><svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>
              <span>Zero-lock-in pay-as-you-go crypto payment or credit card billing</span>
            </div>
            <div class="hero-bullet-item">
              <div class="hero-bullet-icon"><svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>
              <span>Sub-second inference via decentralized GPU cluster routing</span>
            </div>
            <div class="hero-bullet-item">
              <div class="hero-bullet-icon"><svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>
              <span>Dedicated smart contract security auditor with formal verification</span>
            </div>
          </div>

          <div class="billing-toggle-wrap">
            <button class="billing-opt-btn active" id="btn-monthly" type="button">Monthly Billing</button>
            <button class="billing-opt-btn" id="btn-annual" type="button">Annual Billing</button>
            <span class="discount-pill">Save 20%</span>
          </div>
        </div>

        <!-- Hero Visual Terminal Card -->
        <div class="hero-visual-card">
          <div class="card-header-bar">
            <div class="terminal-dots">
              <div class="terminal-dot dot-red"></div>
              <div class="terminal-dot dot-yellow"></div>
              <div class="terminal-dot dot-green"></div>
            </div>
            <div class="terminal-status">● LIVE API INFRASTRUCTURE</div>
          </div>
          <div style="font-family:'Roboto Mono', monospace; font-size:13px; line-height:1.7; color:#9ca3af;">
            <div style="color:#00ffa3; margin-bottom:12px;">$ coingpt-sdk --status --metrics</div>
            <div>[NODE-CLUSTER] Global latency: <span style="color:#ffffff;">42ms</span></div>
            <div>[AI-ENGINE] Models online: <span style="color:#ffffff;">Trading-V3, Auditor-Pro, Chat-Web3</span></div>
            <div>[VERIFICATION] EVM bytecode analyzer: <span style="color:#ffffff;">Operational</span></div>
            <div>[ON-CHAIN] Real-time indexed pairs: <span style="color:#ffffff;">18,400+</span></div>
            <div style="margin-top:16px; padding:12px; background:rgba(0,255,163,0.06); border-radius:8px; border:1px solid rgba(0,255,163,0.2); color:#28efce;">
              &gt; Ready for deployment. Select your plan below to generate dedicated API keys.
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Cut-Corner Divider -->
    <div class="cut-corner-container" block-corners-top="" block-corners-bottom="">
      <div class="divider-line"></div>
    </div>

    <!-- 3 Pricing Cards -->
    <section class="plans-grid">
      <!-- Tier 1: Free Community -->
      <div class="pricing-card">
        <div class="pricing-tier-badge">Community Tier</div>
        <h3 class="pricing-title">Free Access</h3>
        <p class="pricing-subtitle">Perfect for retail crypto traders, Web3 enthusiasts, and individual developers testing our AI tools.</p>
        <div class="pricing-price-wrap">
          <span class="price-num">$0</span>
          <span class="price-period">/ month</span>
        </div>
        <ul class="pricing-features-list">
          <li class="pricing-feature-item">
            <svg class="pricing-check" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
            <span>50 AI Trading &amp; Market queries per day</span>
          </li>
          <li class="pricing-feature-item">
            <svg class="pricing-check" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Standard Web3 Chatbot web access</span>
          </li>
          <li class="pricing-feature-item">
            <svg class="pricing-check" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
            <span>3 Smart Contract Audits / month (Solidity)</span>
          </li>
          <li class="pricing-feature-item">
            <svg class="pricing-check" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Community Discord &amp; Telegram support</span>
          </li>
        </ul>
        <a class="btn-primary w-inline-block" href="ai-trading-assistant.html" scramble-link="" style="text-align:center;display:flex;justify-content:center;text-decoration:none;">
          <div class="btn-primary-lines btn-primary-lines-1" style="width:100%;">
            <div class="btn-primary-lines btn-primary-lines-2" style="width:100%;">
              <div class="btn-primary-text" scramble-text="">Start Free</div>
            </div>
          </div>
        </a>
      </div>

      <!-- Tier 2: Pro Trader (Featured) -->
      <div class="pricing-card featured">
        <div class="pricing-tier-badge" style="background:#00ffa3; color:#0b0c10;">Most Popular</div>
        <h3 class="pricing-title">Pro Trader</h3>
        <p class="pricing-subtitle">Full algorithmic market intelligence, real-time trigger alerts, and high-precision audit models.</p>
        <div class="pricing-price-wrap">
          <span class="price-num" id="pro-price">$49</span>
          <span class="price-period" id="pro-period">/ month</span>
        </div>
        <ul class="pricing-features-list">
          <li class="pricing-feature-item">
            <svg class="pricing-check" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
            <span><strong>Unlimited</strong> AI Trading Assistant queries</span>
          </li>
          <li class="pricing-feature-item">
            <svg class="pricing-check" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Real-time technical alerts via Telegram / Discord</span>
          </li>
          <li class="pricing-feature-item">
            <svg class="pricing-check" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Unlimited Smart Contract Audits &amp; Generator</span>
          </li>
          <li class="pricing-feature-item">
            <svg class="pricing-check" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Early access to newly trained on-chain LLMs</span>
          </li>
          <li class="pricing-feature-item">
            <svg class="pricing-check" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Priority GPU compute queue (sub-second response)</span>
          </li>
        </ul>
        <a class="btn-primary w-inline-block" href="contact-us.html" scramble-link="" style="text-align:center;display:flex;justify-content:center;text-decoration:none;">
          <div class="btn-primary-lines btn-primary-lines-1" style="width:100%;">
            <div class="btn-primary-lines btn-primary-lines-2" style="width:100%;">
              <div class="btn-primary-text" scramble-text="">Get Pro Access</div>
            </div>
          </div>
        </a>
      </div>

      <!-- Tier 3: Enterprise & Developer API -->
      <div class="pricing-card">
        <div class="pricing-tier-badge">Institutional / B2B</div>
        <h3 class="pricing-title">Enterprise API</h3>
        <p class="pricing-subtitle">Dedicated GPU infrastructure, custom fine-tuned weights, SLA guarantees, and high-rate REST/WebSocket APIs.</p>
        <div class="pricing-price-wrap">
          <span class="price-num" id="ent-price">$299</span>
          <span class="price-period" id="ent-period">/ month</span>
        </div>
        <ul class="pricing-features-list">
          <li class="pricing-feature-item">
            <svg class="pricing-check" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
            <span>1,000,000 API calls / month (custom rate limits)</span>
          </li>
          <li class="pricing-feature-item">
            <svg class="pricing-check" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
            <span>White-label Telegram &amp; Web chatbot integration</span>
          </li>
          <li class="pricing-feature-item">
            <svg class="pricing-check" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Custom LLM fine-tuning on protocol documentation</span>
          </li>
          <li class="pricing-feature-item">
            <svg class="pricing-check" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
            <span>99.99% Uptime Service Level Agreement (SLA)</span>
          </li>
          <li class="pricing-feature-item">
            <svg class="pricing-check" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
            <span>Dedicated Telegram engineering support channel</span>
          </li>
        </ul>
        <a class="btn-primary w-inline-block" href="contact-us.html" scramble-link="" style="text-align:center;display:flex;justify-content:center;text-decoration:none;">
          <div class="btn-primary-lines btn-primary-lines-1" style="width:100%;">
            <div class="btn-primary-lines btn-primary-lines-2" style="width:100%;">
              <div class="btn-primary-text" scramble-text="">Contact Sales</div>
            </div>
          </div>
        </a>
      </div>
    </section>

    <!-- FAQ Accordion Section -->
    <section class="faq-section">
      <div class="faq-title-wrap">
        <div class="section-title-bordered section-title-bordered--gradient">
          <div class="section-title-bordered-line-1"></div>
          <div class="section-title-bordered-line-2"></div>
          <div class="section-title-bordered-text">FREQUENTLY ASKED QUESTIONS</div>
        </div>
        <h2 style="font-size:clamp(26px, 3.5vw, 36px); font-weight:800; color:#ffffff; margin-top:16px;">Everything You Need To Know</h2>
      </div>

      <div class="faq-list">
        <div class="faq-item faq-2 miscellaneous-2 is-open">
          <div class="faq-header">
            <span>Can I pay for my subscription in cryptocurrency?</span>
            <div class="faq-toggle-icon">+</div>
          </div>
          <div class="faq-body">
            Yes! You can pay using major crypto assets (USDT, USDC, ETH, BNB) directly via on-chain smart contracts or Web3 wallet connection, as well as standard credit card / fiat methods.
          </div>
        </div>

        <div class="faq-item faq-2 miscellaneous-2">
          <div class="faq-header">
            <span>What happens if my project exceeds the monthly API limits?</span>
            <div class="faq-toggle-icon">+</div>
          </div>
          <div class="faq-body">
            Your API key will remain active without service interruption. Additional queries are billed at our standard pay-as-you-go micro-rate of $0.0003 per inference call, or you can seamlessly upgrade to an Enterprise Tier.
          </div>
        </div>

        <div class="faq-item faq-2 miscellaneous-2">
          <div class="faq-header">
            <span>Can I integrate the CoinGPT Web3 Chatbot into my own dApp or Telegram community?</span>
            <div class="faq-toggle-icon">+</div>
          </div>
          <div class="faq-body">
            Yes, our B2B SDK and White-Label bot solutions allow you to deploy a customized, custom-branded AI chatbot into your Discord server, Telegram group, or website with just a few lines of code.
          </div>
        </div>

        <div class="faq-item faq-2 miscellaneous-2">
          <div class="faq-header">
            <span>How accurate is the Smart Contract Security Auditor?</span>
            <div class="faq-toggle-icon">+</div>
          </div>
          <div class="faq-body">
            Our Auditor models are trained on hundreds of thousands of audited smart contracts and known reentrancy, overflow, logic, and flash loan exploits. It performs both automated vulnerability scans and formal verification with line-by-line remediation steps.
          </div>
        </div>

        <div class="faq-item faq-2 miscellaneous-2">
          <div class="faq-header">
            <span>Can I cancel or change my plan at any time?</span>
            <div class="faq-toggle-icon">+</div>
          </div>
          <div class="faq-body">
            Absolutely. There are no long-term contracts. You can upgrade, downgrade, or cancel your subscription at any moment directly from your account dashboard.
          </div>
        </div>
      </div>
    </section>

    <!-- Bottom Conversion Banner -->
    <section class="bottom-cta-section">
      <div class="bottom-cta-card">
        <h2 style="font-size:clamp(28px, 4vw, 42px); font-weight:800; color:#ffffff; margin:0 0 16px;">Supercharge Your Web3 Operations With CoinGPT AI</h2>
        <p style="font-size:16px; color:#9ca3af; max-width:650px; margin:0 auto 32px; line-height:1.6;">Join thousands of traders, developers, and blockchain protocols utilizing decentralized intelligence for trading, development, and security.</p>
        <a class="btn-primary w-inline-block" href="contact-us.html" scramble-link="" style="text-decoration:none;">
          <div class="btn-primary-lines btn-primary-lines-1">
            <div class="btn-primary-lines btn-primary-lines-2">
              <div class="btn-primary-text" scramble-text="">Get Started Now</div>
            </div>
          </div>
        </a>
      </div>
    </section>
  </main>

  <!-- Universal Footer -->
  {footer_html}

  <script src="vector-nav.js"></script>
  <script>
    // FAQ Accordion Interactivity
    document.querySelectorAll('.faq-header').forEach(header => {{
      header.addEventListener('click', () => {{
        const item = header.parentElement;
        item.classList.toggle('is-open');
      }});
    }});

    // Annual / Monthly Pricing Toggle
    const btnMonthly = document.getElementById('btn-monthly');
    const btnAnnual = document.getElementById('btn-annual');
    const proPrice = document.getElementById('pro-price');
    const proPeriod = document.getElementById('pro-period');
    const entPrice = document.getElementById('ent-price');
    const entPeriod = document.getElementById('ent-period');

    if (btnMonthly && btnAnnual) {{
      btnMonthly.addEventListener('click', () => {{
        btnMonthly.classList.add('active');
        btnAnnual.classList.remove('active');
        proPrice.textContent = '$49';
        proPeriod.textContent = '/ month';
        entPrice.textContent = '$299';
        entPeriod.textContent = '/ month';
      }});
      btnAnnual.addEventListener('click', () => {{
        btnAnnual.classList.add('active');
        btnMonthly.classList.remove('active');
        proPrice.textContent = '$39';
        proPeriod.textContent = '/ mo (billed yearly)';
        entPrice.textContent = '$239';
        entPeriod.textContent = '/ mo (billed yearly)';
      }});
    }}
  </script>
</body>
</html>
"""

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(PAGE_HTML)

print("Successfully generated Webflow native pricing.html")
