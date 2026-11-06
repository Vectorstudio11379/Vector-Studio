import os
import shutil
from bs4 import BeautifulSoup

BACKUP_DIR = 'backup_pages'
os.makedirs(BACKUP_DIR, exist_ok=True)

with open('template_header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

with open('template_footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

pages_already_done = {'about.html', 'careers.html', 'contact-us.html', 'pricing.html'}

all_html_files = sorted([
    f for f in os.listdir('.') 
    if f.endswith('.html') 
    and not f.endswith('.bak') 
    and not f.startswith('test_') 
    and f not in ['navbar_current.html', 'template_header.html', 'template_footer.html']
])

known_pages = {
    '/about': 'about.html', 'about': 'about.html',
    '/pricing': 'pricing.html', 'pricing': 'pricing.html',
    '/careers': 'careers.html', 'careers': 'careers.html',
    '/contact': 'contact-us.html', 'contact': 'contact-us.html',
    '/contact-us': 'contact-us.html', 'contact-us': 'contact-us.html',
    '/case-studies': 'case-studies.html', 'case-studies': 'case-studies.html',
    '/blog': 'blog.html', 'blog': 'blog.html',
    '/brand-kit': 'brand-kit.html', 'brand-kit': 'brand-kit.html',
    '/verify': 'verify.html', 'verify': 'verify.html',
    '/videos': 'videos.html', 'videos': 'videos.html',
    '/privacy-policy': 'privacy-policy.html', 'privacy-policy': 'privacy-policy.html',
    '/tos': 'tos.html', 'tos': 'tos.html',
    '/cookies': 'cookies.html', 'cookies': 'cookies.html',
    '/eligibility-policy': 'eligibility-policy.html', 'eligibility-policy': 'eligibility-policy.html',
    '/ai-agents': 'ai-agents.html', 'ai-agents': 'ai-agents.html',
    '/ai-crypto-alerts': 'ai-crypto-alerts.html', 'ai-crypto-alerts': 'ai-crypto-alerts.html',
    '/ai-trading-assistant': 'ai-trading-assistant.html', 'ai-trading-assistant': 'ai-trading-assistant.html',
    '/ai-web3-news': 'ai-web3-news.html', 'ai-web3-news': 'ai-web3-news.html',
    '/crypto-ai-hub': 'crypto-ai-hub.html', 'crypto-ai-hub': 'crypto-ai-hub.html',
    '/crypto-compliance-assistant': 'crypto-compliance-assistant.html', 'crypto-compliance-assistant': 'crypto-compliance-assistant.html',
    '/smart-contract-auditor': 'smart-contract-auditor.html', 'smart-contract-auditor': 'smart-contract-auditor.html',
    '/smart-contract-generator': 'smart-contract-generator.html', 'smart-contract-generator': 'smart-contract-generator.html',
    '/web3-ai-grant': 'web3-ai-grant.html', 'web3-ai-grant': 'web3-ai-grant.html',
    '/web3-chatbot': 'web3-chatbot.html', 'web3-chatbot': 'web3-chatbot.html',
    '/': 'index.html',
    'https://www.vectorstudioz.com/': 'index.html',
    'https://www.vectorstudioz.com': 'index.html',
}

def update_page(fname):
    print(f"Updating {fname}...")
    backup_path = os.path.join(BACKUP_DIR, fname)
    if not os.path.exists(backup_path):
        shutil.copy2(fname, backup_path)
    
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # 1. Title update
    title_tag = soup.find('title')
    if title_tag and title_tag.string:
        new_title = title_tag.string.replace('CoinGPT', 'Vector Studioz').replace('ChainGPT', 'Vector Studioz')
        title_tag.string = new_title
    
    # 2. Add Google Fonts and vector-nav.css in head
    if soup.head:
        if not soup.find('link', href=lambda h: h and 'vector-nav.css' in h):
            css_link = soup.new_tag('link', rel='stylesheet', href='vector-nav.css')
            soup.head.append(css_link)
        
        if not soup.find('link', href=lambda h: h and 'fonts.googleapis.com' in h):
            font_pre1 = soup.new_tag('link', rel='preconnect', href='https://fonts.googleapis.com')
            font_pre2 = soup.new_tag('link', rel='preconnect', href='https://fonts.gstatic.com', crossorigin='anonymous')
            font_link = soup.new_tag('link', rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Roboto+Mono:wght@400;500;700&display=swap')
            soup.head.append(font_pre1)
            soup.head.append(font_pre2)
            soup.head.append(font_link)
    
    # 3. Replace Navigation
    old_nav = soup.find(class_='navbar-4') or soup.find(class_='site-header')
    if old_nav:
        new_nav_soup = BeautifulSoup(header_html, 'html.parser')
        old_nav.replace_with(new_nav_soup)
    
    # 4. Replace Footer
    old_footer = soup.find('footer') or soup.find(class_='site-footer') or soup.find(class_='footer')
    if old_footer:
        parent_footer = old_footer.find_parent('footer')
        target_footer = parent_footer if parent_footer else old_footer
        new_footer_soup = BeautifulSoup(footer_html, 'html.parser')
        target_footer.replace_with(new_footer_soup)
    
    # 5. Add vector-nav.js
    if soup.body:
        if not soup.find('script', src=lambda s: s and 'vector-nav.js' in s):
            js_tag = soup.new_tag('script', src='vector-nav.js')
            soup.body.append(js_tag)
    
    # 6. Sanitize links in the entire page
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href in known_pages:
            a['href'] = known_pages[href]
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print(f"  Successfully updated {fname}")

for fname in all_html_files:
    if fname not in pages_already_done:
        update_page(fname)
    else:
        # For pages already done, still sanitize links
        with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        soup = BeautifulSoup(content, 'html.parser')
        modified = False
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href in known_pages and a['href'] != known_pages[href]:
                a['href'] = known_pages[href]
                modified = True
        if modified:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"  Sanitized links in {fname}")

print("\n--- ALL PAGES UPDATED SUCCESSFULLY ---")
