#!/usr/bin/env python3
"""
V2 Crisp Flat-Vector Artwork & Launcher Icons for Thaker (ذاكر)
Matches mockups in /mnt/sdcard/تطبيق ذاكر (01-splash, 02-onboarding, 03-home, 04-subject)
"""
import os
import math
from PIL import Image, ImageDraw


def _antialias_save(img, out_path, target_size):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    if img.size != target_size:
        img = img.resize(target_size, Image.Resampling.LANCZOS)
    img.save(out_path, "PNG")


def _draw_rounded_rect(draw, xy, radius, fill, outline=None, width=0):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def _draw_open_book_sun(draw, s, book_color=(5, 150, 105, 255), sun_color=(245, 158, 11, 255)):
    """Draws rising golden sun + rays above an open emerald book on a normalized canvas of size s."""
    cx, cy = s * 0.5, s * 0.52

    # Subtle sunbeams behind rising sun
    beam_color = (16, 185, 129, 48)
    for deg in range(-70, 75, 28):
        rad = math.radians(deg - 90)
        x1 = cx + math.cos(rad) * (s * 0.14)
        y1 = (cy - s * 0.08) + math.sin(rad) * (s * 0.14)
        x2 = cx + math.cos(rad) * (s * 0.34)
        y2 = (cy - s * 0.08) + math.sin(rad) * (s * 0.34)
        draw.line([(x1, y1), (x2, y2)], fill=beam_color, width=max(2, int(s * 0.032)))

    # Rising Sun semicircle
    sun_r = s * 0.145
    sun_cy = cy - s * 0.075
    draw.ellipse(
        [cx - sun_r, sun_cy - sun_r, cx + sun_r, sun_cy + sun_r],
        fill=sun_color,
    )
    # Inner bright core highlight
    inner_r = sun_r * 0.62
    draw.ellipse(
        [cx - inner_r, sun_cy - inner_r, cx + inner_r, sun_cy + inner_r],
        fill=(252, 211, 77, 255),
    )

    # Open Book (two curved pages meeting cleanly at spine)
    top_y = cy - s * 0.04
    bot_y = cy + s * 0.25
    mid_top_y = cy + s * 0.02
    mid_bot_y = cy + s * 0.29

    # Left page polygon
    left_poly = [
        (cx - s * 0.025, mid_top_y),
        (cx - s * 0.30, top_y),
        (cx - s * 0.30, bot_y),
        (cx - s * 0.025, mid_bot_y),
    ]
    right_poly = [
        (cx + s * 0.025, mid_top_y),
        (cx + s * 0.30, top_y),
        (cx + s * 0.30, bot_y),
        (cx + s * 0.025, mid_bot_y),
    ]
    draw.polygon(left_poly, fill=book_color)
    draw.polygon(right_poly, fill=(4, 120, 87, 255))

    # Crisp page lines inside book
    line_col = (209, 250, 229, 220)
    lw = max(2, int(s * 0.018))
    for idx in range(3):
        frac = 0.26 + idx * 0.22
        ly1 = top_y + (bot_y - top_y) * frac
        ly2 = mid_top_y + (mid_bot_y - mid_top_y) * frac
        draw.line([(cx - s * 0.23, ly1), (cx - s * 0.07, ly2)], fill=line_col, width=lw)
        draw.line([(cx + s * 0.07, ly2), (cx + s * 0.23, ly1)], fill=line_col, width=lw)

    # Bottom curved spine cradle
    draw.line(
        [(cx - s * 0.31, bot_y + s * 0.02), (cx, mid_bot_y + s * 0.045), (cx + s * 0.31, bot_y + s * 0.02)],
        fill=(6, 78, 59, 255),
        width=max(3, int(s * 0.028)),
    )


def generate_v2_icons(res_dir):
    """Generates launcher mipmaps matching 01-splash emblem."""
    densities = {
        "mipmap-mdpi": 48,
        "mipmap-hdpi": 72,
        "mipmap-xhdpi": 96,
        "mipmap-xxhdpi": 144,
        "mipmap-xxxhdpi": 192,
    }
    base_sz = 512
    # Compose master 512x512 icon
    master = Image.new("RGBA", (base_sz, base_sz), (0, 0, 0, 0))
    d = ImageDraw.Draw(master)
    # Deep emerald background rounded squircle
    _draw_rounded_rect(d, [16, 16, base_sz - 16, base_sz - 16], 112, fill=(4, 120, 87, 255))
    # Inner crisp white card
    pad = 72
    _draw_rounded_rect(d, [pad, pad, base_sz - pad, base_sz - pad], 84, fill=(255, 255, 255, 255))
    # Draw open book & sun inside white card
    card_img = Image.new("RGBA", (base_sz, base_sz), (0, 0, 0, 0))
    _draw_open_book_sun(ImageDraw.Draw(card_img), base_sz)
    master = Image.alpha_composite(master, card_img)

    # Round variant
    round_master = Image.new("RGBA", (base_sz, base_sz), (0, 0, 0, 0))
    dr = ImageDraw.Draw(round_master)
    dr.ellipse([16, 16, base_sz - 16, base_sz - 16], fill=(4, 120, 87, 255))
    _draw_rounded_rect(dr, [pad + 8, pad + 8, base_sz - pad - 8, base_sz - pad - 8], 78, fill=(255, 255, 255, 255))
    round_master = Image.alpha_composite(round_master, card_img)

    for folder, px in densities.items():
        _antialias_save(master, f"{res_dir}/{folder}/ic_launcher.png", (px, px))
        _antialias_save(round_master, f"{res_dir}/{folder}/ic_launcher_round.png", (px, px))


