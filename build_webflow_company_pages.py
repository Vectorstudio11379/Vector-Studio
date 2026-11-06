"""
build_webflow_company_pages.py
Generates about.html, careers.html, and contact-us.html using the exact
canonical 11-section Webflow landing page layout template from web3-chatbot.html
(as shown in the user's reference screenshot media_1793214418187_04f368f1.png).

Full 11-Section Hierarchy (Pixel-by-pixel match with web3-chatbot.html):
- Section 0: landing-hero-2 (hero-columns, hero-assets-container video, and landing-hero-features bar)
- Section 1: landing-why (4 item-50 cards with corner cuts & gradient icons)
- Section 2: landing-features (feature items with mobile nav, dot list, and banner screenshots)
- Section 3: landing-who-for (4 cards with title block and corner lines)
- Section 4: landing-why (second 4-card item-50 grid matching Webflow layout)
- Section 5: landing-hiw (4 numbered steps with dot lists: step 1 wide, steps 2-4 vertical)
- Section 6: landing-comparison (3-column Webflow comparison table)
- Section 7: landing-launch (single full-width glow CTA bar with action button)
- Section 8: landing-group (2 large side-by-side comparison/channel cards)
- Section 9: landing-faq (Webflow split FAQ layout with interactive accordions)
- Section 10: landing-cta (large CTA banner with 3D robot/aura asset and action buttons)

Strictly enforces:
- Vector Studioz branding, vs-navbar, and site-footer
- Zero team section on about.html
- Zero pricing.html or crypto token links
- index.html remains untouched
"""

import os

with open('template_header.html', 'r', encoding='utf-8') as f:
    HEADER_HTML = f.read().strip()

with open('template_footer.html', 'r', encoding='utf-8') as f:
    FOOTER_HTML = f.read().strip()

def get_head(title, description, canonical_url):
    return f"""  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{title}</title>
  <meta name="description" content="{description}"/>
  <meta property="og:title" content="{title}"/>
  <meta property="og:description" content="{description}"/>
  <meta property="og:type" content="website"/>
  <link rel="canonical" href="{canonical_url}"/>

  <!-- Google Fonts Preconnect -->
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous"/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&family=Roboto+Mono:wght@400;500;600&display=swap" rel="stylesheet"/>

  <!-- Webflow Core Shared CSS -->
  <link rel="stylesheet" type="text/css" crossorigin="anonymous" href="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/css/chain-gpt.shared.a3558708c.min.css"/>
  <link rel="stylesheet" href="vector-nav.css"/>

  <style>
    body {{
      background-color: #08090c;
      color: #efefe5;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      overflow-x: hidden;
    }}
    .gradient-cyan-purple {{
      background: linear-gradient(135deg, #ffffff 0%, #00e5ff 50%, #7a00df 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .landing-badge-pill {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 16px;
      border-radius: 9999px;
      background: rgba(0, 229, 255, 0.08);
      border: 1px solid rgba(0, 229, 255, 0.25);
      color: #00e5ff;
      font-family: 'Roboto Mono', monospace;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 20px;
    }}
    .landing-faq-answer-wrapper {{
      overflow: hidden;
      transition: height 0.3s ease;
    }}
    .landing-faq-question-icon {{
      transition: transform 0.3s ease;
      cursor: pointer;
    }}
    .landing-faq-question-title-wrapper {{
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      user-select: none;
    }}
    /* Form inputs inside Webflow card */
    .form-input-webflow {{
      width: 100%;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 8px;
      padding: 12px 16px;
      color: #ffffff;
      font-size: 14px;
      outline: none;
      transition: border-color 0.2s;
      box-sizing: border-box;
      font-family: 'Inter', sans-serif;
      margin-bottom: 14px;
    }}
    .form-input-webflow:focus {{
      border-color: #00e5ff;
      box-shadow: 0 0 0 1px #00e5ff;
    }}
    .form-label {{
      display: block;
      font-size: 11px;
      font-weight: 600;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 6px;
      font-family: 'Roboto Mono', monospace;
    }}
    /* Scoped 2x2 How It Works Grid Layout */
    .landing-hiw-list-wrapper, .landing-hiw-list-wrapper.sca-hiw-list {{
      display: grid !important;
      grid-template-columns: repeat(2, 1fr) !important;
      grid-template-rows: auto auto !important;
      gap: 24px !important;
    }}
    .landing-hiw-item-wrapper {{
      grid-column: auto !important;
      grid-row: auto !important;
      width: 100% !important;
      max-width: 100% !important;
      margin: 0 !important;
    }}
    .landing-hiw-item {{
      height: 100% !important;
      display: flex !important;
      flex-direction: column !important;
      justify-content: flex-start !important;
    }}
    .landing-hiw-item.chatbot-item-1 {{
      height: 100% !important;
    }}
    .landing-hiw-item-content.item-width-75 {{
      width: 100% !important;
    }}
    @media (max-width: 768px) {{
      .landing-hiw-list-wrapper, .landing-hiw-list-wrapper.sca-hiw-list {{
        grid-template-columns: 1fr !important;
      }}
    }}
  </style>"""

FAQ_ACCORDION_SCRIPT = """  <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
  <script src="vector-nav.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      const faqTitles = document.querySelectorAll('.landing-faq-question-title-wrapper');
      faqTitles.forEach(title => {
        title.addEventListener('click', function() {
          const parent = this.closest('.landing-faq-question-item');
          const answer = parent.querySelector('.landing-faq-answer-wrapper');
          const icon = this.querySelector('.landing-faq-question-icon');
          const isOpen = answer.style.height && answer.style.height !== '0px';

          // Close all others
          document.querySelectorAll('.landing-faq-question-item').forEach(item => {
            const a = item.querySelector('.landing-faq-answer-wrapper');
            const ic = item.querySelector('.landing-faq-question-icon');
            if (a) a.style.height = '0px';
            if (ic) ic.style.transform = 'rotate(0deg)';
          });

          if (!isOpen) {
            answer.style.height = 'auto';
            if (icon) icon.style.transform = 'rotate(45deg)';
          }
        });
      });

      // Open first item by default
      const firstItem = document.querySelector('.landing-faq-question-item');
      if (firstItem) {
        const a = firstItem.querySelector('.landing-faq-answer-wrapper');
        const ic = firstItem.querySelector('.landing-faq-question-icon');
        if (a) a.style.height = 'auto';
        if (ic) ic.style.transform = 'rotate(45deg)';
      }
    });
  </script>"""

