# Synchronize template_header.html and template_footer.html across all pages
# and remove all remaining pricing references

import glob
import re

with open('template_header.html', 'r', encoding='utf-8') as f:
    header_template = f.read().strip()

with open('template_footer.html', 'r', encoding='utf-8') as f:
    footer_template = f.read().strip()

PAGES = [
    f for f in glob.glob('*.html') 
    if f not in ['template_header.html', 'template_footer.html', 'navbar_current.html']
]

print(f"Starting synchronization of {len(PAGES)} pages...")

header_regex = re.compile(r'<header[\s\S]*?</header>', re.IGNORECASE)
footer_regex = re.compile(r'<footer[\s\S]*?</footer>', re.IGNORECASE)

synced_count = 0

for page in sorted(PAGES):
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace header
    if header_regex.search(content):
        content = header_regex.sub(lambda m: header_template, content, count=1)
    else:
        print(f"Warning: No <header> tag found in {page}")

    # 2. Replace footer
    if footer_regex.search(content):
        content = footer_regex.sub(lambda m: footer_template, content, count=1)
    else:
        print(f"Warning: No <footer> tag found in {page}")

    # 3. Ensure vector-nav.css in head
    if 'vector-nav.css' not in content:
        head_end = re.search(r'</head>', content, re.IGNORECASE)
        if head_end:
            content = content[:head_end.start()] + '  <link rel="stylesheet" href="vector-nav.css"/>\n' + content[head_end.start():]

    # 4. Ensure vector-nav.js before </body>
    if 'vector-nav.js' not in content:
        body_end = re.search(r'</body>', content, re.IGNORECASE)
        if body_end:
            content = content[:body_end.start()] + '  <script src="vector-nav.js"></script>\n' + content[body_end.start():]

    # 5. Sanitize any remaining pricing links/buttons in page body
    content = content.replace('href="pricing.html"', 'href="contact-us.html"')
    content = content.replace('href="/pricing.html"', 'href="/contact-us.html"')
    content = content.replace('href="https://app.vectorstudioz.com/pricing"', 'href="contact-us.html"')
    content = content.replace('View Pricing &amp; Retainers', 'Start a Project')
    content = content.replace('View Pricing & Retainers', 'Start a Project')
    content = content.replace('View Plans &amp; Pricing', 'Start a Project')
    content = content.replace('View Plans & Pricing', 'Start a Project')
    content = content.replace('Explore Retainers', 'Start a Project')

    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)
        
    synced_count += 1
    print(f"[OK] Synchronized {page}")

print(f"\nSuccessfully synchronized {synced_count} pages with master Vector Studioz header & footer!")
