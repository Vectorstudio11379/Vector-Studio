"""
capture_hero_thumbnails.py
Visits the 6 client website links, captures high-resolution screenshots of their hero sections,
and saves them as optimized 16:9 widescreen thumbnails in images/case-studies/
"""
import subprocess
import os
import time
from PIL import Image

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
DEST_DIR = os.path.abspath("images/case-studies")
os.makedirs(DEST_DIR, exist_ok=True)

SITES = [
    {
        "name": "mesuullogic",
        "url": "https://mesuullogic.com/",
        "filename": "mesuullogic.jpg",
        "wait_time": 6000
    },
    {
        "name": "expressteck",
        "url": "https://expressteck.tech/",
        "filename": "expressteck.jpg",
        "wait_time": 6000
    },
    {
        "name": "lake-greenfield",
        "url": "https://lakegreenfieldhotel.com/",
        "filename": "lake-greenfield.jpg",
        "wait_time": 7000
    },
    {
        "name": "iclvirtualservices",
        "url": "https://iclvirtualservices.com/",
        "filename": "operational-excellence.png",  # Also keep name for compatibility
        "alt_filename": "iclvirtualservices.jpg",
        "wait_time": 6000
    },
    {
        "name": "mirola-cleaning",
        "url": "https://mirolacleaningservices.com/",
        "filename": "mirola-cleaning.jpg",
        "wait_time": 6000
    },
    {
        "name": "mirola-nigeria",
        "url": "https://mirolanigeria.com/",
        "filename": "mirola-nigeria.jpg",
        "wait_time": 6000
    }
]

def capture_and_process():
    temp_dir = os.path.abspath("scratch/hero_temp")
    os.makedirs(temp_dir, exist_ok=True)

    for site in SITES:
        name = site["name"]
        url = site["url"]
        target_path = os.path.join(DEST_DIR, site["filename"])
        temp_shot = os.path.join(temp_dir, f"{name}_raw.png")

        print(f"\n[+] Visiting {url}...")
        cmd = [
            CHROME_PATH,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--hide-scrollbars",
            "--window-size=1600,900",
            f"--virtual-time-budget={site['wait_time']}",
            f"--screenshot={temp_shot}",
            url
        ]

        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=40)
            if os.path.exists(temp_shot) and os.path.getsize(temp_shot) > 1000:
                print(f"  Captured raw screenshot: {os.path.getsize(temp_shot)} bytes")

                # Crop/resize to exact 16:9 ratio (1920x1080)
                with Image.open(temp_shot) as img:
                    img_w, img_h = img.size
                    target_ratio = 16 / 9
                    current_ratio = img_w / img_h

                    if current_ratio > target_ratio:
                        # Too wide: crop width
                        new_w = int(img_h * target_ratio)
                        left = (img_w - new_w) // 2
                        img_cropped = img.crop((left, 0, left + new_w, img_h))
                    else:
                        # Too tall: crop from top (keep hero section)
                        new_h = int(img_w / target_ratio)
                        img_cropped = img.crop((0, 0, img_w, min(img_h, new_h)))

                    img_resized = img_cropped.resize((1920, 1080), Image.Resampling.LANCZOS)

                    # Save as target
                    if target_path.endswith('.jpg') or target_path.endswith('.jpeg'):
                        rgb_img = img_resized.convert('RGB')
                        rgb_img.save(target_path, 'JPEG', quality=92, optimize=True)
                    else:
                        img_resized.save(target_path, 'PNG', optimize=True)

                    if "alt_filename" in site:
                        alt_path = os.path.join(DEST_DIR, site["alt_filename"])
                        rgb_img = img_resized.convert('RGB')
                        rgb_img.save(alt_path, 'JPEG', quality=92, optimize=True)
                        print(f"  Saved alternate thumbnail: {alt_path}")

                print(f"  Successfully processed and saved to {target_path}!")
            else:
                print(f"  [!] Failed to capture {url}: exit {res.returncode}")
        except Exception as e:
            print(f"  [!] Error capturing {url}: {e}")

if __name__ == '__main__':
    capture_and_process()
