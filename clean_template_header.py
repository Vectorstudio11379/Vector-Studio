with open('template_header.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('class="vs-nav-link active"', 'class="vs-nav-link"')
c = c.replace('class="vs-dropdown-item active"', 'class="vs-dropdown-item"')
c = c.replace('class="vs-mobile-sublink active"', 'class="vs-mobile-sublink"')

with open('template_header.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Cleaned active classes from template_header.html')
