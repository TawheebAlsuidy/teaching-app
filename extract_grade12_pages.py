#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
High-Speed Page Extraction & Optimization Script for Grade 12 Physics & Biology
Renders PDF pages directly into high-fidelity web-optimized images (Full & Opt).
"""
import os
import sys
import shutil
import subprocess
import time
from PIL import Image

BASE_DIR = "/media/tawheeb/New Volume2/ذاكر/teaching-app"

BOOKS = [
    {
        "id": "physics",
        "name": "الفيزياء - الصف الثالث الثانوي",
        "pdf": f"{BASE_DIR}/المنهج/ثالث ثانوي/كتاب-فيزياء-ثالث-ثانوي-اليمن.pdf",
        "start_pdf_page": 6,
        "end_pdf_page": 219,
        "book_offset": 0, # Page 6 in PDF corresponds to book TOC page 6
        "out_dirs": [
            f"{BASE_DIR}/assets/curriculum/grade12/physics/pages",
            f"{BASE_DIR}/thaker-android-src/assets/curriculum/grade12/physics/pages",
            f"{BASE_DIR}/thaker-android-src/assets/assets/curriculum/grade12/physics/pages"
        ]
    },
    {
        "id": "biology",
        "name": "الأحياء - الصف الثالث الثانوي",
        "pdf": f"{BASE_DIR}/المنهج/ثالث ثانوي/الأحياء-للصف-الثالث-الثانوي.pdf",
        "start_pdf_page": 4,
        "end_pdf_page": 221,
        "book_offset": 0,
        "out_dirs": [
            f"{BASE_DIR}/assets/curriculum/grade12/biology/pages",
            f"{BASE_DIR}/thaker-android-src/assets/curriculum/grade12/biology/pages",
            f"{BASE_DIR}/thaker-android-src/assets/assets/curriculum/grade12/biology/pages"
        ]
    }
]

def render_book(b):
    print(f"\n=======================================================")
    print(f"[*] Rendering: {b['name']} ({b['id']})")
    print(f"[*] Pages: PDF {b['start_pdf_page']} -> {b['end_pdf_page']}")
    print(f"=======================================================")
    
    primary_dir = b["out_dirs"][0]
    os.makedirs(primary_dir, exist_ok=True)
    temp_dir = f"/tmp/render_{b['id']}"
    os.makedirs(temp_dir, exist_ok=True)

    t0 = time.time()
    
    # 1. Render Full High-Resolution (135 DPI, quality=80)
    print(" -> Rendering Full Pages via pdftoppm (135 DPI)...")
    subprocess.run([
        "pdftoppm", "-jpeg", "-jpegopt", "quality=80",
        "-r", "135",
        "-f", str(b["start_pdf_page"]),
        "-l", str(b["end_pdf_page"]),
        b["pdf"],
        f"{temp_dir}/p"
    ], check=True)

    # Move and generate _opt.jpg
    rendered_files = sorted(os.listdir(temp_dir))
    print(f" -> Generated {len(rendered_files)} raw pages. Optimizing and structuring...")
    
    for f in rendered_files:
        if not f.endswith(".jpg"):
            continue
        # Format from pdftoppm is like p-006.jpg or p-06.jpg
        num_str = f.replace("p-", "").replace(".jpg", "")
        pdf_page_num = int(num_str)
        target_name_full = f"page_{pdf_page_num:03d}.jpg"
        target_name_opt = f"page_{pdf_page_num:03d}_opt.jpg"

        src_path = os.path.join(temp_dir, f)
        dest_full = os.path.join(primary_dir, target_name_full)
        dest_opt = os.path.join(primary_dir, target_name_opt)

        shutil.copy2(src_path, dest_full)

        # Create optimized version (half size, quality 75)
        with Image.open(src_path) as img:
            w, h = img.size
            opt_img = img.resize((w // 2, h // 2), Image.Resampling.LANCZOS)
            opt_img.save(dest_opt, "JPEG", quality=75, optimize=True)

    # Mirror to android asset directories
    print(f" -> Mirroring pages to Android asset directories...")
    for mirror_dir in b["out_dirs"][1:]:
        os.makedirs(mirror_dir, exist_ok=True)
        for fname in os.listdir(primary_dir):
            shutil.copy2(os.path.join(primary_dir, fname), os.path.join(mirror_dir, fname))

    # Cleanup temp
    shutil.rmtree(temp_dir, ignore_errors=True)
    t1 = time.time()
    print(f"[*] Completed {b['name']} in {t1 - t0:.2f} seconds!")

def main():
    start_total = time.time()
    for b in BOOKS:
        render_book(b)
    print(f"\n[✓] ALL PAGES EXTRACTED AND OPTIMIZED IN {time.time() - start_total:.2f}s TOTAL!")

if __name__ == "__main__":
    main()
