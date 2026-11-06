import os
from bs4 import BeautifulSoup

def analyze_all():
    files = sorted([f for f in os.listdir('.') if f.endswith('.html') and not f.endswith('.bak')])
    print(f"Total HTML files: {len(files)}")
    for f in files:
        with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
            html = fp.read()
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string.strip() if soup.title and soup.title.string else 'No Title'
        h1 = soup.find('h1')
        h1_txt = h1.get_text(strip=True)[:50] if h1 else 'No H1'
        
        # Check main stylesheet
        styles = [link.get('href') for link in soup.find_all('link', rel='stylesheet')]
        has_webflow_css = any('chain-gpt' in (s or '') or 'webflow' in (s or '') for s in styles)
        has_next_css = any('_next' in (s or '') for s in styles)
        
        # Check main content div
        main_div = soup.find('main') or soup.find(class_='page-wrapper') or soup.find(class_='main-wrapper') or soup.find(id='__next')
        
        print(f"{f:32} | Title: {title[:30]:30} | H1: {h1_txt:30} | CSS: WF={has_webflow_css}/Next={has_next_css} | Main: {main_div.name if main_div else 'None'} ({main_div.get('class') if main_div and main_div.get('class') else ''})")

if __name__ == '__main__':
    analyze_all()