def _make_splash_logo_card(out_path):
    s = 512
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Soft outer glow shadow
    _draw_rounded_rect(d, [22, 28, s - 22, s - 16], 110, fill=(6, 78, 59, 95))
    # Crisp white squircle card
    _draw_rounded_rect(d, [30, 24, s - 30, s - 36], 106, fill=(255, 255, 255, 255))
    _draw_open_book_sun(d, s)
    # Two gold sparkles
    for sx, sy, sr in [(s * 0.78, s * 0.24, 11), (s * 0.22, s * 0.29, 8)]:
        d.polygon(
            [(sx, sy - sr), (sx + sr * 0.35, sy), (sx, sy + sr), (sx - sr * 0.35, sy)],
            fill=(251, 191, 36, 255),
        )
        d.polygon(
            [(sx - sr, sy), (sx, sy - sr * 0.35), (sx + sr, sy), (sx, sy + sr * 0.35)],
            fill=(251, 191, 36, 255),
        )
    _antialias_save(img, out_path, (360, 360))


def _make_splash_rays(out_path):
    s = 720
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx, cy = s // 2, int(s * 0.36)
    for i in range(18):
        a0 = math.radians(i * 20)
        a1 = math.radians(i * 20 + 9)
        r = s * 0.75
        pts = [
            (cx, cy),
            (cx + math.cos(a0) * r, cy + math.sin(a0) * r),
            (cx + math.cos(a1) * r, cy + math.sin(a1) * r),
        ]
        d.polygon(pts, fill=(255, 255, 255, 16))
    # Subtle concentric glow ring
    d.ellipse([cx - 210, cy - 210, cx + 210, cy + 210], fill=(16, 185, 129, 26))
    _antialias_save(img, out_path, (640, 640))


def _make_mini_book_preview(out_path):
    w, h = 280, 340
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # Soft mint background card
    _draw_rounded_rect(d, [8, 12, w - 8, h - 8], 28, fill=(209, 250, 229, 255))
    # White textbook page inside
    _draw_rounded_rect(d, [26, 28, w - 26, h - 28], 20, fill=(255, 255, 255, 255), outline=(167, 243, 208, 255), width=4)
    # Green unit header strip
    _draw_rounded_rect(d, [46, 52, w - 46, 86], 10, fill=(5, 150, 105, 255))
    # Text skeleton lines
    for y in [108, 130]:
        _draw_rounded_rect(d, [50, y, w - 50, y + 12], 6, fill=(203, 213, 225, 255))
    # Mini diagram box with amber dot pin
    _draw_rounded_rect(d, [48, 162, w - 48, 268], 16, fill=(236, 253, 245, 255), outline=(110, 231, 183, 255), width=3)
    d.ellipse([108, 186, 172, 248], fill=(16, 185, 129, 90), outline=(5, 150, 105, 255), width=4)
    # Interactive sparkle hotspot dot
    d.ellipse([156, 176, 186, 206], fill=(245, 158, 11, 255), outline=(255, 255, 255, 255), width=4)
    # Page footer line
    _draw_rounded_rect(d, [96, 284, w - 96, 296], 6, fill=(148, 163, 184, 255))
    _antialias_save(img, out_path, (210, 255))


def _make_avatar_student(out_path):
    s = 256
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    _draw_rounded_rect(d, [8, 8, s - 8, s - 8], 58, fill=(16, 185, 129, 55))
    # Head
    d.ellipse([90, 68, 166, 144], fill=(255, 255, 255, 235))
    # Shoulders arc
    d.chord([54, 150, 202, 246], start=180, end=360, fill=(255, 255, 255, 235))
    # Gold mortarboard cap on top
    d.polygon([(128, 40), (186, 62), (128, 84), (70, 62)], fill=(251, 191, 36, 255))
    d.line([(182, 63), (182, 92)], fill=(245, 158, 11, 255), width=5)
    _antialias_save(img, out_path, (160, 160))


