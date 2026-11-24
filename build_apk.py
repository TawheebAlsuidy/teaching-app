#!/usr/bin/env python3
"""
Comprehensive Build Script for "ذاكر" (Thaker) Android APK
Featuring:
- High School (3rd Secondary 3D Chemistry Lab Book)
- Middle School (9th Grade Complete Official Curriculum: Science Part 1 & 2, Math Part 1 & 2)
- 9th Grade Interactive Science Lab (13 simplified 3D lessons + quizzes)
- Native Hardware-Accelerated PDF Viewer with Zoom & Navigation
- Interactive Ministerial Exams for 9th Grade
- Educational Summaries & Mathematical Laws
"""
import os
import sys
import re
import shutil
import subprocess
import math
from PIL import Image, ImageDraw, ImageFont

SDK_DIR = "/opt/android-sdk"
BUILD_TOOLS_DIR = f"{SDK_DIR}/build-tools/36.0.0"
PLATFORM_JAR = f"{SDK_DIR}/platforms/android-36/android.jar"
AAPT2 = f"{BUILD_TOOLS_DIR}/aapt2"
D8 = f"{BUILD_TOOLS_DIR}/d8"
ZIPALIGN = f"{BUILD_TOOLS_DIR}/zipalign"
APKSIGNER = f"{BUILD_TOOLS_DIR}/apksigner"

WORKSPACE = "/mnt/sdcard/projects/teaching-app"
SOURCE_HTML = f"{WORKSPACE}/chem-lab-book.html"
SOURCE_SCI9_HTML = f"{WORKSPACE}/science9-interactive.html"
SOURCE_SCI9_3D = f"{WORKSPACE}/science-9th-book.html"
SOURCE_MATH9_3D = f"{WORKSPACE}/math-9th-book.html"
CURRICULUM_9TH_DIR = f"{WORKSPACE}/المنهج/تاسع"
BUILD_DIR = "/tmp/thaker_full_build"
KEYSTORE_PATH = f"{BUILD_DIR}/thaker_debug.keystore"

FINAL_APK_EN = f"{WORKSPACE}/Thaker.apk"
FINAL_APK_AR = f"{WORKSPACE}/ذاكر.apk"

