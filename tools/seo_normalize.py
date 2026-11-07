"""Normalise SEO / social-share tags across every public page.

- Canonical URLs never point at another domain (template pages pointed at coingpt.tech).
- Every page gets a full Open Graph + Twitter card set with an absolute image URL.
- Leftover template pages (CoinGPT crypto tools and legal copy) are noindex,follow
  until they're rewritten for Vector Studioz, and are excluded from the sitemap.
- The template's Google Tag Manager container (GTM-K43K2ZQ), Gleam airdrop
  widget and Cookie3 analytics (all ChainGPT accounts) are removed so visitor
  data isn't sent to a third party.
- Writes sitemap.xml and robots.txt.

The homepage head is maintained by hand in index.html; this script only strips
the GTM container there.

Run from the repo root:  python tools/seo_normalize.py
"""
import html
import os
import re
from datetime import date

SITE = 'https://vectorstudioz.uk'
DEFAULT_IMAGE = f'{SITE}/images/og-vector-studioz-hero.jpg'
SKIP_PREFIXES = ('test_', 'navbar_', 'template_')

# Template leftovers: CoinGPT product pages.
NOINDEX = {
    'ai-crypto-alerts.html', 'ai-web3-news.html', 'crypto-compliance-assistant.html',
    'eligibility-policy.html', 'verify.html', 'web3-ai-grant.html',
}

SITEMAP = [  # (path, changefreq, priority)
    ('', 'weekly', '1.0'),
    ('web-design.html', 'monthly', '0.9'),
    ('web-development.html', 'monthly', '0.9'),
    ('webgl-3d.html', 'monthly', '0.9'),
    ('mobile-development.html', 'monthly', '0.9'),
    ('software-engineering.html', 'monthly', '0.9'),
    ('ai-automation.html', 'monthly', '0.9'),
    ('projects.html', 'weekly', '0.8'),
    ('about.html', 'monthly', '0.7'),
    ('contact-us.html', 'yearly', '0.7'),
    ('careers.html', 'monthly', '0.5'),
    ('privacy-policy.html', 'yearly', '0.3'),
    ('tos.html', 'yearly', '0.3'),
    ('cookies.html', 'yearly', '0.3'),
]

GTM_SCRIPT = re.compile(
    r"(<!-- Google Tag Manager -->\s*)?<script>\(function\(w,d,s,l,i\)[\s\S]*?GTM-K43K2ZQ'\);</script>(\s*<!-- End Google Tag Manager -->)?\n?")
GTM_NOSCRIPT = re.compile(
    r"(<!-- Google Tag Manager \(noscript\) -->\s*)?<noscript><iframe[^>]*GTM-K43K2ZQ[^>]*>\s*</iframe></noscript>(\s*<!-- End Google Tag Manager \(noscript\) -->)?\n?")
# ChainGPT's Gleam airdrop widget and Cookie3 analytics account, left over from the template.
GLEAM = re.compile(r"<script type=\"text/javascript\">\(function\(d, t\)\{\s*if\(window\.location\.hash!='#Airdrop'[\s\S]*?widget\.gleamjs\.io[\s\S]*?</script>\n?")
COOKIE3 = re.compile(r"<script>\s*var cookie3Options[\s\S]*?cookie3\.analytics\.min\.js[\s\S]*?</script>\n?")
SOCIAL_META = re.compile(r'<meta\b[^>]*\b(?:property|name)="(?:og|twitter):[^"]*"[^>]*/?>\n?')
ROBOTS_META = re.compile(r'<meta\b[^>]*\bname="robots"[^>]*/?>\n?')
CANONICAL = re.compile(r'<link\b[^>]*\brel="canonical"[^>]*/?>')


def attr(tag, name):
    m = re.search(rf'\b{name}="([^"]*)"', tag)
    return m.group(1) if m else None


def strip_gtm(s):
    s = GTM_SCRIPT.sub('', s)
    s = GLEAM.sub('', s)
    s = COOKIE3.sub('', s)
    return GTM_NOSCRIPT.sub('', s)


def page_url(rel):
    return f'{SITE}/{rel.replace(os.sep, "/")}'


