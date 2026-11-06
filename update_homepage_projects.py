"""
Updates index.html to transform the Case Studies slider into the Projects slider
showcasing all 15 client platforms with 16:9 widescreen imagery and subpage links,
and updates the hidden CMS list.
"""
import re
from projects_data import PROJECTS_LIST

def build_slider_items():
    slides = []
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

        slide = f'''<div class="caselist-slider-item w-slide"><div class="articles-collection w-dyn-list"><div class="w-dyn-items" role="list"><div class="w-dyn-item" role="listitem"><div class="vid_slide-wrapper"><a class="link-block article-slide w-inline-block" href="/projects/{slug}.html"><div class="case-item-head"><div class="case-itempartner-logo"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/66f4342dde3e7c3beaed31fe_ico-indicator%20(1).svg"/></div><div class="case-item-category">{category}</div></div><div class="case-item-image-wrapper"><div class="case-item-thmb slider-case-image"><img alt="{title}" class="slide-image-elem" loading="lazy" src="{thumbnail}"/><div class="arrow-el-wrap"><div class="arrow-el arrow-el-bottom-right"></div><div class="arrow-el arrow-el-top-right"></div><div class="arrow-el arrow-el-bottom-left"></div><div class="arrow-el arrow-el-top-left"></div></div></div></div><div class="vid_slide-desc caseslider-desc"><h3 class="sub-heading-02 twolines-ellipsis">{title}</h3></div><div class="case-item-footer"><div><div class="caseitem-footer-text">{m1_val}</div><div class="caseitem-footer-subtext">{m1_lbl}</div></div><div><div class="caseitem-footer-text">{m2_val}</div><div class="caseitem-footer-subtext">{m2_lbl}</div></div><div><div class="caseitem-footer-text">{m3_val}</div><div class="caseitem-footer-subtext">{m3_lbl}</div></div></div></a></div></div></div></div></div>'''
        slides.append(slide)

    # Add a final empty slide for the "Explore more" box append script
    slides.append('<div class="caselist-slider-item w-slide"></div>')
    return ''.join(slides)

def build_cms_list_items():
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

        item = f'''<div class="w-dyn-item" role="listitem"><div class="vid_slide-wrapper"><a class="link-block article-slide w-inline-block" href="/projects/{slug}.html"><div class="case-item-head"><div class="case-itempartner-logo"><img alt="" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/66f4342dde3e7c3beaed31fe_ico-indicator%20(1).svg"/></div><div class="case-item-category">{category}</div></div><div class="case-item-image-wrapper"><div class="case-item-thmb slider-case-image"><img alt="{title}" class="slide-image-elem" loading="lazy" src="{thumbnail}"/><div class="arrow-el-wrap"><div class="arrow-el arrow-el-bottom-right"></div><div class="arrow-el arrow-el-top-right"></div><div class="arrow-el arrow-el-bottom-left"></div><div class="arrow-el arrow-el-top-left"></div></div></div></div><div class="vid_slide-desc caseslider-desc"><h3 class="sub-heading-02 twolines-ellipsis">{title}</h3></div><div class="case-item-footer"><div><div class="caseitem-footer-text">{m1_val}</div><div class="caseitem-footer-subtext">{m1_lbl}</div></div><div><div class="caseitem-footer-text">{m2_val}</div><div class="caseitem-footer-subtext">{m2_lbl}</div></div><div><div class="caseitem-footer-text">{m3_val}</div><div class="caseitem-footer-subtext">{m3_lbl}</div></div></div></a></div></div>'''
        items.append(item)
    return ''.join(items)

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update tab label: Case Studies -> Projects
    content = content.replace(
        '<div anim-trigger-text="" class="text-block-140">Case Studies</div>',
        '<div anim-trigger-text="" class="text-block-140">Projects</div>'
    )
    content = content.replace(
        '<div class="text-block-140" anim-trigger-text="">Case Studies</div>',
        '<div class="text-block-140" anim-trigger-text="">Projects</div>'
    )

    # 2. Update heading if needed
    content = content.replace(
        '<h2 anim-trigger="" class="section-title">\n<span anim-trigger-text="">Explore our</span>\n</h2>',
        '<h2 anim-trigger="" class="section-title">\n<span anim-trigger-text="">Explore our Projects</span>\n</h2>'
    )

    # 3. Update top button link to projects.html
    content = re.sub(
        r'<a class="link-more link-more--sm w-inline-block" href="[^"]*case-studies[^"]*"[^>]*>.*?</a>',
        '<a class="link-more link-more--sm w-inline-block" href="projects.html" rel="noopener noreferrer" scramble-link=""><div class="text-block-194" scramble-text="">ALL PROJECTS (15)</div><div class="learn-more-icon-border"><img alt="" class="link-more-icon link-more-icon--sm no-marg" height="38" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/6437b8bc549a694211710a04_arrow-right-color.svg" width="38"/></div></a>',
        content,
        flags=re.DOTALL
    )

    # 4. Replace mask slider content
    new_mask_content = build_slider_items()
    pattern = r'<div class="mask-5 w-slider-mask">.*?</div>\s*<div class="custom-slider-arrow custom-slider-arrow--prev'
    replacement = f'<div class="mask-5 w-slider-mask">{new_mask_content}</div><div class="custom-slider-arrow custom-slider-arrow--prev'
    
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)
        print("Replaced slider mask content successfully!")

    # 5. Update bottom learn more box
    content = re.sub(
        r'<a class="learn-more-box w-inline-block" href="[^"]*case-studies[^"]*" id="learn-more-case">.*?</a>',
        '<a class="learn-more-box w-inline-block" href="projects.html" id="learn-more-case"><div class="learn-more-box-frame"><div class="arrow-el-wrap"><div class="arrow-el arrow-el-bottom-right"></div><div class="arrow-el arrow-el-top-right"></div><div class="arrow-el arrow-el-bottom-left"></div><div class="arrow-el arrow-el-top-left"></div></div><div class="learn-more-box-inner"><div class="learn-more-box-top"><img alt="" class="learn-more-box-top-icon" height="5" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/65d7024239f549e9be5ab902_ico-indicator-down.svg" width="6"/><div>Read more</div></div><img alt="" class="learn-more-box-arrow" height="96" loading="lazy" src="https://cdn.prod.website-files.com/64354b8ce4872ad8cd1c7b04/6437b8bc549a694211710a04_arrow-right-color.svg" width="96"/><div class="learn-more-box-bottom">Explore all 15 Client Projects &amp; Platforms</div></div></div></a>',
        content,
        flags=re.DOTALL
    )

    # 6. Replace hidden CMS list items
    new_cms_items = build_cms_list_items()
    cms_pattern = r'<div class="w-dyn-items" fs-cmsslider-element="list-42" role="list">.*?</div>'
    cms_replacement = f'<div class="w-dyn-items" fs-cmsslider-element="list-42" role="list">{new_cms_items}</div>'
    if re.search(cms_pattern, content, flags=re.DOTALL):
        content = re.sub(cms_pattern, cms_replacement, content, count=1, flags=re.DOTALL)
        print("Replaced hidden CMS list successfully!")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html updated successfully with Projects slider and CMS list!")

if __name__ == '__main__':
    update_index()