def make_icons(res_dir):
    print("-> Generating high-resolution Thaker App Icons...")
    sizes = {
        "mipmap-mdpi": 48,
        "mipmap-hdpi": 72,
        "mipmap-xhdpi": 96,
        "mipmap-xxhdpi": 144,
        "mipmap-xxxhdpi": 192,
    }

    def mark(d, cx, cy, s, cap, cap_line, cover, page, line):
        capw = int(s * 0.58)
        caph = int(s * 0.20)
        top = cy - int(s * 0.30)
        cap_pts = [
            (cx, top),
            (cx - capw // 2, top + caph // 2),
            (cx - capw // 2, top + caph),
            (cx - capw // 2 + int(s * 0.05), top + caph),
            (cx - capw // 2 + int(s * 0.05), top + caph + int(s * 0.13)),
            (cx + capw // 2 - int(s * 0.05), top + caph + int(s * 0.13)),
            (cx + capw // 2 - int(s * 0.05), top + caph),
            (cx + capw // 2, top + caph),
            (cx + capw // 2, top + caph // 2),
        ]
        d.polygon(cap_pts, fill=cap)
        d.line([(cx + capw // 2 - int(s * 0.06), top + caph + int(s * 0.06)),
                (cx + capw // 2 + int(s * 0.16), top + caph + int(s * 0.06))], fill=cap_line, width=max(1, int(s * 0.035)))
        d.ellipse([cx + capw // 2 + int(s * 0.13), top + caph + int(s * 0.03),
                   cx + capw // 2 + int(s * 0.23), top + caph + int(s * 0.13)], fill=cap_line)

        bw = int(s * 0.66)
        bh = int(s * 0.28)
        by = cy + int(s * 0.10)
        left = [(cx, by - bh // 3), (cx - bw // 2, by - bh // 2),
                (cx - bw // 2, by + bh // 2), (cx, by + bh // 3)]
        right = [(cx, by - bh // 3), (cx + bw // 2, by - bh // 2),
                 (cx + bw // 2, by + bh // 2), (cx, by + bh // 3)]
        d.polygon(left, fill=page)
        d.polygon(right, fill=cover)
        d.line([(cx, by - bh // 3), (cx, by + bh // 3)], fill=line, width=max(1, int(s * 0.02)))
        for i in range(2):
            yy = by - bh // 6 + i * int(s * 0.07)
            d.line([(cx - bw // 3, yy), (cx - int(s * 0.05), yy + int(s * 0.02))], fill=(0, 120, 86, 110), width=max(1, int(s * 0.012)))
            d.line([(cx + int(s * 0.05), yy + int(s * 0.02)), (cx + bw // 3, yy)], fill=(255, 255, 255, 150), width=max(1, int(s * 0.012)))

    def gradient(size, c1, c2):
        strip = Image.new("RGB", (1, size))
        p = strip.load()
        for y in range(size):
            t = y / float(size - 1)
            p[0, y] = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
        return strip.resize((size, size)).convert("RGBA")

    for folder, size in sizes.items():
        out_folder = os.path.join(res_dir, folder)
        os.makedirs(out_folder, exist_ok=True)
        hi = size * 4
        bg = gradient(hi, (0, 201, 133), (0, 128, 92))
        d = ImageDraw.Draw(bg, "RGBA")
        d.ellipse([hi * 0.62, -hi * 0.12, hi * 1.18, hi * 0.44], fill=(255, 255, 255, 34))
        d.ellipse([-hi * 0.18, hi * 0.64, hi * 0.38, hi * 1.18], fill=(255, 255, 255, 26))
        mark(d, hi // 2, hi // 2, hi * 0.62, (255, 255, 255, 245), (2, 92, 68, 220),
             (2, 104, 78, 235), (245, 255, 250, 250), (0, 150, 104, 220))
        img = bg.resize((size, size), Image.LANCZOS)
        img.save(os.path.join(out_folder, "ic_launcher.png"), "PNG")
        if size == 192:
            os.makedirs(os.path.join(res_dir, "drawable-nodpi"), exist_ok=True)
            img.save(os.path.join(res_dir, "drawable-nodpi", "ic_launcher_splash.png"), "PNG")

        mask = Image.new("L", (hi, hi), 0)
        ImageDraw.Draw(mask).ellipse([0, 0, hi - 1, hi - 1], fill=255)
        round_img = Image.new("RGBA", (hi, hi), (0, 0, 0, 0))
        round_img.paste(bg, (0, 0), mask)
        round_img.resize((size, size), Image.LANCZOS).save(os.path.join(out_folder, "ic_launcher_round.png"), "PNG")

    fg_size = 432
    fg = Image.new("RGBA", (fg_size, fg_size), (0, 0, 0, 0))
    fgd = ImageDraw.Draw(fg, "RGBA")
    mark(fgd, fg_size // 2, fg_size // 2, fg_size * 0.58, (255, 255, 255, 255), (0, 96, 72, 255),
         (0, 104, 78, 255), (244, 255, 250, 255), (0, 150, 104, 255))
    os.makedirs(os.path.join(res_dir, "drawable-nodpi"), exist_ok=True)
    fg.save(os.path.join(res_dir, "drawable-nodpi", "ic_launcher_foreground.png"), "PNG")

    adaptive_dir = os.path.join(res_dir, "mipmap-anydpi-v26")
    os.makedirs(adaptive_dir, exist_ok=True)
    for name in ["ic_launcher.xml", "ic_launcher_round.xml"]:
        with open(os.path.join(adaptive_dir, name), "w", encoding="utf-8") as f:
            f.write("""<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background" />
    <foreground android:drawable="@drawable/ic_launcher_foreground" />
</adaptive-icon>
""")

    print("  ✓ App icons created.")

def make_subject_illustrations(res_dir):
    out_dir = f"{res_dir}/drawable-nodpi"
    os.makedirs(out_dir, exist_ok=True)
    size = 512

    def load_font(px, arabic=False):
        fp = "/tmp/Tajawal-Bold.ttf" if arabic else "/tmp/Tajawal-Bold.ttf"
        try:
            return ImageFont.truetype(fp, px)
        except Exception:
            return ImageFont.load_default()

    # 1. Hero Lab (Floating 3D Erlenmeyer flask with glowing green liquid, neon orbit, floating atoms)
    img_hero = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img_hero, "RGBA")
    # Soft mint glow
    for r in range(size//2, 40, -15):
        alpha = int(22 * (1 - r / (size//2)))
        d.ellipse([size//2 - r, size//2 - r, size//2 + r, size//2 + r], fill=(0, 230, 118, alpha))
    cx, cy = size//2, int(size * 0.58)
    orbit_w, orbit_h = int(size * 0.44), int(size * 0.22)
    for w in range(5, 0, -1):
        d.ellipse([cx - orbit_w - w, cy - int(size * 0.16) - orbit_h//2 - w,
                   cx + orbit_w + w, cy - int(size * 0.16) + orbit_h//2 + w],
                  outline=(0, 230, 118, 180), width=3)
    spheres = [
        (cx - 150, cy - 80, 22, (0, 230, 118, 240)),
        (cx + 140, cy - 100, 18, (105, 240, 174, 230)),
        (cx - 120, cy + 60, 14, (0, 230, 118, 220)),
        (cx + 130, cy + 50, 16, (56, 189, 248, 220)),
        (cx - 80, cy - 150, 12, (105, 240, 174, 210)),
        (cx + 90, cy - 170, 14, (0, 230, 118, 230)),
    ]
    for sx, sy, sr, col in spheres:
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=col)
        d.ellipse([sx - sr//2, sy - sr//2, sx - sr//6, sy - sr//6], fill=(255, 255, 255, 180))
    nw, nh = int(size * 0.08), int(size * 0.24)
    top_y = cy - int(size * 0.38)
    neck_bottom_y = top_y + nh
    bw = int(size * 0.28)
    base_y = cy + int(size * 0.22)
    flask_poly = [(cx - nw, top_y), (cx + nw, top_y), (cx + nw, neck_bottom_y), (cx + bw, base_y), (cx - bw, base_y), (cx - nw, neck_bottom_y)]
    liq_top_y = cy - int(size * 0.02)
    t = (liq_top_y - neck_bottom_y) / (base_y - neck_bottom_y)
    lw = int(nw + t * (bw - nw))
    d.polygon([(cx - lw, liq_top_y), (cx + lw, liq_top_y), (cx + bw - 6, base_y - 6), (cx - bw + 6, base_y - 6)], fill=(0, 200, 83, 230))
    d.ellipse([cx - lw, liq_top_y - 10, cx + lw, liq_top_y + 10], fill=(105, 240, 174, 240))
    for bx, by, br in [(cx - 30, cy + 40, 10), (cx + 25, cy + 20, 12), (cx - 10, cy + 60, 8), (cx + 40, cy + 50, 7), (cx, cy + 10, 6)]:
        d.ellipse([bx - br, by - br, bx + br, by + br], fill=(255, 255, 255, 160))
        d.ellipse([bx - br, by - br, bx + br, by + br], outline=(255, 255, 255, 220), width=2)
    d.polygon(flask_poly, outline=(180, 245, 210, 220), width=5)
    d.ellipse([cx - nw - 4, top_y - 6, cx + nw + 4, top_y + 6], fill=(220, 255, 235, 230), outline=(180, 245, 210, 240), width=3)
    d.line([(cx - bw + 14, base_y - 14), (cx - nw + 8, neck_bottom_y + 10)], fill=(255, 255, 255, 140), width=6)
    img_hero.save(f"{out_dir}/illustration_hero_lab.png", "PNG")

    # 2. Featured Lab (3D cube badge + flask + molecules + 3D book)
    img_feat = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img_feat, "RGBA")
    bx, by, bw_badge, bh_badge = 50, 50, 110, 110
    d.rounded_rectangle([bx, by, bx + bw_badge, by + bh_badge], radius=24, fill=(0, 176, 80, 240), outline=(105, 240, 174, 255), width=3)
    f_badge = load_font(48, True)
    d.text((bx + 16, by + 16), "3D", fill=(255, 255, 255), font=f_badge)
    cx, cy = 180, 360
    d.ellipse([cx - 100, cy - 80, cx - 60, cy - 40], fill=(56, 189, 248, 240))
    d.ellipse([cx - 120, cy - 10, cx - 80, cy + 30], fill=(16, 185, 129, 240))
    d.line([(cx - 80, cy - 60), (cx - 100, cy + 10)], fill=(148, 163, 184, 180), width=4)
    d.line([(cx - 80, cy - 60), (cx - 30, cy - 40)], fill=(148, 163, 184, 180), width=4)
    d.ellipse([cx - 40, cy - 50, cx - 10, cy - 20], fill=(56, 189, 248, 240))
    nw, nh = 26, 70
    top_y = cy - 120
    neck_bot = top_y + nh
    bw_flask = 90
    base_y = cy + 70
    poly = [(cx - nw, top_y), (cx + nw, top_y), (cx + nw, neck_bot), (cx + bw_flask, base_y), (cx - bw_flask, base_y), (cx - nw, neck_bot)]
    liq_y = cy - 20
    t = (liq_y - neck_bot) / (base_y - neck_bot)
    lw = int(nw + t * (bw_flask - nw))
    d.polygon([(cx - lw, liq_y), (cx + lw, liq_y), (cx + bw_flask - 4, base_y - 4), (cx - bw_flask + 4, base_y - 4)], fill=(0, 200, 83, 235))
    d.ellipse([cx - lw, liq_y - 8, cx + lw, liq_y + 8], fill=(105, 240, 174, 250))
    d.polygon(poly, outline=(180, 245, 210, 220), width=4)
    d.ellipse([cx - nw - 3, top_y - 4, cx + nw + 3, top_y + 4], fill=(220, 255, 235, 240), outline=(180, 245, 210, 240), width=2)
    d.line([(cx - bw_flask + 10, base_y - 8), (cx - nw + 6, neck_bot + 6)], fill=(255, 255, 255, 140), width=5)
    bk_x, bk_y = 350, 220
    bk_w, bk_h = 130, 190
    d.polygon([(bk_x + bk_w, bk_y), (bk_x + bk_w + 22, bk_y - 12), (bk_x + bk_w + 22, bk_y + bk_h - 12), (bk_x + bk_w, bk_y + bk_h)], fill=(240, 245, 240))
    d.polygon([(bk_x, bk_y), (bk_x + 22, bk_y - 12), (bk_x + bk_w + 22, bk_y - 12), (bk_x + bk_w, bk_y)], fill=(220, 235, 225))
    d.rounded_rectangle([bk_x, bk_y, bk_x + bk_w, bk_y + bk_h], radius=12, fill=(0, 140, 68), outline=(0, 176, 80), width=3)
    em_cx, em_cy = bk_x + bk_w//2, bk_y + bk_h//2
    d.polygon([(em_cx - 8, em_cy - 24), (em_cx + 8, em_cy - 24), (em_cx + 8, em_cy - 8), (em_cx + 24, em_cy + 24), (em_cx - 24, em_cy + 24), (em_cx - 8, em_cy - 8)], outline=(255, 255, 255), width=3)
    d.line([(em_cx - 10, em_cy - 24), (em_cx + 10, em_cy - 24)], fill=(255, 255, 255), width=3)
    img_feat.save(f"{out_dir}/illustration_featured_lab.png", "PNG")
    img_feat.save(f"{out_dir}/illustration_chemistry.png", "PNG")

    # 3. Physics (Atom with blue squircle theme)
    img_phy = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    dp = ImageDraw.Draw(img_phy, "RGBA")
    dp.rounded_rectangle([20, 20, size - 20, size - 20], radius=90, fill=(224, 242, 254, 255), outline=(186, 230, 253, 255), width=4)
    pcx, pcy = size//2, size//2
    for r in range(40, 0, -8):
        dp.ellipse([pcx - r, pcy - r, pcx + r, pcy + r], fill=(2, 132, 199, int(220 * (1 - r/45))))
    dp.ellipse([pcx - 14, pcy - 14, pcx + 14, pcy + 14], fill=(255, 255, 255, 240))
    dp.ellipse([pcx - 180, pcy - 70, pcx + 180, pcy + 70], outline=(2, 132, 199, 220), width=8)
    dp.ellipse([pcx - 80, pcy - 170, pcx + 80, pcy + 170], outline=(14, 165, 233, 200), width=7)
    dp.ellipse([pcx - 140, pcy - 140, pcx + 140, pcy + 140], outline=(56, 189, 248, 190), width=6)
    for ex, ey in [(pcx + 160, pcy - 30), (pcx - 60, pcy + 150), (pcx - 120, pcy - 100), (pcx + 100, pcy + 120)]:
        dp.ellipse([ex - 12, ey - 12, ex + 12, ey + 12], fill=(2, 132, 199, 255))
        dp.ellipse([ex - 5, ey - 5, ex + 5, ey + 5], fill=(255, 255, 255, 230))
    img_phy.save(f"{out_dir}/illustration_physics.png", "PNG")

    # 4. Biology (DNA Helix with purple squircle theme)
    img_bio = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    db = ImageDraw.Draw(img_bio, "RGBA")
    db.rounded_rectangle([20, 20, size - 20, size - 20], radius=90, fill=(243, 232, 255, 255), outline=(233, 213, 255, 255), width=4)
    pts1, pts2 = [], []
    for i in range(24):
        y = 70 + i * 16
        x1 = size//2 + int(110 * math.sin(i * 0.45))
        x2 = size//2 - int(110 * math.sin(i * 0.45))
        pts1.append((x1, y))
        pts2.append((x2, y))
    for i in range(len(pts1)):
        if i % 2 == 0:
            db.line([pts1[i], pts2[i]], fill=(147, 51, 234, 180), width=6)
            db.ellipse([pts1[i][0] - 8, pts1[i][1] - 8, pts1[i][0] + 8, pts1[i][1] + 8], fill=(168, 85, 247, 240))
            db.ellipse([pts2[i][0] - 8, pts2[i][1] - 8, pts2[i][0] + 8, pts2[i][1] + 8], fill=(147, 51, 234, 240))
    db.line(pts1, fill=(147, 51, 234, 255), width=12)
    db.line(pts2, fill=(168, 85, 247, 255), width=12)
    img_bio.save(f"{out_dir}/illustration_biology.png", "PNG")

    # 5. Science & Mathematics & others
    for name in ["science", "mathematics", "english", "arabic", "computer"]:
        img_gen = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        dg = ImageDraw.Draw(img_gen, "RGBA")
        if name == "science":
            dg.rounded_rectangle([20, 20, size - 20, size - 20], radius=90, fill=(204, 251, 241, 255), outline=(153, 246, 228, 255), width=4)
            dg.ellipse([size//2 - 90, size//2 - 90, size//2 + 90, size//2 + 90], outline=(13, 148, 136, 220), width=10)
            dg.line([(size//2 - 120, size//2 + 100), (size//2 + 120, size//2 + 100)], fill=(13, 148, 136, 255), width=12)
        elif name == "mathematics":
            dg.rounded_rectangle([20, 20, size - 20, size - 20], radius=90, fill=(237, 233, 254, 255), outline=(221, 214, 254, 255), width=4)
            f_math = load_font(120, False)
            dg.text((120, 160), "π", fill=(109, 40, 217, 255), font=f_math)
            dg.text((280, 160), "√", fill=(124, 58, 237, 255), font=f_math)
        else:
            dg.rounded_rectangle([20, 20, size - 20, size - 20], radius=90, fill=(241, 245, 249, 255), outline=(226, 232, 240, 255), width=4)
        img_gen.save(f"{out_dir}/illustration_{name}.png", "PNG")


def apply_design_tokens(base_dir):
    res_dir = f"{base_dir}/res"
    mapping = {
        "@color/bg_dark": "?attr/thakerBackground",
        "@color/card_dark": "?attr/thakerSurface",
        "@color/card_border": "?attr/thakerBorder",
        "@color/cyan_accent": "?attr/thakerPrimary",
        "@color/gold_accent": "?attr/thakerPrimary",
        "@color/green_accent": "?attr/thakerSuccess",
        "@color/red_accent": "?attr/thakerError",
        "@color/text_primary": "?attr/thakerTextPrimary",
        "@color/text_secondary": "?attr/thakerTextSecondary",
        "@color/btn_start": "?attr/thakerPrimary",
        "@color/btn_end": "?attr/thakerPrimaryDark",
        "@color/paper": "?attr/thakerPrimaryLight",
        "@color/paper_ink": "?attr/thakerTextPrimary",
        "@color/paper_muted": "?attr/thakerTextSecondary",
        "@color/rule": "?attr/thakerBorder",
        "#111C22": "?attr/thakerBackground",
        "#1A282F": "?attr/thakerSurface",
        "#16232A": "?attr/thakerSurface",
        "#33434A": "?attr/thakerBorder",
        "#C9A15C": "?attr/thakerPrimary",
        "#D7B26B": "?attr/thakerPrimaryLight",
        "#7FA98B": "?attr/thakerSuccess",
        "#B85C4A": "?attr/thakerError",
        "#F2EAD9": "?attr/thakerTextPrimary",
        "#A9AEA6": "?attr/thakerTextSecondary",
        "#EFE7D6": "?attr/thakerPrimaryLight",
        "#1F2A2F": "?attr/thakerTextPrimary",
        "#6F7369": "?attr/thakerTextSecondary",
        "#8A6B33": "?attr/thakerPrimaryDark",
        "#064E3B": "?attr/thakerPrimaryLight",
        "#1E293B": "?attr/thakerSurfaceSoft",
        "#475569": "?attr/thakerBorder",
        "#0E7490": "?attr/thakerPhysics",
        "#7C3AED": "?attr/thakerBiology",
        "#162238": "?attr/thakerSurface",
        "#0F172A": "?attr/thakerSurface",
        "#E00B132B": "?attr/thakerBackground",
        "#D00B132B": "?attr/thakerBackground",
        "#2A3B5C": "?attr/thakerBorder",
        "#166534": "?attr/thakerPrimaryDark",
        "#22C55E": "?attr/thakerSuccess",
        "#991B1B": "?attr/thakerError",
        "#EF4444": "?attr/thakerError",
        "#050C16": "?attr/thakerBackground",
    }
    for folder in ["layout", "drawable"]:
        folder_path = os.path.join(res_dir, folder)
        for name in os.listdir(folder_path):
            if not name.endswith(".xml"):
                continue
            file_path = os.path.join(folder_path, name)
            text = open(file_path, encoding="utf-8").read()
            for old, new in mapping.items():
                text = text.replace(old, new)
            open(file_path, "w", encoding="utf-8").write(text)


def prune_unused_drawables(base_dir):
    res_dir = f"{base_dir}/res"
    refs = set()
    for folder in ["layout", "drawable", "values"]:
        folder_path = os.path.join(res_dir, folder)
        for name in os.listdir(folder_path):
            if name.endswith(".xml"):
                text = open(os.path.join(folder_path, name), encoding="utf-8").read()
                refs.update(re.findall(r"@drawable/(\w+)", text))
    adaptive_dir = os.path.join(res_dir, "mipmap-anydpi-v26")
    if os.path.exists(adaptive_dir):
        for name in os.listdir(adaptive_dir):
            if name.endswith(".xml"):
                text = open(os.path.join(adaptive_dir, name), encoding="utf-8").read()
                refs.update(re.findall(r"@drawable/(\w+)", text))
    java_dir = os.path.join(base_dir, "src", "com", "thaker", "app")
    if os.path.exists(java_dir):
        for name in os.listdir(java_dir):
            if name.endswith(".java"):
                text = open(os.path.join(java_dir, name), encoding="utf-8").read()
                refs.update(re.findall(r"R\.drawable\.(\w+)", text))
    drawable_dir = os.path.join(res_dir, "drawable")
    for name in os.listdir(drawable_dir):
        if name.endswith(".xml") and name[:-4] not in refs:
            os.remove(os.path.join(drawable_dir, name))

def write_resources(base_dir):
    print("-> Writing complete Android resources (layouts, drawables, strings, styles)...")
    res_dir = f"{base_dir}/res"
    os.makedirs(f"{res_dir}/values", exist_ok=True)
    os.makedirs(f"{res_dir}/drawable", exist_ok=True)
    os.makedirs(f"{res_dir}/layout", exist_ok=True)
    
    # 1. Strings
    with open(f"{res_dir}/values/strings.xml", "w", encoding="utf-8") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">ذاكر</string>
    <string name="app_tagline">منصتك التعليمية الشاملة</string>
    <string name="app_tagline_new">منصتك التعليمية الشاملة</string>
    <string name="stage_high_school">الثانوية</string>
    <string name="stage_middle_school">الإعدادية</string>
    <string name="grade_12_title">الصف الثالث الثانوي · علمي</string>
    <string name="grade_9_title">الصف التاسع الأساسي</string>
    
    <!-- 9th Grade Subject Names -->
    <string name="sci_p1_title">العلوم · الجزء الأول</string>
    <string name="sci_p1_sub">المحاليل، التفاعلات، الصوت والضوء، الإخراج، التكاثر</string>
    <string name="sci_p2_title">العلوم · الجزء الثاني</string>
    <string name="sci_p2_sub">الكهرباء، الطاقة، البيئة، علوم الأرض والفضاء</string>
    <string name="math_p1_title">الرياضيات · الجزء الأول</string>
    <string name="math_p1_sub">المجموعات، الأعداد الحقيقية، المقادير الجبرية</string>
    <string name="math_p2_title">الرياضيات · الجزء الثاني</string>
    <string name="math_p2_sub">الهندسة، الدائرة، حساب المثلثات، الإحصاء</string>
    
    <string name="btn_read_book">الكتاب</string>
    <string name="btn_index">الفهرس</string>
    <string name="btn_summary">الملخص</string>
    <string name="btn_quiz">اختبار</string>
    <string name="btn_comprehensive_quiz">الاختبار الشامل · تاسع</string>
    
    <!-- Chem 3D Lab Strings -->
    <string name="chem_card_title">كتاب ومعمل الكيمياء</string>
    <string name="chem_card_subtitle">الثالث الثانوي · المنهج اليمني</string>
    <string name="chem_card_desc">اقرأ الكتاب، وجرّب التفاعلات بثلاثة أبعاد، واستمع للشرح. يعمل دون اتصال.</string>
    <string name="btn_start_lab">افتح المعمل</string>
    <string name="tag_curriculum">20 صفحة ممسوحة</string>
    <string name="tag_experiments">15 تجربة 3D</string>
    <string name="tag_offline">بدون إنترنت</string>
    <string name="tag_interactive">تفاعل باللمس</string>
    <string name="auto_launch_pref">فتح المعمل عند تشغيل التطبيق</string>
    <string name="about_app">عن ذاكر</string>

    <string name="section_books_title">الكتب الدراسية</string>
    <string name="section_books_sub">اختر المادة التي تريد دراستها</string>
    <string name="subject_physics">الفيزياء</string>
    <string name="subject_physics_sub">الصوت، الضوء، الكهرباء والطاقة</string>
    <string name="subject_biology">الأحياء</string>
    <string name="subject_biology_sub">الخلية، الوراثة، البيئة والجسم</string>
    <string name="subject_math">الرياضيات</string>
    <string name="subject_math_sub">الجبر، الهندسة والإحصاء</string>
    <string name="subject_science">العلوم</string>
    <string name="subject_science_sub">المحاليل، التفاعلات وعلوم الأرض</string>
    <string name="soon">قريباً</string>
    <string name="book_science_3d">كتاب ومعمل العلوم 3D</string>
    <string name="book_math_3d">كتاب ومعمل الرياضيات 3D</string>
    <string name="science_lab">معمل العلوم التفاعلي</string>

    <string name="nav_home">الرئيسية</string>
    <string name="nav_subjects">موادي</string>
    <string name="nav_library">المكتبة</string>
    <string name="nav_favorites">المفضلة</string>
    <string name="nav_settings">الإعدادات</string>
    <string name="theme_light">الوضع الفاتح</string>
    <string name="theme_dark">الوضع الداكن</string>
    <string name="theme_toggle">تغيير المظهر</string>
    <string name="library_title">مكتبة ذاكر</string>
    <string name="favorites_empty">لم تضف أي مادة إلى المفضلة بعد.</string>
</resources>""")

    # 2. Colors and theme tokens
    with open(f"{res_dir}/values/colors.xml", "w", encoding="utf-8") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<resources>
    <!-- Light Mode (Exact match to prototipe.for.image.png) -->
    <color name="light_background">#F5FAF7</color>
    <color name="light_surface">#FFFFFF</color>
    <color name="light_surface_elevated">#FFFFFF</color>
    <color name="light_surface_soft">#EDF8F2</color>
    <color name="light_text_primary">#0F172A</color>
    <color name="light_text_secondary">#64748B</color>
    <color name="light_border">#E2F0E7</color>
    <color name="light_primary">#00A859</color>
    <color name="light_primary_dark">#008C4A</color>
    <color name="light_primary_light">#E8F8F0</color>
    <color name="light_disabled">#CBD5E1</color>
    <color name="light_success">#059669</color>
    <color name="light_warning">#F59E0B</color>
    <color name="light_error">#EF4444</color>
    <color name="light_physics">#0284C7</color>
    <color name="light_biology">#9333EA</color>

    <!-- Dark Mode -->
    <color name="dark_background">#0B151C</color>
    <color name="dark_surface">#12242E</color>
    <color name="dark_surface_elevated">#182F3B</color>
    <color name="dark_surface_soft">#1A3D36</color>
    <color name="dark_text_primary">#F8FAFC</color>
    <color name="dark_text_secondary">#94A3B8</color>
    <color name="dark_border">#244852</color>
    <color name="dark_primary">#00D678</color>
    <color name="dark_primary_dark">#00A859</color>
    <color name="dark_primary_light">#1A453B</color>
    <color name="dark_disabled">#334D55</color>
    <color name="dark_success">#10B981</color>
    <color name="dark_warning">#FBBF24</color>
    <color name="dark_error">#F87171</color>
    <color name="dark_physics">#38BDF8</color>
    <color name="dark_biology">#C084FC</color>
</resources>""")

    with open(f"{res_dir}/values/attrs.xml", "w", encoding="utf-8") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<resources>
    <attr name="thakerBackground" format="color" />
    <attr name="thakerSurface" format="color" />
    <attr name="thakerSurfaceElevated" format="color" />
    <attr name="thakerSurfaceSoft" format="color" />
    <attr name="thakerTextPrimary" format="color" />
    <attr name="thakerTextSecondary" format="color" />
    <attr name="thakerBorder" format="color" />
    <attr name="thakerPrimary" format="color" />
    <attr name="thakerPrimaryDark" format="color" />
    <attr name="thakerPrimaryLight" format="color" />
    <attr name="thakerDisabled" format="color" />
    <attr name="thakerSuccess" format="color" />
    <attr name="thakerWarning" format="color" />
    <attr name="thakerError" format="color" />
    <attr name="thakerPhysics" format="color" />
    <attr name="thakerBiology" format="color" />
</resources>""")

    with open(f"{res_dir}/values/styles.xml", "w", encoding="utf-8") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="AppTheme" parent="@android:style/Theme.Material.NoActionBar">
        <item name="android:windowBackground">@drawable/splash_background</item>
        <item name="android:colorPrimary">@color/dark_primary</item>
        <item name="android:colorPrimaryDark">@color/dark_primary_dark</item>
        <item name="android:colorAccent">@color/dark_primary</item>
        <item name="android:textColorPrimary">@color/dark_text_primary</item>
        <item name="android:textColorSecondary">@color/dark_text_secondary</item>
        <item name="android:windowLightStatusBar">false</item>
        <item name="thakerBackground">@color/dark_background</item>
        <item name="thakerSurface">@color/dark_surface</item>
        <item name="thakerSurfaceElevated">@color/dark_surface_elevated</item>
        <item name="thakerSurfaceSoft">@color/dark_surface_soft</item>
        <item name="thakerTextPrimary">@color/dark_text_primary</item>
        <item name="thakerTextSecondary">@color/dark_text_secondary</item>
        <item name="thakerBorder">@color/dark_border</item>
        <item name="thakerPrimary">@color/dark_primary</item>
        <item name="thakerPrimaryDark">@color/dark_primary_dark</item>
        <item name="thakerPrimaryLight">@color/dark_primary_light</item>
        <item name="thakerDisabled">@color/dark_disabled</item>
        <item name="thakerSuccess">@color/dark_success</item>
        <item name="thakerWarning">@color/dark_warning</item>
        <item name="thakerError">@color/dark_error</item>
        <item name="thakerPhysics">@color/dark_physics</item>
        <item name="thakerBiology">@color/dark_biology</item>
    </style>

    <style name="AppTheme.Dark" parent="AppTheme">
        <item name="android:windowLightStatusBar">false</item>
    </style>

    <style name="AppTheme.Light" parent="AppTheme">
        <item name="android:windowBackground">@drawable/splash_background</item>
        <item name="android:colorPrimary">@color/light_primary</item>
        <item name="android:colorPrimaryDark">@color/light_primary_dark</item>
        <item name="android:colorAccent">@color/light_primary</item>
        <item name="android:textColorPrimary">@color/light_text_primary</item>
        <item name="android:textColorSecondary">@color/light_text_secondary</item>
        <item name="android:windowLightStatusBar">true</item>
        <item name="thakerBackground">@color/light_background</item>
        <item name="thakerSurface">@color/light_surface</item>
        <item name="thakerSurfaceElevated">@color/light_surface_elevated</item>
        <item name="thakerSurfaceSoft">@color/light_surface_soft</item>
        <item name="thakerTextPrimary">@color/light_text_primary</item>
        <item name="thakerTextSecondary">@color/light_text_secondary</item>
        <item name="thakerBorder">@color/light_border</item>
        <item name="thakerPrimary">@color/light_primary</item>
        <item name="thakerPrimaryDark">@color/light_primary_dark</item>
        <item name="thakerPrimaryLight">@color/light_primary_light</item>
        <item name="thakerDisabled">@color/light_disabled</item>
        <item name="thakerSuccess">@color/light_success</item>
        <item name="thakerWarning">@color/light_warning</item>
        <item name="thakerError">@color/light_error</item>
        <item name="thakerPhysics">@color/light_physics</item>
        <item name="thakerBiology">@color/light_biology</item>
    </style>
</resources>""")

    # 4. Drawables
    drawables = {
        "bg_top_wave.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="#2000B050" android:endColor="#00F5FAF7" android:angle="270" />
</shape>""",
        "header_squircle_btn.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurface" />
    <corners android:radius="14dp" />
    <stroke android:width="1dp" android:color="?attr/thakerBorder" />
</shape>""",
        "hero_card_banner.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurface" />
    <corners android:radius="26dp" />
    <stroke android:width="1.2dp" android:color="?attr/thakerBorder" />
</shape>""",
        "chip_chem_pill.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerPrimaryLight" />
    <corners android:radius="999dp" />
</shape>""",
        "chip_feature_pill.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#EDFBF4" />
    <corners android:radius="999dp" />
</shape>""",
        "stage_tab_bar_bg.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#EEF8F3" />
    <corners android:radius="999dp" />
    <stroke android:width="1dp" android:color="?attr/thakerBorder" />
</shape>""",
        "featured_book_card.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurface" />
    <corners android:radius="24dp" />
    <stroke android:width="1.2dp" android:color="?attr/thakerBorder" />
</shape>""",
        "switch_container_bg.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#EDF8F3" />
    <corners android:radius="14dp" />
</shape>""",
        "squircle_physics.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#E0F2FE" />
    <corners android:radius="16dp" />
</shape>""",
        "squircle_biology.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#F3E8FF" />
    <corners android:radius="16dp" />
</shape>""",
        "squircle_science.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#CCFBF1" />
    <corners android:radius="16dp" />
</shape>""",
        "squircle_math.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#EDE9FE" />
    <corners android:radius="16dp" />
</shape>""",
        "bottom_nav_dock.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurface" />
    <corners android:radius="28dp" />
    <stroke android:width="1dp" android:color="?attr/thakerBorder" />
</shape>""",
        "nav_fab_home.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">
    <gradient android:startColor="#00C853" android:endColor="#008C4A" android:angle="45" />
</shape>""",
        "nav_fab_glow.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">
    <solid android:color="#2600B050" />
</shape>""",
        "notification_badge_green.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">
    <solid android:color="#00A859" />
</shape>""",
        "ic_atom.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="28dp" android:height="28dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="#0284C7" android:pathData="M12,12m-2,0a2,2 0,1 1,4 0a2,2 0,1 1,-4 0"/>
    <path android:strokeColor="#0284C7" android:strokeWidth="1.4" android:pathData="M12,4.5C6.75,4.5 2.5,7.86 2.5,12C2.5,16.14 6.75,19.5 12,19.5C17.25,19.5 21.5,16.14 21.5,12C21.5,7.86 17.25,4.5 12,4.5Z" />
    <path android:strokeColor="#0284C7" android:strokeWidth="1.4" android:pathData="M5.5,7.7C2.88,12.24 3.73,17.48 7.39,19.6C11.06,21.72 16.18,19.92 18.8,15.38C21.42,10.84 20.57,5.6 16.91,3.48C13.24,1.36 8.12,3.16 5.5,7.7Z" />
    <path android:strokeColor="#0284C7" android:strokeWidth="1.4" android:pathData="M18.8,7.7C16.18,3.16 11.06,1.36 7.39,3.48C3.73,5.6 2.88,10.84 5.5,15.38C8.12,19.92 13.24,21.72 16.91,19.6C20.57,17.48 21.42,12.24 18.8,7.7Z" />
</vector>""",
        "ic_dna.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="28dp" android:height="28dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="#9333EA" android:pathData="M7.7,2.5c0.4,-0.4 1,-0.4 1.4,0l0.7,0.7c2.3,2.3 3.6,5.3 3.6,8.5s-1.3,6.2 -3.6,8.5l-0.7,0.7c-0.4,0.4 -1,0.4 -1.4,0c-0.4,-0.4 -0.4,-1 0,-1.4l0.7,-0.7C10.1,17 11.2,14.4 11.2,11.7S10.1,6.4 8.4,4.6L7.7,3.9C7.3,3.5 7.3,2.9 7.7,2.5z"/>
    <path android:fillColor="#9333EA" android:pathData="M16.3,2.5c-0.4,-0.4 -1,-0.4 -1.4,0l-0.7,0.7c-2.3,2.3 -3.6,5.3 -3.6,8.5s1.3,6.2 3.6,8.5l0.7,0.7c0.4,0.4 1,0.4 1.4,0c0.4,-0.4 0.4,-1 0,-1.4l-0.7,-0.7C13.9,17 12.8,14.4 12.8,11.7s1.1,-5.3 2.8,-7.1l0.7,-0.7C16.7,2.9 16.7,2.5 16.3,2.5z"/>
    <path android:strokeColor="#9333EA" android:strokeWidth="1.5" android:pathData="M8.5,5.5h7M6.5,9.5h11M6.5,14.5h11M8.5,18.5h7"/>
</vector>""",
        "ic_chevron_left.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:strokeColor="#94A3B8" android:strokeWidth="2.2" android:strokeLineCap="round" android:strokeLineJoin="round" android:pathData="M15,18l-6,-6l6,-6" />
</vector>""",
        "ic_layers.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="22dp" android:height="22dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:strokeColor="#FFFFFF" android:strokeWidth="2" android:strokeLineCap="round" android:strokeLineJoin="round" android:pathData="M12,2L2,7l10,5l10,-5zM2,12l10,5l10,-5M2,17l10,5l10,-5" />
</vector>""",
        "ic_ribbon.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="36dp" android:viewportWidth="24" android:viewportHeight="36">
    <path android:fillColor="#00A859" android:pathData="M0,0h24v36l-12,-8l-12,8z" />
</vector>""",
        "ic_download_box.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:strokeColor="?attr/thakerTextSecondary" android:strokeWidth="1.8" android:strokeLineCap="round" android:strokeLineJoin="round" android:pathData="M4,17v2a2,2 0,0 0,2 2h12a2,2 0,0 0,2 -2v-2M7,11l5,5l5,-5M12,4v12" />
</vector>""",
        "ic_bookmark.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:strokeColor="?attr/thakerTextSecondary" android:strokeWidth="1.8" android:strokeLineCap="round" android:strokeLineJoin="round" android:pathData="M19,21l-7,-5l-7,5V5a2,2 0,0 1,2 -2h10a2,2 0,0 1,2 2z" />
</vector>""",
        "ic_settings_gear.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:strokeColor="?attr/thakerTextSecondary" android:strokeWidth="1.8" android:strokeLineCap="round" android:strokeLineJoin="round" android:pathData="M12,15a3,3 0,1 0,0 -6a3,3 0,0 0,0 6zM19.4,15a1.65,1.65 0,0 0,0.33 1.82l0.06,0.06a2,2 0,0 1,-2.83 2.83l-0.06,-0.06a1.65,1.65 0,0 0,-1.82,-0.33 1.65,1.65 0,0 0,-1 1.51V21a2,2 0,0 1,-4 0v-0.09A1.65,1.65 0,0 0,9 19.4a1.65,1.65 0,0 0,-1.82,0.33l-0.06,0.06a2,2 0,0 1,-2.83,-2.83l0.06,-0.06a1.65,1.65 0,0 0,0.33,-1.82 1.65,1.65 0,0 0,-1.51,-1H3a2,2 0,0 1,0,-4h0.09A1.65,1.65 0,0 0,4.6 9a1.65,1.65 0,0 0,-0.33,-1.82l-0.06,-0.06a2,2 0,0 1,2.83,-2.83l0.06,0.06a1.65,1.65 0,0 0,1.82,0.33H9a1.65,1.65 0,0 0,1,-1.51V3a2,2 0,0 1,4 0v0.09a1.65,1.65 0,0 0,1,1.51 1.65,1.65 0,0 0,1.82,-0.33l0.06,-0.06a2,2 0,0 1,2.83,2.83l-0.06,0.06a1.65,1.65 0,0 0,-0.33,1.82V9a1.65,1.65 0,0 0,1.51,1H21a2,2 0,0 1,0,4h-0.09a1.65,1.65 0,0 0,-1.51,1z" />
</vector>""",
        "ic_graduation_cap.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:strokeColor="?attr/thakerTextSecondary" android:strokeWidth="1.8" android:strokeLineCap="round" android:strokeLineJoin="round" android:pathData="M22,10v6M2,10l10,-5l10,5l-10,5zM6,12v5c0,2.2 2.7,4 6,4s6,-1.8 6,-4v-5" />
</vector>""",
        "ic_home_white.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="26dp" android:height="26dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="#FFFFFF" android:pathData="M10,20v-6h4v6h5v-8h3L12,3 2,12h3v8z" />
</vector>""",
        "ic_book_green.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:strokeColor="#00A859" android:strokeWidth="2" android:strokeLineCap="round" android:strokeLineJoin="round" android:pathData="M2,3h6a4,4 0,0 1,4 4v14a3,3 0,0 0,-3 -3H2zM22,3h-6a4,4 0,0 0,-4 4v14a3,3 0,0 1,3 -3h7z" />
</vector>""",
        "ic_app_logo_mortarboard.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="36dp" android:height="36dp" android:viewportWidth="36" android:viewportHeight="36">
    <path android:fillColor="#00A859" android:pathData="M18,3L2,11l16,8l16,-8z" />
    <path android:fillColor="#008C4A" android:pathData="M8,14.5v6c0,3 4.5,5.5 10,5.5s10,-2.5 10,-5.5v-6l-10,4.5z" />
    <path android:strokeColor="#F59E0B" android:strokeWidth="2" android:strokeLineCap="round" android:pathData="M32,13v10l2,2" />
    <path android:strokeColor="#1E293B" android:strokeWidth="2.2" android:strokeLineCap="round" android:pathData="M5,31c4.5,-2.5 8.5,-2.5 13,0c4.5,-2.5 8.5,-2.5 13,0M18,22v9" />
</vector>""",
        "card_bg.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="@color/card_dark" />
    <corners android:radius="14dp" />
    <stroke android:width="1dp" android:color="@color/card_border" />
</shape>""",
        "hero_card_bg.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="#162238" android:endColor="#0F172A" android:angle="135" />
    <corners android:radius="16dp" />
    <stroke android:width="1.5dp" android:color="@color/cyan_accent" />
</shape>""",
        "subject_card_sci.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="#13273D" android:endColor="#0F1F33" android:angle="135" />
    <corners android:radius="16dp" />
    <stroke android:width="1.2dp" android:color="#C9A15C" />
</shape>""",
        "subject_card_math.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="#2A1B3D" android:endColor="#1C142A" android:angle="135" />
    <corners android:radius="16dp" />
    <stroke android:width="1.2dp" android:color="#A855F7" />
</shape>""",
        "btn_primary.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="@color/btn_start" android:endColor="@color/btn_end" android:angle="45" />
    <corners android:radius="10dp" />
</shape>""",
        "btn_secondary.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#1E293B" />
    <corners android:radius="10dp" />
    <stroke android:width="1dp" android:color="#475569" />
</shape>""",
        "btn_action_pill.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?android:attr/colorBackground" />
    <corners android:radius="16dp" />
    <stroke android:width="1dp" android:color="@color/cyan_accent" />
</shape>""",
        "tab_active.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="?attr/thakerPrimary" android:endColor="?attr/thakerPrimaryDark" android:angle="45" />
    <corners android:radius="999dp" />
</shape>""",
        "tab_inactive.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurfaceSoft" />
    <corners android:radius="999dp" />
    <stroke android:width="1dp" android:color="?attr/thakerBorder" />
</shape>""",
        "badge_active.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#1A282F" />
    <corners android:radius="2dp" />
    <stroke android:width="1dp" android:color="@color/green_accent" />
</shape>""",
        "badge_soon.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#1A282F" />
    <corners android:radius="2dp" />
    <stroke android:width="1dp" android:color="@color/rule" />
</shape>""",
        "bar_bg.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#E00B132B" />
    <stroke android:width="1dp" android:color="#2A3B5C" />
</shape>""",
        "floating_back_bg.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#D00B132B" />
    <corners android:radius="20dp" />
    <stroke android:width="1dp" android:color="@color/cyan_accent" />
</shape>""",
        "floating_back_transparent.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#20000000" />
    <corners android:radius="20dp" />
</shape>""",
        "quiz_option_normal.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#1A282F" />
    <corners android:radius="12dp" />
    <stroke android:width="1.2dp" android:color="#33434A" />
</shape>""",
        "quiz_option_correct.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#166534" />
    <corners android:radius="12dp" />
    <stroke android:width="1.5dp" android:color="#22C55E" />
</shape>""",
        "quiz_option_wrong.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#991B1B" />
    <corners android:radius="12dp" />
    <stroke android:width="1.5dp" android:color="#EF4444" />
</shape>""",
        "appbar_bg.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="#08182E" android:endColor="#0D3040" android:angle="90" />
</shape>""",
        "about_btn_bg.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#12263C" />
    <corners android:radius="20dp" />
    <stroke android:width="1dp" android:color="#2A6B7A" />
</shape>""",
        "tab_host_bg.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#0E1B2E" />
    <corners android:radius="26dp" />
    <stroke android:width="1dp" android:color="#243B57" />
</shape>""",
        "chip_gold_bg.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#2E2412" />
    <corners android:radius="14dp" />
    <stroke android:width="1dp" android:color="#8A641C" />
</shape>""",
        "chip_soft_bg.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#16334A" />
    <corners android:radius="12dp" />
    <stroke android:width="1dp" android:color="#2C6377" />
</shape>""",
        "card_modern.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="#14243A" android:endColor="#0F1B2E" android:angle="135" />
    <corners android:radius="20dp" />
    <stroke android:width="1dp" android:color="#27405F" />
</shape>""",
        "hero_modern.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="#0D3B4A" android:endColor="#122044" android:angle="135" />
    <corners android:radius="22dp" />
    <stroke android:width="1.5dp" android:color="#1E7C86" />
</shape>""",
        "card_science_modern.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="#0D3040" android:endColor="#102239" android:angle="135" />
    <corners android:radius="20dp" />
    <stroke android:width="1dp" android:color="#1E7C8A" />
</shape>""",
        "card_math_modern.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="#2A1E44" android:endColor="#17152E" android:angle="135" />
    <corners android:radius="20dp" />
    <stroke android:width="1dp" android:color="#7C5CC4" />
</shape>""",
        "btn_primary_modern.xml": """<ripple xmlns:android="http://schemas.android.com/apk/res/android" android:color="#55FFFFFF">
    <item>
        <shape android:shape="rectangle">
            <gradient android:startColor="#0EA5A4" android:endColor="#2563EB" android:angle="45" />
            <corners android:radius="14dp" />
        </shape>
    </item>
</ripple>""",
        "btn_secondary_modern.xml": """<ripple xmlns:android="http://schemas.android.com/apk/res/android" android:color="#33FFFFFF">
    <item>
        <shape android:shape="rectangle">
            <solid android:color="#1B2A42" />
            <corners android:radius="14dp" />
            <stroke android:width="1dp" android:color="#35506F" />
        </shape>
    </item>
</ripple>""",
        "btn_science_modern.xml": """<ripple xmlns:android="http://schemas.android.com/apk/res/android" android:color="#55FFFFFF">
    <item>
        <shape android:shape="rectangle">
            <gradient android:startColor="#0F766E" android:endColor="#0891B2" android:angle="45" />
            <corners android:radius="14dp" />
        </shape>
    </item>
</ripple>""",
        "btn_math_modern.xml": """<ripple xmlns:android="http://schemas.android.com/apk/res/android" android:color="#55FFFFFF">
    <item>
        <shape android:shape="rectangle">
            <gradient android:startColor="#6D28D9" android:endColor="#9333EA" android:angle="45" />
            <corners android:radius="14dp" />
        </shape>
    </item>
</ripple>""",
        "badge_circle_sci.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">
    <solid android:color="#0E7490" />
</shape>""",
        "badge_circle_math.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">
    <solid android:color="#7C3AED" />
</shape>""",
        "paper_panel.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="@color/paper" />
    <corners android:radius="3dp" />
</shape>""",
        "btn_ink.xml": """<ripple xmlns:android="http://schemas.android.com/apk/res/android" android:color="#33D7B26B">
    <item>
        <shape android:shape="rectangle">
            <solid android:color="#16232A" />
            <corners android:radius="4dp" />
            <stroke android:width="1dp" android:color="@color/gold_accent" />
        </shape>
    </item>
</ripple>""",
        "btn_outline.xml": """<ripple xmlns:android="http://schemas.android.com/apk/res/android" android:color="#22F2EAD9">
    <item>
        <shape android:shape="rectangle">
            <solid android:color="#16232A" />
            <corners android:radius="3dp" />
            <stroke android:width="1dp" android:color="@color/card_border" />
        </shape>
    </item>
</ripple>""",
        "row_action.xml": """<ripple xmlns:android="http://schemas.android.com/apk/res/android" android:color="#22F2EAD9">
    <item>
        <layer-list>
            <item>
                <shape android:shape="rectangle">
                    <solid android:color="@color/card_dark" />
                    <stroke android:width="1dp" android:color="@color/card_border" />
                    <corners android:radius="2dp" />
                </shape>
            </item>
            <item android:gravity="start|center_vertical" android:top="10dp" android:bottom="10dp">
                <shape android:shape="rectangle">
                    <solid android:color="@color/gold_accent" />
                    <size android:width="2dp" />
                </shape>
            </item>
        </layer-list>
    </item>
</ripple>""",
        "ic_launcher_background.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="#00C985" android:endColor="#007A5A" android:angle="90" />
</shape>""",
        "splash_background.xml": """<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="?attr/thakerBackground" />
    <item>
        <bitmap android:src="@drawable/ic_launcher_splash" android:gravity="center" android:tileMode="disabled" />
    </item>
</layer-list>""",
        "header_surface.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="?attr/thakerPrimary" android:endColor="?attr/thakerPrimaryDark" android:angle="90" />
    <corners android:bottomLeftRadius="28dp" android:bottomRightRadius="28dp" />
</shape>""",
        "surface_card.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurface" />
    <corners android:radius="16dp" />
    <stroke android:width="1dp" android:color="?attr/thakerBorder" />
</shape>""",
        "surface_soft.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurfaceSoft" />
    <corners android:radius="10dp" />
</shape>""",
        "hero_card.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="?attr/thakerPrimaryLight" android:endColor="?attr/thakerSurface" android:angle="135" />
    <corners android:radius="22dp" />
    <stroke android:width="1dp" android:color="?attr/thakerBorder" />
</shape>""",
        "chip_primary.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerPrimaryLight" />
    <corners android:radius="999dp" />
    <stroke android:width="1dp" android:color="?attr/thakerPrimary" />
</shape>""",
        "chip_neutral.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurfaceSoft" />
    <corners android:radius="999dp" />
    <stroke android:width="1dp" android:color="?attr/thakerBorder" />
</shape>""",
        "btn_primary_emerald.xml": """<ripple xmlns:android="http://schemas.android.com/apk/res/android" android:color="#44FFFFFF">
    <item>
        <shape android:shape="rectangle">
            <gradient android:startColor="?attr/thakerPrimary" android:endColor="?attr/thakerPrimaryDark" android:angle="45" />
            <corners android:radius="14dp" />
        </shape>
    </item>
</ripple>""",
        "btn_secondary_emerald.xml": """<ripple xmlns:android="http://schemas.android.com/apk/res/android" android:color="#22FFFFFF">
    <item>
        <shape android:shape="rectangle">
            <solid android:color="?attr/thakerSurfaceSoft" />
            <corners android:radius="14dp" />
            <stroke android:width="1dp" android:color="?attr/thakerBorder" />
        </shape>
    </item>
</ripple>""",
        "bottom_nav_bg.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurfaceElevated" />
    <corners android:radius="22dp" />
    <stroke android:width="1dp" android:color="?attr/thakerBorder" />
</shape>""",
        "nav_active_bg.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="?attr/thakerPrimary" android:endColor="?attr/thakerPrimaryDark" android:angle="45" />
    <corners android:radius="999dp" />
</shape>""",
        "notification_badge.xml": """<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">
    <solid android:color="?attr/thakerError" />
</shape>""",
        "ic_bell.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="?attr/thakerTextPrimary" android:pathData="M12,3a6,6 0,0 0,-6 6v4l-2,3h16l-2,-3v-4a6,6 0,0 0,-6 -6zM10,19a2,2 0,0 0,4 0z" />
</vector>""",
        "ic_person.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="?attr/thakerTextPrimary" android:pathData="M12,12a4,4 0,1 0,0 -8a4,4 0,0 0,0 8zM4,20a8,8 0,0 1,16 0z" />
</vector>""",
        "ic_home.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="?attr/thakerTextPrimary" android:pathData="M12,3L2,11h3v9h6v-6h2v6h6v-9h3z" />
</vector>""",
        "ic_subjects.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="?attr/thakerTextPrimary" android:pathData="M3,3h8v8H3zM13,3h8v8h-8zM3,13h8v8H3zM13,13h8v8h-8z" />
</vector>""",
        "ic_library.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="?attr/thakerTextPrimary" android:pathData="M4,4h6v16H4zM11,4h6v16h-6zM18,6l3,1l-3,13l-2,-0.6z" />
</vector>""",
        "ic_star.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="?attr/thakerTextPrimary" android:pathData="M12,2l3.1,6.3l6.9,1l-5,4.9l1.2,6.8L12,17.8L5.8,21L7,14.2L2,9.3l6.9,-1z" />
</vector>""",
        "ic_settings.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="?attr/thakerTextPrimary" android:pathData="M12,8a4,4 0,1 0,0 8a4,4 0,0 0,0 -8zM20,12l2,1.5l-2,3.5l-2.4,-0.6l-1.2,2l1,2.2l-3,2l-1.7,-1.8l-2.3,0.6l-0.8,2.6h-4l-0.8,-2.6l-2.3,-0.6L2.4,20.6l-3,-2l1,-2.2l-1.2,-2L-3,13.7l2,-3.5L-3,8.7l2.4,-0.6l1.2,-2L-0.4,3.9l3,-2L4.3,3.7l2.3,-0.6L7.4,0.5h4l0.8,2.6l2.3,0.6l1.7,-1.8l3,2l-1,2.2l1.2,2z" />
</vector>""",
        "ic_play.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="#FFFFFF" android:pathData="M8,5v14l11,-7z" />
</vector>""",
        "ic_book.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="?attr/thakerPrimary" android:pathData="M12,5C9,3 5,3 2,4v15c3,-1 7,-1 10,1c3,-2 7,-2 10,-1V4c-3,-1 -7,-1 -10,1zM12,7v12" />
</vector>""",
        "ic_flask.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="?attr/thakerPrimary" android:pathData="M9,2h6v2h-2v6l6,10H5l6,-10V4H9zM8,17h8l-1.5,-2.5h-5z" />
</vector>""",
        "ic_arrow.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="?attr/thakerTextSecondary" android:pathData="M13,4l-1.4,1.4L17.2,11H4v2h13.2l-5.6,5.6L13,20l8,-8z" />
</vector>""",
        "ic_graduation.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="?attr/thakerPrimary" android:pathData="M12,3L1,8l11,5l9,-4.1V13h2V8zM5,11.5V15c0,2 3.1,3.5 7,3.5s7,-1.5 7,-3.5v-3.5l-7,3.2z" />
</vector>""",
        "ic_moon.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="?attr/thakerTextPrimary" android:pathData="M20,15.5A8.5,8.5 0,0 1,8.5 4A8.5,8.5 0,1 0,20 15.5z" />
</vector>""",
        "ic_sun.xml": """<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="?attr/thakerTextPrimary" android:pathData="M12,7a5,5 0,1 0,0 10a5,5 0,0 0,0 -10zM12,1v3M12,20v3M1,12h3M20,12h3M4.2,4.2l2.1,2.1M17.7,17.7l2.1,2.1M19.8,4.2l-2.1,2.1M6.3,17.7l-2.1,2.1" />
</vector>""",
    }
    for name, content in drawables.items():
        with open(f"{res_dir}/drawable/{name}", "w", encoding="utf-8") as f:
            f.write(content)

    # 5. Layouts
    # A. activity_main.xml
    with open(f"{res_dir}/layout/activity_main.xml", "w", encoding="utf-8") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:layoutDirection="rtl"
    android:background="?attr/thakerBackground">

    <!-- Top soft gradient wave -->
    <View
        android:layout_width="match_parent"
        android:layout_height="220dp"
        android:background="@drawable/bg_top_wave" />

    <!-- Main Container -->
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical">

        <!-- Header Bar -->
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal"
            android:gravity="center_vertical"
            android:paddingStart="20dp"
            android:paddingEnd="20dp"
            android:paddingTop="20dp"
            android:paddingBottom="10dp">

            <!-- Profile Button -->
            <ImageButton
                android:id="@+id/btn_profile"
                android:layout_width="46dp"
                android:layout_height="46dp"
                android:background="@drawable/header_squircle_btn"
                android:src="@drawable/ic_person"
                android:tint="?attr/thakerPrimary"
                android:contentDescription="الملف الشخصي"
                android:scaleType="centerInside" />

            <!-- Center Logo & Title -->
            <LinearLayout
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:orientation="vertical"
                android:gravity="center_horizontal">

                <LinearLayout
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:orientation="horizontal"
                    android:gravity="center_vertical">

                    <ImageView
                        android:layout_width="32dp"
                        android:layout_height="32dp"
                        android:src="@drawable/ic_app_logo_mortarboard"
                        android:contentDescription="" />

                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:layout_marginStart="8dp"
                        android:text="@string/app_name"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textSize="24sp"
                        android:textStyle="bold" />
                </LinearLayout>

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="2dp"
                    android:text="@string/app_tagline_new"
                    android:textColor="?attr/thakerTextSecondary"
                    android:textSize="11sp" />

                <!-- Hidden grade label for controller binding -->
                <TextView
                    android:id="@+id/tv_grade_label"
                    android:layout_width="0dp"
                    android:layout_height="0dp"
                    android:visibility="gone" />
            </LinearLayout>

            <!-- Notifications Button with green dot -->
            <FrameLayout
                android:layout_width="46dp"
                android:layout_height="46dp">

                <ImageButton
                    android:id="@+id/btn_notifications"
                    android:layout_width="match_parent"
                    android:layout_height="match_parent"
                    android:background="@drawable/header_squircle_btn"
                    android:src="@drawable/ic_bell"
                    android:tint="?attr/thakerTextPrimary"
                    android:contentDescription="الإشعارات"
                    android:scaleType="centerInside" />

                <View
                    android:layout_width="10dp"
                    android:layout_height="10dp"
                    android:layout_gravity="top|end"
                    android:layout_marginTop="8dp"
                    android:layout_marginEnd="8dp"
                    android:background="@drawable/notification_badge_green" />
            </FrameLayout>

            <ImageButton
                android:id="@+id/btn_theme"
                android:layout_width="0dp"
                android:layout_height="0dp"
                android:visibility="gone" />
        </LinearLayout>

        <!-- Scrollable Body -->
        <ScrollView
            android:layout_width="match_parent"
            android:layout_height="0dp"
            android:layout_weight="1"
            android:fillViewport="true"
            android:clipToPadding="false"
            android:paddingStart="18dp"
            android:paddingEnd="18dp"
            android:paddingTop="6dp"
            android:paddingBottom="100dp">

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:orientation="vertical">

                <!-- 1. Top Featured Hero Card (كتاب ومعمل الكيمياء) -->
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="horizontal"
                    android:background="@drawable/hero_card_banner"
                    android:paddingStart="16dp"
                    android:paddingEnd="16dp"
                    android:paddingTop="18dp"
                    android:paddingBottom="18dp"
                    android:gravity="center_vertical"
                    android:elevation="3dp">

                    <ImageView
                        android:layout_width="114dp"
                        android:layout_height="114dp"
                        android:src="@drawable/illustration_hero_lab"
                        android:scaleType="fitCenter"
                        android:contentDescription="" />

                    <View
                        android:layout_width="12dp"
                        android:layout_height="match_parent" />

                    <LinearLayout
                        android:layout_width="0dp"
                        android:layout_height="wrap_content"
                        android:layout_weight="1"
                        android:orientation="vertical">

                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:background="@drawable/chip_chem_pill"
                            android:text="⚗️ الكيمياء"
                            android:textColor="?attr/thakerPrimary"
                            android:textSize="11sp"
                            android:textStyle="bold"
                            android:paddingStart="12dp"
                            android:paddingEnd="12dp"
                            android:paddingTop="4dp"
                            android:paddingBottom="4dp" />

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="8dp"
                            android:text="@string/chem_card_title"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="19sp"
                            android:textStyle="bold" />

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="2dp"
                            android:text="@string/chem_card_subtitle"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="12sp" />

                        <LinearLayout
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="10dp"
                            android:orientation="horizontal">

                            <TextView
                                android:layout_width="wrap_content"
                                android:layout_height="wrap_content"
                                android:background="@drawable/chip_feature_pill"
                                android:text="✓ شرح تفاعلي"
                                android:textColor="#059669"
                                android:textSize="9sp"
                                android:textStyle="bold"
                                android:paddingStart="7dp"
                                android:paddingEnd="7dp"
                                android:paddingTop="3dp"
                                android:paddingBottom="3dp" />

                            <View
                                android:layout_width="4dp"
                                android:layout_height="match_parent" />

                            <TextView
                                android:layout_width="wrap_content"
                                android:layout_height="wrap_content"
                                android:background="@drawable/chip_feature_pill"
                                android:text="✓ تجارب افتراضية"
                                android:textColor="#059669"
                                android:textSize="9sp"
                                android:textStyle="bold"
                                android:paddingStart="7dp"
                                android:paddingEnd="7dp"
                                android:paddingTop="3dp"
                                android:paddingBottom="3dp" />

                            <View
                                android:layout_width="4dp"
                                android:layout_height="match_parent" />

                            <TextView
                                android:layout_width="wrap_content"
                                android:layout_height="wrap_content"
                                android:background="@drawable/chip_feature_pill"
                                android:text="✓ بدون اتصال"
                                android:textColor="#059669"
                                android:textSize="9sp"
                                android:textStyle="bold"
                                android:paddingStart="7dp"
                                android:paddingEnd="7dp"
                                android:paddingTop="3dp"
                                android:paddingBottom="3dp" />
                        </LinearLayout>
                    </LinearLayout>
                </LinearLayout>

                <!-- 2. Segmented Stage Switcher (الثانوية / الإعدادية) -->
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="52dp"
                    android:layout_marginTop="18dp"
                    android:orientation="horizontal"
                    android:background="@drawable/stage_tab_bar_bg"
                    android:padding="4dp">

                    <Button
                        android:id="@+id/tab_high_school"
                        android:layout_width="0dp"
                        android:layout_height="match_parent"
                        android:layout_weight="1"
                        android:minHeight="0dp"
                        android:minWidth="0dp"
                        android:background="@drawable/tab_active"
                        android:text="@string/stage_high_school"
                        android:textColor="#FFFFFF"
                        android:textSize="14sp"
                        android:textStyle="bold"
                        android:drawableStart="@drawable/ic_layers"
                        android:drawablePadding="8dp"
                        android:paddingStart="16dp"
                        android:paddingEnd="16dp" />

                    <Button
                        android:id="@+id/tab_middle_school"
                        android:layout_width="0dp"
                        android:layout_height="match_parent"
                        android:layout_weight="1"
                        android:minHeight="0dp"
                        android:minWidth="0dp"
                        android:background="@drawable/tab_inactive"
                        android:text="@string/stage_middle_school"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textSize="14sp"
                        android:textStyle="bold"
                        android:drawableStart="@drawable/ic_graduation"
                        android:drawablePadding="8dp"
                        android:paddingStart="16dp"
                        android:paddingEnd="16dp" />
                </LinearLayout>

                <!-- 3. Section Header: الكتب الدراسية -->
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="22dp"
                    android:layout_marginBottom="12dp"
                    android:orientation="horizontal"
                    android:gravity="center_vertical">

                    <ImageView
                        android:layout_width="24dp"
                        android:layout_height="24dp"
                        android:src="@drawable/ic_book_green"
                        android:contentDescription="" />

                    <LinearLayout
                        android:layout_width="0dp"
                        android:layout_height="wrap_content"
                        android:layout_weight="1"
                        android:orientation="vertical"
                        android:paddingStart="10dp">

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:text="@string/section_books_title"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="18sp"
                            android:textStyle="bold" />

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="1dp"
                            android:text="@string/section_books_sub"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="12sp" />
                    </LinearLayout>
                </LinearLayout>

                <!-- High School Container -->
                <LinearLayout
                    android:id="@+id/container_high_school"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="vertical"
                    android:visibility="visible">

                    <!-- Featured Book & Lab Card -->
                    <FrameLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:background="@drawable/featured_book_card"
                        android:elevation="3dp">

                        <LinearLayout
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:orientation="vertical"
                            android:padding="16dp">

                            <LinearLayout
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:orientation="horizontal"
                                android:gravity="center_vertical">

                                <ImageView
                                    android:layout_width="128dp"
                                    android:layout_height="110dp"
                                    android:src="@drawable/illustration_featured_lab"
                                    android:scaleType="fitCenter"
                                    android:contentDescription="" />

                                <View
                                    android:layout_width="12dp"
                                    android:layout_height="match_parent" />

                                <LinearLayout
                                    android:layout_width="0dp"
                                    android:layout_height="wrap_content"
                                    android:layout_weight="1"
                                    android:orientation="vertical">

                                    <TextView
                                        android:layout_width="match_parent"
                                        android:layout_height="wrap_content"
                                        android:text="@string/chem_card_title"
                                        android:textColor="?attr/thakerTextPrimary"
                                        android:textSize="18sp"
                                        android:textStyle="bold" />

                                    <TextView
                                        android:layout_width="match_parent"
                                        android:layout_height="wrap_content"
                                        android:layout_marginTop="2dp"
                                        android:text="@string/chem_card_subtitle"
                                        android:textColor="?attr/thakerTextSecondary"
                                        android:textSize="11sp" />

                                    <Button
                                        android:id="@+id/btn_open_chem_lab"
                                        android:layout_width="match_parent"
                                        android:layout_height="46dp"
                                        android:layout_marginTop="12dp"
                                        android:minHeight="0dp"
                                        android:minWidth="0dp"
                                        android:background="@drawable/btn_primary_emerald"
                                        android:text="فتح المعمل  ▶"
                                        android:textColor="#FFFFFF"
                                        android:textSize="14sp"
                                        android:textStyle="bold"
                                        android:paddingStart="16dp"
                                        android:paddingEnd="16dp" />
                                </LinearLayout>
                            </LinearLayout>

                            <LinearLayout
                                android:layout_width="match_parent"
                                android:layout_height="44dp"
                                android:layout_marginTop="12dp"
                                android:orientation="horizontal"
                                android:background="@drawable/switch_container_bg"
                                android:gravity="center_vertical"
                                android:paddingStart="14dp"
                                android:paddingEnd="10dp">

                                <TextView
                                    android:layout_width="0dp"
                                    android:layout_height="wrap_content"
                                    android:layout_weight="1"
                                    android:text="@string/auto_launch_pref"
                                    android:textColor="?attr/thakerTextPrimary"
                                    android:textSize="12sp"
                                    android:textStyle="bold" />

                                <Switch
                                    android:id="@+id/cb_auto_launch"
                                    android:layout_width="wrap_content"
                                    android:layout_height="wrap_content"
                                    android:thumbTint="?attr/thakerPrimary"
                                    android:trackTint="#A7F3D0" />
                            </LinearLayout>
                        </LinearLayout>

                        <ImageView
                            android:layout_width="22dp"
                            android:layout_height="32dp"
                            android:layout_gravity="top|start"
                            android:layout_marginStart="24dp"
                            android:src="@drawable/ic_ribbon"
                            android:contentDescription="" />
                    </FrameLayout>

                    <!-- Physics Card -->
                    <LinearLayout
                        android:id="@+id/card_physics"
                        android:layout_width="match_parent"
                        android:layout_height="72dp"
                        android:layout_marginTop="14dp"
                        android:orientation="horizontal"
                        android:background="@drawable/surface_card"
                        android:gravity="center_vertical"
                        android:paddingStart="16dp"
                        android:paddingEnd="16dp"
                        android:elevation="2dp">

                        <ImageView
                            android:layout_width="18dp"
                            android:layout_height="18dp"
                            android:src="@drawable/ic_chevron_left"
                            android:contentDescription="" />

                        <LinearLayout
                            android:layout_width="0dp"
                            android:layout_height="wrap_content"
                            android:layout_weight="1"
                            android:orientation="vertical"
                            android:paddingStart="14dp">

                            <TextView
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:text="@string/subject_physics"
                                android:textColor="?attr/thakerTextPrimary"
                                android:textSize="16sp"
                                android:textStyle="bold" />

                            <TextView
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:layout_marginTop="2dp"
                                android:text="بصريات"
                                android:textColor="?attr/thakerTextSecondary"
                                android:textSize="12sp" />
                        </LinearLayout>

                        <FrameLayout
                            android:layout_width="48dp"
                            android:layout_height="48dp"
                            android:background="@drawable/squircle_physics">

                            <ImageView
                                android:layout_width="28dp"
                                android:layout_height="28dp"
                                android:layout_gravity="center"
                                android:src="@drawable/ic_atom"
                                android:contentDescription="" />
                        </FrameLayout>
                    </LinearLayout>

                    <!-- Biology Card -->
                    <LinearLayout
                        android:id="@+id/card_biology"
                        android:layout_width="match_parent"
                        android:layout_height="72dp"
                        android:layout_marginTop="12dp"
                        android:orientation="horizontal"
                        android:background="@drawable/surface_card"
                        android:gravity="center_vertical"
                        android:paddingStart="16dp"
                        android:paddingEnd="16dp"
                        android:elevation="2dp">

                        <ImageView
                            android:layout_width="18dp"
                            android:layout_height="18dp"
                            android:src="@drawable/ic_chevron_left"
                            android:contentDescription="" />

                        <LinearLayout
                            android:layout_width="0dp"
                            android:layout_height="wrap_content"
                            android:layout_weight="1"
                            android:orientation="vertical"
                            android:paddingStart="14dp">

                            <TextView
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:text="@string/subject_biology"
                                android:textColor="?attr/thakerTextPrimary"
                                android:textSize="16sp"
                                android:textStyle="bold" />

                            <TextView
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:layout_marginTop="2dp"
                                android:text="مجسمات"
                                android:textColor="?attr/thakerTextSecondary"
                                android:textSize="12sp" />
                        </LinearLayout>

                        <FrameLayout
                            android:layout_width="48dp"
                            android:layout_height="48dp"
                            android:background="@drawable/squircle_biology">

                            <ImageView
                                android:layout_width="28dp"
                                android:layout_height="28dp"
                                android:layout_gravity="center"
                                android:src="@drawable/ic_dna"
                                android:contentDescription="" />
                        </FrameLayout>
                    </LinearLayout>
                </LinearLayout>

                <!-- Middle School Container -->
                <LinearLayout
                    android:id="@+id/container_middle_school"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="vertical"
                    android:visibility="gone">

                    <!-- 9th Grade Hero Banner -->
                    <LinearLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:orientation="horizontal"
                        android:background="@drawable/hero_card_banner"
                        android:padding="16dp"
                        android:gravity="center_vertical"
                        android:elevation="3dp">

                        <ImageView
                            android:layout_width="96dp"
                            android:layout_height="96dp"
                            android:src="@drawable/illustration_science"
                            android:contentDescription="" />

                        <View
                            android:layout_width="12dp"
                            android:layout_height="match_parent" />

                        <LinearLayout
                            android:layout_width="0dp"
                            android:layout_height="wrap_content"
                            android:layout_weight="1"
                            android:orientation="vertical">

                            <TextView
                                android:layout_width="wrap_content"
                                android:layout_height="wrap_content"
                                android:background="@drawable/chip_chem_pill"
                                android:text="🔬 العلوم والرياضيات · تاسع"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="10sp"
                                android:textStyle="bold"
                                android:paddingStart="10dp"
                                android:paddingEnd="10dp"
                                android:paddingTop="3dp"
                                android:paddingBottom="3dp" />

                            <TextView
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:layout_marginTop="6dp"
                                android:text="منهج الصف التاسع التفاعلي"
                                android:textColor="?attr/thakerTextPrimary"
                                android:textSize="17sp"
                                android:textStyle="bold" />

                            <TextView
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:layout_marginTop="2dp"
                                android:text="كتب 3D ومعامل وتجارب واختبارات وزارية"
                                android:textColor="?attr/thakerTextSecondary"
                                android:textSize="11sp" />
                        </LinearLayout>
                    </LinearLayout>

                    <!-- Next-Gen Intelligent Interactive Textbook Engine Card -->
                    <LinearLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:orientation="horizontal"
                        android:background="@drawable/hero_card_banner"
                        android:padding="14dp"
                        android:layout_marginTop="12dp"
                        android:gravity="center_vertical"
                        android:elevation="3dp">

                        <ImageView
                            android:layout_width="60dp"
                            android:layout_height="60dp"
                            android:src="@drawable/illustration_science"
                            android:contentDescription="" />

                        <LinearLayout
                            android:layout_width="0dp"
                            android:layout_height="wrap_content"
                            android:layout_weight="1"
                            android:orientation="vertical"
                            android:paddingStart="12dp">

                            <TextView
                                android:layout_width="wrap_content"
                                android:layout_height="wrap_content"
                                android:background="@drawable/chip_chem_pill"
                                android:text="✨ الجيل الجديد · محرك تفاعلي ذكي"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="10sp"
                                android:textStyle="bold"
                                android:paddingStart="8dp"
                                android:paddingEnd="8dp"
                                android:paddingTop="2dp"
                                android:paddingBottom="2dp" />

                            <TextView
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:layout_marginTop="4dp"
                                android:text="كتاب العلوم التفاعلي الذكي"
                                android:textColor="?attr/thakerTextPrimary"
                                android:textSize="15sp"
                                android:textStyle="bold" />

                            <TextView
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:layout_marginTop="2dp"
                                android:text="الكتاب الوزاري الأصلي + طبقة الذكاء ومعامل 3D"
                                android:textColor="?attr/thakerTextSecondary"
                                android:textSize="11sp" />

                            <Button
                                android:id="@+id/btn_open_sci9_interactive_engine"
                                android:layout_width="match_parent"
                                android:layout_height="42dp"
                                android:layout_marginTop="8dp"
                                android:background="@drawable/btn_primary_emerald"
                                android:text="افتح الكتاب التفاعلي الذكي  ▶"
                                android:textColor="#FFFFFF"
                                android:textSize="12sp"
                                android:textStyle="bold" />
                        </LinearLayout>
                    </LinearLayout>

                    <Button
                        android:id="@+id/btn_open_sci9_3d_book"
                        android:layout_width="match_parent"
                        android:layout_height="50dp"
                        android:layout_marginTop="12dp"
                        android:background="@drawable/btn_primary_emerald"
                        android:text="كتاب ومعمل العلوم 3D  ▶"
                        android:textColor="#FFFFFF"
                        android:textSize="13sp"
                        android:textStyle="bold" />

                    <Button
                        android:id="@+id/btn_open_math9_3d_book"
                        android:layout_width="match_parent"
                        android:layout_height="50dp"
                        android:layout_marginTop="8dp"
                        android:background="@drawable/btn_primary_emerald"
                        android:text="كتاب ومعمل الرياضيات 3D  ▶"
                        android:textColor="#FFFFFF"
                        android:textSize="13sp"
                        android:textStyle="bold" />

                    <Button
                        android:id="@+id/btn_open_sci9_lab"
                        android:layout_width="match_parent"
                        android:layout_height="48dp"
                        android:layout_marginTop="8dp"
                        android:background="@drawable/surface_card"
                        android:text="معمل العلوم التفاعلي (13 درس)  ⚗️"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textSize="13sp"
                        android:textStyle="bold" />

                    <Button
                        android:id="@+id/btn_exam_9th_all"
                        android:layout_width="match_parent"
                        android:layout_height="48dp"
                        android:layout_marginTop="8dp"
                        android:background="@drawable/surface_card"
                        android:text="الاختبار الوزاري الشامل  📝"
                        android:textColor="?attr/thakerPrimary"
                        android:textSize="13sp"
                        android:textStyle="bold" />

                    <!-- Middle School Subjects -->
                    <!-- Sci P1 -->
                    <LinearLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:layout_marginTop="14dp"
                        android:background="@drawable/surface_card"
                        android:padding="12dp"
                        android:orientation="vertical">

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:text="@string/sci_p1_title"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="15sp"
                            android:textStyle="bold" />
                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="2dp"
                            android:text="@string/sci_p1_sub"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="11sp" />

                        <LinearLayout
                            android:layout_width="match_parent"
                            android:layout_height="38dp"
                            android:layout_marginTop="10dp"
                            android:orientation="horizontal">

                            <Button
                                android:id="@+id/btn_read_sci_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الكتاب"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_index_sci_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الفهرس"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_summary_sci_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الملخص"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_quiz_sci_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="اختبار"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                        </LinearLayout>
                    </LinearLayout>

                    <!-- Sci P2 -->
                    <LinearLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:layout_marginTop="10dp"
                        android:background="@drawable/surface_card"
                        android:padding="12dp"
                        android:orientation="vertical">

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:text="@string/sci_p2_title"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="15sp"
                            android:textStyle="bold" />
                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="2dp"
                            android:text="@string/sci_p2_sub"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="11sp" />

                        <LinearLayout
                            android:layout_width="match_parent"
                            android:layout_height="38dp"
                            android:layout_marginTop="10dp"
                            android:orientation="horizontal">

                            <Button
                                android:id="@+id/btn_read_sci_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الكتاب"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_index_sci_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الفهرس"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_summary_sci_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الملخص"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_quiz_sci_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="اختبار"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                        </LinearLayout>
                    </LinearLayout>

                    <!-- Math P1 -->
                    <LinearLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:layout_marginTop="10dp"
                        android:background="@drawable/surface_card"
                        android:padding="12dp"
                        android:orientation="vertical">

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:text="@string/math_p1_title"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="15sp"
                            android:textStyle="bold" />
                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="2dp"
                            android:text="@string/math_p1_sub"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="11sp" />

                        <LinearLayout
                            android:layout_width="match_parent"
                            android:layout_height="38dp"
                            android:layout_marginTop="10dp"
                            android:orientation="horizontal">

                            <Button
                                android:id="@+id/btn_read_math_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الكتاب"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_index_math_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الفهرس"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_summary_math_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الملخص"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_quiz_math_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="اختبار"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                        </LinearLayout>
                    </LinearLayout>

                    <!-- Math P2 -->
                    <LinearLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:layout_marginTop="10dp"
                        android:background="@drawable/surface_card"
                        android:padding="12dp"
                        android:orientation="vertical">

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:text="@string/math_p2_title"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="15sp"
                            android:textStyle="bold" />
                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="2dp"
                            android:text="@string/math_p2_sub"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="11sp" />

                        <LinearLayout
                            android:layout_width="match_parent"
                            android:layout_height="38dp"
                            android:layout_marginTop="10dp"
                            android:orientation="horizontal">

                            <Button
                                android:id="@+id/btn_read_math_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الكتاب"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_index_math_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الفهرس"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_summary_math_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الملخص"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_quiz_math_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="اختبار"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                        </LinearLayout>
                    </LinearLayout>
                </LinearLayout>

                <!-- About App Button -->
                <Button
                    android:id="@+id/btn_about"
                    android:layout_width="wrap_content"
                    android:layout_height="34dp"
                    android:layout_gravity="center_horizontal"
                    android:layout_marginTop="20dp"
                    android:minHeight="0dp"
                    android:minWidth="0dp"
                    android:background="@drawable/chip_neutral"
                    android:text="@string/about_app"
                    android:textColor="?attr/thakerTextSecondary"
                    android:textSize="10sp"
                    android:paddingStart="14dp"
                    android:paddingEnd="14dp" />
            </LinearLayout>
        </ScrollView>
    </LinearLayout>

    <!-- Bottom Navigation Dock Bar (Matches Prototype Exactly) -->
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="72dp"
        android:layout_gravity="bottom"
        android:layout_marginStart="14dp"
        android:layout_marginEnd="14dp"
        android:layout_marginBottom="12dp"
        android:orientation="horizontal"
        android:background="@drawable/bottom_nav_dock"
        android:elevation="12dp"
        android:gravity="center_vertical"
        android:paddingStart="6dp"
        android:paddingEnd="6dp">

        <!-- 1. موادي -->
        <Button
            android:id="@+id/nav_subjects"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:minHeight="0dp"
            android:minWidth="0dp"
            android:background="@android:color/transparent"
            android:text="@string/nav_subjects"
            android:textColor="?attr/thakerTextSecondary"
            android:textSize="11sp"
            android:textStyle="bold"
            android:drawableTop="@drawable/ic_graduation_cap"
            android:drawablePadding="2dp"
            android:paddingTop="10dp"
            android:paddingBottom="4dp" />

        <!-- 2. المكتبة -->
        <Button
            android:id="@+id/nav_library"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:minHeight="0dp"
            android:minWidth="0dp"
            android:background="@android:color/transparent"
            android:text="@string/nav_library"
            android:textColor="?attr/thakerTextSecondary"
            android:textSize="11sp"
            android:textStyle="bold"
            android:drawableTop="@drawable/ic_download_box"
            android:drawablePadding="2dp"
            android:paddingTop="10dp"
            android:paddingBottom="4dp" />

        <!-- 3. الرئيسية (Elevated FAB Center) -->
        <FrameLayout
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1.2">

            <View
                android:layout_width="56dp"
                android:layout_height="56dp"
                android:layout_gravity="center_horizontal|top"
                android:layout_marginTop="2dp"
                android:background="@drawable/nav_fab_glow" />

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:orientation="vertical"
                android:gravity="center_horizontal">

                <Button
                    android:id="@+id/nav_home"
                    android:layout_width="48dp"
                    android:layout_height="48dp"
                    android:background="@drawable/nav_fab_home"
                    android:drawableTop="@drawable/ic_home_white"
                    android:gravity="center"
                    android:paddingTop="12dp"
                    android:elevation="4dp" />

                <TextView
                    android:id="@+id/tv_nav_home"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="1dp"
                    android:text="@string/nav_home"
                    android:textColor="?attr/thakerPrimary"
                    android:textSize="11sp"
                    android:textStyle="bold" />
            </LinearLayout>
        </FrameLayout>

        <!-- 4. المفضلة -->
        <Button
            android:id="@+id/nav_favorites"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:minHeight="0dp"
            android:minWidth="0dp"
            android:background="@android:color/transparent"
            android:text="@string/nav_favorites"
            android:textColor="?attr/thakerTextSecondary"
            android:textSize="11sp"
            android:textStyle="bold"
            android:drawableTop="@drawable/ic_bookmark"
            android:drawablePadding="2dp"
            android:paddingTop="10dp"
            android:paddingBottom="4dp" />

        <!-- 5. الإعدادات -->
        <Button
            android:id="@+id/nav_settings"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:minHeight="0dp"
            android:minWidth="0dp"
            android:background="@android:color/transparent"
            android:text="@string/nav_settings"
            android:textColor="?attr/thakerTextSecondary"
            android:textSize="11sp"
            android:textStyle="bold"
            android:drawableTop="@drawable/ic_settings_gear"
            android:drawablePadding="2dp"
            android:paddingTop="10dp"
            android:paddingBottom="4dp" />
    </LinearLayout>
</FrameLayout>""")

    # B. activity_book_viewer.xml
    with open(f"{res_dir}/layout/activity_book_viewer.xml", "w", encoding="utf-8") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#050C16">

    <!-- Zoomable PDF Page Display -->
    <ImageView
        android:id="@+id/pdf_image_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:scaleType="matrix"
        android:contentDescription="صفحة الكتاب" />

    <!-- Loading Spinner -->
    <ProgressBar
        android:id="@+id/pdf_progress"
        android:layout_width="48dp"
        android:layout_height="48dp"
        android:layout_gravity="center"
        android:visibility="gone" />

    <!-- Top Toolbar (Toggleable) -->
    <LinearLayout
        android:id="@+id/top_toolbar"
        android:layout_width="match_parent"
        android:layout_height="52dp"
        android:layout_gravity="top"
        android:orientation="horizontal"
        android:background="@drawable/bar_bg"
        android:gravity="center_vertical"
        android:paddingStart="12dp"
        android:paddingEnd="12dp">

        <Button
            android:id="@+id/btn_back_viewer"
            android:layout_width="38dp"
            android:layout_height="38dp"
            android:text="⬅"
            android:textColor="@color/text_primary"
            android:background="@drawable/badge_soon"
            android:textSize="16sp" />

        <LinearLayout
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:orientation="vertical"
            android:layout_marginStart="10dp"
            android:layout_marginEnd="8dp">

            <TextView
                android:id="@+id/tv_viewer_book_title"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="عنوان الكتاب"
                android:textColor="@color/text_primary"
                android:textSize="13sp"
                android:textStyle="bold"
                android:singleLine="true" />

            <TextView
                android:id="@+id/tv_viewer_unit_name"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="الوحدة الحالية"
                android:textColor="@color/cyan_accent"
                android:textSize="11sp"
                android:singleLine="true" />
        </LinearLayout>

        <Button
            android:id="@+id/btn_open_unit_index"
            android:layout_width="wrap_content"
            android:layout_height="34dp"
            android:text="📋 الفهرس"
            android:textColor="@color/cyan_accent"
            android:background="@drawable/badge_soon"
            android:textSize="11sp"
            android:paddingStart="10dp"
            android:paddingEnd="10dp"
            android:layout_marginEnd="6dp" />

        <Button
            android:id="@+id/btn_reset_zoom"
            android:layout_width="34dp"
            android:layout_height="34dp"
            android:text="🔍"
            android:textColor="@color/text_primary"
            android:background="@drawable/badge_soon"
            android:textSize="12sp" />
    </LinearLayout>

    <!-- Bottom Toolbar: Prev, Next, Page Indicator & Scrubber -->
    <LinearLayout
        android:id="@+id/bottom_toolbar"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_gravity="bottom"
        android:orientation="vertical"
        android:background="@drawable/bar_bg"
        android:paddingStart="12dp"
        android:paddingEnd="12dp"
        android:paddingTop="6dp"
        android:paddingBottom="10dp">

        <SeekBar
            android:id="@+id/page_seekbar"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginBottom="4dp" />

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal"
            android:gravity="center_vertical">

            <Button
                android:id="@+id/btn_prev_page"
                android:layout_width="wrap_content"
                android:layout_height="36dp"
                android:text="◀ السابق"
                android:textColor="@color/text_primary"
                android:background="@drawable/btn_secondary"
                android:textSize="12sp"
                android:paddingStart="14dp"
                android:paddingEnd="14dp" />

            <TextView
                android:id="@+id/tv_page_indicator"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:text="صفحة 1 من 100"
                android:textColor="@color/text_primary"
                android:textSize="13sp"
                android:textStyle="bold"
                android:gravity="center" />

            <Button
                android:id="@+id/btn_next_page"
                android:layout_width="wrap_content"
                android:layout_height="36dp"
                android:text="التالي ▶"
                android:textColor="@color/text_primary"
                android:background="@drawable/btn_secondary"
                android:textSize="12sp"
                android:paddingStart="14dp"
                android:paddingEnd="14dp" />
        </LinearLayout>
    </LinearLayout>
</FrameLayout>""")

    # C. activity_quiz.xml
    with open(f"{res_dir}/layout/activity_quiz.xml", "w", encoding="utf-8") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:fillViewport="true"
    android:background="@color/bg_dark">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:orientation="vertical"
        android:padding="16dp">

        <!-- Header -->
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal"
            android:gravity="center_vertical"
            android:layout_marginBottom="16dp">

            <Button
                android:id="@+id/btn_quiz_back"
                android:layout_width="38dp"
                android:layout_height="38dp"
                android:text="⬅"
                android:textColor="@color/text_primary"
                android:background="@drawable/badge_soon"
                android:textSize="16sp" />

            <LinearLayout
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:orientation="vertical"
                android:layout_marginStart="12dp">

                <TextView
                    android:id="@+id/tv_quiz_subject"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="اختبار وزاري مؤتمت"
                    android:textColor="@color/text_primary"
                    android:textSize="16sp"
                    android:textStyle="bold" />

                <TextView
                    android:id="@+id/tv_quiz_progress"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="السؤال 1 من 15"
                    android:textColor="@color/cyan_accent"
                    android:textSize="12sp" />
            </LinearLayout>

            <TextView
                android:id="@+id/tv_quiz_score_top"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="النقاط: 0"
                android:textColor="@color/gold_accent"
                android:background="@drawable/badge_soon"
                android:paddingStart="10dp"
                android:paddingEnd="10dp"
                android:paddingTop="4dp"
                android:paddingBottom="4dp"
                android:textSize="12sp"
                android:textStyle="bold" />
        </LinearLayout>

        <!-- Question Card -->
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:background="@drawable/hero_card_bg"
            android:padding="16dp"
            android:layout_marginBottom="16dp">

            <TextView
                android:id="@+id/tv_question_text"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:text="نص السؤال هنا..."
                android:textColor="#FFFFFF"
                android:textSize="16sp"
                android:textStyle="bold"
                android:lineSpacingExtra="4dp" />
        </LinearLayout>

        <!-- Options Container -->
        <LinearLayout
            android:id="@+id/options_container"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:layout_marginBottom="16dp">

            <Button
                android:id="@+id/btn_opt_0"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:minHeight="48dp"
                android:text="الخيار الأول"
                android:textColor="#FFFFFF"
                android:background="@drawable/quiz_option_normal"
                android:textSize="14sp"
                android:textStyle="bold"
                android:gravity="right|center_vertical"
                android:paddingStart="16dp"
                android:paddingEnd="16dp"
                android:layout_marginBottom="10dp" />

            <Button
                android:id="@+id/btn_opt_1"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:minHeight="48dp"
                android:text="الخيار الثاني"
                android:textColor="#FFFFFF"
                android:background="@drawable/quiz_option_normal"
                android:textSize="14sp"
                android:textStyle="bold"
                android:gravity="right|center_vertical"
                android:paddingStart="16dp"
                android:paddingEnd="16dp"
                android:layout_marginBottom="10dp" />

            <Button
                android:id="@+id/btn_opt_2"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:minHeight="48dp"
                android:text="الخيار الثالث"
                android:textColor="#FFFFFF"
                android:background="@drawable/quiz_option_normal"
                android:textSize="14sp"
                android:textStyle="bold"
                android:gravity="right|center_vertical"
                android:paddingStart="16dp"
                android:paddingEnd="16dp"
                android:layout_marginBottom="10dp" />

            <Button
                android:id="@+id/btn_opt_3"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:minHeight="48dp"
                android:text="الخيار الرابع"
                android:textColor="#FFFFFF"
                android:background="@drawable/quiz_option_normal"
                android:textSize="14sp"
                android:textStyle="bold"
                android:gravity="right|center_vertical"
                android:paddingStart="16dp"
                android:paddingEnd="16dp"
                android:layout_marginBottom="10dp" />
        </LinearLayout>

        <!-- Explanation Card -->
        <LinearLayout
            android:id="@+id/card_explanation"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:background="@drawable/card_bg"
            android:padding="14dp"
            android:visibility="gone"
            android:layout_marginBottom="16dp">

            <TextView
                android:id="@+id/tv_explain_header"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="إجابة صحيحة! ✅"
                android:textColor="@color/green_accent"
                android:textSize="14sp"
                android:textStyle="bold"
                android:layout_marginBottom="4dp" />

            <TextView
                android:id="@+id/tv_explain_body"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:text="الشرح والتعليل العلمي هنا..."
                android:textColor="#FFFFFF"
                android:textSize="13sp"
                android:lineSpacingExtra="3dp" />
        </LinearLayout>

        <!-- Next / Finish Button -->
        <Button
            android:id="@+id/btn_quiz_next"
            android:layout_width="match_parent"
            android:layout_height="48dp"
            android:text="السؤال التالي ⬅"
            android:textColor="@color/text_primary"
            android:background="@drawable/btn_primary"
            android:textSize="15sp"
            android:textStyle="bold"
            android:visibility="gone" />
    </LinearLayout>
</ScrollView>""")

    # D. activity_summary.xml
    with open(f"{res_dir}/layout/activity_summary.xml", "w", encoding="utf-8") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:background="@color/bg_dark">

    <!-- Top Bar -->
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="52dp"
        android:orientation="horizontal"
        android:background="@drawable/bar_bg"
        android:gravity="center_vertical"
        android:paddingStart="12dp"
        android:paddingEnd="12dp">

        <Button
            android:id="@+id/btn_summary_back"
            android:layout_width="38dp"
            android:layout_height="38dp"
            android:text="⬅"
            android:textColor="@color/text_primary"
            android:background="@drawable/badge_soon"
            android:textSize="16sp" />

        <TextView
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:text="💡 ملخصات وقوانين ونظريات الصف التاسع"
            android:textColor="@color/text_primary"
            android:textSize="14sp"
            android:textStyle="bold"
            android:layout_marginStart="10dp" />
    </LinearLayout>

    <!-- Subject Tabs -->
    <HorizontalScrollView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:padding="8dp"
        android:scrollbars="none">

        <LinearLayout
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:orientation="horizontal">

            <Button
                android:id="@+id/tab_sum_math1"
                android:layout_width="wrap_content"
                android:layout_height="38dp"
                android:text="📐 رياضيات - ج1"
                android:textColor="@color/text_primary"
                android:background="@drawable/tab_active"
                android:textSize="12sp"
                android:paddingStart="14dp"
                android:paddingEnd="14dp"
                android:layout_marginEnd="6dp" />

            <Button
                android:id="@+id/tab_sum_math2"
                android:layout_width="wrap_content"
                android:layout_height="38dp"
                android:text="📐 رياضيات - ج2"
                android:textColor="@color/text_secondary"
                android:background="@drawable/tab_inactive"
                android:textSize="12sp"
                android:paddingStart="14dp"
                android:paddingEnd="14dp"
                android:layout_marginEnd="6dp" />

            <Button
                android:id="@+id/tab_sum_sci1"
                android:layout_width="wrap_content"
                android:layout_height="38dp"
                android:text="🧪 علوم - ج1"
                android:textColor="@color/text_secondary"
                android:background="@drawable/tab_inactive"
                android:textSize="12sp"
                android:paddingStart="14dp"
                android:paddingEnd="14dp"
                android:layout_marginEnd="6dp" />

            <Button
                android:id="@+id/tab_sum_sci2"
                android:layout_width="wrap_content"
                android:layout_height="38dp"
                android:text="🧪 علوم - ج2"
                android:textColor="@color/text_secondary"
                android:background="@drawable/tab_inactive"
                android:textSize="12sp"
                android:paddingStart="14dp"
                android:paddingEnd="14dp" />
        </LinearLayout>
    </HorizontalScrollView>

    <!-- Content Cards Scroll -->
    <ScrollView
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"
        android:fillViewport="true"
        android:padding="12dp">

        <LinearLayout
            android:id="@+id/summary_cards_container"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical" />
    </ScrollView>
</LinearLayout>""")

    # E. activity_lab.xml (same as before)
    with open(f"{res_dir}/layout/activity_lab.xml", "w", encoding="utf-8") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/bg_dark">

    <WebView
        android:id="@+id/lab_webview"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

    <ImageButton
        android:id="@+id/btn_exit_to_hub"
        android:layout_width="40dp"
        android:layout_height="40dp"
        android:layout_gravity="top|start"
        android:layout_margin="10dp"
        android:background="@drawable/floating_back_transparent"
        android:src="@drawable/ic_chevron_left"
        android:tint="@color/cyan_accent"
        android:scaleType="centerInside"
        android:contentDescription="العودة"
        android:visibility="gone" />
</FrameLayout>""")

    # 6. AndroidManifest.xml
    with open(f"{base_dir}/AndroidManifest.xml", "w", encoding="utf-8") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.thaker.app"
    android:versionCode="4"
    android:versionName="1.3.0">

    <uses-sdk
        android:minSdkVersion="24"
        android:targetSdkVersion="34" />

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.WAKE_LOCK" />
    <uses-permission android:name="android.permission.RECORD_AUDIO" />
    <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" android:maxSdkVersion="32" />

    <supports-screens
        android:anyDensity="true"
        android:largeScreens="true"
        android:normalScreens="true"
        android:smallScreens="true"
        android:xlargeScreens="true" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:label="@string/app_name"
        android:supportsRtl="true"
        android:hardwareAccelerated="true"
        android:largeHeap="true"
        android:requestLegacyExternalStorage="true"
        android:theme="@style/AppTheme">

        <!-- 1. Main Hub: Grade & Subject selection -->
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:configChanges="orientation|screenSize|keyboardHidden"
            android:screenOrientation="unspecified">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <!-- 2. Hardware-Accelerated PDF Textbook Reader -->
        <activity
            android:name=".BookViewerActivity"
            android:exported="false"
            android:configChanges="orientation|screenSize|screenLayout|keyboardHidden"
            android:screenOrientation="sensor">
        </activity>

        <!-- 3. Automated Ministerial Quiz System -->
        <activity
            android:name=".QuizActivity"
            android:exported="false"
            android:configChanges="orientation|screenSize|keyboardHidden"
            android:screenOrientation="sensor">
        </activity>

        <!-- 4. Laws & Summaries Activity -->
        <activity
            android:name=".SummaryActivity"
            android:exported="false"
            android:configChanges="orientation|screenSize|keyboardHidden"
            android:screenOrientation="sensor">
        </activity>

        <!-- 5. 3D Interactive Chemistry Lab Book -->
        <activity
            android:name=".LabActivity"
            android:exported="false"
            android:configChanges="orientation|screenSize|screenLayout|keyboardHidden"
            android:screenOrientation="sensor">
        </activity>
    </application>
</manifest>""")

    print("  ✓ Resources, layouts, and manifest written successfully.")

def write_java_sources(base_dir):
    print("-> Writing Java source files...")
    src_dir = f"{base_dir}/src/com/thaker/app"
    os.makedirs(src_dir, exist_ok=True)
    
    with open(f"{src_dir}/ThemeUtil.java", "w", encoding="utf-8") as f:
        f.write("""package com.thaker.app;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;
import android.util.TypedValue;

public final class ThemeUtil {
    private static final String PREFS = "thaker_theme_prefs";
    private static final String KEY_DARK = "dark_mode";

    public static void apply(Activity activity) {
        SharedPreferences prefs = activity.getSharedPreferences(PREFS, Context.MODE_PRIVATE);
        boolean dark = prefs.getBoolean(KEY_DARK, false);
        activity.setTheme(dark ? R.style.AppTheme_Dark : R.style.AppTheme_Light);
    }

    public static boolean isDark(Context context) {
        return context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getBoolean(KEY_DARK, false);
    }

    public static void setDark(Activity activity, boolean dark) {
        activity.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().putBoolean(KEY_DARK, dark).apply();
        activity.recreate();
    }

    public static void toggle(Activity activity) {
        setDark(activity, !isDark(activity));
    }

    public static int color(Context context, int attr) {
        TypedValue value = new TypedValue();
        if (context.getTheme().resolveAttribute(attr, value, true)) {
            return value.data;
        }
        return 0;
    }
}
""")

    # 1. MainActivity.java
    with open(f"{src_dir}/MainActivity.java", "w", encoding="utf-8") as f:
        f.write("""package com.thaker.app;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Switch;
import android.widget.CompoundButton;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends Activity {

    private static final String PREFS_NAME = "thaker_app_prefs";
    private static final String KEY_AUTO_LAUNCH = "auto_launch_lab";

    private SharedPreferences prefs;
    private LinearLayout containerHighSchool;
    private LinearLayout containerMiddleSchool;
    private Button tabHighSchool;
    private Button tabMiddleSchool;
    private TextView tvGradeLabel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);

        prefs = getSharedPreferences(PREFS_NAME, MODE_PRIVATE);
        boolean autoLaunch = prefs.getBoolean(KEY_AUTO_LAUNCH, false);

        if (autoLaunch && !getIntent().getBooleanExtra("no_auto_launch", false)) {
            Intent intent = new Intent(this, LabActivity.class);
            startActivity(intent);
        }

        setContentView(R.layout.activity_main);

        containerHighSchool = findViewById(R.id.container_high_school);
        containerMiddleSchool = findViewById(R.id.container_middle_school);
        tabHighSchool = findViewById(R.id.tab_high_school);
        tabMiddleSchool = findViewById(R.id.tab_middle_school);
        tvGradeLabel = findViewById(R.id.tv_grade_label);

        // Stage Switcher Tabs
        tabHighSchool.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                switchToHighSchool();
            }
        });

        tabMiddleSchool.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                switchToMiddleSchool();
            }
        });

        // Chem Lab 3D Launch
        findViewById(R.id.btn_open_chem_lab).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, LabActivity.class));
            }
        });

        // Next-Gen Intelligent Interactive Textbook Engine (Science P2)
        View btnInteractiveEngine = findViewById(R.id.btn_open_sci9_interactive_engine);
        if (btnInteractiveEngine != null) {
            btnInteractiveEngine.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    Intent labIntent = new Intent(MainActivity.this, LabActivity.class);
                    labIntent.putExtra("html_asset", "thaker-interactive-book.html");
                    startActivity(labIntent);
                }
            });
        }

        // 9th Grade 3D Science Book & Laboratory
        findViewById(R.id.btn_open_sci9_3d_book).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent labIntent = new Intent(MainActivity.this, LabActivity.class);
                labIntent.putExtra("html_asset", "science-9th-book.html");
                startActivity(labIntent);
            }
        });

        // 9th Grade 3D Math Book & Laboratory
        findViewById(R.id.btn_open_math9_3d_book).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent labIntent = new Intent(MainActivity.this, LabActivity.class);
                labIntent.putExtra("html_asset", "math-9th-book.html");
                startActivity(labIntent);
            }
        });

        // 9th Grade Interactive Science Lab (opens complete 3D Science Book & Lab)
        findViewById(R.id.btn_open_sci9_lab).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent labIntent = new Intent(MainActivity.this, LabActivity.class);
                labIntent.putExtra("html_asset", "science-9th-book.html");
                startActivity(labIntent);
            }
        });

        // Auto launch checkbox
        Switch cb = findViewById(R.id.cb_auto_launch);
        cb.setChecked(autoLaunch);
        cb.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                prefs.edit().putBoolean(KEY_AUTO_LAUNCH, isChecked).apply();
            }
        });

        // About Button
        findViewById(R.id.btn_about).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showAboutDialog();
            }
        });

        setupMiddleSchoolButtons();

        findViewById(R.id.btn_notifications).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showSimpleDialog("الإشعارات", "لا توجد إشعارات جديدة.");
            }
        });
        findViewById(R.id.btn_profile).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showSimpleDialog("الملف الشخصي", "تطبيق ذاكر يعمل بالكامل دون اتصال بالإنترنت.");
            }
        });
        findViewById(R.id.btn_theme).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                ThemeUtil.toggle(MainActivity.this);
            }
        });
        findViewById(R.id.nav_home).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setNav(0);
            }
        });
        findViewById(R.id.nav_subjects).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setNav(1);
                switchToMiddleSchool();
            }
        });
        findViewById(R.id.nav_library).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setNav(2);
                showLibraryDialog();
            }
        });
        findViewById(R.id.nav_favorites).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setNav(3);
                showSimpleDialog("المفضلة", getString(R.string.favorites_empty));
            }
        });
        findViewById(R.id.nav_settings).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setNav(4);
                showThemeDialog();
            }
        });

        setNav(0);
        int stage = prefs.getInt(KEY_STAGE, 0);
        if (stage == 1) {
            switchToMiddleSchool();
        }
    }

    private static final String KEY_STAGE = "stage";

    private void setNav(int active) {
        TextView tvHome = findViewById(R.id.tv_nav_home);
        if (tvHome != null) {
            tvHome.setTextColor(active == 0 ? ThemeUtil.color(this, R.attr.thakerPrimary) : ThemeUtil.color(this, R.attr.thakerTextSecondary));
        }
        int[] otherIds = new int[]{R.id.nav_subjects, R.id.nav_library, R.id.nav_favorites, R.id.nav_settings};
        int[] otherIndices = new int[]{1, 2, 3, 4};
        for (int i = 0; i < otherIds.length; i++) {
            Button b = findViewById(otherIds[i]);
            if (b != null) {
                boolean isCurrent = (active == otherIndices[i]);
                b.setTextColor(isCurrent ? ThemeUtil.color(this, R.attr.thakerPrimary) : ThemeUtil.color(this, R.attr.thakerTextSecondary));
            }
        }
    }

    private void showSimpleDialog(String title, String message) {
        new AlertDialog.Builder(this).setTitle(title).setMessage(message).setPositiveButton("حسناً", null).show();
    }

    private void showThemeDialog() {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle(R.string.theme_toggle);
        builder.setItems(new CharSequence[]{getString(R.string.theme_light), getString(R.string.theme_dark)}, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                ThemeUtil.setDark(MainActivity.this, which == 1);
            }
        });
        builder.show();
    }

    private void showLibraryDialog() {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle(R.string.library_title);
        builder.setItems(new CharSequence[]{
                getString(R.string.chem_card_title),
                getString(R.string.book_science_3d),
                getString(R.string.book_math_3d),
                getString(R.string.science_lab)
        }, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                String asset = null;
                if (which == 1 || which == 3) {
                    asset = "science-9th-book.html";
                } else if (which == 2) {
                    asset = "math-9th-book.html";
                }
                Intent intent = new Intent(MainActivity.this, LabActivity.class);
                if (asset != null) {
                    intent.putExtra("html_asset", asset);
                }
                startActivity(intent);
            }
        });
        builder.show();
    }

    private void switchToHighSchool() {
        tabHighSchool.setBackgroundResource(R.drawable.tab_active);
        tabHighSchool.setTextColor(0xFFFFFFFF);
        tabMiddleSchool.setBackgroundResource(R.drawable.tab_inactive);
        tabMiddleSchool.setTextColor(ThemeUtil.color(this, R.attr.thakerTextSecondary));
        tvGradeLabel.setText(R.string.grade_12_title);
        containerHighSchool.setVisibility(View.VISIBLE);
        containerMiddleSchool.setVisibility(View.GONE);
        prefs.edit().putInt(KEY_STAGE, 0).apply();
    }

    private void switchToMiddleSchool() {
        tabMiddleSchool.setBackgroundResource(R.drawable.tab_active);
        tabMiddleSchool.setTextColor(0xFFFFFFFF);
        tabHighSchool.setBackgroundResource(R.drawable.tab_inactive);
        tabHighSchool.setTextColor(ThemeUtil.color(this, R.attr.thakerTextSecondary));
        tvGradeLabel.setText(R.string.grade_9_title);
        containerHighSchool.setVisibility(View.GONE);
        containerMiddleSchool.setVisibility(View.VISIBLE);
        prefs.edit().putInt(KEY_STAGE, 1).apply();
    }

    private void setupMiddleSchoolButtons() {
        // Science Part 1
        findViewById(R.id.btn_read_sci_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openBook("sci_p1", 0);
            }
        });
        findViewById(R.id.btn_index_sci_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showUnitIndexDialog("sci_p1");
            }
        });
        findViewById(R.id.btn_summary_sci_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openSummary("sci_p1");
            }
        });
        findViewById(R.id.btn_quiz_sci_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openQuiz("sci_p1");
            }
        });

        // Science Part 2
        findViewById(R.id.btn_read_sci_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openBook("sci_p2", 0);
            }
        });
        findViewById(R.id.btn_index_sci_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showUnitIndexDialog("sci_p2");
            }
        });
        findViewById(R.id.btn_summary_sci_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openSummary("sci_p2");
            }
        });
        findViewById(R.id.btn_quiz_sci_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openQuiz("sci_p2");
            }
        });

        // Math Part 1
        findViewById(R.id.btn_read_math_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openBook("math_p1", 0);
            }
        });
        findViewById(R.id.btn_index_math_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showUnitIndexDialog("math_p1");
            }
        });
        findViewById(R.id.btn_summary_math_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openSummary("math_p1");
            }
        });
        findViewById(R.id.btn_quiz_math_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openQuiz("math_p1");
            }
        });

        // Math Part 2
        findViewById(R.id.btn_read_math_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openBook("math_p2", 0);
            }
        });
        findViewById(R.id.btn_index_math_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showUnitIndexDialog("math_p2");
            }
        });
        findViewById(R.id.btn_summary_math_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openSummary("math_p2");
            }
        });
        findViewById(R.id.btn_quiz_math_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openQuiz("math_p2");
            }
        });

        // Comprehensive Exam (all 9th subjects)
        findViewById(R.id.btn_exam_9th_all).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openQuiz("all_9th");
            }
        });
    }

    private void openBook(String bookKey, int startPage) {
        Intent intent = new Intent(this, BookViewerActivity.class);
        intent.putExtra("book_key", bookKey);
        intent.putExtra("start_page", startPage);
        startActivity(intent);
    }

    private void openSummary(String tabKey) {
        Intent intent = new Intent(this, SummaryActivity.class);
        intent.putExtra("active_tab", tabKey);
        startActivity(intent);
    }

    private void openQuiz(String subjectKey) {
        Intent intent = new Intent(this, QuizActivity.class);
        intent.putExtra("quiz_subject", subjectKey);
        startActivity(intent);
    }

    private void showUnitIndexDialog(final String bookKey) {
        final String[] units;
        final int[] pages;
        String title;

        if ("sci_p1".equals(bookKey)) {
            title = "فهرس وحدات العلوم (الجزء الأول)";
            units = new String[]{
                "الوحدة 1: المحاليل وطرق التعبير عنها (ص 1)",
                "الوحدة 2: التفاعلات الكيميائية في حياتنا (ص 21)",
                "الوحدة 3: الصوت وانتقاله وتطبيقاته (ص 47)",
                "الوحدة 4: الضوء والرؤية والمرايا والعدسات (ص 67)",
                "الوحدة 5: الإخراج في الكائنات الحية (ص 99)",
                "الوحدة 6: التكاثر في الكائنات الحية (ص 125)",
                "الوحدة 7: أمراض الجهازين البولي والتناسلي (ص 151)"
            };
            pages = new int[]{1, 21, 47, 67, 99, 125, 151};
        } else if ("sci_p2".equals(bookKey)) {
            title = "فهرس وحدات العلوم (الجزء الثاني)";
            units = new String[]{
                "الوحدة 8: الكهرباء الساكنة والتيار وقانون أوم (ص 1)",
                "الوحدة 9: المغناطيسية والكهرومغناطيسية (ص 25)",
                "الوحدة 10: الطاقة ومصادرها وتحولاتها (ص 55)",
                "الوحدة 11: البيئة والتوازن البيئي والتلوث (ص 81)",
                "الوحدة 12: علوم الأرض والمعادن والطبقات (ص 105)",
                "الوحدة 13: الفضاء والكون والنظام الشمسي (ص 131)"
            };
            pages = new int[]{1, 25, 55, 81, 105, 131};
        } else if ("math_p1".equals(bookKey)) {
            title = "فهرس وحدات الرياضيات (الجزء الأول)";
            units = new String[]{
                "الوحدة 1: المجموعات والعلاقات والتكافؤ (ص 7)",
                "الوحدة 2: التطبيقات وأنواعها (ص 32)",
                "الوحدة 3: مجموعة الأعداد الحقيقية R (ص 40)",
                "الوحدة 4: تحليل المقادير الجبرية (ص 61)",
                "الوحدة 5: الكسور الجبرية والعمليات عليها (ص 94)",
                "تمارين عامة ومسائل وزارية شاملة (ص 160)"
            };
            pages = new int[]{7, 32, 40, 61, 94, 160};
        } else {
            title = "فهرس وحدات الرياضيات (الجزء الثاني)";
            units = new String[]{
                "الوحدة 5: الهندسة المستوية (الدائرة ونظرياتها) (ص 5)",
                "الوحدة 6: حساب المثلثات والزوايا الحادة (ص 45)",
                "الوحدة 7: التحويلات الهندسية والتكبير (ص 80)",
                "الوحدة 8: الإحصاء والاحتمالات (ص 111)"
            };
            pages = new int[]{5, 45, 80, 111};
        }

        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle(title);
        builder.setItems(units, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                openBook(bookKey, pages[which] - 1);
            }
        });
        builder.setNegativeButton("إلغاء", null);
        builder.show();
    }

    private void showAboutDialog() {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("عن ذاكر");
        builder.setMessage("كتاب ومعمل للصف التاسع والثالث الثانوي.\\n\\nتقرأ المنهج، وتجرّب التفاعلات بثلاثة أبعاد، وتتدرب على الأسئلة الوزارية. كل شيء يعمل دون إنترنت.\\n\\nتعلّم بوضوح.");
        builder.setPositiveButton("حسناً", null);
        builder.show();
    }
}
""")

    # 2. BookViewerActivity.java
    with open(f"{src_dir}/BookViewerActivity.java", "w", encoding="utf-8") as f:
        f.write("""package com.thaker.app;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.graphics.Bitmap;
