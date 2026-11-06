from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

old_nav = soup.find(class_='navbar-4') or soup.find(class_='site-header')
old_footer = soup.find(class_='footer') or soup.find(class_='site-footer')

if old_nav:
    print("Old Nav tag:", old_nav.name)
    print("Old Nav class:", old_nav.get('class'))
    str_nav = str(old_nav)
    print("Old Nav length:", len(str_nav))
    idx = content.find(str_nav[:100])
    print("Old Nav substring found in content:", idx != -1)

if old_footer:
    print("Old Footer tag:", old_footer.name)
    print("Old Footer class:", old_footer.get('class'))
    # In index.html, is old_footer wrapped in <footer> tag?
    parent_footer = old_footer.find_parent('footer')
    if parent_footer:
        print("Old Footer is inside parent <footer", parent_footer.get('class'))
    str_footer = str(parent_footer if parent_footer else old_footer)
    print("Old Footer length:", len(str_footer))
