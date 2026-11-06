from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

token_sec = soup.find(id='our-token')
if token_sec:
    # Print the headings, paragraphs, and buttons inside our-token
    print("=== OUR-TOKEN SECTION ===")
    for el in token_sec.find_all(['h2', 'h3', 'p', 'a']):
        txt = el.get_text().strip()
        if txt and len(txt) < 120:
            print(f"<{el.name}>: {txt}")
