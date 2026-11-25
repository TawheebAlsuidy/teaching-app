#!/usr/bin/env python3
"""
Sync curriculum data, HTML books, and assets to Android assets directory.
Enforces the Single Source of Truth architecture (P0-D).
"""
import os
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_DATA = os.path.join(ROOT, "data", "curriculum")
DST_DATA = os.path.join(ROOT, "thaker-android-src", "assets", "data", "curriculum")

def sync():
    print(f"[*] Syncing curriculum data: {SRC_DATA} -> {DST_DATA}")
    for root, dirs, files in os.walk(SRC_DATA):
        rel = os.path.relpath(root, SRC_DATA)
        target_dir = os.path.join(DST_DATA, rel)
        os.makedirs(target_dir, exist_ok=True)
        for f in files:
            s_file = os.path.join(root, f)
            d_file = os.path.join(target_dir, f)
            shutil.copy2(s_file, d_file)

    # Sync interactive HTML books to android assets
    books = [
        "chemistry-12th-book.html",
        "physics-12th-book.html",
        "biology-12th-book.html",
        "chem-lab-book.html",
    ]
    assets_dir = os.path.join(ROOT, "thaker-android-src", "assets")
    os.makedirs(assets_dir, exist_ok=True)

    for b in books:
        src_book = os.path.join(ROOT, b)
        if os.path.exists(src_book):
            shutil.copy2(src_book, os.path.join(assets_dir, b))
            print(f"[✓] Mirrored {b} to Android assets.")
        else:
            print(f"[!] Warning: {src_book} not found.")

    print("[✓] Sync completed successfully.")

if __name__ == "__main__":
    sync()