# ==========================================
# 1. ABOUT PAGE GENERATOR
# ==========================================
def build_about_page():
    head = get_head(
        title="About Studio — Vector Studioz | Elite Digital Experience &amp; AI Engineering",
        description="Learn how Vector Studioz crafts category-defining digital platforms, WebGL 3D experiences, and autonomous AI systems for global innovators.",
        canonical_url="https://www.vectorstudioz.com/about.html"
    )

    html = f"""<!DOCTYPE html>
<html data-wf-domain="www.vectorstudioz.com" data-wf-page="693d7d6a593bdf05b27d8ec8" data-wf-site="64354b8ce4872ad8cd1c7b04" lang="en">
<head>
{head}
</head>
<body class="landing-body page-ready">

  {HEADER_HTML}

  <main class="main-content">
    <!-- Section 0: Webflow Hero Section -->
    <section class="landing-hero-2 landing-hero-dots-top-left landing-hero-columns">
      <div class="landing-dark-gradient"></div>
      <div class="landing-dark-gradient landing-gradient-bottom landing-mobile-show"></div>
      <div class="landing-dark-gradient landing-gradient-left"></div>
      <div class="landing-dark-gradient landing-gradient-right"></div>
      <div class="landing-container landing-mobile-full-height">
        <div class="landing-hero-wrapper landing-columns">
          
          <!-- Left Column -->
          <div class="landing-hero-title-wrapper landing-column">
            <div class="landing-badge-pill section-title-bordered">ABOUT VECTOR STUDIOZ</div>
            <h1 class="landing-ai-alerts-heading">
              Radical Design Craft. <br/><span class="gradient-cyan-purple">Resilient Engineering.</span>
            </h1>
            <div class="landing-hero-description landing-hero-column">
              Vector Studioz is an elite digital product &amp; experience agency. We bridge bespoke UI/UX design, immersive WebGL spatial graphics, and scalable full-stack software architecture to engineer digital flagships for ambitious innovators worldwide.
            </div>
            <div class="landing-hero-button-wrapper landing-hero-column landing-mobile-hidden" style="display:flex;gap:12px;margin-top:28px;">
              <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="projects.html">
                <div class="btn-primary-wrapper" data-scramble-text="">
                  <div class="btn-primary-text-3" scramble-text="">Explore Client Work &rarr;</div>
                </div>
              </a>
              <a class="btn-secondary-4 w-inline-block" href="contact-us.html">
                <div class="btn-secondary-4-wrapper">
                  <div class="btn-secondary-text-4" scramble-text="">Book Discovery Call</div>
                </div>
              </a>
            </div>
          </div>

          <!-- Right Column: Native Webflow 3D Video Asset -->
          <div class="landing-hero-asset-wrapper hero-column">
            <div class="hero-assets-container w-embed">
              <video autoplay="" class="landing-hero-asset landing-hero-column" loop="" muted="" playsinline="">
                <source src="https://static.coingpt.tech/assets/Videos/ai-chatbot.mp4" type="video/mp4; codecs=hvc1"/>
                <source src="https://static.coingpt.tech/assets/Videos/ai-chatbot.webm" type="video/webm"/>
              </video>
            </div>
          </div>

          <div class="landing-hero-button-wrapper landing-hero-column desktop-hidden">
            <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="projects.html">
              <div class="btn-primary-wrapper" data-scramble-text="">
                <div class="btn-primary-text-3" scramble-text="">Explore Client Work &rarr;</div>
              </div>
            </a>
          </div>
        </div>

        <!-- Hero Features Bar -->
        <div class="landing-hero-features">
          <div class="landing-section-border landing-border-top"></div>
          <div class="landing-section-border"></div>
          <div class="landing-hero-features-list">
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">Zero Bloat Codebases (Next.js &amp; TypeScript)</div>
            </div>
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">Sub-Second Global Edge Latency</div>
            </div>
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">Direct Senior Partner Slack Access</div>
            </div>
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">100% IP &amp; Code Ownership Transfer</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 1: Webflow Why Section (Core Philosophy) -->
    <section class="landing-why">
      <div class="landing-container">
        <div class="landing-why-wrapper">
          <div class="landing-why-title-wrapper" style="text-align:center;max-width:800px;margin:0 auto 40px;">
            <div class="landing-badge-pill section-title-bordered">WHY CHOOSE US</div>
            <h2 class="landing-why-title">Why Ambitious Brands Partner with Vector Studioz</h2>
          </div>
          <div class="landing-why-list why-list-wrap">
            <div class="landing-section-border landing-border-top"></div>
            
            <div class="landing-why-item item-50" block-corners-top="">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e7d5b2039a9b3ae1be0f6_Icon_chatbot_1.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Design from First Principles</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">We reject generic cookie-cutter templates. Every layout, typeface selection, and interaction model is handcrafted to create distinctive brand equity.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Interactive motion prototypes and design token systems that scale seamlessly across multi-platform touchpoints.</div>
              </div>
              <div block-corners-bottom=""></div>
            </div>

            <div class="landing-why-item item-50 no-br-right" block-corners-top="">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e7db0c27f1aad7ae634c4_Icon_chatbot_2.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Enterprise Full-Stack Architecture</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Engineered with Next.js 14, React, Node.js, and TypeScript. Bulletproof security, strict typing, and cloud-native auto-scaling come standard.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">High-throughput database design, distributed caching, and zero-downtime deployment pipelines built for enterprise resilience.</div>
              </div>
              <div block-corners-bottom=""></div>
            </div>

            <div class="landing-why-item item-50 no-br-bottom" block-corners-top="">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693aba8ecc1adb24f3671cae_feature-icon-3.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">High-Velocity Shipping Cadence</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Eliminate bureaucratic project delays. You collaborate directly with principal creative designers and lead systems engineers with weekly production ship releases.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Shared private Slack channels, continuous staging URLs, and asynchronous Loom walkthroughs for total transparency.</div>
              </div>
              <div block-corners-bottom=""></div>
            </div>

            <div class="landing-why-item item-50 no-br-right no-br-bottom" block-corners-top="">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a828953e0dd9d1bce9156_icon_Traders.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Autonomous AI Automation</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Integrate custom fine-tuned LLM agents, dynamic vector data pipelines, and intelligent automated workflows directly into your operational stack.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Multi-agent swarms that triage customer inquiries, generate personalized content, and automate mission-critical operations.</div>
              </div>
              <div block-corners-bottom=""></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Webflow Features (Core Capabilities) -->
    <section class="landing-features" id="landing-features">
      <div class="w-layout-blockcontainer landing-container w-container">
        <div class="landing-features-wrapper">
          <div class="landing-features-title-wrapper">
            <h2 class="landing-features-title">Core Capabilities &amp; Specialized Disciplines</h2>
            <div class="landing-features-desc-wrapper">
              <div class="landing-features-title-desc">We combine aesthetic taste with technical rigor across five core agency pillars. Explore how we transform ambitious concepts into category leaders.</div>
              <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="projects.html">
                <div class="btn-primary-wrapper btn-features" data-scramble-text="">
                  <div class="btn-primary-text-3" scramble-text="">View Featured Work</div>
                  <img alt="" class="btn-primary-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a8238e7f07a24a861ed19_Icon16.svg"/>
                </div>
              </a>
            </div>
          </div>

          <div class="landing-features-list">
            <!-- Feature 1 -->
            <div class="landing-features-list-item">
              <div class="landing-features-item-wrapper">
                <div class="landing-features-content-wrapper content-center">
                  <div class="landing-features-icon-wrapper">
                    <div class="landing-features-mobile-nav landing-nav-full-width">
                      <div class="landing-features-navigation-text">01</div>
                      <div class="landing-features-navigation-line"><div class="landing-line-gradient _16"></div></div>
                      <div class="landing-features-navigation-text">04</div>
                    </div>
                  </div>
                  <h3 class="landing-features-item-title">Bespoke UI/UX &amp; Design Systems</h3>
                  <div class="features-description">Crafting distinctive digital identities that command category leadership.</div>
                  <div class="landing-features-desc-list">
                    <div class="landing-secondary-desc-item">
                      <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                      <div class="landing-secondary-desc-text">Complete Figma design systems with reusable atomic tokens and dark/light components.</div>
                    </div>
                    <div class="landing-secondary-desc-item">
                      <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                      <div class="landing-secondary-desc-text">Interactive micro-interactions, spring physics, and fluid mobile-first ergonomics.</div>
                    </div>
                  </div>
                </div>
                <div class="landing-features-banner-wrapper">
                  <img alt="" class="landing-features-banner landing-desktop" loading="lazy" src="images/features/vector-design-system.png"/>
                </div>
              </div>
            </div>

            <!-- Feature 2 -->
            <div class="landing-features-list-item">
              <div class="landing-features-item-wrapper">
                <div class="landing-features-content-wrapper content-center">
                  <div class="landing-features-icon-wrapper">
                    <div class="landing-features-mobile-nav landing-nav-full-width">
                      <div class="landing-features-navigation-text">02</div>
                      <div class="landing-features-navigation-line"><div class="landing-line-gradient _50"></div></div>
                      <div class="landing-features-navigation-text">04</div>
                    </div>
                  </div>
                  <h3 class="landing-features-item-title">3D &amp; Spatial WebGL Experiences</h3>
                  <div class="features-description">Transforming flat websites into unforgettable spatial playgrounds.</div>
                  <div class="landing-features-desc-list">
                    <div class="landing-secondary-desc-item">
                      <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                      <div class="landing-secondary-desc-text">Custom GLSL shaders, procedural mesh generation, and GPU-optimized Three.js canvases.</div>
                    </div>
                    <div class="landing-secondary-desc-item">
                      <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                      <div class="landing-secondary-desc-text">Silky 60fps performance across iOS Safari, Android Chrome, and desktop browsers.</div>
                    </div>
                  </div>
                </div>
                <div class="landing-features-banner-wrapper">
                  <img alt="" class="landing-features-banner landing-desktop" loading="lazy" src="images/features/vector-webgl-shader.png"/>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 3: Webflow Who For Section -->
    <section class="landing-who-for">
      <div class="landing-container-4">
        <div class="landing-who-for-wrapper">
          <div class="landing-who-for-item landing-item-title">
            <div class="landing-who-for-title-wrapper">
              <h2 class="landing-heading">Who Vector Studioz Is For</h2>
            </div>
            <div class="landing-landing-line landing-section-line landing-right"></div>
            <div class="landing-landing-line landing-section-line"></div>
          </div>
          <div class="landing-who-for-item">
            <img alt="" class="landing-who-for-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a828953e0dd9d1bce9156_icon_Traders.svg"/>
            <h3 class="landing-who-tor-item-title">High-Growth Tech Startups</h3>
            <div class="landing-secondary-desc-item">
              <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot-3"></div><div class="landing-btn-dot-3"></div></div>
              <div class="landing-secondary-desc-text landing-p-24-mob">Establish category dominance before Series A/B fundraising rounds with a magnetic flagship site.</div>
            </div>
          </div>
          <div class="landing-who-for-item">
            <img alt="" class="landing-who-for-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a828953e0dd9d1bce915b_icon_Developers.svg"/>
            <h3 class="landing-who-tor-item-title">Web3 Protocols &amp; DeFi Flagships</h3>
            <div class="landing-secondary-desc-item">
              <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot-3"></div><div class="landing-btn-dot-3"></div></div>
              <div class="landing-secondary-desc-text landing-p-24-mob">Differentiate beyond plain technical docs with cinematic 3D visuals and intuitive dApp UX.</div>
            </div>
          </div>
          <div class="landing-who-for-item">
            <img alt="" class="landing-who-for-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693c201efebd91cec66fc823_cca-icon%20-%20Who%20For1.svg"/>
            <h3 class="landing-who-tor-item-title">Visionary Enterprise Innovators</h3>
            <div class="landing-secondary-desc-item">
              <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot-3"></div><div class="landing-btn-dot-3"></div></div>
              <div class="landing-secondary-desc-text landing-p-24-mob">Replace clunky legacy corporate portals with high-converting, lightning-fast digital storefronts.</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: Webflow Why Section (Second Why: Studio Standards) -->
    <section class="landing-why">
      <div class="landing-container">
        <div class="landing-why-wrapper">
          <h2 class="landing-comparison-title width-80">
            Why Vector Studioz <br/>Leads in Digital Engineering
          </h2>
          <div class="landing-why-list why-list-wrap">
            <div class="landing-section-border landing-border-top"></div>
            
            <div class="landing-why-item item-50">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693abce6109ac59f8c14faee_icon_Founders.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Pure Craftsmanship Standards</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Built specifically for high-growth tech flagships, Web3 leaders, and modern consumer brands.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Zero bloat, strict semantic markup, sub-second latency, and fluid 60fps micro-interactions.</div>
              </div>
            </div>

            <div class="landing-why-item item-50 no-br-right">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e8a2611e18a0751129131_Icon_chatbot_12.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Modern Production Stacks</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Engineered with Next.js 14, WebGL shaders, Three.js, and autonomous AI agents.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Future-proof architectures ready for extreme traffic surges and global edge distribution.</div>
              </div>
            </div>

            <div class="landing-why-item item-50 no-br-bottom">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e8a2686063ea02afa2ae2_Icon_chatbot_13.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Radical Transparency &amp; Telemetry</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Direct private Slack channels, continuous staging URLs, and asynchronous video demos.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Real-time status updates and weekly milestone shipments with zero surprises.</div>
              </div>
            </div>

            <div class="landing-why-item item-50 no-br-bottom no-br-right">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e8aefbabd04e5225e371a_Icon_chatbot_14.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Relentless Performance Obsession</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Guaranteed 95+ Lighthouse scores across performance, accessibility, and best practices.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Engineered for lightning-fast conversions and unmatched client satisfaction.</div>
              </div>
            </div>

            <div class="landing-section-border mobile-hidden"></div>
          </div>
        </div>
      </div>
      <div class="landing-dark-gradient"></div>
      <div class="landing-dark-gradient landing-gradient-bottom"></div>
      <div class="landing-dark-gradient landing-gradient-right"></div>
      <div class="landing-dark-gradient landing-gradient-left"></div>
    </section>

    <!-- Section 5: Webflow How It Works (4-Stage Sprint Journey) -->
    <section class="landing-hiw">
      <div class="landing-container">
        <div class="landing-hiw-wrapper">
          <div class="landing-hiw-title-wrapper">
            <h2 class="landing-hiw-title full-width">Our 4-Stage Sprint Methodology</h2>
            <div class="landing-hiw-desc-wrapper">
              <div class="landing-desc-color">A battle-tested engineering lifecycle designed for precision, velocity, and zero surprises.</div>
            </div>
          </div>

          <div class="landing-hiw-list-wrapper">
            <!-- Step 1 -->
            <div class="landing-hiw-item-wrapper">
              <div class="landing-hiw-item landing-vertical">
                <div class="landing-hiw-item-content hiw-item-vertical">
                  <div class="landing-hiw-item-title-wrapper">
                    <div class="landing-gradient-icon-wrapper landing-hiw-icon">
                      <div class="landing-gradient-icon-container landing-hiw-icon-container">
                        <div class="landing-hiw-number-text">1</div>
                      </div>
                    </div>
                    <h2 class="landing-hiw-item-title">Discovery &amp; Architectural Tech Spec</h2>
                  </div>
                  <div class="landing-secondary-desc-item">
                    <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                    <div class="landing-secondary-desc-text landing-p-24-mob">We align on core product objectives, target customer personas, tech stack requirements, and sprint timelines.</div>
                  </div>
                  <div class="landing-secondary-desc-item">
                    <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                    <div class="landing-secondary-desc-text landing-p-24-mob">Establish Lighthouse performance targets, database schema models, and security requirements upfront.</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Step 2 -->
            <div class="landing-hiw-item-wrapper">
              <div class="landing-hiw-item landing-vertical">
                <div class="landing-hiw-item-content hiw-item-vertical">
                  <div class="landing-hiw-item-title-wrapper">
                    <div class="landing-gradient-icon-wrapper landing-hiw-icon">
                      <div class="landing-gradient-icon-container landing-hiw-icon-container">
                        <div class="landing-hiw-number-text">2</div>
                      </div>
                    </div>
                    <h2 class="landing-hiw-item-title">Bespoke UI/UX &amp; Design Systems</h2>
                  </div>
                  <div class="landing-secondary-desc-text landing-no-padding">High-fidelity interactive Figma wireframes, typography tokens, component libraries, and client review cycles with zero cookie-cutter shortcuts.</div>
                </div>
              </div>
            </div>

            <!-- Step 3 -->
            <div class="landing-hiw-item-wrapper">
              <div class="landing-hiw-item landing-vertical">
                <div class="landing-hiw-item-content hiw-item-vertical">
                  <div class="landing-hiw-item-title-wrapper">
                    <div class="landing-gradient-icon-wrapper landing-hiw-icon">
                      <div class="landing-gradient-icon-container landing-hiw-icon-container">
                        <div class="landing-hiw-number-text">3</div>
                      </div>
                    </div>
                    <h2 class="landing-hiw-item-title">High-Velocity Production Sprints</h2>
                  </div>
                  <div class="landing-secondary-desc-text landing-no-padding">Weekly live deployment staging links, direct Slack engineering channels, clean git commits, and rigorous automated cross-browser testing.</div>
                </div>
              </div>
            </div>

            <!-- Step 4 -->
            <div class="landing-hiw-item-wrapper">
              <div class="landing-hiw-item landing-vertical">
                <div class="landing-hiw-item-content hiw-item-vertical">
                  <div class="landing-hiw-item-title-wrapper">
                    <div class="landing-gradient-icon-wrapper landing-hiw-icon">
                      <div class="landing-gradient-icon-container landing-hiw-icon-container">
                        <div class="landing-hiw-number-text">4</div>
                      </div>
                    </div>
                    <h2 class="landing-hiw-item-title">Launch, Telemetry &amp; Scaling</h2>
                  </div>
                  <div class="landing-secondary-desc-text landing-no-padding">Global CDN propagation, DNS cutover, automated telemetry, performance monitoring, and ongoing monthly retainer iterations.</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 6: Webflow Comparison Table -->
    <section class="landing-comparison">
      <div class="landing-container">
        <h2 class="landing-comparison-title width-80">Vector Studioz vs Traditional Agencies &amp; Freelancers</h2>
        <div class="landing-comparison-table">
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-table-title">Feature / Discipline</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-table-title">Traditional Agency / Dev Shop</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text landing-table-title">Vector Studioz</div>
          </div>

          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text">Design Originality</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-text-secondary">Generic purchased Webflow / WP themes</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text">100% handcrafted from first principles</div>
          </div>

          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text">Direct Communication</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-text-secondary">Slow project manager gatekeepers</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text">Direct Slack with senior engineers &amp; designers</div>
          </div>

          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text">Shipping Cadence</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-text-secondary">Multi-month waterfall release delays</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text">Weekly live staging deployments &amp; ship cycles</div>
          </div>

          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text">Tech Stack Modernity</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-text-secondary">Bloated PHP / legacy CMS plugins</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text">Next.js 14, WebGL shaders, Three.js, AI swarms</div>
          </div>

          <div class="landing-section-border landing-border-top"></div>
          <div class="landing-section-border"></div>
        </div>
      </div>
    </section>

    <!-- Section 7: Webflow Launch CTA Banner -->
    <section class="landing-launch">
      <div class="w-layout-blockcontainer landing-container w-container">
        <div class="landing-launch-wrapper">
          <div class="landing-section-border landing-border-top"></div>
          <div class="landing-section-border"></div>
          <div class="landing-launch-container">
            <h2 class="landing-launch-title">Replace slow agency bureaucracy with high-velocity creative engineering.</h2>
            <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="contact-us.html">
              <div class="btn-primary-wrapper btn-features" data-scramble-text="">
                <div class="btn-primary-text-3" scramble-text="">Schedule Discovery Call &rarr;</div>
              </div>
            </a>
          </div>
        </div>
      </div>
      <div class="landing-dark-gradient landing-gradient-left"></div>
      <div class="landing-dark-gradient landing-gradient-right"></div>
    </section>

    <!-- Section 8: Webflow Group Section (Principles vs Legacy Models) -->
    <section class="landing-group">
      <div class="landing-container">
        <div class="landing-group-wrapper">
          <h2 class="landing-group-title">Studio Operating Principles vs Traditional Agency Models</h2>
          <div class="landing-group-list">
            <div class="landing-group-item-wrapper">
              <div class="landing-group-item">
                <div class="landing-group-item-title-wrapper">
                  <img alt="" class="landing-group-item-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a83613f60ebaed5c9c7fe_group%20Icon%201.svg"/>
                  <div class="landing-group-item-title">Traditional Agency Pitfalls</div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text">Bloated management layers and slow ticket handoffs.</div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text">Opaque hourly billing with surprise scope creep fees.</div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text">Junior talent doing actual build work behind senior pitches.</div>
                </div>
              </div>
              <div class="landing-landing-line landing-section-line landing-right"></div>
            </div>
            <div class="landing-group-item-wrapper right">
              <div class="landing-group-item landing-right">
                <div class="landing-group-item-title-wrapper">
                  <img alt="" class="landing-group-item-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a83613f60ebaed5c9c80b_grout%20Icon2.svg"/>
                  <div class="landing-group-item-title">Vector Studioz Model</div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text">Direct Slack access to principal architects and lead designers.</div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text">Transparent fixed-cost sprints with weekly production deploys.</div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text">100% intellectual property and clean repository ownership transfer.</div>
                </div>
              </div>
              <div class="landing-landing-line landing-section-line"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="landing-dark-gradient"></div>
      <div class="landing-dark-gradient landing-gradient-bottom"></div>
    </section>

    <!-- Section 9: Webflow FAQ Section -->
    <section class="landing-faq">
      <div class="landing-dark-gradient tablet-hidden"></div>
      <div class="landing-dark-gradient landing-gradient-bottom tablet-hidden"></div>
      <div class="landing-dark-gradient landing-gradient-left tablet-hidden"></div>
      <div class="landing-dark-gradient landing-gradient-right tablet-hidden"></div>
      <div class="landing-container">
        <div class="landing-faq-wrapper">
          <div class="landing-section-border tablet-hidden"></div>
          <div class="landing-section-border landing-border-top tablet-hidden"></div>
          <div class="landing-faq-content-wrapper">
            <div class="landing-faq-title-wrapper">
              <h2 class="landing-faq-title">F.A.Q.</h2>
              <div class="landing-faq-desc">
                Have questions regarding our studio sprints? <br/>
                Feel free to <a href="contact-us.html">contact our partners</a>.
              </div>
            </div>
            <div class="landing-faq-questions-list">
              <div class="landing-faq-question-item">
                <div class="landing-faq-question-title-wrapper">
                  <div class="landing-faq-question">What types of digital platforms does Vector Studioz build?</div>
                  <img alt="" class="landing-faq-question-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a836be9c7c929cdb9994d_faq-icon.svg"/>
                </div>
                <div class="landing-faq-answer-wrapper" style="height:0px">
                  <div class="landing-faq-answer w-richtext">
                    <p>We architect bespoke corporate websites, high-converting e-commerce storefronts, high-throughput SaaS web applications, interactive 3D WebGL experiences, and autonomous AI automation pipelines.</p>
                  </div>
                </div>
              </div>

              <div class="landing-faq-question-item">
                <div class="landing-faq-question-title-wrapper">
                  <div class="landing-faq-question">How quickly can we kick off a new project sprint?</div>
                  <img alt="" class="landing-faq-question-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a836be9c7c929cdb9994d_faq-icon.svg"/>
                </div>
                <div class="landing-faq-answer-wrapper" style="height:0px">
                  <div class="landing-faq-answer w-richtext">
                    <p>Upon scope alignment and signed engagement terms, our principal design and engineering leads can typically initiate architectural onboarding within 48 to 72 hours.</p>
                  </div>
                </div>
              </div>

              <div class="landing-faq-question-item">
                <div class="landing-faq-question-title-wrapper">
                  <div class="landing-faq-question">Do we own 100% of the code and intellectual property?</div>
                  <img alt="" class="landing-faq-question-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a836be9c7c929cdb9994d_faq-icon.svg"/>
                </div>
                <div class="landing-faq-answer-wrapper" style="height:0px">
                  <div class="landing-faq-answer w-richtext">
                    <p>Yes. All custom codebases, design files, animations, and infrastructure configurations are 100% client-owned with complete IP transfer upon delivery.</p>
                  </div>
                </div>
              </div>

              <div class="landing-faq-question-item">
                <div class="landing-faq-question-title-wrapper">
                  <div class="landing-faq-question">Do you offer post-launch maintenance and support?</div>
                  <img alt="" class="landing-faq-question-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a836be9c7c929cdb9994d_faq-icon.svg"/>
                </div>
                <div class="landing-faq-answer-wrapper" style="height:0px">
                  <div class="landing-faq-answer w-richtext">
                    <p>Yes. We offer dedicated monthly studio retainers covering ongoing feature development, infrastructure monitoring, 3D model refreshes, and guaranteed SLAs.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 10: Webflow Closing CTA Banner -->
    <section class="landing-cta landing-cta-with-desc">
      <div class="landing-dark-gradient"></div>
      <div class="landing-dark-gradient landing-gradient-bottom"></div>
      <div class="landing-dark-gradient landing-gradient-left"></div>
      <div class="landing-dark-gradient landing-gradient-right"></div>
      <div class="cta-asset-wrapper">
        <img alt="" class="cta-asset" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e928c2ad9d6d66dd9c06e_web%20news%20cta.png"/>
      </div>
      <div class="landing-container full-height">
        <div class="cta-wrapper">
          <div class="landing-section-border landing-border-top"></div>
          <div class="cta-title-wrapper">
            <h2 class="cta-title-2">Ready to Architect an Iconic Digital Flagship?</h2>
            <div class="cta-desk">
              Let’s discuss your upcoming product roadmap, explore interactive 3D concepts, and establish high-velocity production sprint timelines.
            </div>
            <div class="landing-cta-button-wrapper">
              <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="contact-us.html">
                <div class="btn-primary-wrapper" data-scramble-text="">
                  <div class="btn-primary-text-3" scramble-text="">Schedule Discovery Call &rarr;</div>
                </div>
              </a>
              <a class="btn-secondary-4 w-inline-block" href="projects.html">
                <div class="btn-secondary-4-wrapper">
                  <div class="btn-secondary-text-4" scramble-text="">Browse Case Studies</div>
                </div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  {FOOTER_HTML}

  {FAQ_ACCORDION_SCRIPT}
</body>
</html>"""

    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully built canonical 11-section Webflow about.html!")


