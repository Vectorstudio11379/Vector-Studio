"""
Creates beautiful, high-res 16:9 (1920x1080) showcase thumbnails for the newly added projects:
- mesuullogic.jpg
- expressteck.jpg
- lake-greenfield.jpg
- mirola-cleaning.jpg
- mirola-nigeria.jpg
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUTPUT_DIR = os.path.join('images', 'case-studies')
os.makedirs(OUTPUT_DIR, exist_ok=True)

THUMBNAILS = [
    {
        'filename': 'mesuullogic.jpg',
        'title': 'MESSULOGIC',
        'subtitle': 'Enterprise EdTech & Learning Management Platform',
        'domain': 'mesuullogic.com',
        'accent': (255, 115, 0), # Brand orange
        'gradient_start': (12, 10, 18),
        'gradient_end': (28, 16, 8),
        'tag': 'EDTECH & LMS PLATFORM'
    },
    {
        'filename': 'expressteck.jpg',
        'title': 'EXPRESSTECK',
        'subtitle': 'Innovation & Digital Training Academy',
        'domain': 'expressteck.tech',
        'accent': (0, 229, 255), # Neon cyan
        'gradient_start': (8, 14, 24),
        'gradient_end': (14, 28, 48),
        'tag': 'REACT 18 & DIGITAL ACADEMY'
    },
    {
        'filename': 'lake-greenfield.jpg',
        'title': 'LAKE GREENFIELD',
        'subtitle': 'Luxury Boutique Hospitality & Direct Reservation Engine',
        'domain': 'lakegreenfieldhotel.com',
        'accent': (212, 175, 55), # Gold
        'gradient_start': (10, 16, 14),
        'gradient_end': (24, 22, 12),
        'tag': 'LUXURY HOSPITALITY & BOOKING'
    },
    {
        'filename': 'mirola-cleaning.jpg',
        'title': 'MIROLA CLEANING',
        'subtitle': 'Commercial Janitorial & Facility Sanitization Portal',
        'domain': 'mirolacleaningservices.com',
        'accent': (220, 38, 38), # Red
        'gradient_start': (18, 10, 12),
        'gradient_end': (34, 12, 16),
        'tag': 'COMMERCIAL FACILITY MANAGEMENT'
    },
    {
        'filename': 'mirola-nigeria.jpg',
        'title': 'MIROLA NIGERIA',
        'subtitle': 'Digital & Remote Work Skills Development Academy',
        'domain': 'mirolanigeria.com',
        'accent': (16, 185, 129), # Emerald green
        'gradient_start': (8, 18, 14),
        'gradient_end': (12, 32, 22),
        'tag': 'REMOTE SKILLS & WORKFORCE HUB'
    }
]

W, H = 1920, 1080

def generate():
    for item in THUMBNAILS:
        img = Image.new('RGB', (W, H))
        draw = ImageDraw.Draw(img)

        # Smooth vertical gradient
        r1, g1, b1 = item['gradient_start']
        r2, g2, b2 = item['gradient_end']
        for y in range(H):
            ratio = y / H
            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)
            b = int(b1 + (b2 - b1) * ratio)
            draw.line([(0, y), (W, y)], fill=(r, g, b))

        # Ambient Glow Circle in Center-Top
        ar, ag, ab = item['accent']
        for radius in range(500, 50, -30):
            alpha = int(25 * (1 - (radius / 500)))
            glow_color = (
                min(255, int(r1 + (ar - r1) * (alpha / 100))),
                min(255, int(g1 + (ag - g1) * (alpha / 100))),
                min(255, int(b1 + (ab - b1) * (alpha / 100)))
            )
            draw.ellipse([W//2 - radius, 250 - radius, W//2 + radius, 250 + radius], outline=glow_color, width=15)

        # Subtle geometric grid pattern
        for x in range(0, W, 80):
            draw.line([(x, 0), (x, H)], fill=(255, 255, 255, 8), width=1)
        for y in range(0, H, 80):
            draw.line([(0, y), (W, y)], fill=(255, 255, 255, 8), width=1)

        # Modern card frame
        margin = 60
        draw.rounded_rectangle(
            [(margin, margin), (W - margin, H - margin)],
            radius=24,
            outline=(ar, ag, ab),
            width=2
        )

        # Inner decorative corner brackets
        bracket_len = 50
        # Top Left
        draw.line([(margin + 15, margin + 15), (margin + 15 + bracket_len, margin + 15)], fill=(ar, ag, ab), width=3)
        draw.line([(margin + 15, margin + 15), (margin + 15, margin + 15 + bracket_len)], fill=(ar, ag, ab), width=3)
        # Top Right
        draw.line([(W - margin - 15 - bracket_len, margin + 15), (W - margin - 15, margin + 15)], fill=(ar, ag, ab), width=3)
        draw.line([(W - margin - 15, margin + 15), (W - margin - 15, margin + 15 + bracket_len)], fill=(ar, ag, ab), width=3)
        # Bottom Left
        draw.line([(margin + 15, H - margin - 15), (margin + 15 + bracket_len, H - margin - 15)], fill=(ar, ag, ab), width=3)
        draw.line([(margin + 15, H - margin - 15 - bracket_len), (margin + 15, H - margin - 15)], fill=(ar, ag, ab), width=3)
        # Bottom Right
        draw.line([(W - margin - 15 - bracket_len, H - margin - 15), (W - margin - 15, H - margin - 15)], fill=(ar, ag, ab), width=3)
        draw.line([(W - margin - 15, H - margin - 15 - bracket_len), (W - margin - 15, H - margin - 15)], fill=(ar, ag, ab), width=3)

        # Category Pill
        pill_text = item['tag']
        pill_w, pill_h = len(pill_text) * 16, 48
        px, py = W//2 - pill_w//2, 280
        draw.rounded_rectangle([(px, py), (px + pill_w, py + pill_h)], radius=24, fill=(ar//4, ag//4, ab//4), outline=(ar, ag, ab), width=2)
        draw.text((W//2, py + 24), pill_text, fill=(240, 240, 245), anchor="mm")

        # Big Title
        draw.text((W//2, 460), item['title'], fill=(255, 255, 255), anchor="mm", font_size=96)
        
        # Subtitle
        draw.text((W//2, 570), item['subtitle'], fill=(180, 185, 200), anchor="mm", font_size=38)

        # Domain Badge
        draw.text((W//2, 690), f"https://{item['domain']}/", fill=(ar, ag, ab), anchor="mm", font_size=32)

        # Bottom Agency Signature
        draw.text((W//2, 950), "VECTOR STUDIOZ  |  CLIENT PRODUCTION SHOWCASE", fill=(120, 125, 140), anchor="mm", font_size=24)

        target_path = os.path.join(OUTPUT_DIR, item['filename'])
        img.save(target_path, 'JPEG', quality=95)
        print(f"Generated {target_path} (1920x1080 16:9)")

if __name__ == '__main__':
    generate()
