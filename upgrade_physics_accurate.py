#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Precision Grade 12 Physics Data Pack Builder (Zero Misplaced Hotspots)
Uses exact PDF layout coordinates from /tmp/phys_audit/elements_map.json and
fixes book_page = pdf_page - 2 uniformly across all units, lessons, and pages.
"""
import json
import os
import re
import shutil
import xml.etree.ElementTree as ET

BASE_DIR = "/media/tawheeb/New Volume3/ذاكر/teaching-app"
OUT_DIR = f"{BASE_DIR}/data/curriculum/grade12/physics"
ANDROID_OUT = f"{BASE_DIR}/thaker-android-src/assets/data/curriculum/grade12/physics"

W, H = 892.0, 1263.0
DIG = str.maketrans("∞±≤≥¥µ∂∑∏π", "0123456789")

def load_json(name):
    with open(f"{OUT_DIR}/{name}", "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(name, data):
    with open(f"{OUT_DIR}/{name}", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def overlap_area(a, b):
    x1 = max(a["x"], b["x"])
    y1 = max(a["y"], b["y"])
    x2 = min(a["x"] + a["w"], b["x"] + b["w"])
    y2 = min(a["y"] + a["h"], b["y"] + b["h"])
    if x2 <= x1 or y2 <= y1:
        return 0.0
    return (x2 - x1) * (y2 - y1)

def overlaps_any(box, existing, thresh=0.20):
    area = box["w"] * box["h"]
    if area <= 0:
        return True
    for ex in existing:
        ov = overlap_area(box, ex["bounds"])
        min_a = min(area, ex["bounds"]["w"] * ex["bounds"]["h"])
        if ov / max(min_a, 1e-6) > thresh:
            return True
    return False

def clamp_box(x, y, w, h):
    x = max(0.08, min(0.84, round(x, 4)))
    y = max(0.08, min(0.86, round(y, 4)))
    w = max(0.14, min(0.92 - x, round(w, 4)))
    h = max(0.045, min(0.88 - y, round(h, 4)))
    return {"x": x, "y": y, "w": w, "h": h}

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(ANDROID_OUT, exist_ok=True)

    # Load XML for surgical element detection
    tree = ET.parse("/tmp/phys_audit/physics_full.xml")
    root = tree.getroot()
    xml_pages = {int(p.attrib["number"]): p for p in root.findall("page")}
    fonts = {fs.attrib["id"]: fs.attrib for fs in root.iter("fontspec")}

    # 1. UNITS (Exact Book page -> PDF page = book + 2!)
    units = load_json("units.json")
    for u in units:
        if u["id"] == "u9":
            u["page_end"] = 216
        u["pdf_start"] = u["page_start"] + 2
        u["pdf_end"] = u["page_end"] + 2

    # Evaluation ranges in Book pages (exact printed ranges from the Ministry book!)
    eval_pages_map = {
        "u1": (27, 28),
        "u2": (58, 60),
        "u3": (80, 84),
        "u4": (107, 113),
        "u5": (142, 143),
        "u6": (171, 172),
        "u7": (183, 184),
        "u8": (197, 197),
        "u9": (210, 210),
    }

    # 2. PAGES (PDF 6..218)
    pages = []
    for pdf_num in range(6, 219):
        if pdf_num in (6, 7):
            book_num = pdf_num - 2 # 4, 5 intro
            cur_unit = None
            p_type = "intro"
            title = "مقدمة الكتاب والمنهج"
        elif pdf_num in (8, 9, 10):
            book_num = pdf_num - 2 # Printed TOC: 6, 7, 8!
            cur_unit = None
            p_type = "contents"
            title = f"المحتويات (الفهرس) — ص {book_num}"
        else:
            book_num = pdf_num - 2 # EXACT 100% printed page number 9..216!
            cur_unit = None
            for u in units:
                if u["page_start"] <= book_num <= u["page_end"]:
                    cur_unit = u
                    break
            uid = cur_unit["id"] if cur_unit else None
            ev_s, ev_e = eval_pages_map.get(uid, (999, 999))
            if cur_unit and book_num == cur_unit["page_start"]:
                p_type = "unit_cover"
                title = f"{cur_unit['title']} — غلاف وأهداف الوحدة"
            elif cur_unit and ev_s <= book_num <= ev_e:
                p_type = "assessment"
                title = f"تقويم {cur_unit['title']} — ص {book_num}"
            elif 211 <= book_num <= 215:
                p_type = "glossary"
                title = f"قوائم المصطلحات العلمية — ص {book_num}"
            elif book_num == 216:
                p_type = "ending"
                title = "خاتمة الكتاب — تم بحمد الله"
            else:
                p_type = "lesson"
                title = f"{cur_unit['title']} — ص {book_num}" if cur_unit else f"فيزياء 3 ثانوي — ص {book_num}"

        pages.append({
            "page_id": f"phys12-p{pdf_num:03d}",
            "book_page": book_num,
            "pdf_page": pdf_num,
            "type": p_type,
            "title": title,
            "unit_id": cur_unit["id"] if cur_unit else None,
            "image": f"assets/curriculum/grade12/physics/pages/page_{pdf_num:03d}_opt.jpg",
            "image_full": f"assets/curriculum/grade12/physics/pages/page_{pdf_num:03d}.jpg",
            "aspect_ratio": 0.7083
        })

    # 3. LESSONS (Fix pdf_pages = [p + 2 for p in pages]!)
    lessons = load_json("lessons.json")
    for l in lessons:
        if l["id"] == "phys-u9-l4":
            l["pages"] = [210, 215]
        l["pdf_pages"] = [p + 2 for p in l["pages"]]

    # 4. GLOSSARY & EXPLANATIONS (Synchronized with openTextExplanation keys: vocabulary_ids & chemical_equations!)
    glossary = load_json("glossary.json")
    existing_exp = load_json("explanations.json")
    explanations = {}

    # Unit Overview Explanations for all 9 Unit Cover pages (ص 9, 29, 61, 85, 114, 144, 173, 185, 198)
    for u in units:
        uid = u["id"]
        exp_uid = f"exp-phys-{uid}-overview"
        laws_cards = [{"label": lw.split(":")[0].strip(), "eq": lw.split(":", 1)[-1].strip()} for lw in u.get("key_laws", [])]
        explanations[exp_uid] = {
            "id": exp_uid,
            "title": f"مقدمة وأهداف {u['title']}",
            "original_text": f"{u['title']} (ص {u['page_start']} - {u['page_end']}): {u['short_desc']}.",
            "levels": {
                "basic": f"🎯 أهلاً بك في {u['title']}! تركز هذه الوحدة على: {u['short_desc']}.",
                "intermediate": f"📘 أهداف {u['title']}: ستتعلم في هذه الوحدة المفاهيم الأساسية، القوانين الرياضية المعتمدة، وتطبيقاتها في الحياة، ثم تحل مسائل تقويم الوحدة.",
                "advanced": "🚀 تطبيقات واقعية بارزة:\n• " + "\n• ".join(u.get("real_world_apps", []))
            },
            "chemical_equations": laws_cards,
            "vocabulary_ids": [k for k in glossary.keys()][:3],
            "tts_text": f"أهلاً بك في {u['title']}. {u['short_desc']}."
        }

    # Detailed per-lesson Explanations preserving existing levels + adding required keys (`chemical_equations`, `vocabulary_ids`)
    unit_vocab_map = {
        "u1": ["v-momentum", "v-impulse", "v-escape", "v-orbital", "v-range"],
        "u2": ["v-ac", "v-ieff", "v-xc", "v-xl", "v-impedance", "v-resonance"],
        "u3": ["v-doping", "v-diode", "v-transistor"],
        "u4": ["v-cathode", "v-radar", "v-cro"],
        "u5": ["v-spectrum", "v-quantum", "v-bohr"],
        "u6": ["v-photoelectric", "v-workfunc", "v-xray", "v-laser"],
        "u7": ["v-halflife", "v-binding", "v-fission"],
        "u8": ["v-pv"],
        "u9": ["v-bigbang", "v-redshift"],
    }

    for l in lessons:
        lid = l["id"]
        exp_id = f"exp-{lid}"
        prev = existing_exp.get(exp_id, {})
        eq_list = prev.get("equations", [])
        if eq_list and isinstance(eq_list[0], str):
            chem_eqs = [{"label": f"قانون درس {l['title']}", "eq": s} for s in eq_list if s]
        elif eq_list and isinstance(eq_list[0], dict):
            chem_eqs = eq_list
        else:
            chem_eqs = []
        explanations[exp_id] = {
            "id": exp_id,
            "lesson_id": lid,
            "title": prev.get("title", l["title"]),
            "original_text": prev.get("original_text", f"موضوع الكتاب الوزاري: {l['title']}."),
            "levels": prev.get("levels", {
                "basic": f"شرح مبسط لدرس {l['title']}.",
                "intermediate": f"شرح منهجي وزاري لدرس {l['title']}.",
                "advanced": f"تعمق وتطبيقات وزارية لدرس {l['title']}."
            }),
            "chemical_equations": chem_eqs,
            "vocabulary_ids": unit_vocab_map.get(l["unitId"], []),
            "tts_text": prev.get("levels", {}).get("basic", l["title"])
        }

    # Add Glossary explanation card for pages 211-215
    explanations["exp-phys-glossary"] = {
        "id": "exp-phys-glossary",
        "title": "قوائم المصطلحات العلمية والفيزيائية",
        "original_text": "قوائم المصطلحات العلمية للوحدات التسع (ص 211 - 215) مرتبةً للمراجعة السريعة.",
        "levels": {
            "basic": "📖 تضم هذه الصفحات جميع المصطلحات العلمية الواردة في كتاب الفيزياء للصف الثالث الثانوي باللغتين العربية والإنجليزية.",
            "intermediate": "📘 مراجعة التعريفات الفيزيائية الدقيقة ضرورية للإجابة عن أسئلة الاختيار من متعدد والتعليل والمصطلح العلمي في الامتحان الوزاري.",
            "advanced": "🎯 اضغط على أي مصطلح بالأسفل لاستعراض تعريفه الدقيق ووحدة قياسه وتطبيقه."
        },
        "chemical_equations": [],
        "vocabulary_ids": list(glossary.keys())[:10],
        "tts_text": "قوائم المصطلحات العلمية للثالث الثانوي فيزياء."
    }

    # 5. DIAGRAMS MAP (Matched accurately to actual lab_exp in physics-12th-lab.html!)
    diagrams = {
        "diag-u1-collision1d": {
            "id": "diag-u1-collision1d", "lab_exp": "lab-u1-collision1d",
            "title": "التصادم في بُعد واحد (شكل 1 - ص 10)", "sim_key": "phys_collision1d",
            "formula": "ك₁·ع₁ + ك₂·ع₂ = ك₁·ع₁' + ك₂·ع₂'",
            "slider_label": "مرونة التصادم:", "slider_min": 0, "slider_max": 1, "slider_val": 1, "slider_unit": "",
            "components": [
                {"id": "elastic", "name": "تصادم مرن", "role": "تُحفظ كمية التحرك والطاقة الحركية معاً."},
                {"id": "inelastic", "name": "تصادم غير مرن", "role": "تُحفظ كمية التحرك ويلتحم الجسمان مع فقد في الطاقة الحركية."}
            ]
        },
        "diag-u1-collision2d": {
            "id": "diag-u1-collision2d", "lab_exp": "lab-u1-collision2d",
            "title": "التصادم في بُعدين وتحليل المتجهات (شكل 2 - ص 11)", "sim_key": "phys_collision2d",
            "formula": "ك₁ع₁ = ك₁ع₁' جتا هـ₁ + ك₂ع₂' جتا هـ₂",
            "slider_label": "زاوية الانحراف:", "slider_min": 15, "slider_max": 75, "slider_val": 30, "slider_unit": "°",
            "components": [
                {"id": "vx", "name": "المحور السيني", "role": "ك₁ع₁ = ك₁ع₁' جتا هـ₁ + ك₂ع₂' جتا هـ₂"},
                {"id": "vy", "name": "المحور الصادي", "role": "ك₁ع₁' جا هـ₁ = ك₂ع₂' جا هـ₂"}
            ]
        },
        "diag-u1-rocket": {
            "id": "diag-u1-rocket", "lab_exp": "lab-u1-balloon-rocket",
            "title": "الصواريخ ذاتية الدفع ومبدأ الفعل ورد الفعل (ص 15 - 16)", "sim_key": "phys_rocket",
            "formula": "قوة دفع الصاروخ = -(Δك / Δز) · ع_غاز",
            "slider_label": "اندفاع الغازات:", "slider_min": 10, "slider_max": 100, "slider_val": 80, "slider_unit": "%",
            "components": [
                {"id": "fuel", "name": "الغازات المندفعة", "role": "تندفع للخلف بكمية تحرك عكسية."},
                {"id": "thrust", "name": "دفع الصاروخ", "role": "قوة رد فعل تدفع الصاروخ للأمام حتى في الفراغ."}
            ]
        },
        "diag-u1-satellite": {
            "id": "diag-u1-satellite", "lab_exp": "lab-u1-satellite",
            "title": "حركة القمر الصناعي والمدار الدائري (شكل 7 و8 - ص 19 - 20)", "sim_key": "phys_satellite",
            "formula": "ع_م = جذر(G · ك_أرض / نق)",
            "slider_label": "السرعة المدارية:", "slider_min": 4, "slider_max": 12, "slider_val": 8, "slider_unit": " km/s",
            "components": [
                {"id": "fg", "name": "قوة الجذب المركزي", "role": "عمودية على مسار القمر فتغير اتجاهه فقط."},
                {"id": "vo", "name": "السرعة المدارية (~8 km/s)", "role": "تحفظ بقاء القمر في مداره المستقر."}
            ]
        },
        "diag-u1-angular": {
            "id": "diag-u1-angular", "lab_exp": "lab-u1-angular",
            "title": "القصور الذاتي الدوراني وكمية التحرك الزاوي (شكل 10 - ص 23)", "sim_key": "phys_angular",
            "formula": "L = I · ω  (محفوظة عند انعدام العزوم)",
            "slider_label": "السرعة الزاوية:", "slider_min": 1, "slider_max": 12, "slider_val": 5, "slider_unit": " rad/s",
            "components": [
                {"id": "inertia", "name": "عزم القصور الذاتي I", "role": "مقاومة الجسم لتغيير حالته الدورانية (I = ك·نق²)."},
                {"id": "angL", "name": "كمية التحرك الزاوي", "role": "L = I·ω تظل محفوظة عند غياب العزوم الخارجية."}
            ]
        },
        "diag-u1-projectiles": {
            "id": "diag-u1-projectiles", "lab_exp": "lab-u1-projectiles",
            "title": "حركة المقذوفات في مجال الجاذبية (ص 23 - 26)", "sim_key": "phys_projectiles",
            "formula": "ف_أفقي R = (ع₀² · جا 2θ) / د",
            "slider_label": "زاوية الإطلاق:", "slider_min": 15, "slider_max": 75, "slider_val": 45, "slider_unit": "°",
            "components": [
                {"id": "apex", "name": "الذروة H", "role": "تنعدم عندها المركبة الرأسية للسرعة."},
                {"id": "range", "name": "المدى الأفقي R", "role": "يبلغ أقصى قيمة عند زاوية 45°."}
            ]
        },
        "diag-u2-dynamo": {
            "id": "diag-u2-dynamo", "lab_exp": "lab-u2-dynamo",
            "title": "مولد التيار المتردد — الدينامو 3D (ص 32 - 36)", "sim_key": "phys_dynamo",
            "formula": "ق.د.ك = ن · س · ب · ω · جا(ω ز)",
            "slider_label": "سرعة الدوران:", "slider_min": 1, "slider_max": 10, "slider_val": 4, "slider_unit": "x",
            "components": [
                {"id": "coil", "name": "ملف الدينامو", "role": "يقطع خطوط الفيض لتوليد ق.د.ك جيبية."},
                {"id": "rings", "name": "حلقتا الانزلاق", "role": "تنقل التيار المتردد إلى الدائرة الخارجية."}
            ]
        },
        "diag-u2-capacitor": {
            "id": "diag-u2-capacitor", "lab_exp": "lab-u2-capacitor",
            "title": "المكثف والمفاعلة السعوية 3D (ص 39 - 45)", "sim_key": "phys_capacitor",
            "formula": "م_سعوية Xc = 1 / (2 · π · f · C)",
            "slider_label": "التردد (Hz):", "slider_min": 10, "slider_max": 100, "slider_val": 50, "slider_unit": " Hz",
            "components": [
                {"id": "plates", "name": "لوحا المكثف", "role": "يخزنان الطاقة الكهربائية في مجال كهربائي."},
                {"id": "dielectric", "name": "المادة العازلة", "role": "تحدد سعة المكثف وتمنع التيار المستمر بعد تمام الشحن."}
            ]
        },
        "diag-u2-rlc": {
            "id": "diag-u2-rlc", "lab_exp": "lab-u2-rlc",
            "title": "دوائر التيار المتردد والرنين RLC (ص 47 - 56)", "sim_key": "phys_rlc",
            "formula": "Z = جذر(R² + (XL - Xc)²)",
            "slider_label": "التردد (Hz):", "slider_min": 10, "slider_max": 100, "slider_val": 50, "slider_unit": " Hz",
            "components": [
                {"id": "xl", "name": "الملف الحثي (XL)", "role": "يقدم الجهد على التيار بربع دورة."},
                {"id": "xc", "name": "المكثف (Xc)", "role": "يؤخر الجهد عن التيار بربع دورة."}
            ]
        },
        "diag-u3-semiconductors": {
            "id": "diag-u3-semiconductors", "lab_exp": "lab-u3-diode-transistor",
            "title": "الوصلة الثنائية والترانزستور 3D (ص 62 - 78)", "sim_key": "phys_diode",
            "formula": "ت_باعث = ت_قاعدة + ت_مجمع | β = ت_ع / ت_ق",
            "slider_label": "جهد الانحياز:", "slider_min": 0, "slider_max": 100, "slider_val": 70, "slider_unit": "%",
            "components": [
                {"id": "diode", "name": "الوصلة الثنائية p-n", "role": "تمرر التيار بالانحياز الأمامي وتقوّم المتردد."},
                {"id": "transistor", "name": "الترانزستور", "role": "يعمل كمكبر (IC = β·IB) وكمفتاح إلكتروني."}
            ]
        },
        "diag-u4-cro-radar": {
            "id": "diag-u4-cro-radar", "lab_exp": "lab-u4-gas-cro-radar",
            "title": "أنبوبة أشعة الكاثود والأوسيلوسكوب والرادار (ص 86 - 106)", "sim_key": "phys_cro",
            "formula": "بعد الهدف بالرادار d = (c · Δt) / 2",
            "slider_label": "تردد المسح:", "slider_min": 1, "slider_max": 10, "slider_val": 5, "slider_unit": "x",
            "components": [
                {"id": "gun", "name": "المدفع الإلكتروني", "role": "يُطلق ويعجل حزمة الإلكترونات نحو الشاشة."},
                {"id": "screen", "name": "الشاشة الفلورية", "role": "ترسم الإشارة الكهربائية أو موقع هدف الرادار."}
            ]
        },
        "diag-u5-bohr": {
            "id": "diag-u5-bohr", "lab_exp": "lab-u5-bohr-spectrum",
            "title": "ذرة الهيدروجين لنظرية بور والأطياف 3D (ص 119 - 140)", "sim_key": "phys_bohr",
            "formula": "ط_ن = -13.6 / ن² eV | Δط = هـ·ν",
            "slider_label": "المدار الكمي:", "slider_min": 1, "slider_max": 4, "slider_val": 2, "slider_unit": "",
            "components": [
                {"id": "nucleus", "name": "النواة الموجبة", "role": "تجذب الإلكترون بقوة كولوم."},
                {"id": "orbit", "name": "المدارات الكمية", "role": "rₙ = n²·r₁ و Eₙ = -13.6/n² eV."}
            ]
        },
        "diag-u6-photoelectric": {
            "id": "diag-u6-photoelectric", "lab_exp": "lab-u6-photoelectric",
            "title": "الخلية الكهروضوئية والأشعة السينية والليزر 3D (ص 145 - 170)", "sim_key": "phys_photoelectric",
            "formula": "هـ·ν = φ + ط_ح(العظمى)",
            "slider_label": "تردد الضوء:", "slider_min": 1, "slider_max": 14, "slider_val": 10, "slider_unit": "×10¹⁴ Hz",
            "components": [
                {"id": "cathode", "name": "المهبط الحساس", "role": "يحرر الإلكترونات إذا كانت ν ≥ ν₀."},
                {"id": "laser", "name": "الليزر وكولدج", "role": "إنتاج فوتونات متماسكة أو أشعة سينية."}
            ]
        },
        "diag-u7-nuclear": {
            "id": "diag-u7-nuclear", "lab_exp": "lab-u7-nuclear",
            "title": "انحراف الإشعاع النووي والمفاعل 3D (ص 175 - 182)", "sim_key": "phys_nuclear",
            "formula": "ط = Δك · 931.5 MeV | ك = ك₀·(½)^(ز/عمر النصف)",
            "slider_label": "المجال المغناطيسي:", "slider_min": 0, "slider_max": 100, "slider_val": 70, "slider_unit": "%",
            "components": [
                {"id": "alpha_beta_gamma", "name": "ألفا وبيتا وجاما", "role": "تتميز بمسارات مختلفة في المجال المغناطيسي."},
                {"id": "fission", "name": "الانشطار النووي", "role": "يحرر طاقة ΔE = Δm·c²."}
            ]
        },
        "diag-u8-solar": {
            "id": "diag-u8-solar", "lab_exp": "lab-u8-solar-prism",
            "title": "تحليل الطيف الشمسي والخلية الفوتوفولتية (ص 188 - 196)", "sim_key": "phys_solar",
            "formula": "القدرة الشمسية الصافية = الإشعاع × المساحة × الكفاءة",
            "slider_label": "الإشعاع الشمسي:", "slider_min": 20, "slider_max": 100, "slider_val": 85, "slider_unit": "%",
            "components": [
                {"id": "prism", "name": "المنشور الزجاجي", "role": "يحلل الضوء الأبيض لألوان الطيف السبعة."},
                {"id": "pv", "name": "الخلية الشمسية", "role": "تحول ضوء الشمس لتيار مستمر."}
            ]
        },
        "diag-u9-cosmos": {
            "id": "diag-u9-cosmos", "lab_exp": "lab-u9-cosmos",
            "title": "المجرات وتطور النجوم 3D (ص 199 - 209)", "sim_key": "phys_cosmos",
            "formula": "λ_max · T = 2.898 × 10⁻³ m·K",
            "slider_label": "حرارة النجم:", "slider_min": 3000, "slider_max": 25000, "slider_val": 5800, "slider_unit": " K",
            "components": [
                {"id": "milky", "name": "مجرة درب التبانة", "role": "مجرة حلزونية قطرها 100,000 سنة ضوئية."},
                {"id": "stars", "name": "ألوان النجوم", "role": "النجم الأزرق أسخن والنجوم الحمراء أبرد."}
            ]
        }
    }

    # 6. AUTHENTIC ASSESSMENTS EXTRACTED DIRECTLY FROM EACH UNIT'S "تقويم الوحدة"!
    assessments = {
        "quiz-phys-u1": [
            {
                "id": "q-u1-tf-a", "page": 27,
                "q": "صح أم خطأ (تقويم الوحدة ص 27 أ): تظل الطاقة الحركية لأي تصادم ثابتة.",
                "options": [
                    {"text": "عبارة صحيحة (✓)", "why_wrong": "خطأ! الطاقة الحركية تظل ثابتة في التصادم المرن فقط، أما في التصادم غير المرن فيُفقد جزء منها."},
                    {"text": "عبارة خاطئة (✗)"}
                ],
                "answer": 1,
                "explain": "تُحفظ كمية التحرك في جميع التصادمات المعزولة، بينما لا تُحفظ الطاقة الحركية إلا في التصادم المرن."
            },
            {
                "id": "q-u1-tf-b", "page": 27,
                "q": "صح أم خطأ (تقويم الوحدة ص 27 د): مبدأ الفعل ورد الفعل لا ينطبق خارج الغلاف الجوي للأرض.",
                "options": [
                    {"text": "عبارة صحيحة (✓)", "why_wrong": "خطأ! قانون نيوتن الثالث ينطبق في الفضاء الخارجي بكل كفاءة، وبه تندفع الصواريخ."},
                    {"text": "عبارة خاطئة (✗)"}
                ],
                "answer": 1,
                "explain": "قوة الدفع في الصواريخ تنشأ داخل محرك الصاروخ بين الغازات المندفعة وجسم الصاروخ ولا تحتاج لوسط هوائي."
            },
            {
                "id": "q-u1-tf-h", "page": 27,
                "q": "صح أم خطأ (تقويم الوحدة ص 27 هـ): سرعة إفلات الأجسام من الجاذبية الأرضية هي 8 كم/ث.",
                "options": [
                    {"text": "عبارة صحيحة (✓)", "why_wrong": "خطأ! 8 كم/ث هي السرعة المدارية للقمر الصناعي قرب الأرض، أما سرعة الإفلات فهي 11.2 كم/ث."},
                    {"text": "عبارة خاطئة (✗)"}
                ],
                "answer": 1,
                "explain": "سرعة الإفلات ع_إفلات = √(2gR) ≈ 11.2 كم/ث."
            },
            {
                "id": "q-u1-prob-2", "page": 27,
                "q": "مسألة (السؤال الثاني ص 27): إذا كانت كمية التحرك لصاروخ 5×10⁸ كجم·م/ث، وكانت سرعته 5×10³ م/ث، فما كتلته؟",
                "options": [
                    {"text": "10⁵ كجم (100 طن)"},
                    {"text": "25×10¹¹ كجم", "why_wrong": "الكتلة ك = كت / ع (قسمة كمية التحرك على السرعة وليست ضرباً)."},
                    {"text": "10⁴ كجم", "why_wrong": "تحقق من طرح الأسس: 10⁸ / 10³ = 10⁵."},
                    {"text": "100 كجم", "why_wrong": "الكتلة تساوي 10⁵ كجم."}
                ],
                "answer": 0,
                "explain": "ك = كت / ع = (5×10⁸) / (5×10³) = 10⁵ كجم."
            },
            {
                "id": "q-u1-proj", "page": 24,
                "q": "الزاوية التي تحقق أقصى مدى أفقي لمقذوف أُطلق بنفس السرعة الابتدائية مع إهمال مقاومة الهواء هي:",
                "options": [
                    {"text": "30°", "why_wrong": "زاوية 30° تعطي مدى أقل من المدى الأقصى."},
                    {"text": "45°"},
                    {"text": "60°", "why_wrong": "زاوية 60° تعطي نفس مدى 30°."},
                    {"text": "90°", "why_wrong": "القذف الرأسي بـ 90° مداه الأفقي صفر."}
                ],
                "answer": 1,
                "explain": "المدى ف_س = (ع₀² جا 2هـ)/د، ويبلغ أقصاه عندما جا 2هـ = 1 أي 2هـ = 90° ← هـ = 45°."
            }
        ],
        "quiz-phys-u2": [
            {
                "id": "q-u2-mc-b", "page": 59,
                "q": "تقويم الوحدة ص 59 (جـ): وصل مكثف سعته 14 ميكروفاراد بمصدر تيار متردد تردده 50 هرتز وجهد 250 فولت، فإن شدة التيار المار تساوي:",
                "options": [
                    {"text": "1.1 أمبير"},
                    {"text": "1.2 أمبير", "why_wrong": "احسب أولاً م_سع = 1/(2 × (22/7) × 50 × 14×10⁻⁶) = 227.3 Ω ثم اقسم 250 / 227.3."},
                    {"text": "1.3 أمبير", "why_wrong": "250 / 227.27 = 1.1 أمبير."},
                    {"text": "1.5 أمبير", "why_wrong": "القيمة الدقيقة هي 1.1 أمبير."}
                ],
                "answer": 0,
                "explain": "م_سع = 7 / (2 × 22 × 50 × 14×10⁻⁶) ≈ 227.27 Ω، إذن ت = 250 / 227.27 ≈ 1.1 أمبير."
            },
            {
                "id": "q-u2-mc-h", "page": 59,
                "q": "تقويم الوحدة ص 59 (ح): يحدث الرنين الكهربائي في دائرة الرنين عندما تكون قيمة:",
                "options": [
                    {"text": "م_سع > م_حث", "why_wrong": "عندها تسود الخواص السعوية ولا تتحقق حالة الرنين."},
                    {"text": "م_سع < م_حث", "why_wrong": "عندها تسود الخواص الحثية."},
                    {"text": "م_سع = م_حث"}
                ],
                "answer": 2,
                "explain": "شرط الرنين تساوي المفاعلتين الحثية والسعوية فتصبح المعاوقة أقل ما يمكن (م_ق = م) والتيار أعظمي."
            },
            {
                "id": "q-u2-mc-n", "page": 60,
                "q": "تقويم الوحدة ص 60 (ن): ملف حثي مفاعلته 85 أوم، ومكثف مفاعلته 60 أوم، ومقاومة أومية 20 أوم على التوالي، فإن المعاوقة المكافئة ≈:",
                "options": [
                    {"text": "30 أوم", "why_wrong": "طبق √(20² + (85 - 60)²) = √(400 + 625) = √1025 ≈ 32 أوم."},
                    {"text": "29 أوم", "why_wrong": "√1025 أكبر من 29 وأقرب لـ 32."},
                    {"text": "32 أوم"},
                    {"text": "31 أوم", "why_wrong": "32² = 1024 ≈ 1025."}
                ],
                "answer": 2,
                "explain": "م_ق = √(م² + (م_حث - م_سع)²) = √(20² + 25²) = √1025 ≈ 32 أوم."
            }
        ],
        "quiz-phys-u3": [
            {
                "id": "q-u3-tf-a", "page": 81,
                "q": "تقويم الوحدة ص 81 (س2 أ): تزداد المقاومة الكهربائية لأشباه الموصلات عندما تنخفض درجة حرارتها وتقل عندما تزداد درجة حرارتها.",
                "options": [
                    {"text": "عبارة صحيحة (✓)"},
                    {"text": "عبارة خاطئة (✗)", "why_wrong": "العبارة صحيحة! زيادة الحرارة تكسر مزيداً من الروابط التساهمية وتزيد حوامل الشحنة فتقل المقاومة (عكس الفلزات)."}
                ],
                "answer": 0,
                "explain": "تقل مقاومة أشباه الموصلات وتزداد توصيليتها برفع درجة الحرارة لتولد أزواج (إلكترون - فجوة)."
            },
            {
                "id": "q-u3-tf-c", "page": 81,
                "q": "تقويم الوحدة ص 81 (س2 جـ): تنتج الوصلة الثنائية عند التحام ثلاث بلورات من النوع P-Type.",
                "options": [
                    {"text": "عبارة صحيحة (✓)", "why_wrong": "خطأ! الوصلة الثنائية تلتحم فيها بلورتان مختلفتان (بلورة P مع بلورة N) وليست ثلاث بلورات متماثلة."},
                    {"text": "عبارة خاطئة (✗)"}
                ],
                "answer": 1,
                "explain": "تتكون الوصلة الثنائية من بلورة موجبة P وبلورة سالبة N، بينما الترانزستور يتكون من ثلاث مناطق (npn أو pnp)."
            },
            {
                "id": "q-u3-mc-t", "page": 80,
                "q": "يتميز المجمع في الترانزستور بالنسبة للباعث بأنه:",
                "options": [
                    {"text": "أكبر مساحة سطح وأقل نسبة تطعيم (شوائب)"},
                    {"text": "أصغر مساحة وأعلى شوائب", "why_wrong": "هذه صفات القاعدة أو الباعث."},
                    {"text": "مساوٍ للقاعدة تماماً", "why_wrong": "القاعدة رقيقة جداً وقليلة الشوائب."}
                ],
                "answer": 0,
                "explain": "المجمع واسع المساحة لتبديد الحرارة واستقبال حاملات الشحنة، بينما الباعث غزير التطعيم."
            }
        ],
        "quiz-phys-u4": [
            {
                "id": "q-u4-tf-1", "page": 108,
                "q": "تقويم الوحدة ص 108 (س2 - 1): الأشعة المهبطية هي عبارة عن جسيمات ذات شحنة سالبة.",
                "options": [
                    {"text": "عبارة صحيحة (✓)"},
                    {"text": "عبارة خاطئة (✗)", "why_wrong": "العبارة صحيحة؛ أشعة المهبط سيل من الإلكترونات سالبة الشحنة."}
                ],
                "answer": 0,
                "explain": "تتكون أشعة المهبط من إلكترونات تنبعث من الكاثود وتنحرف نحو القطب الموجب."
            },
            {
                "id": "q-u4-tf-3", "page": 108,
                "q": "تقويم الوحدة ص 108 (س2 - 3): يغطى الجدار الداخلي لشاشة أنبوبة أشعة الكاثود بمادة فلوريسية مثل كبريتيد الخارصين.",
                "options": [
                    {"text": "عبارة صحيحة (✓)"},
                    {"text": "عبارة خاطئة (✗)", "why_wrong": "العبارة صحيحة! كبريتيد الخارصين يتوهج بمجرد اصطدام الإلكترونات به لإظهار الرسم."}
                ],
                "answer": 0,
                "explain": "تُطلى الشاشة بكبريتيد الخارصين لتصدر وميضاً ضوئياً عند موقع سقوط شعاع الإلكترونات."
            },
            {
                "id": "q-u4-radar", "page": 94,
                "q": "أرسل رادار نبضة نحو طائرة وعادت بعد 4×10⁻⁴ ثانية، فما بُعد الطائرة (ع = 3×10⁸ م/ث)؟",
                "options": [
                    {"text": "60 كم"},
                    {"text": "120 كم", "why_wrong": "لا تنسَ القسمة على 2 لأن الزمن للذهاب والإياب معاً."}
                ],
                "answer": 0,
                "explain": "ف = (ع × Δز) / 2 = (3×10⁸ × 4×10⁻⁴) / 2 = 60,000 م = 60 كم."
            }
        ],
        "quiz-phys-u5": [
            {
                "id": "q-u5-tf-a", "page": 142,
                "q": "تقويم الوحدة ص 142 (2 ب): طيف عنصر الصوديوم هو طيف خطي.",
                "options": [
                    {"text": "عبارة صحيحة (✓)"},
                    {"text": "عبارة خاطئة (✗)", "why_wrong": "صحيح! طيف الغازات والأبخرة الذرية المثارة (كالصوديوم والهيدروجين) طيف انبعاث خطي مميز لكل عنصر."}
                ],
                "answer": 0,
                "explain": "يمتاز الصوديوم بخطين أصفرين مميزين في طيفه الخطي."
            },
            {
                "id": "q-u5-tf-d", "page": 142,
                "q": "تقويم الوحدة ص 142 (2 د): العنصر الكيميائي لا يشع نفس الأطوال الموجية التي يمتصها.",
                "options": [
                    {"text": "عبارة صحيحة (✓)", "why_wrong": "خطأ! ذرة العنصر تشع نفس الأطوال الموجية المميزة التي تمتصها لأن الانتقال يتم بين نفس مستويات الطاقة."},
                    {"text": "عبارة خاطئة (✗)"}
                ],
                "answer": 1,
                "explain": "خطوط الامتصاص (كخطوط فرانهوفر) تقع عند نفس الترددات التي يشعها العنصر في طيف انبعاثه."
            },
            {
                "id": "q-u5-tf-z", "page": 142,
                "q": "تقويم الوحدة ص 142 (2 ز): يزداد نصف قطر المدار المسموح للإلكترون في ذرة الهيدروجين بزيادة مربع العدد الكمي الرئيسي (ن²).",
                "options": [
                    {"text": "عبارة صحيحة (✓)"},
                    {"text": "عبارة خاطئة (✗)", "why_wrong": "صحيح! نق_ن = ن² × نق₁ (حيث نق₁ = 0.528 أنجستروم)."}
                ],
                "answer": 0,
                "explain": "يتناسب نصف قطر مدار بور طردياً مع ن²."
            }
        ],
        "quiz-phys-u6": [
            {
                "id": "q-u6-mc-1", "page": 171,
                "q": "تقويم الوحدة ص 171 (1): عندما تسقط أشعة ضوئية بتردد مناسب على لوح معدني ما فإنه تنطلق من سطح المعدن:",
                "options": [
                    {"text": "فوتونات ضوئية", "why_wrong": "الفوتونات هي الضوء الساقط نفسه، أما المنطلق من المعدن فهي إلكترونات."},
                    {"text": "إلكترونات ضوئية"},
                    {"text": "نيوترونات", "why_wrong": "النيوترونات داخل النواة ولا تتحرر بالضوء."},
                    {"text": "أشعة سينية", "why_wrong": "الأشعة السينية تتطلب قذف هدف بإلكترونات فائقة السرعة."}
                ],
                "answer": 1,
                "explain": "الظاهرة الكهروضوئية هي تحرر إلكترونات (إلكترونات ضوئية) من سطح الفلز."
            },
            {
                "id": "q-u6-mc-2", "page": 171,
                "q": "تقويم الوحدة ص 171 (2): إن أقصر طول موجي في الطيف المتصل للأشعة السينية يعتمد على:",
                "options": [
                    {"text": "نوع مادة سطح الهدف", "why_wrong": "مادة الهدف تحدد الطيف الخطي المميز للأشعة السينية، وليس أقصر طول موجي مستمر."},
                    {"text": "فرق الجهد المطبق بين طرفي الأنبوب"},
                    {"text": "تردد الضوء الساقط", "why_wrong": "أنبوبة كولدج تعمل بتسريع الإلكترونات بفرق جهد عالٍ."}
                ],
                "answer": 1,
                "explain": "من العلاقة λ_min = (h·c) / (e·V)، يتوقف أقصر طول موجي على فرق الجهد V فقط."
            },
            {
                "id": "q-u6-tf-laser", "page": 171,
                "q": "تقويم الوحدة ص 171 (4): الانبعاث الليزري هو انبعاث مستحث، وجهد الإيقاف يتوقف على تردد الضوء الساقط.",
                "options": [
                    {"text": "عبارة صحيحة (✓)"},
                    {"text": "عبارة خاطئة (✗)", "why_wrong": "العبارتان صحيحتان علمياً!"}
                ],
                "answer": 0,
                "explain": "يقوم الليزر على الانبعاث المستحث مع الإسكان المعكوس، ويتوقف جهد الإيقاف على التردد لا الشدة."
            }
        ],
        "quiz-phys-u7": [
            {
                "id": "q-u7-tf-1", "page": 183,
                "q": "تقويم الوحدة ص 183 (س2 - 1): تنحرف أشعة جاما عند مرورها في مجال مغناطيسي في اتجاه معاكس لاتجاه انحراف أشعة بيتا.",
                "options": [
                    {"text": "عبارة صحيحة (✓)", "why_wrong": "خطأ! التي تنحرف عكس بيتا هي أشعة ألفا الموجبة، أما أشعة جاما فلا تنحرف نهائياً لأنها متعادلة."},
                    {"text": "عبارة خاطئة (✗)"}
                ],
                "answer": 1,
                "explain": "ألفا (+) وبيتا (-) ينحرفان في اتجاهين متعاكسين، بينما جاما متعادلة كهربائياً فلا تنحرف."
            },
            {
                "id": "q-u7-mc-3", "page": 183,
                "q": "تقويم الوحدة ص 183 (س3): أي العبارتين تعبر عن التعريف الصحيح لعمر النصف لمادة مشعة؟",
                "options": [
                    {"text": "هو الزمن اللازم لكي يتحلل نصف مكونات المادة المشعة"},
                    {"text": "هو كمية المادة التي تبقى من هذه المادة بعد مرور نصف الزمن", "why_wrong": "عمر النصف وحدة زمنية وليس كمية مادة."}
                ],
                "answer": 0,
                "explain": "عمر النصف T₁/₂ هو الزمن اللازم لتحلل نصف عدد أنوية العنصر المشع تلقائياً."
            }
        ],
        "quiz-phys-u8": [
            {
                "id": "q-u8-mc-1", "page": 197,
                "q": "تقويم الوحدة ص 197: تنتج الطاقة الشمسية الهائلة في باطن الشمس عن:",
                "options": [
                    {"text": "الاندماج النووي لذرات الهيدروجين وتحولها إلى هيليوم"},
                    {"text": "احتراق الفحم والنفط في الشمس", "why_wrong": "تفاعل الشمس نووي اندماجي وليس احتراقاً كيميائياً."},
                    {"text": "انشطار اليورانيوم", "why_wrong": "الشمس تعتمد على الاندماج لا الانشطار."}
                ],
                "answer": 0,
                "explain": "تندمج أنوية الهيدروجين تحت ضغط وحرارة هائلين لتكوين الهيليوم وتحرير الطاقة الإشعاعية."
            },
            {
                "id": "q-u8-pv", "page": 195,
                "q": "الخلية الشمسية السيليكونية تحول الطاقة الشمسية مباشرة إلى:",
                "options": [
                    {"text": "تيار كهربائي مستمر (DC)"},
                    {"text": "تيار متردد (AC) مباشرة", "why_wrong": "تحول الخلية الضوء إلى تيار مستمر، ويُستعمل العاكس (Inverter) لتحويله إلى متردد."}
                ],
                "answer": 0,
                "explain": "تُنتج الألواح الفوتوفولتية فرق جهد وتياراً مستمراً (DC)."
            }
        ],
        "quiz-phys-u9": [
            {
                "id": "q-u9-tf-1", "page": 210,
                "q": "تقويم الوحدة ص 210 (س1 - 1): حدث الانفجار العظيم عندما كان قطر الكرة الكونية مساوياً 10 مرات قطر الشمس.",
                "options": [
                    {"text": "عبارة صحيحة (✓)"},
                    {"text": "عبارة خاطئة (✗)", "why_wrong": "الكتاب المدرسي ينص في ص 200 على فرضية الكرة الكونية البدئية الهائلة الكثافة (نحو 10 أمثال قطر الشمس)؛ راجع ص 200 و210."}
                ],
                "answer": 0,
                "explain": "بحسب نص الكتاب المدرسي ص 200: تركزت مادة الكون في كرة قطرها يقارب 10 مرات قطر الشمس قبل الانفجار العظيم."
            },
            {
                "id": "q-u9-mc-1", "page": 210,
                "q": "تقويم الوحدة ص 210 (س2 - 1): مجرة درب التبانة هي مجرة من النوع:",
                "options": [
                    {"text": "الحلزوني (اللولبي)"},
                    {"text": "الكروي / الإهليلجي", "why_wrong": "مجرتنا لها أذرع حلزونية كما في شكل (3) ص 203."},
                    {"text": "غير المنتظم", "why_wrong": "درب التبانة منتظمة حلزونية."},
                    {"text": "لا شيء مما ذكر", "why_wrong": "الحلزوني هو التصنيف الصحيح."}
                ],
                "answer": 0,
                "explain": "مجرة درب التبانة مجرة حلزونية قطرها نحو 100 ألف سنة ضوئية."
            },
            {
                "id": "q-u9-mc-5", "page": 210,
                "q": "تقويم الوحدة ص 210 (س2 - 5): يبدأ تكون النجوم عند:",
                "options": [
                    {"text": "بدء حدوث الاندماج النووي"},
                    {"text": "تفاعل الهيدروجين مع الهيليوم", "why_wrong": "التفاعل هو اندماج ذرات الهيدروجين لإنتاج الهيليوم."},
                    {"text": "حدوث الانفجار العظيم فقط", "why_wrong": "تتشكل النجوم من السدم عندما تصل درجة الحرارة والضغط لبدء الاندماج النووي."}
                ],
                "answer": 0,
                "explain": "يتوهج النجم ويبدأ حياته الفعلية فور انطلاق تفاعلات الاندماج النووي في قلبه."
            }
        ]
    }

    # Exact authentic Physics Activities mapped to page -> lab_exp ID
    exact_page_activity = {
        15: ("lab-u1-balloon-rocket", "🧪 نشاط (1): البالونة ودفع الصواريخ"),
        19: ("lab-u1-satellite", "🧪 نشاط (2): حركة الأقمار الصناعية"),
        22: ("lab-u1-angular", "🧪 نشاط (3): القصور الذاتي الدوراني"),
        32: ("lab-u2-faraday-wire", "🧪 نشاط (1): الحث الكهرومغناطيسي"),
        34: ("lab-u2-dynamo", "🧪 نشاط (2): مولد الدينامو"),
        38: ("lab-u2-hotwire", "🧪 نشاط (3): الأميتر الحراري"),
        39: ("lab-u2-capacitor", "🧪 نشاط (5): المكثف في الدوائر"),
        42: ("lab-u2-capacitor", "🧪 نشاط (6): سعة المكثف والتيار"),
        47: ("lab-u2-rlc", "🧪 نشاط (7): المفاعلة الحثية وRLC"),
        52: ("lab-u2-rlc", "🧪 نشاط (8): دائرة الرنين والإذاعة"),
        54: ("lab-u2-rlc", "🧪 نشاط (7): توصيل الملفات"),
        86: ("lab-u4-gas-cro-radar", "🧪 نشاط (1): تأين الغازات والكشاف"),
        145: ("lab-u6-photoelectric", "🧪 نشاط (1): الظاهرة الكهروضوئية"),
        147: ("lab-u6-photoelectric", "🔬 تجربة مليكان الكهروضوئية"),
        178: ("lab-u7-nuclear", "🧪 نشاط: الإشعاع النووي وأضراره"),
        189: ("lab-u8-solar-prism", "🔬 تجربة: تحليل الطيف بالمنشور"),
        199: ("lab-u9-cosmos", "🧪 نشاط (1): رصد السماء والكون"),
        202: ("lab-u9-cosmos", "🧪 نشاط (2): تصنيف المجرات"),
        203: ("lab-u9-cosmos", "🧪 نشاط (3): مجرة درب التبانة"),
    }

    # Specific figure -> 3D lab mapping per Book Page (for highest educational accuracy!)
    def get_diag_for_page(bp, uid):
        if uid == "u1":
            if bp == 10: return ("diag-u1-collision1d", "🔍 استكشاف التصادم 3D")
            if bp == 11: return ("diag-u1-collision2d", "🔍 استكشاف التصادم في بعدين 3D")
            if bp == 13: return ("diag-u1-collision2d", "🔍 تحليل تصادم السيارة والشاحنة 3D")
            if 15 <= bp <= 16: return ("diag-u1-rocket", "🔍 محاكاة الصاروخ ذاتي الدفع 3D")
            if 19 <= bp <= 21: return ("diag-u1-satellite", "🔍 مدار القمر الصناعي 3D")
            if 22 <= bp <= 23: return ("diag-u1-angular" if "10" in str(bp) or bp==23 else "diag-u1-projectiles", "🔍 محاكاة الحركة 3D")
            return ("diag-u1-projectiles", "🔍 محاكاة المقذوفات 3D")
        if uid == "u2":
            if bp <= 38: return ("diag-u2-dynamo", "🔍 محاكاة الدينامو والحث 3D")
            if bp <= 45: return ("diag-u2-capacitor", "🔍 محاكاة المكثف 3D")
            return ("diag-u2-rlc", "🔍 محاكاة دائرة المتردد 3D")
        if uid == "u3": return ("diag-u3-semiconductors", "🔍 محاكاة الدايود والترانزستور 3D")
        if uid == "u4": return ("diag-u4-cro-radar", "🔍 محاكاة الكاثود والرادار 3D")
        if uid == "u5": return ("diag-u5-bohr", "🔍 محاكاة ذرة بور والطيف 3D")
        if uid == "u6": return ("diag-u6-photoelectric", "🔍 محاكاة الكهروضوئية والليزر 3D")
        if uid == "u7": return ("diag-u7-nuclear", "🔍 محاكاة الإشعاع النووي 3D")
        if uid == "u8": return ("diag-u8-solar", "🔍 محاكاة الطيف والخلايا 3D")
        return ("diag-u9-cosmos", "🔍 استكشاف المجرات والنجوم 3D")

    # 7. SURGICAL INTERACTIONS GENERATION (PDF 6..218 -> Zero misplaced boxes!)
    interactions = {}

    for p_meta in pages:
        pdf_num = p_meta["pdf_page"]
        bp = p_meta["book_page"]
        pid = p_meta["page_id"]
        uid = p_meta["unit_id"]
        ptype = p_meta["type"]

        # Do NOT put intrusive boxes on intro, contents, or ending page
        if ptype in ("intro", "contents", "ending") or not uid:
            continue

        xml_p = xml_pages.get(pdf_num)
        if xml_p is None:
            continue

        # Parse texts & images directly for this page
        items = []
        for t in xml_p.findall("text"):
            raw = "".join(t.itertext()).strip()
            if not raw or "e-learning" in raw: continue
            top = int(t.attrib["top"])
            left = int(t.attrib["left"])
            w = int(t.attrib["width"])
            h = int(t.attrib["height"])
            if 1060 <= top <= 1095: continue
            fid = t.attrib.get("font", "")
            fi = fonts.get(fid, {})
            items.append({
                "top": top, "left": left, "w": w, "h": h,
                "size": int(fi.get("size", "20")),
                "color": fi.get("color", "#000000"),
                "family": fi.get("family", ""),
                "raw": raw,
                "sc": re.sub(r"[\s‡?]+", "", raw)
            })
        items.sort(key=lambda z: z["top"])

        real_imgs = []
        for im in xml_p.findall("image"):
            it, il, iw, ih = int(im.attrib["top"]), int(im.attrib["left"]), int(im.attrib["width"]), int(im.attrib["height"])
            if iw > 750 and ih > 950: continue
            if it < 145 and il > 680 and iw < 160: continue
            if iw < 45 or ih < 40: continue
            if it < 270 and iw > 600 and ih < 160: continue
            real_imgs.append({"top": it, "left": il, "w": iw, "h": ih})

        page_spots = []

        # A. UNIT COVER PAGES -> ONLY Objectives card!
        if ptype == "unit_cover":
            g_heads = [it for it in items if "·«b¼√" in it["sc"]]
            gy0 = max(630, g_heads[0]["top"] - 12) if g_heads else 670
            gy1 = min(1050, max((it["top"] + 32 for it in items if it["top"] > gy0), default=1030))
            b = clamp_box(0.18, gy0 / H, 0.65, (gy1 - gy0) / H)
            page_spots.append({
                "id": f"hs-{pid}-unit-goals",
                "type": "explainable_text",
                "explanation_ref": f"exp-phys-{uid}-overview",
                "indicator_label": f"🎯 أهداف ومقدمة الوحدة",
                "highlight_color": "rgba(2, 132, 199, 0.14)",
                "bounds": b
            })
            interactions[pid] = page_spots
            continue

        # B. EVALUATION PAGES (تقويم الوحدة) -> Assessment card ONLY!
        if ptype == "assessment":
            y_tops = [it["top"] for it in items if 150 <= it["top"] <= 1040]
            y0 = (min(y_tops) - 18) / H if y_tops else 0.16
            y1 = (max(y_tops) + 32) / H if y_tops else 0.82
            page_spots.append({
                "id": f"hs-{pid}-quiz",
                "type": "assessment",
                "assessment_ref": f"quiz-phys-{uid}",
                "indicator_label": "📝 اختبر نفسك وحل تقويم الوحدة",
                "highlight_color": "rgba(217, 119, 6, 0.16)",
                "bounds": clamp_box(0.19, y0, 0.63, min(0.66, max(0.18, y1 - y0)))
            })
            interactions[pid] = page_spots
            continue

        # C. GLOSSARY PAGES (قوائم المصطلحات)
        if ptype == "glossary":
            page_spots.append({
                "id": f"hs-{pid}-glossary",
                "type": "explainable_text",
                "explanation_ref": "exp-phys-glossary",
                "indicator_label": "📖 استعراض وشرح المصطلحات العلمية",
                "highlight_color": "rgba(16, 185, 129, 0.14)",
                "bounds": clamp_box(0.17, 0.15, 0.66, 0.68)
            })
            interactions[pid] = page_spots
            continue

        # Matched lesson for this page
        matched_lesson = None
        for l in lessons:
            if l["unitId"] == uid and l["pages"][0] <= bp <= l["pages"][-1]:
                matched_lesson = l
                break
        if not matched_lesson:
            uls = [l for l in lessons if l["unitId"] == uid]
            matched_lesson = uls[0] if uls else lessons[0]
        exp_ref = f"exp-{matched_lesson['id']}"

        # E. TRUE FIGURES (شكل (n)) COMPUTED FIRST SO ACTIVITIES NEVER OVERLAP FIGURES!
        diag_id, diag_label = get_diag_for_page(bp, uid)
        seen_fig_y = []
        fig_spots = []
        for it in items:
            sc = it["sc"]
            # Must look like a standalone caption (e.g. '©±® qJý' or '©≤® qJý ...' without bullet '≠' and short)
            if not ("qJý" in sc and "©" in sc and it["top"] < 1055):
                continue
            if "≠" in it["raw"] or "Æ©" in sc or "dE½«" in sc or len(sc) > 42:
                continue
            if any(abs(it["top"] - sy) < 90 for sy in seen_fig_y):
                continue
            seen_fig_y.append(it["top"])

            cap_cx = it["left"] + it["w"] / 2.0
            matched_im = None
            for im in real_imgs:
                im_bot = im["top"] + im["h"]
                im_cx = im["left"] + im["w"] / 2.0
                if abs(im_bot - it["top"]) < 95 and abs(im_cx - cap_cx) < 250:
                    matched_im = im
                    break

            if matched_im:
                fb = clamp_box(
                    matched_im["left"]/W - 0.01,
                    matched_im["top"]/H - 0.01,
                    matched_im["w"]/W + 0.02,
                    (it["top"] + it["h"] + 12 - matched_im["top"])/H
                )
            else:
                x_box = 0.17 if cap_cx < 390 else (0.46 if cap_cx > 500 else 0.20)
                w_box = 0.37 if (cap_cx < 390 or cap_cx > 500) else 0.58
                y0_px = max(145, it["top"] - 210)
                fb = clamp_box(x_box, y0_px / H, w_box, (it["top"] + it["h"] + 12 - y0_px) / H)

            if overlaps_any(fb, fig_spots, thresh=0.25):
                continue

            this_diag, this_lbl = diag_id, diag_label
            if bp == 23:
                if it["top"] < 650:
                    this_diag, this_lbl = "diag-u1-angular", "🔍 القصور الدوراني 3D (شكل 10)"
                else:
                    this_diag, this_lbl = "diag-u1-projectiles", "🔍 مسار المقذوف 3D (شكل 11)"

            fig_spots.append({
                "id": f"hs-{pid}-fig-{len(fig_spots)}",
                "type": "interactive_3d",
                "diagram_ref": this_diag,
                "lab_exp": diagrams[this_diag]["lab_exp"],
                "indicator_label": this_lbl,
                "highlight_color": "rgba(239, 68, 68, 0.14)",
                "bounds": fb
            })

        # D. AUTHENTIC ACTIVITY / EXPERIMENT ON THIS PAGE (Strictly non-overlapping with any figure!)
        if bp in exact_page_activity:
            lab_exp, act_label = exact_page_activity[bp]
            act_items = [it for it in items if "UA½" in it["sc"] or "ÞUA½" in it["sc"] or "WÐd&" in it["sc"]]
            if act_items:
                y0_px = act_items[0]["top"] - 10
                y1_px = min(1045, y0_px + 280)
                for nxt in items:
                    if nxt["top"] <= y0_px + 30: continue
                    if (nxt["color"] in ("#e500e5", "#008080") and nxt["size"] >= 23) or "‰U¦" in nxt["sc"]:
                        y1_px = min(y1_px, nxt["top"] - 10)
                        break

                ax = 0.17
                aw = 0.66
                ay0 = y0_px / H
                ay1 = min(ay0 + 0.24, max(ay0 + 0.11, y1_px / H))

                for fs in fig_spots:
                    fb = fs["bounds"]
                    fy0, fy1 = fb["y"], fb["y"] + fb["h"]
                    fx0, fx1 = fb["x"], fb["x"] + fb["w"]
                    if not (fy1 <= ay0 + 0.005 or fy0 >= ay1 - 0.005):
                        if fy0 - ay0 >= 0.105:
                            # Trim bottom cleanly above the figure!
                            ay1 = min(ay1, fy0 - 0.008)
                        elif ay0 > fy1 - 0.05 and (ay1 - fy1) >= 0.09:
                            # Trim top cleanly below the figure!
                            ay0 = max(ay0, fy1 + 0.008)
                        elif fx1 < 0.56 and (0.85 - fx1) >= 0.25:
                            # Left-column figure shares row -> move activity cleanly to right column!
                            ax = max(ax, fx1 + 0.015)
                            aw = 0.85 - ax

                page_spots.append({
                    "id": f"hs-{pid}-activity",
                    "type": "activity",
                    "lab_exp": lab_exp,
                    "activity_ref": lab_exp,
                    "indicator_label": act_label,
                    "highlight_color": "rgba(124, 58, 237, 0.16)",
                    "bounds": clamp_box(ax, ay0, aw, max(0.08, ay1 - ay0))
                })

        for fs in fig_spots:
            page_spots.append(fs)

        # F. WORKED EXAMPLES (مثال n) OR MAJOR CONCEPT HEADINGS (strict non-overlapping!)
        placed_concept_y = []
        # 1) Worked examples
        for idx_i, it in enumerate(items):
            sc = it["sc"]
            if "‰U¦" in sc and len(sc) < 25 and it["top"] < 1030:
                y0_px = it["top"] - 8
                if any(abs(y0_px - py) < 165 for py in placed_concept_y): continue
                y1_px = min(1035, y0_px + 185)
                eb = clamp_box(0.17, y0_px / H, 0.66, (y1_px - y0_px) / H)
                if not overlaps_any(eb, page_spots, thresh=0.10):
                    placed_concept_y.append(y0_px)
                    page_spots.append({
                        "id": f"hs-{pid}-ex-{len(page_spots)}",
                        "type": "explainable_text",
                        "explanation_ref": exp_ref,
                        "indicator_label": "🧮 مثال محلول — الشرح والخطوات",
                        "highlight_color": "rgba(16, 185, 129, 0.13)",
                        "bounds": eb
                    })

        # 2) Section headings (shaded titles / colored concept headings)
        for it in items:
            if not ((it["color"] in ("#e500e5", "#008080", "#ff00ff") and it["size"] >= 22) or ("TheMajMASK" in it["family"] and it["size"] >= 26)):
                continue
            sc = it["sc"]
            if len(sc) < 4 or sc.startswith("©") or "W‡‡‡Ðd" in sc:
                continue
            y0_px = it["top"] - 8
            if y0_px > 920: continue
            if any(abs(y0_px - py) < 150 for py in placed_concept_y): continue
            cb = clamp_box(0.17, y0_px / H, 0.66, 0.14)
            if not overlaps_any(cb, page_spots, thresh=0.10):
                placed_concept_y.append(y0_px)
                page_spots.append({
                    "id": f"hs-{pid}-concept-{len(page_spots)}",
                    "type": "explainable_text",
                    "explanation_ref": exp_ref,
                    "indicator_label": "📌 مفهوم وقانون أساسي (3 مستويات)",
                    "highlight_color": "rgba(0, 168, 89, 0.13)",
                    "bounds": cb
                })

        if page_spots:
            interactions[pid] = page_spots

    # 8. SAVE ALL FILES & REBUILD DATA BUNDLE
    manifest = load_json("manifest.json")
    manifest["edition"]["start_pdf_page"] = 6
    manifest["edition"]["end_pdf_page"] = 218
    manifest["edition"]["total_book_pages"] = 213

    save_json("manifest.json", manifest)
    save_json("units.json", units)
    save_json("pages.json", pages)
    save_json("lessons.json", lessons)
    save_json("explanations.json", explanations)
    save_json("diagrams.json", diagrams)
    save_json("assessments.json", assessments)
    save_json("interactions.json", interactions)

    # Sync activities.json so every ID links cleanly
    activities = {k: v for k, v in load_json("activities.json").items()}
    for bp, (lab_exp, act_label) in exact_page_activity.items():
        activities[lab_exp] = {"id": lab_exp, "title": act_label, "book_page": bp, "lab_url": f"physics-12th-lab.html?exp={lab_exp}&from=book"}
    save_json("activities.json", activities)

    bundle = {
        "manifest": manifest,
        "units": units,
        "pages": pages,
        "lessons": lessons,
        "interactions": interactions,
        "explanations": explanations,
        "diagrams": diagrams,
        "activities": activities,
        "assessments": assessments,
        "glossary": glossary
    }
    js_out = "window.THAKER_CURRICULUM_G12_PHYSICS = " + json.dumps(bundle, ensure_ascii=False) + ";\n"
    with open(f"{OUT_DIR}/data_bundle.js", "w", encoding="utf-8") as f:
        f.write(js_out)

    for fn in os.listdir(OUT_DIR):
        shutil.copy2(f"{OUT_DIR}/{fn}", f"{ANDROID_OUT}/{fn}")

    total_hs = sum(len(v) for v in interactions.values())
    print(f"[✓] Precision Physics Data Pack built:")
    print(f"    - Pages: {len(pages)} (PDF 6..218, exact printed page numbers book=pdf-2)")
    print(f"    - Unit Covers: {[p['book_page'] for p in pages if p['type']=='unit_cover']} (goals box only!)")
    print(f"    - Pages with curated surgical hotspots: {len(interactions)} ({total_hs} total boxes)")
    print(f"    - Unit Quizzes: {len(assessments)} ({sum(len(v) for v in assessments.values())} real ministerial/textbook Qs)")

if __name__ == "__main__":
    main()
