from bs4 import BeautifulSoup

with open('about.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

header = soup.find('header', class_='vs-navbar')
footer = soup.find('footer', class_='site-footer')

with open('template_header.html', 'w', encoding='utf-8') as f:
    f.write(str(header))

with open('template_footer.html', 'w', encoding='utf-8') as f:
    f.write(str(footer))

print("Saved template_header.html (len:", len(str(header)), ") and template_footer.html (len:", len(str(footer)), ")")
