# projects_data.py
"""
Centralized Data Model for Vector Studioz Client Projects & Platforms.
Single source of truth for:
- Standalone project subpages (projects/<slug>.html)
- Main projects catalog (projects.html & case-studies.html)
- Homepage interactive slider (index.html#cases)
"""

PROJECTS_LIST = [
    {
        'slug': 'mesuullogic',
        'title': 'Messulogic — Enterprise EdTech & Learning Management Platform',
        'short_title': 'Messulogic',
        'client': 'Messulogic Technologies Ltd.',
        'category': 'EdTech & Learning Management',
        'category_tag': 'EdTech',
        'industry': 'Education & Digital Skills',
        'year': '2025',
        'live_url': 'https://mesuullogic.com/',
        'thumbnail': 'images/case-studies/mesuullogic.jpg',
        'tagline': 'High-Performance LMS Engine, Real-Time Student Portal & Course Commerce',
        'badge': 'EdTech Platform',
        'metrics': [
            {'value': '10,000+', 'label': 'Active Learners'},
            {'value': '99.9%', 'label': 'Platform Uptime'},
            {'value': '< 1.1s', 'label': 'Course Load Speed'}
        ],
        'overview': (
            'Messulogic is a premier Nigerian technology education hub and learning management system based in Abuja. '
            'Vector Studioz engineered a high-throughput, student-centric digital ecosystem complete with interactive course modules, '
            'SIWES industrial internship tracking, authenticated student portal, and automated certificate issuance.'
        ),
        'challenge': (
            'The existing infrastructure struggled with student concurrency during enrollment periods, suffered from fragmented course delivery across third-party tools, and lacked a centralized portal for assignment submission and grade monitoring.'
        ),
        'solution': (
            'We architected an integrated LMS with custom WordPress engine and Masteriyo hooks, high-speed CDN caching, automated student onboarding workflows, and responsive course catalog with friction-free enrollment pathways.'
        ),
        'tech_stack': ['WordPress Engine', 'Masteriyo LMS', 'WooCommerce', 'PHP 8.2', 'Tailwind CSS', 'Redis Caching', 'Cloudflare CDN'],
        'testimonial': {
            'quote': 'Vector Studioz completely redefined our digital footprint. Student enrollment jumped 65% in the first quarter post-launch, and our learning portal runs with zero lag.',
            'author': 'Academic Director',
            'role': 'Messulogic Technologies'
        }
    },
    {
        'slug': 'expressteck',
        'title': 'ExpressTeck — Innovation & Transformation Digital Training Academy',
        'short_title': 'ExpressTeck',
        'client': 'ExpressTeck Global',
        'category': 'SaaS & EdTech Portal',
        'category_tag': 'EdTech',
        'industry': 'Tech Training & Enterprise Transformation',
        'year': '2025',
        'live_url': 'https://expressteck.tech/',
        'thumbnail': 'images/case-studies/expressteck.jpg',
        'tagline': 'Full-Stack React Course Commerce, Event Engine & Interactive Skills Portal',
        'badge': 'Tech Academy',
        'metrics': [
            {'value': '+80%', 'label': 'Course Registrations'},
            {'value': '100/100', 'label': 'Lighthouse Performance'},
            {'value': '24/7', 'label': 'Real-Time Mentorship'}
        ],
        'overview': (
            'ExpressTeck empowers ambitious professionals to master in-demand tech disciplines. '
            'Vector Studioz designed and deployed an ultra-modern hybrid React theme platform featuring dynamic dark/light mode toggles, '
            'interactive curriculum roadmaps, integrated event booking, and automated payment gateways.'
        ),
        'challenge': (
            'The client needed a digital presence that signaled elite engineering pedigree while handling multi-currency course checkouts, live event registrations, and automated webinar links seamlessly.'
        ),
        'solution': (
            'We engineered a custom React-powered theme with instant client-side theme switching, seamless WooCommerce course commerce integration, optimized SVG asset pipelines, and automated CRM lead capture.'
        ),
        'tech_stack': ['React 18', 'WordPress Core', 'WooCommerce API', 'Mastercard Cloud Gateway', 'Elementor Engine', 'Vite Asset Pipeline'],
        'testimonial': {
            'quote': 'The interactive UI and snappy performance immediately set us apart from standard academy sites. Conversions on course sales scaled beyond all our initial targets.',
            'author': 'Lead Technical Partner',
            'role': 'ExpressTeck'
        }
    },
    {
        'slug': 'lake-greenfield-hotel',
        'title': 'Lake Greenfield Hotel — Luxury Boutique Hospitality & Direct Booking Platform',
        'short_title': 'Lake Greenfield Hotel',
        'client': 'Lake Greenfield Hospitality',
        'category': 'Hospitality & Web Booking',
        'category_tag': 'Web Design',
        'industry': 'Luxury Hospitality & Tourism',
        'year': '2025',
        'live_url': 'https://lakegreenfieldhotel.com/',
        'thumbnail': 'images/case-studies/lake-greenfield.jpg',
        'tagline': 'Serene Lakeside Luxury Showcase & Integrated Direct Reservation Engine',
        'badge': 'Luxury Hospitality',
        'metrics': [
            {'value': '+120%', 'label': 'Direct Bookings'},
            {'value': '-40%', 'label': 'OTA Commission Fees'},
            {'value': '4K Visuals', 'label': 'Jabi Lake Suite Tours'}
        ],
        'overview': (
            'Situated along the shores of Jabi Lake in Abuja, Lake Greenfield Hotel offers tranquil luxury accommodations. '
            'Vector Studioz crafted an experiential booking portal highlighting lakeside suites, fine dining, and conference venues, '
            'directly connected to an automated date-picker reservation pipeline.'
        ),
        'challenge': (
            'Over-reliance on third-party online travel agencies (OTAs) was eroding profit margins, and previous website visitors struggled to visualize room tiers and amenities on mobile devices.'
        ),
        'solution': (
            'We designed a visual-first mobile experience with ambient video headers, instant room availability checks, frictionless check-in/check-out selectors, and secure credit card payment handling.'
        ),
        'tech_stack': ['Headless WordPress', 'Custom Booking Engine', 'Stripe & Local Gateway', 'GSAP Motion', 'Responsive CSS3', 'Fastly CDN'],
        'testimonial': {
            'quote': 'Our guests consistently remark on how seamless the website is. Vector Studioz helped us recapture our direct guest relationship and significantly boosted direct room revenue.',
            'author': 'General Manager',
            'role': 'Lake Greenfield Hotel'
        }
    },
    {
        'slug': 'iclvirtualservices',
        'title': 'icL Virtual Services — Your Operational Excellence Assistant',
        'short_title': 'icL Virtual Services',
        'client': 'icL Virtual Services LLC',
        'category': 'Operations & Virtual Talent',
        'category_tag': 'Operations',
        'industry': 'Virtual Operations & Professional Staffing',
        'year': '2025',
        'live_url': 'https://iclvirtualservices.com/',
        'thumbnail': 'images/case-studies/operational-excellence.png',
        'tagline': 'High-Efficiency Remote Operations, Vetted Professionals & Rapid Staffing',
        'badge': 'Operational Hub',
        'metrics': [
            {'value': '3x', 'label': 'Executive Productivity'},
            {'value': '100%', 'label': 'W-2 Vetted Staff'},
            {'value': '< 48h', 'label': 'Talent Match Turnaround'}
        ],
        'overview': (
            'icL Virtual Services provides high-caliber, vetted operational assistants and remote talent for fast-moving startups and global enterprises. '
            'Vector Studioz engineered a high-converting, single-page application built with Vite and React, engineered for high credibility and instant consultation booking.'
        ),
        'challenge': (
            'Competing in a crowded virtual assistant market required instant credibility, transparent pricing tiers, and an ultra-fast onboarding funnel that eliminates administrative friction.'
        ),
        'solution': (
            'We developed a sleek dark-mode web application featuring real-time interactive engagement calculators, video testimonials, interactive service tier matrices, and automated Calendly synchronization.'
        ),
        'tech_stack': ['Vite', 'React', 'Tailwind CSS', 'Lucide Icons', 'Hostinger Cloud', 'Automated Calendly Integration'],
        'testimonial': {
            'quote': 'The new platform positions icL as the premier remote operational partner. Our conversion from discovery visitor to signed contract grew exponentially within the first 60 days.',
            'author': 'Operations Director',
            'role': 'icL Virtual Services'
        }
    },
    {
        'slug': 'mirola-cleaning-services',
        'title': 'Mirola Cleaning Services — Commercial Janitorial & Facility Sanitization Portal',
        'short_title': 'Mirola Cleaning Services',
        'client': 'Mirola Cleaning Services LLC',
        'category': 'Commercial Facility Care',
        'category_tag': 'Web Design',
        'industry': 'Commercial Facility Management',
        'year': '2025',
        'live_url': 'https://mirolacleaningservices.com/',
        'thumbnail': 'images/case-studies/mirola-cleaning.jpg',
        'tagline': 'Hospital-Grade Sanitization, Floor Strip & Waxing & Automated Walkthrough Booking',
        'badge': 'Facility Care',
        'metrics': [
            {'value': '+150%', 'label': 'Facility Quotes'},
            {'value': '24/7', 'label': 'Rapid Emergency Dispatch'},
            {'value': '100% Vetted', 'label': 'OSHA Certified Teams'}
        ],
        'overview': (
            'Mirola Cleaning Services delivers hospital-grade commercial cleaning, floor stripping & waxing, and recurring janitorial facility management across New Jersey and nationwide corporate clients. '
            'Vector Studioz built a high-performance commercial portal with instant square-footage estimation calculators and emergency dispatch request tools.'
        ),
        'challenge': (
            'Corporate facility managers need swift verification of insurance, OSHA compliance, and instant pricing quotes without lengthy back-and-forth email chains.'
        ),
        'solution': (
            'We crafted a robust conversion architecture featuring interactive facility-type selectors (Medical, Corporate, Industrial, Education), structured Schema.org local SEO, and 1-click walkthrough scheduling.'
        ),
        'tech_stack': ['Vite SPA', 'React 18', 'Tailwind CSS', 'Schema.org JSON-LD', 'Google Cloud Platform', 'Twilio SMS Alerts'],
        'testimonial': {
            'quote': 'Vector Studioz built exactly what facility managers need: clear service specs, immediate trust triggers, and effortless walkthrough bookings.',
            'author': 'Managing Partner',
            'role': 'Mirola Cleaning Services'
        }
    },
    {
        'slug': 'mirola-nigeria',
        'title': 'Mirola Enterprise Nigeria — Digital & Remote Work Skills Development Academy',
        'short_title': 'Mirola Enterprise Nigeria',
        'client': 'Mirola Enterprise Nigeria',
        'category': 'Digital Skills & Talent Hub',
        'category_tag': 'EdTech',
        'industry': 'Workforce Development & Remote Careers',
        'year': '2025',
        'live_url': 'https://mirolanigeria.com/',
        'thumbnail': 'images/case-studies/mirola-nigeria.jpg',
        'tagline': 'Empowering Nigerian Youth with Global Remote Skills & Direct Career Placement',
        'badge': 'Skills Academy',
        'metrics': [
            {'value': '5,000+', 'label': 'Graduates Placed'},
            {'value': '85%', 'label': 'Remote Employment Rate'},
            {'value': '4.9/5', 'label': 'Student Satisfaction'}
        ],
        'overview': (
            'Mirola Enterprise Nigeria bridges the opportunity gap by training youth in high-demand remote skills, from virtual operations and data analytics to digital marketing and customer success. '
            'Vector Studioz engineered a high-impact, accessible web portal designed to inspire, educate, and streamline nationwide scholarship applications.'
        ),
        'challenge': (
            'The site required fast, low-bandwidth mobile performance across diverse network conditions in Nigeria, while communicating massive social impact to corporate sponsors and international partners.'
        ),
        'solution': (
            'We built a lightweight, typography-driven portal utilizing modern web standards, optimized vector graphics, comprehensive cohort schedules, and an accessible application funnel.'
        ),
        'tech_stack': ['WordPress Engine', 'Elementor Pro Custom Theme', 'Inter & Cardo Typography', 'Contact Form 7 API', 'Optimized CDN Caching'],
        'testimonial': {
            'quote': 'The platform gave our mission the national and international authority it deserved. It handled thousands of simultaneous cohort applicants effortlessly.',
            'author': 'Country Director',
            'role': 'Mirola Enterprise Nigeria'
        }
    },
    {
        'slug': 'beacon-corporate-realty',
        'title': 'Beacon Corporate Realty — Global Real Estate Platform & Visual Media System',
        'short_title': 'Beacon Corporate Realty',
        'client': 'Beacon Corporate Realty Ltd.',
        'category': 'Enterprise Corporate Web',
        'category_tag': 'Web Design',
        'industry': 'Commercial Real Estate',
        'year': '2025',
        'live_url': 'https://beaconcorporaterealty.com',
        'thumbnail': 'images/case-studies/beacon.jpg',
        'tagline': 'Bespoke Corporate Web Platform, 4K Aerial Showcase & Investor Inquiry Engine',
        'badge': 'Commercial Real Estate',
        'metrics': [
            {'value': '+50%', 'label': 'Investor Inquiries'},
            {'value': '100/100', 'label': 'Lighthouse SEO'},
            {'value': '4K Aerial', 'label': 'Visual Showcase'}
        ],
        'overview': (
            'Beacon Corporate Realty is an elite commercial real estate brokerage representing prime institutional assets. '
            'Vector Studioz designed and engineered a full-bleed luxury digital experience with immersive property portfolio tours, '
            'interactive site plans, and institutional investor inquiry workflows.'
        ),
        'challenge': (
            'Ultra-high-net-worth investors and commercial tenants demanded a digital portal reflecting the prestige of premier asset portfolios, with zero compromise on page speed.'
        ),
        'solution': (
            'We architected an ultra-fast headless portal featuring 4K architectural video showcases, structured data SEO, and bespoke inquiry funnels that increased qualified investor engagement.'
        ),
        'tech_stack': ['Next.js', 'React', 'Tailwind CSS', 'Framer Motion', 'Vercel Edge', 'Sanity CMS'],
        'testimonial': {
            'quote': 'Vector Studioz elevated our firm into a different tier of digital presentation. Institutional buyers and tenants now interact with our portfolio with unparalleled ease.',
            'author': 'Managing Broker',
            'role': 'Beacon Corporate Realty'
        }
    },
    {
        'slug': 'twist-studio',
        'title': 'Twist Studio / JumboDTG — Direct-to-Garment Custom Apparel E-Commerce Store',
        'short_title': 'Twist Studio / JumboDTG',
        'client': 'JumboDTG / Twist Studio',
        'category': 'Shopify & Custom UX',
        'category_tag': 'E-Commerce',
        'industry': 'Apparel & E-Commerce',
        'year': '2025',
        'live_url': 'https://jumbodtg.com/',
        'thumbnail': 'images/case-studies/jumbodtg.png',
        'tagline': 'High-Conversion Direct-to-Garment Customizer, Liquid Architecture & Mobile Checkout',
        'badge': 'Custom E-Commerce',
        'metrics': [
            {'value': '+25%', 'label': 'Checkout Conversions'},
            {'value': 'Mobile-First', 'label': 'Conversion Flow'},
            {'value': 'Liquid', 'label': 'Custom Architecture'}
        ],
        'overview': (
            'Twist Studio / JumboDTG is a state-of-the-art custom direct-to-garment apparel printing brand. '
            'Vector Studioz revamped the entire digital shopping journey with custom Shopify Liquid engineering, interactive mockup generators, and frictionless 1-click checkouts.'
        ),
        'challenge': (
            'Custom printed apparel requires complex multi-attribute variant selection (sizes, print placements, garment blanks) that previously overwhelmed mobile shoppers.'
        ),
        'solution': (
            'We engineered a tailored mobile-first Shopify theme with instantaneous live garment previews, simplified variant steppers, and lightning-fast checkout integrations.'
        ),
        'tech_stack': ['Shopify Plus', 'Custom Liquid', 'Tailwind CSS', 'JavaScript ES6+', 'Shopify App Bridge'],
        'testimonial': {
            'quote': 'Our cart abandonment dropped significantly after the launch. The product customizer is fast, intuitive, and generates orders on autopilot.',
            'author': 'Founder & Creative Lead',
            'role': 'JumboDTG'
        }
    },
    {
        'slug': 'resilient-solutions',
        'title': 'Resilient Solutions — Enterprise Cybersecurity & IT Advisory Digital Hub',
        'short_title': 'Resilient Solutions',
        'client': 'Resilient Solutions Group',
        'category': 'Cybersecurity & IT Advisory',
        'category_tag': 'SaaS & Cloud',
        'industry': 'Cybersecurity & Enterprise IT',
        'year': '2025',
        'live_url': 'https://timi-portfolio.onrender.com/work',
        'thumbnail': 'images/case-studies/resilient-solutions.png',
        'tagline': 'SOC-2 Compliance Portal, Interactive Threat Visualizer & Executive Advisory Portal',
        'badge': 'Enterprise Security',
        'metrics': [
            {'value': 'SOC-2', 'label': 'Compliance Standard'},
            {'value': 'Interactive', 'label': 'Cyber Risk Engine'},
            {'value': 'Next.js', 'label': 'Full-Stack Portal'}
        ],
        'overview': (
            'Resilient Solutions provides critical infrastructure cybersecurity and SOC-2 audit advisory for fintech and healthcare leaders. '
            'Vector Studioz crafted an authoritative, high-security digital hub featuring interactive cyber threat simulations and compliance roadmap calculators.'
        ),
        'challenge': (
            'Enterprise CISOs require immediate technical validation, ironclad trust markers, and transparent service methodology before initiating advisory consultations.'
        ),
        'solution': (
            'We built a modern Next.js platform showcasing security frameworks, real-time vulnerability scan demos, and an automated enterprise intake portal.'
        ),
        'tech_stack': ['Next.js 14', 'TypeScript', 'Tailwind CSS', 'Radix UI', 'Vercel Security Headers'],
        'testimonial': {
            'quote': 'Vector Studioz understood our technical domain deeply and delivered a platform that commands trust with enterprise security executives.',
            'author': 'Chief Information Security Officer',
            'role': 'Resilient Solutions'
        }
    },
    {
        'slug': 'mirola-ambassador',
        'title': 'Mirola Enterprises — High-Conversion Ambassador & Affiliate Platform',
        'short_title': 'Mirola Ambassador Platform',
        'client': 'Mirola Enterprises Ltd.',
        'category': 'Affiliate & Ambassador Engine',
        'category_tag': 'Operations',
        'industry': 'Brand Partnerships & Affiliate Growth',
        'year': '2025',
        'live_url': 'https://timi-portfolio.onrender.com/work',
        'thumbnail': 'images/case-studies/mirola-ambassador.png',
        'tagline': '4-Tier Ambassador Gamification, Real-Time Payout Tracking & Creator Dashboard',
        'badge': 'Creator Economy',
        'metrics': [
            {'value': '4 Tiers', 'label': 'Progression System'},
            {'value': 'Real-Time', 'label': 'Referral Telemetry'},
            {'value': 'React', 'label': 'Interactive UI Cards'}
        ],
        'overview': (
            'Mirola Enterprises powers international brand campaigns through high-performing creator ambassador programs. '
            'Vector Studioz engineered a gamified creator hub featuring multi-tier commission structures, instant link generation, and automated payout telemetries.'
        ),
        'challenge': (
            'Ambassadors lacked real-time visibility into attribution metrics, leading to drop-offs in campaign engagement and creator retention.'
        ),
        'solution': (
            'We designed an intuitive creator portal with gamified progression badges, live click-to-conversion analytics, and seamless referral asset downloads.'
        ),
        'tech_stack': ['React', 'Node.js API', 'Tailwind CSS', 'PostgreSQL', 'JWT Authentication'],
        'testimonial': {
            'quote': 'Our creator network expanded 4x because influencers love the transparent earnings dashboard. It completely transformed our partnership channel.',
            'author': 'Head of Growth',
            'role': 'Mirola Enterprises'
        }
    },
    {
        'slug': 'mirodata',
        'title': 'MIRODATA — Enterprise Role-Based Authentication & Data Hub',
        'short_title': 'MIRODATA',
        'client': 'MIRODATA Technologies',
        'category': 'Enterprise Data Portal & Auth',
        'category_tag': 'SaaS & Cloud',
        'industry': 'Data Intelligence & SaaS',
        'year': '2025',
        'live_url': 'https://timi-portfolio.onrender.com/work',
        'thumbnail': 'images/case-studies/mirodata.png',
        'tagline': 'Zero-Trust RBAC Access, Multi-Tenant Data Dashboards & Real-Time Query Visualization',
        'badge': 'Data Infrastructure',
        'metrics': [
            {'value': 'RBAC', 'label': 'Admin & Team Portals'},
            {'value': 'Secure', 'label': 'Session Management'},
            {'value': 'TypeScript', 'label': 'Robust Architecture'}
        ],
        'overview': (
            'MIRODATA serves enterprise analytics teams with distributed business intelligence. '
            'Vector Studioz engineered their secure front-end access portal featuring granular role-based access control (RBAC), '
            'SSO integration, and low-latency visualization widgets.'
        ),
        'challenge': (
            'The client needed a frictionless, enterprise-grade login and permission routing architecture meeting strict corporate compliance mandates.'
        ),
        'solution': (
            'We built a robust TypeScript application featuring hardware security key MFA support, session hijacking protection, and instant tenant switching.'
        ),
        'tech_stack': ['TypeScript', 'React', 'Next.js', 'NextAuth', 'Zod Validation', 'Tailwind CSS'],
        'testimonial': {
            'quote': 'The security implementation and UI execution are top notch. Our enterprise clients passed their internal security reviews on day one.',
            'author': 'VP of Engineering',
            'role': 'MIRODATA'
        }
    },
    {
        'slug': 'cleaner-spaces',
        'title': 'Cleaner Spaces — Commercial & Residential Cleaning Platform (New Jersey)',
        'short_title': 'Cleaner Spaces',
        'client': 'Cleaner Spaces LLC',
        'category': 'Web Platform & Quote Engine',
        'category_tag': 'Web Design',
        'industry': 'Local Services & Facilities',
        'year': '2025',
        'live_url': 'https://timi-portfolio.onrender.com/work',
        'thumbnail': 'images/case-studies/cleaner-spaces.png',
        'tagline': 'Dynamic Instant Quote Calculator, Geo-Targeted Local SEO & On-Demand Booking',
        'badge': 'Booking Engine',
        'metrics': [
            {'value': 'Instant', 'label': 'Quote Calculator'},
            {'value': 'Local SEO', 'label': 'Geo-Targeting NJ'},
            {'value': 'WordPress', 'label': 'High Conversion'}
        ],
        'overview': (
            'Cleaner Spaces provides residential and commercial cleaning throughout New Jersey. '
            'Vector Studioz engineered a high-converting web booking engine that delivers instant custom estimates and automated dispatch scheduling.'
        ),
        'challenge': (
            'Manual phone estimates caused significant lead leakage, particularly during evening hours when residential clients were searching for cleaning services.'
        ),
        'solution': (
            'We developed an intuitive dynamic calculator taking square footage, service type, and frequency, instantly booking appointments into the dispatch CRM.'
        ),
        'tech_stack': ['WordPress Engine', 'Custom PHP Calculator', 'Stripe Payments', 'Twilio API', 'Tailwind CSS'],
        'testimonial': {
            'quote': 'Over 70% of our bookings now come straight through the online calculator without our team needing to pick up the phone.',
            'author': 'Operations Manager',
            'role': 'Cleaner Spaces NJ'
        }
    },
    {
        'slug': '5th-element-media',
        'title': '5th Element Media Group — Multi-Brand Client Websites Portfolio',
        'short_title': '5th Element Media Group',
        'client': '5th Element Media Group',
        'category': 'Creative Agency & Multi-Brand',
        'category_tag': 'Web Design',
        'industry': 'Media & Digital Publishing',
        'year': '2025',
        'live_url': 'https://timi-portfolio.onrender.com/work',
        'thumbnail': 'images/case-studies/5th-element.png',
        'tagline': 'Bespoke Multi-Brand Portfolio, Fluid GSAP Micro-Interactions & Headless CMS',
        'badge': 'Creative Portfolio',
        'metrics': [
            {'value': '+40%', 'label': 'Client Engagement'},
            {'value': 'Framer', 'label': 'Fluid UI Animations'},
            {'value': 'Multi-Brand', 'label': 'CMS Architecture'}
        ],
        'overview': (
            '5th Element Media Group represents a portfolio of modern digital publishing brands. '
            'Vector Studioz crafted an artistic showcase website featuring cinematic micro-interactions, responsive editorial grids, and seamless video streaming.'
        ),
        'challenge': (
            'Presenting vastly different media properties under one unified parent agency identity without diluting each subsidiary brand.'
        ),
        'solution': (
            'We designed an interactive dark luxury layout with dynamic brand filters, custom cursors, and responsive media galleries.'
        ),
        'tech_stack': ['HTML5', 'GSAP Animation', 'Framer Motion', 'Tailwind CSS', 'Vercel Deployment'],
        'testimonial': {
            'quote': 'The motion design and aesthetic polish reflect our creative standards perfectly. It has been a powerful client conversion tool.',
            'author': 'Creative Director',
            'role': '5th Element Media Group'
        }
    },
    {
        'slug': 'aliola-global-services',
        'title': 'Aliola Global Services — Corporate Digital Transformation Platform',
        'short_title': 'Aliola Global Services',
        'client': 'Aliola Global Services Ltd.',
        'category': 'Corporate Digital Transformation',
        'category_tag': 'Operations',
        'industry': 'Global Trade & Logistics',
        'year': '2025',
        'live_url': 'https://timi-portfolio.onrender.com/work',
        'thumbnail': 'images/case-studies/aliola.png',
        'tagline': 'Cross-Border Logistics Tracking, Automated Procurement & Corporate Portal',
        'badge': 'Global Logistics',
        'metrics': [
            {'value': '-35%', 'label': 'Operational Overhead'},
            {'value': 'Modern', 'label': 'Corporate Portal'},
            {'value': 'Process', 'label': 'Digital Automation'}
        ],
        'overview': (
            'Aliola Global Services coordinates cross-border supply chain logistics and corporate procurement. '
            'Vector Studioz delivered an end-to-end digital transformation, consolidating customer tracking, quotation engines, and vendor management.'
        ),
        'challenge': (
            'Global procurement clients suffered from fragmented tracking systems and manual customs documentation processing.'
        ),
        'solution': (
            'We architected an integrated web platform with real-time shipment status lookups, automated bill-of-lading generation, and responsive client dashboards.'
        ),
        'tech_stack': ['React', 'Next.js', 'Tailwind CSS', 'Node.js Backend', 'PostgreSQL'],
        'testimonial': {
            'quote': 'The platform modernized our entire customer-facing operation. International partners praise the clarity and speed of our new tracking hub.',
            'author': 'Managing Director',
            'role': 'Aliola Global Services'
        }
    },
    {
        'slug': 'tom-ojo-sports-academy',
        'title': 'Tom Ojo Sports Academy — Global Athlete Discovery & Sports Platform',
        'short_title': 'Tom Ojo Sports Academy',
        'client': 'Tom Ojo Sports Foundation',
        'category': 'Sports & Talent Discovery',
        'category_tag': 'Web Design',
        'industry': 'Sports Athletics & Youth Discovery',
        'year': '2025',
        'live_url': 'https://timi-portfolio.onrender.com/work',
        'thumbnail': 'images/case-studies/tom-ojo.png',
        'tagline': 'Scout Scouting Portals, Live Tournament Broadcasts & Athlete Profile CMS',
        'badge': 'Sports Academy',
        'metrics': [
            {'value': 'Streamlined', 'label': 'Player Registration'},
            {'value': 'Live Updates', 'label': 'Event Broadcast'},
            {'value': 'CMS', 'label': 'Content Management'}
        ],
        'overview': (
            'Tom Ojo Sports Academy scouts, develops, and mentors top youth athletic talent for international collegiate and professional drafts. '
            'Vector Studioz developed an interactive scouting portal with video highlight reels, verified athletic stats, and tournament schedules.'
        ),
        'challenge': (
            'International scouts and college recruiters needed a verified, centralized digital platform to evaluate athlete performance data and game footage.'
        ),
        'solution': (
            'We built a media-rich sports portal featuring athlete profiles with verified physical metrics, video highlights, and automated tryout registration.'
        ),
        'tech_stack': ['WordPress Engine', 'Custom Athlete Post Types', 'YouTube & Vimeo API', 'Tailwind CSS', 'Cloudflare Stream'],
        'testimonial': {
            'quote': 'Thanks to Vector Studioz, our athletes now have an international digital stage. Several European scouts discovered our academy directly through the portal.',
            'author': 'Head Coach & Founder',
            'role': 'Tom Ojo Sports Academy'
        }
    }
]
