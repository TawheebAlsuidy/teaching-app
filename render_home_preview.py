#!/usr/bin/env python3
"""
Render a visual mockup comparison of the enhanced Android Home Screen layout.
"""
import os
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image, ImageDraw, ImageFont

def reshape(text):
    return get_display(arabic_reshaper.reshape(text))

def render_home(out_path='/tmp/app_home_preview.png'):
    W, H = 390, 844
    img = Image.new('RGB', (W, H), (245, 250, 247))
    d = ImageDraw.Draw(img)

    # Fonts
    f_bold = ImageFont.truetype('/tmp/Tajawal-Bold.ttf', 16)
    f_title = ImageFont.truetype('/tmp/Tajawal-Bold.ttf', 20)
    f_brand = ImageFont.truetype('/tmp/Tajawal-Bold.ttf', 22)
    f_med = ImageFont.truetype('/tmp/Tajawal-Medium.ttf', 13)
    f_small = ImageFont.truetype('/tmp/Tajawal-Medium.ttf', 10)
    f_badge = ImageFont.truetype('/tmp/Tajawal-Bold.ttf', 11)

    # 1. Top soft mint wave
    for y in range(160):
        alpha = int(28 * (1 - y/160))
        d.line([(0, y), (W, y)], fill=(245 - alpha, 250 - alpha//2, 247 - alpha))

    # 2. Top Header Bar
    # Profile button (right in LTR / left side in RTL display)
    d.rounded_rectangle([20, 20, 66, 66], radius=14, fill=(255, 255, 255), outline=(226, 240, 231), width=1)
    # Green profile icon placeholder
    d.ellipse([34, 30, 52, 48], fill=(0, 168, 89))
    d.ellipse([27, 48, 59, 66], fill=(0, 168, 89))

    # Center Brand: Logo + ذاكر + منصتك التعليمية الشاملة
    # Logo cap
    d.polygon([(W//2 - 20, 32), (W//2, 24), (W//2 + 20, 32), (W//2, 40)], fill=(0, 168, 89))
    d.text((W//2 + 26, 22), reshape("ذاكر"), fill=(15, 23, 42), font=f_brand)
    d.text((W//2 - 58, 48), reshape("منصتك التعليمية الشاملة"), fill=(100, 116, 139), font=f_small)

    # Notification button (left in LTR / right in RTL)
    d.rounded_rectangle([W - 66, 20, W - 20, 66], radius=14, fill=(255, 255, 255), outline=(226, 240, 231), width=1)
    # Bell icon
    d.text((W - 51, 31), "🔔", font=f_bold)
    # Green notification badge dot
    d.ellipse([W - 32, 26, W - 24, 34], fill=(0, 168, 89))

    # 3. Hero Card (Top Featured Banner)
    hc_left, hc_top, hc_right, hc_bottom = 18, 80, W - 18, 220
    d.rounded_rectangle([hc_left, hc_top, hc_right, hc_bottom], radius=24, fill=(255, 255, 255), outline=(226, 242, 233), width=1)

    # Chemistry Illustration on the left
    hero_illus_path = "/mnt/sdcard/projects/teaching-app/thaker-android-src/res/drawable-nodpi/illustration_hero_lab.png"
    if os.path.exists(hero_illus_path):
        h_img = Image.open(hero_illus_path).convert("RGBA").resize((110, 110), Image.LANCZOS)
        img.paste(h_img, (hc_left + 10, hc_top + 15), h_img)

    # Right Content inside Hero Card
    # Badge: ⚗️ الكيمياء
    d.rounded_rectangle([hc_right - 96, hc_top + 16, hc_right - 14, hc_top + 40], radius=12, fill=(232, 248, 240))
    d.text((hc_right - 88, hc_top + 20), reshape("⚗️ الكيمياء"), fill=(0, 168, 89), font=f_badge)

    # Title: كتاب ومعمل الكيمياء
    d.text((hc_right - 180, hc_top + 48), reshape("كتاب ومعمل الكيمياء"), fill=(15, 23, 42), font=f_bold)
    # Subtitle: الثالث الثانوي • المنهج اليمني
    d.text((hc_right - 170, hc_top + 74), reshape("الثالث الثانوي • المنهج اليمني"), fill=(100, 116, 139), font=f_small)

    # 3 Feature Pills
    pills = [("✓ شرح تفاعلي", 76), ("✓ تجارب افتراضية", 82), ("✓ بدون اتصال", 68)]
    px = hc_right - 14
    for ptext, pw in pills:
        px -= pw
        d.rounded_rectangle([px, hc_top + 98, px + pw - 4, hc_top + 120], radius=10, fill=(237, 251, 244))
        d.text((px + 5, hc_top + 102), reshape(ptext), fill=(5, 150, 105), font=f_small)

    # 4. Stage Switcher (Segmented Tabs)
    st_top = hc_bottom + 14
    st_bottom = st_top + 48
    d.rounded_rectangle([18, st_top, W - 18, st_bottom], radius=24, fill=(238, 248, 243), outline=(226, 240, 231), width=1)
    # الثانوية (Selected)
    d.rounded_rectangle([W//2, st_top + 3, W - 21, st_bottom - 3], radius=21, fill=(0, 168, 89))
    d.text((W//2 + 36, st_top + 13), reshape("الثانوية  📚"), fill=(255, 255, 255), font=f_bold)
    # الإعدادية (Unselected)
    d.text((56, st_top + 13), reshape("الإعدادية  🎓"), fill=(15, 23, 42), font=f_bold)

    # 5. Section Header: الكتب الدراسية
    sh_y = st_bottom + 16
    d.text((W - 46, sh_y), "📖", font=f_title)
    d.text((W - 145, sh_y), reshape("الكتب الدراسية"), fill=(15, 23, 42), font=f_title)
    d.text((W - 175, sh_y + 24), reshape("اختر المادة التي تريد دراستها"), fill=(100, 116, 139), font=f_small)

    # 6. Featured Book & Interactive Lab Card
    fc_top = sh_y + 48
    fc_bottom = fc_top + 165
    d.rounded_rectangle([18, fc_top, W - 18, fc_bottom], radius=24, fill=(255, 255, 255), outline=(226, 242, 233), width=1)
    # Bookmark ribbon
    d.polygon([(W - 48, fc_top), (W - 30, fc_top), (W - 30, fc_top + 28), (W - 39, fc_top + 22), (W - 48, fc_top + 28)], fill=(0, 168, 89))

    # Featured visual
    feat_illus_path = "/mnt/sdcard/projects/teaching-app/thaker-android-src/res/drawable-nodpi/illustration_featured_lab.png"
    if os.path.exists(feat_illus_path):
        f_img = Image.open(feat_illus_path).convert("RGBA").resize((115, 100), Image.LANCZOS)
        img.paste(f_img, (26, fc_top + 10), f_img)

    # Right titles
    d.text((W - 195, fc_top + 16), reshape("كتاب ومعمل الكيمياء"), fill=(15, 23, 42), font=f_bold)
    d.text((W - 185, fc_top + 38), reshape("الثالث الثانوي • المنهج اليمني"), fill=(100, 116, 139), font=f_small)

    # Action Button: فتح المعمل ▶
    btn_top = fc_top + 60
    btn_box = [W - 200, btn_top, W - 32, btn_top + 40]
    d.rounded_rectangle(btn_box, radius=20, fill=(0, 168, 89))
    d.text((W - 146, btn_top + 11), reshape("فتح المعمل  ▶"), fill=(255, 255, 255), font=f_bold)

    # Auto Launch Switch row
    sw_top = fc_top + 114
    d.rounded_rectangle([28, sw_top, W - 28, sw_top + 38], radius=12, fill=(237, 248, 243))
    d.text((W - 195, sw_top + 11), reshape("فتح المعمل عند تشغيل التطبيق"), fill=(15, 23, 42), font=f_small)
    # Green toggle switch on left
    d.rounded_rectangle([38, sw_top + 9, 74, sw_top + 29], radius=10, fill=(0, 168, 89))
    d.ellipse([54, sw_top + 10, 72, sw_top + 28], fill=(255, 255, 255))

    # 7. Subject Cards (الفيزياء & الأحياء)
    # Physics Card
    phy_top = fc_bottom + 12
    d.rounded_rectangle([18, phy_top, W - 18, phy_top + 64], radius=16, fill=(255, 255, 255), outline=(230, 240, 235), width=1)
    d.rounded_rectangle([W - 68, phy_top + 8, W - 26, phy_top + 54], radius=12, fill=(224, 242, 254))
    d.text((W - 55, phy_top + 16), "⚛️", font=f_bold)
    d.text((W - 130, phy_top + 12), reshape("الفيزياء"), fill=(15, 23, 42), font=f_bold)
    d.text((W - 120, phy_top + 36), reshape("بصريات"), fill=(100, 116, 139), font=f_small)
    d.text((32, phy_top + 20), "❮", fill=(148, 163, 184), font=f_bold)

    # Biology Card
    bio_top = phy_top + 72
    d.rounded_rectangle([18, bio_top, W - 18, bio_top + 64], radius=16, fill=(255, 255, 255), outline=(230, 240, 235), width=1)
    d.rounded_rectangle([W - 68, bio_top + 8, W - 26, bio_top + 54], radius=12, fill=(243, 232, 255))
    d.text((W - 55, bio_top + 16), "🧬", font=f_bold)
    d.text((W - 130, bio_top + 12), reshape("الأحياء"), fill=(15, 23, 42), font=f_bold)
    d.text((W - 124, bio_top + 36), reshape("مجسمات"), fill=(100, 116, 139), font=f_small)
    d.text((32, bio_top + 20), "❮", fill=(148, 163, 184), font=f_bold)

    # 8. Bottom Navigation Dock Bar (Matches Prototype exactly)
    nav_h = 66
    nav_top = H - nav_h - 14
    d.rounded_rectangle([14, nav_top, W - 14, nav_top + nav_h], radius=28, fill=(255, 255, 255), outline=(226, 240, 231), width=1)

    # Elevated Green Home FAB in center
    fab_cx = W // 2
    # Glow halo
    d.ellipse([fab_cx - 28, nav_top - 2, fab_cx + 28, nav_top + 54], fill=(0, 168, 89, 40))
    d.ellipse([fab_cx - 24, nav_top + 2, fab_cx + 24, nav_top + 50], fill=(0, 168, 89))
    d.text((fab_cx - 9, nav_top + 13), "🏠", font=f_bold)
    d.text((fab_cx - 16, nav_top + 48), reshape("الرئيسية"), fill=(0, 168, 89), font=f_small)

    # Other nav icons
    # Right side: موادي + المكتبة
    d.text((W - 65, nav_top + 14), "🎓", font=f_bold)
    d.text((W - 70, nav_top + 40), reshape("موادي"), fill=(100, 116, 139), font=f_small)

    d.text((W - 125, nav_top + 14), "📥", font=f_bold)
    d.text((W - 132, nav_top + 40), reshape("المكتبة"), fill=(100, 116, 139), font=f_small)

    # Left side: المفضلة + الإعدادات
    d.text((105, nav_top + 14), "🔖", font=f_bold)
    d.text((98, nav_top + 40), reshape("المفضلة"), fill=(100, 116, 139), font=f_small)

    d.text((45, nav_top + 14), "⚙️", font=f_bold)
    d.text((36, nav_top + 40), reshape("الإعدادات"), fill=(100, 116, 139), font=f_small)

    img.save(out_path, "PNG", quality=95)
    print(f"✓ Generated Home Preview: {out_path}")

render_home("/mnt/sdcard/projects/teaching-app/app_home_prototype_render.png")
render_home("/root/.gemini/antigravity-cli/brain/b2b09aa1-e682-4694-8051-911cc53119ce/app_home_prototype_render.png")
