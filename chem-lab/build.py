#!/usr/bin/env python3
"""
Production Build Script for Chem Lab Book (معمل كيمياء الثالث الثانوي - اليمن)
Bundles src/ into a single standalone offline HTML file: dist/chem-lab-book.html
"""
import os
import sys
import json
import base64
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
DIST_DIR = os.path.join(BASE_DIR, "dist")
WORKSPACE_ROOT = os.path.dirname(BASE_DIR)

def build():
    print("=== Building chem-lab-book.html (المرحلة أ: الأساس) ===")
    os.makedirs(DIST_DIR, exist_ok=True)

    index_path = os.path.join(SRC_DIR, "index.html")
    styles_path = os.path.join(SRC_DIR, "styles.css")
    vendor_three_path = os.path.join(SRC_DIR, "vendor", "three.min.js")
    questions_path = os.path.join(SRC_DIR, "data", "questions.json")
    pages_dir = os.path.join(SRC_DIR, "assets", "pages")
    app_path = os.path.join(SRC_DIR, "app.js")

    # 1. Read files
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    with open(styles_path, "r", encoding="utf-8") as f:
        css = f.read()

    with open(vendor_three_path, "r", encoding="utf-8") as f:
        three_js = f.read()

    with open(questions_path, "r", encoding="utf-8") as f:
        questions_json_data = json.load(f)

    with open(app_path, "r", encoding="utf-8") as f:
        app_js = f.read()

    # 2. Encode page JPGs into PG dictionary
    pg_dict = {}
    page_files = sorted(os.listdir(pages_dir), key=lambda x: int(x.split(".")[0]) if x.split(".")[0].isdigit() else 9999)
    print(f"-> Processing {len(page_files)} textbook page images...")
    for pf in page_files:
        if not pf.endswith(".jpg"): continue
        page_num = pf.split(".")[0]
        full_pf = os.path.join(pages_dir, pf)
        with open(full_pf, "rb") as img_f:
            b64_str = base64.b64encode(img_f.read()).decode("ascii")
            pg_dict[page_num] = f"data:image/jpeg;base64,{b64_str}"

    pg_code = "const PG = " + json.dumps(pg_dict, ensure_ascii=False) + ";"
    questions_code = "const QUESTIONS_DATA = " + json.dumps(questions_json_data, ensure_ascii=False) + ";"

    # 3. Inline styles
    html = html.replace(
        '<link rel="stylesheet" href="styles.css">',
        f'<style>\n{css}\n</style>'
    )

    # 4. Inline Three.js
    html = html.replace(
        '<script src="vendor/three.min.js"></script>',
        f'<script>\n/**\n * Three.js r128 minified\n */\n{three_js}\n</script>'
    )

    # 5. Inline PG, questions, and app.js
    combined_script = f"<script>\n{pg_code}\n\n{questions_code}\n\n{app_js}\n</script>"
    html = html.replace(
        '<script src="app.js"></script>',
        combined_script
    )

    # 6. Write final dist file
    out_dist_path = os.path.join(DIST_DIR, "chem-lab-book.html")
    with open(out_dist_path, "w", encoding="utf-8") as f:
        f.write(html)

    size_mb = os.path.getsize(out_dist_path) / (1024 * 1024)
    print(f"✓ Generated standalone bundle: {out_dist_path} ({size_mb:.2f} MB)")

    # 7. Sync with root workspace and Android assets
    root_chem_path = os.path.join(WORKSPACE_ROOT, "chem-lab-book.html")
    shutil.copy2(out_dist_path, root_chem_path)
    print(f"✓ Synchronized to workspace root: {root_chem_path}")

    android_assets_chem = os.path.join(WORKSPACE_ROOT, "thaker-android-src", "assets", "chem-lab-book.html")
    if os.path.exists(os.path.dirname(android_assets_chem)):
        shutil.copy2(out_dist_path, android_assets_chem)
        print(f"✓ Synchronized to Android assets: {android_assets_chem}")

    print("=== Build Completed Successfully! ===")
    return out_dist_path

if __name__ == "__main__":
    build()
