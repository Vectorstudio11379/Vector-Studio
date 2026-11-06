# Update template_header.html and template_footer.html with redesigned CoinGPT logo and .btn-primary CTA

LOGO_SVG = '''<svg width="34" height="34" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cgpt-grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00ffa3"/>
      <stop offset="50%" stop-color="#28efce"/>
      <stop offset="100%" stop-color="#6a59e5"/>
    </linearGradient>
    <linearGradient id="cgpt-grad2" x1="100%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#28efce"/>
      <stop offset="100%" stop-color="#00ffa3"/>
    </linearGradient>
    <filter id="cgpt-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>
  <!-- Outer Cyber Hexagon -->
  <polygon points="18,2 32,10 32,26 18,34 4,26 4,10" fill="#0b0c10" stroke="url(#cgpt-grad1)" stroke-width="1.8" filter="url(#cgpt-glow)"/>
  <!-- Inner Neural Core Geometry -->
  <polygon points="18,7 28,13 28,23 18,29 8,23 8,13" fill="rgba(0, 255, 163, 0.08)" stroke="url(#cgpt-grad2)" stroke-width="1.2"/>
  <!-- Central Quantum Node -->
  <circle cx="18" cy="18" r="3.2" fill="#00ffa3"/>
  <circle cx="18" cy="18" r="5" stroke="#28efce" stroke-width="0.8" stroke-dasharray="2 2"/>
  <!-- Connective Data Beams -->
  <line x1="18" y1="7" x2="18" y2="13" stroke="#00ffa3" stroke-width="1.2"/>
  <line x1="18" y1="23" x2="18" y2="29" stroke="#6a59e5" stroke-width="1.2"/>
  <line x1="8" y1="18" x2="13" y2="18" stroke="#28efce" stroke-width="1.2"/>
  <line x1="23" y1="18" x2="28" y2="18" stroke="#28efce" stroke-width="1.2"/>
</svg>'''

BRAND_HTML = f'''<a aria-label="CoinGPT Home" class="vs-brand" href="index.html">
<div class="vs-brand-logo" style="display:flex;align-items:center;justify-content:center;">
{LOGO_SVG}
</div>
<div class="vs-brand-text" style="font-family:'Inter',sans-serif;font-weight:800;font-size:21px;letter-spacing:-0.5px;color:#ffffff;display:flex;align-items:center;gap:2px;">CoinGPT<span style="color:#00ffa3;font-size:14px;font-weight:700;margin-left:2px;background:rgba(0,255,163,0.12);padding:2px 6px;border-radius:4px;border:1px solid rgba(0,255,163,0.3);letter-spacing:0.04em;">.tech</span></div>
</a>'''

BTN_PRIMARY_HTML = '''<a class="btn-primary ml-auto w-inline-block" href="pricing.html" scramble-link="" style="text-decoration:none;">
<div class="btn-primary-lines btn-primary-lines-1">
<div class="btn-primary-lines btn-primary-lines-2">
<div class="btn-primary-text" scramble-text="">Launch App</div>
</div>
</div>
</a>'''

MOBILE_BTN_HTML = '''<div class="vs-mobile-actions" style="margin-top:20px;padding:0 10px;">
<a class="btn-primary w-inline-block" href="pricing.html" scramble-link="" style="width:100%;text-align:center;display:flex;justify-content:center;text-decoration:none;">
<div class="btn-primary-lines btn-primary-lines-1" style="width:100%;">
<div class="btn-primary-lines btn-primary-lines-2" style="width:100%;">
<div class="btn-primary-text" scramble-text="">Launch App</div>
</div>
</div>
</a>
</div>'''

from bs4 import BeautifulSoup
import re

# 1. Update template_header.html
with open('template_header.html', 'r', encoding='utf-8') as f:
    h_soup = BeautifulSoup(f.read(), 'html.parser')

# Replace brand
old_brand = h_soup.find(class_='vs-brand')
if old_brand:
    old_brand.replace_with(BeautifulSoup(BRAND_HTML, 'html.parser'))

# Replace CTA button
cta_area = h_soup.find(class_='vs-nav-actions')
if cta_area:
    old_btn = cta_area.find('a')
    if old_btn:
        old_btn.replace_with(BeautifulSoup(BTN_PRIMARY_HTML, 'html.parser'))

# Replace mobile CTA button
old_mobile_act = h_soup.find(class_='vs-mobile-actions')
if old_mobile_act:
    old_mobile_act.replace_with(BeautifulSoup(MOBILE_BTN_HTML, 'html.parser'))

with open('template_header.html', 'w', encoding='utf-8') as f:
    f.write(str(h_soup))
