import os
from bs4 import BeautifulSoup

files = sorted([f for f in os.listdir('.') if f.endswith('.html') and not f.endswith('.bak')])
for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    soup = BeautifulSoup(content, 'html.parser')
    h = soup.find(class_='navbar-4') or soup.find(class_='site-header') or soup.find('header')
    footer = soup.find(class_='footer') or soup.find(class_='site-footer') or soup.find('footer')
    print(f"{f:32} | Header: {bool(h)} ({h.name if h else 'none'}) | Footer: {bool(footer)} ({footer.name if footer else 'none'})")