import android.graphics.Matrix;
import android.graphics.PointF;
import android.graphics.pdf.PdfRenderer;
import android.os.Bundle;
import android.os.Environment;
import android.os.Handler;
import android.os.Looper;
import android.os.ParcelFileDescriptor;
import android.view.GestureDetector;
import android.view.MotionEvent;
import android.view.ScaleGestureDetector;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.SeekBar;
import android.widget.TextView;
import android.widget.Toast;

import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class BookViewerActivity extends Activity {

    private String bookKey = "sci_p1";
    private int curPageIndex = 0;
    private int totalPages = 1;

    private ParcelFileDescriptor pfd;
    private PdfRenderer renderer;
    private ExecutorService renderExecutor;
    private Handler mainHandler;

    private ImageView imageView;
    private ProgressBar progressBar;
    private View topToolbar;
    private View bottomToolbar;
    private TextView tvBookTitle;
    private TextView tvUnitName;
    private TextView tvPageIndicator;
    private SeekBar pageSeekBar;

    // Zoom & Pan Matrix
    private Matrix matrix = new Matrix();
    private Matrix savedMatrix = new Matrix();
    private static final int MODE_NONE = 0;
    private static final int MODE_DRAG = 1;
    private static final int MODE_ZOOM = 2;
    private int touchMode = MODE_NONE;
    private PointF startPoint = new PointF();
    private PointF midPoint = new PointF();
    private float oldDist = 1f;
    private float currentScale = 1f;

    private ScaleGestureDetector scaleDetector;
    private GestureDetector gestureDetector;
    private boolean toolbarsVisible = true;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);

        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED, WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED);

        setContentView(R.layout.activity_book_viewer);

        bookKey = getIntent().getStringExtra("book_key");
        if (bookKey == null) bookKey = "sci_p1";
        curPageIndex = getIntent().getIntExtra("start_page", 0);

        renderExecutor = Executors.newSingleThreadExecutor();
        mainHandler = new Handler(Looper.getMainLooper());

        imageView = findViewById(R.id.pdf_image_view);
        progressBar = findViewById(R.id.pdf_progress);
        topToolbar = findViewById(R.id.top_toolbar);
        bottomToolbar = findViewById(R.id.bottom_toolbar);
        tvBookTitle = findViewById(R.id.tv_viewer_book_title);
        tvUnitName = findViewById(R.id.tv_viewer_unit_name);
        tvPageIndicator = findViewById(R.id.tv_page_indicator);
        pageSeekBar = findViewById(R.id.page_seekbar);

        tvBookTitle.setText(getBookDisplayName(bookKey));

        setupGestures();
        setupControls();
        openPdfDocument();
    }

    private String getBookDisplayName(String key) {
        if ("sci_p1".equals(key)) return "علوم - الجزء الأول (الصف التاسع)";
        if ("sci_p2".equals(key)) return "علوم - الجزء الثاني (الصف التاسع)";
        if ("math_p1".equals(key)) return "رياضيات - الجزء الأول (الصف التاسع)";
        if ("math_p2".equals(key)) return "رياضيات - الجزء الثاني (الصف التاسع)";
        return "كتاب المنهج المدرسي";
    }

    private String getBookFileName(String key) {
        if ("sci_p1".equals(key)) return "science_part1_9th.pdf";
        if ("sci_p2".equals(key)) return "science_part2_9th.pdf";
        if ("math_p1".equals(key)) return "mathematics_part1_9th.pdf";
        if ("math_p2".equals(key)) return "mathematics_part2_9th.pdf";
        return "science_part1_9th.pdf";
    }

    private File resolvePdfFile(String key) {
        String fn = getBookFileName(key);

        // 1. First priority: App private internal files (100% permission-free, guaranteed to work)
        File internalFile = new File(getFilesDir(), fn);
        if (internalFile.exists() && internalFile.length() > 50000) {
            return internalFile;
        }

        // 2. Extract from bundled APK assets into internal private files
        try {
            InputStream in = getAssets().open("curriculum/9th/" + fn);
            File tempFile = new File(getFilesDir(), fn + ".tmp");
            FileOutputStream out = new FileOutputStream(tempFile);
            byte[] buf = new byte[65536];
            int len;
            while ((len = in.read(buf)) > 0) {
                out.write(buf, 0, len);
            }
            in.close();
            out.flush();
            out.close();
            if (tempFile.exists() && tempFile.length() > 50000) {
                tempFile.renameTo(internalFile);
                return internalFile;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        // 3. Fallback: try external storage ONLY if test open succeeds without permission error
        try {
            File[] candidates = new File[]{
                new File("/mnt/sdcard/projects/teaching-app/المنهج/تاسع/" + fn),
                new File(Environment.getExternalStorageDirectory(), "projects/teaching-app/المنهج/تاسع/" + fn),
                new File("/sdcard/projects/teaching-app/المنهج/تاسع/" + fn)
            };
            for (File cand : candidates) {
                if (cand.exists() && cand.canRead()) {
                    ParcelFileDescriptor testPfd = ParcelFileDescriptor.open(cand, ParcelFileDescriptor.MODE_READ_ONLY);
                    testPfd.close();
                    return cand;
                }
            }
        } catch (Throwable ignored) {}

        return null;
    }

    private void openPdfDocument() {
        progressBar.setVisibility(View.VISIBLE);
        renderExecutor.execute(new Runnable() {
            @Override
            public void run() {
                try {
                    File file = resolvePdfFile(bookKey);
                    if (file == null || !file.exists()) {
                        mainHandler.post(new Runnable() {
                            @Override
                            public void run() {
                                progressBar.setVisibility(View.GONE);
                                Toast.makeText(BookViewerActivity.this, "تعذر العثور على ملف الكتاب في مجلد المنهج!", Toast.LENGTH_LONG).show();
                            }
                        });
                        return;
                    }

                    pfd = ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY);
                    renderer = new PdfRenderer(pfd);
                    totalPages = renderer.getPageCount();

                    if (curPageIndex < 0) curPageIndex = 0;
                    if (curPageIndex >= totalPages) curPageIndex = totalPages - 1;

                    mainHandler.post(new Runnable() {
                        @Override
                        public void run() {
                            progressBar.setVisibility(View.GONE);
                            pageSeekBar.setMax(Math.max(0, totalPages - 1));
                            pageSeekBar.setProgress(curPageIndex);
                            renderCurrentPage();
                        }
                    });
                } catch (final Exception e) {
                    mainHandler.post(new Runnable() {
                        @Override
                        public void run() {
                            progressBar.setVisibility(View.GONE);
                            Toast.makeText(BookViewerActivity.this, "خطأ أثناء فتح الكتاب: " + e.getMessage(), Toast.LENGTH_LONG).show();
                        }
                    });
                }
            }
        });
    }

    private void renderCurrentPage() {
        if (renderer == null || curPageIndex < 0 || curPageIndex >= totalPages) return;
        progressBar.setVisibility(View.VISIBLE);

        final int targetPage = curPageIndex;
        renderExecutor.execute(new Runnable() {
            @Override
            public void run() {
                try {
                    PdfRenderer.Page page = renderer.openPage(targetPage);
                    int screenW = getResources().getDisplayMetrics().widthPixels;
                    int screenH = getResources().getDisplayMetrics().heightPixels;

                    // Scale to fit screen width while keeping sharp resolution
                    int renderW = Math.max(screenW, page.getWidth() * 2);
                    int renderH = (int) ((float) renderW * page.getHeight() / page.getWidth());

                    final Bitmap bitmap = Bitmap.createBitmap(renderW, renderH, Bitmap.Config.ARGB_8888);
                    page.render(bitmap, null, null, PdfRenderer.Page.RENDER_MODE_FOR_DISPLAY);
                    page.close();

                    mainHandler.post(new Runnable() {
                        @Override
                        public void run() {
                            progressBar.setVisibility(View.GONE);
                            imageView.setImageBitmap(bitmap);
                            resetZoomMatrix(bitmap);
                            updateUiInfo();
                        }
                    });
                } catch (Exception e) {
                    e.printStackTrace();
                    mainHandler.post(new Runnable() {
                        @Override
                        public void run() {
                            progressBar.setVisibility(View.GONE);
                        }
                    });
                }
            }
        });
    }

    private void resetZoomMatrix(Bitmap bitmap) {
        if (bitmap == null) return;
        int viewW = imageView.getWidth();
        int viewH = imageView.getHeight();
        if (viewW <= 0 || viewH <= 0) {
            viewW = getResources().getDisplayMetrics().widthPixels;
            viewH = getResources().getDisplayMetrics().heightPixels;
        }

        matrix.reset();
        float scale = (float) viewW / bitmap.getWidth();
        matrix.postScale(scale, scale);
        float dy = (viewH - bitmap.getHeight() * scale) / 2f;
        if (dy > 0) matrix.postTranslate(0, dy);

        currentScale = 1f;
        imageView.setImageMatrix(matrix);
    }

    private void updateUiInfo() {
        tvPageIndicator.setText("صفحة " + (curPageIndex + 1) + " من " + totalPages);
        pageSeekBar.setProgress(curPageIndex);
        tvUnitName.setText(getUnitNameForPage(bookKey, curPageIndex + 1));
    }

    private String getUnitNameForPage(String key, int page) {
        if ("sci_p1".equals(key)) {
            if (page < 21) return "الوحدة 1: المحاليل وتطبيقاتها";
            if (page < 47) return "الوحدة 2: التفاعلات الكيميائية";
            if (page < 67) return "الوحدة 3: الصوت وانتقاله";
            if (page < 99) return "الوحدة 4: الضوء والرؤية";
            if (page < 125) return "الوحدة 5: الإخراج في الكائنات الحية";
            if (page < 151) return "الوحدة 6: التكاثر في الكائنات الحية";
            return "الوحدة 7: أمراض الجهازين البولي والتناسلي";
        } else if ("sci_p2".equals(key)) {
            if (page < 25) return "الوحدة 8: الكهرباء الساكنة والتيار";
            if (page < 55) return "الوحدة 9: المغناطيسية والكهرومغناطيسية";
            if (page < 81) return "الوحدة 10: الطاقة وتحولاتها";
            if (page < 105) return "الوحدة 11: البيئة والتوازن البيئي";
            if (page < 131) return "الوحدة 12: علوم الأرض والمعادن";
            return "الوحدة 13: الفضاء والنظام الشمسي";
        } else if ("math_p1".equals(key)) {
            if (page < 32) return "الوحدة 1: المجموعات والعلاقات";
            if (page < 40) return "الوحدة 2: التطبيقات";
            if (page < 61) return "الوحدة 3: مجموعة الأعداد الحقيقية R";
            if (page < 94) return "الوحدة 4: تحليل المقادير الجبرية";
            return "الوحدة 5: الكسور الجبرية والعمليات عليها";
        } else {
            if (page < 45) return "الوحدة 5: الهندسة المستوية (الدائرة)";
            if (page < 80) return "الوحدة 6: حساب المثلثات";
            if (page < 111) return "الوحدة 7: التحويلات الهندسية والتكبير";
            return "الوحدة 8: الإحصاء والاحتمالات";
        }
    }

    private void setupControls() {
        findViewById(R.id.btn_back_viewer).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });

        findViewById(R.id.btn_prev_page).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (curPageIndex > 0) {
                    curPageIndex--;
                    renderCurrentPage();
                }
            }
        });

        findViewById(R.id.btn_next_page).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (curPageIndex < totalPages - 1) {
                    curPageIndex++;
                    renderCurrentPage();
                }
            }
        });

        findViewById(R.id.btn_reset_zoom).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (imageView.getDrawable() != null) {
                    matrix.reset();
                    currentScale = 1f;
                    imageView.setImageMatrix(matrix);
                    Toast.makeText(BookViewerActivity.this, "تمت إعادة ضبط التكبير", Toast.LENGTH_SHORT).show();
                }
            }
        });

        findViewById(R.id.btn_open_unit_index).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showJumpUnitDialog();
            }
        });

        tvPageIndicator.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showJumpPageDialog();
            }
        });

        pageSeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                if (fromUser && progress >= 0 && progress < totalPages) {
                    curPageIndex = progress;
                    renderCurrentPage();
                }
            }
            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {}
            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {}
        });
    }

    private void setupGestures() {
        scaleDetector = new ScaleGestureDetector(this, new ScaleGestureDetector.SimpleOnScaleGestureListener() {
            @Override
            public boolean onScale(ScaleGestureDetector detector) {
                float factor = detector.getScaleFactor();
                currentScale *= factor;
                currentScale = Math.max(0.8f, Math.min(currentScale, 4.0f));
                matrix.postScale(factor, factor, detector.getFocusX(), detector.getFocusY());
                imageView.setImageMatrix(matrix);
                return true;
            }
        });

        gestureDetector = new GestureDetector(this, new GestureDetector.SimpleOnGestureListener() {
            @Override
            public boolean onSingleTapConfirmed(MotionEvent e) {
                toggleToolbars();
                return true;
            }

            @Override
            public boolean onDoubleTap(MotionEvent e) {
                if (currentScale > 1.2f) {
                    currentScale = 1.0f;
                    matrix.reset();
                } else {
                    currentScale = 2.0f;
                    matrix.postScale(2.0f, 2.0f, e.getX(), e.getY());
                }
                imageView.setImageMatrix(matrix);
                return true;
            }

            @Override
            public boolean onFling(MotionEvent e1, MotionEvent e2, float velocityX, float velocityY) {
                if (currentScale <= 1.1f && e1 != null && e2 != null) {
                    float diffX = e2.getX() - e1.getX();
                    if (diffX > 100 && curPageIndex > 0) {
                        curPageIndex--;
                        renderCurrentPage();
                        return true;
                    } else if (diffX < -100 && curPageIndex < totalPages - 1) {
                        curPageIndex++;
                        renderCurrentPage();
                        return true;
                    }
                }
                return false;
            }
        });

        imageView.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                scaleDetector.onTouchEvent(event);
                gestureDetector.onTouchEvent(event);

                switch (event.getAction() & MotionEvent.ACTION_MASK) {
                    case MotionEvent.ACTION_DOWN:
                        savedMatrix.set(matrix);
                        startPoint.set(event.getX(), event.getY());
                        touchMode = MODE_DRAG;
                        break;
                    case MotionEvent.ACTION_POINTER_DOWN:
                        oldDist = spacing(event);
                        if (oldDist > 10f) {
                            savedMatrix.set(matrix);
                            midPoint(midPoint, event);
                            touchMode = MODE_ZOOM;
                        }
                        break;
                    case MotionEvent.ACTION_MOVE:
                        if (touchMode == MODE_DRAG && currentScale > 1.05f) {
                            matrix.set(savedMatrix);
                            matrix.postTranslate(event.getX() - startPoint.x, event.getY() - startPoint.y);
                            imageView.setImageMatrix(matrix);
                        }
                        break;
                    case MotionEvent.ACTION_UP:
                    case MotionEvent.ACTION_POINTER_UP:
                        touchMode = MODE_NONE;
                        break;
                }
                return true;
            }
        });
    }

    private float spacing(MotionEvent event) {
        float x = event.getX(0) - event.getX(1);
        float y = event.getY(0) - event.getY(1);
        return (float) Math.sqrt(x * x + y * y);
    }

    private void midPoint(PointF point, MotionEvent event) {
        float x = event.getX(0) + event.getX(1);
        float y = event.getY(0) + event.getY(1);
        point.set(x / 2, y / 2);
    }

    private void toggleToolbars() {
        toolbarsVisible = !toolbarsVisible;
        topToolbar.setVisibility(toolbarsVisible ? View.VISIBLE : View.GONE);
        bottomToolbar.setVisibility(toolbarsVisible ? View.VISIBLE : View.GONE);
    }

    private void showJumpPageDialog() {
        final EditText input = new EditText(this);
        input.setHint("أدخل رقم الصفحة (1 - " + totalPages + ")");
        input.setInputType(android.text.InputType.TYPE_CLASS_NUMBER);

        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("الانتقال إلى صفحة");
        builder.setView(input);
        builder.setPositiveButton("انتقال", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                try {
                    int p = Integer.parseInt(input.getText().toString().trim());
                    if (p >= 1 && p <= totalPages) {
                        curPageIndex = p - 1;
                        renderCurrentPage();
                    } else {
                        Toast.makeText(BookViewerActivity.this, "رقم الصفحة خارج النطاق!", Toast.LENGTH_SHORT).show();
                    }
                } catch (Exception ignored) {}
            }
        });
        builder.setNegativeButton("إلغاء", null);
        builder.show();
    }

    private void showJumpUnitDialog() {
        final String[] units;
        final int[] pages;

        if ("sci_p1".equals(bookKey)) {
            units = new String[]{
                "الوحدة 1: المحاليل وتطبيقاتها (ص 1)",
                "الوحدة 2: التفاعلات الكيميائية (ص 21)",
                "الوحدة 3: الصوت وانتقاله (ص 47)",
                "الوحدة 4: الضوء والرؤية (ص 67)",
                "الوحدة 5: الإخراج في الكائنات الحية (ص 99)",
                "الوحدة 6: التكاثر في الكائنات الحية (ص 125)",
                "الوحدة 7: أمراض الجهازين البولي والتناسلي (ص 151)"
            };
            pages = new int[]{1, 21, 47, 67, 99, 125, 151};
        } else if ("sci_p2".equals(bookKey)) {
            units = new String[]{
                "الوحدة 8: الكهرباء الساكنة والتيار (ص 1)",
                "الوحدة 9: المغناطيسية والكهرومغناطيسية (ص 25)",
                "الوحدة 10: الطاقة ومصادرها (ص 55)",
                "الوحدة 11: البيئة والتوازن البيئي (ص 81)",
                "الوحدة 12: علوم الأرض والمعادن (ص 105)",
                "الوحدة 13: الفضاء والنظام الشمسي (ص 131)"
            };
            pages = new int[]{1, 25, 55, 81, 105, 131};
        } else if ("math_p1".equals(bookKey)) {
            units = new String[]{
                "الوحدة 1: المجموعات والعلاقات (ص 7)",
                "الوحدة 2: التطبيقات وخواصها (ص 32)",
                "الوحدة 3: مجموعة الأعداد الحقيقية R (ص 40)",
                "الوحدة 4: تحليل المقادير الجبرية (ص 61)",
                "الوحدة 5: الكسور الجبرية والعمليات عليها (ص 94)",
                "تمارين عامة ومسائل وزارية (ص 160)"
            };
            pages = new int[]{7, 32, 40, 61, 94, 160};
        } else {
            units = new String[]{
                "الوحدة 5: الهندسة المستوية (الدائرة) (ص 5)",
                "الوحدة 6: حساب المثلثات (ص 45)",
                "الوحدة 7: التحويلات الهندسية والتكبير (ص 80)",
                "الوحدة 8: الإحصاء والاحتمالات (ص 111)"
            };
            pages = new int[]{5, 45, 80, 111};
        }

        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("فهرس الوحدات - اختر وحدة:");
        builder.setItems(units, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                curPageIndex = pages[which] - 1;
                renderCurrentPage();
            }
        });
        builder.setNegativeButton("إلغاء", null);
        builder.show();
    }

    @Override
    protected void onDestroy() {
        if (renderExecutor != null) renderExecutor.shutdown();
        try {
            if (renderer != null) renderer.close();
            if (pfd != null) pfd.close();
        } catch (Exception ignored) {}
        super.onDestroy();
    }
}
""")

    # 3. QuizActivity.java
    with open(f"{src_dir}/QuizActivity.java", "w", encoding="utf-8") as f:
        f.write("""package com.thaker.app;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class QuizActivity extends Activity {

    public static class Question {
        String text;
        String[] options;
        int correctIdx;
        String explanation;

        public Question(String text, String[] options, int correctIdx, String explanation) {
            this.text = text;
            this.options = options;
            this.correctIdx = correctIdx;
            this.explanation = explanation;
        }
    }

    private String quizSubject = "sci_p1";
    private List<Question> questions = new ArrayList<Question>();
    private int curIndex = 0;
    private int score = 0;
    private boolean answered = false;

    private TextView tvSubject;
    private TextView tvProgress;
    private TextView tvScoreTop;
    private TextView tvQuestion;
    private Button[] btnOpts = new Button[4];
    private LinearLayout cardExplain;
    private TextView tvExplainHeader;
    private TextView tvExplainBody;
    private Button btnNext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_quiz);

        quizSubject = getIntent().getStringExtra("quiz_subject");
        if (quizSubject == null) quizSubject = "sci_p1";

        tvSubject = findViewById(R.id.tv_quiz_subject);
        tvProgress = findViewById(R.id.tv_quiz_progress);
        tvScoreTop = findViewById(R.id.tv_quiz_score_top);
        tvQuestion = findViewById(R.id.tv_question_text);

        btnOpts[0] = findViewById(R.id.btn_opt_0);
        btnOpts[1] = findViewById(R.id.btn_opt_1);
        btnOpts[2] = findViewById(R.id.btn_opt_2);
        btnOpts[3] = findViewById(R.id.btn_opt_3);

        cardExplain = findViewById(R.id.card_explanation);
        tvExplainHeader = findViewById(R.id.tv_explain_header);
        tvExplainBody = findViewById(R.id.tv_explain_body);
        btnNext = findViewById(R.id.btn_quiz_next);

        findViewById(R.id.btn_quiz_back).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });

        loadQuestions();
        displayCurrentQuestion();
    }

    private void loadQuestions() {
        questions.clear();

        if ("sci_p1".equals(quizSubject) || "all_9th".equals(quizSubject)) {
            questions.add(new Question("المحلول الذي لا يستطيع إذابة أي كمية إضافية من المذاب عند درجة حرارة معينة يُسمى:",
                new String[]{"المحلول غير المشبع", "المحلول المشبع", "المحلول فوق المشبع", "المحلول المعلق"}, 1,
                "المحلول المشبع يحتوي على أقصى كمية ممكنة من المذاب عند ثبوت درجة الحرارة."));

            questions.add(new Question("تُقاس سرعة الصوت في الهواء الجاف عند درجة الصفر المئوي بحوالي:",
                new String[]{"331 م/ث", "500 م/ث", "1500 م/ث", "300000 كم/ث"}, 0,
                "سرعة الصوت في الهواء عند صفر مئوي هي 331 م/ث وتزداد بارتفاع درجة الحرارة."));

            questions.add(new Question("المرآة الكروية التي تُكوّن دائماً صورة تقديرية مصغرة ومعتدلة للأجسام هي:",
                new String[]{"المرآة المقعرة", "المرآة المحدبة", "المرآة المستوية", "المرآة الأسطوانية"}, 1,
                "المرآة المحدبة تفرق الأشعة وتُستخدم على جانبي السيارة لكشف مساحة أوسع."));

            questions.add(new Question("الوحدة الوظيفية الأساسية للإخراج وتنقية الدم في كلية الإنسان هي:",
                new String[]{"الحالب", "النفرون (الأنبوبة البولية)", "حوض الكلية", "المثانة"}, 1,
                "تحتوي كل كلية على حوالي مليون نفرون يقوم بترشيح الدم واستعادة المواد النافعة."));

            questions.add(new Question("التكاثر الخضري في النباتات يتميز بأنه:",
                new String[]{"ينتج أفراداً متطابقة مع النبات الأصلي", "يتطلب وجود حبوب اللقاح", "يؤدي لتنوع وراثي كبير", "يتم فقط عن طريق البذور"}, 0,
                "التكاثر الخضري هو تكاثر لا جنسي يُحافظ على الصفات الممتازة للنبات الأم."));
        }

        if ("sci_p2".equals(quizSubject) || "all_9th".equals(quizSubject)) {
            questions.add(new Question("ينص قانون أوم في الكهرباء على أن شدة التيار (ت) تتناسب طردياً مع فرق الجهد (جـ) وعكسياً مع:",
                new String[]{"المقاومة الكهربائية (م)", "القدرة الكهربائية", "الطاقة المستهلكة", "الشحنة الكهربائية"}, 0,
                "قانون أوم: جـ = ت × م، فكلما زادت المقاومة قلّ التيار الكهربائي."));

            questions.add(new Question("الجهاز الذي يحول الطاقة الميكانيكية الحركية إلى طاقة كهربائية هو:",
                new String[]{"المحرك الكهربائي", "المولد الكهربائي (الدينامو)", "المحول الكهربائي", "المكثف"}, 1,
                "المولد يعمل بظاهرة الحث الكهرومغناطيسي لفاراداي لتوليد التيار."));

            questions.add(new Question("أقرب الكواكب إلى الشمس في نظامنا الشمسي هو:",
                new String[]{"الزهرة", "المريخ", "عطارد", "الأرض"}, 2,
                "عطارد هو أصغر وأقرب الكواكب للشمس ويدور حولها في 88 يوماً."));

            questions.add(new Question("الصخور المتكونة من تبريد وتبلور الماغما في باطن الأرض أو اللابة على سطحها هي:",
                new String[]{"الصخور الرسوبية", "الصخور النارية", "الصخور المتحولة", "الصخور الطينية"}, 1,
                "الصخور النارية مثل البازلت والجرانيت هي أصل جميع الصخور في القشرة الأرضية."));
        }

        if ("math_p1".equals(quizSubject) || "all_9th".equals(quizSubject)) {
            questions.add(new Question("العلاقة التي تتصف بأنها انعكاسية ومتماثلة ومتعدية تُسمى:",
                new String[]{"علاقة ترتيب جزئي", "علاقة تكافؤ", "علاقة عكسية", "تطبيق شامل"}, 1,
                "علاقة التكافؤ تجمع الخواص الثلاث: الانعكاس والتماثل والتعدي."));

            questions.add(new Question("تحليل المقدار الجبري (س² − 25) هو:",
                new String[]{"(س − 5)(س − 5)", "(س + 5)(س − 5)", "(س + 25)(س − 1)", "س(س − 25)"}, 1,
                "الفرق بين مربعين: أ² − ب² = (أ − ب)(أ + ب)."));

            questions.add(new Question("تحليل مجموع المكعبين (س³ + 8) يساوي:",
                new String[]{"(س + 2)(س² − 2س + 4)", "(س + 2)(س² + 2س + 4)", "(س − 2)(س² + 2س + 4)", "(س + 2)³"}, 0,
                "مجموع مكعبين: (س + أ)(س² − أس + أ²)."));

            questions.add(new Question("مجموعة الأعداد الحقيقية R تتكون من اتحاد مجموعة الأعداد النسبية Q مع:",
                new String[]{"الأعداد الطبيعية", "الأعداد الصحيحة", "الأعداد غير النسبية (الجذور الصماء)", "الصفر فقط"}, 2,
                "ح = ن ∪ ن̄ (النسبية وغير النسبية مثل π وجذر 2)."));
        }

        if ("math_p2".equals(quizSubject) || "all_9th".equals(quizSubject)) {
            questions.add(new Question("العمود النازل من مركز الدائرة على أي وتر فيها:",
                new String[]{"يوازي الوتر", "ينصف الوتر", "يضاعف طول الوتر", "يمس الدائرة"}, 1,
                "مبرهنة هندسية أساسية: المستقيم المار بمركز الدائرة عمودياً على وتر ينصف ذلك الوتر."));

            questions.add(new Question("قياس الزاوية المحيطية يساوي دائماً:",
                new String[]{"ضعف قياس المركزية المشتركة معها في القوس", "نصف قياس المركزية المشتركة معها في القوس", "يساوي تماماً قياس المركزية", "180 درجة"}, 1,
                "الزاوية المحيطية = 1/2 الزاوية المركزية المشتركة معها في القوس نفسه."));

            questions.add(new Question("في أي شكل رباعي دائري، مجموع قياسي أي زاويتين متقابلتين يساوي:",
                new String[]{"90°", "180° (متكاملتان)", "360°", "270°"}, 1,
                "خاصية مميزة للرباعي الدائري: كل زاويتين متقابلتين متكاملتان (مجموعهما 180°)."));

            questions.add(new Question("قيمة النسبة المثلثية جيب تمام الزاوية 60° (جتا 60°) تساوي:",
                new String[]{"1/2", "جذر(3)/2", "1", "جذر(2)"}, 0,
                "جتا 60° = 1/2 = جا 30°، وظا 45° = 1."));

            questions.add(new Question("المتوسط الحسابي للقيم (4 ، 6 ، 8 ، 10 ، 12) يساوي:",
                new String[]{"6", "8", "10", "40"}, 1,
                "المتوسط الحسابي = مجموع القيم (40) / عددها (5) = 8."));
        }

        Collections.shuffle(questions);
    }

    private void displayCurrentQuestion() {
        if (curIndex >= questions.size()) {
            showFinalResults();
            return;
        }

        answered = false;
        Question q = questions.get(curIndex);

        tvSubject.setText(getQuizTitle(quizSubject));
        tvProgress.setText("السؤال " + (curIndex + 1) + " من " + questions.size());
        tvScoreTop.setText("النقاط: " + score);
        tvQuestion.setText(q.text);

        cardExplain.setVisibility(View.GONE);
        btnNext.setVisibility(View.GONE);

        for (int i = 0; i < 4; i++) {
            final int optIdx = i;
            btnOpts[i].setText(q.options[i]);
            btnOpts[i].setBackgroundResource(R.drawable.quiz_option_normal);
            btnOpts[i].setEnabled(true);
            btnOpts[i].setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    handleOptionClick(optIdx);
                }
            });
        }
    }

    private void handleOptionClick(int selectedIdx) {
        if (answered) return;
        answered = true;

        Question q = questions.get(curIndex);
        boolean isCorrect = (selectedIdx == q.correctIdx);

        for (int i = 0; i < 4; i++) {
            btnOpts[i].setEnabled(false);
            if (i == q.correctIdx) {
                btnOpts[i].setBackgroundResource(R.drawable.quiz_option_correct);
            } else if (i == selectedIdx) {
                btnOpts[i].setBackgroundResource(R.drawable.quiz_option_wrong);
            }
        }

        if (isCorrect) {
            score++;
            tvExplainHeader.setText("إجابة صحيحة وممتازة! ✅");
            tvExplainHeader.setTextColor(ThemeUtil.color(this, R.attr.thakerSuccess));
        } else {
            tvExplainHeader.setText("إجابة غير صحيحة ❌");
            tvExplainHeader.setTextColor(ThemeUtil.color(this, R.attr.thakerError));
        }

        tvExplainBody.setText(q.explanation);
        cardExplain.setVisibility(View.VISIBLE);

        btnNext.setVisibility(View.VISIBLE);
        btnNext.setText(curIndex + 1 < questions.size() ? "السؤال التالي ⬅" : "عرض النتيجة النهائية 🏆");
        btnNext.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                curIndex++;
                displayCurrentQuestion();
            }
        });
    }

    private void showFinalResults() {
        int pct = Math.round(((float) score / questions.size()) * 100);
        String msg = "حصلت على: " + score + " من " + questions.size() + " (" + pct + "%)\\n\\n";
        if (pct >= 85) msg += "🌟 ممتاز جداً! أداء متميز ومتقن في المنهج الوزاري!";
        else if (pct >= 65) msg += "👍 جيد جداً! واصل المراجعة لضمان الدرجة الكاملة.";
        else msg += "📚 ننصحك بمراجعة وحدات الكتاب والملخصات ثم إعادة الاختبار.";

        AlertDialog.Builder b = new AlertDialog.Builder(this);
        b.setTitle("نتيجة الاختبار الوزاري");
        b.setMessage(msg);
        b.setCancelable(false);
        b.setPositiveButton("إعادة الاختبار", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                curIndex = 0;
                score = 0;
                loadQuestions();
                displayCurrentQuestion();
            }
        });
        b.setNegativeButton("العودة للرئيسية", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                finish();
            }
        });
        b.show();
    }

    private String getQuizTitle(String key) {
        if ("sci_p1".equals(key)) return "اختبار علوم 9 - الجزء الأول";
        if ("sci_p2".equals(key)) return "اختبار علوم 9 - الجزء الثاني";
        if ("math_p1".equals(key)) return "اختبار رياضيات 9 - الجزء الأول";
        if ("math_p2".equals(key)) return "اختبار رياضيات 9 - الجزء الثاني";
        return "الاختبار الشامل للشهادة الأساسية (تاسع)";
    }
}
""")

    # 4. SummaryActivity.java
    with open(f"{src_dir}/SummaryActivity.java", "w", encoding="utf-8") as f:
        f.write("""package com.thaker.app;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

