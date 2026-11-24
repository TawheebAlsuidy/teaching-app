#!/usr/bin/env python3
import os
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image, ImageDraw, ImageFont

def reshape(text):
    return get_display(arabic_reshaper.reshape(text))

def draw_rounded_rect(draw, bbox, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)

def render_quiz(theme='dark', out_path='quiz.png'):
    W, H = 390, 844
    img = Image.new('RGB', (W, H))
    draw = ImageDraw.Draw(img)

    # Fonts
    font_bold = ImageFont.truetype('/tmp/Tajawal-Bold.ttf', 16)
    font_title = ImageFont.truetype('/tmp/Tajawal-Bold.ttf', 18)
    font_med = ImageFont.truetype('/tmp/Tajawal-Medium.ttf', 14)
    font_small = ImageFont.truetype('/tmp/Tajawal-Medium.ttf', 12)
    font_math = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13)

    if theme == 'dark':
        bg_color = (20, 16, 12)
        modal_bg = (32, 26, 20)
        card_bg = (42, 34, 27)
        fg_color = (245, 237, 228)
        text_muted = (168, 152, 139)
        bd_color = (70, 58, 48)
        accent_color = (224, 120, 48)
        success_bg = (24, 60, 35)
        success_bd = (92, 184, 120)
        success_fg = (140, 230, 170)
        btn_exp_bg = (45, 32, 22)
        btn_exp_bd = (224, 120, 48)
    else: # light
        bg_color = (248, 246, 240)
        modal_bg = (255, 255, 255)
        card_bg = (243, 239, 230)
        fg_color = (44, 34, 30)
        text_muted = (125, 110, 101)
        bd_color = (215, 200, 185)
        accent_color = (194, 105, 40)
        success_bg = (232, 248, 238)
        success_bd = (74, 140, 94)
        success_fg = (35, 110, 55)
        btn_exp_bg = (250, 243, 235)
        btn_exp_bd = (194, 105, 40)

    # 1. Background (simulating app 3D lab background behind modal)
    draw.rectangle([0, 0, W, H], fill=bg_color)
    
    # Backdrop dim overlay
    overlay_fill = (0, 0, 0)
    # We can draw simulated 3D shelf behind
    for y in range(60, 200, 40):
        draw.line([20, y, W - 20, y], fill=(60, 50, 40) if theme == 'dark' else (220, 210, 200), width=1)

    # Modal window (mobile card style)
    m_left, m_top, m_right, m_bottom = 12, 45, W - 12, H - 40
    draw_rounded_rect(draw, (m_left, m_top, m_right, m_bottom), radius=16, fill=modal_bg, outline=bd_color, width=1)

    # Top modal bar
    # Close button (left)
    draw.text((m_left + 16, m_top + 14), "✕", fill=text_muted, font=font_title)
    
    # Title (center/right)
    title_txt = reshape("الوحدة 1: العناصر الانتقالية")
    draw.text((W - 200, m_top + 15), title_txt, fill=fg_color, font=font_title)

    # Score pill (right)
    draw_rounded_rect(draw, (W - 75, m_top + 14, W - 24, m_top + 36), radius=11, fill=card_bg, outline=bd_color)
    score_txt = reshape("1 / 3")
    draw.text((W - 62, m_top + 17), score_txt, fill=accent_color, font=font_bold)

    # Progress bar line
    bar_y = m_top + 50
    draw.line([m_left, bar_y, m_right, bar_y], fill=bd_color, width=2)
    draw.line([m_left, bar_y, m_left + (m_right - m_left) // 3, bar_y], fill=accent_color, width=3)

    # Question Box
    q_top = bar_y + 16
    q_bottom = q_top + 95
    draw_rounded_rect(draw, (m_left + 14, q_top, m_right - 14, q_bottom), radius=12, fill=card_bg, outline=bd_color)
    
    q_num = reshape("السؤال 1 من 3:")
    draw.text((m_right - 105, q_top + 10), q_num, fill=accent_color, font=font_small)
    
    q_line1 = reshape("ما هو لون الراسب المتكون عند إضافة NaOH")
    draw.text((m_right - 280, q_top + 32), q_line1, fill=fg_color, font=font_bold)
    q_line2 = reshape("إلى محلول يحتوي على أيونات الحديد (III)؟")
    draw.text((m_right - 265, q_top + 58), q_line2, fill=fg_color, font=font_bold)

    # Option choices (4 options)
    options = [
        ("أبيض مخضر", False, False),
        ("بني محمر جيلاتيني", True, True),   # Correct & chosen
        ("أزرق فاتح", False, False),
        ("أصفر باهت", False, False)
    ]

    opt_y = q_bottom + 14
    for opt_txt, is_correct, is_selected in options:
        opt_box = (m_left + 14, opt_y, m_right - 14, opt_y + 46)
        if is_selected and is_correct:
            draw_rounded_rect(draw, opt_box, radius=10, fill=success_bg, outline=success_bd, width=2)
            lbl = reshape(f"✓  {opt_txt}")
            draw.text((m_right - 170, opt_y + 12), lbl, fill=success_fg, font=font_bold)
        else:
            draw_rounded_rect(draw, opt_box, radius=10, fill=modal_bg, outline=bd_color, width=1)
            lbl = reshape(f"○  {opt_txt}")
            draw.text((m_right - 130, opt_y + 13), lbl, fill=fg_color, font=font_med)
        opt_y += 54

    # Explanation card
    exp_top = opt_y + 8
    exp_bottom = exp_top + 145
    draw_rounded_rect(draw, (m_left + 14, exp_top, m_right - 14, exp_bottom), radius=12, fill=card_bg, outline=bd_color)
    
    exp_header = reshape("💡 التفسير العلمي والتفاعل:")
    draw.text((m_right - 180, exp_top + 10), exp_header, fill=accent_color, font=font_bold)

    exp_desc = reshape("يترسب هيدروكسيد الحديد (III) ذو اللون البني المحمر:")
    draw.text((m_right - 295, exp_top + 34), exp_desc, fill=fg_color, font=font_med)
    
    eq_str = "Fe³⁺(aq) + 3OH⁻(aq)  ➔  Fe(OH)₃(s) ↓"
    draw.text((m_left + 45, exp_top + 58), eq_str, fill=fg_color, font=font_math)

    # "Review Experiment" button inside explanation
    btn_exp_box = (m_left + 26, exp_top + 92, m_right - 26, exp_top + 130)
    draw_rounded_rect(draw, btn_exp_box, radius=8, fill=btn_exp_bg, outline=btn_exp_bd, width=1)
    btn_exp_txt = reshape("⚗️  راجع التجربة في المعمل والكتاب المدرسي")
    draw.text((m_left + 42, exp_top + 102), btn_exp_txt, fill=accent_color, font=font_bold)

    # Footer navigation button: "Next Question"
    btn_next_top = exp_bottom + 16
    btn_next_box = (m_left + 14, btn_next_top, m_right - 14, btn_next_top + 46)
    draw_rounded_rect(draw, btn_next_box, radius=10, fill=accent_color)
    next_txt = reshape("السؤال التالي  ➔")
    draw.text((W // 2 - 45, btn_next_top + 12), next_txt, fill=(255, 255, 255), font=font_bold)

    # Theme badge in top right for visual reference
    badge_txt = reshape("الوضع الداكن" if theme == 'dark' else "الوضع الفاتح")
    draw_rounded_rect(draw, (18, 12, 115, 34), radius=6, fill=modal_bg, outline=bd_color)
    draw.text((28, 16), badge_txt, fill=text_muted, font=font_small)

    img.save(out_path, format="PNG", quality=95)
    print(f"✓ Rendered {theme} mode screenshot: {out_path}")

if __name__ == '__main__':
    shots_dir = "/mnt/sdcard/projects/teaching-app/chem-lab/screenshots"
    brain_dir = "/root/.gemini/antigravity-cli/brain/b2b09aa1-e682-4694-8051-911cc53119ce/screenshots"
    
    for theme in ['light', 'dark']:
        out1 = os.path.join(shots_dir, f"quiz_modal_{theme}.png")
        out2 = os.path.join(brain_dir, f"quiz_modal_{theme}.png")
        render_quiz(theme, out1)
        render_quiz(theme, out2)