def _make_badge_icon(out_path, bg_rgba, kind):
    s = 256
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    _draw_rounded_rect(d, [12, 12, s - 12, s - 12], 56, fill=bg_rgba)

    if kind == "prep":
        # Coral Backpack
        _draw_rounded_rect(d, [84, 56, 172, 108], 24, fill=(0, 0, 0, 0), outline=(225, 29, 72, 255), width=12)
        _draw_rounded_rect(d, [68, 80, 188, 196], 30, fill=(244, 63, 94, 255))
        _draw_rounded_rect(d, [86, 126, 170, 182], 16, fill=(251, 113, 133, 255))
        _draw_rounded_rect(d, [96, 106, 160, 118], 6, fill=(254, 205, 211, 255))
    elif kind == "sec":
        # Indigo / Emerald Graduation Cap
        d.polygon([(128, 66), (204, 104), (128, 142), (52, 104)], fill=(5, 150, 105, 255))
        d.polygon([(82, 128), (128, 150), (174, 128), (174, 172), (128, 188), (82, 172)], fill=(4, 120, 87, 255))
        d.line([(194, 108), (194, 164)], fill=(245, 158, 11, 255), width=9)
        d.ellipse([184, 160, 204, 180], fill=(245, 158, 11, 255))
    elif kind == "science":
        # Emerald Lab Erlenmeyer Flask + Test Tube
        d.line([(106, 56), (150, 56)], fill=(4, 120, 87, 255), width=12)
        d.polygon([(112, 58), (144, 58), (186, 184), (70, 184)], fill=(16, 185, 129, 220))
        d.polygon([(88, 140), (168, 140), (186, 184), (70, 184)], fill=(5, 150, 105, 255))
        d.ellipse([104, 150, 120, 166], fill=(254, 243, 199, 255))
        d.ellipse([134, 158, 146, 170], fill=(255, 255, 255, 240))
        d.ellipse([120, 96, 134, 110], fill=(16, 185, 129, 200))
    elif kind == "math":
        # Set-Square Triangle Ruler + Compass Accent
        d.polygon([(72, 184), (192, 184), (72, 64)], fill=(2, 132, 199, 235))
        d.polygon([(94, 162), (138, 162), (94, 118)], fill=(254, 249, 231, 255))
        # Amber pencil overlay
        d.line([(140, 116), (192, 64)], fill=(245, 158, 11, 255), width=16)
        d.ellipse([130, 114, 148, 132], fill=(180, 83, 9, 255))
    elif kind == "physics":
        # Orbital Atom
        d.ellipse([112, 112, 144, 144], fill=(2, 132, 199, 255))
        d.arc([58, 98, 198, 158], start=0, end=360, fill=(14, 165, 233, 255), width=10)
        d.arc([98, 58, 158, 198], start=0, end=360, fill=(5, 150, 105, 255), width=10)
        d.ellipse([178, 116, 196, 134], fill=(245, 158, 11, 255))
    elif kind == "chem":
        # Benzene Hex + Drop
        pts = []
        for i in range(6):
            a = math.radians(i * 60)
            pts.append((128 + math.cos(a) * 58, 128 + math.sin(a) * 58))
        d.polygon(pts, outline=(5, 150, 105, 255), fill=(167, 243, 208, 180))
        d.ellipse([104, 104, 152, 152], outline=(4, 120, 87, 255), width=9)
        d.ellipse([166, 62, 192, 88], fill=(245, 158, 11, 255))
    elif kind == "bio":
        # Stylized DNA / Leaf
        d.chord([68, 70, 188, 190], start=210, end=30, fill=(16, 185, 129, 255))
        d.chord([68, 70, 188, 190], start=30, end=210, fill=(5, 150, 105, 255))
        d.line([(86, 170), (170, 86)], fill=(255, 255, 255, 240), width=8)
        d.ellipse([106, 98, 126, 118], fill=(254, 243, 199, 255))

    _antialias_save(img, out_path, (192, 192))


def generate_v2_artwork(res_dir):
    """Generates all V2 icons and UI illustrations into res/."""
    generate_v2_icons(res_dir)
    nodpi = f"{res_dir}/drawable-nodpi"
    _make_splash_logo_card(f"{nodpi}/logo_splash_card.png")
    _make_splash_rays(f"{nodpi}/splash_rays.png")
    _make_mini_book_preview(f"{nodpi}/mini_book_preview.png")
    _make_avatar_student(f"{nodpi}/avatar_student.png")
    _make_badge_icon(f"{nodpi}/ic_stage_prep.png", (255, 228, 230, 255), "prep")
    _make_badge_icon(f"{nodpi}/ic_stage_sec.png", (209, 250, 229, 255), "sec")
    _make_badge_icon(f"{nodpi}/ic_subj_science.png", (209, 250, 229, 255), "science")
    _make_badge_icon(f"{nodpi}/ic_subj_math.png", (254, 243, 199, 255), "math")
    _make_badge_icon(f"{nodpi}/ic_subj_physics.png", (224, 242, 254, 255), "physics")
    _make_badge_icon(f"{nodpi}/ic_subj_chem.png", (204, 251, 241, 255), "chem")
    _make_badge_icon(f"{nodpi}/ic_subj_bio.png", (220, 252, 231, 255), "bio")