public class SummaryActivity extends Activity {

    private LinearLayout cardsContainer;
    private Button tabMath1, tabMath2, tabSci1, tabSci2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_summary);

        cardsContainer = findViewById(R.id.summary_cards_container);
        tabMath1 = findViewById(R.id.tab_sum_math1);
        tabMath2 = findViewById(R.id.tab_sum_math2);
        tabSci1 = findViewById(R.id.tab_sum_sci1);
        tabSci2 = findViewById(R.id.tab_sum_sci2);

        findViewById(R.id.btn_summary_back).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });

        tabMath1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                selectTab("math_p1");
            }
        });
        tabMath2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                selectTab("math_p2");
            }
        });
        tabSci1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                selectTab("sci_p1");
            }
        });
        tabSci2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                selectTab("sci_p2");
            }
        });

        String active = getIntent().getStringExtra("active_tab");
        if (active == null) active = "math_p1";
        selectTab(active);
    }

    private void selectTab(String key) {
        resetTabs();
        cardsContainer.removeAllViews();

        if ("math_p1".equals(key)) {
            tabMath1.setBackgroundResource(R.drawable.tab_active);
            tabMath1.setTextColor(ThemeUtil.color(this, R.attr.thakerTextPrimary));
            populateMath1();
        } else if ("math_p2".equals(key)) {
            tabMath2.setBackgroundResource(R.drawable.tab_active);
            tabMath2.setTextColor(ThemeUtil.color(this, R.attr.thakerTextPrimary));
            populateMath2();
        } else if ("sci_p1".equals(key)) {
            tabSci1.setBackgroundResource(R.drawable.tab_active);
            tabSci1.setTextColor(ThemeUtil.color(this, R.attr.thakerTextPrimary));
            populateSci1();
        } else {
            tabSci2.setBackgroundResource(R.drawable.tab_active);
            tabSci2.setTextColor(ThemeUtil.color(this, R.attr.thakerTextPrimary));
            populateSci2();
        }
    }

    private void resetTabs() {
        tabMath1.setBackgroundResource(R.drawable.tab_inactive);
        tabMath1.setTextColor(ThemeUtil.color(this, R.attr.thakerTextSecondary));
        tabMath2.setBackgroundResource(R.drawable.tab_inactive);
        tabMath2.setTextColor(ThemeUtil.color(this, R.attr.thakerTextSecondary));
        tabSci1.setBackgroundResource(R.drawable.tab_inactive);
        tabSci1.setTextColor(ThemeUtil.color(this, R.attr.thakerTextSecondary));
        tabSci2.setBackgroundResource(R.drawable.tab_inactive);
        tabSci2.setTextColor(ThemeUtil.color(this, R.attr.thakerTextSecondary));
    }

    private void addCard(String title, String body, String badge) {
        LinearLayout card = new LinearLayout(this);
        card.setOrientation(LinearLayout.VERTICAL);
        card.setBackgroundResource(R.drawable.card_bg);
        card.setPadding(24, 20, 24, 20);

        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(
            LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);
        lp.setMargins(0, 0, 0, 20);
        card.setLayoutParams(lp);

        TextView tvTitle = new TextView(this);
        tvTitle.setText(title + (badge != null ? " (" + badge + ")" : ""));
        tvTitle.setTextColor(ThemeUtil.color(this, R.attr.thakerPrimary));
        tvTitle.setTextSize(15);
        tvTitle.setTypeface(null, android.graphics.Typeface.BOLD);
        tvTitle.setPadding(0, 0, 0, 8);

        TextView tvBody = new TextView(this);
        tvBody.setText(body);
        tvBody.setTextColor(0xFFFFFFFF);
        tvBody.setTextSize(13);
        tvBody.setLineSpacing(6, 1);

        card.addView(tvTitle);
        card.addView(tvBody);
        cardsContainer.addView(card);
    }

    private void populateMath1() {
        addCard("طرق تحليل المقادير الجبرية الست",
            "1. إخراج العامل المشترك الأعلى (ع.م.أ): مثل 3س + 6 = 3(س + 2).\\n" +
            "2. الفرق بين مربعين: س² − ص² = (س − ص)(س + ص).\\n" +
            "3. مجموع مكعبين: س³ + ص³ = (س + ص)(س² − س ص + ص²).\\n" +
            "4. الفرق بين مكعبين: س³ − ص³ = (س − ص)(س² + س ص + ص²).\\n" +
            "5. المقدار الثلاثي البسيط: س² + ب س + جـ = (س + م)(س + ن) حيث م+ن=ب وم×ن=جـ.\\n" +
            "6. التحليل بالتقسيم وإكمال المربع للمقادير الرباعية والخاصة.", "الوحدة 4");

        addCard("العلاقات والتطبيقات",
            "• العلاقة الانعكاسية: (أ ، أ) ينتمي للعلاقة لكل أ.\\n" +
            "• العلاقة المتماثلة: إذا كان (أ ، ب) ينتمي للعلاقة فإن (ب ، أ) ينتمي لها.\\n" +
            "• العلاقة المتعدية: إذا كان (أ ، ب) و(ب ، جـ) ينتميان فإن (أ ، جـ) ينتمي لها.\\n" +
            "• علاقة التكافؤ: هي العلاقة التي تكون انعكاسية ومتماثلة ومتعدية معاً.\\n" +
            "• التطبيق: علاقة يرتبط فيها كل عنصر من المجال بعنصر واحد فقط في المجال المقابل.\\n" +
            "• أنواع التطبيقات: شامل (المدى = المجال المقابل)، متباين (عناصر مختلفة لها صور مختلفة)، تقابل (شامل ومتباين معاً).", "الوحدة 1 و 2");

        addCard("الأعداد الحقيقية R والعمليات عليها",
            "• ح = ن ∪ ن̄ (مجموعة الأعداد النسبية وغير النسبية).\\n" +
            "• إنطاق المقام: ضرب البسط والمقام في مرافق المقام للتخلص من الجذور في المقام.\\n" +
            "• الفترات: المغلقة [أ ، ب]، المفتوحة ]أ ، ب[، ونصف المغلقة.\\n" +
            "• القيمة المطلقة: |س| ≥ 0 دائماً، وتُعبر عن المسافة على خط الأعداد.", "الوحدة 3");
    }

    private void populateMath2() {
        addCard("نظريات ومبرهنات الدائرة",
            "• مبرهنة الوتر والعمود: المستقيم المار بمركز الدائرة عمودياً على وتر فيها ينصف ذلك الوتر وينصف قوسه.\\n" +
            "• مبرهنة الأوتار المتطابقة: في الدائرة الواحدة أو الدوائر المتطابقة، الأوتار المتطابقة تكون على أبعاد متساوية من المركز.\\n" +
            "• الزاوية المركزية والمحيطية: قياس الزاوية المحيطية = نصف قياس الزاوية المركزية المشتركة معها في نفس القوس.\\n" +
            "• زوايا في نفس القوس: جميع الزوايا المحيطية المقامة على قوس واحد في دائرة متطابقة.\\n" +
            "• مبرهنة الرباعي الدائري: كل زاويتين متقابلتين في أي شكل رباعي دائري متكاملتان (مجموعهما = 180°).\\n" +
            "• مبرهنة المماس: مماس الدائرة عمودي على نصف القطر عند نقطة التماس.", "الوحدة 5");

        addCard("حساب المثلثات والزوايا",
            "في المثلث القائم الزاوية:\\n" +
            "• جيب الزاوية (جا هـ) = المقابل / الوتر\\n" +
            "• جيب تمام الزاوية (جتا هـ) = المجاور / الوتر\\n" +
            "• ظل الزاوية (ظا هـ) = المقابل / المجاور = جا هـ / جتا هـ\\n" +
            "• المتطابقة الأساسية: جا² هـ + جتا² هـ = 1\\n\\n" +
            "النسب للزوايا الخاصة:\\n" +
            "• جا 30° = 1/2 ، جتا 30° = √3/2 ، ظا 30° = 1/√3\\n" +
            "• جا 45° = 1/√2 ، جتا 45° = 1/√2 ، ظا 45° = 1\\n" +
            "• جا 60° = √3/2 ، جتا 60° = 1/2 ، ظا 60° = √3", "الوحدة 6");

        addCard("الإحصاء والاحتمالات",
            "• المتوسط الحسابي: مجموع القيم مقسوماً على عددها (س̄ = مجـ س / ن).\\n" +
            "• المنوال: القيمة الأكثر تكراراً أو شيوعاً بين البيانات.\\n" +
            "• الوسيط: القيمة التي تقسم البيانات المرتبة (تصاعدياً أو تنازلياً) إلى نصفين متساويين.\\n" +
            "• المدى: الفرق بين أكبر قيمة وأصغر قيمة في مجموعة البيانات.", "الوحدة 8");
    }

    private void populateSci1() {
        addCard("المحاليل والتفاعلات الكيميائية",
            "• المحلول المشبع: يحتوي على أقصى كمية مذاب عند ثبوت درجة الحرارة.\\n" +
            "• النسبة المئوية الكتلية = (كتلة المذاب / كتلة المحلول) × 100%.\\n" +
            "• تفاعلات الترسيب: تفاعلات كيميائية ينتج عنها مادة صلبة غير ذائبة في المحلول.\\n" +
            "• العوامل المؤثرة في سرعة التفاعل: طبيعة المواد المتفاعلة، التركيز، درجة الحرارة، والمحفزات.", "الوحدة 1 و 2");

        addCard("الصوت والضوء",
            "• سرعة الصوت: 331 م/ث عند 0° مئوية في الهواء وتزداد مع زيادة الحرارة والكثافة.\\n" +
            "• صدى الصوت: تكرار سماع الصوت نتيجة انعكاسه على حاجز على بعد لا يقل عن 17 متراً.\\n" +
            "• قانونا الانعكاس في الضوء:\\n" +
            "  1. زاوية السقوط = زاوية الانعكاس.\\n" +
            "  2. الشعاع الساقط والمنعكس والعمود المقام تقع جميعها في مستوى واحد عمودي على السطح العاكس.\\n" +
            "• المرايا المقعرة تجمّع الأشعة (مجمعة)، بينما المحدبة تفرق الأشعة وتكون صوراً مصغرة.", "الوحدة 3 و 4");

        addCard("الإخراج والتكاثر وأجهزة الجسم",
            "• الكلية والنفرونات: ترشيح الدم، التخلص من الفضلات النيتروجينية كاليوريا والأملاح الزائدة.\\n" +
            "• الجلد: الإخراج عن طريق الغدد العرقية وتنظيم درجة حرارة الجسم.\\n" +
            "• التكاثر في النبات: التلقيح (ذاتي وخلطي) يتبعه الإخصاب لتكوين البذور والثمار.\\n" +
            "• أمراض الجهازين البولي والتناسلي: حصوات الكلى، بلهارسيا المجاري البولية، والتهابات المسالك البولية وطرق الوقاية منها.", "الوحدة 5 و 6 و 7");
    }

    private void populateSci2() {
        addCard("الكهرباء والمغناطيسية",
            "• قانون أوم: جـ = ت × م (فرق الجهد = شدة التيار × المقاومة).\\n" +
            "• التوصيل على التوالي: شدة التيار ثابتة، والمقاومة الكلية = م1 + م2 + ...\\n" +
            "• التوصيل على التوازي: فرق الجهد ثابت، و 1/م الكلية = 1/م1 + 1/م2 + ...\\n" +
            "• الحث الكهرومغناطيسي: توليد تيار كهربائي في موصل عند تغير المجال المغناطيسي القاطع له.\\n" +
            "• المحول الكهربائي: جهاز لرفع أو خفض الجهد المتردد (جـ2 / جـ1 = ن2 / ن1).", "الوحدة 8 و 9");

        addCard("الطاقة والبيئة",
            "• قانون بقاء الطاقة: الطاقة لا تفنى ولا تستحدث من العدم بل تتحول من شكل إلى آخر.\\n" +
            "• الطاقة الحركية طح = 1/2 ك ع² ، طاقة الوضع طو = ك × جـ × ف.\\n" +
            "• التوازن البيئي: التفاعل المتوازن بين المكونات الحية (المنتجات، المستهلكات، المحللات) وغير الحية.\\n" +
            "• الاحتباس الحراري: زيادة تركيز غازات الدفيئة (مثل CO₂) تحبس الأشعة تحت الحمراء في الجو.", "الوحدة 10 و 11");

        addCard("علوم الأرض والفضاء",
            "• طبقات الأرض: القشرة الأرضية، الوشاح (الستار)، واللب (الداخلي والخارجي).\\n" +
            "• الصخور: نارية (بازلت، جرانيت)، رسوبية (حجر رملي، جيري)، ومتحولة (رخام).\\n" +
            "• النظام الشمسي: الشمس و8 كواكب: عطارد، الزهرة، الأرض، المريخ (داخلية)، المشتري، زحل، أورانوس، نبتون (خارجية).\\n" +
            "• السنة الضوئية: المسافة التي يقطعها الضوء في سنة كاملة وتساوي حوالي 9.46 تريليون كم.", "الوحدة 12 و 13");
    }
}
""")

    # 5. LabActivity.java
    with open(f"{src_dir}/LabActivity.java", "w", encoding="utf-8") as f:
        f.write("""package com.thaker.app;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;
