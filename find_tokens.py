with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

s = c.find('fs-cmsslider-element="list-42"')
print("FOUND list-42 AT:", s)
# find next section or major tag
for token in ['</section>', '<div class="vertical-line', '<section', 'id="our-token"', 'id="']:
    idx = c.find(token, s)
    print(f"Token '{token}': found at {idx}")
