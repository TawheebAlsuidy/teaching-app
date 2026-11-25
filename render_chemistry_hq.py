#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
High-Resolution Page Renderer for Grade 12 Chemistry
- Renders crisp 240 DPI full pages -> page_XXX.jpg (PDF 5..191 -> Book 3..189)
- Renders crisp 180 DPI optimized pages -> page_XXX_opt.jpg
- Mirrors to Android assets folders.
"""
import os
import shutil
import subprocess
import time

BASE_DIR = "/media/tawheeb/New Volume3/ذاكر/teaching-app"
PDF_PATH = f"{BASE_DIR}/المنهج/ثالث ثانوي/كتاب-الكيمياء-ثالث-ثانوي.pdf"
START_PDF = 5
END_PDF = 191

OUT_DIRS = [
    f"{BASE_DIR}/assets/curriculum/grade12/chemistry/pages",
    f"{BASE_DIR}/thaker-android-src/assets/curriculum/grade12/chemistry/pages",
    f"{BASE_DIR}/thaker-android-src/assets/assets/curriculum/grade12/chemistry/pages",
]

def render_pass(dpi, quality, tmp_dir):
    os.makedirs(tmp_dir, exist_ok=True)
    for start in range(START_PDF, END_PDF + 1, 50):
        end = min(END_PDF, start + 49)
        subprocess.run([
            "pdftoppm", "-jpeg", "-jpegopt", f"quality={quality}",
            "-r", str(dpi),
            "-f", str(start), "-l", str(end),
            PDF_PATH,
            f"{tmp_dir}/p"
        ], check=True)

def main():
    t0 = time.time()
    primary = OUT_DIRS[0]
    os.makedirs(primary, exist_ok=True)

    tmp_full = "/tmp/render_chem_240"
    tmp_opt = "/tmp/render_chem_180"
    shutil.rmtree(tmp_full, ignore_errors=True)
    shutil.rmtree(tmp_opt, ignore_errors=True)

    print("[*] Rendering 240 DPI Chemistry full pages (PDF 5..191)...")
    render_pass(240, 84, tmp_full)
    print("[*] Rendering 180 DPI Chemistry opt pages (PDF 5..191)...")
    render_pass(180, 82, tmp_opt)

    for fn in sorted(os.listdir(tmp_full)):
        if not fn.endswith(".jpg"): continue
        pnum = int(fn.replace("p-", "").replace(".jpg", ""))
        shutil.copy2(os.path.join(tmp_full, fn), os.path.join(primary, f"page_{pnum:03d}.jpg"))

    for fn in sorted(os.listdir(tmp_opt)):
        if not fn.endswith(".jpg"): continue
        pnum = int(fn.replace("p-", "").replace(".jpg", ""))
        shutil.copy2(os.path.join(tmp_opt, fn), os.path.join(primary, f"page_{pnum:03d}_opt.jpg"))

    print("[*] Mirroring high-res chemistry pages to Android asset dirs...")
    files = [f for f in os.listdir(primary) if f.endswith(".jpg")]
    for mdir in OUT_DIRS[1:]:
        os.makedirs(mdir, exist_ok=True)
        for fn in files:
            shutil.copy2(os.path.join(primary, fn), os.path.join(mdir, fn))

    shutil.rmtree(tmp_full, ignore_errors=True)
    shutil.rmtree(tmp_opt, ignore_errors=True)
    total_mb = sum(os.path.getsize(os.path.join(primary, fn)) for fn in files) / (1024 * 1024)
    print(f"[✓] Done! {len(files)} Chemistry images ({total_mb:.1f} MB) rendered & mirrored in {time.time()-t0:.1f}s.")

if __name__ == "__main__":
    main()
