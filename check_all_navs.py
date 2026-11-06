import os
from bs4 import BeautifulSoup

for f in sorted(os.listdir('.')):
    if f.endswith('.html') and not f.endswith('.bak'):
        with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
            soup = BeautifulSoup(fp.read(), 'html.parser')
            header = soup.find(class_='navbar-4') or soup.find(class_='site-header') or soup.find('header') or soup.find('nav')
            links_summary = []
            if header:
                for a in header.find_all('a')[:8]:
                    href = a.get('href', '')
                    text = a.get_text(strip=True)[:20]
                    links_summary.append(f"{href} ({text})")
            print(f"{f:32} | Nav found: {bool(header)} | Links ({len(header.find_all('a')) if header else 0}): {', '.join(links_summary[:4])}")
