import os
from bs4 import BeautifulSoup

html_files = sorted([f for f in os.listdir('.') if f.endswith('.html') and not f.endswith('.bak') and f != 'navbar_current.html'])

for fname in html_files:
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    vs_nav = soup.find('header', class_='vs-navbar')
    old_nav = soup.find(class_='navbar-4') or soup.find(class_='site-header')
    
    vs_footer = soup.find('footer', class_='site-footer')
    old_footer = soup.find(class_='site-footer') or soup.find(class_='footer')
    has_nav_css = 'vector-nav.css' in str(soup.head)
    has_nav_js = 'vector-nav.js' in str(soup)
    
    print(f"{fname:32} | VS Nav: {bool(vs_nav):<5} | Old Nav: {bool(old_nav):<5} | VS CSS: {has_nav_css:<5} | VS JS: {has_nav_js:<5}")
