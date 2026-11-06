from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

footer = soup.find(class_='site-footer') or soup.find(class_='footer')
if footer:
    print(f"Total links in footer: {len(footer.find_all('a'))}")
    for a in footer.find_all('a'):
        href = a.get('href', '')
        text = a.get_text(strip=True)
        print(f"  {href:45} | {text:30}")