# ==========================================
# 2. CAREERS PAGE GENERATOR
# ==========================================
def build_careers_page():
    head = get_head(
        title="Careers — Vector Studioz | Join Our Distributed Design &amp; Engineering Studio",
        description="Explore open roles at Vector Studioz. We are seeking elite creative technologists, UI/UX designers, and full-stack software engineers.",
        canonical_url="https://www.vectorstudioz.com/careers.html"
    )

    html = f"""<!DOCTYPE html>
<html data-wf-domain="www.vectorstudioz.com" data-wf-page="693d7d6a593bdf05b27d8ec8" data-wf-site="64354b8ce4872ad8cd1c7b04" lang="en">
<head>
{head}
</head>
<body class="landing-body page-ready">

  {HEADER_HTML}

  <main class="main-content">
    <!-- Section 0: Webflow Hero Section -->
    <section class="landing-hero-2 landing-hero-dots-top-left landing-hero-columns">
      <div class="landing-dark-gradient"></div>
      <div class="landing-dark-gradient landing-gradient-bottom landing-mobile-show"></div>
      <div class="landing-dark-gradient landing-gradient-left"></div>
      <div class="landing-dark-gradient landing-gradient-right"></div>
      <div class="landing-container landing-mobile-full-height">
        <div class="landing-hero-wrapper landing-columns">
          
          <!-- Left Column -->
          <div class="landing-hero-title-wrapper landing-column">
            <div class="landing-badge-pill section-title-bordered">WE'RE HIRING</div>
            <h1 class="landing-ai-alerts-heading">
              Build The Future of <br/><span class="gradient-cyan-purple">Digital Products.</span>
            </h1>
            <div class="landing-hero-description landing-hero-column">
              Join a distributed collective of obsessive creative technologists, UI/UX craftsmen, and systems engineers building world-class platforms for global leaders.
            </div>
            <div class="landing-hero-button-wrapper landing-hero-column landing-mobile-hidden" style="display:flex;gap:12px;margin-top:28px;">
              <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="#open-roles">
                <div class="btn-primary-wrapper" data-scramble-text="">
                  <div class="btn-primary-text-3" scramble-text="">View Open Roles &rarr;</div>
                </div>
              </a>
              <a class="btn-secondary-4 w-inline-block" href="contact-us.html">
                <div class="btn-secondary-4-wrapper">
                  <div class="btn-secondary-text-4" scramble-text="">General Application</div>
                </div>
              </a>
            </div>
          </div>

          <!-- Right Column: Native Webflow 3D Video Asset -->
          <div class="landing-hero-asset-wrapper hero-column">
            <div class="hero-assets-container w-embed">
              <video autoplay="" class="landing-hero-asset landing-hero-column" loop="" muted="" playsinline="">
                <source src="https://static.coingpt.tech/assets/Videos/ai-chatbot.mp4" type="video/mp4; codecs=hvc1"/>
                <source src="https://static.coingpt.tech/assets/Videos/ai-chatbot.webm" type="video/webm"/>
              </video>
            </div>
          </div>

          <div class="landing-hero-button-wrapper landing-hero-column desktop-hidden">
            <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="#open-roles">
              <div class="btn-primary-wrapper" data-scramble-text="">
                <div class="btn-primary-text-3" scramble-text="">View Open Roles &rarr;</div>
              </div>
            </a>
          </div>
        </div>

        <!-- Hero Features Bar -->
        <div class="landing-hero-features">
          <div class="landing-section-border landing-border-top"></div>
          <div class="landing-section-border"></div>
          <div class="landing-hero-features-list">
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">Competitive Global Compensation</div>
            </div>
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">Flexible Hours &amp; Async Flow</div>
            </div>
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">Paid Annual Studio Retreats</div>
            </div>
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">$3,000 Hardware &amp; Tooling Budget</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 1: Webflow Why Section (Studio Culture & Values) -->
    <section class="landing-why">
      <div class="landing-container">
        <div class="landing-why-wrapper">
          <div class="landing-why-title-wrapper" style="text-align:center;max-width:800px;margin:0 auto 40px;">
            <div class="landing-badge-pill section-title-bordered">WHY VECTOR STUDIOZ</div>
            <h2 class="landing-why-title">Why Build Your Career at Vector Studioz</h2>
          </div>
          <div class="landing-why-list why-list-wrap">
            <div class="landing-section-border landing-border-top"></div>
            
            <div class="landing-why-item item-50" block-corners-top="">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e7d5b2039a9b3ae1be0f6_Icon_chatbot_1.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Autonomous Remote Freedom</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">We measure output, creativity, and craftsmanship—not hours logged in a chair. Work from anywhere with true async scheduling.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Zero pointless meetings. Dedicated daily 4-hour deep focus blocks across all teams.</div>
              </div>
              <div block-corners-bottom=""></div>
            </div>

            <div class="landing-why-item item-50 no-br-right" block-corners-top="">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e7db0c27f1aad7ae634c4_Icon_chatbot_2.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Category-Defining Work</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">You will never build boring CRUD apps. You craft high-profile WebGL flagships, spatial 3D products, and autonomous AI systems.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Direct client impact with real-world case studies featured across Awwwards, FWA, and GitHub.</div>
              </div>
              <div block-corners-bottom=""></div>
            </div>

            <div class="landing-why-item item-50 no-br-bottom" block-corners-top="">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693aba8ecc1adb24f3671cae_feature-icon-3.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Top-Tier Tooling &amp; Stipends</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">$3,000 upfront hardware budget for M3 Max MacBook Pros, ultra-wide monitors, and ergonomic setups.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Unlimited access to OpenAI, Claude, Cursor, Figma, and premium software licenses.</div>
              </div>
              <div block-corners-bottom=""></div>
            </div>

            <div class="landing-why-item item-50 no-br-right no-br-bottom" block-corners-top="">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a828953e0dd9d1bce9156_icon_Traders.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Competitive Global Salaries</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Tier-1 compensation benchmarks regardless of your geographic location, paid bi-weekly via Deel or Stripe.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Performance profit-sharing bonuses distributed after successful client sprint completions.</div>
              </div>
              <div block-corners-bottom=""></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Webflow Features (Open Roles) -->
    <section class="landing-features" id="open-roles">
      <div class="w-layout-blockcontainer landing-container w-container">
        <div class="landing-features-wrapper">
          <div class="landing-features-title-wrapper">
            <h2 class="landing-features-title">Open Studio Positions</h2>
            <div class="landing-features-desc-wrapper">
              <div class="landing-features-title-desc">We hire exceptional craftsmen who obsess over details and take immense pride in what they ship. Explore our current open engineering and design roles.</div>
              <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="contact-us.html">
                <div class="btn-primary-wrapper btn-features" data-scramble-text="">
                  <div class="btn-primary-text-3" scramble-text="">Apply Directly &rarr;</div>
                  <img alt="" class="btn-primary-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a8238e7f07a24a861ed19_Icon16.svg"/>
                </div>
              </a>
            </div>
          </div>

          <div class="landing-features-list">
            <!-- Role 1 -->
            <div class="landing-features-list-item">
              <div class="landing-features-item-wrapper">
                <div class="landing-features-content-wrapper content-center">
                  <div class="landing-features-icon-wrapper">
                    <div class="landing-features-mobile-nav landing-nav-full-width">
                      <div class="landing-features-navigation-text">01</div>
                      <div class="landing-features-navigation-line"><div class="landing-line-gradient _16"></div></div>
                      <div class="landing-features-navigation-text">04</div>
                    </div>
                  </div>
                  <h3 class="landing-features-item-title">Senior UI/UX &amp; Design Systems Lead</h3>
                  <div class="features-description">Lead visual direction for tier-1 client flagships and establish foundational Figma token architectures.</div>
                  <div class="landing-features-desc-list">
                    <div class="landing-secondary-desc-item">
                      <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                      <div class="landing-secondary-desc-text">5+ years crafting bespoke digital interfaces, web design systems, and mobile ergonomics.</div>
                    </div>
                    <div class="landing-secondary-desc-item">
                      <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                      <div class="landing-secondary-desc-text">Proficiency with interactive prototyping, spring animation curves, and developer handoffs.</div>
                    </div>
                  </div>
                </div>
                <div class="landing-features-banner-wrapper">
                  <img alt="" class="landing-features-banner landing-desktop" loading="lazy" src="images/features/vector-careers-squad.png"/>
                </div>
              </div>
            </div>

            <!-- Role 2 -->
            <div class="landing-features-list-item">
              <div class="landing-features-item-wrapper">
                <div class="landing-features-content-wrapper content-center">
                  <div class="landing-features-icon-wrapper">
                    <div class="landing-features-mobile-nav landing-nav-full-width">
                      <div class="landing-features-navigation-text">02</div>
                      <div class="landing-features-navigation-line"><div class="landing-line-gradient _50"></div></div>
                      <div class="landing-features-navigation-text">04</div>
                    </div>
                  </div>
                  <h3 class="landing-features-item-title">Creative Technologist (Three.js &amp; WebGL)</h3>
                  <div class="features-description">Architect interactive 3D spatial environments, custom shaders, and particle physics simulations.</div>
                  <div class="landing-features-desc-list">
                    <div class="landing-secondary-desc-item">
                      <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                      <div class="landing-secondary-desc-text">Deep experience with Three.js, React Three Fiber, GLSL fragment/vertex shaders, and WebGPU.</div>
                    </div>
                    <div class="landing-secondary-desc-item">
                      <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                      <div class="landing-secondary-desc-text">Proven track record of maintaining 60fps frame rates on low-power mobile devices.</div>
                    </div>
                  </div>
                </div>
                <div class="landing-features-banner-wrapper">
                  <img alt="" class="landing-features-banner landing-desktop" loading="lazy" src="images/features/vector-fullstack-telemetry.png"/>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 3: Webflow Who For Section (Ideal Candidate Profile) -->
    <section class="landing-who-for">
      <div class="landing-container-4">
        <div class="landing-who-for-wrapper">
          <div class="landing-who-for-item landing-item-title">
            <div class="landing-who-for-title-wrapper">
              <h2 class="landing-heading">Who Thrives at Vector Studioz</h2>
            </div>
            <div class="landing-landing-line landing-section-line landing-right"></div>
            <div class="landing-landing-line landing-section-line"></div>
          </div>
          <div class="landing-who-for-item">
            <img alt="" class="landing-who-for-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a828953e0dd9d1bce9156_icon_Traders.svg"/>
            <h3 class="landing-who-tor-item-title">Autonomous Self-Starters</h3>
            <div class="landing-secondary-desc-item">
              <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot-3"></div><div class="landing-btn-dot-3"></div></div>
              <div class="landing-secondary-desc-text landing-p-24-mob">You take total ownership from blank canvas to production deploy without needing micro-management.</div>
            </div>
          </div>
          <div class="landing-who-for-item">
            <img alt="" class="landing-who-for-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a828953e0dd9d1bce915b_icon_Developers.svg"/>
            <h3 class="landing-who-tor-item-title">Obsessive Polish Champions</h3>
            <div class="landing-secondary-desc-item">
              <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot-3"></div><div class="landing-btn-dot-3"></div></div>
              <div class="landing-secondary-desc-text landing-p-24-mob">You care about sub-pixel alignment, smooth easing transitions, and Lighthouse 100 benchmark scores.</div>
            </div>
          </div>
          <div class="landing-who-for-item">
            <img alt="" class="landing-who-for-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693c201efebd91cec66fc823_cca-icon%20-%20Who%20For1.svg"/>
            <h3 class="landing-who-tor-item-title">Clear Async Communicators</h3>
            <div class="landing-secondary-desc-item">
              <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot-3"></div><div class="landing-btn-dot-3"></div></div>
              <div class="landing-secondary-desc-text landing-p-24-mob">You communicate design decisions and technical tradeoffs clearly via crisp Loom videos and Slack briefs.</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: Webflow Why Section (Second Why: Culture Standards) -->
    <section class="landing-why">
      <div class="landing-container">
        <div class="landing-why-wrapper">
          <h2 class="landing-comparison-title width-80">
            Our Studio Culture <br/>&amp; Engineering Principles
          </h2>
          <div class="landing-why-list why-list-wrap">
            <div class="landing-section-border landing-border-top"></div>
            
            <div class="landing-why-item item-50">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693abce6109ac59f8c14faee_icon_Founders.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Obsession with Craft</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">We never settle for good enough. Every pixel, line of code, and animation curve is refined to world-class standards.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Work alongside teammates who push you to execute at your absolute creative peak.</div>
              </div>
            </div>

            <div class="landing-why-item item-50 no-br-right">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e8a2611e18a0751129131_Icon_chatbot_12.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Zero Bureaucracy</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">No middle managers, no endless sprint planning ceremonies, and no political overhead.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Engineers and designers collaborate directly with founders and partners to ship rapidly.</div>
              </div>
            </div>

            <div class="landing-why-item item-50 no-br-bottom">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e8a2686063ea02afa2ae2_Icon_chatbot_13.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Asynchronous by Default</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Documented decisions, recorded walkthroughs, and protected deep-focus work blocks.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Freedom to work when your energy peaks, whether early morning or late night.</div>
              </div>
            </div>

            <div class="landing-why-item item-50 no-br-bottom no-br-right">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e8aefbabd04e5225e371a_Icon_chatbot_14.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Sustainable Pace</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">We reject startup crunch culture. High velocity comes from clarity and focus, not burnout.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Generous paid time off, mental wellness days, and mandatory disconnected vacations.</div>
              </div>
            </div>

            <div class="landing-section-border mobile-hidden"></div>
          </div>
        </div>
      </div>
      <div class="landing-dark-gradient"></div>
      <div class="landing-dark-gradient landing-gradient-bottom"></div>
      <div class="landing-dark-gradient landing-gradient-right"></div>
      <div class="landing-dark-gradient landing-gradient-left"></div>
    </section>

    <!-- Section 5: Webflow How It Works (Hiring Sprint) -->
    <section class="landing-hiw">
      <div class="landing-container">
        <div class="landing-hiw-wrapper">
          <div class="landing-hiw-title-wrapper">
            <h2 class="landing-hiw-title full-width">Our 4-Stage Hiring Sprint</h2>
            <div class="landing-hiw-desc-wrapper">
              <div class="landing-desc-color">A respectful, fast-paced evaluation process completed in less than 10 business days.</div>
            </div>
          </div>

          <div class="landing-hiw-list-wrapper">
            <!-- Step 1 -->
            <div class="landing-hiw-item-wrapper">
              <div class="landing-hiw-item landing-vertical">
                <div class="landing-hiw-item-content hiw-item-vertical">
                  <div class="landing-hiw-item-title-wrapper">
                    <div class="landing-gradient-icon-wrapper landing-hiw-icon">
                      <div class="landing-gradient-icon-container landing-hiw-icon-container">
                        <div class="landing-hiw-number-text">1</div>
                      </div>
                    </div>
                    <h2 class="landing-hiw-item-title">Portfolio &amp; GitHub Review (&lt; 48 hrs)</h2>
                  </div>
                  <div class="landing-secondary-desc-item">
                    <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                    <div class="landing-secondary-desc-text landing-p-24-mob">We review your real-world case studies, live production websites, Figma files, and code repositories.</div>
                  </div>
                  <div class="landing-secondary-desc-item">
                    <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                    <div class="landing-secondary-desc-text landing-p-24-mob">Guaranteed feedback response within 48 hours for every submitted portfolio.</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Step 2 -->
            <div class="landing-hiw-item-wrapper">
              <div class="landing-hiw-item landing-vertical">
                <div class="landing-hiw-item-content hiw-item-vertical">
                  <div class="landing-hiw-item-title-wrapper">
                    <div class="landing-gradient-icon-wrapper landing-hiw-icon">
                      <div class="landing-gradient-icon-container landing-hiw-icon-container">
                        <div class="landing-hiw-number-text">2</div>
                      </div>
                    </div>
                    <h2 class="landing-hiw-item-title">30-Min Craft &amp; Values Alignment</h2>
                  </div>
                  <div class="landing-secondary-desc-text landing-no-padding">Informal video call with a lead technologist discussing design systems, architecture challenges, and mutual expectations.</div>
                </div>
              </div>
            </div>

            <!-- Step 3 -->
            <div class="landing-hiw-item-wrapper">
              <div class="landing-hiw-item landing-vertical">
                <div class="landing-hiw-item-content hiw-item-vertical">
                  <div class="landing-hiw-item-title-wrapper">
                    <div class="landing-gradient-icon-wrapper landing-hiw-icon">
                      <div class="landing-gradient-icon-container landing-hiw-icon-container">
                        <div class="landing-hiw-number-text">3</div>
                      </div>
                    </div>
                    <h2 class="landing-hiw-item-title">Paid Collaborative Micro-Sprint</h2>
                  </div>
                  <div class="landing-secondary-desc-text landing-no-padding">No whiteboard puzzles. You complete a realistic, paid 3-day micro-challenge compensating your standard consulting rate.</div>
                </div>
              </div>
            </div>

            <!-- Step 4 -->
            <div class="landing-hiw-item-wrapper">
              <div class="landing-hiw-item landing-vertical">
                <div class="landing-hiw-item-content hiw-item-vertical">
                  <div class="landing-hiw-item-title-wrapper">
                    <div class="landing-gradient-icon-wrapper landing-hiw-icon">
                      <div class="landing-gradient-icon-container landing-hiw-icon-container">
                        <div class="landing-hiw-number-text">4</div>
                      </div>
                    </div>
                    <h2 class="landing-hiw-item-title">Formal Offer &amp; Day 1 Onboarding</h2>
                  </div>
                  <div class="landing-secondary-desc-text landing-no-padding">Transparent offer package, hardware ordering, and direct pairing with a senior studio mentor on day one.</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 6: Webflow Comparison Table -->
    <section class="landing-comparison">
      <div class="landing-container">
        <h2 class="landing-comparison-title width-80">Vector Studioz vs Big Corporate Agency Roles</h2>
        <div class="landing-comparison-table">
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-table-title">Culture Factor</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-table-title">Traditional Corporate Agency</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text landing-table-title">Vector Studioz</div>
          </div>

          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text">Creative Ownership</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-text-secondary">Micromanaged by non-technical managers</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text">Total autonomy and credit on shipped work</div>
          </div>

          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text">Meeting Load</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-text-secondary">15–20 hours of fragmented Zoom calls/week</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text">&lt; 2 hours/week (strictly asynchronous updates)</div>
          </div>

          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text">Hardware &amp; Tooling</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-text-secondary">Locked-down slow corporate laptops</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text">$3,000 custom gear stipend + unlimited AI tools</div>
          </div>

          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text">Work Location</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-text-secondary">Mandatory RTO office mandates</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text">100% remote anywhere on Earth</div>
          </div>

          <div class="landing-section-border landing-border-top"></div>
          <div class="landing-section-border"></div>
        </div>
      </div>
    </section>

    <!-- Section 7: Webflow Launch CTA Banner -->
    <section class="landing-launch">
      <div class="w-layout-blockcontainer landing-container w-container">
        <div class="landing-launch-wrapper">
          <div class="landing-section-border landing-border-top"></div>
          <div class="landing-section-border"></div>
          <div class="landing-launch-container">
            <h2 class="landing-launch-title">Don't see your specific discipline? We create roles for exceptional talent.</h2>
            <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="contact-us.html">
              <div class="btn-primary-wrapper btn-features" data-scramble-text="">
                <div class="btn-primary-text-3" scramble-text="">Send General Application &rarr;</div>
              </div>
            </a>
          </div>
        </div>
      </div>
      <div class="landing-dark-gradient landing-gradient-left"></div>
      <div class="landing-dark-gradient landing-gradient-right"></div>
    </section>

    <!-- Section 8: Webflow Group Section (Benefits & Community) -->
    <section class="landing-group">
      <div class="landing-container">
        <div class="landing-group-wrapper">
          <h2 class="landing-group-title">Remote Benefits &amp; Studio Team Rituals</h2>
          <div class="landing-group-list">
            <div class="landing-group-item-wrapper">
              <div class="landing-group-item">
                <div class="landing-group-item-title-wrapper">
                  <img alt="" class="landing-group-item-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a83613f60ebaed5c9c7fe_group%20Icon%201.svg"/>
                  <div class="landing-group-item-title">Asynchronous Freedom</div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text">Protected 4-hour daily maker time with zero interruptions.</div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text">Flexible working schedules tailored to your timezone and peak hours.</div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text">Unlimited sick leave and paid family care days.</div>
                </div>
              </div>
              <div class="landing-landing-line landing-section-line landing-right"></div>
            </div>
            <div class="landing-group-item-wrapper right">
              <div class="landing-group-item landing-right">
                <div class="landing-group-item-title-wrapper">
                  <img alt="" class="landing-group-item-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a83613f60ebaed5c9c80b_grout%20Icon2.svg"/>
                  <div class="landing-group-item-title">Global Studio Retreats</div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text">All-expenses-paid annual week-long international retreats.</div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text">Collaborative in-person hackathons, design jams, and great food.</div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text">Comprehensive international travel insurance included.</div>
                </div>
              </div>
              <div class="landing-landing-line landing-section-line"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="landing-dark-gradient"></div>
      <div class="landing-dark-gradient landing-gradient-bottom"></div>
    </section>

    <!-- Section 9: Webflow FAQ Section -->
    <section class="landing-faq">
      <div class="landing-dark-gradient tablet-hidden"></div>
      <div class="landing-dark-gradient landing-gradient-bottom tablet-hidden"></div>
      <div class="landing-dark-gradient landing-gradient-left tablet-hidden"></div>
      <div class="landing-dark-gradient landing-gradient-right tablet-hidden"></div>
      <div class="landing-container">
        <div class="landing-faq-wrapper">
          <div class="landing-section-border tablet-hidden"></div>
          <div class="landing-section-border landing-border-top tablet-hidden"></div>
          <div class="landing-faq-content-wrapper">
            <div class="landing-faq-title-wrapper">
              <h2 class="landing-faq-title">Careers F.A.Q.</h2>
              <div class="landing-faq-desc">
                Everything you need to know about joining Vector Studioz.<br/>
                Have a question? <a href="contact-us.html">Reach out to talent team</a>.
              </div>
            </div>
            <div class="landing-faq-questions-list">
              <div class="landing-faq-question-item">
                <div class="landing-faq-question-title-wrapper">
                  <div class="landing-faq-question">What timezones does the team work in?</div>
                  <img alt="" class="landing-faq-question-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a836be9c7c929cdb9994d_faq-icon.svg"/>
                </div>
                <div class="landing-faq-answer-wrapper" style="height:0px">
                  <div class="landing-faq-answer w-richtext">
                    <p>We are a 100% globally distributed team with core engineers across the Americas, Europe, and Asia. As long as you have a 2-hour daily overlap with UTC, you can work wherever you thrive.</p>
                  </div>
                </div>
              </div>

              <div class="landing-faq-question-item">
                <div class="landing-faq-question-title-wrapper">
                  <div class="landing-faq-question">How does payroll and contracting work internationally?</div>
                  <img alt="" class="landing-faq-question-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a836be9c7c929cdb9994d_faq-icon.svg"/>
                </div>
                <div class="landing-faq-answer-wrapper" style="height:0px">
                  <div class="landing-faq-answer w-richtext">
                    <p>We process global salaries and contractor invoices via Deel in USD or your local currency with guaranteed bi-weekly payouts and compliant statutory contracts.</p>
                  </div>
                </div>
              </div>

              <div class="landing-faq-question-item">
                <div class="landing-faq-question-title-wrapper">
                  <div class="landing-faq-question">What is the paid micro-sprint stage?</div>
                  <img alt="" class="landing-faq-question-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a836be9c7c929cdb9994d_faq-icon.svg"/>
                </div>
                <div class="landing-faq-answer-wrapper" style="height:0px">
                  <div class="landing-faq-answer w-richtext">
                    <p>Instead of abstract coding puzzles, you work on a scoped real-world challenge alongside our team for 3 days. We compensate you at your full consulting day rate regardless of the final outcome.</p>
                  </div>
                </div>
              </div>

              <div class="landing-faq-question-item">
                <div class="landing-faq-question-title-wrapper">
                  <div class="landing-faq-question">Can I take on personal side projects while at Vector Studioz?</div>
                  <img alt="" class="landing-faq-question-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a836be9c7c929cdb9994d_faq-icon.svg"/>
                </div>
                <div class="landing-faq-answer-wrapper" style="height:0px">
                  <div class="landing-faq-answer w-richtext">
                    <p>Yes, absolutely. We encourage open-source contributions, digital art experiments, and side ventures provided they do not conflict directly with client confidentiality.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 10: Webflow Closing CTA Banner -->
    <section class="landing-cta landing-cta-with-desc">
      <div class="landing-dark-gradient"></div>
      <div class="landing-dark-gradient landing-gradient-bottom"></div>
      <div class="landing-dark-gradient landing-gradient-left"></div>
      <div class="landing-dark-gradient landing-gradient-right"></div>
      <div class="cta-asset-wrapper">
        <img alt="" class="cta-asset" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e928c2ad9d6d66dd9c06e_web%20news%20cta.png"/>
      </div>
      <div class="landing-container full-height">
        <div class="cta-wrapper">
          <div class="landing-section-border landing-border-top"></div>
          <div class="cta-title-wrapper">
            <h2 class="cta-title-2">Ready to Elevate Your Craft with Vector Studioz?</h2>
            <div class="cta-desk">
              Submit your portfolio and join a team that ships category-defining digital products for global visionaries.
            </div>
            <div class="landing-cta-button-wrapper">
              <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="contact-us.html">
                <div class="btn-primary-wrapper" data-scramble-text="">
                  <div class="btn-primary-text-3" scramble-text="">Apply for an Open Role &rarr;</div>
                </div>
              </a>
              <a class="btn-secondary-4 w-inline-block" href="about.html">
                <div class="btn-secondary-4-wrapper">
                  <div class="btn-secondary-text-4" scramble-text="">Explore Studio Culture</div>
                </div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  {FOOTER_HTML}

  {FAQ_ACCORDION_SCRIPT}
</body>
</html>"""

    with open('careers.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully built canonical 11-section Webflow careers.html!")


# ==========================================
# 3. CONTACT US PAGE GENERATOR
# ==========================================
def build_contact_page():
    head = get_head(
        title="Contact Us — Vector Studioz | Start a Project or Schedule a Discovery Call",
        description="Connect with the partners at Vector Studioz. Submit your project discovery brief to kick off high-velocity UI/UX design, WebGL, or software engineering sprints.",
        canonical_url="https://www.vectorstudioz.com/contact-us.html"
    )

    html = f"""<!DOCTYPE html>
<html data-wf-domain="www.vectorstudioz.com" data-wf-page="693d7d6a593bdf05b27d8ec8" data-wf-site="64354b8ce4872ad8cd1c7b04" lang="en">
<head>
{head}
</head>
<body class="landing-body page-ready">

  {HEADER_HTML}

  <main class="main-content">
    <!-- Section 0: Webflow Hero Section -->
    <section class="landing-hero-2 landing-hero-dots-top-left landing-hero-columns">
      <div class="landing-dark-gradient"></div>
      <div class="landing-dark-gradient landing-gradient-bottom landing-mobile-show"></div>
      <div class="landing-dark-gradient landing-gradient-left"></div>
      <div class="landing-dark-gradient landing-gradient-right"></div>
      <div class="landing-container landing-mobile-full-height">
        <div class="landing-hero-wrapper landing-columns">
          
          <!-- Left Column -->
          <div class="landing-hero-title-wrapper landing-column">
            <div class="landing-badge-pill section-title-bordered">START A PROJECT</div>
            <h1 class="landing-ai-alerts-heading">
              Let’s Architect <br/><span class="gradient-cyan-purple">Something Iconic.</span>
            </h1>
            <div class="landing-hero-description landing-hero-column">
              Ready to elevate your digital presence? Fill out the project brief below or connect directly with our studio partners. We guarantee an architectural response within 24 hours.
            </div>
            <div class="landing-hero-button-wrapper landing-hero-column landing-mobile-hidden" style="display:flex;gap:12px;margin-top:28px;">
              <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="#discovery-brief">
                <div class="btn-primary-wrapper" data-scramble-text="">
                  <div class="btn-primary-text-3" scramble-text="">Fill Out Discovery Brief &darr;</div>
                </div>
              </a>
              <a class="btn-secondary-4 w-inline-block" href="https://t.me/vectorstudioz" target="_blank" rel="noopener noreferrer">
                <div class="btn-secondary-4-wrapper">
                  <div class="btn-secondary-text-4" scramble-text="">Telegram Direct &rarr;</div>
                </div>
              </a>
            </div>
          </div>

          <!-- Right Column: Native Webflow 3D Video Asset -->
          <div class="landing-hero-asset-wrapper hero-column">
            <div class="hero-assets-container w-embed">
              <video autoplay="" class="landing-hero-asset landing-hero-column" loop="" muted="" playsinline="">
                <source src="https://static.coingpt.tech/assets/Videos/ai-chatbot.mp4" type="video/mp4; codecs=hvc1"/>
                <source src="https://static.coingpt.tech/assets/Videos/ai-chatbot.webm" type="video/webm"/>
              </video>
            </div>
          </div>

          <div class="landing-hero-button-wrapper landing-hero-column desktop-hidden">
            <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="#discovery-brief">
              <div class="btn-primary-wrapper" data-scramble-text="">
                <div class="btn-primary-text-3" scramble-text="">Fill Out Discovery Brief &darr;</div>
              </div>
            </a>
          </div>
        </div>

        <!-- Hero Features Bar -->
        <div class="landing-hero-features">
          <div class="landing-section-border landing-border-top"></div>
          <div class="landing-section-border"></div>
          <div class="landing-hero-features-list">
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">&lt; 24h Guaranteed Proposal Response</div>
            </div>
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">Direct Senior Partner Slack Access</div>
            </div>
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">Fixed Timelines &amp; Transparent Milestones</div>
            </div>
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">100% Full IP &amp; Code Transfer</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 1: Webflow Why Section (Why Choose Us) -->
    <section class="landing-why">
      <div class="landing-container">
        <div class="landing-why-wrapper">
          <div class="landing-why-title-wrapper" style="text-align:center;max-width:800px;margin:0 auto 40px;">
            <div class="landing-badge-pill section-title-bordered">CLIENT COMMITMENTS</div>
            <h2 class="landing-why-title">Why Ambitious Leaders Partner with Vector Studioz</h2>
          </div>
          <div class="landing-why-list why-list-wrap">
            <div class="landing-section-border landing-border-top"></div>
            
            <div class="landing-why-item item-50" block-corners-top="">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e7d5b2039a9b3ae1be0f6_Icon_chatbot_1.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Guaranteed SLAs &amp; Timelines</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">We establish strict sprint milestones with contractual delivery dates and clear acceptance criteria.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Weekly ship cycles backed by automated CI/CD pipelines and live staging environments.</div>
              </div>
              <div block-corners-bottom=""></div>
            </div>

            <div class="landing-why-item item-50 no-br-right" block-corners-top="">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e7db0c27f1aad7ae634c4_Icon_chatbot_2.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Direct Senior Partner Access</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">No middle-tier account managers or game of telephone. You collaborate directly with principal architects.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Private shared Slack channels, async video reviews, and continuous communication.</div>
              </div>
              <div block-corners-bottom=""></div>
            </div>

            <div class="landing-why-item item-50 no-br-bottom" block-corners-top="">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693aba8ecc1adb24f3671cae_feature-icon-3.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Rapid 48-Hour Sprint Kickoff</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Eliminate the 4-week onboarding slog. We initiate architectural onboarding within 48 to 72 hours.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Pre-configured design token repositories, Next.js templates, and test harnesses ready to roll.</div>
              </div>
              <div block-corners-bottom=""></div>
            </div>

            <div class="landing-why-item item-50 no-br-right no-br-bottom" block-corners-top="">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a828953e0dd9d1bce9156_icon_Traders.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Flexible Engagement Retainers</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Fixed-fee product sprints or rolling monthly engineering retainers aligned with your funding stage.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Transparent pricing with zero hidden fees and 100% intellectual property ownership transfer.</div>
              </div>
              <div block-corners-bottom=""></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Webflow Features (Engagement Disciplines) -->
    <section class="landing-features" id="disciplines">
      <div class="w-layout-blockcontainer landing-container w-container">
        <div class="landing-features-wrapper">
          <div class="landing-features-title-wrapper">
            <h2 class="landing-features-title">Project Engagement Disciplines</h2>
            <div class="landing-features-desc-wrapper">
              <div class="landing-features-title-desc">We offer tailored engagement tracks depending on your product development lifecycle, roadmap speed, and visual requirements.</div>
              <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="#discovery-brief">
                <div class="btn-primary-wrapper btn-features" data-scramble-text="">
                  <div class="btn-primary-text-3" scramble-text="">Submit Brief &rarr;</div>
                  <img alt="" class="btn-primary-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a8238e7f07a24a861ed19_Icon16.svg"/>
                </div>
              </a>
            </div>
          </div>

          <div class="landing-features-list">
            <!-- Feature 1 -->
            <div class="landing-features-list-item">
              <div class="landing-features-item-wrapper">
                <div class="landing-features-content-wrapper content-center">
                  <div class="landing-features-icon-wrapper">
                    <div class="landing-features-mobile-nav landing-nav-full-width">
                      <div class="landing-features-navigation-text">01</div>
                      <div class="landing-features-navigation-line"><div class="landing-line-gradient _16"></div></div>
                      <div class="landing-features-navigation-text">04</div>
                    </div>
                  </div>
                  <h3 class="landing-features-item-title">Design Flagships &amp; Rebrands</h3>
                  <div class="features-description">Complete UI/UX overhaul, atomic Figma design tokens, and bespoke Webflow/Next.js implementations.</div>
                  <div class="landing-features-desc-list">
                    <div class="landing-secondary-desc-item">
                      <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                      <div class="landing-secondary-desc-text">High-converting marketing sites designed for Series A/B fundraising and customer acquisition.</div>
                    </div>
                    <div class="landing-secondary-desc-item">
                      <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                      <div class="landing-secondary-desc-text">Interactive spring physics, custom cursors, and mobile-first responsive optimization.</div>
                    </div>
                  </div>
                </div>
                <div class="landing-features-banner-wrapper">
                  <img alt="" class="landing-features-banner landing-desktop" loading="lazy" src="images/features/vector-contact-onboarding.png"/>
                </div>
              </div>
            </div>

            <!-- Feature 2 -->
            <div class="landing-features-list-item">
              <div class="landing-features-item-wrapper">
                <div class="landing-features-content-wrapper content-center">
                  <div class="landing-features-icon-wrapper">
                    <div class="landing-features-mobile-nav landing-nav-full-width">
                      <div class="landing-features-navigation-text">02</div>
                      <div class="landing-features-navigation-line"><div class="landing-line-gradient _50"></div></div>
                      <div class="landing-features-navigation-text">04</div>
                    </div>
                  </div>
                  <h3 class="landing-features-item-title">Interactive 3D WebGL &amp; Shaders</h3>
                  <div class="features-description">Custom GPU-accelerated spatial graphics, 3D product configurators, and interactive hero canvases.</div>
                  <div class="landing-features-desc-list">
                    <div class="landing-secondary-desc-item">
                      <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                      <div class="landing-secondary-desc-text">Three.js and WebGL shaders engineered for instant load times and 60fps frame rates.</div>
                    </div>
                    <div class="landing-secondary-desc-item">
                      <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                      <div class="landing-secondary-desc-text">Unforgettable spatial storytelling that distinguishes your product from all competitors.</div>
                    </div>
                  </div>
                </div>
                <div class="landing-features-banner-wrapper">
                  <img alt="" class="landing-features-banner landing-desktop" loading="lazy" src="images/features/vector-cloud-architecture.png"/>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 3: Webflow Who For Section -->
    <section class="landing-who-for">
      <div class="landing-container-4">
        <div class="landing-who-for-wrapper">
          <div class="landing-who-for-item landing-item-title">
            <div class="landing-who-for-title-wrapper">
              <h2 class="landing-heading">Who We Collaborate With</h2>
            </div>
            <div class="landing-landing-line landing-section-line landing-right"></div>
            <div class="landing-landing-line landing-section-line"></div>
          </div>
          <div class="landing-who-for-item">
            <img alt="" class="landing-who-for-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a828953e0dd9d1bce9156_icon_Traders.svg"/>
            <h3 class="landing-who-tor-item-title">Seed &amp; Series A Startups</h3>
            <div class="landing-secondary-desc-item">
              <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot-3"></div><div class="landing-btn-dot-3"></div></div>
              <div class="landing-secondary-desc-text landing-p-24-mob">Establish instant market credibility and outshine competitors with an iconic digital flagship.</div>
            </div>
          </div>
          <div class="landing-who-for-item">
            <img alt="" class="landing-who-for-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a828953e0dd9d1bce915b_icon_Developers.svg"/>
            <h3 class="landing-who-tor-item-title">Web3 &amp; AI Technology Leaders</h3>
            <div class="landing-secondary-desc-item">
              <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot-3"></div><div class="landing-btn-dot-3"></div></div>
              <div class="landing-secondary-desc-text landing-p-24-mob">Transform technical whitepapers into captivating, interactive dApp and AI workflow experiences.</div>
            </div>
          </div>
          <div class="landing-who-for-item">
            <img alt="" class="landing-who-for-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693c201efebd91cec66fc823_cca-icon%20-%20Who%20For1.svg"/>
            <h3 class="landing-who-tor-item-title">Global Enterprise Innovators</h3>
            <div class="landing-secondary-desc-item">
              <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot-3"></div><div class="landing-btn-dot-3"></div></div>
              <div class="landing-secondary-desc-text landing-p-24-mob">Modernize critical legacy software platforms with sub-second performance and modular design systems.</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: Webflow Why Section (Second Why: Studio Standards) -->
    <section class="landing-why">
      <div class="landing-container">
        <div class="landing-why-wrapper">
          <h2 class="landing-comparison-title width-80">
            Studio Standards <br/>&amp; Quality Assurance
          </h2>
          <div class="landing-why-list why-list-wrap">
            <div class="landing-section-border landing-border-top"></div>
            
            <div class="landing-why-item item-50">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693abce6109ac59f8c14faee_icon_Founders.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Strict Lighthouse 95+ Scores</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">We optimize asset payloads, font rendering, and layout shifts to guarantee near-perfect speed benchmarks.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Sub-second Core Web Vitals for maximum SEO ranking and conversion velocity.</div>
              </div>
            </div>

            <div class="landing-why-item item-50 no-br-right">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e8a2611e18a0751129131_Icon_chatbot_12.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Cross-Device Ergonomics</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Every element tested across iPhone, iPad, Android, Mac Retina, and 4K desktop screens.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Zero awkward layout wraps, text clipping, or broken touch interactions.</div>
              </div>
            </div>

            <div class="landing-why-item item-50 no-br-bottom">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e8a2686063ea02afa2ae2_Icon_chatbot_13.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Production CI/CD Pipelines</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Automated testing, linting, and preview branches deployed continuously on Vercel or AWS.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Zero manual file FTPs or fragile production scripts.</div>
              </div>
            </div>

            <div class="landing-why-item item-50 no-br-bottom no-br-right">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e8aefbabd04e5225e371a_Icon_chatbot_14.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">Full IP Handover</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">Complete transfer of all Figma design files, source repositories, and deployment configurations.</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">You retain 100% unrestricted intellectual property ownership from day one.</div>
              </div>
            </div>

            <div class="landing-section-border mobile-hidden"></div>
          </div>
        </div>
      </div>
      <div class="landing-dark-gradient"></div>
      <div class="landing-dark-gradient landing-gradient-bottom"></div>
      <div class="landing-dark-gradient landing-gradient-right"></div>
      <div class="landing-dark-gradient landing-gradient-left"></div>
    </section>

    <!-- Section 5: Webflow How It Works (Onboarding Lifecycle) -->
    <section class="landing-hiw">
      <div class="landing-container">
        <div class="landing-hiw-wrapper">
          <div class="landing-hiw-title-wrapper">
            <h2 class="landing-hiw-title full-width">Our Onboarding &amp; Project Lifecycle</h2>
            <div class="landing-hiw-desc-wrapper">
              <div class="landing-desc-color">From initial discovery brief to live production release in 4 structured stages.</div>
            </div>
          </div>

          <div class="landing-hiw-list-wrapper">
            <!-- Step 1 -->
            <div class="landing-hiw-item-wrapper">
              <div class="landing-hiw-item landing-vertical">
                <div class="landing-hiw-item-content hiw-item-vertical">
                  <div class="landing-hiw-item-title-wrapper">
                    <div class="landing-gradient-icon-wrapper landing-hiw-icon">
                      <div class="landing-gradient-icon-container landing-hiw-icon-container">
                        <div class="landing-hiw-number-text">1</div>
                      </div>
                    </div>
                    <h2 class="landing-hiw-item-title">Brief Submission &amp; Architecture Call (&lt; 24h)</h2>
                  </div>
                  <div class="landing-secondary-desc-item">
                    <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                    <div class="landing-secondary-desc-text landing-p-24-mob">Submit the brief below. We review your goals and schedule a 30-minute discovery call within 24 hours.</div>
                  </div>
                  <div class="landing-secondary-desc-item">
                    <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                    <div class="landing-secondary-desc-text landing-p-24-mob">We audit your existing assets, performance benchmarks, and tech requirements upfront.</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Step 2 -->
            <div class="landing-hiw-item-wrapper">
              <div class="landing-hiw-item landing-vertical">
                <div class="landing-hiw-item-content hiw-item-vertical">
                  <div class="landing-hiw-item-title-wrapper">
                    <div class="landing-gradient-icon-wrapper landing-hiw-icon">
                      <div class="landing-gradient-icon-container landing-hiw-icon-container">
                        <div class="landing-hiw-number-text">2</div>
                      </div>
                    </div>
                    <h2 class="landing-hiw-item-title">Fixed Scope Proposal &amp; Roadmap</h2>
                  </div>
                  <div class="landing-secondary-desc-text landing-no-padding">Receive a detailed proposal with fixed sprint costs, deliverable checklists, and exact milestone ship dates.</div>
                </div>
              </div>
            </div>

            <!-- Step 3 -->
            <div class="landing-hiw-item-wrapper">
              <div class="landing-hiw-item landing-vertical">
                <div class="landing-hiw-item-content hiw-item-vertical">
                  <div class="landing-hiw-item-title-wrapper">
                    <div class="landing-gradient-icon-wrapper landing-hiw-icon">
                      <div class="landing-gradient-icon-container landing-hiw-icon-container">
                        <div class="landing-hiw-number-text">3</div>
                      </div>
                    </div>
                    <h2 class="landing-hiw-item-title">Private Slack Channel &amp; Sprint Kickoff</h2>
                  </div>
                  <div class="landing-secondary-desc-text landing-no-padding">You are added to a dedicated studio Slack channel with daily updates, weekly staging URLs, and fast async reviews.</div>
                </div>
              </div>
            </div>

            <!-- Step 4 -->
            <div class="landing-hiw-item-wrapper">
              <div class="landing-hiw-item landing-vertical">
                <div class="landing-hiw-item-content hiw-item-vertical">
                  <div class="landing-hiw-item-title-wrapper">
                    <div class="landing-gradient-icon-wrapper landing-hiw-icon">
                      <div class="landing-gradient-icon-container landing-hiw-icon-container">
                        <div class="landing-hiw-number-text">4</div>
                      </div>
                    </div>
                    <h2 class="landing-hiw-item-title">Production Cutover &amp; Retention Retainer</h2>
                  </div>
                  <div class="landing-secondary-desc-text landing-no-padding">Global DNS propagation, live telemetry verification, complete IP handover, and optional monthly retainer maintenance.</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 6: Webflow Comparison Table -->
    <section class="landing-comparison">
      <div class="landing-container">
        <h2 class="landing-comparison-title width-80">Studio Partnership vs Freelancer Uncertainty</h2>
        <div class="landing-comparison-table">
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-table-title">Partnership Metric</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-table-title">Freelancer / Generic Dev Shop</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text landing-table-title">Vector Studioz</div>
          </div>

          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text">Delivery Reliability</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-text-secondary">Ghosting risks, missed deadlines, scope creep</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text">100% on-time delivery backed by formal SLAs</div>
          </div>

          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text">Architectural Quality</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-text-secondary">Messy spaghetti code with zero typing or tests</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text">Strict TypeScript, Next.js, and CI/CD pipelines</div>
          </div>

          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text">Design Sophistication</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-text-secondary">Generic cookie-cutter templates</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text">Handcrafted design tokens and WebGL spatial graphics</div>
          </div>

          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text">Communication</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-text-secondary">Days to respond to critical inquiries</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text">Direct private Slack with sub-4h response SLAs</div>
          </div>

          <div class="landing-section-border landing-border-top"></div>
          <div class="landing-section-border"></div>
        </div>
      </div>
    </section>

    <!-- Section 7: Webflow Launch CTA Banner -->
    <section class="landing-launch">
      <div class="w-layout-blockcontainer landing-container w-container">
        <div class="landing-launch-wrapper">
          <div class="landing-section-border landing-border-top"></div>
          <div class="landing-section-border"></div>
          <div class="landing-launch-container">
            <h2 class="landing-launch-title">Have an urgent product deadline? We can onboard your sprint within 48 hours.</h2>
            <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="#discovery-brief">
              <div class="btn-primary-wrapper btn-features" data-scramble-text="">
                <div class="btn-primary-text-3" scramble-text="">Fill Out Brief Below &darr;</div>
              </div>
            </a>
          </div>
        </div>
      </div>
      <div class="landing-dark-gradient landing-gradient-left"></div>
      <div class="landing-dark-gradient landing-gradient-right"></div>
    </section>

    <!-- Section 8: Webflow Group Section (Direct Channels & Project Brief Form) -->
    <section class="landing-group" id="discovery-brief">
      <div class="landing-container">
        <div class="landing-group-wrapper">
          <h2 class="landing-group-title">Direct Partner Channels &amp; Project Discovery Brief</h2>
          <div class="landing-group-list">
            
            <!-- Left Card: Contact Information -->
            <div class="landing-group-item-wrapper">
              <div class="landing-group-item">
                <div class="landing-group-item-title-wrapper">
                  <img alt="" class="landing-group-item-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a83613f60ebaed5c9c7fe_group%20Icon%201.svg"/>
                  <div class="landing-group-item-title">Direct Studio Channels</div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text"><strong>Direct Email:</strong> <a href="mailto:contact@vectorstudioz.com" style="color:#00e5ff;">contact@vectorstudioz.com</a></div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text"><strong>Telegram Direct:</strong> <a href="https://t.me/vectorstudioz" target="_blank" rel="noopener noreferrer" style="color:#00e5ff;">@VectorStudiozTeam</a></div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text"><strong>Response Guarantee:</strong> Inquiries triaged in &lt; 24 business hours.</div>
                </div>
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text"><strong>Office / Studio:</strong> Distributed teams across San Francisco, London &amp; Singapore.</div>
                </div>
              </div>
              <div class="landing-landing-line landing-section-line landing-right"></div>
            </div>

            <!-- Right Card: Interactive Project Discovery Brief Form -->
            <div class="landing-group-item-wrapper right">
              <div class="landing-group-item landing-right">
                <div class="landing-group-item-title-wrapper">
                  <img alt="" class="landing-group-item-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a83613f60ebaed5c9c80b_grout%20Icon2.svg"/>
                  <div class="landing-group-item-title">Project Discovery Brief</div>
                </div>
                
                <form id="contact-form" action="#" method="POST" onsubmit="event.preventDefault(); document.getElementById('contact-success').style.display='block'; this.style.display='none';">
                  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
                    <div>
                      <label class="form-label" for="full-name">Full Name *</label>
                      <input class="form-input-webflow" id="full-name" name="name" placeholder="Elijah Ezekiel" required="" type="text"/>
                    </div>
                    <div>
                      <label class="form-label" for="work-email">Work Email *</label>
                      <input class="form-input-webflow" id="work-email" name="email" placeholder="you@company.com" required="" type="email"/>
                    </div>
                  </div>

                  <div>
                    <label class="form-label" for="service-type">Project Discipline *</label>
                    <select class="form-input-webflow" id="service-type" name="service" required="" style="cursor:pointer;background:#0d0e14;">
                      <option value="web-design">Bespoke Web Design &amp; UI/UX</option>
                      <option value="webgl-3d">3D &amp; Spatial WebGL Experience</option>
                      <option value="fullstack-dev">Full-Stack Web Development (Next.js)</option>
                      <option value="ai-automation">Autonomous AI Workflow Automation</option>
                      <option value="mobile-app">Cross-Platform Mobile App (Flutter)</option>
                      <option value="retainer">Full Studio Retainer</option>
                    </select>
                  </div>

                  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
                    <div>
                      <label class="form-label" for="budget-range">Estimated Budget *</label>
                      <select class="form-input-webflow" id="budget-range" name="budget" required="" style="cursor:pointer;background:#0d0e14;">
                        <option value="10k-25k">$10,000 – $25,000</option>
                        <option value="25k-50k">$25,000 – $50,000</option>
                        <option value="50k-100k">$50,000 – $100,000</option>
                        <option value="100k+">$100,000+</option>
                      </select>
                    </div>
                    <div>
                      <label class="form-label" for="timeline">Timeline</label>
                      <select class="form-input-webflow" id="timeline" name="timeline" style="cursor:pointer;background:#0d0e14;">
                        <option value="asap">Immediate / Next 2 Weeks</option>
                        <option value="1-2-months">1 – 2 Months</option>
                        <option value="q1-q2">Next Quarter</option>
                      </select>
                    </div>
                  </div>

                  <div>
                    <label class="form-label" for="project-brief">Project Summary &amp; Goals</label>
                    <textarea class="form-input-webflow" id="project-brief" name="brief" placeholder="Tell us about your brand, current pain points, and key deliverables..." rows="3"></textarea>
                  </div>

                  <div>
                    <button type="submit" class="btn-primary-4 custom-button" style="width:100%;border:none;cursor:pointer;">
                      <div class="btn-primary-wrapper" data-scramble-text="" style="justify-content:center;">
                        <div class="btn-primary-text-3" scramble-text="">Submit Discovery Brief &rarr;</div>
                      </div>
                    </button>
                  </div>
                </form>

                <div id="contact-success" style="display:none;padding:24px;background:rgba(0,255,163,0.08);border:1px solid rgba(0,255,163,0.3);border-radius:8px;text-align:center;">
                  <div style="font-size:24px;margin-bottom:8px;">✓</div>
                  <h3 style="color:#00ffa3;font-size:16px;margin:0 0 6px;">Brief Received Successfully</h3>
                  <p style="color:#94a3b8;font-size:13px;margin:0;">A senior partner will review your project brief and follow up within 24 hours.</p>
                </div>
              </div>
              <div class="landing-landing-line landing-section-line"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="landing-dark-gradient"></div>
      <div class="landing-dark-gradient landing-gradient-bottom"></div>
    </section>

    <!-- Section 9: Webflow FAQ Section -->
    <section class="landing-faq">
      <div class="landing-dark-gradient tablet-hidden"></div>
      <div class="landing-dark-gradient landing-gradient-bottom tablet-hidden"></div>
      <div class="landing-dark-gradient landing-gradient-left tablet-hidden"></div>
      <div class="landing-dark-gradient landing-gradient-right tablet-hidden"></div>
      <div class="landing-container">
        <div class="landing-faq-wrapper">
          <div class="landing-section-border tablet-hidden"></div>
          <div class="landing-section-border landing-border-top tablet-hidden"></div>
          <div class="landing-faq-content-wrapper">
            <div class="landing-faq-title-wrapper">
              <h2 class="landing-faq-title">Onboarding F.A.Q.</h2>
              <div class="landing-faq-desc">
                Everything you need to know about working with Vector Studioz.<br/>
                Have a question? <a href="mailto:contact@vectorstudioz.com">Email our team directly</a>.
              </div>
            </div>
            <div class="landing-faq-questions-list">
              <div class="landing-faq-question-item">
                <div class="landing-faq-question-title-wrapper">
                  <div class="landing-faq-question">What is your typical project kickoff turnaround?</div>
                  <img alt="" class="landing-faq-question-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a836be9c7c929cdb9994d_faq-icon.svg"/>
                </div>
                <div class="landing-faq-answer-wrapper" style="height:0px">
                  <div class="landing-faq-answer w-richtext">
                    <p>Upon reviewing your discovery brief and executing mutual agreements, our engineering and design leads can initiate discovery onboarding within 48 to 72 hours.</p>
                  </div>
                </div>
              </div>

              <div class="landing-faq-question-item">
                <div class="landing-faq-question-title-wrapper">
                  <div class="landing-faq-question">How are project deliverables and billing structured?</div>
                  <img alt="" class="landing-faq-question-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a836be9c7c929cdb9994d_faq-icon.svg"/>
                </div>
                <div class="landing-faq-answer-wrapper" style="height:0px">
                  <div class="landing-faq-answer w-richtext">
                    <p>We work on fixed-scope weekly sprints or dedicated monthly retainers. Projects are typically billed 50% upfront and 50% upon final acceptance handover, with zero hidden hourly surprises.</p>
                  </div>
                </div>
              </div>

              <div class="landing-faq-question-item">
                <div class="landing-faq-question-title-wrapper">
                  <div class="landing-faq-question">Do we own 100% of all intellectual property?</div>
                  <img alt="" class="landing-faq-question-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a836be9c7c929cdb9994d_faq-icon.svg"/>
                </div>
                <div class="landing-faq-answer-wrapper" style="height:0px">
                  <div class="landing-faq-answer w-richtext">
                    <p>Yes. Upon completion and final settlement, all custom codebases, design Figma files, 3D meshes, and deployment scripts are 100% your property with full transfer.</p>
                  </div>
                </div>
              </div>

              <div class="landing-faq-question-item">
                <div class="landing-faq-question-title-wrapper">
                  <div class="landing-faq-question">What happens if we need post-launch iterations or support?</div>
                  <img alt="" class="landing-faq-question-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a836be9c7c929cdb9994d_faq-icon.svg"/>
                </div>
                <div class="landing-faq-answer-wrapper" style="height:0px">
                  <div class="landing-faq-answer w-richtext">
                    <p>We include a 14-day warranty on all delivered codebases and offer flexible monthly retainer packages covering continuous feature development, WebGL performance updates, and SLAs.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 10: Webflow Closing CTA Banner -->
    <section class="landing-cta landing-cta-with-desc">
      <div class="landing-dark-gradient"></div>
      <div class="landing-dark-gradient landing-gradient-bottom"></div>
      <div class="landing-dark-gradient landing-gradient-left"></div>
      <div class="landing-dark-gradient landing-gradient-right"></div>
      <div class="cta-asset-wrapper">
        <img alt="" class="cta-asset" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e928c2ad9d6d66dd9c06e_web%20news%20cta.png"/>
      </div>
      <div class="landing-container full-height">
        <div class="cta-wrapper">
          <div class="landing-section-border landing-border-top"></div>
          <div class="cta-title-wrapper">
            <h2 class="cta-title-2">Ready to Transform Your Digital Presence?</h2>
            <div class="cta-desk">
              Submit your project brief above or reach out directly to schedule an architectural discovery discussion.
            </div>
            <div class="landing-cta-button-wrapper">
              <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="#discovery-brief">
                <div class="btn-primary-wrapper" data-scramble-text="">
                  <div class="btn-primary-text-3" scramble-text="">Submit Project Brief &darr;</div>
                </div>
              </a>
              <a class="btn-secondary-4 w-inline-block" href="projects.html">
                <div class="btn-secondary-4-wrapper">
                  <div class="btn-secondary-text-4" scramble-text="">Browse Case Studies</div>
                </div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  {FOOTER_HTML}

  {FAQ_ACCORDION_SCRIPT}
</body>
</html>"""

    with open('contact-us.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully built canonical 11-section Webflow contact-us.html!")


if __name__ == '__main__':
    build_about_page()
    build_careers_page()
    build_contact_page()
