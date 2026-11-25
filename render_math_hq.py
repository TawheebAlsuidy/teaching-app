#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
High-resolution page renderer for Grade 12 Math (Scientific Section).

Canonical theory source: كتاب الرياضيات للصف الثالث الثانوي (259 PDF pages)
Practice source: كتاب التمارين للصف الثالث الثانوي (84 PDF pages)

Page mapping for both books: book_page = pdf_page - 2.
Theory reader pages: PDF 9..258 -> printed 7..256.
Workbook reference pages: PDF 8..82 -> printed 6..80.
"""
import os
import re
import shutil
import subprocess
import time

BASE_DIR = "/media/tawheeb/New Volume3/ذاكر/teaching-app"
THEORY_PDF = f"{BASE_DIR}/المنهج/ثالث ثانوي/الرياضيات-للصف-الثالث-الثانوي.pdf"
WORKBOOK_PDF = f"{BASE_DIR}/المنهج/ثالث ثانوي/الرياضيات-التمارين-للصف-الثالث-الثانوي-القسم-العلمي.pdf"
THEORY_DIR = f"{BASE_DIR}/assets/curriculum/grade12/math/pages"
WORKBOOK_DIR = f"{BASE_DIR}/assets/curriculum/grade12/math/workbook_pages"

ANDROID_MIRRORS = [
    f"{BASE_DIR}/thaker-android-src/assets/curriculum/grade12/math",
    f"{BASE_DIR}/thaker-android-src/assets/assets/curriculum/grade12/math",
]


def render_pass(pdf_path, start, end, dpi, quality, tmp_dir):
    os.makedirs(tmp_dir, exist_ok=True)
    for batch_start in range(start, end + 1, 50):
        batch_end = min(end, batch_start + 49)
        subprocess.run([
            "pdftoppm", "-jpeg", "-jpegopt", f"quality={quality}",
            "-r", str(dpi),
            "-f", str(batch_start), "-l", str(batch_end),
            pdf_path,
            f"{tmp_dir}/p"
        ], check=True)


def collect_pages(tmp_dir, prefix, suffix=""):
    pages = {}
    for name in os.listdir(tmp_dir):
        match = re.fullmatch(r"p-(\d+)\.jpg", name)
        if not match:
            continue
        pages[int(match.group(1))] = os.path.join(tmp_dir, name)
    return pages


def mirror_file(src, rel_path):
    for base in ANDROID_MIRRORS:
        dst = os.path.join(base, rel_path)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)


def render_book(pdf_path, start, end, out_dir, file_prefix):
    os.makedirs(out_dir, exist_ok=True)
    tmp_full = f"/tmp/render_math_{file_prefix}_full"
    tmp_opt = f"/tmp/render_math_{file_prefix}_opt"
    shutil.rmtree(tmp_full, ignore_errors=True)
    shutil.rmtree(tmp_opt, ignore_errors=True)

    print(f"[*] Rendering {file_prefix} full pages (PDF {start}..{end})...")
    render_pass(pdf_path, start, end, 200, 82, tmp_full)
    print(f"[*] Rendering {file_prefix} optimized pages (PDF {start}..{end})...")
    render_pass(pdf_path, start, end, 150, 78, tmp_opt)

    full_pages = collect_pages(tmp_full, file_prefix)
    opt_pages = collect_pages(tmp_opt, file_prefix)
    written = []
    for pdf_page in sorted(set(full_pages) | set(opt_pages)):
        if not (start <= pdf_page <= end):
            continue
        full_dst = os.path.join(out_dir, f"{file_prefix}_{pdf_page:03d}.jpg")
        opt_dst = os.path.join(out_dir, f"{file_prefix}_{pdf_page:03d}_opt.jpg")
        if pdf_page in full_pages:
            shutil.copy2(full_pages[pdf_page], full_dst)
            mirror_file(full_dst, f"pages/{os.path.basename(full_dst)}" if file_prefix == "page" else f"workbook_pages/{os.path.basename(full_dst)}")
            written.append(full_dst)
        if pdf_page in opt_pages:
            shutil.copy2(opt_pages[pdf_page], opt_dst)
            mirror_file(opt_dst, f"pages/{os.path.basename(opt_dst)}" if file_prefix == "page" else f"workbook_pages/{os.path.basename(opt_dst)}")
            written.append(opt_dst)

    shutil.rmtree(tmp_full, ignore_errors=True)
    shutil.rmtree(tmp_opt, ignore_errors=True)
    total_mb = sum(os.path.getsize(p) for p in written) / (1024 * 1024)
    print(f"[✓] {file_prefix}: {len(written)} images ({total_mb:.1f} MB).")
    return written


def main():
    t0 = time.time()
    render_book(THEORY_PDF, 9, 258, THEORY_DIR, "page")
    render_book(WORKBOOK_PDF, 8, 82, WORKBOOK_DIR, "workbook_page")
    print(f"[✓] Math page rendering completed in {time.time() - t0:.1f}s.")


if __name__ == "__main__":
    main()
