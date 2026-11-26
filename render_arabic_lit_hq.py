#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""High-resolution page renderer for Grade 12 Arabic literature.

Source: الأدب والنصوص والنقد للصف الثالث الثانوي (218 PDF pages).

Page mapping: book_page = pdf_page - 1.
Reader pages: PDF 7..218 -> printed 6..217.
"""
import os
import re
import shutil
import subprocess
import time

BASE_DIR = "/media/tawheeb/New Volume3/ذاكر/teaching-app"
SOURCE_PDF = f"{BASE_DIR}/المنهج/ثالث ثانوي/الأدب-والنصوص-والنقد-للصف-الثالث-الثانوي.pdf"
OUT_DIR = f"{BASE_DIR}/assets/curriculum/grade12/arabic_lit/pages"

ANDROID_MIRRORS = [
    f"{BASE_DIR}/thaker-android-src/assets/curriculum/grade12/arabic_lit",
    f"{BASE_DIR}/thaker-android-src/assets/assets/curriculum/grade12/arabic_lit",
]


def render_pass(start, end, dpi, quality, tmp_dir):
    os.makedirs(tmp_dir, exist_ok=True)
    for batch_start in range(start, end + 1, 50):
        batch_end = min(end, batch_start + 49)
        subprocess.run([
            "pdftoppm", "-jpeg", "-jpegopt", f"quality={quality}",
            "-r", str(dpi),
            "-f", str(batch_start), "-l", str(batch_end),
            SOURCE_PDF,
            f"{tmp_dir}/p"
        ], check=True)


def collect_pages(tmp_dir):
    pages = {}
    for name in os.listdir(tmp_dir):
        match = re.fullmatch(r"p-(\d+)\.jpg", name)
        if match:
            pages[int(match.group(1))] = os.path.join(tmp_dir, name)
    return pages


def mirror_file(src, rel_path):
    for base in ANDROID_MIRRORS:
        dst = os.path.join(base, rel_path)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)


def main():
    t0 = time.time()
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp_full = "/tmp/render_arabic_lit_full"
    tmp_opt = "/tmp/render_arabic_lit_opt"
    shutil.rmtree(tmp_full, ignore_errors=True)
    shutil.rmtree(tmp_opt, ignore_errors=True)

    print("[*] Rendering Arabic literature full pages (PDF 7..218)...")
    render_pass(7, 218, 200, 82, tmp_full)
    print("[*] Rendering Arabic literature optimized pages (PDF 7..218)...")
    render_pass(7, 218, 150, 78, tmp_opt)

    full_pages = collect_pages(tmp_full)
    opt_pages = collect_pages(tmp_opt)
    written = []
    for pdf_page in sorted(set(full_pages) | set(opt_pages)):
        if not (7 <= pdf_page <= 218):
            continue
        full_dst = os.path.join(OUT_DIR, f"page_{pdf_page:03d}.jpg")
        opt_dst = os.path.join(OUT_DIR, f"page_{pdf_page:03d}_opt.jpg")
        if pdf_page in full_pages:
            shutil.copy2(full_pages[pdf_page], full_dst)
            mirror_file(full_dst, f"pages/{os.path.basename(full_dst)}")
            written.append(full_dst)
        if pdf_page in opt_pages:
            shutil.copy2(opt_pages[pdf_page], opt_dst)
            mirror_file(opt_dst, f"pages/{os.path.basename(opt_dst)}")
            written.append(opt_dst)

    shutil.rmtree(tmp_full, ignore_errors=True)
    shutil.rmtree(tmp_opt, ignore_errors=True)
    total_mb = sum(os.path.getsize(p) for p in written) / (1024 * 1024)
    print(f"[✓] Arabic literature: {len(written)} images ({total_mb:.1f} MB).")
    print(f"[✓] Rendering completed in {time.time() - t0:.1f}s.")


if __name__ == "__main__":
    main()
