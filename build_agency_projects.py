"""
Master Builder for Vector Studioz Client Projects Catalog (projects.html & case-studies.html)
Pixel-by-pixel Webflow Architecture Replica of coingpt.tech/case-studies.
"""

import os
import shutil
from projects_data import PROJECTS_LIST

def build_projects_catalog():
    with open('template_header.html', 'r', encoding='utf-8') as f:
        template_header = f.read().strip()
    with open('template_footer.html', 'r', encoding='utf-8') as f:
        template_footer = f.read().strip()

    # Color accents for dynamic card gradient glows
    glow_colors = [
        '#00e5ff', '#7928ca', '#00ffa3', '#ff007a',
        '#ffe600', '#26f4d0', '#724ce8', '#fc6756'
    ]

    cards_html = []
    for idx, p in enumerate(PROJECTS_LIST):
        slug = p['slug']
        title = p['title']
        short_title = p.get('short_title', title)
        category = p.get('category', 'Web Design')
        category_tag = p.get('category_tag', 'Web Design')
        badge = p.get('badge', category_tag)
        year = p.get('year', '2025')
        live_url = p.get('live_url', '#')
        thumbnail = p.get('thumbnail', 'images/case-studies/beacon.jpg')
        if thumbnail.startswith('/'):
            thumbnail = thumbnail.lstrip('/')
        tagline = p.get('tagline', p.get('overview', '')[:120] + '...')
        metrics = p.get('metrics', [])
        accent = glow_colors[idx % len(glow_colors)]

        # Map category_tag to standard filter slug
        filter_slug = category_tag.lower().replace('&', '').replace(' ', '-').strip('-')

        # Build metrics HTML (case-item-footer)
        metrics_cells = "".join([
            f'''<div class="case-metric-block">
                <div class="caseitem-footer-text">{m['value']}</div>
                <div class="caseitem-footer-subtext">{m['label']}</div>
            </div>'''
            for m in metrics[:3]
        ])

        card = f'''
        <div role="listitem" class="articles-item w-dyn-item" data-category="{category_tag}" data-category-slug="{filter_slug}">
          <div class="article-card case-card">
            <div class="case-item-head">
              <div class="case-itempartner-logo">
                <img src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/66f4342dde3e7c3beaed31fe_ico-indicator%20(1).svg" loading="lazy" alt="" class="image-1040"/>
                <span class="case-partner-badge-text">{badge}</span>
              </div>
              <div class="case-category-label">{category}</div>
            </div>
            
            <div class="case-item-image-wrapper" data-glow-color="{accent}">
              <div class="case-bg-color" style="display:none;">{accent}</div>
              <img src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/66f541217865e2860531e46b_Group%201%20(3).png" loading="lazy" alt="" class="case-item-thumb-bg"/>
              <div class="case-item-bg-gradient" style="background: linear-gradient(134.28deg, {accent} 10.03%, rgba(9, 9, 14, 0) 42.81%);"></div>
              
              <div class="article-thumb case-item-thmb">
                <a href="/projects/{slug}.html" class="article-thumb-link w-inline-block" aria-label="View {short_title} Case Study">
                  <img src="{thumbnail}" loading="lazy" alt="{title}" class="article-thumb-img"/>
                </a>
                <div class="corners-wrap">
                  <div class="corner-elem corner-elem-top-left"></div>
                  <div class="corner-elem corner-elem-top-right"></div>
                  <div class="corner-elem corner-elem-bottom-right"></div>
                  <div class="corner-elem corner-bottom-left"></div>
                </div>
                <div class="arrow-el-wrap">
                  <div class="arrow-el arrow-el-bottom-right"></div>
                  <div class="arrow-el arrow-el-top-right"></div>
                  <div class="arrow-el arrow-el-bottom-left"></div>
                  <div class="arrow-el arrow-el-top-left"></div>
                </div>
              </div>
            </div>
            
            <div class="case-desc-wrap">
              <a href="/projects/{slug}.html" class="ai-title-link case-item-title-link w-inline-block">
                <h3 fs-cmsfilter-field="title" class="article-title">{title}</h3>
              </a>
              <p class="case-item-summary">{tagline}</p>
            </div>
            
            <div class="case-item-footer">
              {metrics_cells}
            </div>

            <div class="case-card-actions-bar">
              <a href="/projects/{slug}.html" class="case-action-view">View Case Study &rarr;</a>
              <a href="{live_url}" target="_blank" rel="noopener noreferrer" class="case-action-live">Live Site &#8599;</a>
            </div>
          </div>
        </div>
        '''
        cards_html.append(card)

    rendered_cards = "\n".join(cards_html)

    page_html = f'''<!DOCTYPE html>
<html data-wf-domain="www.vectorstudioz.com" data-wf-page="66f3d637353a72aac8d46bde" data-wf-site="64354b8ce4872ad8cd1c7b04" lang="en">
<head>
  <meta charset="utf-8"/>
  <title>Client Projects &amp; Digital Case Studies | Vector Studioz</title>
  <meta name="description" content="Explore Vector Studioz' portfolio of 15 production web platforms, SaaS applications, custom e-commerce stores, and digital experience engines built for global leaders."/>
  <meta property="og:title" content="Client Projects &amp; Digital Case Studies | Vector Studioz"/>
  <meta property="og:description" content="Explore Vector Studioz' portfolio of 15 production web platforms, SaaS applications, and interactive digital experiences."/>
  <meta property="og:image" content="images/case-studies/beacon.jpg"/>
  <meta property="og:type" content="website"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <link rel="canonical" href="https://www.vectorstudioz.com/projects.html"/>

  <!-- Google Fonts Preconnect -->
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous"/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&family=Roboto+Mono:wght@400;500;600&display=swap" rel="stylesheet"/>

  <!-- Core Webflow & Shared CSS Architecture -->
  <link rel="stylesheet" type="text/css" crossorigin="anonymous" href="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/css/chain-gpt.shared.a3558708c.min.css"/>
  <link rel="stylesheet" href="vector-nav.css"/>

  <style>
    /* Custom Webflow Project Page Overrides & Enhancements */
    body {{
      background-color: #08090c;
      color: #efefe5;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      overflow-x: hidden;
    }}

    .gradient-cyan-purple {{
      background: linear-gradient(135deg, #ffffff 0%, #00e5ff 60%, #7a00df 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .articles-hero {{
      padding-top: 140px;
      padding-bottom: 40px;
      position: relative;
    }}

    .section-title-bordered-line-1.stbl-blog:after {{
      left: 0;
      width: calc(100% - 13px);
    }}

    /* Webflow Articles / Projects Grid Section Layout & Centering */
    .articles-section {{
      padding: 60px 0 120px !important;
      width: 100% !important;
      max-width: 100vw !important;
      overflow-x: hidden !important;
      position: relative !important;
      box-sizing: border-box !important;
    }}

    .articles-section .container {{
      max-width: 1240px !important;
      width: 100% !important;
      margin-left: auto !important;
      margin-right: auto !important;
      padding-left: 24px !important;
      padding-right: 24px !important;
      box-sizing: border-box !important;
      float: none !important;
      position: relative !important;
    }}

    .articles-wrap {{
      display: block !important;
      width: 100% !important;
      max-width: 100% !important;
      margin: 0 auto !important;
      padding: 0 !important;
      float: none !important;
      box-sizing: border-box !important;
    }}

    .container-middle {{
      display: block !important;
      width: 100% !important;
      max-width: 100% !important;
      margin: 0 auto !important;
      padding: 0 !important;
      float: none !important;
      box-sizing: border-box !important;
    }}

    .w-dyn-list {{
      width: 100% !important;
      max-width: 100% !important;
      margin: 0 auto !important;
      padding: 0 !important;
      box-sizing: border-box !important;
    }}

    .filters-panel {{
      width: 100% !important;
      max-width: 100% !important;
      margin: 0 auto !important;
      box-sizing: border-box !important;
    }}

    .filter-search-wrap {{
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box !important;
    }}

    /* Multi-Column Grid with Generous Spacing for Project Cards */
    .articles-list {{
      display: grid !important;
      grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
      gap: 36px 28px !important;
      margin-top: 40px !important;
      margin-left: 0 !important;
      margin-right: 0 !important;
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box !important;
      padding: 0 !important;
      float: none !important;
    }}

    @media screen and (max-width: 1100px) {{
      .articles-list {{
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 28px 24px !important;
      }}
    }}

    @media screen and (max-width: 700px) {{
      .articles-list {{
        grid-template-columns: minmax(0, 1fr) !important;
        gap: 24px !important;
      }}
    }}

    .articles-item {{
      width: 100% !important;
      min-width: 0 !important;
      max-width: 100% !important;
      margin: 0 !important;
      margin-bottom: 0 !important;
      display: flex !important;
      box-sizing: border-box !important;
      float: none !important;
      overflow: hidden !important;
    }}

    /* Project Cards Enhanced Styling & Breathing Room */
    .case-card {{
      background: rgba(13, 14, 20, 0.75) !important;
      border: 1px solid rgba(255, 255, 255, 0.08) !important;
      border-radius: 14px !important;
      padding: 24px !important;
      box-sizing: border-box !important;
      transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease, background 0.3s ease !important;
      display: flex !important;
      flex-direction: column !important;
      justify-content: space-between !important;
      height: 100% !important;
      width: 100% !important;
      min-width: 0 !important;
      max-width: 100% !important;
      overflow: hidden !important;
      position: relative !important;
      word-wrap: break-word !important;
      overflow-wrap: break-word !important;
    }}

    .case-card:hover {{
      transform: translateY(-5px) !important;
      border-color: rgba(0, 229, 255, 0.4) !important;
      background: rgba(18, 20, 28, 0.9) !important;
      box-shadow: 0 16px 36px -10px rgba(0, 229, 255, 0.15) !important;
    }}

    .case-item-head {{
      display: flex !important;
      align-items: center !important;
      justify-content: space-between !important;
      gap: 12px !important;
      margin-bottom: 16px !important;
      width: 100% !important;
      min-width: 0 !important;
      box-sizing: border-box !important;
      padding-left: 0 !important;
      padding-right: 0 !important;
    }}

    .case-itempartner-logo {{
      display: inline-flex !important;
      align-items: center !important;
      gap: 8px !important;
      min-width: 0 !important;
    }}

    .case-itempartner-logo .image-1040 {{
      width: 14px !important;
      height: 14px !important;
      display: inline-block !important;
      flex-shrink: 0 !important;
    }}

    .case-partner-badge-text {{
      font-family: 'Roboto Mono', monospace !important;
      font-size: 11px !important;
      font-weight: 600 !important;
      color: #00e5ff !important;
      letter-spacing: 0.06em !important;
      text-transform: uppercase !important;
      background: rgba(0, 229, 255, 0.08) !important;
      border: 1px solid rgba(0, 229, 255, 0.2) !important;
      padding: 3px 8px !important;
      border-radius: 4px !important;
      white-space: nowrap !important;
    }}

    .case-category-label {{
      font-family: 'Inter', sans-serif !important;
      font-size: 12px !important;
      color: #94a3b8 !important;
      font-weight: 500 !important;
      white-space: nowrap !important;
      overflow: hidden !important;
      text-overflow: ellipsis !important;
      min-width: 0 !important;
    }}

    .case-item-image-wrapper {{
      position: relative !important;
      width: 100% !important;
      min-width: 0 !important;
      max-width: 100% !important;
      aspect-ratio: 16 / 9 !important;
      border-radius: 10px !important;
      overflow: hidden !important;
      margin-bottom: 18px !important;
      background: #0d0f15 !important;
      border: 1px solid rgba(255, 255, 255, 0.06) !important;
      box-sizing: border-box !important;
      padding-left: 0 !important;
      padding-right: 0 !important;
    }}

    .case-item-image-wrapper .article-thumb.case-item-thmb {{
      margin: 0 !important;
      padding: 0 !important;
      width: 100% !important;
      height: 100% !important;
    }}

    .case-item-image-wrapper .article-thumb-link {{
      display: block !important;
      width: 100% !important;
      height: 100% !important;
    }}

    .case-item-image-wrapper .article-thumb-img {{
      width: 100% !important;
      height: 100% !important;
      object-fit: cover !important;
      object-position: top center !important;
      display: block !important;
      transition: transform 0.4s ease !important;
    }}

    .case-card:hover .case-item-image-wrapper .article-thumb-img {{
      transform: scale(1.04) !important;
    }}

    .case-desc-wrap {{
      flex-grow: 1 !important;
      display: flex !important;
      flex-direction: column !important;
      margin-bottom: 18px !important;
      width: 100% !important;
      min-width: 0 !important;
      box-sizing: border-box !important;
    }}

    .case-item-title-link {{
      text-decoration: none !important;
      display: block !important;
      margin-bottom: 8px !important;
      margin-left: 0 !important;
      margin-right: 0 !important;
      width: 100% !important;
      min-width: 0 !important;
    }}

    .case-desc-wrap .article-title {{
      font-size: 17px !important;
      line-height: 1.4 !important;
      font-weight: 700 !important;
      color: #ffffff !important;
      margin: 0 !important;
      transition: color 0.2s ease !important;
      overflow-wrap: break-word !important;
      word-break: break-word !important;
      min-width: 0 !important;
    }}

    .case-card:hover .article-title {{
      color: #00e5ff !important;
    }}

    .case-item-summary {{
      color: #94a3b8 !important;
      font-size: 13.5px !important;
      line-height: 1.55 !important;
      margin: 0 !important;
      display: -webkit-box !important;
      -webkit-line-clamp: 2 !important;
      -webkit-box-orient: vertical !important;
      overflow: hidden !important;
      overflow-wrap: break-word !important;
      word-break: break-word !important;
      min-width: 0 !important;
    }}

    .case-item-footer {{
      display: grid !important;
      grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
      gap: 12px !important;
      padding-top: 16px !important;
      margin-top: auto !important;
      margin-left: 0 !important;
      margin-right: 0 !important;
      border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
      width: 100% !important;
      min-width: 0 !important;
      box-sizing: border-box !important;
    }}

    .case-metric-block {{
      text-align: left !important;
      padding: 2px 0 !important;
      min-width: 0 !important;
      overflow: hidden !important;
      box-sizing: border-box !important;
    }}

    .caseitem-footer-text {{
      font-family: 'Roboto Mono', monospace !important;
      font-size: 14.5px !important;
      font-weight: 700 !important;
      color: #00ffa3 !important;
      line-height: 1.3 !important;
      overflow-wrap: break-word !important;
      word-break: break-word !important;
    }}

    .caseitem-footer-subtext {{
      font-size: 11px !important;
      color: #64748b !important;
      margin-top: 3px !important;
      text-transform: uppercase !important;
      letter-spacing: 0.04em !important;
      line-height: 1.3 !important;
      overflow-wrap: break-word !important;
      word-break: break-word !important;
    }}

    .case-card-actions-bar {{
      display: flex !important;
      align-items: center !important;
      justify-content: space-between !important;
      margin-top: 16px !important;
      padding-top: 14px !important;
      border-top: 1px dashed rgba(255, 255, 255, 0.07) !important;
      font-size: 12.5px !important;
      font-weight: 600 !important;
      width: 100% !important;
      min-width: 0 !important;
      box-sizing: border-box !important;
    }}

    .case-action-view {{
      color: #00e5ff !important;
      text-decoration: none !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 4px !important;
      transition: color 0.2s, transform 0.2s !important;
      min-width: 0 !important;
      white-space: nowrap !important;
    }}

    .case-action-view:hover {{
      color: #ffffff !important;
      transform: translateX(3px) !important;
    }}

    .case-action-live {{
      color: #94a3b8 !important;
      text-decoration: none !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 4px !important;
      transition: color 0.2s, transform 0.2s !important;
      min-width: 0 !important;
      white-space: nowrap !important;
    }}

    .case-action-live:hover {{
      color: #ffffff !important;
      transform: translateY(-2px) !important;
    }}

    /* Category Filter Pills */
    .filter-pills-container {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 20px;
      align-items: center;
    }}

    .category-filter-pill {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #94a3b8;
      font-size: 13px;
      font-weight: 600;
      padding: 7px 16px;
      border-radius: 9999px;
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: 'Inter', sans-serif;
    }}

    .category-filter-pill:hover {{
      background: rgba(255, 255, 255, 0.08);
      color: #ffffff;
      border-color: rgba(255, 255, 255, 0.2);
    }}

    .category-filter-pill.is-active {{
      background: linear-gradient(135deg, rgba(0, 229, 255, 0.15) 0%, rgba(122, 0, 223, 0.15) 100%);
      border-color: #00e5ff;
      color: #00e5ff;
      box-shadow: 0 0 12px rgba(0, 229, 255, 0.2);
    }}

    .filter-search-block {{
      position: relative;
      width: 100%;
    }}

    .filter-search-field {{
      width: 100%;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.09);
      border-radius: 8px;
      color: #ffffff;
      padding: 12px 16px 12px 42px;
      font-size: 14px;
      outline: none;
      transition: border-color 0.2s;
    }}

    .filter-search-field:focus {{
      border-color: #00e5ff;
      box-shadow: 0 0 0 1px #00e5ff;
    }}

    .filter-search-icon {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      pointer-events: none;
      z-index: 2;
    }}

    .no-results-msg {{
      display: none;
      text-align: center;
      padding: 60px 20px;
      color: #64748b;
      font-size: 15px;
    }}
  </style>
</head>
<body class="landing-body page-ready">

  {template_header}

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
          <div class="landing-hero-title-wrapper landing-column section-head-cols">
            <div class="section-heading" style="display:none;"><div class="section-heading-dot"></div></div>
            <div class="landing-badge-pill section-title-bordered">CLIENT PORTFOLIO &amp; CASE STUDIES</div>
            <h1 class="landing-ai-alerts-heading">
              Proven Platforms. <br/><span class="gradient-cyan-purple">Production-Grade Craft.</span>
            </h1>
            <div class="landing-hero-description landing-hero-column">
              Explore Vector Studioz' portfolio of 15 production client digital platforms, bespoke e-commerce engines, WebGL 3D interactive experiences, and full-stack SaaS systems built for global leaders.
            </div>
            <div class="landing-hero-button-wrapper landing-hero-column landing-mobile-hidden" style="display:flex;gap:12px;margin-top:28px;">
              <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="#projects-grid-list">
                <div class="btn-primary-wrapper" data-scramble-text="">
                  <div class="btn-primary-text-3" scramble-text="">Explore Projects &darr;</div>
                </div>
              </a>
              <a class="btn-secondary-4 w-inline-block" href="contact-us.html">
                <div class="btn-secondary-4-wrapper">
                  <div class="btn-secondary-text-4" scramble-text="">Start a Project</div>
                </div>
              </a>
            </div>
          </div>

          <!-- Right Column: Native Webflow 3D Video Asset -->
          <div class="landing-hero-asset-wrapper hero-column">
            <div class="hero-assets-container w-embed">
              <video autoplay="" class="landing-hero-asset landing-hero-column" loop="" muted="" playsinline="">
                <source src="https://static.vectorstudioz.com/assets/Videos/ai-chatbot.mp4" type="video/mp4; codecs=hvc1"/>
                <source src="https://static.vectorstudioz.com/assets/Videos/ai-chatbot.webm" type="video/webm"/>
              </video>
            </div>
          </div>
        </div>

        <!-- Hero Features Bar -->
        <div class="landing-hero-features">
          <div class="landing-section-border landing-border-top"></div>
          <div class="landing-section-border"></div>
          <div class="landing-hero-features-list">
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">15 Production Case Studies</div>
            </div>
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">100% Live Verified Deployments</div>
            </div>
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">Bespoke Design &amp; Architecture</div>
            </div>
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">Enterprise Performance Guarantee</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Webflow Articles / Projects Grid Section -->
    <section class="articles-section">
      <div class="container">
        <div class="articles-wrap">
          <div class="container-middle">
            <div class="filters-panel">
              <div class="filters-form w-form">
                <div class="filter-search-wrap">
                  <div class="filter-search-row" style="position:relative;">
                    <div class="filter-search-icon">
                      <img src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/65b3cad635601f2303e34110_Search.svg" loading="lazy" alt="" class="filter-search-icon-image" width="18" height="18"/>
                    </div>
                    <div class="filter-search-block">
                      <input class="filter-search-field w-input" id="projects-search-input" placeholder="Search client projects, stacks, industries..." type="text"/>
                    </div>
                  </div>
                </div>

                <div class="filter-pills-container">
                  <button type="button" class="category-filter-pill is-active" data-filter="all">All Work (15)</button>
                  <button type="button" class="category-filter-pill" data-filter="web-design">Web Design &amp; UX</button>
                  <button type="button" class="category-filter-pill" data-filter="e-commerce">E-Commerce</button>
                  <button type="button" class="category-filter-pill" data-filter="saas--cloud">SaaS &amp; Cloud</button>
                  <button type="button" class="category-filter-pill" data-filter="edtech">EdTech &amp; LMS</button>
                  <button type="button" class="category-filter-pill" data-filter="operations">Operations &amp; Portals</button>
                </div>
              </div>
            </div>

            <!-- Dynamic Project Cards Grid -->
            <div class="w-dyn-list" style="margin-top: 40px;">
              <div fs-cmsfilter-element="list" role="list" class="articles-list w-dyn-items" id="projects-grid-list">
                {rendered_cards}
              </div>
              <div id="no-projects-found" class="no-results-msg">
                No client projects matched your search criteria. Try a different keyword or reset categories.
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section: Webflow Closing CTA Banner -->
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

  {template_footer}

  <!-- Scripts -->
  <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
  <script src="vector-nav.js"></script>
  <script>
    // Real-time client-side filter and search
    document.addEventListener('DOMContentLoaded', function() {{
      const searchInput = document.getElementById('projects-search-input');
      const filterPills = document.querySelectorAll('.category-filter-pill');
      const cards = document.querySelectorAll('#projects-grid-list .articles-item');
      const noResults = document.getElementById('no-projects-found');

      let currentFilter = 'all';
      let currentQuery = '';

      function filterCards() {{
        let visibleCount = 0;
        cards.forEach(card => {{
          const cardCat = card.getAttribute('data-category-slug') || '';
          const cardText = card.textContent.toLowerCase();

          const matchesCat = (currentFilter === 'all') || (cardCat === currentFilter);
          const matchesQuery = !currentQuery || cardText.includes(currentQuery);

          if (matchesCat && matchesQuery) {{
            card.style.display = '';
            visibleCount++;
          }} else {{
            card.style.display = 'none';
          }}
        }});

        if (noResults) {{
          noResults.style.display = visibleCount === 0 ? 'block' : 'none';
        }}
      }}

      filterPills.forEach(pill => {{
        pill.addEventListener('click', function() {{
          filterPills.forEach(p => p.classList.remove('is-active'));
          this.classList.add('is-active');
          currentFilter = this.getAttribute('data-filter') || 'all';
          filterCards();
        }});
      }});

      if (searchInput) {{
        searchInput.addEventListener('input', function() {{
          currentQuery = this.value.trim().toLowerCase();
          filterCards();
        }});
      }}
    }});
  </script>
</body>
</html>
'''

    # Write projects.html
    with open('projects.html', 'w', encoding='utf-8') as f:
        f.write(page_html)
    print("Successfully built projects.html (Webflow Architecture Replica)")

    # Synchronize case-studies.html for backwards compatibility
    with open('case-studies.html', 'w', encoding='utf-8') as f:
        f.write(page_html)
    print("Successfully synchronized case-studies.html")

if __name__ == '__main__':
    build_projects_catalog()
