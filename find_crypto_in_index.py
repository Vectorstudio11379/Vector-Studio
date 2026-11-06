from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

keywords = ['bnb', 'blockchain', 'solidity', 'minting', 'chaingpt', 'binance', 'nft', 'smart contract', 'token']

results = []
for tag in soup.find_all(True):
    # Only direct string children
    for s in tag.strings:
        text = str(s).strip()
        if not text:
            continue
        for kw in keywords:
            if re.search(r'\b' + re.escape(kw) + r'\b', text, re.IGNORECASE):
                results.append((kw, tag.name, tag.get('class'), text[:80]))
                break

print(f"Total crypto text matches in index.html: {len(results)}")
for r in results[:25]:
    print(r)
