# Generator for Agency Native Webflow contact-us.html

with open('template_header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

with open('template_footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

PAGE_HTML = f"""<!DOCTYPE html>
<html data-wf-domain="www.vectorstudioz.com" data-wf-page="6488c93b137bd37e5762ce48" data-wf-site="64354b8ce4872ad8cd1c7b04" lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>Start a Project — Vector Studioz | Bespoke Web Design &amp; AI Engineering</title>
  <meta name="description" content="Connect with Vector Studioz partners to discuss bespoke web design, custom full-stack software development, dedicated product squads, and autonomous AI automation."/>
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
      border-color: rgba(0, 225, 255, 0.35);
      transform: translateY(-2px);
    }}
    .channel-label {{
      font-family: 'Roboto Mono', monospace;
      font-size: 12px;
      color: #00e1ff;
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
      color: #00ffa3;
      font-size: 15px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: color 0.2s;
    }}
    .channel-link:hover {{
      color: #00e1ff;
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
      border-color: #00e1ff;
      box-shadow: 0 0 10px rgba(0, 225, 255, 0.2);
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

  <!-- Contact Hero -->
  <section class="contact-hero-container" style="text-align: center;">
    <div class="hero-glow-bg"></div>
    <div class="section-title-bordered">DISCOVERY &amp; INTAKE</div>
    <h1 class="hero-title-h1">Start a Project with <span class="gradient-text">Vector Studioz</span></h1>
    <p class="hero-desc-p">
      Accelerate your brand with bespoke UI/UX design, high-speed full-stack software development, and autonomous AI automation. Our founding partners review all submissions and respond within 24 hours.
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
          <div class="channel-label">NEW PROJECT INQUIRIES</div>
          <div class="channel-title">Direct Client Scopes &amp; RFPs</div>
          <a class="channel-link" href="mailto:projects@vectorstudioz.com">
            <span>✉️ projects@vectorstudioz.com</span>
          </a>
          <div class="channel-desc">
            Direct inbox for design sprints, dedicated product squads, and bespoke software architecture inquiries.
          </div>
          <div block-corners-bottom=""></div>
        </div>

        <!-- Channel 2 -->
        <div class="channel-card">
          <div block-corners-top=""></div>
          <div class="channel-label">PARTNERSHIPS &amp; GENERAL</div>
          <div class="channel-title">Studio Collaborations &amp; Press</div>
          <a class="channel-link" href="mailto:hello@vectorstudioz.com">
            <span>🤝 hello@vectorstudioz.com</span>
          </a>
          <div class="channel-desc">
            Strategic co-ventures, podcast/keynote speaking, media assets, and general studio communications.
          </div>
          <div block-corners-bottom=""></div>
        </div>

        <!-- Channel 3 -->
        <div class="channel-card">
          <div block-corners-top=""></div>
          <div class="channel-label">STUDIO HUBS</div>
          <div class="channel-title">San Francisco &amp; London</div>
          <div style="font-size: 14px; color: #d1d5db; margin-top: 6px; line-height: 1.5;">
            📍 <strong>SF Studio:</strong> 550 Montgomery St, Financial District, CA<br/>
            📍 <strong>London Hub:</strong> 100 Shoreditch High St, Tech City, UK
          </div>
          <div class="channel-desc" style="margin-top: 10px;">
            We operate asynchronously with dedicated team coverage spanning Pacific to Central European time zones.
          </div>
          <div block-corners-bottom=""></div>
        </div>

        <!-- Channel 4 -->
        <div class="channel-card">
          <div block-corners-top=""></div>
          <div class="channel-label">DISCOVERY CALL</div>
          <div class="channel-title">30-Minute Architecture Alignment</div>
          <div class="channel-desc">
            Prefer an immediate conversation? Schedule directly with one of our founding partners to walk through your design, software, or AI roadmap.
          </div>
          <div block-corners-bottom=""></div>
        </div>
      </div>

      <!-- Right Column: Interactive Form -->
      <div class="form-wrapper-card">
        <div block-corners-top=""></div>
        <div class="section-title-bordered" style="margin-bottom: 20px;">PROJECT INTAKE</div>
        <h2 style="font-size: 22px; font-weight: 700; color: #ffffff; margin: 0 0 18px;">
          Tell Us About Your Vision
        </h2>
        
        <form id="contact-form" onsubmit="event.preventDefault(); alert('Inquiry received! A Vector Studioz partner will contact you within 24 hours.');">
          <div class="form-row-2">
            <div class="form-group">
              <label class="field-label" for="full-name">Your Name *</label>
              <input class="form-input" type="text" id="full-name" required placeholder="Alex Mercer"/>
            </div>
            <div class="form-group">
              <label class="field-label" for="work-email">Work Email *</label>
              <input class="form-input" type="email" id="work-email" required placeholder="alex@company.com"/>
            </div>
          </div>

          <div class="form-row-2">
            <div class="form-group">
              <label class="field-label" for="org-name">Company / Brand Name</label>
              <input class="form-input" type="text" id="org-name" placeholder="E.g. Acme Technologies"/>
            </div>
            <div class="form-group">
              <label class="field-label" for="inquiry-type">Primary Capability *</label>
              <select class="form-select" id="inquiry-type" required>
                <option value="web-design">Bespoke Web Design &amp; UI/UX</option>
                <option value="fullstack-dev">Full-Stack Web Development</option>
                <option value="software-eng">Custom Software Engineering</option>
                <option value="ai-automation">AI Automation &amp; Multi-Agent Workflows</option>
                <option value="webgl-3d">3D &amp; WebGL Spatial Experiences</option>
                <option value="dedicated-squad">Dedicated Product Squad Retainer</option>
              </select>
            </div>
          </div>

          <div class="form-row-2">
            <div class="form-group">
              <label class="field-label" for="budget-range">Estimated Budget Range</label>
              <select class="form-select" id="budget-range">
                <option value="under-25k">$10,000 – $25,000</option>
                <option value="25k-50k" selected>$25,000 – $50,000</option>
                <option value="50k-100k">$50,000 – $100,000</option>
                <option value="100k-plus">$100,000+</option>
              </select>
            </div>
            <div class="form-group">
              <label class="field-label" for="project-timeline">Target Timeline</label>
              <select class="form-select" id="project-timeline">
                <option value="asap">ASAP (Next 2-4 weeks)</option>
                <option value="1-3-months" selected>1 – 3 Months</option>
                <option value="ongoing">Ongoing Monthly Retainer</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label class="field-label" for="message">Project Scope &amp; Goals *</label>
            <textarea class="form-textarea" id="message" required placeholder="Describe your product vision, target audience, core deliverables, and success metrics..."></textarea>
          </div>

          <button type="submit" class="btn-primary w-inline-block" style="border:none;background:transparent;cursor:pointer;width:100%;margin-top:10px;" scramble-link="">
            <div class="btn-primary-lines btn-primary-lines-1" style="width: 100%;">
              <div class="btn-primary-lines btn-primary-lines-2" style="width: 100%; text-align: center;">
                <div class="btn-primary-text" scramble-text="" style="justify-content: center; width: 100%;">Transmit Project Inquiry</div>
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
        Discovery &amp; Onboarding FAQs
      </h2>
      <p style="color: #9ca3af; font-size: 16px; line-height: 1.6;">
        Answers regarding response times, NDA execution, and kick-off timelines.
      </p>
    </div>

    <div class="faq-list">
      <!-- Item 1 -->
      <div class="faq-2 open">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">What happens after I submit this intake form?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          A founding partner reviews your project details within 24 hours. If there is a strong fit, we will send preliminary architectural thoughts and invite you to a 30-minute discovery video call.
        </div>
      </div>

      <!-- Item 2 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">Can we sign an NDA before sharing proprietary details?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Yes. We regularly execute bilateral non-disclosure agreements with venture-backed startups and enterprises before reviewing confidential product specs or unreleased intellectual property.
        </div>
      </div>

      <!-- Item 3 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">How do you manage communication during active sprints?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          We invite your team into a private shared Slack channel with our designers and engineers. We provide daily async video walkthroughs via Loom and conduct weekly live sprint demos.
        </div>
      </div>

      <!-- Item 4 -->
      <div class="faq-2">
        <div class="faq-2-top" onclick="toggleFaq(this)">
          <div class="faq-2-title">What are your payment and invoicing terms?</div>
          <div class="faq-2-plus">+</div>
        </div>
        <div class="faq-2-bottom">
          Fixed-scope sprints are invoiced 50% upfront and 50% upon final delivery and code transfer. Dedicated squads are billed on a flat monthly retainer on the 1st of each month with 30-day cancellation flexibility.
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
        <div class="section-title-bordered" style="margin-bottom: 12px;">EXPLORE PRICING</div>
        <h3 style="font-size: clamp(24px, 3vw, 36px); font-weight: 800; color: #ffffff; margin: 0 0 12px;">
          Review Transparent Plans &amp; Retainers
        </h3>
        <p style="color: #9ca3af; font-size: 15px; margin: 0; line-height: 1.6;">
          Check out our fixed-scope design sprints and dedicated agile engineering squads with zero hidden fees.
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
      document.querySelectorAll('.faq-2').forEach(f => f.classList.remove('open'));
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

print("Successfully generated Vector Studioz agency contact-us.html")