def normalise(rel):
    s = open(rel, encoding='utf-8').read()
    s = strip_gtm(s)
    if rel == 'index.html':
        return s

    title = re.search(r'<title>([^<]*)</title>', s).group(1).strip()
    desc_tag = re.search(r'<meta\b[^>]*\bname="description"[^>]*>', s)
    desc = attr(desc_tag.group(0), 'content') if desc_tag else ''

    # Project pages keep their own case-study screenshot, made absolute.
    image = DEFAULT_IMAGE
    if rel.startswith('projects' + os.sep):
        old = next((attr(t, 'content') for t in SOCIAL_META.findall(s) if 'og:image"' in t), None)
        if old and not old.startswith('http'):
            image = SITE + '/' + os.path.normpath(os.path.join('projects', old)).replace(os.sep, '/')

    canon_m = CANONICAL.search(s)
    canon = attr(canon_m.group(0), 'href') if canon_m else None
    if not canon or not canon.startswith(SITE):
        canon = page_url(rel)

    s = SOCIAL_META.sub('', s)
    s = ROBOTS_META.sub('', s)
    s = re.sub(CANONICAL.pattern + r'\n?', '', s, count=1) if canon_m else s
    # Removed tags can leave blank lines behind; drop them so reruns are stable.
    s = re.sub(r'(<title>[^<]*</title>)\n(?:[ \t]*\n)+', r'\1\n', s, count=1)

    robots = 'noindex, follow' if rel in NOINDEX else \
        'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1'
    alt = html.escape(html.unescape(title), quote=True)
    block = '\n'.join([
        f'<link rel="canonical" href="{canon}"/>',
        f'<meta name="robots" content="{robots}"/>',
        '<meta property="og:type" content="website"/>',
        '<meta property="og:site_name" content="Vector Studioz"/>',
        '<meta property="og:locale" content="en_GB"/>',
        f'<meta property="og:url" content="{canon}"/>',
        f'<meta property="og:title" content="{title}"/>',
        f'<meta property="og:description" content="{desc}"/>',
        f'<meta property="og:image" content="{image}"/>',
        *([f'<meta property="og:image:width" content="1200"/>',
           f'<meta property="og:image:height" content="630"/>'] if image == DEFAULT_IMAGE else []),
        f'<meta property="og:image:alt" content="{alt}"/>',
        '<meta name="twitter:card" content="summary_large_image"/>',
        f'<meta name="twitter:title" content="{title}"/>',
        f'<meta name="twitter:description" content="{desc}"/>',
        f'<meta name="twitter:image" content="{image}"/>',
    ]) + '\n'

    # Insert right after the <title> so crawlers see it early.
    s = re.sub(r'(<title>[^<]*</title>\n?)', lambda m: m.group(1) + ('' if m.group(1).endswith('\n') else '\n') + block, s, count=1)
    return s


def main():
    pages = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith(SKIP_PREFIXES)]
    pages += [os.path.join('projects', f) for f in os.listdir('projects') if f.endswith('.html')]
    for rel in sorted(pages):
        new = normalise(rel)
        if new != open(rel, encoding='utf-8').read():
            open(rel, 'w', encoding='utf-8', newline='').write(new)
            print('updated', rel)

    today = date.today().isoformat()
    projects = sorted(f for f in os.listdir('projects') if f.endswith('.html'))
    entries = SITEMAP + [(f'projects/{p}', 'monthly', '0.6') for p in projects]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, freq, prio in entries:
        xml += ['  <url>', f'    <loc>{SITE}/{path}</loc>', f'    <lastmod>{today}</lastmod>',
                f'    <changefreq>{freq}</changefreq>', f'    <priority>{prio}</priority>', '  </url>']
    xml.append('</urlset>')
    open('sitemap.xml', 'w', encoding='utf-8', newline='\n').write('\n'.join(xml) + '\n')

    open('robots.txt', 'w', encoding='utf-8', newline='\n').write(
        'User-agent: *\n'
        'Allow: /\n'
        'Disallow: /backup_pages/\n'
        'Disallow: /scratch/\n'
        'Disallow: /tools/\n'
        'Disallow: /test_index.html\n'
        'Disallow: /navbar_current.html\n'
        'Disallow: /template_header.html\n'
        'Disallow: /template_footer.html\n'
        '\n'
        f'Sitemap: {SITE}/sitemap.xml\n')
    print(f'sitemap.xml: {len(entries)} URLs; robots.txt written')


if __name__ == '__main__':
    main()
