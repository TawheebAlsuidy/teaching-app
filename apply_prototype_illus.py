#!/usr/bin/env python3
"""
Script to update build_apk.py with the exact prototype design from prototipe.for.image.png
"""
import sys
import re

BUILD_APK_PATH = "/mnt/sdcard/projects/teaching-app/build_apk.py"

with open(BUILD_APK_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. NEW make_subject_illustrations
new_illustrations_func = '''def make_subject_illustrations(res_dir):
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
'''

# Find make_subject_illustrations and replace it
pattern_illus = re.compile(r'def make_subject_illustrations\(res_dir\):.*?(?=def apply_design_tokens)', re.DOTALL)
if pattern_illus.search(content):
    content = pattern_illus.sub(new_illustrations_func + "\n\n", content)
    print("✓ Replaced make_subject_illustrations successfully.")
else:
    print("Warning: Could not match make_subject_illustrations pattern!")

with open(BUILD_APK_PATH, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated illustrations function.")
