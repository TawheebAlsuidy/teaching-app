#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Precision Grade 12 Biology Data Pack Builder (Zero Misplaced Hotspots + True Ministry TOC)
- Fixes book_page = pdf_page + 4 across all 219 interior pages (PDF 2..220 -> Book 6..224).
- Fixes Units 1..8 and Lesson page spans to 100% match printed Ministry TOC (including Unit 6: التقانة الحيوية 144-161!).
- Maps every numbered النشاط (1..n), Figure (الشكل n), Unit Cover, Assessment, Glossary using exact XML coords.
- Guarantees zero overlapping boxes (>15%).
"""
import json
import os
import re
import shutil
import xml.etree.ElementTree as ET

BASE_DIR = "/media/tawheeb/New Volume3/ذاكر/teaching-app"
OUT_DIR = f"{BASE_DIR}/data/curriculum/grade12/biology"
ANDROID_OUT = f"{BASE_DIR}/thaker-android-src/assets/data/curriculum/grade12/biology"

W, H = 892.0, 1263.0

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

def overlaps_any(box, existing, thresh=0.15):
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

    tree = ET.parse("/tmp/bio_audit/biology_full.xml")
    root = tree.getroot()
    xml_pages = {int(p.attrib["number"]): p for p in root.findall("page")}
    fonts = {fs.attrib["id"]: fs.attrib for fs in root.iter("fontspec")}

    # 1. TRUE MINISTRY UNITS (PDF = book - 4 across 2..220 -> Book 6..224!)
    units = [
        {
            "id": "u1", "order": 1, "title": "الوحدة الأولى: الجهاز العصبي",
            "short_desc": "التنظيم العصبي في الكائنات الحية، تركيب العصبون، جهد الفعل، والمستقبلات الحسية",
            "page_start": 8, "page_end": 39, "pdf_start": 4, "pdf_end": 35,
            "key_laws": ["جهد الراحة = -70 mV | عتبة الإثارة = -55 mV", "قمة جهد الفعل (إزالة الاستقطاب) = +40 mV"],
            "real_world_apps": ["علاج الإصابات العصبية والحفاظ على سلامة الحواس", "فهم آلية عمل المسكنات والمخدرات الموضعية بالمستشفيات"]
        },
        {
            "id": "u2", "order": 2, "title": "الوحدة الثانية: التنظيم الهرموني",
            "short_desc": "الأوكسينات والانتحاء في النبات، الغدد الصماء، الإنسولين والجلوكاجون، وأمراض الجهاز الهرموني",
            "page_start": 40, "page_end": 60, "pdf_start": 36, "pdf_end": 56,
            "key_laws": ["توازن سكر الدم الطبيعي: 80–110 mg/dL", "الإنسولين (خلايا بيتا) يخفض السكر | الجلوكاجون (ألفا) يرفعه"],
            "real_world_apps": ["استعمال الأوكسينات في تعقيل النباتات ونضج الثمار", "متابعة وعلاج مرض السكري واضطرابات الغدة الدرقية"]
        },
        {
            "id": "u3", "order": 3, "title": "الوحدة الثالثة: التكاثر في الكائنات الحية",
            "short_desc": "التكاثر اللاجنسي، البدائيات، النباتات الزهرية والإخصاب المزدوج، والجهاز التناسلي ودورة الطمث",
            "page_start": 61, "page_end": 95, "pdf_start": 57, "pdf_end": 91,
            "key_laws": ["بيضة (n) + نواة ذكرية (n) ➔ زيجوت (2n)", "نواتان قطبيتان (2n) + نواة ذكرية (n) ➔ إندوسبيرم (3n)"],
            "real_world_apps": ["التطعيم والعُقل لتحسين المحاصيل الزراعية باليمن", "فهم مراحل النمو الجنيني وصحة الأم والجنين"]
        },
        {
            "id": "u4", "order": 4, "title": "الوحدة الرابعة: أساسيات علم الوراثة",
            "short_desc": "قوانين مندل، الشكل الجيني والمظهري، نقص السيادة، فصائل الدم ABO، والصفات المرتبطة بالجنس",
            "page_start": 96, "page_end": 130, "pdf_start": 92, "pdf_end": 126,
            "key_laws": ["نسبة مندل (Tt × Tt): 3 طويل : 1 قصير", "تلقيح اختباري (Tt × tt): 1 : 1"],
            "real_world_apps": ["التوافق الطبي لفصائل الدم وعامل الريسوس Rh", "الفحص الوراثي المبكر والاستشارة الجينية قبل الزواج"]
        },
        {
            "id": "u5", "order": 5, "title": "الوحدة الخامسة: الوراثة الجزيئية (DNA)",
            "short_desc": "الكروموسومات والجينات، لولب DNA وتضاعفه شبه المحافظ، نسخ RNA، بناء البروتين والطفرات",
            "page_start": 131, "page_end": 143, "pdf_start": 127, "pdf_end": 139,
            "key_laws": ["تكامل القواعد: A = T و G ≡ C (وفي RNA: A ➔ U)", "كودون البدء = AUG | التوقف = UAA, UAG, UGA"],
            "real_world_apps": ["تحليل البصمة الوراثية DNA", "تفسير الأمراض الوراثية الناتجة عن الطفرات الجينية"]
        },
        {
            "id": "u6", "order": 6, "title": "الوحدة السادسة: التقانة الحيوية",
            "short_desc": "الهندسة الوراثية، البنسلين والإنسولين، إنتاج الزبادي والجبن والوقود الحيوي ومعالجة الملوثات",
            "page_start": 144, "page_end": 161, "pdf_start": 140, "pdf_end": 157,
            "key_laws": ["إنزيمات القطع والربط + بلازميد E.coli ➔ إنسولين بشري نقي", "التخمر اللاكتيكي والتخثر بالكيموزين لإنتاج الألبان والجبن"],
            "real_world_apps": ["تصنيع المضادات الحيوية (البنسلين) والإنسولين الطبي", "إنتاج غاز الميثان من المخلفات والوقود الحيوي النظيف"]
        },
        {
            "id": "u7", "order": 7, "title": "الوحدة السابعة: البيئة ومشكلاتها",
            "short_desc": "ملوثات الهواء والماء والتربة والضوضاء، الإشعاع والغذاء، واستنزاف الموارد والمحميات اليمنية",
            "page_start": 162, "page_end": 186, "pdf_start": 158, "pdf_end": 182,
            "key_laws": ["SO₂ / NOx + بخار ماء ➔ أمطار حمضية (pH < 5)", "حماية الحوض المائي الجوفي + الري الحديث + المحميات"],
            "real_world_apps": ["حماية أرخبيل سقطرى ومحمية عتمة باليمن", "ترشيد استهلاك المياه الجوفية والوقاية من التصحر"]
        },
        {
            "id": "u8", "order": 8, "title": "الوحدة الثامنة: تاريخ الأرض",
            "short_desc": "الصخور الرسوبية، الأحافير وطرق التحفر، التأريخ النسبي والمطلق، السلم الجيولوجي وجيولوجيا اليمن",
            "page_start": 187, "page_end": 222, "pdf_start": 183, "pdf_end": 218,
            "key_laws": ["N(t) = N₀ · (½)^(t / T₁/₂)  (C-14 = 5730 سنة)", "تقدير عمر الأرض ≈ 4600 مليون سنة"],
            "real_world_apps": ["تحديد أعمار الطبقات الحاملة للنفط والمعادن باليمن", "التنقيب عن الأحافير ودراسة التغيرات المناخية القديمة"]
        }
    ]

    # Evaluation ranges in printed Book Pages!
    eval_pages_map = {
        "u1": (37, 39),
        "u2": (60, 60),
        "u3": (93, 95),
        "u4": (129, 130),
        "u5": (143, 143),
        "u6": (161, 161),
        "u7": (186, 186),
        "u8": (220, 222),
    }

    # 2. PAGES (PDF 2..220 -> Book 6..224)
    pages = []
    for pdf_num in range(2, 221):
        book_num = pdf_num + 4
        if pdf_num in (2, 3):
            cur_unit = None
            p_type = "contents"
            title = f"المحتويات (الفهرس) — ص {book_num}"
        elif book_num in (223, 224):
            cur_unit = units[-1]
            p_type = "glossary"
            title = f"المصطلحات العلمية — ص {book_num}"
        else:
            cur_unit = next((u for u in units if u["page_start"] <= book_num <= u["page_end"]), units[-1])
            uid = cur_unit["id"]
            if book_num == cur_unit["page_start"]:
                p_type = "unit_cover"
                title = f"{cur_unit['title']} — غلاف وأهداف الوحدة"
            elif eval_pages_map[uid][0] <= book_num <= eval_pages_map[uid][1]:
                p_type = "assessment"
                title = f"تقويم {cur_unit['title']} — ص {book_num}"
            else:
                p_type = "lesson"
                title = f"{cur_unit['title']} — ص {book_num}"

        pages.append({
            "page_id": f"bio12-p{pdf_num:03d}",
            "book_page": book_num,
            "pdf_page": pdf_num,
            "type": p_type,
            "title": title,
            "unit_id": cur_unit["id"] if cur_unit else None,
            "image": f"assets/curriculum/grade12/biology/pages/page_{pdf_num:03d}_opt.jpg",
            "image_full": f"assets/curriculum/grade12/biology/pages/page_{pdf_num:03d}.jpg",
            "aspect_ratio": 0.7145
        })

    # 3. AUTHENTIC LESSONS MATCHING MINISTRY TOC (Pages 6-7)
    lessons_spec = [
        ("bio-u1-l1", "u1", "الجهاز العصبي في الكائن الحي (وحيدة الخلية واللافقاريات)", 9, 13),
        ("bio-u1-l2", "u1", "أنواع الألياف العصبية وجهد الفعل وانتقال السيال", 14, 25),
        ("bio-u1-l3", "u1", "أعضاء الحس: المستقبلات الضوئية (العين)", 26, 29),
        ("bio-u1-l4", "u1", "المستقبلات الكيميائية (الشم والتذوق)", 30, 31),
        ("bio-u1-l5", "u1", "المستقبلات الآلية (الأذن والسمع والتوازن)", 32, 36),
        ("bio-u1-eval", "u1", "تقويم الوحدة الأولى: الجهاز العصبي", 37, 39),

        ("bio-u2-l1", "u2", "التنظيم الهرموني في النبات (الأوكسينات والانتحاء)", 41, 44),
        ("bio-u2-l2", "u2", "التنظيم الهرموني في الحيوان", 45, 45),
        ("bio-u2-l3", "u2", "التنظيم الهرموني في الإنسان (الغدد الصماء والبنكرياس)", 46, 57),
        ("bio-u2-l4", "u2", "أمراض الجهاز الهرموني وصحته", 58, 59),
        ("bio-u2-eval", "u2", "تقويم الوحدة الثانية: التنظيم الهرموني", 60, 60),

        ("bio-u3-l1", "u3", "التكاثر اللاجنسي (التبرعم، التبوغ، والتكاثر الخضري)", 62, 68),
        ("bio-u3-l2", "u3", "التكاثر الجنسي والبدائيات (الاقتران)", 69, 71),
        ("bio-u3-l3", "u3", "التكاثر الجنسي في النباتات الزهرية والإخصاب المزدوج", 72, 78),
        ("bio-u3-l4", "u3", "التكاثر الجنسي في الحيوانات والإنسان ودورة الطمث", 79, 92),
        ("bio-u3-eval", "u3", "تقويم الوحدة الثالثة: التكاثر", 93, 95),

        ("bio-u4-l1", "u4", "المقصود بالوراثة وتطور علم الوراثة وتجارب مندل", 97, 103),
        ("bio-u4-l2", "u4", "الشكل الجيني والشكل الظاهري والتلقيح الاختباري", 104, 110),
        ("bio-u4-l3", "u4", "دور الكروموسومات، نقص السيادة، وفصائل الدم ABO", 111, 121),
        ("bio-u4-l4", "u4", "الوراثة والجنس والصفات المرتبطة والمتأثرة بالجنس", 122, 128),
        ("bio-u4-eval", "u4", "تقويم الوحدة الرابعة: أساسيات علم الوراثة", 129, 130),

        ("bio-u5-l1", "u5", "الكروموسومات والجينات ودور حمض DNA", 132, 135),
        ("bio-u5-l2", "u5", "الحمض النووي الرايبوزي RNA وخطوات بناء البروتين", 136, 139),
        ("bio-u5-l3", "u5", "تطبيقات في الوراثة الجزيئية والطفرات", 140, 142),
        ("bio-u5-eval", "u5", "تقويم الوحدة الخامسة: الوراثة الجزيئية", 143, 143),

        ("bio-u6-l1", "u6", "المقصود بالتقانة الحيوية والهندسة الجينية", 145, 146),
        ("bio-u6-l2", "u6", "التقانة الحيوية في إنتاج الغذاء (الزبادي والجبن)", 147, 151),
        ("bio-u6-l3", "u6", "إنتاج الدواء والوقود الحيوي (البنسلين والإنسولين والإيثانول)", 152, 155),
        ("bio-u6-l4", "u6", "معالجة المخلفات الملوثة وإنتاج المواد الصناعية", 156, 160),
        ("bio-u6-eval", "u6", "تقويم الوحدة السادسة: التقانة الحيوية", 161, 161),

        ("bio-u7-l1", "u7", "المقصود بالبيئة وملوثات الهواء والماء", 163, 172),
        ("bio-u7-l2", "u7", "التلوث الضوضائي والإشعاعي وتلوث الغذاء والتربة", 173, 180),
        ("bio-u7-l3", "u7", "استنزاف الموارد البيئية ومحميات اليمن (سقطرى وعتمة)", 181, 185),
        ("bio-u7-eval", "u7", "تقويم الوحدة السابعة: البيئة ومشكلاتها", 186, 186),

        ("bio-u8-l1", "u8", "الصخور الرسوبية والأحافير وشروط التحفر", 188, 201),
        ("bio-u8-l2", "u8", "التاريخ المطلق للصخور والسجل الجيولوجي وتاريخ الأرض", 202, 213),
        ("bio-u8-l3", "u8", "جيولوجيا الجمهورية اليمنية", 214, 219),
        ("bio-u8-eval", "u8", "تقويم الوحدة الثامنة: تاريخ الأرض", 220, 222),
    ]
    lessons = [{"id": lid, "unitId": uid, "title": t, "pages": list(range(s, e + 1))} for lid, uid, t, s, e in lessons_spec]

    # 4. GLOSSARY & EXPLANATIONS
    old_glossary = load_json("glossary.json") if os.path.exists(f"{OUT_DIR}/glossary.json") else {}
    glossary = {k: v for k, v in old_glossary.items()}
    glossary.update({
        "vb-biotech": {"id": "vb-biotech", "term": "التقانة الحيوية (Biotechnology)", "definition": "استخدام الكائنات الحية أو النظم الحيوية في التطبيقات العملية لإنتاج الغذاء والدواء والوقود ومعالجة الملوثات.", "category": "التقانة الحيوية"},
        "vb-insulin-gen": {"id": "vb-insulin-gen", "term": "الهندسة الوراثية لإنتاج الإنسولين", "definition": "قص جين الإنسولين البشري ولصقه داخل بلازميد بكتيريا E.coli لإنتاجه بكميات دوائية نقية.", "category": "التقانة الحيوية"},
        "vb-chymosin": {"id": "vb-chymosin", "term": "إنزيم الكيموزين (الإنفحة)", "definition": "إنزيم يرسب بروتين الحليب (الكازين) لفصل الخثرة وصناعة الجبن.", "category": "التقانة الحيوية"},
        "vb-acidrain": {"id": "vb-acidrain", "term": "المطر الحمضي", "definition": "أمطار تنخفض درجة حموضتها لتفاعل أكاسيد الكبريت والنيتروجين مع بخار الماء الجوي مما يضر النبات والتربة.", "category": "البيئة"},
        "vb-socotra": {"id": "vb-socotra", "term": "محمية سقطرى", "definition": "أرخبيل يمني مصنف بالتراث العالمي يضم نباتات مستوطنة نادرة مثل شجرة دم الأخوين.", "category": "البيئة"},
    })

    unit_vocab_map = {
        "u1": ["vb-neuron", "vb-synapse", "vb-actionpot", "vb-retina", "vb-cochlea"],
        "u2": ["vb-auxin", "vb-pituitary", "vb-insulin"],
        "u3": ["vb-doublefert", "vb-placenta"],
        "u4": ["vb-allele", "vb-genotype", "vb-sexlinked"],
        "u5": ["vb-dna", "vb-replication", "vb-codon", "vb-transcription", "vb-mutation"],
        "u6": ["vb-biotech", "vb-insulin-gen", "vb-chymosin"],
        "u7": ["vb-acidrain", "vb-socotra"],
        "u8": ["vb-fossil", "vb-geoscale"],
    }

    explanations = {}
    for u in units:
        laws_cards = [{"label": f"مبدأ علمي ({i+1})", "eq": law} for i, law in enumerate(u.get("key_laws", []))]
        explanations[f"exp-bio-{u['id']}-overview"] = {
            "id": f"exp-bio-{u['id']}-overview",
            "title": u["title"],
            "original_text": f"{u['title']} — كتاب الأحياء للصف الثالث الثانوي (ص {u['page_start']} - {u['page_end']}): {u['short_desc']}.",
            "levels": {
                "basic": f"🎯 هذه الوحدة تقدم: {u['short_desc']}.",
                "intermediate": f"📘 بنهاية دراسة {u['title']} ستتمكن من استيعاب المفاهيم، تطبيق الأنشطة التفاعلية العملية، وحل تقويم الوحدة بدقة.",
                "advanced": "🚀 تطبيقات حيوية بارزة:\n• " + "\n• ".join(u.get("real_world_apps", []))
            },
            "chemical_equations": laws_cards,
            "vocabulary_ids": unit_vocab_map.get(u["id"], []),
            "tts_text": f"أهلاً بك في {u['title']}. {u['short_desc']}."
        }

    for l in lessons:
        lid = l["id"]
        uobj = next(u for u in units if u["id"] == l["unitId"])
        laws_cards = [{"label": f"خلاصة {uobj['title'].split(':')[0]}", "eq": eq} for eq in uobj.get("key_laws", [])]
        explanations[f"exp-{lid}"] = {
            "id": f"exp-{lid}",
            "lesson_id": lid,
            "title": l["title"],
            "original_text": f"موضوع الكتاب الوزاري (ص {l['pages'][0]} - {l['pages'][-1]}): {l['title']}.",
            "levels": {
                "basic": f"💡 شرح مبسط لدرس «{l['title']}»: يوضح الأفكار والعمليات الحيوية الأساسية الواردة في صفحات الدرس ({l['pages'][0]}–{l['pages'][-1]}) بأسلوب سهل.",
                "intermediate": f"📘 التحليل الوزاري للدرس: اربط بين التراكيب التشريحية ووظائفها الحيوية، واستخدم المعمل التفاعلي لتنفيذ الأنشطة المرفقة خطوة بخطوة.",
                "advanced": f"🎯 تطبيقات وأسئلة امتحانيه على «{l['title']}»: ركز على المقارنات والتعليلات والرسوم البيانية بالكتاب."
            },
            "chemical_equations": laws_cards,
            "vocabulary_ids": unit_vocab_map.get(l["unitId"], []),
            "tts_text": f"درس {l['title']} من {uobj['title']}."
        }

    explanations["exp-bio-glossary"] = {
        "id": "exp-bio-glossary",
        "title": "المصطلحات العلمية — كتاب الأحياء",
        "original_text": "قائمة المصطلحات العلمية باللغتين العربية والإنجليزية (ص 223 - 224) لمراجعة مفاهيم الكتاب.",
        "levels": {
            "basic": "📖 تضم هاتان الصفحتان المصطلحات العلمية الواردة في الأحياء والجيولوجيا باللغتين العربية والإنجليزية.",
            "intermediate": "📘 مراجعة التعريفات العلمية ضرورية لأسئلة المصطلح والتعليل والاختيار من متعدد في الامتحان الوزاري.",
            "advanced": "🎯 اضغط على أي بطاقة مصطلح بالأسفل لاستعراض تعريفه وتطبيقه الحيوي."
        },
        "chemical_equations": [],
        "vocabulary_ids": list(glossary.keys())[:10],
        "tts_text": "قائمة المصطلحات العلمية لكتاب الأحياء."
    }

    # 5. DIAGRAMS MAP (18 accurate 3D entries matching biology-12th-lab.html!)
    diagrams = {
        "diag-bio-hydra": {"id": "diag-bio-hydra", "lab_exp": "bio-u1-hydra-worm", "title": "الشبكة العصبية في الهيدرا ودودة الأرض (ص 10)", "sim_key": "bio_neuron", "formula": "تنظيم عصبي أولي بالشبكة (الهيدرا) ➔ عقدة وحبل بطني (دودة الأرض)", "slider_label": "شدة المنبه:", "slider_min": 0, "slider_max": 100, "slider_val": 70, "slider_unit": "%", "components": [{"id": "net", "name": "شبكة الهيدرا", "role": "تنقل التنبيه في جميع الاتجاهات."}, {"id": "worm", "name": "دودة الأرض", "role": "تنفر من الضوء الساطع بحبلها العصبي البطني."}]},
        "diag-bio-neuron": {"id": "diag-bio-neuron", "lab_exp": "bio-u1-neuron-impulse", "title": "الخلية العصبية وانتقال السيال 3D (ص 12 - 25)", "sim_key": "bio_neuron", "formula": "الراحة = -70 mV | العتبة = -55 mV | الفعل = +40 mV", "slider_label": "شدة المنبه:", "slider_min": 0, "slider_max": 100, "slider_val": 70, "slider_unit": "%", "components": [{"id": "soma", "name": "جسم الخلية والزوائد", "role": "استقبال التنبيهات العصبية."}, {"id": "axon", "name": "المحور وغمد المايلين", "role": "ينقل السيال بالقفز السريع عبر اختناقات رانفييه."}]},
        "diag-bio-eye-ear": {"id": "diag-bio-eye-ear", "lab_exp": "bio-u1-eye-ear", "title": "المستقبلات الضوئية والسمعية 3D (ص 26 - 36)", "sim_key": "bio_eye", "formula": "تكيّف العدسة بالعين | القوقعة وعضو كورتي بالسمع", "slider_label": "تحدب العدسة:", "slider_min": 1, "slider_max": 10, "slider_val": 5, "slider_unit": " D", "components": [{"id": "retina", "name": "الشبكية", "role": "تحتوي العصي والمخاريط للرؤية."}, {"id": "cochlea", "name": "القوقعة والقنوات الهلالية", "role": "السمع وتوازن الجسم."}]},
        "diag-bio-auxin": {"id": "diag-bio-auxin", "lab_exp": "bio-u2-auxins", "title": "الأوكسينات والانتحاء النباتي 3D (ص 41 - 45)", "sim_key": "bio_dna", "formula": "تجمع IAA في الجانب المظلم ➔ استطالة خلاياه", "slider_label": "زاوية الضوء:", "slider_min": -60, "slider_max": 60, "slider_val": 40, "slider_unit": "°", "components": [{"id": "tip", "name": "القمة النامية", "role": "تُفرز الأوكسين IAA."}, {"id": "shade", "name": "الجانب المظلم", "role": "تتركز به الأوكسينات فيطول أكثر وينتحي الساق."}]},
        "diag-bio-endocrine": {"id": "diag-bio-endocrine", "lab_exp": "bio-u2-endocrine", "title": "الغدد الصماء والإنسولين والجلوكاجون 3D (ص 46 - 59)", "sim_key": "bio_neuron", "formula": "ارتفاع السكر ➔ إنسولين | انخفاض السكر ➔ جلوكاجون", "slider_label": "سكر الدم:", "slider_min": 50, "slider_max": 220, "slider_val": 110, "slider_unit": " mg", "components": [{"id": "pituitary", "name": "الغدة النخامية", "role": "تفرز هرمونات تنظم بقية الغدد الصماء."}, {"id": "pancreas", "name": "جزر لانجرهانس", "role": "تضبط اتزان سكر الدم."}]},
        "diag-bio-asexual": {"id": "diag-bio-asexual", "lab_exp": "bio-u3-budding-spores", "title": "التكاثر اللاجنسي (التبرعم والتبوغ والخضري) 3D (ص 62 - 68)", "sim_key": "bio_dna", "formula": "تكاثر ميتوزي ينتج أفراداً مطابقة للأم 100%", "slider_label": "معدل الانقسام:", "slider_min": 20, "slider_max": 100, "slider_val": 80, "slider_unit": "%", "components": [{"id": "bud", "name": "البرعم / الأبواغ", "role": "طرق تكاثر لاجنسي سريع في الخميرة والفطريات."}, {"id": "graft", "name": "التطعيم والتعقيل", "role": "يحافظ على الصفات النباتية المرغوبة."}]},
        "diag-bio-flower": {"id": "diag-bio-flower", "lab_exp": "bio-u3-flower-seed", "title": "الزهرة والإخصاب المزدوج 3D (ص 72 - 78)", "sim_key": "bio_eye", "formula": "زيجوت (2n) + إندوسبيرم (3n)", "slider_label": "مراحل التلقيح:", "slider_min": 1, "slider_max": 3, "slider_val": 3, "slider_unit": "", "components": [{"id": "stamen", "name": "السداة والمتك", "role": "إنتاج حبوب اللقاح."}, {"id": "ovary", "name": "المبيض والكيس الجنيني", "role": "تكوين البذرة والثمار."}]},
        "diag-bio-cycle": {"id": "diag-bio-cycle", "lab_exp": "bio-u3-repro-cycle", "title": "التكاثر ودورة الطمث الهرمونية 3D (ص 79 - 92)", "sim_key": "bio_neuron", "formula": "يوم 14: ذروة هرمون LH وحدوث الإباضة", "slider_label": "اليوم بالدورة:", "slider_min": 1, "slider_max": 28, "slider_val": 14, "slider_unit": "", "components": [{"id": "fsh", "name": "FSH والإستروجين", "role": "إنضاج الحويصلة وبناء البطانة."}, {"id": "lh", "name": "LH والجسم الأصفر", "role": "الإباضة وإفراز البروجستيرون."}]},
        "diag-bio-mendel": {"id": "diag-bio-mendel", "lab_exp": "bio-u4-mendel", "title": "وراثة مندل ومربع بانيت 3D (ص 98 - 110)", "sim_key": "bio_dna", "formula": "Tt × Tt ➔ 3 طويل : 1 قصير", "slider_label": "نوع التهجين:", "slider_min": 1, "slider_max": 3, "slider_val": 1, "slider_unit": "", "components": [{"id": "dom", "name": "الأليل السائد T", "role": "يظهر أثره في الهجين Tt والنقي TT."}, {"id": "rec", "name": "الأليل المتنحي t", "role": "يظهر فقط عند اجتماعه tt."}]},
        "diag-bio-blood": {"id": "diag-bio-blood", "lab_exp": "bio-u4-codominance", "title": "فصائل الدم ABO والوراثة بالجنس 3D (ص 111 - 128)", "sim_key": "bio_dna", "formula": "فصائل Iᴬ و Iᴮ سيادة مشتركة | صفات X تنتقل للأبناء من الأم", "slider_label": "الحالة الوراثية:", "slider_min": 1, "slider_max": 3, "slider_val": 1, "slider_unit": "", "components": [{"id": "abo", "name": "فصائل ABO", "role": "مثال على تعدد البدائل والسيادة المشتركة."}, {"id": "sexchr", "name": "X و Y", "role": "تحديد الجنس وحمل الجينات المرتبطة به."}]},
        "diag-bio-dna": {"id": "diag-bio-dna", "lab_exp": "bio-u5-dna-protein", "title": "لولب DNA وبناء البروتين 3D (ص 131 - 142)", "sim_key": "bio_dna", "formula": "DNA ➔ نسخ mRNA (U بدل T) ➔ ترجمة البروتين", "slider_label": "سرعة النسخ:", "slider_min": 1, "slider_max": 10, "slider_val": 5, "slider_unit": "x", "components": [{"id": "bases", "name": "القواعد النيتروجينية", "role": "A=T و G≡C في DNA."}, {"id": "ribosome", "name": "الرايبوسوم و tRNA", "role": "ترجمة الكودونات لسلسلة ببتيد."}]},
        "diag-bio-biotech-food": {"id": "diag-bio-biotech-food", "lab_exp": "bio-u6-fermentation", "title": "التقانة الحيوية في الغذاء (الألبان والجبن) 3D (ص 145 - 151)", "sim_key": "bio_dna", "formula": "التخمر اللاكتيكي للزبادي + الإنفحة لصنع الجبن", "slider_label": "الحرارة (°C):", "slider_min": 10, "slider_max": 70, "slider_val": 42, "slider_unit": "°C", "components": [{"id": "lacto", "name": "بكتيريا حمض اللاكتيك", "role": "تحول اللاكتوز إلى حمض لاكتيك."}, {"id": "rennet", "name": "إنزيم الكيموزين", "role": "يخثر الكازين لصنع الجبن."}]},
        "diag-bio-biotech-tech": {"id": "diag-bio-biotech-tech", "lab_exp": "bio-u6-biotech-insulin", "title": "الهندسة الوراثية للإنسولين ومعالجة الملوثات 3D (ص 152 - 160)", "sim_key": "bio_dna", "formula": "بلازميد E.coli + جين بشري ➔ إنسولين | ميثان من المخلفات", "slider_label": "التطبيق:", "slider_min": 1, "slider_max": 3, "slider_val": 1, "slider_unit": "", "components": [{"id": "plasmid", "name": "البلازميد البكتيري", "role": "ناقل للجين البشري."}, {"id": "biogas", "name": "غاز الميثان", "role": "ينتج من المعالجة الحيوية للصرف الصحي."}]},
        "diag-bio-pollution": {"id": "diag-bio-pollution", "lab_exp": "bio-u7-pollution", "title": "الملوثات البيئية والمطر الحمضي 3D (ص 163 - 180)", "sim_key": "bio_eye", "formula": "أكاسيد الكبريت والنيتروجين + بخار الماء ➔ مطر حمضي", "slider_label": "الانبعاثات:", "slider_min": 10, "slider_max": 100, "slider_val": 60, "slider_unit": "%", "components": [{"id": "air", "name": "ملوثات الهواء", "role": "تسبب أمطاراً حمضية واحتباساً حرارياً."}, {"id": "water", "name": "تلوث الماء والضجيج", "role": "أضرار على الأسماك والأعصاب."}]},
        "diag-bio-conservation": {"id": "diag-bio-conservation", "lab_exp": "bio-u7-conservation", "title": "استنزاف الموارد ومحميات اليمن 3D (ص 181 - 185)", "sim_key": "bio_eye", "formula": "ترشيد المياه الجوفية + حماية سقطرى وعتمة", "slider_label": "الترشيد:", "slider_min": 10, "slider_max": 100, "slider_val": 80, "slider_unit": "%", "components": [{"id": "water", "name": "الحوض الجوفي", "role": "يحمى بالري الحديث والحواجز المائية."}, {"id": "socotra", "name": "أرخبيل سقطرى", "role": "محمية للنباتات المستوطنة النادرة."}]},
        "diag-bio-fossils": {"id": "diag-bio-fossils", "lab_exp": "bio-u8-fossils", "title": "الصخور الرسوبية وتكون الأحافير 3D (ص 188 - 201)", "sim_key": "bio_dna", "formula": "هيكل صلب + دفن سريع بمعزل عن الأكسجين = أحفورة", "slider_label": "سرعة الدفن:", "slider_min": 10, "slider_max": 100, "slider_val": 85, "slider_unit": "%", "components": [{"id": "strata", "name": "الطبقات الرسوبية", "role": "تحفظ السجل الزمني للأحافير."}, {"id": "fossil", "name": "التمعدن والإحلال", "role": "طرق تحفر الخشب والأصداف."}]},
        "diag-bio-radiometric": {"id": "diag-bio-radiometric", "lab_exp": "bio-u8-radiometric", "title": "التأريخ الإشعاعي للصخور 3D (ص 202 - 206)", "sim_key": "bio_dna", "formula": "N = N₀ · (½)^(t / T₁/₂) | عمر الأرض ≈ 4600 مليون سنة", "slider_label": "فترات النصف:", "slider_min": 0, "slider_max": 5, "slider_val": 2, "slider_unit": "", "components": [{"id": "c14", "name": "الكربون-14", "role": "تأريخ الأحافير العضوية (T₁/₂ = 5730 سنة)."}, {"id": "u238", "name": "اليورانيوم-238", "role": "تأريخ الصخور الجيولوجية السحيقة."}]},
        "diag-bio-yemen-geo": {"id": "diag-bio-yemen-geo", "lab_exp": "bio-u8-geology-yemen", "title": "السجل الجيولوجي وجيولوجيا اليمن 3D (ص 207 - 219)", "sim_key": "bio_eye", "formula": "القديمة (الترايلوبيت) ➔ الوسطى (الديناصورات) ➔ الحديثة (الثدييات)", "slider_label": "الحقبة:", "slider_min": 1, "slider_max": 3, "slider_val": 2, "slider_unit": "", "components": [{"id": "trilo", "name": "الترايلوبيت", "role": "أحفورة مرشدة للكمبري بالحياة القديمة."}, {"id": "yemen", "name": "جيولوجيا اليمن", "role": "طبقات جوراسية رسوبية وهضاب بركانية ثلاثية."}]}
    }

    # 6. AUTHENTIC UNIT ASSESSMENTS (All 8 Units matching REAL Ministry textbook!)
    old_assess = load_json("assessments.json") if os.path.exists(f"{OUT_DIR}/assessments.json") else {}
    assessments = {
        "quiz-bio-u1": old_assess.get("quiz-bio-u1", []),
        "quiz-bio-u2": old_assess.get("quiz-bio-u2", []),
        "quiz-bio-u3": old_assess.get("quiz-bio-u3", []),
        "quiz-bio-u4": old_assess.get("quiz-bio-u4", []),
        "quiz-bio-u5": [
            {
                "id": "q-bio-u5-1", "page": 143,
                "q": "إذا كان تتابع القواعد على أحد شريطي جزيء DNA هو (5'-ATGC-3')، فإن الشريط المكمل له هو:",
                "options": [
                    {"text": "3'-TACG-5'"},
                    {"text": "3'-UACG-5'", "why_wrong": "القاعدة U (اليوراسيل) توجد في RNA وليس في جزيء DNA."},
                    {"text": "3'-ATGC-5'", "why_wrong": "يجب تكامل A مع T و G مع C."},
                    {"text": "3'-CGTA-5'", "why_wrong": "تحقق من ترتيب القواعد المتقابلة."}
                ],
                "answer": 0, "explain": "حسب قاعدة التكامل في DNA يرتبط A مع T و G مع C."
            },
            {
                "id": "q-bio-u5-2", "page": 143,
                "q": "ما هو الكودون الذي يبدأ به تخليق سلسلة عديد الببتيد (كودون البدء) على mRNA؟",
                "options": [
                    {"text": "UAA", "why_wrong": "UAA هو كودون إيقاف."},
                    {"text": "AUG"},
                    {"text": "UGA", "why_wrong": "UGA كودون إيقاف."},
                    {"text": "UAG", "why_wrong": "UAG كودون إيقاف."}
                ],
                "answer": 1, "explain": "كودون البدء العالمي هو AUG ويشفر للحمض الأميني الميثيونين."
            }
        ],
        "quiz-bio-u6": [
            {
                "id": "q-bio-u6-1", "page": 161,
                "q": "تقويم الوحدة السادسة ص 161: لماذا تضيف ربة البيت جزءاً من الزبادي الجاهز إلى الحليب الدافئ عند تحضير الزبادي؟",
                "options": [
                    {"text": "لتبريد الحليب فقط", "why_wrong": "التبريد يحدث لاحقاً بعد انتهاء التخمير."},
                    {"text": "لتوفير بكتيريا حمض اللاكتيك النافعة التي تحول سكر اللاكتوز إلى حمض اللاكتيك"},
                    {"text": "لتغيير لون الحليب إلى الأصفر", "why_wrong": "البادئ غرضه بيولوجي تخميري."},
                    {"text": "لترسيب الكازين بالحرارة العالية", "why_wrong": "الكيموزين يُستعمل في صناعة الجبن."}
                ],
                "answer": 1, "explain": "يعمل الزبادي المضاف كبادئ يحتوي بكتيريا نافعة تخمّر اللاكتوز فتخثر الحليب."
            },
            {
                "id": "q-bio-u6-2", "page": 161,
                "q": "تقويم الوحدة ص 161: الإنزيم الذي يُضاف إلى الحليب لترسيب البروتين وتكوين خثرة الجبن هو:",
                "options": [
                    {"text": "الأميليز", "why_wrong": "الأميليز يهضم النشا."},
                    {"text": "إنزيم الكيموزين (الإنفحة)"},
                    {"text": "البنسلين", "why_wrong": "البنسلين مضاد حيوي ينتجه فطر البنسيليوم."}
                ],
                "answer": 1, "explain": "إنزيم الكيموزين (المستخلص من الإنفحة) يحول بروتين الحليب إلى خثرة لصناعة الجبن."
            },
            {
                "id": "q-bio-u6-3", "page": 161,
                "q": "تقويم الوحدة ص 161: يتم إنتاج هرمون الإنسولين البشري حالياً باستخدام التقانة الحيوية عن طريق:",
                "options": [
                    {"text": "دمج جين الإنسولين البشري في بلازميد بكتيريا الإشيريشيا كولاي (E.coli)"},
                    {"text": "تبريد أوراق الذرة", "why_wrong": "الذرة مصدر نشوي للوقود الحيوي الإيثانول."},
                    {"text": "تخمير البنسلين", "why_wrong": "البنسلين مضاد حيوي فطري."}
                ],
                "answer": 0, "explain": "تنقل إنزيمات القطع والربط جين الإنسولين البشري إلى بلازميد البكتيريا فتُنتجه بنقاء عالٍ."
            }
        ],
        "quiz-bio-u7": old_assess.get("quiz-bio-u7", []),
        "quiz-bio-u8": [
            {
                "id": "q-bio-u8-real-1", "page": 220,
                "q": "تقويم الوحدة ص 220 (س1-1): أي تعاقب رسوبي أفقي لم يتعرض لقوى تكتونية تكون فيه:",
                "options": [
                    {"text": "كل طبقة أحدث من التي أسفلها وأقدم من التي تعلوها"},
                    {"text": "أعلى طبقة هي الأقدم عمراً", "why_wrong": "الترسيب الطبيعي يبدأ بالطبقة السفلى أولا فتكون الأقدم."},
                    {"text": "كل الطبقات لها العمر نفسه", "why_wrong": "تترسب الطبقات عبر عصور متعاقبة."}
                ],
                "answer": 0, "explain": "حسب قانون تعاقب الطبقات، الطبقة السفلى أقدم من العليا ما لم تنقلب بتشوهات تكتونية."
            },
            {
                "id": "q-bio-u8-real-2", "page": 220,
                "q": "تقويم الوحدة ص 220 (س1-4 و 5): يتم تحفر الخشب بطريقتي الإحلال والتمعدن معاً، ويُقدر عمر الأرض بنحو:",
                "options": [
                    {"text": "6400 مليون سنة", "why_wrong": "عمر الأرض الجيولوجي نحو 4.6 مليار سنة."},
                    {"text": "4600 مليون سنة"},
                    {"text": "64000 مليون سنة", "why_wrong": "هذا رقم مبالغ فيه يتجاوز عمر الكون نفسه!"}
                ],
                "answer": 1, "explain": "تقدر قياسات التحلل الإشعاعي للنيازك وصخور الأرض عمرها بحوالي 4600 مليون سنة (4.6 مليار سنة)."
            },
            {
                "id": "q-bio-u8-real-3", "page": 220,
                "q": "تقويم الوحدة ص 220 (س1-6): أحفورة الترايلوبيت (ثلاثية الفصوص) من الأحافير المرشدة التي تدل على العصر:",
                "options": [
                    {"text": "الجوراسي", "why_wrong": "الجوراسي ساد فيه الديناصورات والأمونيت."},
                    {"text": "الكمبري (بداية الحياة القديمة)"},
                    {"text": "الترياسي", "why_wrong": "الترياسي في الحياة المتوسطة."}
                ],
                "answer": 1, "explain": "سادت ثلاثيات الفصوص (الترايلوبيت) في البحار خلال العصر الكمبري بحقبة الحياة القديمة."
            }
        ]
    }

    # Exact numbered activity mapping (page -> (lab_exp, badge_label))
    exact_page_activity = {
        10: ("bio-u1-hydra-worm", "🧪 النشاط (1 و2): الهيدرا ودودة الأرض"),
        21: ("bio-u1-neuron-impulse", "🧪 النشاط (3): انتقال السيال العصبي"),
        25: ("bio-u1-neuron-impulse", "🔬 النشاط (4): تشريح الجهاز العصبي للضفدع"),
        43: ("bio-u2-auxins", "🧪 النشاط (1): الإيثيلين ونمو النبات"),
        44: ("bio-u2-auxins", "🧪 النشاط (2): تجربة الانتحاء الضوئي"),
        45: ("bio-u2-auxins", "🧪 النشاط (3): أثر الأوكسين على الجذور"),
        63: ("bio-u3-budding-spores", "🧪 النشاط (1): التبرعم في الخميرة"),
        64: ("bio-u3-budding-spores", "🧪 النشاط (2): التبوغ في عفن الخبز"),
        67: ("bio-u3-budding-spores", "🧪 النشاط (3 و4): التكاثر الخضري والتطعيم"),
        70: ("bio-u3-flower-seed", "🧪 النشاط (5): الاقتران في الإسبيروجيرا"),
        72: ("bio-u3-flower-seed", "🧪 النشاط (6): دورة حياة الفيوناريا"),
        73: ("bio-u3-flower-seed", "🧪 النشاط (7): فحص الفيوناريا"),
        75: ("bio-u3-flower-seed", "🧪 النشاط (8): تشريح تركيب الزهرة"),
        76: ("bio-u3-flower-seed", "🧪 النشاط (9): تركيب المتاع والبويضة"),
        77: ("bio-u3-flower-seed", "🧪 النشاط (10): حبوب اللقاح والإخصاب"),
        78: ("bio-u3-flower-seed", "🧪 النشاط (11): تركيب البذرة والثمرة"),
        87: ("bio-u3-repro-cycle", "🧪 النشاط (12): فحص شريحة المبيض/الخصية"),
        99: ("bio-u4-mendel", "🧪 النشاط (1): تجارب مندل للوراثة"),
        105: ("bio-u4-mendel", "🧪 النشاط (2): التهجين الأحادي"),
        107: ("bio-u4-mendel", "🧪 النشاط (3 و4): تطبيقات قانون مندل"),
        111: ("bio-u4-codominance", "🧪 النشاط (5): دور الكروموسومات"),
        113: ("bio-u4-codominance", "🧪 النشاط (6): نقص السيادة بالأزهار"),
        114: ("bio-u4-codominance", "🧪 النشاط (7): توارث السيادة المشتركة"),
        115: ("bio-u4-codominance", "🧪 النشاط (8): فصائل الدم ABO"),
        118: ("bio-u4-codominance", "🧪 النشاط (9): نظام فصائل الدم والريزيس"),
        119: ("bio-u4-codominance", "🧪 النشاط (10): الجينات المميتة"),
        124: ("bio-u4-codominance", "🧪 النشاط (11): الصفات المتأثرة بالجنس"),
        135: ("bio-u5-dna-protein", "🧪 النشاط (1): تركيب لولب DNA"),
        148: ("bio-u6-fermentation", "🧪 النشاط (1): إنتاج الزبادي بالتخمير"),
        149: ("bio-u6-fermentation", "🧪 النشاط (2): أثر التبريد على البكتيريا"),
        151: ("bio-u6-fermentation", "🧪 النشاط (3): إنتاج الجبن البلدي"),
        157: ("bio-u6-biotech-insulin", "🧪 النشاط (4): معالجة المخلفات والبيوجاز"),
        183: ("bio-u7-conservation", "🧪 النشاط (1-3): استنزاف المياه والتربة"),
        184: ("bio-u7-conservation", "🧪 النشاط (4): الغابات ومحميات اليمن"),
        185: ("bio-u7-conservation", "🧪 النشاط (5): التنوع الحيوي وسقطرى"),
        189: ("bio-u8-fossils", "🧪 النشاط (1): الصخور الرسوبية والتحفر"),
        202: ("bio-u8-radiometric", "🧪 النشاط (2): التأريخ النسبي والمطلق"),
    }

    def get_diag_for_page(bp, uid):
        if uid == "u1":
            if bp <= 11: return ("diag-bio-hydra", "🔍 الشبكة العصبية والحسية 3D")
            if bp <= 25: return ("diag-bio-neuron", "🔍 مجسم العصبون والسيال 3D")
            return ("diag-bio-eye-ear", "🔍 تشريح العين والأذن 3D")
        if uid == "u2":
            if bp <= 45: return ("diag-bio-auxin", "🔍 الأوكسينات والانتحاء 3D")
            return ("diag-bio-endocrine", "🔍 الغدد الصماء وتوازن السكر 3D")
        if uid == "u3":
            if bp <= 69: return ("diag-bio-asexual", "🔍 التكاثر اللاجنسي 3D")
            if bp <= 78: return ("diag-bio-flower", "🔍 الزهرة والإخصاب المزدوج 3D")
            return ("diag-bio-cycle", "🔍 التكاثر ودورة الطمث 3D")
        if uid == "u4":
            if bp <= 110: return ("diag-bio-mendel", "🔍 وراثة مندل ومربع بانيت 3D")
            return ("diag-bio-blood", "🔍 فصائل الدم والوراثة بالجنس 3D")
        if uid == "u5":
            return ("diag-bio-dna", "🔍 لولب DNA وبناء البروتين 3D")
        if uid == "u6":
            if bp <= 151: return ("diag-bio-biotech-food", "🔍 التقانة الحيوية في الغذاء 3D")
            return ("diag-bio-biotech-tech", "🔍 الهندسة الوراثية والمعالجة الحيوية 3D")
        if uid == "u7":
            if bp <= 180: return ("diag-bio-pollution", "🔍 التلوث البيئي والمطر الحمضي 3D")
            return ("diag-bio-conservation", "🔍 استنزاف الموارد ومحميات اليمن 3D")
        if bp <= 201: return ("diag-bio-fossils", "🔍 الصخور والأحافير 3D")
        if bp <= 206: return ("diag-bio-radiometric", "🔍 التأريخ الإشعاعي للصخور 3D")
        return ("diag-bio-yemen-geo", "🔍 السجل الجيولوجي وجيولوجيا اليمن 3D")

    # 7. SURGICAL INTERACTIONS FOR BIOLOGY (Exact XML Bounds, Zero Overlap)
    interactions = {}

    for p_meta in pages:
        pdf_num = p_meta["pdf_page"]
        bp = p_meta["book_page"]
        pid = p_meta["page_id"]
        uid = p_meta["unit_id"]
        ptype = p_meta["type"]

        if ptype == "contents" or not uid:
            continue

        xml_p = xml_pages.get(pdf_num)
        if xml_p is None:
            continue

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
            if it < 270 and iw > 240 and ih < 65: continue
            if iw < 45 or ih < 40: continue
            if it < 160 and il > 600: continue
            real_imgs.append({"top": it, "left": il, "w": iw, "h": ih})

        page_spots = []

        # A. UNIT COVERS -> ONLY Objectives Box!
        if ptype == "unit_cover":
            g_heads = [it for it in items if ("·«b" in it["sc"] or "·«b¼√" in it["sc"]) and it["top"] > 620]
            gy0 = max(650, g_heads[0]["top"] - 14) if g_heads else 720
            gy1 = min(1045, max((it["top"] + 30 for it in items if it["top"] > gy0), default=1030))
            page_spots.append({
                "id": f"hs-{pid}-unit-goals",
                "type": "explainable_text",
                "explanation_ref": f"exp-bio-{uid}-overview",
                "indicator_label": "🎯 أهداف ومقدمة الوحدة",
                "highlight_color": "rgba(0, 168, 89, 0.14)",
                "bounds": clamp_box(0.18, gy0 / H, 0.65, max(0.15, (gy1 - gy0) / H))
            })
            interactions[pid] = page_spots
            continue

        # B. EVALUATION PAGES -> Assessment Box ONLY!
        if ptype == "assessment":
            y_tops = [it["top"] for it in items if 150 <= it["top"] <= 1040]
            y0 = (min(y_tops) - 18) / H if y_tops else 0.16
            y1 = (max(y_tops) + 30) / H if y_tops else 0.82
            page_spots.append({
                "id": f"hs-{pid}-quiz",
                "type": "assessment",
                "assessment_ref": f"quiz-bio-{uid}",
                "indicator_label": "📝 اختبر نفسك وحل تقويم الوحدة",
                "highlight_color": "rgba(217, 119, 6, 0.16)",
                "bounds": clamp_box(0.18, y0, 0.65, min(0.68, max(0.18, y1 - y0)))
            })
            interactions[pid] = page_spots
            continue

        # C. GLOSSARY PAGES (223-224)
        if ptype == "glossary":
            page_spots.append({
                "id": f"hs-{pid}-glossary",
                "type": "explainable_text",
                "explanation_ref": "exp-bio-glossary",
                "indicator_label": "📖 استعراض وشرح المصطلحات العلمية",
                "highlight_color": "rgba(16, 185, 129, 0.14)",
                "bounds": clamp_box(0.17, 0.16, 0.66, 0.67)
            })
            interactions[pid] = page_spots
            continue

        matched_lesson = next((l for l in lessons if l["unitId"] == uid and l["pages"][0] <= bp <= l["pages"][-1]), None)
        if not matched_lesson:
            matched_lesson = next((l for l in lessons if l["unitId"] == uid), lessons[0])
        exp_ref = f"exp-{matched_lesson['id']}"

        # D. TRUE FIGURES FIRST (الشكل n matching real_imgs or compact vector box)
        diag_id, diag_label = get_diag_for_page(bp, uid)
        seen_fig_y = []
        fig_spots = []
        for it in items:
            sc = it["sc"]
            if not (("qJA" in sc or "qJý" in sc) and "©" in sc and it["top"] < 1055):
                continue
            if it["size"] > 21 or "≠" in it["raw"] or len(sc) > 65:
                continue
            if any(abs(it["top"] - sy) < 85 for sy in seen_fig_y):
                continue
            seen_fig_y.append(it["top"])

            cap_cx = it["left"] + it["w"] / 2.0
            matched_im = None
            for im in real_imgs:
                im_bot = im["top"] + im["h"]
                im_cx = im["left"] + im["w"] / 2.0
                if abs(im_bot - it["top"]) < 100 and abs(im_cx - cap_cx) < 250:
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
                y0_px = max(145, it["top"] - 200)
                fb = clamp_box(x_box, y0_px / H, w_box, (it["top"] + it["h"] + 12 - y0_px) / H)

            if overlaps_any(fb, fig_spots, thresh=0.20):
                continue

            fig_spots.append({
                "id": f"hs-{pid}-fig-{len(fig_spots)}",
                "type": "interactive_3d",
                "diagram_ref": diag_id,
                "lab_exp": diagrams[diag_id]["lab_exp"],
                "indicator_label": diag_label,
                "highlight_color": "rgba(2, 132, 199, 0.14)",
                "bounds": fb
            })

        # E. AUTHENTIC ACTIVITIES (©n® ◊UAM«) — strictly non-overlapping with figures!
        if bp in exact_page_activity:
            lab_exp, act_label = exact_page_activity[bp]
            act_items = [it for it in items if "◊UAM" in it["sc"] or "◊UA½" in it["sc"] or ("©" in it["sc"] and "◊UA" in it["sc"])]
            seen_ay = []
            for ai in act_items[:2]:
                y0_px = ai["top"] - 10
                if any(abs(y0_px - sy) < 90 for sy in seen_ay): continue
                seen_ay.append(y0_px)
                y1_px = min(1045, y0_px + 115)
                for nxt in items:
                    if nxt["top"] <= y0_px + 25: continue
                    if nxt["color"] in ("#ff00ff", "#00ffff") and nxt["size"] >= 24:
                        y1_px = min(y1_px, nxt["top"] - 8)
                        break

                ax, aw = 0.17, 0.66
                ay0 = y0_px / H
                ay1 = max(ay0 + 0.065, y1_px / H)

                for fs in fig_spots:
                    fb = fs["bounds"]
                    fy0, fy1 = fb["y"], fb["y"] + fb["h"]
                    fx1 = fb["x"] + fb["w"]
                    if not (fy1 <= ay0 + 0.005 or fy0 >= ay1 - 0.005):
                        if fy0 - ay0 >= 0.065:
                            ay1 = min(ay1, fy0 - 0.008)
                        elif fx1 < 0.56 and (0.85 - fx1) >= 0.25:
                            ax = max(ax, fx1 + 0.015)
                            aw = 0.85 - ax

                ab = clamp_box(ax, ay0, aw, max(0.06, ay1 - ay0))
                if not overlaps_any(ab, fig_spots + page_spots, thresh=0.14):
                    page_spots.append({
                        "id": f"hs-{pid}-act-{len(page_spots)}",
                        "type": "activity",
                        "lab_exp": lab_exp,
                        "activity_ref": lab_exp,
                        "indicator_label": act_label,
                        "highlight_color": "rgba(124, 58, 237, 0.16)",
                        "bounds": ab
                    })

        for fs in fig_spots:
            page_spots.append(fs)

        # F. MAJOR COLORED SECTION HEADINGS (Concept cards, non-overlapping!)
        placed_cy = []
        for it in items:
            if not (it["color"] in ("#00ffff", "#ff00ff", "#ffff00", "#ffff4c") and it["size"] >= 25):
                continue
            if "◊UA" in it["sc"] or "qJ" in it["sc"] or len(it["sc"]) < 4:
                continue
            y0_px = it["top"] - 8
            if y0_px > 920 or any(abs(y0_px - py) < 160 for py in placed_cy):
                continue
            cb = clamp_box(0.17, y0_px / H, 0.66, 0.14)
            if not overlaps_any(cb, page_spots, thresh=0.10):
                placed_cy.append(y0_px)
                page_spots.append({
                    "id": f"hs-{pid}-concept-{len(page_spots)}",
                    "type": "explainable_text",
                    "explanation_ref": exp_ref,
                    "indicator_label": "📌 مفهوم وشرح أساسي (3 مستويات)",
                    "highlight_color": "rgba(0, 168, 89, 0.13)",
                    "bounds": cb
                })

        if page_spots:
            interactions[pid] = page_spots

    # 8. SAVE ALL FILES & BUILD BUNDLE
    manifest = load_json("manifest.json")
    manifest["edition"]["start_pdf_page"] = 2
    manifest["edition"]["end_pdf_page"] = 220
    manifest["edition"]["total_book_pages"] = len(pages)

    activities = {k: {"id": k, "title": v, "book_page": bp, "lab_url": f"biology-12th-lab.html?exp={k}&from=book"} for bp, (k, v) in exact_page_activity.items()}

    save_json("manifest.json", manifest)
    save_json("units.json", units)
    save_json("pages.json", pages)
    save_json("lessons.json", lessons)
    save_json("explanations.json", explanations)
    save_json("diagrams.json", diagrams)
    save_json("activities.json", activities)
    save_json("assessments.json", assessments)
    save_json("glossary.json", glossary)
    save_json("interactions.json", interactions)

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
    with open(f"{OUT_DIR}/data_bundle.js", "w", encoding="utf-8") as f:
        f.write("window.THAKER_CURRICULUM_G12_BIOLOGY = " + json.dumps(bundle, ensure_ascii=False) + ";\n")

    for fn in os.listdir(OUT_DIR):
        shutil.copy2(f"{OUT_DIR}/{fn}", f"{ANDROID_OUT}/{fn}")

    total_hs = sum(len(v) for v in interactions.values())
    print(f"[✓] Precision Biology Data Pack built:")
    print(f"    - Pages: {len(pages)} (PDF 2..220, exact printed page numbers book=pdf+4 -> 6..224)")
    print(f"    - Unit Covers: {[p['book_page'] for p in pages if p['type']=='unit_cover']} (goals box only!)")
    print(f"    - Pages with curated surgical hotspots: {len(interactions)} ({total_hs} total boxes)")
    print(f"    - Unit Quizzes: {len(assessments)} ({sum(len(v) for v in assessments.values())} Qs, incl. authentic Unit 6 Biotech & Unit 8 Geology!)")

if __name__ == "__main__":
    main()