import android.webkit.JavascriptInterface;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;

public class LabActivity extends Activity {

    private WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);

        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED, WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED);

        enableImmersiveMode();
        setContentView(R.layout.activity_lab);

        webView = findViewById(R.id.lab_webview);
        setupWebView();

        View btnExit = findViewById(R.id.btn_exit_to_hub);
        if (btnExit != null) {
            btnExit.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    confirmExit();
                }
            });
        }
    }

    private void enableImmersiveMode() {
        View decorView = getWindow().getDecorView();
        decorView.setSystemUiVisibility(
            View.SYSTEM_UI_FLAG_LAYOUT_STABLE
            | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
            | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
            | View.SYSTEM_UI_FLAG_FULLSCREEN
            | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
            | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
        );
    }

    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        if (hasFocus) {
            enableImmersiveMode();
        }
    }

    private void setupWebView() {
        WebSettings ws = webView.getSettings();
        ws.setJavaScriptEnabled(true);
        ws.setDomStorageEnabled(true);
        ws.setDatabaseEnabled(true);
        ws.setAllowFileAccess(true);
        ws.setAllowContentAccess(true);
        ws.setAllowFileAccessFromFileURLs(true);
        ws.setAllowUniversalAccessFromFileURLs(true);
        ws.setMediaPlaybackRequiresUserGesture(false);
        ws.setBuiltInZoomControls(false);
        ws.setDisplayZoomControls(false);
        ws.setSupportZoom(true);
        ws.setUseWideViewPort(true);
        ws.setLoadWithOverviewMode(true);
        ws.setCacheMode(WebSettings.LOAD_NO_CACHE);

        webView.clearCache(true);
        webView.setLayerType(View.LAYER_TYPE_HARDWARE, null);
        webView.setWebChromeClient(new WebChromeClient());
        webView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                return false;
            }
        });

        webView.addJavascriptInterface(new Object() {
            @JavascriptInterface
            public void returnToHome() {
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        returnToMain();
                    }
                });
            }
        }, "ThakerBridge");

        String htmlAsset = getIntent().getStringExtra("html_asset");
        if (htmlAsset == null || htmlAsset.isEmpty() || htmlAsset.contains("/") || htmlAsset.contains("..")) {
            htmlAsset = "chem-lab-book.html";
        }
        webView.loadUrl("file:///android_asset/" + htmlAsset);
    }

    private void returnToMain() {
        Intent intent = new Intent(LabActivity.this, MainActivity.class);
        intent.putExtra("no_auto_launch", true);
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
        startActivity(intent);
        finish();
    }

    private void confirmExit() {
        returnToMain();
    }

    @Override
    public void onBackPressed() {
        returnToMain();
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (webView != null) webView.onResume();
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (webView != null) webView.onPause();
    }

    @Override
    protected void onDestroy() {
        if (webView != null) webView.destroy();
        super.onDestroy();
    }
}
""")

    print("  ✓ Java source code written successfully.")

def copy_assets(base_dir):
    print("-> Preparing assets (interactive books & 9th Grade PDFs)...")
    assets_dir = f"{base_dir}/assets"
    os.makedirs(f"{assets_dir}/curriculum/9th", exist_ok=True)
    
    # 1. Interactive books
    shutil.copy2(SOURCE_HTML, f"{assets_dir}/chem-lab-book.html")
    if os.path.exists(SOURCE_SCI9_3D):
        shutil.copy2(SOURCE_SCI9_3D, f"{assets_dir}/science-9th-book.html")
        shutil.copy2(SOURCE_SCI9_3D, f"{assets_dir}/science9-interactive.html")
        print(f"  ✓ Bundled 3D Science Book: science-9th-book.html ({os.path.getsize(SOURCE_SCI9_3D) / 1024:.0f} KB)")
    if os.path.exists(f"{WORKSPACE}/thaker-interactive-book.html"):
        shutil.copy2(f"{WORKSPACE}/thaker-interactive-book.html", f"{assets_dir}/thaker-interactive-book.html")
        print(f"  ✓ Bundled Next-Gen Interactive Textbook: thaker-interactive-book.html")
    if os.path.exists(SOURCE_MATH9_3D):
        shutil.copy2(SOURCE_MATH9_3D, f"{assets_dir}/math-9th-book.html")
        print(f"  ✓ Bundled 3D Math Book: math-9th-book.html ({os.path.getsize(SOURCE_MATH9_3D) / 1024:.0f} KB)")
    
    # 2. 9th Grade Curriculum PDFs
    pdf_files = [
        "science_part1_9th.pdf",
        "science_part2_9th.pdf",
        "mathematics_part1_9th.pdf",
        "mathematics_part2_9th.pdf"
    ]
    for fn in pdf_files:
        src_path = os.path.join(CURRICULUM_9TH_DIR, fn)
        dst_path = os.path.join(assets_dir, "curriculum/9th", fn)
        if os.path.exists(src_path):
            shutil.copy2(src_path, dst_path)
            print(f"  ✓ Bundled PDF: {fn} ({os.path.getsize(dst_path) / (1024*1024):.2f} MB)")
        else:
            print(f"  ⚠️ Warning: {src_path} not found!")

    # 3. Curriculum Data Packs
    if os.path.exists(f"{WORKSPACE}/data"):
        shutil.copytree(f"{WORKSPACE}/data", f"{assets_dir}/data", dirs_exist_ok=True)
        print("  ✓ Bundled Structured Data Packs: assets/data")
    if os.path.exists(f"{WORKSPACE}/assets"):
        shutil.copytree(f"{WORKSPACE}/assets", f"{assets_dir}/assets", dirs_exist_ok=True)
        if os.path.exists(f"{WORKSPACE}/assets/curriculum"):
            shutil.copytree(f"{WORKSPACE}/assets/curriculum", f"{assets_dir}/curriculum", dirs_exist_ok=True)
        print("  ✓ Bundled Curriculum Page Assets: assets/assets & assets/curriculum")
    if os.path.exists(f"{WORKSPACE}/thaker-engine"):
        shutil.copytree(f"{WORKSPACE}/thaker-engine", f"{assets_dir}/thaker-engine", dirs_exist_ok=True)
        print("  ✓ Bundled Thaker Engine: assets/thaker-engine")

def compile_and_package(base_dir):
    print("-> Running Android Toolchain (aapt2, javac, d8, zipalign, apksigner)...")
    
    # 1. Compile resources
    res_zip = f"{base_dir}/compiled_res.zip"
    print("  1/6. aapt2 compile...")
    subprocess.run([AAPT2, "compile", "--dir", f"{base_dir}/res", "-o", res_zip], check=True)
    
    # 2. Link resources (-0 pdf to store PDFs uncompressed for fast mmap access)
    gen_dir = f"{base_dir}/gen"
    os.makedirs(gen_dir, exist_ok=True)
    unaligned_apk = f"{base_dir}/unaligned.apk"
    print("  2/6. aapt2 link with uncompressed PDFs (-0 pdf)...")
    cmd_link = [
        AAPT2, "link",
        "-I", PLATFORM_JAR,
        "--manifest", f"{base_dir}/AndroidManifest.xml",
        "-o", unaligned_apk,
        res_zip,
        "-A", f"{base_dir}/assets",
        "-0", "pdf",
        "--java", gen_dir
    ]
    subprocess.run(cmd_link, check=True)
    
    # 3. Compile Java sources
    obj_dir = f"{base_dir}/obj"
    os.makedirs(obj_dir, exist_ok=True)
    print("  3/6. javac compile...")
    java_files = []
    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.endswith(".java"):
                java_files.append(os.path.join(root, f))
                
    cmd_javac = [
        "javac",
        "-source", "8",
        "-target", "8",
        "-bootclasspath", PLATFORM_JAR,
        "-Xlint:-options",
        "-d", obj_dir
    ] + java_files
    subprocess.run(cmd_javac, check=True)
    
    # 4. Dexing with d8
    dex_dir = f"{base_dir}/dex"
    os.makedirs(dex_dir, exist_ok=True)
    print("  4/6. d8 dexing...")
    class_files = []
    for root, _, files in os.walk(obj_dir):
        for f in files:
            if f.endswith(".class"):
                class_files.append(os.path.join(root, f))
                
    cmd_d8 = [D8, "--lib", PLATFORM_JAR, "--output", dex_dir] + class_files
    subprocess.run(cmd_d8, check=True)
    
    subprocess.run(["zip", "-uj", unaligned_apk, f"{dex_dir}/classes.dex"], check=True)
    
    # 5. Zipalign
    aligned_apk = f"{base_dir}/aligned.apk"
    print("  5/6. zipalign...")
    subprocess.run([ZIPALIGN, "-f", "-p", "4", unaligned_apk, aligned_apk], check=True)
    
    # 6. Apksigner
    print("  6/6. apksigner...")
    if not os.path.exists(KEYSTORE_PATH):
        subprocess.run([
            "keytool", "-genkeypair", "-v",
            "-keystore", KEYSTORE_PATH,
            "-storepass", "android",
            "-alias", "thaker",
            "-keypass", "android",
            "-keyalg", "RSA",
            "-keysize", "2048",
            "-validity", "10000",
            "-dname", "CN=Thaker,OU=Education,O=Yemen,C=YE"
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    signed_apk = f"{base_dir}/Thaker_signed.apk"
    cmd_sign = [
        APKSIGNER, "sign",
        "--v1-signing-enabled", "true",
        "--v2-signing-enabled", "true",
        "--v3-signing-enabled", "true",
        "--ks", KEYSTORE_PATH,
        "--ks-pass", "pass:android",
        "--key-pass", "pass:android",
        "--out", signed_apk,
        aligned_apk
    ]
    subprocess.run(cmd_sign, check=True)
    
    # Copy final APKs
    shutil.copy2(signed_apk, FINAL_APK_EN)
    shutil.copy2(signed_apk, FINAL_APK_AR)
    
    # Copy source project for user access
    project_source_dest = f"{WORKSPACE}/thaker-android-src"
    if os.path.exists(project_source_dest):
        shutil.rmtree(project_source_dest)
    shutil.copytree(base_dir, project_source_dest, ignore=shutil.ignore_patterns("*.zip", "*.apk", "obj", "dex", "compiled_res.zip"))
    
    size_mb = os.path.getsize(FINAL_APK_EN) / (1024 * 1024)
    print(f"\n🎉 SUCCESS! Generated APK files with complete 9th grade curriculum:")
    print(f"  -> {FINAL_APK_EN} ({size_mb:.2f} MB)")
    print(f"  -> {FINAL_APK_AR} ({size_mb:.2f} MB)")
    print(f"  -> Source code saved to: {project_source_dest}")

def main():
    print("=== Building 'ذاكر' (Thaker) Android APK - Complete High School & Middle School ===")
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    os.makedirs(BUILD_DIR, exist_ok=True)
    
    make_icons(f"{BUILD_DIR}/res")
    make_subject_illustrations(f"{BUILD_DIR}/res")
    write_resources(BUILD_DIR)
    apply_design_tokens(BUILD_DIR)
    write_java_sources(BUILD_DIR)
    prune_unused_drawables(BUILD_DIR)
    copy_assets(BUILD_DIR)
    compile_and_package(BUILD_DIR)

if __name__ == "__main__":
    main()
