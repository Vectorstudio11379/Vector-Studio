# Master builder script for Vector Studioz Case Studies Page (case-studies.html)
# Widescreen 16:9 cinematic showcase matching the user's reference design

import os

with open('template_header.html', 'r', encoding='utf-8') as f:
    HEADER_HTML = f.read().strip()

with open('template_footer.html', 'r', encoding='utf-8') as f:
    FOOTER_HTML = f.read().strip()

PROJECTS = [
    {
        'title': 'Beacon Corporate Realty — Global Real Estate Platform & Visual Media System',
        'category': 'Enterprise Corporate Web',
        'image': '/images/case-studies/beacon.jpg',
        'link': 'https://beaconcorporaterealty.com',
        'desc': 'High-performance commercial real estate investment portal featuring interactive asset catalogs, drone video embeds, and friction-free lead capture.',
        'metrics': [
            ('+50%', 'Investor Inquiries'),
            ('100/100', 'Lighthouse SEO'),
            ('4K Aerial', 'Visual Showcase')
        ]
    },
    {
        'title': 'Twist Studio / JumboDTG — Direct-to-Garment Custom Apparel E-Commerce Store',
        'category': 'Shopify & Custom UX',
        'image': '/images/case-studies/jumbodtg.png',
        'link': 'https://jumbodtg.com/',
        'desc': 'Cinematic digital experience and custom e-commerce storefront with interactive garment configurator, fluid checkout flow, and custom Liquid architecture.',
        'metrics': [
            ('+25%', 'Checkout Conversions'),
            ('Mobile-First', 'Conversion Flow'),
            ('Liquid', 'Custom Architecture')
        ]
    },
    {
        'title': 'Resilient Solutions — Enterprise Cybersecurity & IT Advisory Digital Hub',
        'category': 'Cybersecurity & IT Advisory',
        'image': '/images/case-studies/resilient-solutions.png',
        'link': 'https://timi-portfolio.onrender.com/work',
        'desc': 'Enterprise cybersecurity authority platform engineered with Next.js, featuring an interactive vulnerability risk calculator and automated audit booking.',
        'metrics': [
            ('SOC-2', 'Compliance Standard'),
            ('Interactive', 'Cyber Risk Engine'),
            ('Next.js', 'Full-Stack Portal')
        ]
    },
    {
        'title': 'Mirola Enterprises — High-Conversion Ambassador & Affiliate Platform',
        'category': 'Affiliate & Ambassador Engine',
        'image': '/images/case-studies/mirola-ambassador.png',
        'link': 'https://timi-portfolio.onrender.com/work',
        'desc': 'Multi-tiered partner growth portal built with React, offering real-time commission tracking, gamified progression tiers, and frictionless onboarding.',
        'metrics': [
            ('4 Tiers', 'Progression System'),
            ('Real-Time', 'Referral Telemetry'),
            ('React', 'Interactive UI Cards')
        ]
    },
    {
        'title': 'MIRODATA — Enterprise Role-Based Authentication & Data Hub',
        'category': 'Enterprise Data Portal & Auth',
        'image': '/images/case-studies/mirodata.png',
        'link': 'https://timi-portfolio.onrender.com/work',
        'desc': 'Secure cloud data platform with role-based access controls, encrypted tenant isolation, and interactive data visualization dashboards.',
        'metrics': [
            ('RBAC', 'Admin & Team Portals'),
            ('Secure', 'Session Management'),
            ('TypeScript', 'Robust Architecture')
        ]
    },
    {
        'title': 'Cleaner Spaces — Commercial & Residential Cleaning Platform (New Jersey)',
        'category': 'Web Platform & Quote Engine',
        'image': '/images/case-studies/cleaner-spaces.png',
        'link': 'https://timi-portfolio.onrender.com/work',
        'desc': 'Local service authority site with dynamic square-footage pricing calculator, regional SEO geo-landing pages, and calendar scheduling integration.',
        'metrics': [
            ('Instant', 'Quote Calculator'),
            ('Local SEO', 'Geo-Targeting NJ'),
            ('WordPress', 'High Conversion')
        ]
    },
    {
        'title': '5th Element Media Group — Multi-Brand Client Websites Portfolio',
        'category': 'Creative Agency & Multi-Brand',
        'image': '/images/case-studies/5th-element.png',
        'link': 'https://timi-portfolio.onrender.com/work',
        'desc': 'Fluid Framer agency portfolio demonstrating bespoke micro-interactions, dark glassmorphism styling, and dynamic CMS client showcase modules.',
        'metrics': [
            ('+40%', 'Client Engagement'),
            ('Framer', 'Fluid UI Animations'),
            ('Multi-Brand', 'CMS Architecture')
        ]
    },
    {
        'title': 'Operational Excellence — Digital Operations & Virtual Talent Portal',
        'category': 'Operations & Virtual Talent',
        'image': '/images/case-studies/operational-excellence.png',
        'link': 'https://timi-portfolio.onrender.com/work',
        'desc': 'Consulting marketplace interface connecting technology founders with vetted offshore operators, integrated with automated interview booking.',
        'metrics': [
            ('Interactive', 'Booking Calendar'),
            ('Direct', 'Client Onboarding'),
            ('Tailwind', 'Responsive Design')
        ]
    },
    {
        'title': 'Aliola Global Services — Corporate Digital Transformation Platform',
        'category': 'Corporate Digital Transformation',
        'image': '/images/case-studies/aliola.png',
        'link': 'https://timi-portfolio.onrender.com/work',
        'desc': 'Enterprise management advisory portal featuring process modernization roadmaps, downloadable case studies, and executive consultation funnels.',
        'metrics': [
            ('-35%', 'Operational Overhead'),
            ('Modern', 'Corporate Portal'),
            ('Process', 'Digital Automation')
        ]
    },
    {
        'title': 'Tom Ojo Sports Academy — Global Athlete Discovery & Sports Platform',
        'category': 'Sports & Talent Discovery',
        'image': '/images/case-studies/tom-ojo.png',
        'link': 'https://timi-portfolio.onrender.com/work',
        'desc': 'High-energy athletic academy platform featuring player showcase highlight reels, tournament schedules, and streamlined tryout registrations.',
        'metrics': [
            ('Streamlined', 'Player Registration'),
            ('Live Updates', 'Event Broadcast'),
            ('CMS', 'Content Management')
        ]
    }
]

