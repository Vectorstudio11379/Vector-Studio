from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

with open('template_header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

with open('template_footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

soup = BeautifulSoup(content, 'html.parser')

# Check nav
old_nav = soup.find(class_='navbar-4') or soup.find(class_='site-header')
new_nav_soup = BeautifulSoup(header_html, 'html.parser')

if old_nav:
    old_nav.replace_with(new_nav_soup)
    print("Replaced old nav with new vs-navbar")

# Check footer
old_footer = soup.find(class_='footer') or soup.find(class_='site-footer')
parent_footer = old_footer.find_parent('footer') if old_footer else None
target_footer = parent_footer if parent_footer else old_footer

new_footer_soup = BeautifulSoup(footer_html, 'html.parser')

if target_footer:
    target_footer.replace_with(new_footer_soup)
    print("Replaced old footer with new vs-footer")

# Add css link to head if not present
if not soup.find('link', href='vector-nav.css'):
    css_tag = soup.new_tag('link', rel='stylesheet', href='vector-nav.css')
    soup.head.append(css_tag)
    print("Added vector-nav.css to head")

# Add js script to body if not present
if not soup.find('script', src='vector-nav.js'):
    js_tag = soup.new_tag('script', src='vector-nav.js')
    soup.body.append(js_tag)
    print("Added vector-nav.js to body")

with open('test_index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Wrote test_index.html successfully!")
