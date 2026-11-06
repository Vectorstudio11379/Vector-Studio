import os
from bs4 import BeautifulSoup

with open('template_header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

with open('template_footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

all_files = sorted([f for f in os.listdir('.') if f.endswith('.html') and not f.endswith('.bak') and not f.startswith('test_') and f not in ['navbar_current.html', 'template_header.html', 'template_footer.html']])

already_done = ['about.html', 'careers.html', 'contact-us.html', 'pricing.html']
pages_to_update = [f for f in all_files if f not in already_done]

print(f"Total pages to update: {len(pages_to_update)}")

for fname in pages_to_update:
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    old_nav = soup.find(class_='navbar-4') or soup.find(class_='site-header') or soup.find('header')
    old_footer = soup.find('footer') or soup.find(class_='site-footer') or soup.find(class_='footer')
    
    print(f"{fname:32} | Nav found: {old_nav.name if old_nav else 'None':<7} | Footer found: {old_footer.name if old_footer else 'None':<7}")
