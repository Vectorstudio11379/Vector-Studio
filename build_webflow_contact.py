# Generator for Webflow Native contact-us.html

with open('template_header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

with open('template_footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

PAGE_HTML = f"""<!DOCTYPE html>
<html data-wf-domain="www.coingpt.tech" data-wf-page="6488c93b137bd37e5762ce48" data-wf-site="64354b8ce4872ad8cd1c7b04" lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Contact Us — CoinGPT | Institutional Web3 AI Infrastructure &amp; Audits</title>
  <meta name="description" content="Get in touch with CoinGPT research and engineering teams for protocol security audits, institutional API access, custom model fine-tuning, and ecosystem partnerships."/>
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
    .contact-hero-container {{
      max-width: 1400px;
      margin: 0 auto;
      padding: 90px 2rem 40px;
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
      max-width: 760px;
      margin: 0 auto;
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
      padding: 50px 2rem 70px;
    }}

    /* 2 Column Layout */
    .contact-grid-2col {{
      display: grid;
      grid-template-columns: 1fr 1.15fr;
      gap: 40px;
      align-items: start;
    }}
    @media (max-width: 991px) {{
      .contact-grid-2col {{ grid-template-columns: 1fr; }}
    }}

    /* Left Column Info */
    .contact-channels {{
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .channel-card {{
      background: rgba(18, 20, 29, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 24px;
      position: relative;
      border-radius: 4px;
      transition: all 0.25s ease;
    }}
    .channel-card:hover {{
      border-color: rgba(0, 255, 163, 0.35);
      transform: translateY(-2px);
    }}
    .channel-label {{
      font-family: 'Roboto Mono', monospace;
      font-size: 12px;
      color: #00ffa3;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 6px;
    }}
    .channel-title {{
      font-size: 18px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 6px;
    }}
    .channel-link {{
      color: #28efce;
      font-size: 15px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: color 0.2s;
    }}
    .channel-link:hover {{
      color: #00ffa3;
      text-decoration: underline;
    }}
    .channel-desc {{
      font-size: 13.5px;
      color: #9ca3af;
      margin-top: 8px;
      line-height: 1.5;
    }}

    /* Right Column Form */
    .form-wrapper-card {{
      background: rgba(18, 20, 29, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 38px 34px;
      position: relative;
      border-radius: 4px;
    }}
    .form-group {{
      margin-bottom: 20px;
    }}
    .field-label {{
      display: block;
      font-size: 13px;
      font-weight: 600;
      color: #d1d5db;
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .form-input, .form-select, .form-textarea {{
      width: 100%;
      background: rgba(11, 12, 16, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 3px;
      padding: 12px 16px;
      font-size: 15px;
      color: #ffffff;
      font-family: inherit;
      outline: none;
      transition: border-color 0.2s, box-shadow 0.2s;
      box-sizing: border-box;
    }}
    .form-input:focus, .form-select:focus, .form-textarea:focus {{
      border-color: #00ffa3;
      box-shadow: 0 0 10px rgba(0, 255, 163, 0.2);
    }}
    .form-textarea {{
      min-height: 130px;
      resize: vertical;
    }}
    .form-row-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }}
    @media (max-width: 600px) {{
      .form-row-2 {{ grid-template-columns: 1fr; }}
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

  <!-- Contact Hero -->
  <section class="contact-hero-container" style="text-align: center;">
    <div class="hero-glow-bg"></div>
    <div class="section-title-bordered">COMMUNICATION MATRIX</div>
    <h1 class="hero-title-h1">Connect with the <span class="gradient-text">CoinGPT Team</span></h1>
    <p class="hero-desc-p">
      Accelerate your protocol with institutional-grade AI models, automated smart contract security audits, and dedicated developer support. Our engineering cluster responds within 24 hours.
    </p>
  </section>

  <!-- 2-Column Contact Section -->
  <section class="content-section">
    <div class="contact-grid-2col">
      
      <!-- Left Column: Official Channels -->
      <div class="contact-channels">
        <!-- Channel 1 -->
        <div class="channel-card">
          <div block-corners-top=""></div>
          <div class="channel-label">PARTNERSHIPS &amp; ECOSYSTEM</div>
          <div class="channel-title">Institutional Inquiries &amp; Grants</div>
          <a class="channel-link" href="mailto:partnerships@coingpt.tech">
            <span>✉️ partnerships@coingpt.tech</span>
          </a>
          <div class="channel-desc">
            Direct channel for Tier-1 DEX integrations, Layer-1/Layer-2 foundations, and institutional quant API volume agreements.
          </div>
          <div block-corners-bottom=""></div>
        </div>

        <!-- Channel 2 -->
        <div class="channel-card">
          <div block-corners-top=""></div>
          <div class="channel-label">SECURITY &amp; FORMAL VERIFICATION</div>
          <div class="channel-title">Protocol Audits &amp; Incident Triage</div>
          <a class="channel-link" href="mailto:security@coingpt.tech">
            <span>🛡️ security@coingpt.tech</span>
          </a>
          <div class="channel-desc">
            Emergency vulnerability disclosure, comprehensive smart contract auditing quotes, and zero-day threat analysis.
          </div>
          <div block-corners-bottom=""></div>
        </div>

        <!-- Channel 3 -->
        <div class="channel-card">
          <div block-corners-top=""></div>
          <div class="channel-label">PRESS &amp; COMMUNICATIONS</div>
          <div class="channel-title">Global Media &amp; Brand Assets</div>
          <a class="channel-link" href="mailto:press@coingpt.tech">
            <span>📰 press@coingpt.tech</span>
          </a>
          <div class="channel-desc">
            Keynote speaking inquiries, press releases, media kits, and executive interview requests.
          </div>
          <div block-corners-bottom=""></div>
        </div>

        <!-- Channel 4 -->
        <div class="channel-card">
          <div block-corners-top=""></div>
          <div class="channel-label">DEVELOPER HUBS</div>
          <div class="channel-title">Community &amp; Real-Time Support</div>
          <div style="display: flex; gap: 16px; margin-top: 10px; flex-wrap: wrap;">
            <a class="channel-link" href="https://discord.com" target="_blank" rel="noopener">
              <span>👾 Discord Developer Lounge</span>
            </a>
            <a class="channel-link" href="https://t.me" target="_blank" rel="noopener">
              <span>✈️ Telegram Official Feed</span>
            </a>
          </div>
          <div block-corners-bottom=""></div>
        </div>
      </div>

      <!-- Right Column: Interactive Form -->
      <div class="form-wrapper-card">
        <div block-corners-top=""></div>
        <div class="section-title-bordered" style="margin-bottom: 20px;">DIRECT DISPATCH</div>
        <h2 style="font-size: 22px; font-weight: 700; color: #ffffff; margin: 0 0 18px;">
          Transmit a Priority Transmission
        </h2>
        
        <form id="contact-form" onsubmit="event.preventDefault(); alert('Message transmitted successfully! A CoinGPT engineer will contact you shortly.');">
          <div class="form-row-2">
            <div class="form-group">
              <label class="field-label" for="full-name">Your Name *</label>
              <input class="form-input" type="text" id="full-name" required placeholder="Alex Mercer"/>
            </div>
            <div class="form-group">
              <label class="field-label" for="work-email">Work Email *</label>
              <input class="form-input" type="email" id="work-email" required placeholder="alex@protocol.fi"/>
            </div>
          </div>

          <div class="form-row-2">
            <div class="form-group">
              <label class="field-label" for="org-name">Organization / Protocol</label>
              <input class="form-input" type="text" id="org-name" placeholder="E.g. Nexus Capital / DEX"/>
            </div>
            <div class="form-group">
              <label class="field-label" for="inquiry-type">Inquiry Topic *</label>
              <select class="form-select" id="inquiry-type" required>
                <option value="security-audit">Smart Contract AI Security Audit</option>
                <option value="api-access">High-Throughput Enterprise API Access</option>
                <option value="custom-model">Custom Model Fine-Tuning &amp; Copilot</option>
                <option value="partnership">Strategic Protocol Partnership</option>
                <option value="careers">Careers &amp; Research Fellowship</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label class="field-label" for="message">Transmission Details *</label>
            <textarea class="form-textarea" id="message" required placeholder="Describe your protocol architecture, timeline, and requirements..."></textarea>
          </div>

          <button type="submit" class="btn-primary w-inline-block" style="border:none;background:transparent;cursor:pointer;width:100%;margin-top:10px;" scramble-link="">
            <div class="btn-primary-lines btn-primary-lines-1" style="width: 100%;">
              <div class="btn-primary-lines btn-primary-lines-2" style="width: 100%; text-align: center;">
                <div class="btn-primary-text" scramble-text="" style="justify-content: center; width: 100%;">Transmit Message</div>
              </div>
            </div>
          </button>
        </form>
        <div block-corners-bottom=""></div>
      </div>

    </div>
  </section>

  <!-- FAQ Section (Webflow .faq-2 Accordion) -->
  <section class="content-section" style="border-top: 1px solid rgba(255, 255, 255, 0.06); padding-top: 70px;">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 30px;">
      <div class="section-title-bordered">FREQUENTLY ASKED QUESTIONS</div>
      <h2 style="font-size: clamp(28px, 3.5vw, 42px); font-weight: 800; color: #ffffff; margin: 12px 0 16px; letter-spacing: -0.02em;">
        Client &amp; Partner Inquiries
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        Answers regarding response times, NDA execution, and audit timelines.
      </p>
    </div>

    <div class="faq-list">
      <!-- Item 1 -->
      <div class="faq-2 open">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">What is the typical turnaround time for contact submissions?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Our client solutions engineers review all transmissions continuously. For enterprise inquiries, API keys, and security audits, you will receive an initial technical response within 24 hours.
        </div>
      </div>

      <!-- Item 2 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">Can CoinGPT execute standard mutual NDAs before reviewing proprietary smart contracts?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Yes. We regularly execute bilateral non-disclosure agreements with enterprise clients, hedge funds, and unreleased DeFi protocols before receiving closed source codebases.
        </div>
      </div>

      <!-- Item 3 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">How do I get dedicated institutional API rate limits?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Select "High-Throughput Enterprise API Access" in the contact form or email partnerships@coingpt.tech. We provide dedicated RPC clusters, sub-millisecond endpoints, and custom SLA agreements.
        </div>
      </div>

      <!-- Item 4 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">Where are the CoinGPT core research foundations legally registered?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          The CoinGPT Protocol Foundation is based in Crypto Valley (Zug, Switzerland), with research engineering labs operated out of San Francisco, California.
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
        <div class="section-title-bordered" style="margin-bottom: 12px;">IMMEDIATE ACCESS</div>
        <h3 style="font-size: clamp(24px, 3vw, 36px); font-weight: 800; color: #ffffff; margin: 0 0 12px;">
          Explore the CoinGPT Web3 AI Ecosystem Today
        </h3>
        <p style="color: #9ca3af; font-size: 15px; margin: 0; line-height: 1.6;">
          Tap into autonomous trading assistants, live smart contract scanners, and predictive on-chain intelligence.
        </p>
      </div>

      <div style="position: relative; z-index: 1; display: flex; gap: 16px; flex-wrap: wrap;">
        <a class="btn-primary w-inline-block" href="pricing.html" scramble-link="">
          <div class="btn-primary-lines btn-primary-lines-1">
            <div class="btn-primary-lines btn-primary-lines-2">
              <div class="btn-primary-text" scramble-text="">View Plans &amp; Pricing</div>
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

with open('contact-us.html', 'w', encoding='utf-8') as f:
    f.write(PAGE_HTML)

print("Successfully generated Webflow native contact-us.html")
