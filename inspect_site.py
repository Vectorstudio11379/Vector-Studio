import os
import re
from bs4 import BeautifulSoup

def inspect():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    print("Title:", soup.title.string if soup.title else None)
    
    # Check nav / header elements
    navs = soup.find_all(['nav', 'header'])
    print(f"Found {len(navs)} nav/header elements:")
    for n in navs:
        print(n.name, n.get('class'), n.get('id'))
        # print some children
        links = n.find_all('a')
        print(f"  Contains {len(links)} links:")
        for a in links[:15]:
            print(f"    href: {a.get('href')} | text: {a.get_text(strip=True)[:40]}")

    # Also search for class containing nav
    class_navs = soup.find_all(class_=re.compile(r'nav|menu|header', re.I))
    print(f"\nFound {len(class_navs)} elements with class matching nav/menu/header:")
    for cn in class_navs[:10]:
        print(cn.name, cn.get('class'), cn.get('id'))

    print("\nAll HTML files in directory:")
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    print(files)

if __name__ == '__main__':
    inspect()
