"""
build_all_service_pages.py
Compiles all 6 Vector Studioz Agency Service Pages using the exact canonical
11-section Webflow landing page layout template from web3-chatbot.html (matching company pages).

Sections (11 total):
0: landing-hero-2 (hero columns, hero-assets-container video, landing-hero-features)
1: landing-why (4 item-50 cards with corner cuts & gradient icons)
2: landing-features (feature items with mobile nav, dot list, and banner screenshots)
3: landing-who-for (4 cards with title block and corner lines)
4: landing-why (second 4-card item-50 grid matching Webflow layout)
5: landing-hiw (4 numbered steps in clean 2x2 grid)
6: landing-comparison (3-column Webflow comparison table)
7: landing-launch (single full-width glow CTA bar with action button)
8: landing-group (2 large side-by-side comparison/channel cards)
9: landing-faq (Webflow split FAQ layout with interactive accordions)
10: landing-cta (large CTA banner with 3D robot/aura asset and action buttons)

Services:
1. web-design.html (Bespoke UI/UX & Design Systems) -> mirrors to ai-agents.html
2. webgl-3d.html (3D & WebGL Studio) -> mirrors to web3-chatbot.html
3. web-development.html (Full-Stack Web Development) -> mirrors to ai-trading-assistant.html
4. software-engineering.html (Custom Software & Systems Engineering) -> mirrors to smart-contract-auditor.html
5. ai-automation.html (Autonomous AI Workflows & Agents) -> mirrors to crypto-ai-hub.html
6. mobile-development.html (Mobile App Development) -> mirrors to smart-contract-generator.html
"""

import os

with open('template_header.html', 'r', encoding='utf-8') as f:
    HEADER_HTML = f.read().strip()

with open('template_footer.html', 'r', encoding='utf-8') as f:
    FOOTER_HTML = f.read().strip()

