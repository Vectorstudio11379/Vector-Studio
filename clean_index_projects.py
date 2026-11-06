"""
Cleans and replaces the hidden CMS list in index.html with the 15 updated projects.
"""
from projects_data import PROJECTS_LIST

def run():
    with open('index.html', 'r', encoding='utf-8') as f:
        c = f.read()

    # Build the 15 CMS items
    items = []
    for p in PROJECTS_LIST:
        slug = p['slug']
        title = p['title']
        category = p['category']
        thumbnail = p['thumbnail']
        metrics = p['metrics']

        m1_val = metrics[0]['value'] if len(metrics) > 0 else 'High Impact'
        m1_lbl = metrics[0]['label'] if len(metrics) > 0 else 'Performance'
        m2_val = metrics[1]['value'] if len(metrics) > 1 else 'Custom'
        m2_lbl = metrics[1]['label'] if len(metrics) > 1 else 'Architecture'
        m3_val = metrics[2]['value'] if len(metrics) > 2 else 'Fast'
        m3_lbl = metrics[2]['label'] if len(metrics) > 2 else 'Delivery'

        item = f'<div class="w-dyn-item" role="listitem"><div class="vid_slide-wrapper"><a class="link-block article-slide w-inline-block" href="/projects/{slug}.html"><div class="case-item-head"><div class="case-itempartner-logo"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/66f4342dde3e7c3beaed31fe_ico-indicator%20(1).svg"/></div><div class="case-item-category">{category}</div></div><div class="case-item-image-wrapper"><div class="case-item-thmb slider-case-image"><img alt="{title}" class="slide-image-elem" loading="lazy" src="{thumbnail}"/><div class="arrow-el-wrap"><div class="arrow-el arrow-el-bottom-right"></div><div class="arrow-el arrow-el-top-right"></div><div class="arrow-el arrow-el-bottom-left"></div><div class="arrow-el arrow-el-top-left"></div></div></div></div><div class="vid_slide-desc caseslider-desc"><h3 class="sub-heading-02 twolines-ellipsis">{title}</h3></div><div class="case-item-footer"><div><div class="caseitem-footer-text">{m1_val}</div><div class="caseitem-footer-subtext">{m1_lbl}</div></div><div><div class="caseitem-footer-text">{m2_val}</div><div class="caseitem-footer-subtext">{m2_lbl}</div></div><div><div class="caseitem-footer-text">{m3_val}</div><div class="caseitem-footer-subtext">{m3_lbl}</div></div></div></a></div></div>'
        items.append(item)

    cms_list_html = ''.join(items)

    start_token = '<div class="hidden w-dyn-list"><div class="w-dyn-items" fs-cmsslider-element="list-42" role="list">'
    end_token = '<div class="ecosystem-section"'

    s = c.find(start_token)
    e = c.find(end_token, s)

    if s != -1 and e != -1:
        # Before ecosystem section, there are closing divs for tabs-content, etc.
        # Find the last closing divs before ecosystem
        closing_divs = c[s:e]
        # In original structure: <div class="hidden w-dyn-list"><div class="w-dyn-items" ...>...</div></div></div></div></div>
        new_block = f'{start_token}{cms_list_html}</div></div></div></div></div>'
        c = c[:s] + new_block + c[e:]
        print(f"Successfully replaced CMS list from index {s} to {e}")
    else:
        print("Could not find start or end token:", s, e)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(c)

if __name__ == '__main__':
    run()
