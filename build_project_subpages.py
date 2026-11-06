"""
Builds 15 dedicated standalone HTML subpages inside projects/<slug>.html
for Vector Studioz client showcase platforms.
"""
import os
from projects_data import PROJECTS_LIST

OUTPUT_DIR = 'projects'

with open('template_header.html', 'r', encoding='utf-8') as f:
    raw_header = f.read().strip()
with open('template_footer.html', 'r', encoding='utf-8') as f:
    raw_footer = f.read().strip()

def adapt_for_subpage(html_str):
    pages = [
        'index.html', 'projects.html', 'about.html', 'careers.html', 'contact-us.html',
        'blog.html', 'brand-kit.html', 'videos.html', 'privacy-policy.html', 'tos.html',
        'cookies.html', 'web-design.html', 'webgl-3d.html', 'web-development.html',
        'software-engineering.html', 'ai-automation.html', 'mobile-development.html'
    ]
    res = html_str
    for p in pages:
        res = res.replace(f'href="{p}"', f'href="../{p}"')
    return res

sub_header = adapt_for_subpage(raw_header)
sub_footer = adapt_for_subpage(raw_footer)

os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_subpage(project, prev_project, next_project):
    slug = project['slug']
    title = project['title']
    short_title = project['short_title']
    client = project['client']
    category = project['category']
    industry = project['industry']
    year = project['year']
    live_url = project['live_url']
    thumbnail = project['thumbnail'].lstrip('/')
    if not thumbnail.startswith('../'):
        thumbnail = f"../{thumbnail}"
    tagline = project['tagline']
    badge = project.get('badge', 'Production Showcase')
    metrics = project['metrics']
    overview = project['overview']
    challenge = project['challenge']
    solution = project['solution']
    tech_stack = project['tech_stack']
    testimonial = project.get('testimonial', {
        'quote': 'Vector Studioz executed our vision with exceptional design precision, technical speed, and measurable impact.',
        'author': 'Executive Leadership',
        'role': client
    })

    # Tech stack pills
    tech_pills = ''.join([f'<span class="vs-tech-pill">{tech}</span>' for tech in tech_stack])

    # Metrics HTML
    metrics_html = ''.join([f'''
        <div class="project-stat-card item-50" block-corners-top="">
            <div class="project-stat-val">{m['value']}</div>
            <div class="project-stat-lbl">{m['label']}</div>
            <div block-corners-bottom=""></div>
        </div>
    ''' for m in metrics])

    # Cross navigation
    prev_link = f'{prev_project["slug"]}.html'
    prev_name = prev_project["short_title"]
    next_link = f'{next_project["slug"]}.html'
    next_name = next_project["short_title"]

    html = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{title} | Vector Studioz Projects</title>
  <meta name="description" content="{overview[:160]}..."/>
  <meta property="og:title" content="{title} | Vector Studioz"/>
  <meta property="og:description" content="{overview[:160]}..."/>
  <meta property="og:image" content="{thumbnail}"/>
  <meta property="og:type" content="website"/>
  <link rel="canonical" href="https://www.vectorstudioz.com/projects/{slug}.html"/>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;700;800&family=Roboto+Mono:wght@400;500;600&display=swap" rel="stylesheet"/>

  <!-- Global Vector Studioz Styling -->
  <!-- Core Webflow & Component Stylesheet -->
  <link crossorigin="anonymous" href="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/css/chain-gpt.shared.a3558708c.min.css" integrity="sha384-o1WHCMrnJbbS0LfUpKSZppAv4pAvYlNYeJKbMRQ8arxTAWf4irz+ALXOnFDpslf+" rel="stylesheet" type="text/css"/>

  <!-- Global Vector Studioz Styling -->
  <link rel="stylesheet" href="../vector-nav.css"/>

  <style>
    :root {{
      --vs-bg: #07070a;
      --vs-card-bg: #0d0d14;
      --vs-card-border: rgba(255, 255, 255, 0.08);
      --vs-cyan: #00e5ff;
      --vs-purple: #7a00df;
      --vs-text-muted: #94a3b8;
    }}

    body {{
      background-color: var(--vs-bg);
      color: #f1f5f9;
      font-family: 'Inter', sans-serif;
      margin: 0;
      padding: 0;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }}

    .project-detail-hero {{
      padding: 130px 24px 50px;
      max-width: 1240px;
      margin: 0 auto;
    }}

    .project-breadcrumb {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 13px;
      color: var(--vs-text-muted);
      margin-bottom: 24px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-family: 'Roboto Mono', monospace;
    }}

    .project-breadcrumb a {{
      color: var(--vs-text-muted);
      text-decoration: none;
      transition: color 0.2s;
    }}

    .project-breadcrumb a:hover {{
      color: var(--vs-cyan);
    }}

    .project-meta-pills {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
    }}

    .project-category-badge {{
      background: rgba(0, 229, 255, 0.1);
      border: 1px solid rgba(0, 229, 255, 0.3);
      color: var(--vs-cyan);
      font-size: 12px;
      font-weight: 600;
      padding: 6px 14px;
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .project-year-badge {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--vs-card-border);
      color: #cbd5e1;
      font-size: 12px;
      font-weight: 500;
      padding: 6px 12px;
      border-radius: 9999px;
      font-family: 'Roboto Mono', monospace;
    }}

    .project-live-indicator {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      font-weight: 600;
      color: #10b981;
      background: rgba(16, 185, 129, 0.1);
      border: 1px solid rgba(16, 185, 129, 0.25);
      padding: 6px 14px;
      border-radius: 9999px;
    }}

    .live-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 10px #10b981;
      animation: pulseLive 2s infinite ease-in-out;
    }}

    @keyframes pulseLive {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.4; transform: scale(0.85); }}
    }}

    .project-main-title {{
      font-size: clamp(32px, 4.5vw, 56px);
      font-weight: 800;
      line-height: 1.15;
      margin: 0 0 18px;
      color: #ffffff;
      letter-spacing: -0.02em;
    }}

    .project-lead-tagline {{
      font-size: clamp(16px, 1.8vw, 22px);
      color: #94a3b8;
      max-width: 860px;
      margin: 0 0 32px;
      line-height: 1.5;
    }}

    .project-action-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 16px;
      margin-bottom: 40px;
    }}

    .btn-visit-live {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: linear-gradient(135deg, #00e5ff 0%, #7a00df 100%);
      color: #ffffff;
      font-size: 15px;
      font-weight: 700;
      padding: 14px 28px;
      border-radius: 9999px;
      text-decoration: none;
      transition: transform 0.2s, box-shadow 0.2s;
      box-shadow: 0 8px 24px rgba(0, 229, 255, 0.25);
    }}

    .btn-visit-live:hover {{
      transform: translateY(-2px);
      box-shadow: 0 12px 30px rgba(0, 229, 255, 0.4);
    }}

    .btn-all-projects {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--vs-card-border);
      color: #e2e8f0;
      font-size: 14px;
      font-weight: 600;
      padding: 14px 24px;
      border-radius: 9999px;
      text-decoration: none;
      transition: background 0.2s, border-color 0.2s;
    }}

    .btn-all-projects:hover {{
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.25);
    }}

    /* 16:9 Cinematic Media Container */
    .project-hero-media {{
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 9;
      min-height: 320px;
      border-radius: 20px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.6);
      margin-bottom: 50px;
      background: #0d0d14;
    }}

    .project-hero-media img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s ease;
    }}

    .project-hero-media:hover img {{
      transform: scale(1.02);
    }}

    /* Stats Grid */
    .project-stats-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 20px;
      margin-bottom: 60px;
    }}

    [block-corners-top],
    [block-corners-bottom] {{
      position: relative;
    }}
    [block-corners-top]:before,
    [block-corners-top]:after {{
      content: '';
      position: absolute;
      width: 22px;
      height: 22px;
      background-color: var(--vs-bg);
      z-index: 1;
    }}
    [block-corners-top]:before {{
      top: -11px;
      left: -13px;
      transform: rotate(45deg);
      border-right: 1px solid rgba(255, 255, 255, 0.12);
    }}
    [block-corners-top]:after {{
      top: -11px;
      right: -13px;
      transform: rotate(-45deg);
      border-left: 1px solid rgba(255, 255, 255, 0.12);
    }}
    [block-corners-bottom]:before,
    [block-corners-bottom]:after {{
      content: '';
      position: absolute;
      width: 22px;
      height: 22px;
      background-color: var(--vs-bg);
      z-index: 1;
    }}
    [block-corners-bottom]:before {{
      bottom: -11px;
      left: -13px;
      transform: rotate(45deg);
      border-top: 1px solid rgba(255, 255, 255, 0.12);
    }}
    [block-corners-bottom]:after {{
      bottom: -11px;
      right: -13px;
      transform: rotate(-45deg);
      border-top: 1px solid rgba(255, 255, 255, 0.12);
    }}

    .project-stat-card {{
      background: var(--vs-card-bg);
      border: 1px solid var(--vs-card-border);
      border-radius: 16px;
      padding: 24px 28px;
      position: relative;
      transition: border-color 0.2s, transform 0.2s;
    }}

    .project-stat-card:hover {{
      border-color: rgba(0, 229, 255, 0.3);
      transform: translateY(-2px);
    }}

    .project-stat-val {{
      font-size: 36px;
      font-weight: 800;
      background: linear-gradient(135deg, #ffffff 0%, #00e5ff 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 6px;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }}

    .project-stat-lbl {{
      font-size: 13px;
      color: var(--vs-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      font-family: 'Roboto Mono', monospace;
    }}

    /* Main Content Two-Column Layout */
    .project-narrative-grid {{
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 40px;
      margin-bottom: 80px;
    }}

    @media (max-width: 991px) {{
      .project-narrative-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .narrative-col-main {{
      display: flex;
      flex-direction: column;
      gap: 44px;
    }}

    .narrative-section-card {{
      background: var(--vs-card-bg);
      border: 1px solid var(--vs-card-border);
      border-radius: 18px;
      padding: 36px;
    }}

    .narrative-section-num {{
      font-size: 12px;
      font-family: 'Roboto Mono', monospace;
      color: var(--vs-cyan);
      margin-bottom: 8px;
      letter-spacing: 0.1em;
    }}

    .narrative-section-heading {{
      font-size: 24px;
      font-weight: 700;
      color: #ffffff;
      margin: 0 0 16px;
      letter-spacing: -0.01em;
    }}

    .narrative-body-text {{
      font-size: 16px;
      color: #cbd5e1;
      line-height: 1.75;
      margin: 0;
    }}

    .project-testimonial-card {{
      background: linear-gradient(135deg, rgba(13, 13, 20, 0.9) 0%, rgba(20, 16, 32, 0.9) 100%);
      border: 1px solid rgba(122, 0, 223, 0.3);
      border-radius: 18px;
      padding: 36px;
      position: relative;
    }}

    .project-testimonial-quote {{
      font-size: 18px;
      font-style: italic;
      color: #f1f5f9;
      line-height: 1.6;
      margin-bottom: 20px;
    }}

    .project-testimonial-author {{
      font-size: 14px;
      font-weight: 700;
      color: var(--vs-cyan);
    }}

    .project-testimonial-role {{
      font-size: 12px;
      color: var(--vs-text-muted);
    }}

    /* Sidebar Column */
    .narrative-col-side {{
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}

    .sidebar-widget {{
      background: var(--vs-card-bg);
      border: 1px solid var(--vs-card-border);
      border-radius: 18px;
      padding: 28px;
    }}

    .sidebar-widget-title {{
      font-size: 14px;
      font-weight: 700;
      color: #ffffff;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin: 0 0 20px;
      font-family: 'Roboto Mono', monospace;
      padding-bottom: 12px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }}

    .sidebar-dl {{
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .sidebar-dl-item {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .sidebar-dt {{
      font-size: 11px;
      color: var(--vs-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      font-family: 'Roboto Mono', monospace;
    }}

    .sidebar-dd {{
      font-size: 15px;
      font-weight: 600;
      color: #f1f5f9;
    }}

    .vs-tech-pill {{
      display: inline-block;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #e2e8f0;
      font-size: 12px;
      font-weight: 500;
      padding: 6px 12px;
      border-radius: 8px;
      margin: 4px 4px 4px 0;
    }}

    /* Cross Navigation Bar */
    .project-cross-nav {{
      background: var(--vs-card-bg);
      border-top: 1px solid var(--vs-card-border);
      border-bottom: 1px solid var(--vs-card-border);
      padding: 24px 0;
      margin-bottom: 80px;
    }}

    .project-cross-nav-inner {{
      max-width: 1240px;
      margin: 0 auto;
      padding: 0 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .cross-nav-item {{
      text-decoration: none;
      color: #cbd5e1;
      display: flex;
      flex-direction: column;
      gap: 4px;
      transition: color 0.2s;
    }}

    .cross-nav-item:hover {{
      color: var(--vs-cyan);
    }}

    .cross-nav-dir {{
      font-size: 11px;
      color: var(--vs-text-muted);
      text-transform: uppercase;
      font-family: 'Roboto Mono', monospace;
      letter-spacing: 0.08em;
    }}

    .cross-nav-title {{
      font-size: 16px;
      font-weight: 700;
    }}

    .cross-nav-center {{
      text-align: center;
    }}

    .btn-center-projects {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: var(--vs-cyan);
      text-decoration: none;
      font-size: 13px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-family: 'Roboto Mono', monospace;
      padding: 8px 16px;
      border-radius: 9999px;
      background: rgba(0, 229, 255, 0.08);
      border: 1px solid rgba(0, 229, 255, 0.2);
      transition: background 0.2s;
    }}

    .btn-center-projects:hover {{
      background: rgba(0, 229, 255, 0.16);
    }}

    /* Global Call To Action Banner */
    .project-cta-banner {{
      max-width: 1240px;
      margin: 0 auto 100px;
      padding: 60px 40px;
      background: radial-gradient(circle at top left, rgba(0, 229, 255, 0.12), transparent 70%),
                  radial-gradient(circle at bottom right, rgba(122, 0, 223, 0.15), transparent 70%),
                  #0c0c14;
      border: 1px solid rgba(0, 229, 255, 0.2);
      border-radius: 24px;
      text-align: center;
      position: relative;
      overflow: hidden;
    }}

    .cta-banner-h2 {{
      font-size: clamp(28px, 3.5vw, 44px);
      font-weight: 800;
      color: #ffffff;
      margin: 0 0 16px;
      letter-spacing: -0.02em;
    }}

    .cta-banner-p {{
      font-size: 17px;
      color: #94a3b8;
      max-width: 600px;
      margin: 0 auto 32px;
      line-height: 1.6;
    }}
  </style>
</head>
<body class="home-page landing-body">

  {sub_header}

  <!-- Main Subpage Body -->
  <main id="main-content">
    <article class="project-detail-hero">
      
      <!-- Breadcrumb -->
      <nav class="project-breadcrumb" aria-label="Breadcrumb">
        <a href="../index.html">Vector Studioz</a>
        <span>/</span>
        <a href="../projects.html">Projects</a>
        <span>/</span>
        <span style="color:#ffffff;">{short_title}</span>
      </nav>

      <!-- Meta Badges -->
      <div class="project-meta-pills">
        <span class="project-category-badge">{category}</span>
        <span class="project-year-badge">{year}</span>
        <span class="project-live-indicator">
          <span class="live-dot"></span> Live Production
        </span>
      </div>

      <!-- Main Headline -->
      <h1 class="project-main-title">{title}</h1>
      <p class="project-lead-tagline">{tagline}</p>

      <!-- Action Row -->
      <div class="project-action-row">
        <a href="{live_url}" class="btn-visit-live" target="_blank" rel="noopener noreferrer">
          Visit Live Website ↗
        </a>
        <a href="../projects.html" class="btn-all-projects">
          ← Back to All Projects
        </a>
      </div>

      <!-- 16:9 Showcase Thumbnail Media -->
      <div class="project-hero-media">
        <img src="{thumbnail}" alt="{title}" loading="lazy"/>
      </div>

      <!-- Impact Metrics -->
      <section class="project-stats-grid" aria-label="Key Performance Results">
        {metrics_html}
      </section>

      <!-- Two-Column Case Narrative -->
      <div class="project-narrative-grid">
        <div class="narrative-col-main">
          
          <!-- 01 Overview -->
          <div class="narrative-section-card item-50" block-corners-top="">
            <div class="narrative-section-num">01 / OVERVIEW</div>
            <h2 class="narrative-section-heading">Project Scope &amp; Mission</h2>
            <p class="narrative-body-text">{overview}</p>
            <div block-corners-bottom=""></div>
          </div>

          <!-- 02 Challenge -->
          <div class="narrative-section-card item-50" block-corners-top="">
            <div class="narrative-section-num">02 / THE CHALLENGE</div>
            <h2 class="narrative-section-heading">Strategic Roadblocks &amp; Friction Points</h2>
            <p class="narrative-body-text">{challenge}</p>
            <div block-corners-bottom=""></div>
          </div>

          <!-- 03 Solution -->
          <div class="narrative-section-card item-50" block-corners-top="">
            <div class="narrative-section-num">03 / THE SOLUTION</div>
            <h2 class="narrative-section-heading">Engineering Architecture &amp; Delivery</h2>
            <p class="narrative-body-text">{solution}</p>
            <div block-corners-bottom=""></div>
          </div>

          <!-- Testimonial Quote -->
          <div class="project-testimonial-card item-50" block-corners-top="">
            <div class="project-testimonial-quote">"{testimonial['quote']}"</div>
            <div class="project-testimonial-author">{testimonial['author']}</div>
            <div class="project-testimonial-role">{testimonial['role']}</div>
            <div block-corners-bottom=""></div>
          </div>

        </div>

        <!-- Sidebar Meta -->
        <aside class="narrative-col-side" aria-label="Project Metadata">
          
          <div class="sidebar-widget">
            <div class="sidebar-widget-title">Project Details</div>
            <div class="sidebar-dl">
              <div class="sidebar-dl-item">
                <span class="sidebar-dt">Client</span>
                <span class="sidebar-dd">{client}</span>
              </div>
              <div class="sidebar-dl-item">
                <span class="sidebar-dt">Industry</span>
                <span class="sidebar-dd">{industry}</span>
              </div>
              <div class="sidebar-dl-item">
                <span class="sidebar-dt">Year Delivered</span>
                <span class="sidebar-dd">{year}</span>
              </div>
              <div class="sidebar-dl-item">
                <span class="sidebar-dt">Scope of Work</span>
                <span class="sidebar-dd">{category}</span>
              </div>
            </div>
          </div>

          <div class="sidebar-widget">
            <div class="sidebar-widget-title">Technologies Deployed</div>
            <div style="margin-top: 10px;">
              {tech_pills}
            </div>
          </div>

          <div class="sidebar-widget" style="background: radial-gradient(circle at top right, rgba(0, 229, 255, 0.08), transparent 70%), #0d0d14;">
            <div class="sidebar-widget-title">Live URL</div>
            <p style="font-size: 13px; color: #94a3b8; margin: 0 0 16px; word-break: break-all;">
              {live_url}
            </p>
            <a href="{live_url}" class="btn-visit-live" style="width: 100%; box-sizing: border-box; justify-content: center; padding: 12px 20px; font-size: 14px;" target="_blank" rel="noopener noreferrer">
              Open Live Site ↗
            </a>
          </div>

        </aside>
      </div>

    </article>

    <!-- Cross Navigation Bar -->
    <nav class="project-cross-nav" aria-label="Project Navigation">
      <div class="project-cross-nav-inner">
        <a href="{prev_link}" class="cross-nav-item">
          <span class="cross-nav-dir">← Previous Project</span>
          <span class="cross-nav-title">{prev_name}</span>
        </a>

        <div class="cross-nav-center">
          <a href="../projects.html" class="btn-center-projects">
            All 15 Projects
          </a>
        </div>

        <a href="{next_link}" class="cross-nav-item" style="text-align: right;">
          <span class="cross-nav-dir">Next Project →</span>
          <span class="cross-nav-title">{next_name}</span>
        </a>
      </div>
    </nav>

    <!-- Section: Webflow Closing CTA Banner -->
    <section class="landing-cta landing-cta-with-desc" style="margin-top: 80px;">
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
              <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="../contact-us.html">
                <div class="btn-primary-wrapper" data-scramble-text="">
                  <div class="btn-primary-text-3" scramble-text="">Schedule Discovery Call &rarr;</div>
                </div>
              </a>
              <a class="btn-secondary-4 w-inline-block" href="../projects.html">
                <div class="btn-secondary-4-wrapper">
                  <div class="btn-secondary-text-4" scramble-text="">Browse All Projects</div>
                </div>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

  </main>

  {sub_footer}

  <script src="../vector-nav.js"></script>

</body>
</html>
'''
    return html

def build_all():
    total = len(PROJECTS_LIST)
    for i, p in enumerate(PROJECTS_LIST):
        prev_p = PROJECTS_LIST[(i - 1) % total]
        next_p = PROJECTS_LIST[(i + 1) % total]
        html = generate_subpage(p, prev_p, next_p)
        out_path = os.path.join(OUTPUT_DIR, f"{p['slug']}.html")
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Generated standalone project subpage: {out_path}")

if __name__ == '__main__':
    build_all()