print("Updated template_header.html")

# 2. Update template_footer.html
with open('template_footer.html', 'r', encoding='utf-8') as f:
    f_content = f.read()

f_soup = BeautifulSoup(f_content, 'html.parser')

# Replace footer brand
f_brand = f_soup.find('a', href='index.html')
if f_brand:
    f_brand_html = f'''<a href="index.html" style="display:inline-flex;align-items:center;gap:12px;text-decoration:none;margin-bottom:16px;">
{LOGO_SVG}
<span style="font-size:20px;font-weight:800;letter-spacing:-0.5px;color:#ffffff;font-family:'Inter',sans-serif;">CoinGPT<span style="color:#00ffa3;font-size:13px;font-weight:700;margin-left:4px;background:rgba(0,255,163,0.15);padding:2px 6px;border-radius:4px;border:1px solid rgba(0,255,163,0.3);">.tech</span></span>
</a>'''
    f_brand.replace_with(BeautifulSoup(f_brand_html, 'html.parser'))

# Replace description
p_tag = f_soup.find('p')
if p_tag:
    p_tag.string = "Leading AI infrastructure and Web3 intelligence ecosystem powering decentralized autonomous agents, smart contract tooling, and real-time algorithmic market intelligence."

# Replace copyright
f_str = str(f_soup)
f_str = f_str.replace("Vector Studioz", "CoinGPT").replace("VectorStudioz", "CoinGPT")

with open('template_footer.html', 'w', encoding='utf-8') as f:
    f.write(f_str)
print("Updated template_footer.html")

# 3. Add btn-primary fallback rules to vector-nav.css
with open('vector-nav.css', 'r', encoding='utf-8') as f:
    css = f.read()

BTN_CSS = """
/* Webflow .btn-primary default styling support */
.btn-primary {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 10px 24px;
  background-color: transparent;
  color: #efefe5 !important;
  font-family: 'Roboto Mono', monospace;
  font-size: 13px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  text-decoration: none !important;
  cursor: pointer;
  overflow: visible;
  transition: all 0.25s ease;
}
.btn-primary:before,
.btn-primary:after {
  position: absolute;
  width: 10px;
  height: 1px;
  content: "";
}
.btn-primary:before {
  top: 0;
  left: -3px;
  transform: rotate(-45deg);
  transform-origin: top right;
  background: linear-gradient(to right, #fb6e53 0%, #fb7454 100%);
}
.btn-primary:after {
  bottom: 0;
  right: -3px;
  transform: rotate(-45deg);
  transform-origin: bottom left;
  background: linear-gradient(to right, #74e79a 0%, #74e79a 100%);
}
.btn-primary-lines-1:before,
.btn-primary-lines-1:after {
  position: absolute;
  width: calc(100% - 8px);
  height: 1px;
  content: "";
}
.btn-primary-lines-1:before {
  top: 0;
  left: 7px;
  background: linear-gradient(to right, #fb7454 0%, #bcda68 100%);
}
.btn-primary-lines-1:after {
  bottom: 0;
  right: 7px;
  background: linear-gradient(to right, #6072e2 0%, #74e79a 100%);
}
.btn-primary-lines-2:before,
.btn-primary-lines-2:after {
  position: absolute;
  width: 1px;
  content: "";
}
.btn-primary-lines-2:before {
  bottom: 0;
  left: 0;
  height: 56%;
  background: linear-gradient(to bottom, #6e52e5 0%, #6072e2 100%);
}
.btn-primary-lines-2:after {
  top: 0;
  right: 0;
  height: calc(100% - 7px);
  background: linear-gradient(to bottom, #bcda68 0%, #74e79a 100%);
}
.btn-primary-text {
  position: relative;
  display: inline-flex;
  align-items: center;
  padding-left: 1.25rem;
}
.btn-primary-text:before,
.btn-primary-text:after {
  position: absolute;
  top: 0;
  bottom: 0;
  margin: auto 0;
  width: 0.25rem;
  height: 0.25rem;
  background-color: #efefe5;
  border-radius: 50%;
  content: "";
}
.btn-primary-text:before { left: 0; }
.btn-primary-text:after { left: 0.4375rem; }

.btn-primary:hover {
  background: rgba(0, 255, 163, 0.08);
  box-shadow: 0 0 20px rgba(0, 255, 163, 0.25);
}
"""

if '.btn-primary-lines-1:before' not in css:
    with open('vector-nav.css', 'a', encoding='utf-8') as f:
        f.write(BTN_CSS)
    print("Added .btn-primary CSS to vector-nav.css")
