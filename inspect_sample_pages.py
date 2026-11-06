import os
from bs4 import BeautifulSoup

pages = ['ai-agents.html', 'case-studies.html', 'blog.html', 'brand-kit.html', 'smart-contract-auditor.html']

for p in pages:
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    h1 = soup.find('h1')
    title = soup.find('title')
    print(f"Page: {p:25} | Title: {title.text if title else 'No title'} | H1: {h1.text.strip()[:40] if h1 else 'No H1'}")