def generate_case_studies_html():
    cards_html = ""
    for p in PROJECTS:
        metrics_html = "".join([
            f"""<div><div class="caseitem-footer-text">{m[0]}</div><div class="caseitem-footer-subtext">{m[1]}</div></div>"""
            for m in p['metrics']
        ])
        cards_html += f"""
        <div class="case-card-item">
          <a class="article-slide w-inline-block" href="{p['link']}" target="_blank" rel="noopener noreferrer">
            <div class="case-item-head">
              <div class="case-itempartner-logo">
                <img alt="" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/66f4342dde3e7c3beaed31fe_ico-indicator%20(1).svg"/>
              </div>
              <div class="case-item-category">{p['category']}</div>
            </div>
            
            <div class="case-item-image-wrapper">
              <img alt="{p['title']}" class="slide-image-elem" loading="lazy" src="{p['image']}"/>
              <div class="case-item-bg-gradient"></div>
              <div class="arrow-el-wrap">
                <div class="arrow-el arrow-el-bottom-right"></div>
                <div class="arrow-el arrow-el-top-right"></div>
                <div class="arrow-el arrow-el-bottom-left"></div>
                <div class="arrow-el arrow-el-top-left"></div>
              </div>
            </div>
            
            <div class="case-desc">
              <h3 class="case-card-title">{p['title']}</h3>
              <p style="color: #9ca3af; font-size: 0.875rem; line-height: 1.5; margin-top: 0.5rem; margin-bottom: 0;">{p['desc']}</p>
            </div>
            
            <div class="case-item-footer">
              {metrics_html}
            </div>
          </a>
        </div>
        """

    full_page = f"""<!DOCTYPE html>
<html data-wf-domain="www.vectorstudioz.com" data-wf-page="66f3d637353a72aac8d46bde" data-wf-site="64354b8ce4872ad8cd1c7b04" lang="en">
<head>
  <meta charset="utf-8"/>
  <title>Client Case Studies &amp; Digital Showcase — Vector Studioz</title>
  <meta content="Explore award-winning digital experiences, bespoke websites, and AI software engineered by Vector Studioz." name="description"/>
  <meta content="Client Case Studies &amp; Digital Showcase — Vector Studioz" property="og:title"/>
  <meta content="Explore award-winning digital experiences, bespoke websites, and AI software engineered by Vector Studioz." property="og:description"/>
  <meta content="Client Case Studies &amp; Digital Showcase — Vector Studioz" name="twitter:title"/>
  <meta content="Explore award-winning digital experiences, bespoke websites, and AI software engineered by Vector Studioz." name="twitter:description"/>
  <meta content="width=device-width, initial-scale=1" name="viewport"/>
  <link crossorigin="anonymous" href="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/css/chain-gpt.shared.a3558708c.min.css" rel="stylesheet" type="text/css"/>
  <link rel="stylesheet" href="vector-nav.css"/>
  <script src="https://ajax.googleapis.com/ajax/libs/webfont/1.6.26/webfont.js" type="text/javascript"></script>
  <script type="text/javascript">WebFont.load({{ google: {{ families: ["Inter:300,400,500,600,700","Roboto Mono:300,400,500,600,700"] }} }});</script>
</head>
<body class="landing-body" style="background-color: #0b0c10; color: #f3f4f6;">

{HEADER_HTML}

<main class="main">
  <!-- Case Studies Hero -->
  <section class="section" style="padding: 5rem 1.5rem 2.5rem; position: relative;">
    <div class="container" style="max-width: 1400px; margin: 0 auto;">
      <div style="display: flex; flex-direction: column; align-items: flex-start; max-width: 860px;">
        <div style="display: inline-flex; align-items: center; gap: 8px; border: 1px solid rgba(0, 255, 163, 0.3); background: rgba(0, 255, 163, 0.05); padding: 4px 12px; border-radius: 999px; margin-bottom: 1.25rem;">
          <span style="width: 6px; height: 6px; border-radius: 50%; background: #00ffa3;"></span>
          <span style="font-family: 'Roboto Mono', monospace; font-size: 0.75rem; color: #00ffa3; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em;">
            OUR WORK • 100% PRODUCTION READY
          </span>
        </div>
        <h1 style="font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 700; line-height: 1.1; margin: 0 0 1.25rem 0; letter-spacing: -0.02em;">
          Bespoke Experiences &amp; <span style="background: linear-gradient(135deg, #ff007a 0%, #7928ca 40%, #00e1ff 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Client Platforms</span>
        </h1>
        <p style="font-size: 1.15rem; color: #9ca3af; line-height: 1.6; margin: 0 0 2rem 0;">
          Explore how Vector Studioz designs category-defining brands, engineers scalable web applications, and automates workflows for high-growth technology companies and venture-backed founders.
        </p>
      </div>
    </div>
  </section>

  <!-- Widescreen 2-Column Showcase Grid -->
  <section style="position: relative; padding: 0 1.5rem 5rem;">
    <div class="cases-page-grid">
      {cards_html}
    </div>
  </section>

  <!-- Bottom CTA Banner -->
  <section style="padding: 4rem 1.5rem 6rem; background: radial-gradient(circle at center, rgba(0, 255, 163, 0.06) 0%, transparent 70%);">
    <div class="container" style="max-width: 1000px; margin: 0 auto; text-align: center; border: 1px solid rgba(255, 255, 255, 0.08); background: rgba(13, 14, 18, 0.8); backdrop-filter: blur(20px); border-radius: 12px; padding: 4rem 2rem; position: relative;">
      <h2 style="font-size: clamp(2rem, 4vw, 3rem); font-weight: 700; margin: 0 0 1rem 0;">
        Ready to Build Something <span style="background: linear-gradient(135deg, #00ffa3 0%, #00e1ff 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Category-Defining?</span>
      </h2>
      <p style="font-size: 1.15rem; color: #9ca3af; max-width: 600px; margin: 0 auto 2.5rem; line-height: 1.6;">
        Schedule a discovery sprint with our founding partners. We review your goals and deliver a comprehensive architecture roadmap in under 48 hours.
      </p>
      <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
        <a class="btn-primary w-inline-block" href="contact-us.html">
          <div class="btn-primary-text">START A PROJECT</div>
        </a>
        <a class="btn-secondary w-inline-block" href="pricing.html" style="display: inline-flex; align-items: center; padding: 0.85rem 1.75rem; border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 4px; color: #ffffff; text-decoration: none; font-weight: 600; font-size: 0.9rem; background: rgba(255, 255, 255, 0.03); transition: background 0.3s ease;">
          VIEW PRICING &amp; RETAINERS
        </a>
      </div>
    </div>
  </section>
</main>

{FOOTER_HTML}

<script src="vector-nav.js"></script>
</body>
</html>"""

    with open('case-studies.html', 'w', encoding='utf-8') as f:
        f.write(full_page)

    print("case-studies.html successfully rebuilt with 10 real Vector Studioz projects and 16:9 widescreen showcase!")

if __name__ == '__main__':
    generate_case_studies_html()