def get_service_head(title, description, canonical_url):
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

      const firstItem = document.querySelector('.landing-faq-question-item');
      if (firstItem) {
        const a = firstItem.querySelector('.landing-faq-answer-wrapper');
        const ic = firstItem.querySelector('.landing-faq-question-icon');
        if (a) a.style.height = 'auto';
        if (ic) ic.style.transform = 'rotate(45deg)';
      }
    });
  </script>"""

SERVICES_CONFIG = [
    {
        'clean_file': 'web-design.html',
        'legacy_file': 'ai-agents.html',
        'title': 'Bespoke UI/UX & Web Design Studio | Vector Studioz',
        'description': 'Elevate your brand with bespoke digital design systems, high-converting product interfaces, and interactive prototypes built by Vector Studioz.',
        'canonical_url': 'https://www.vectorstudioz.com/web-design.html',
        'badge': 'BESPOKE UI/UX & DESIGN SYSTEMS',
        'hero_h1': 'Radical Aesthetic Craft. <br/><span class="gradient-cyan-purple">Conversion-Driven UX.</span>',
        'hero_desc': 'Vector Studioz crafts category-defining design systems, responsive web flagships, and intuitive digital product interfaces. We merge striking visual emotion with behavioral psychology to command market leadership.',
        'video_mp4': 'https://static.vectorstudioz.com/assets/Videos/ai-chatbot.mp4',
        'video_webm': 'https://static.vectorstudioz.com/assets/Videos/ai-chatbot.webm',
        'features_bar': [
            'Figma Multi-Tier Tokens',
            'Fluid 60fps Micro-Interactions',
            'Conversion-Tested Wireframes',
            'Full Design System Handover'
        ],
        'why1_title': 'Why Leading Brands Choose Our Design Studio',
        'why1_cards': [
            ('First-Principles Visual Craft', 'We never touch cookie-cutter frameworks. Every typography pair, layout hierarchy, and color palette is tailored to make your brand distinct.', 'Custom responsive component architectures that elevate your digital presence.'),
            ('Atomic Design Token Systems', 'Modular Figma systems engineered with variables and semantic tokens, ensuring lightning-fast developer handoff and zero style drift.', 'Comprehensive style guides covering states, responsive scales, and accessible contrasts.'),
            ('Interactive Motion Prototypes', 'Realistic clickable prototypes with micro-interactions, gesture mechanics, and spring physics validated before engineering begins.', 'Eliminate guessing with user-tested prototypes that establish exact interaction fidelity.'),
            ('Conversion Rate Optimization', 'Data-informed information architecture designed to eliminate user cognitive friction and maximize conversion rates.', 'Strategic layout framing that turns casual visitors into high-value clients.')
        ],
        'features_section_title': 'Design Disciplines & Specialized Deliverables',
        'features_section_desc': 'From early conceptual explorations to enterprise design token libraries, our studio delivers end-to-end design excellence.',
        'features_items': [
            ('01', '02', 'Responsive Design Flagships', 'Translating strategic brand visions into high-impact digital flagships that convert visitors.', 'Pixel-perfect mobile, tablet, and ultra-wide desktop layouts with fluid viewport scaling.', 'WCAG 2.1 AA accessibility compliance across contrast ratios and navigation hierarchies.', 'images/features/vector-design-system.png'),
            ('02', '02', 'SaaS & Web Application Interfaces', 'Intuitive multi-step dashboards, real-time data visualizers, and complex transactional workflows.', 'Streamlined onboarding flows, modular component states, and dense information hierarchies.', 'Designed for enterprise performance and rapid user task completion.', 'images/features/vector-fullstack-telemetry.png')
        ],
        'who_for_title': 'Who Our Web Design Studio Is Built For',
        'who_for_cards': [
            ('High-Growth Tech Startups', 'Establish immediate category dominance before Series A/B fundraising rounds with a flagship digital product.'),
            ('Digital Platform Pioneers', 'Differentiate from generic competitors with distinctive typography, dark-mode ergonomics, and immersive layouts.'),
            ('Enterprise Modernizers', 'Replace legacy corporate interfaces with fast, intuitive user experiences that empower your team.')
        ],
        'why2_title': 'Vector Studioz Standards vs Generic Templates',
        'why2_cards': [
            ('Handcrafted Exclusivity', 'Zero generic themes or drag-and-drop templates. Every vector, layer, and motion curve is created from scratch.'),
            ('Micro-Interaction Finesse', 'Refined button physics, subtle magnetic hovers, and smooth page transitions that create emotional delight.'),
            ('Design-to-Code Precision', 'Designed with clean auto-layout and semantic naming conventions for direct Next.js & Tailwind CSS alignment.'),
            ('Enterprise Scale Readiness', 'Design token libraries equipped to power multiple platform releases without design debt.')
        ],
        'hiw_title': 'Our 4-Stage Design Sprint Methodology',
        'hiw_desc': 'A collaborative, iterative sprint lifecycle ensuring rapid delivery with zero design ambiguity.',
        'hiw_steps': [
            ('Discovery & Visual Identity Audit', 'We align on brand narrative, competitive positioning, customer archetypes, and moodboards.'),
            ('Low-Fidelity UX Architecture', 'Information architecture mapping, user journey wireframes, and interactive low-fidelity clickable flows.'),
            ('High-Fidelity UI & Token Systems', 'Complete visual design with typography scales, color tokens, and responsive layout variations.'),
            ('Interactive Prototype & Handoff', 'High-fidelity clickable prototype, design token export, and direct pairing with frontend engineers.')
        ],
        'comparison_title': 'Vector Studioz Design vs Traditional Agencies',
        'comparison_rows': [
            ('Design Approach', 'Purchased templates & cookie-cutter assets', 'Handcrafted bespoke from first principles'),
            ('Communication', 'Slow account manager relays', 'Direct Slack with Principal UI/UX Designers'),
            ('Delivery Cadence', 'Multi-month opaque waiting cycles', 'Weekly iterative Figma walkthroughs & Looms'),
            ('Design Systems', 'Static style sheets & unorganized files', 'Production-grade Figma tokens & variables')
        ],
        'launch_title': 'Elevate your brand with category-defining design craft.',
        'group_title': 'Studio Design Principles vs Traditional Agency Models',
        'group_card1_title': 'Traditional Agency Pitfalls',
        'group_card1_bullets': [
            'Relying on off-the-shelf templates and predictable layout formulas.',
            'Opaque billing cycles with unexpected change order fees.',
            'Disjointed handoffs leaving developers to guess responsive states.'
        ],
        'group_card2_title': 'Vector Studioz Model',
        'group_card2_bullets': [
            'Bespoke aesthetics tailored specifically to your category positioning.',
            'Transparent sprint scopes with weekly prototype iterations.',
            'Complete production design system transfer with zero IP retention.'
        ],
        'faqs': [
            ('What deliverables are included with a UI/UX project?', 'You receive complete Figma source files, reusable component libraries with auto-layout, interactive prototypes, design token documentation, and exported production assets.'),
            ('How long does a typical web design sprint take?', 'A full flagship website design or product interface typically spans 3 to 6 weeks from initial discovery through final developer-ready design system delivery.'),
            ('Can our internal engineering team build from your designs easily?', 'Yes. We structure all Figma files using clean auto-layout, standard 8pt spacing grids, semantic color tokens, and strict naming conventions aligned with modern React/Tailwind CSS components.'),
            ('Do you also handle frontend engineering?', 'Yes. Vector Studioz offers end-to-end capabilities, seamlessly pairing our design team with our senior frontend engineering team.')
        ],
        'cta_title': 'Transform Your Digital Presence',
        'cta_desc': 'Schedule a 30-minute discovery session with our Principal Designers to explore how we can elevate your brand.',
        'cta_btn_text': 'Book Design Discovery &rarr;'
    },
    {
        'clean_file': 'webgl-3d.html',
        'legacy_file': 'web3-chatbot.html',
        'title': '3D & WebGL Studio | Vector Studioz',
        'description': 'Engineered interactive Three.js environments, GLSL shaders, and hardware-accelerated 3D spatial web experiences with 60fps performance.',
        'canonical_url': 'https://www.vectorstudioz.com/webgl-3d.html',
        'badge': 'INTERACTIVE SPATIAL WEB & 3D STUDIO',
        'hero_h1': 'Immersive 3D Graphics. <br/><span class="gradient-cyan-purple">Hardware-Accelerated WebGL.</span>',
        'hero_desc': 'Vector Studioz transforms standard browser viewports into unforgettable spatial playgrounds. Using Three.js, custom GLSL shaders, and procedural meshes, we craft silky 60fps web experiences that captivate audiences.',
        'video_mp4': 'https://static.vectorstudioz.com/assets/Videos/ai-chatbot.mp4',
        'video_webm': 'https://static.vectorstudioz.com/assets/Videos/ai-chatbot.webm',
        'features_bar': [
            'Silky 60fps Browser Rendering',
            'Draco Geometry Compression',
            'Custom GLSL Fragment Shaders',
            'Graceful Mobile 2D Fallbacks'
        ],
        'why1_title': 'Why Ambitious Brands Bring 3D to the Browser',
        'why1_cards': [
            ('Interactive Spatial Storytelling', 'Break free from flat 2D pages. Engage your audience with dynamic camera paths, lighting, and physics tied to scroll velocity.', 'Memorable visual experiences that elevate dwell time and brand prestige.'),
            ('Custom GLSL Fragment Shaders', 'Bespoke vertex and fragment shaders producing chromatic distortion, fluid liquid meshes, and holographic glows.', 'GPU-accelerated visual fidelity without unnecessary runtime CPU overhead.'),
            ('Draco Asset Compression', 'Blender and CAD models compressed with Draco geometry and KTX2 texture encoding for sub-2-second asset downloads.', 'High-detail 3D geometry running on lightweight web bundles under 2MB.'),
            ('Cross-Device GPU Optimization', 'Engineered to run buttery-smooth across iOS Safari, Android Chrome, and low-power laptops with dynamic DPI scaling.', 'Robust fallback rendering ensures every visitor experiences stunning visuals.')
        ],
        'features_section_title': 'WebGL Disciplines & Specialized Engineering',
        'features_section_desc': 'We bridge 3D spatial artistry with rigorous web optimization to build production-ready digital showpieces.',
        'features_items': [
            ('01', '02', 'Real-Time 3D Product Showcases', 'Interactive 3D configurators allowing users to inspect, orbit, and customize products in real time.', 'Photorealistic PBR materials, dynamic studio reflections, and exploded-view animations.', 'Directly integrated with web shopping carts and checkout flows.', 'images/features/vector-webgl-shader.png'),
            ('02', '02', 'Spatial Web Canvases & Shaders', 'Cinematic hero sections featuring procedural particle swarms, reactive fluid grids, and generative geometry.', 'Tied seamlessly into GSAP ScrollTrigger and React state trees.', 'Maintains strict 60fps hardware rendering with minimal battery drain.', 'images/features/vector-design-system.png')
        ],
        'who_for_title': 'Who Our 3D & WebGL Studio Is Built For',
        'who_for_cards': [
            ('Category-Defining Tech Startups', 'Stand out boldly in crowded markets with cinematic 3D visual storytelling that attracts attention.'),
            ('Premium Consumer & Hardware Brands', 'Let customers explore technical hardware, industrial design, and craftsmanship in 3D.'),
            ('Digital Agency Flagships', 'Showcase innovation and technical mastery with interactive spatial graphics.')
        ],
        'why2_title': 'Vector Studioz WebGL Standards vs Heavy 3D Sites',
        'why2_cards': [
            ('Sub-Second Time to Interactive', 'We optimize assets with Draco compression and progressive streaming so pages load instantly.'),
            ('Dynamic Resolution Scaling', 'Canvas resolution scales intelligently based on device GPU tier to maintain consistent frame rates.'),
            ('Zero Canvas Lockouts', 'Canvas interactions never trap the user or disrupt natural touch scrolling on mobile devices.'),
            ('Semantic DOM Integration', '3D scenes harmonize with semantic HTML typography for high search visibility and accessibility.')
        ],
        'hiw_title': 'Our 4-Stage 3D WebGL Production Roadmap',
        'hiw_desc': 'From Blender modeling to GPU shader optimization and 60fps browser validation.',
        'hiw_steps': [
            ('3D Concept & Topology Prep', 'We sculpt or import 3D models, clean topology, bake PBR textures, and apply Draco compression.'),
            ('GLSL Shader & Lighting Setup', 'Developing custom vertex/fragment shaders, configuring environment lighting, and bloom VFX.'),
            ('Interaction & Scroll Choreography', 'Binding canvas camera animations to cursor position, touch gestures, and scroll triggers.'),
            ('Mobile Benchmarking & Fallbacks', 'Testing across real iOS and Android devices, profiling draw calls, and configuring 2D fallbacks.')
        ],
        'comparison_title': 'Vector Studioz WebGL vs Heavy Freelance 3D',
        'comparison_rows': [
            ('Framerate Stability', 'Laggy 15-25fps with heavy battery drain', 'Guaranteed silky 60fps across mobile and desktop'),
            ('Asset Size', 'Uncompressed 30MB+ GLTF bundles', 'Sub-2MB Draco-compressed, progressively loaded assets'),
            ('Mobile Experience', 'Broken touch controls and overheating', 'Dynamic DPI scaling with responsive touch gestures'),
            ('DOM Choreography', 'Disconnected canvas blocking page content', 'Seamless sync between 3D camera and HTML typography')
        ],
        'launch_title': 'Bring cinematic dimension and visual drama to your digital flagship.',
        'group_title': 'Studio WebGL Principles vs Traditional 3D Approaches',
        'group_card1_title': 'Common 3D Web Pitfalls',
        'group_card1_bullets': [
            'Massive uncompressed files that make pages load sluggishly.',
            'Overheating mobile phones and draining batteries with unoptimized render loops.',
            'Ignoring graceful fallbacks for devices without high-end dedicated GPUs.'
        ],
        'group_card2_title': 'Vector Studioz Model',
        'group_card2_bullets': [
            'Draco mesh compression, KTX2 textures, and sub-2MB initial bundle budgets.',
            'Strict draw-call budgeting and requestAnimationFrame throttling when offscreen.',
            'Automated device tier detection and responsive WebP fallback delivery.'
        ],
        'faqs': [
            ('Will 3D WebGL make our website slow on mobile phones?', 'No. We apply Draco geometry compression, downscaled KTX2 textures, and dynamic resolution scaling to ensure consistent 60fps rendering across modern smartphones.'),
            ('Can you work with our existing CAD or 3D product models?', 'Yes. We ingest STP, OBJ, FBX, and Blender files, optimizing polygon budgets and baking photorealistic PBR materials for real-time web performance.'),
            ('What happens if a visitor has hardware acceleration turned off?', 'Our progressive enhancement pipeline detects WebGL support instantly. If unavailable, the site smoothly displays high-resolution WebP images or MP4 loops with zero downtime.'),
            ('Can 3D canvas animations sync with normal page text scrolling?', 'Yes! We link Three.js camera coordinates directly with GSAP ScrollTrigger, creating fluid choreography between page text and 3D scenes.')
        ],
        'cta_title': 'Bring Your Brand into 3D Space',
        'cta_desc': 'Schedule a technical exploration call with our 3D WebGL engineers to review models, shaders, and performance budgets.',
        'cta_btn_text': 'Launch 3D WebGL Sprint &rarr;'
    },
    {
        'clean_file': 'web-development.html',
        'legacy_file': 'ai-trading-assistant.html',
        'title': 'Full-Stack Web Development | Vector Studioz',
        'description': 'High-velocity full-stack engineering with Next.js 14, TypeScript, Node.js, and edge infrastructure. Sub-second global latency and zero tech debt.',
        'canonical_url': 'https://www.vectorstudioz.com/web-development.html',
        'badge': 'ENTERPRISE FULL-STACK WEB ENGINEERING',
        'hero_h1': 'Next.js &amp; TypeScript. <br/><span class="gradient-cyan-purple">Zero-Bloat Resilient Codebases.</span>',
        'hero_desc': 'Vector Studioz builds high-throughput web applications and scalable digital platforms. We leverage Next.js 14 App Router, strict TypeScript, serverless edge compute, and automated CI/CD to engineer platforms that scale without friction.',
        'video_mp4': 'https://static.vectorstudioz.com/assets/Videos/ai-trading.mp4',
        'video_webm': 'https://static.vectorstudioz.com/assets/Videos/ai-trading.webm',
        'features_bar': [
            'Next.js 14 App Router',
            'Sub-Second Global Edge Latency',
            'Strict TypeScript Static Typing',
            'Automated CI/CD Pipelines'
        ],
        'why1_title': 'Why Fast-Growing Companies Build With Us',
        'why1_cards': [
            ('Next.js 14 & Server Components', 'Leverage React Server Components, streaming SSR, and edge middleware for blistering initial page loads.', 'Instant page transitions and pristine core web vitals across every user route.'),
            ('Zero Tech Debt Architecture', 'Strict TypeScript typing, modular domain-driven code organization, and rigorous ESLint standards.', 'Codebases designed for multi-year maintainability and friction-free onboarding.'),
            ('Edge Distributed Performance', 'Multi-region serverless deployment, distributed Redis caching, and asset distribution across global CDN nodes.', 'Sub-100ms response times worldwide, whether serving 100 or 1,000,000 concurrent visitors.'),
            ('Automated Testing & CI/CD', 'Automated unit tests, end-to-end Playwright suites, and preview deployment environments on every pull request.', 'Ship new features with complete confidence and zero downtime.')
        ],
        'features_section_title': 'Engineering Disciplines & Full-Stack Capabilities',
        'features_section_desc': 'From consumer-facing web flagships to high-load SaaS platforms, our codebases are built for scale.',
        'features_items': [
            ('01', '02', 'SaaS Platforms & Web Applications', 'Custom web portals with authentication, role-based permissions, transactional billing, and analytics.', 'Integrated with Stripe, Supabase, PostgreSQL, and scalable background job queues.', 'Built for reliable data integrity and lightning-fast user interactions.', 'images/features/vector-fullstack-telemetry.png'),
            ('02', '02', 'Headless CMS & High-Speed Marketing Sites', 'Custom headless integrations with Sanity, Strapi, and Contentful giving marketing teams full publishing agility.', 'Real-time content previews and automatic static regeneration (ISR).', 'Blazing 98+ Lighthouse scores across performance, SEO, and accessibility.', 'images/features/vector-cloud-architecture.png')
        ],
        'who_for_title': 'Who Our Full-Stack Web Team Partners With',
        'who_for_cards': [
            ('Venture-Backed Startups', 'Move from Figma to scalable production deployment in weeks with clean, maintainable code.'),
            ('Scaling SaaS Companies', 'Refactor technical debt, accelerate feature velocity, and stabilize backend performance.'),
            ('Modern E-Commerce Brands', 'Build custom headless storefronts that load instantaneously and maximize conversions.')
        ],
        'why2_title': 'Vector Studioz Engineering vs Outdated Dev Shops',
        'why2_cards': [
            ('Modern Production Stack', 'Next.js 14, React 19, TypeScript, and Tailwind CSS vs bloated legacy WordPress plugins.'),
            ('Weekly Staging Deployments', 'Live staging URLs deployed on every branch for continuous progress verification.'),
            ('Direct Senior Engineer Slack Access', 'Collaborate directly with Lead Systems Architects rather than through junior PMs.'),
            ('100% Repository Transfer', 'Clean Git history, detailed documentation, and complete IP ownership delivered upon launch.')
        ],
        'hiw_title': 'Our 4-Stage Agile Engineering Sprint',
        'hiw_desc': 'Sprint-based architecture ensuring velocity, code quality, and continuous deployment.',
        'hiw_steps': [
            ('Architecture Spec & Schema Planning', 'Defining database schemas, API contracts, caching layers, and tech stack dependencies.'),
            ('Component Library & Frontend Scaffolding', 'Building atomic React components from Figma tokens with strict TypeScript props.'),
            ('API Integration & Business Logic', 'Wiring backend APIs, edge middleware, auth workflows, and database queries.'),
            ('Testing, Performance Profiling & Launch', 'Running Lighthouse audits, end-to-end tests, load simulations, and global DNS cutover.')
        ],
        'comparison_title': 'Vector Studioz Engineering vs Traditional Dev Shops',
        'comparison_rows': [
            ('Code Quality', 'Bloated spaghetti code with poor documentation', 'Clean, typed Next.js with modular component architecture'),
            ('Communication', 'Slow ticket ticketing queues', 'Direct Slack with Principal Engineers'),
            ('Deployment Velocity', 'Monthly delayed releases', 'Weekly live staging previews on every pull request'),
            ('Performance', 'Heavy scripts with 3s+ load times', 'Sub-second edge rendering with 95+ Lighthouse scores')
        ],
        'launch_title': 'Build your next web platform with world-class engineering.',
        'group_title': 'Studio Engineering Principles vs Traditional Dev Shops',
        'group_card1_title': 'Traditional Dev Shop Pitfalls',
        'group_card1_bullets': [
            'Using obsolete PHP frameworks and unvetted third-party plugins.',
            'Opaque development progress leaving you wondering what was built.',
            'Codebases that collapse under real traffic surges due to poor database indexing.'
        ],
        'group_card2_title': 'Vector Studioz Model',
        'group_card2_bullets': [
            'Strict TypeScript, Next.js App Router, and serverless edge compute.',
            'Continuous live staging URLs with transparent git commits.',
            'Architected for high concurrency and elastic cloud auto-scaling.'
        ],
        'faqs': [
            ('What tech stacks do you specialize in?', 'We specialize in Next.js 14, React, TypeScript, Node.js, Python, PostgreSQL, Prisma, Redis, Tailwind CSS, and cloud platforms like Vercel and AWS.'),
            ('How fast can a web platform be engineered?', 'A standard custom web flagship or SaaS MVP typically launches in 4 to 8 weeks depending on scope, divided into 2-week deliverable sprints.'),
            ('Do we own all the source code upon completion?', 'Yes, 100%. All repository code, design assets, infrastructure scripts, and documentation are transferred fully to your organization upon project completion.'),
            ('Can you integrate with our existing backend or APIs?', 'Yes. We frequently connect Next.js frontends to existing REST APIs, GraphQL endpoints, legacy databases, and third-party microservices.')
        ],
        'cta_title': 'Scale Your Digital Product',
        'cta_desc': 'Schedule an architecture consultation with our Principal Engineers to map your project roadmap.',
        'cta_btn_text': 'Book Engineering Consultation &rarr;'
    },
    {
        'clean_file': 'software-engineering.html',
        'legacy_file': 'smart-contract-auditor.html',
        'title': 'Custom Software & Cloud Systems Engineering | Vector Studioz',
        'description': 'Mission-critical software engineering, distributed cloud architecture, high-throughput microservices, and enterprise backend systems built by Vector Studioz.',
        'canonical_url': 'https://www.vectorstudioz.com/software-engineering.html',
        'badge': 'CUSTOM SOFTWARE & DISTRIBUTED CLOUD',
        'hero_h1': 'Resilient Software Architecture. <br/><span class="gradient-cyan-purple">Scalable Cloud Systems.</span>',
        'hero_desc': 'Vector Studioz architects and develops fault-tolerant software systems, scalable microservices, and distributed cloud backends. We solve complex data challenges, optimize compute workloads, and build mission-critical digital infrastructure.',
        'video_mp4': 'https://static.vectorstudioz.com/assets/Videos/smart-contract.mp4',
        'video_webm': 'https://static.vectorstudioz.com/assets/Videos/smart-contract.webm',
        'features_bar': [
            'Distributed Cloud Microservices',
            'High-Throughput Event Streaming',
            'Zero-Downtime Infrastructure',
            'Comprehensive Automated Test Suites'
        ],
        'why1_title': 'Why Enterprise Leaders Rely On Our Software Engineering',
        'why1_cards': [
            ('Distributed Cloud Architecture', 'Engineered across AWS, GCP, and Cloudflare. Multi-region deployments with auto-healing and elastic scaling.', 'High availability architectures designed to maintain 99.99% uptime under extreme loads.'),
            ('High-Throughput Data Streaming', 'Real-time message queues using Kafka, Redis Pub/Sub, and RabbitMQ to process millions of transactions.', 'Low-latency event streaming that keeps data synchronized across distributed nodes.'),
            ('Zero-Trust Security & Encryption', 'End-to-end data encryption in transit and at rest, role-based access control (RBAC), and automated vulnerability scans.', 'Rigorous enterprise security standards embedded into every service endpoint.'),
            ('Observability & Telemetry', 'Comprehensive logging, tracing, and metric collection using OpenTelemetry, Datadog, and Prometheus.', 'Real-time system health visibility with automated anomaly alerting.')
        ],
        'features_section_title': 'Core Software Disciplines & Backend Systems',
        'features_section_desc': 'We construct the resilient software foundations that power modern digital enterprises.',
        'features_items': [
            ('01', '02', 'Custom APIs & Microservices Architecture', 'High-performance REST and GraphQL microservices written in Go, Node.js, and Python.', 'Engineered for sub-50ms query latency, strict schema validation, and automatic documentation.', 'Decoupled services that allow independent scaling and deployment.', 'images/features/vector-cloud-architecture.png'),
            ('02', '02', 'Database Architecture & Data Pipelines', 'High-speed relational (PostgreSQL) and NoSQL (MongoDB, DynamoDB) schema modeling with distributed caching.', 'Automated ETL pipelines, real-time database replication, and optimized query indexing.', 'Zero-data-loss failover architectures designed for enterprise scale.', 'images/features/vector-fullstack-telemetry.png')
        ],
        'who_for_title': 'Who Our Software Engineering Team Partners With',
        'who_for_cards': [
            ('High-Scale Digital Enterprises', 'Modernize monolithic legacy applications into agile, high-performance cloud microservices.'),
            ('FinTech & Healthcare Innovators', 'Build secure, compliant platforms with strict data segregation and audit logging.'),
            ('Data-Intensive SaaS Providers', 'Scale backend pipelines to handle rapid customer growth and high data concurrency.')
        ],
        'why2_title': 'Vector Studioz Standards vs Outdated IT Vendors',
        'why2_cards': [
            ('Modern Cloud-Native Tech', 'Serverless, Docker containers, Kubernetes, and Go/Node/Python vs legacy monolithic hosting.'),
            ('Infrastructure as Code (IaC)', 'Reproducible environments orchestrated with Terraform and Pulumi for zero drift.'),
            ('Strict Testing Thresholds', '90%+ unit test coverage, automated integration runs, and continuous chaos testing.'),
            ('Engineering-Led Communication', 'Direct collaboration with Principal Solutions Architects who write and review production code.')
        ],
        'hiw_title': 'Our 4-Stage Software Engineering Lifecycle',
        'hiw_desc': 'Battle-tested software development lifecycle focused on reliability, performance, and security.',
        'hiw_steps': [
            ('Architecture Design & Threat Model', 'Mapping data flow diagrams, evaluating throughput requirements, and designing threat mitigations.'),
            ('API Contracts & Database Prototyping', 'Developing OpenAPI schemas, database migration scripts, and mock service endpoints.'),
            ('Microservice Implementation & CI', 'Writing clean, test-driven backend code with automated linting, security scans, and build tests.'),
            ('Load Testing, Deployment & Telemetry', 'Simulating spike traffic loads, deploying blue/green releases, and verifying telemetry dashboards.')
        ],
        'comparison_title': 'Vector Studioz Software Engineering vs Traditional Dev Agencies',
        'comparison_rows': [
            ('System Reliability', 'Fragile architectures prone to server crashes', 'Fault-tolerant distributed systems with auto-healing'),
            ('Scalability', 'Bottlenecks at modest traffic levels', 'Elastic cloud auto-scaling handling extreme concurrency'),
            ('Security Protocols', 'Afterthought firewalls with exposed endpoints', 'Zero-trust architecture, encryption, and RBAC baked in'),
            ('Infrastructure', 'Manual server setups vulnerable to drift', 'Immutable Infrastructure as Code (Terraform / Docker)')
        ],
        'launch_title': 'Engineer your digital infrastructure for unmatched stability and scale.',
        'group_title': 'Studio Software Principles vs Legacy IT Vendors',
        'group_card1_title': 'Traditional IT Vendor Pitfalls',
        'group_card1_bullets': [
            'Building brittle monoliths that are difficult to update without breaking existing features.',
            'Neglecting database indexing resulting in sluggish query execution as data grows.',
            'Opaque codebases lacking unit tests and continuous deployment automation.'
        ],
        'group_card2_title': 'Vector Studioz Model',
        'group_card2_bullets': [
            'Decoupled microservice architectures and automated CI/CD pipelines.',
            'Optimized database schemas with Redis caching and query profiling standard.',
            'High test coverage with automated Playwright and integration suites.'
        ],
        'faqs': [
            ('What programming languages and cloud platforms do you use?', 'We build with Go, TypeScript, Node.js, Python, PostgreSQL, Redis, Docker, and Kubernetes, deploying across AWS, GCP, and Cloudflare.'),
            ('How do you ensure zero downtime during backend updates?', 'We use blue/green and canary deployment strategies with health-check probes, ensuring traffic only routes to new instances after successful validation.'),
            ('Can you help migrate our legacy monolithic application to the cloud?', 'Yes. We specialize in strangler-fig migration patterns, gradually decomposing monolithic codebases into modern microservices without service interruption.'),
            ('How do you handle system security and data compliance?', 'We implement TLS 1.3, AES-256 encryption, strict least-privilege IAM roles, automated secret rotation, and continuous static analysis security testing (SAST).')
        ],
        'cta_title': 'Architect Your Next-Gen Systems',
        'cta_desc': 'Schedule a technical session with our Principal Software Architects to discuss your infrastructure requirements.',
        'cta_btn_text': 'Book Architecture Session &rarr;'
    },
    {
        'clean_file': 'ai-automation.html',
        'legacy_file': 'crypto-ai-hub.html',
        'title': 'Autonomous AI Workflows & Intelligent Agent Engineering | Vector Studioz',
        'description': 'Deploy custom LLM agents, Retrieval-Augmented Generation (RAG) pipelines, and autonomous multi-agent workflows built by Vector Studioz.',
        'canonical_url': 'https://www.vectorstudioz.com/ai-automation.html',
        'badge': 'AUTONOMOUS AI WORKFLOWS & MULTI-AGENT SWARMS',
        'hero_h1': 'Autonomous Multi-Agent AI. <br/><span class="gradient-cyan-purple">Intelligent Enterprise Automation.</span>',
        'hero_desc': 'Vector Studioz engineers custom LLM pipelines, autonomous multi-agent workflows, and enterprise Retrieval-Augmented Generation (RAG) systems. We turn unstructured proprietary data into real-time operational efficiency.',
        'video_mp4': 'https://static.vectorstudioz.com/assets/Videos/ai-hub.mp4',
        'video_webm': 'https://static.vectorstudioz.com/assets/Videos/ai-hub.webm',
        'features_bar': [
            'Enterprise RAG Knowledge Engines',
            'Autonomous Multi-Agent Swarms',
            'Zero Data Retention Privacy',
            'Sub-Second LLM Inference Latency'
        ],
        'why1_title': 'Why Ambitious Enterprises Deploy AI With Vector Studioz',
        'why1_cards': [
            ('Retrieval-Augmented Generation (RAG)', 'Connect foundational LLMs to your private documentation, databases, and files with semantic vector indexes.', 'Factual, source-cited responses that eliminate hallucinations and boost reliability.'),
            ('Autonomous Multi-Agent Systems', 'Specialized AI agents coordinated via LangGraph and custom state machines to execute multi-step workflows.', 'Agents that research, verify, write, and execute tasks with automated human-in-the-loop approvals.'),
            ('Enterprise Privacy & Data Security', 'Zero data retention protocols and VPC deployments ensuring your proprietary data is never used for public model training.', 'Bank-grade compliance and encryption protecting every automated prompt and completion.'),
            ('Real-Time Tool Calling & APIs', 'Agents equipped with structured JSON tool-calling capabilities to query internal databases and trigger webhooks.', 'Transform passive chat interfaces into autonomous operational execution engines.')
        ],
        'features_section_title': 'AI Disciplines & Autonomous Capabilities',
        'features_section_desc': 'From internal knowledge copilots to automated operational agents, we build practical AI systems that deliver measurable ROI.',
        'features_items': [
            ('01', '02', 'Enterprise RAG Knowledge Engines', 'Semantic search and document synthesis engines that instantly answer complex operational questions.', 'Hybrid search combining dense vector embeddings with sparse keyword BM25 retrieval.', 'Complete citation tracing with direct links to source documents.', 'images/features/vector-ai-agents.png'),
            ('02', '02', 'Autonomous Operational Workflows', 'Multi-agent workflows that triage customer support tickets, generate personalized sales collateral, and review documents.', 'Human-in-the-loop review checkpoints for critical decision gates.', 'Integrated directly with Slack, HubSpot, Zendesk, and internal SQL databases.', 'images/features/vector-cloud-architecture.png')
        ],
        'who_for_title': 'Who Our AI Automation Team Partners With',
        'who_for_cards': [
            ('Operational Scaleups', 'Automate high-volume repetitive workflows to scale output without linearly growing headcount.'),
            ('Knowledge-Intensive Enterprises', 'Unlock institutional knowledge trapped inside PDFs, Notion pages, and Slack channels.'),
            ('Customer Experience Leaders', 'Deploy intelligent support copilots that resolve customer queries with human-level nuance.')
        ],
        'why2_title': 'Vector Studioz Standards vs Fragile AI Wrappers',
        'why2_cards': [
            ('Rigorous Evaluation Benchmarks', 'We test all agents against automated evaluation benchmarks (RAGAS) to guarantee accuracy.'),
            ('Stateful Multi-Agent Graphs', 'Engineered with LangGraph and deterministic state machines rather than brittle prompt chains.'),
            ('Private VPC Deployment Options', 'Deploy open-weights models (Llama 3, Mistral) within your private VPC for total data sovereignty.'),
            ('Live Observability & Tracing', 'Full prompt and latency tracing with LangSmith to continuously monitor token usage and quality.')
        ],
        'hiw_title': 'Our 4-Stage AI Deployment Lifecycle',
        'hiw_desc': 'From workflow audit to evaluation benchmarking, API integration, and continuous tuning.',
        'hiw_steps': [
            ('Workflow Audit & Feasibility Spec', 'Mapping repetitive operational bottlenecks, identifying proprietary data sources, and establishing ROI metrics.'),
            ('RAG Architecture & Benchmark Setup', 'Ingesting documents into vector indexes, configuring chunking strategies, and building ground-truth benchmarks.'),
            ('Agent Tool Integration & Guardrails', 'Connecting agent tools to internal APIs, configuring hallucination filters, and testing fallbacks.'),
            ('Production Rollout & Continuous Tuning', 'Deploying to staging, enabling real-time LangSmith tracing, and iteratively refining prompt strategies.')
        ],
        'comparison_title': 'Vector Studioz AI Engineering vs Generic AI Wrappers',
        'comparison_rows': [
            ('Accuracy & Verification', 'High hallucination rates with no source attribution', 'Rigorous RAG evaluation with strict citation verification'),
            ('Data Privacy', 'Public APIs logging prompt data for training', 'Zero data retention enterprise APIs and private VPC options'),
            ('System Architecture', 'Brittle single-prompt scripts that break on edge cases', 'Stateful multi-agent graphs with automated error recovery'),
            ('Operational Value', 'Gimmicky chat widgets that create frustration', 'Autonomous workflow engines connected directly to production APIs')
        ],
        'launch_title': 'Deploy autonomous AI workflows that drive real operational velocity.',
        'group_title': 'Studio AI Principles vs Fragile Wrappers',
        'group_card1_title': 'Generic AI Wrapper Pitfalls',
        'group_card1_bullets': [
            'Using basic system prompts that hallucinate incorrect information to customers.',
            'Sending proprietary customer data to unvetted third-party servers.',
            'Failing to monitor token consumption, resulting in runaway operational expenses.'
        ],
        'group_card2_title': 'Vector Studioz Model',
        'group_card2_bullets': [
            'Hybrid RAG search and multi-agent verification loops for strict accuracy.',
            'Zero data retention commitments and optional on-premise model execution.',
            'Granular telemetry and caching layers to minimize inference costs.'
        ],
        'faqs': [
            ('How do you ensure AI agents do not generate inaccurate answers?', 'We implement Retrieval-Augmented Generation (RAG) with semantic similarity thresholds, ground-truth evaluation suites, and multi-agent verification steps that discard unverified claims.'),
            ('Is our internal business data protected?', 'Yes. We strictly use enterprise APIs with zero data retention policies or deploy self-hosted models in your private AWS/GCP cloud so your data is never used for training.'),
            ('What frameworks do you use to build AI workflows?', 'We develop with Python, LangGraph, LlamaIndex, OpenAI/Anthropic APIs, Pinecone, Qdrant, and LangSmith for telemetry.'),
            ('How quickly can an AI workflow be deployed?', 'A focused automated workflow or internal knowledge copilot typically transitions from prototype to production within 3 to 5 weeks.')
        ],
        'cta_title': 'Automate Your Enterprise Operations',
        'cta_desc': 'Schedule an AI roadmap consultation with our AI Solutions Architects to identify your highest-ROI opportunities.',
        'cta_btn_text': 'Book AI Roadmap Consultation &rarr;'
    },
    {
        'clean_file': 'mobile-development.html',
        'legacy_file': 'smart-contract-generator.html',
        'title': 'High-Performance Mobile App Development | Vector Studioz',
        'description': 'Bespoke iOS and Android mobile engineering with Flutter and React Native. Fluid 120Hz gesture ergonomics, offline-first sync, and App Store launch management.',
        'canonical_url': 'https://www.vectorstudioz.com/mobile-development.html',
        'badge': 'CROSS-PLATFORM MOBILE ENGINEERING',
        'hero_h1': 'High-Performance Mobile Apps. <br/><span class="gradient-cyan-purple">Fluid 120Hz Native Ergonomics.</span>',
        'hero_desc': 'Vector Studioz designs and engineers high-performance mobile applications for iOS and Android. Using Flutter and React Native, we deliver native compile speeds, fluid gesture transitions, offline-first architectures, and full App Store launch management.',
        'video_mp4': 'https://static.vectorstudioz.com/assets/Videos/scg.mp4',
        'video_webm': 'https://static.vectorstudioz.com/assets/Videos/scg.webm',
        'features_bar': [
            'Unified iOS & Android Codebase',
            'Fluid 120Hz Native Gesture Physics',
            'Offline-First Local Synchronization',
            'End-to-End App Store Approval'
        ],
        'why1_title': 'Why Ambitious Brands Build Mobile Apps With Us',
        'why1_cards': [
            ('Unified Cross-Platform Codebase', 'One elegant codebase compiling to native ARM machine code on both iOS and Android platforms.', 'Cut development and maintenance timelines in half without compromising native responsiveness.'),
            ('Fluid 120Hz Gesture Physics', 'Custom touch interactions, tactile haptic feedback, and fluid 120Hz ProMotion transitions.', 'Ergonomic mobile interfaces designed for effortless one-handed thumb navigation.'),
            ('Offline-First Architecture', 'High-performance local SQLite and Realm storage with automated bidirectional background syncing.', 'Users can access core app features seamlessly, even with spotty connectivity.'),
            ('Guaranteed App Store Launch', 'End-to-end management of Apple App Store and Google Play reviews, TestFlight builds, and compliance.', 'Zero rejection delays through strict adherence to Apple and Google design guidelines.')
        ],
        'features_section_title': 'Mobile Disciplines & Native Capabilities',
        'features_section_desc': 'We construct mobile products that users love to open every day.',
        'features_items': [
            ('01', '02', 'Consumer & Lifestyle Mobile Apps', 'Engaging mobile experiences with personalized feeds, interactive video, social sharing, and push notifications.', 'Engineered for rapid app launches, minimal memory footprint, and low battery consumption.', 'Seamless biometrics, Apple Pay, and Google Pay integrations standard.', 'images/features/vector-mobile-apps.png'),
            ('02', '02', 'Enterprise & Field Operations Apps', 'Secure mobile applications for field personnel, inventory scanning, internal messaging, and real-time dispatch.', 'Equipped with offline signature capture, camera barcode scanning, and secure local data encryption.', 'Deeply connected to your corporate backend systems.', 'images/features/vector-design-system.png')
        ],
        'who_for_title': 'Who Our Mobile Engineering Team Partners With',
        'who_for_cards': [
            ('Consumer Mobile Startups', 'Launch category-defining iOS and Android applications with native responsiveness and high ratings.'),
            ('Established Web Platforms', 'Extend your web presence into pocket form with native push notifications and biometric login.'),
            ('Field Operations Enterprises', 'Equip teams with offline-ready tools that streamline mobile data collection.')
        ],
        'why2_title': 'Vector Studioz Mobile Standards vs Sluggish Web Wrappers',
        'why2_cards': [
            ('True Native Compilation', 'Flutter and React Native compiling to native ARM binaries vs clunky webview wrappers.'),
            ('Smooth 120Hz Scroll Performance', 'Rigorous profiling to eliminate dropped frames and ensure fluid scroll kinetics.'),
            ('Strict Battery & Memory Budgets', 'Optimized background threads to keep battery consumption minimal during daily use.'),
            ('Continuous Automated Builds', 'Fastlane deployment pipelines shipping automated TestFlight and internal Google Play betas.')
        ],
        'hiw_title': 'Our 4-Stage Mobile App Sprint Lifecycle',
        'hiw_desc': 'From wireframe prototyping to TestFlight beta builds, device testing, and App Store launch.',
        'hiw_steps': [
            ('Mobile UX & Gesture Architecture', 'Designing touch wireframes, navigation ergonomics, and backend API contracts.'),
            ('Flutter / React Native Sprints', 'Bi-weekly agile sprints delivering playable TestFlight and Google Play internal releases.'),
            ('Real Device Testing & Profiling', 'Testing across a matrix of real iOS and Android devices, profiling frame rates and battery usage.'),
            ('Store Submission & Launch Management', 'Optimizing store metadata, creating localized screenshots, and managing store review approval.')
        ],
        'comparison_title': 'Vector Studioz Mobile Engineering vs Basic App Agencies',
        'comparison_rows': [
            ('App Responsiveness', 'Sluggish webview rendering with stuttering scrolls', 'Native compiled code with silky 120Hz transitions'),
            ('Offline Capability', 'White screen error when internet connectivity drops', 'Offline-first database with automatic background sync'),
            ('Store Compliance', 'Frequent rejections due to policy violations', '100% App Store and Google Play approval guarantee'),
            ('Code Architecture', 'Two separate disconnected codebases with duplicate bugs', 'Single unified codebase with shared business logic')
        ],
        'launch_title': 'Launch a high-performance mobile app that users love to open.',
        'group_title': 'Studio Mobile Principles vs Webview Wrappers',
        'group_card1_title': 'Webview Wrapper Pitfalls',
        'group_card1_bullets': [
            'Wrapping a website in Cordova/Capacitor resulting in slow, awkward touch gestures.',
            'Failing to implement native OS haptics, keyboard handling, and biometrics.',
            'Frequent rejection from Apple review teams for not feeling like a native application.'
        ],
        'group_card2_title': 'Vector Studioz Model',
        'group_card2_bullets': [
            'Native compiled Flutter and React Native engines with real platform widgets.',
            'Deep platform integration for Apple Pay, FaceID, widgets, and live activities.',
            'Automated Fastlane deployment pipelines shipping continuous beta builds.'
        ],
        'faqs': [
            ('Should our app be built in Flutter or React Native?', 'Both are outstanding modern platforms. We recommend Flutter for rich, custom visual designs and 120Hz animations, and React Native when your team already maintains an extensive React codebase.'),
            ('Do you manage the entire Apple App Store and Google Play submission?', 'Yes. We handle app bundle creation, signing certificates, privacy manifests, store screenshots, metadata descriptions, and review correspondence until live approval.'),
            ('Can the mobile app share databases with our existing web platform?', 'Yes. We architect clean REST and GraphQL API gateways that power both your web application and mobile apps from a unified source of truth.'),
            ('How do you manage push notifications and deep linking?', 'We integrate Firebase Cloud Messaging (FCM) and Apple Push Notification service (APNs), alongside universal links for smooth user onboarding and retention.')
        ],
        'cta_title': 'Launch Your Mobile Product',
        'cta_desc': 'Schedule a mobile architecture session with our Mobile Engineering Leads to review your app specifications.',
        'cta_btn_text': 'Book Mobile Architecture Review &rarr;'
    }
]

def build_service_page(cfg):
    head = get_service_head(
        title=cfg['title'],
        description=cfg['description'],
        canonical_url=cfg['canonical_url']
    )

    # 1. Hero features list HTML
    hero_features_html = "".join([f"""
            <div class="landing-hero-features-item">
              <img alt="" class="landing-hero-features-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a818f151d79fc314e3f50_hero%20features%20icon.svg"/>
              <div class="landing-hero-features-text">{item}</div>
            </div>""" for item in cfg['features_bar']])

    # 2. Why Section 1 Cards HTML
    why1_cards_html = ""
    for idx, (ctitle, cdesc1, cdesc2) in enumerate(cfg['why1_cards']):
        extra_class = ""
        if idx % 2 == 1:
            extra_class += " no-br-right"
        if idx >= 2:
            extra_class += " no-br-bottom"
        why1_cards_html += f"""
            <div class="landing-why-item item-50 feature-card pillar-card{extra_class}" block-corners-top="">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693e7d5b2039a9b3ae1be0f6_Icon_chatbot_1.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">{ctitle}</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">{cdesc1}</div>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">{cdesc2}</div>
              </div>
              <div block-corners-bottom=""></div>
            </div>"""

    # 3. Features Items HTML
    features_items_html = ""
    for num, total, ftitle, fdesc, b1, b2, img_url in cfg['features_items']:
        features_items_html += f"""
            <div class="landing-features-list-item feature-card pillar-card">
              <div class="landing-features-item-wrapper">
                <div class="landing-features-content-wrapper content-center">
                  <div class="landing-features-icon-wrapper">
                    <div class="landing-features-mobile-nav landing-nav-full-width">
                      <div class="landing-features-navigation-text">{num}</div>
                      <div class="landing-features-navigation-line"><div class="landing-line-gradient _50"></div></div>
                      <div class="landing-features-navigation-text">{total}</div>
                    </div>
                  </div>
                  <h3 class="landing-features-item-title">{ftitle}</h3>
                  <div class="features-description">{fdesc}</div>
                  <div class="landing-features-desc-list">
                    <div class="landing-secondary-desc-item">
                      <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                      <div class="landing-secondary-desc-text">{b1}</div>
                    </div>
                    <div class="landing-secondary-desc-item">
                      <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                      <div class="landing-secondary-desc-text">{b2}</div>
                    </div>
                  </div>
                </div>
                <div class="landing-features-banner-wrapper">
                  <img alt="" class="landing-features-banner landing-desktop" loading="lazy" src="{img_url}"/>
                </div>
              </div>
            </div>"""

    # 4. Who For Cards HTML
    who_for_cards_html = f"""
          <div class="landing-who-for-item landing-item-title">
            <div class="landing-who-for-title-wrapper">
              <h2 class="landing-heading">{cfg['who_for_title']}</h2>
            </div>
            <div class="landing-landing-line landing-section-line landing-right"></div>
            <div class="landing-landing-line landing-section-line"></div>
          </div>"""
    for wtitle, wdesc in cfg['who_for_cards']:
        who_for_cards_html += f"""
          <div class="landing-who-for-item">
            <img alt="" class="landing-who-for-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a828953e0dd9d1bce9156_icon_Traders.svg"/>
            <h3 class="landing-who-tor-item-title">{wtitle}</h3>
            <div class="landing-secondary-desc-item">
              <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot-3"></div><div class="landing-btn-dot-3"></div></div>
              <div class="landing-secondary-desc-text landing-p-24-mob">{wdesc}</div>
            </div>
          </div>"""

    # 5. Why Section 2 Cards HTML
    why2_cards_html = ""
    for idx, (ctitle, cdesc) in enumerate(cfg['why2_cards']):
        extra_class = ""
        if idx % 2 == 1:
            extra_class += " no-br-right"
        if idx >= 2:
            extra_class += " no-br-bottom"
        why2_cards_html += f"""
            <div class="landing-why-item item-50 feature-card pillar-card{extra_class}" block-corners-top="">
              <div class="landing-gradient-icon-wrapper">
                <div class="landing-gradient-icon-container">
                  <img alt="" class="landing-why-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693abce6109ac59f8c14faee_icon_Founders.svg"/>
                </div>
              </div>
              <div class="landing-why-item-title-wrapper">
                <h3 class="landing-why-item-title">{ctitle}</h3>
              </div>
              <div class="landing-why-desc-wrapper">
                <div class="landing-col-row-gradient"></div>
                <div class="landing-why-desc">{cdesc}</div>
              </div>
              <div block-corners-bottom=""></div>
            </div>"""

    # 6. HIW Steps HTML (Clean 2x2 grid)
    hiw_steps_html = ""
    for sidx, (stitle, sdesc) in enumerate(cfg['hiw_steps']):
        hiw_steps_html += f"""
            <div class="landing-hiw-item-wrapper">
              <div class="landing-hiw-item landing-vertical">
                <div class="landing-hiw-item-content hiw-item-vertical">
                  <div class="landing-hiw-item-title-wrapper">
                    <div class="landing-gradient-icon-wrapper landing-hiw-icon">
                      <div class="landing-gradient-icon-container landing-hiw-icon-container">
                        <div class="landing-hiw-number-text">{sidx + 1}</div>
                      </div>
                    </div>
                    <h2 class="landing-hiw-item-title">{stitle}</h2>
                  </div>
                  <div class="landing-secondary-desc-text landing-no-padding">{sdesc}</div>
                </div>
              </div>
            </div>"""

    # 7. Comparison Table Rows HTML
    comparison_rows_html = ""
    for metric, traditional, vector in cfg['comparison_rows']:
        comparison_rows_html += f"""
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text">{metric}</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-text-secondary">{traditional}</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text">{vector}</div>
          </div>"""

    # 8. Group Dual Cards HTML
    group_card1_bullets_html = "".join([f"""
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text">{b}</div>
                </div>""" for b in cfg['group_card1_bullets']])

    group_card2_bullets_html = "".join([f"""
                <div class="landing-secondary-desc-item">
                  <div class="landing-btn-dot-wrapper landing-dot-features"><div class="landing-btn-dot"></div><div class="landing-btn-dot"></div></div>
                  <div class="landing-secondary-desc-text">{b}</div>
                </div>""" for b in cfg['group_card2_bullets']])

    # 9. FAQ Questions HTML
    faq_items_html = ""
    for qidx, (q, a) in enumerate(cfg['faqs']):
        faq_items_html += f"""
            <div class="landing-faq-question-item faq-2" block-corners-top="">
              <div class="landing-faq-question-title-wrapper">
                <h3 class="landing-faq-question-title">{q}</h3>
                <div class="landing-faq-question-icon">
                  <div class="landing-faq-icon-line"></div>
                  <div class="landing-faq-icon-line landing-horizontal"></div>
                </div>
              </div>
              <div class="landing-faq-answer-wrapper" style="height: {'auto' if qidx == 0 else '0px'};">
                <div class="landing-faq-answer">{a}</div>
              </div>
              <div block-corners-bottom=""></div>
            </div>"""

    # Assemble complete HTML
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
            <div class="landing-badge-pill section-title-bordered">{cfg['badge']}</div>
            <h1 class="landing-ai-alerts-heading">
              {cfg['hero_h1']}
            </h1>
            <div class="landing-hero-description landing-hero-column">
              {cfg['hero_desc']}
            </div>
            <div class="landing-hero-button-wrapper landing-hero-column landing-mobile-hidden" style="display:flex;gap:12px;margin-top:28px;">
              <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="projects.html">
                <div class="btn-primary-wrapper" data-scramble-text="">
                  <div class="btn-primary-text-3" scramble-text="">Explore Client Work &rarr;</div>
                </div>
              </a>
              <a class="btn-secondary-4 w-inline-block" href="contact-us.html">
                <div class="btn-secondary-4-wrapper">
                  <div class="btn-secondary-text-4" scramble-text="">Schedule Discovery Call</div>
                </div>
              </a>
            </div>
          </div>

          <!-- Right Column: Native Webflow Video Asset -->
          <div class="landing-hero-asset-wrapper hero-column">
            <div class="hero-assets-container w-embed">
              <video autoplay="" class="landing-hero-asset landing-hero-column" loop="" muted="" playsinline="">
                <source src="{cfg['video_mp4']}" type="video/mp4; codecs=hvc1"/>
                <source src="{cfg['video_webm']}" type="video/webm"/>
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
            {hero_features_html}
          </div>
        </div>
      </div>
    </section>

    <!-- Section 1: Webflow Why Section (Core Philosophy) -->
    <section class="landing-why">
      <div class="landing-container">
        <div class="landing-why-wrapper">
          <div class="landing-why-title-wrapper" style="text-align:center;max-width:800px;margin:0 auto 40px;">
            <div class="landing-badge-pill section-title-bordered">CORE PHILOSOPHY</div>
            <h2 class="landing-why-title">{cfg['why1_title']}</h2>
          </div>
          <div class="landing-why-list why-list-wrap">
            <div class="landing-section-border landing-border-top"></div>
            {why1_cards_html}
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Webflow Features (Core Capabilities) -->
    <section class="landing-features" id="landing-features">
      <div class="w-layout-blockcontainer landing-container w-container">
        <div class="landing-features-wrapper">
          <div class="landing-features-title-wrapper">
            <h2 class="landing-features-title">{cfg['features_section_title']}</h2>
            <div class="landing-features-desc-wrapper">
              <div class="landing-features-title-desc">{cfg['features_section_desc']}</div>
              <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="projects.html">
                <div class="btn-primary-wrapper btn-features" data-scramble-text="">
                  <div class="btn-primary-text-3" scramble-text="">View Featured Work</div>
                  <img alt="" class="btn-primary-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a8238e7f07a24a861ed19_Icon16.svg"/>
                </div>
              </a>
            </div>
          </div>

          <div class="landing-features-list">
            {features_items_html}
          </div>
        </div>
      </div>
    </section>

    <!-- Section 3: Webflow Who For Section -->
    <section class="landing-who-for">
      <div class="landing-container-4">
        <div class="landing-who-for-wrapper">
          {who_for_cards_html}
        </div>
      </div>
    </section>

    <!-- Section 4: Webflow Why Section (Second Why: Standards) -->
    <section class="landing-why">
      <div class="landing-container">
        <div class="landing-why-wrapper">
          <h2 class="landing-comparison-title width-80">
            {cfg['why2_title']}
          </h2>
          <div class="landing-why-list why-list-wrap">
            <div class="landing-section-border landing-border-top"></div>
            {why2_cards_html}
            <div class="landing-section-border mobile-hidden"></div>
          </div>
        </div>
      </div>
      <div class="landing-dark-gradient"></div>
      <div class="landing-dark-gradient landing-gradient-bottom"></div>
      <div class="landing-dark-gradient landing-gradient-right"></div>
      <div class="landing-dark-gradient landing-gradient-left"></div>
    </section>

    <!-- Section 5: Webflow How It Works (4-Stage Sprint Journey - Clean 2x2 Grid) -->
    <section class="landing-hiw">
      <div class="landing-container">
        <div class="landing-hiw-wrapper">
          <div class="landing-hiw-title-wrapper">
            <h2 class="landing-hiw-title full-width">{cfg['hiw_title']}</h2>
            <div class="landing-hiw-desc-wrapper">
              <div class="landing-desc-color">{cfg['hiw_desc']}</div>
            </div>
          </div>

          <div class="landing-hiw-list-wrapper">
            {hiw_steps_html}
          </div>
        </div>
      </div>
    </section>

    <!-- Section 6: Webflow Comparison Table -->
    <section class="landing-comparison">
      <div class="landing-container">
        <h2 class="landing-comparison-title width-80">{cfg['comparison_title']}</h2>
        <div class="landing-comparison-table">
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-table-title">Performance Metric</div>
          </div>
          <div class="landing-comparison-table-row">
            <div class="landing-comparison-table-text landing-table-title">Traditional Agency / Dev Shop</div>
          </div>
          <div class="landing-comparison-table-row landing-br-none">
            <div class="landing-comparison-table-text landing-table-title">Vector Studioz</div>
          </div>

          {comparison_rows_html}

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
            <h2 class="landing-launch-title">{cfg['launch_title']}</h2>
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

    <!-- Section 8: Webflow Group Section (Operating Principles) -->
    <section class="landing-group">
      <div class="landing-container">
        <div class="landing-group-wrapper">
          <h2 class="landing-group-title">{cfg['group_title']}</h2>
          <div class="landing-group-list">
            <div class="landing-group-item-wrapper">
              <div class="landing-group-item">
                <div class="landing-group-item-title-wrapper">
                  <img alt="" class="landing-group-item-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a83613f60ebaed5c9c7fe_group%20Icon%201.svg"/>
                  <div class="landing-group-item-title">{cfg['group_card1_title']}</div>
                </div>
                {group_card1_bullets_html}
              </div>
              <div class="landing-landing-line landing-section-line landing-right"></div>
            </div>
            <div class="landing-group-item-wrapper right">
              <div class="landing-group-item landing-right">
                <div class="landing-group-item-title-wrapper">
                  <img alt="" class="landing-group-item-icon" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a83613f60ebaed5c9c80b_grout%20Icon2.svg"/>
                  <div class="landing-group-item-title">{cfg['group_card2_title']}</div>
                </div>
                {group_card2_bullets_html}
              </div>
              <div class="landing-landing-line landing-section-line"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 9: Webflow FAQ Section (Split Interactive Accordions) -->
    <section class="landing-faq">
      <div class="landing-container">
        <div class="landing-faq-wrapper">
          <div class="landing-faq-title-wrapper">
            <div class="landing-badge-pill section-title-bordered">QUESTIONS &amp; ANSWERS</div>
            <h2 class="landing-faq-title">Frequently Asked Questions</h2>
            <div class="landing-faq-desc">Everything you need to know about partnering with Vector Studioz for this discipline.</div>
            <div class="landing-faq-button-wrapper landing-mobile-hidden" style="margin-top:28px;">
              <a class="btn-primary-4 ml-auto custom-button w-inline-block" href="contact-us.html">
                <div class="btn-primary-wrapper" data-scramble-text="">
                  <div class="btn-primary-text-3" scramble-text="">Have Another Question? &rarr;</div>
                </div>
              </a>
            </div>
          </div>

          <div class="landing-faq-questions-list">
            {faq_items_html}
          </div>
        </div>
      </div>
    </section>

    <!-- Section 10: Webflow Closing CTA Banner -->
    <section class="landing-cta cta-banner-wrapper cta-banner">
      <div class="landing-container landing-relative">
        <div class="cta-wrapper">
          <div class="landing-cta-asset-wrapper">
            <img alt="" class="landing-cta-asset" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/693a840e6c646ef67cae8ce9_cta%20asset.png"/>
          </div>
          <div class="landing-section-border landing-border-top"></div>
          <div class="landing-section-border"></div>
          <h2 class="cta-title-2">{cfg['cta_title']}</h2>
          <div class="cta-desc-2">{cfg['cta_desc']}</div>
          <div class="cta-button-wrapper-2" style="display:flex;justify-content:center;gap:12px;margin-top:24px;">
            <a class="btn-primary-4 btn-primary custom-button w-inline-block" href="contact-us.html">
              <div class="btn-primary-wrapper" data-scramble-text="">
                <div class="btn-primary-text-3" scramble-text="">{cfg['cta_btn_text']}</div>
              </div>
            </a>
            <a class="btn-secondary-4 w-inline-block" href="projects.html">
              <div class="btn-secondary-4-wrapper">
                <div class="btn-secondary-text-4" scramble-text="">Explore Projects</div>
              </div>
            </a>
          </div>
        </div>
      </div>
      <div class="landing-dark-gradient landing-gradient-left"></div>
      <div class="landing-dark-gradient landing-gradient-right"></div>
    </section>
  </main>

  {FOOTER_HTML}

{FAQ_ACCORDION_SCRIPT}
</body>
</html>"""

    return html

def build_all_services():
    for cfg in SERVICES_CONFIG:
        clean_file = cfg['clean_file']
        legacy_file = cfg['legacy_file']
        html_content = build_service_page(cfg)

        with open(clean_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Generated canonical 11-section Webflow page: {clean_file}")

        with open(legacy_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Mirrored canonical 11-section Webflow page: {legacy_file}")

    print("All 6 Vector Studioz service pages compiled successfully!")

if __name__ == '__main__':
    build_all_services()
