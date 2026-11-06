import re

def update_title_meta(filename, title, desc):
    with open(filename, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', c, flags=re.DOTALL)
    c = re.sub(r'<meta content=".*?" name="description"/>', f'<meta content="{desc}" name="description"/>', c)
    c = re.sub(r'<meta content=".*?" property="og:title"/>', f'<meta content="{title}" property="og:title"/>', c)
    c = re.sub(r'<meta content=".*?" property="og:description"/>', f'<meta content="{desc}" property="og:description"/>', c)
    c = re.sub(r'<meta content=".*?" name="twitter:title"/>', f'<meta content="{title}" name="twitter:title"/>', c)
    c = re.sub(r'<meta content=".*?" name="twitter:description"/>', f'<meta content="{desc}" name="twitter:description"/>', c)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Updated {filename}")

update_title_meta('case-studies.html', 'Client Case Studies & Digital Showcase — Vector Studioz', 'Explore award-winning digital experiences, web apps, and AI software engineered by Vector Studioz.')
update_title_meta('blog.html', 'Insights, Tech Perspectives & Design Articles — Vector Studioz', 'Articles, architectural breakdowns, and design perspectives from the engineering vanguard at Vector Studioz.')
update_title_meta('videos.html', 'Agency Insights & Digital Product Walkthroughs — Vector Studioz', 'Watch product breakdowns, UI/UX design case studies, and engineering deep dives from Vector Studioz.')
