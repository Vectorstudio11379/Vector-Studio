import glob
from bs4 import BeautifulSoup

def update_header_cta():
    target_files = []
    
    # 1. Root HTML files (excluding index.html and templates)
    for f in sorted(glob.glob('*.html')):
        if f in ['index.html', 'test_index.html', 'template_footer.html', 'navbar_current.html']:
            continue
        target_files.append(f)
        
    # 2. Project subpages
    for f in sorted(glob.glob('projects/*.html')):
        target_files.append(f)

    print(f"Targeting {len(target_files)} HTML files for header CTA button update...")
    
    updated_count = 0
    for filepath in target_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        headers = soup.find_all(lambda tag: tag.name == 'header' or (tag.get('class') and ('vs-navbar' in tag.get('class') or 'navbar-4' in tag.get('class'))))
        
        modified = False
        for h in headers:
            # Find CTA buttons inside header
            cta_btns = h.find_all(class_='btn-primary')
            for btn in cta_btns:
                text_div = btn.find(class_='btn-primary-text')
                if text_div and 'Start a Project' in text_div.get_text():
                    text_div.string = 'SUBMIT PROJECT BRIEF ↓'
                    modified = True
                    
        # Also check mobile drawers that might be outside header tag
        drawers = soup.find_all(class_='vs-mobile-drawer')
        for d in drawers:
            cta_btns = d.find_all(class_='btn-primary')
            for btn in cta_btns:
                text_div = btn.find(class_='btn-primary-text')
                if text_div and 'Start a Project' in text_div.get_text():
                    text_div.string = 'SUBMIT PROJECT BRIEF ↓'
                    modified = True

        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            updated_count += 1
            print(f"  Updated: {filepath}")

    print(f"Successfully updated {updated_count} files!")

if __name__ == '__main__':
    update_header_cta()

