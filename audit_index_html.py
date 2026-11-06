from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("1. HERO SLIDER SLIDES:")
slider = soup.find(class_='hero-feature-prime')
if slider:
    slides = slider.find_all(class_='hero-feature-slide')
    print(f"Found {len(slides)} slides:")
    for idx, s in enumerate(slides):
        title = s.find(class_='hero-feature-score')
        preview = s.find(class_='hero-slide-preview')
        items = [p.get_text().strip() for p in s.find_all(class_='paragraph hero-feature-paragraph') if p != title]
        print(f"  Slide {idx+1}: {preview.get_text() if preview else ''} -> {title.get_text() if title else ''}")
        print(f"    Items: {items}")

print("\n2. TOKEN SECTION:")
token_sec = soup.find(id='our-token')
if token_sec:
    print("Found #our-token section! Parent tag:", token_sec.name, "Classes:", token_sec.get('class'))
    print("Heading text:", [h.get_text().strip() for h in token_sec.find_all(['h1', 'h2', 'h3'])[:5]])

print("\n3. ECOSYSTEM SECTION:")
eco_sec = soup.find(id='ecosystem')
if eco_sec:
    print("Found #ecosystem section! Heading text:", [h.get_text().strip() for h in eco_sec.find_all(['h1', 'h2', 'h3'])[:5]])

print("\n4. AWARDS SECTION:")
awards_sec = soup.find(class_='awards-section')
if awards_sec:
    items = awards_sec.find_all(class_='awards-name')
    print(f"Found {len(items)} award items:")
    for it in items[:6]:
        clean_text = it.get_text().replace('\n', ' ').replace('\u2028', ' ').strip()
        print("  Award:", clean_text.encode('ascii', 'ignore').decode('ascii'))
