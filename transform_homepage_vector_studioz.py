import re
from bs4 import BeautifulSoup

def transform_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # 1. Transform the Hero Feature Slider
    slider = soup.find(class_='hero-feature-prime')
    if slider:
        slides = slider.find_all(class_='hero-feature-slide')
        agency_slides_data = [
            {
                'preview': 'DESIGNING IN…',
                'category': 'UI/UX STUDIO',
                'title': 'BESPOKE WEB DESIGN & UI/UX',
                'bullets': ['Design Systems & Tokens', 'High-Fidelity Figma Prototypes', 'Conversion Rate Architecture', 'Interactive Micro-Motion']
            },
            {
                'preview': 'ENGINEERING IN…',
                'category': 'FULL-STACK LAB',
                'title': 'WEB & CLOUD ENGINEERING',
                'bullets': ['Next.js & React 19', 'Headless Webflow & Sanity', 'Global Edge Serverless', 'Scalable Microservices']
            },
            {
                'preview': 'AUTOMATING IN…',
                'category': 'AI WORKFLOWS',
                'title': 'AI AUTOMATION & AGENTS',
                'bullets': ['Autonomous Agent Systems', 'Custom LLM Pipelines', 'Enterprise RAG Architectures', 'Smart CRM & API Workflows']
            },
            {
                'preview': 'RENDERING IN…',
                'category': '3D STUDIO',
                'title': '3D & WEBGL EXPERIENCES',
                'bullets': ['Interactive Three.js', 'Custom GLSL Shaders', 'Fluid 60 FPS Canvas', 'Spatial Web Interactions']
            },
            {
                'preview': 'BUILDING IN…',
                'category': 'MOBILE LAB',
                'title': 'MOBILE APP ENGINEERING',
                'bullets': ['Flutter & React Native', '120Hz Gesture Animations', 'Offline-First Synced Data', 'App Store & Play Store CI/CD']
            }
        ]

        for idx, slide in enumerate(slides[:len(agency_slides_data)]):
            data = agency_slides_data[idx]
            prev = slide.find(class_='hero-slide-preview')
            if prev:
                prev.string = data['preview']
            cat = slide.find(class_='paragraph hero-feature-paragraph hero-slide')
            if cat:
                cat.string = data['category']
            score = slide.find(class_='hero-feature-score')
            if score:
                score.string = data['title']
            
            bullet_divs = slide.find_all(class_='hero-feature')
            for b_idx, b_div in enumerate(bullet_divs):
                p = b_div.find('p')
                if p and b_idx < len(data['bullets']):
                    p.string = data['bullets'][b_idx]

    # 2. Transform the Awards marquee
    awards = soup.find(class_='awards-section')
    if awards:
        names = awards.find_all(class_='awards-name')
        replacements = {
            'gas grant of the year': 'CSS Design Awards<br/><span class="awards-text-alt">Special Kudos Winner</span>',
            'Ecosystem Catalyst Award': 'Awwwards Site of the Day<br/><span class="awards-text-alt">Honorable Mention</span>',
            'BeInCrypto Excellence': 'Webby Awards Nominee<br/><span class="text-span-31">Best Visual Design</span>',
            '#1 Web3 App': '#1 Product of the Day<br/><span class="awards-text-alt">by ProductHunt</span>',
            'Innovation Excellence': 'Top Web Agency 2025<br/><span class="awards-text-alt">by Clutch.co</span>',
            'from BNB': 'from Global Design Jury'
        }
        for name in names:
            txt = name.decode_contents()
            for k, v in replacements.items():
                if k.lower() in txt.lower():
                    name.clear()
                    name.append(BeautifulSoup(v, 'html.parser'))
                    break

    # 3. Transform #our-token section into Agency OS & Operating Framework
    token_sec = soup.find(id='our-token')
    if token_sec:
        # Update any buy / claim buttons
        for a in token_sec.find_all('a'):
            t = a.get_text().strip()
            if 'Buy' in t:
                a['href'] = 'contact-us.html'
                for s in a.strings:
                    if 'Buy' in s:
                        s.replace_with('Start a Project')
            elif 'Claim' in t:
                a['href'] = 'pricing.html'
                for s in a.strings:
                    if 'Claim' in s or 'Token' in s:
                        s.replace_with('View Retainer Models')
            elif 'token' in t.lower():
                a['href'] = 'services.html'

        # Replace text inside token section
        for s in list(token_sec.strings):
            txt = str(s)
            modified = False
            new_txt = txt
            if 'token' in new_txt.lower():
                new_txt = re.sub(r'\btoken(s)?\b', 'sprint\\1', new_txt, flags=re.IGNORECASE)
                modified = True
            if 'staking' in new_txt.lower():
                new_txt = re.sub(r'\bstaking\b', 'retainer', new_txt, flags=re.IGNORECASE)
                modified = True
            if 'burn' in new_txt.lower():
                new_txt = re.sub(r'\bburn(ing)?\b', 'delivery', new_txt, flags=re.IGNORECASE)
                modified = True
            if modified:
                s.replace_with(new_txt)

    # 4. Transform Blog / Case Studies items on the homepage
    blog_container = soup.find(id='media-blog-container') or soup.find(class_='media-blog-container')
    if blog_container:
        articles = [
            ("How to Ship a High-Converting SaaS Redesign That Drives 3x Growth", "UI/UX & Conversion Architecture"),
            ("Building 60 FPS WebGL Interactive Experiences with Three.js", "3D & Creative Engineering"),
            ("How Autonomous AI Agents Are Transforming Modern Enterprise Workflows", "AI Automation & Workflows"),
            ("Designing Scalable Multi-Brand Design Systems in Figma for Fast Handoff", "Design Systems & Tokens"),
            ("Micro-Interactions and Motion: The Blueprint for Category-Defining Products", "Motion Design & UI/UX"),
            ("From Concept to App Store: Full-Stack Flutter & React Native Engineering", "Cross-Platform Mobile Apps")
        ]
        titles = blog_container.find_all(class_='media-slider-title')
        for i, t in enumerate(titles):
            if i < len(articles):
                t.string = articles[i][0]

    # 5. Global text cleanups across index.html
    html_updated = str(soup)

    # Clean legacy CoinGPT/crypto strings in index.html
    cleanups = [
        ('Real-Time Data Insights', 'Design Systems & Tokens'),
        ('On-Chain Analysis', 'High-Fidelity Figma Prototypes'),
        ('Token Research', 'Conversion Rate Architecture'),
        ('Live Market Updates', 'Interactive Micro-Motion'),
        ('on-chain llm training', 'Next.js & React 19'),
        ('decentralized ai', 'Headless Webflow & Sanity'),
        ('GPU\xa0Marketplace', 'Global Edge Serverless'),
        ('GPU Marketplace', 'Global Edge Serverless'),
        ('AI\xa0Data Marketlace', 'Scalable Microservices'),
        ('AI Data Marketlace', 'Scalable Microservices'),
        ('GENERATE anD AUDIT', 'Autonomous Agent Systems'),
        ('detect exploits', 'Custom LLM Pipelines'),
        ('Deploy CONTRACTS On-CHAIN', 'Enterprise RAG Architectures'),
        ('Gas optimization', 'Smart CRM & API Workflows'),
        ('no-code AI agent launchpad', 'Interactive Three.js'),
        ('TRAIN YOUR OWN AGENT', 'Custom GLSL Shaders'),
        ('BIND to EXISTING CHAT', 'Fluid 60 FPS Canvas'),
        ('BIND to A TOKEN', 'Spatial Web Interactions'),
        ('Text-to-Image AI', 'Flutter & React Native'),
        ('On-Chain Minting', '120Hz Gesture Animations'),
        ('Seamless NFT Creation', 'Offline-First Synced Data'),
        ('WEB3 AI CHATBOT', 'BESPOKE WEB DESIGN & UI/UX'),
        ('AI Virtual Machine', 'WEB & CLOUD ENGINEERING'),
        ('SMART CONTRACT AUDITOR', 'AI AUTOMATION & AGENTS'),
        ('AI AGENTS LAUNCHER', '3D & WEBGL EXPERIENCES'),
        ('AI NFT GENERATOR', 'MOBILE APP ENGINEERING'),
        ('AI TOOLS', 'AGENCY DISCIPLINES'),
        ('from BNB Chai', 'from CSS Design Awards'),
        ('from BNB Chain', 'from Awwwards'),
        ('by Binance', 'by Clutch.co'),
        ('Smart Contract Auditor', 'Custom Software Engineering'),
        ('Smart Contract Generator', 'Mobile App Development'),
        ('AI NFT Generator', '3D & WebGL Studio'),
        ('crypto-aware AI', 'modern digital agency solutions'),
        ('on-chain data', 'user data and analytics'),
        ('Web3-native AI', 'modern bespoke digital agency'),
        ('blockchain applications', 'enterprise software applications'),
        ('CoinGPT', 'Vector Studioz'),
        ('coingpt.tech', 'vectorstudioz.com')
    ]

    for old, new in cleanups:
        html_updated = html_updated.replace(old, new)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_updated)

    print("Index.html transformed successfully!")

if __name__ == '__main__':
    transform_index()
