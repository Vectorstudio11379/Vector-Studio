from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

header = soup.find(class_='navbar-4')
if not header:
    print("No navbar-4 found")
else:
    for a in header.find_all('a'):
        href = a.get('href', '')
        text = a.get_text(strip=True)
        classes = a.get('class', [])
        print(f"{href:40} | {text:35} | {classes}")
