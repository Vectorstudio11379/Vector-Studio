from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

header = soup.find(class_='navbar-4')
if header:
    print("Found navbar-4. HTML preview:")
    with open('navbar_current.html', 'w', encoding='utf-8') as out:
        out.write(header.prettify())
    print("Saved to navbar_current.html (lines:", len(header.prettify().splitlines()), ")")
