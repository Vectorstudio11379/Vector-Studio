from bs4 import BeautifulSoup

def inspect_file(filename):
    print("=" * 60)
    print(f"FILE: {filename}")
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    header = soup.find(class_='navbar-4') or soup.find(class_='site-header')
    if not header:
        header = soup.find('nav')
    print("Header tag:", header.name if header else None, header.get('class') if header else None)
    
    if header:
        links = header.find_all('a')
        print(f"Total links in header: {len(links)}")
        for a in links[:20]:
            print(f"  href: {a.get('href', ''):40} | text: {a.get_text(strip=True)[:30]}")

inspect_file('about.html')
inspect_file('case-studies.html')
inspect_file('smart-contract-auditor.html')
inspect_file('contact-us.html')
