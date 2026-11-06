from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

nav = soup.find(class_='navbar-4') or soup.find(class_='site-header')
footer = soup.find(class_='footer') or soup.find(class_='site-footer')

print('Found nav in index.html:', nav is not None)
if nav:
    print('Nav tag:', nav.name, 'parent:', nav.parent.name if nav.parent else 'None')
    print('Nav classes:', nav.get('class'))

print('Found footer in index.html:', footer is not None)
if footer:
    print('Footer tag:', footer.name, 'parent:', footer.parent.name if footer.parent else 'None')
    print('Footer classes:', footer.get('class'))
