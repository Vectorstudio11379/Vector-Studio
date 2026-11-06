import os
from bs4 import BeautifulSoup

for f in sorted(os.listdir('.')):
    if f.endswith('.html') and not f.endswith('.bak') and not f.startswith('test_') and f not in ['navbar_current.html', 'template_header.html', 'template_footer.html']:
        soup = BeautifulSoup(open(f, encoding='utf-8', errors='ignore').read(), 'html.parser')
        t = soup.find('title')
        print(f"{f:32} | Title: {t.text if t else 'None'}")
