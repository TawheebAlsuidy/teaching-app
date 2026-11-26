#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator for the Grade 12 Arabic literature interactive curriculum pack."""
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "curriculum", "grade12", "arabic_lit")
ANDROID_DATA_DIR = os.path.join(BASE_DIR, "thaker-android-src", "assets", "data", "curriculum", "grade12", "arabic_lit")
BUNDLE_VAR = "window.THAKER_CURRICULUM_G12_ARABIC_LIT"

MANIFEST = {
    "schema_version": "2.0.0",
    "pack_id": "arabic-lit-g12-interactive-2026",
    "subject": "arabic_lit",
    "grade": 12,
    "edition": {
        "title": "الأدب والنصوص والنقد - الصف الثالث الثانوي",
        "ministry": "الجمهورية اليمنية - وزارة التربية والتعليم - قطاع المناهج",
        "curriculum_version": "1447هـ - 2026م",
        "official_pdf": "الأدب-والنصوص-والنقد-للصف-الثالث-الثانوي.pdf",
        "total_pdf_pages": 218,
        "start_pdf_page": 7,
        "end_pdf_page": 218,
        "total_book_pages": 212,
        "page_offset": "book_page = pdf_page - 1",
        "toc_pdf_pages": [7, 8],
        "toc_book_pages": [6, 7]
    },
    "features": {
        "original_page_rendering": True,
        "interactive_overlays": True,
        "smart_text_bottom_sheet": True,
        "literary_analysis_panels": True,
        "author_and_text_cards": True,
        "rhetorical_focus_prompts": True,
        "offline_audio_synthesis": True,
        "yemeni_companion_prompts": True,
        "multi_student_profiles": True
    },
    "data_files": [
        "manifest.json",
        "sections.json",
        "pages.json",
        "topics.json",
        "lessons.json",
        "interactions.json",
        "explanations.json",
        "literary_analyses.json",
        "author_cards.json",
        "assessments.json",
        "glossary.json",
        "data_bundle.js"
    ]
}

SECTIONS = [
    {
        "id": "s1",
        "order": 1,
        "title": "أولاً: الأدب والنصوص",
        "short_desc": "نماذج من الأدب العربي في العصرين المملوكي والعثماني والعصر الحديث، مع قراءات في الشعر والنثر والمدارس الأدبية.",
        "page_start": 9,
        "page_end": 171,
        "pdf_start": 10,
        "pdf_end": 172
    },
    {
        "id": "s2",
        "order": 2,
        "title": "ثانياً: النقد الأدبي",
        "short_desc": "مفاهيم النقد الأدبي والأسلوب والشكل والمضمون والتجربة الشعرية والقصة والنص المسرحي والمقالة.",
        "page_start": 173,
        "page_end": 217,
        "pdf_start": 174,
        "pdf_end": 218
    }
]

TOPIC_ROWS = [
    ("s1", 1, "t01", "الأدب في العصرين المملوكي والعثماني", "", "أدب", 9),
    ("s1", 2, "t02", "في رثاء بغداد", "شمس الدين الكوفي", "شعر", 14),
    ("s1", 3, "t03", "وصف السفينة", "ابن حبيب الحلبي", "نثر", 17),
    ("s1", 4, "t04", "النهضة الأدبية في العصر الحديث", "", "أدب", 23),
    ("s1", 5, "t05", "الشعر العربي في العصر الحديث", "", "أدب", 29),
    ("s1", 6, "t06", "النثر العربي", "", "أدب", 34),
    ("s1", 7, "t07", "فراق وشوق", "محمود سامي البارودي", "شعر", 41),
    ("s1", 8, "t08", "ثمن الحرية", "أحمد شوقي", "شعر", 46),
    ("s1", 9, "t09", "صرخة على الظلم", "محمد محمود الزبيري", "شعر", 50),
    ("s1", 10, "t10", "حضارة ومجد", "محمود غنيم", "شعر", 55),
    ("s1", 11, "t11", "أمتي", "عمر أبو ريشة", "شعر", 61),
    ("s1", 12, "t12", "الإسراء والمعراج", "مصطفى صادق الرافعي", "نثر", 68),
    ("s1", 13, "t13", "الرجولة", "أحمد أمين", "نثر", 77),
    ("s1", 14, "t14", "المدرسة الرومنسية", "", "أدب", 82),
    ("s1", 15, "t15", "المساء", "خليل مطران", "شعر", 87),
    ("s1", 16, "t16", "مشاعر حزينة", "أبو القاسم الشابي", "شعر", 93),
    ("s1", 17, "t17", "كن بلسماً", "إيليا أبو ماضي", "شعر", 99),
    ("s1", 18, "t18", "الدجى المشبوه", "عبد الله البردوني", "شعر", 104),
    ("s1", 19, "t19", "لو أحسن الناس", "المنفلوطي", "نثر", 111),
    ("s1", 20, "t20", "بذار السنين", "ميخائيل نعيمة", "نثر", 113),
    ("s1", 21, "t21", "المدرسة الواقعية", "", "أدب", 121),
    ("s1", 22, "t22", "اليوم الموعود", "لطفي أمان", "شعر", 125),
    ("s1", 23, "t23", "غربة الروح", "بدر شاكر السياب", "شعر", 129),
    ("s1", 24, "t24", "نداء الإخاء", "نازك الملائكة", "شعر", 133),
    ("s1", 25, "t25", "إصرار وتحد", "عبد العزيز المقالح", "شعر", 137),
    ("s1", 26, "t26", "قضية وجود", "محمود درويش", "شعر", 143),
    ("s1", 27, "t27", "لن أبكي", "فدوى طوقان", "شعر", 150),
    ("s1", 28, "t28", "من إشعاعات الأزهر", "نجيب الكيلاني", "نثر", 156),
    ("s1", 29, "t29", "مسمار جحا", "علي أحمد باكثير", "نثر", 164),
    ("s2", 30, "t30", "النقد الأدبي", "", "نقد", 173),
    ("s2", 31, "t31", "الأسلوب", "", "نقد", 180),
    ("s2", 32, "t32", "الشكل والمضمون", "", "نقد", 184),
    ("s2", 33, "t33", "التجربة الشعرية", "", "نقد", 189),
    ("s2", 34, "t34", "القصة", "", "نقد", 198),
    ("s2", 35, "t35", "النص المسرحي", "", "نقد", 200),
    ("s2", 36, "t36", "المقالة", "", "نقد", 202)
]

GLOSSARY_ROWS = [
    ("الأدب", "تعبير جمالي عن الحياة والفكر بصيغة لغوية مؤثرة."),
    ("الشعر", "كلام موزون مقفى يحمل تجربة شاعرية وصوراً فنية."),
    ("النثر", "كتابة غير موزونة تهدف إلى الإفهام أو الإقناع أو الإمتاع."),
    ("الرثاء", "شعر أو نثر يعبّر عن الحزن على فقدان شخص أو مكان أو رمز."),
    ("الوصف", "تصوير المكان أو الشيء أو الحالة بلغة حسية واضحة."),
    ("النهضة الأدبية", "حركة تجديد في الموضوعات والأساليب الأدبية في العصر الحديث."),
    ("الرومنسية", "اتجاه أدبي يميل إلى العاطفة والخيال والتجربة الذاتية."),
    ("الواقعية", "اتجاه أدبي يميل إلى تصوير الحياة الاجتماعية بصدق وتفصيل."),
    ("النقد الأدبي", "قراءة تحليلية للنص لبيان قيمته الفنية ومحاسنه ومآخذه."),
    ("الأسلوب", "الطريقة الخاصة التي يستخدمها الكاتب في اختيار الألفاظ والتراكيب والصور."),
    ("الشكل والمضمون", "العلاقة بين البناء الفني للنص والأفكار والمعاني التي يحملها."),
    ("التجربة الشعرية", "ما يعيشه الشاعر ويصوغه شعراً من إحساس وفكر وصورة."),
    ("القصة", "سرد أدبي يعتمد على الحدث والشخصية والحبكة والزمان والمكان."),
    ("النص المسرحي", "نص مكتوب ليُؤدّى على خشبة المسرح عبر الحوار والحدث والمشهد."),
    ("المقالة", "نثر قصير يعرض فكرة أو رأياً أو تأملاً بأسلوب منظم.")
]


def short_desc(row):
    section, order, topic_id, title, author, genre, start = row
    if section == "s2":
        return f"مفهوم نقدي من مفاهيم {title}، عرضه المنهج في ص {start}."
    if genre == "شعر":
        return f"نص شعري بعنوان {title}" + (f" للشاعر {author}" if author else "") + f"، يبدأ في ص {start}."
    if genre == "نثر":
        return f"نص نثري بعنوان {title}" + (f" للكاتب {author}" if author else "") + f"، يبدأ في ص {start}."
    return f"موضوع أدبي بعنوان {title}، يبدأ في ص {start}."


def build_topics():
    topics = []
    for row in TOPIC_ROWS:
        section, order, topic_id, title, author, genre, start = row
        next_start = TOPIC_ROWS[order][6] if order < len(TOPIC_ROWS) else 218
        end = next_start - 1
        if topic_id == "t29":
            end = 171
        topics.append({
            "id": topic_id,
            "order": order,
            "sectionId": section,
            "title": title,
            "author": author,
            "genre": genre,
            "page_start": start,
            "page_end": end,
            "pdf_start": start + 1,
            "pdf_end": end + 1,
            "short_desc": short_desc(row),
            "source": "official_table_of_contents"
        })
    return topics


TOPICS = build_topics()


def topic_for_page(book_page):
    for topic in TOPICS:
        if topic["page_start"] <= book_page <= topic["page_end"]:
            return topic
    return None


def section_for_page(book_page):
    return "s1" if book_page <= 171 else "s2"


def build_pages():
    pages = []
    for book_page in range(6, 218):
        pdf_page = book_page + 1
        topic = topic_for_page(book_page)
        pages.append({
            "page_id": f"lit12-p{book_page:03d}",
            "book_page": book_page,
            "pdf_page": pdf_page,
            "type": "toc" if book_page <= 7 else "lesson",
            "title": topic["title"] if topic else "فهرس الأدب والنصوص والنقد",
            "section_id": section_for_page(book_page),
            "topic_id": topic["id"] if topic else "",
            "image": f"assets/curriculum/grade12/arabic_lit/pages/page_{pdf_page:03d}_opt.jpg",
            "image_full": f"assets/curriculum/grade12/arabic_lit/pages/page_{pdf_page:03d}.jpg",
            "aspect_ratio": 0.7078
        })
    return pages


def build_lessons():
    return [{
        "id": topic["id"],
        "unitId": topic["sectionId"],
        "order": topic["order"],
        "title": topic["title"],
        "pages": [topic["page_start"], topic["page_end"]],
        "pdf_pages": [topic["pdf_start"], topic["pdf_end"]]
    } for topic in TOPICS]


def build_explanations():
    result = {}
    for topic in TOPICS:
        result[f"exp-lit-{topic['id']}"] = {
            "id": f"exp-lit-{topic['id']}",
            "title": f"قراءة ميسّرة: {topic['title']}",
            "original_text": f"العنوان وصفحة البداية منقولان من فهرس الكتاب الرسمي: {topic['title']}، ص {topic['page_start']}.",
            "levels": {
                "basic": f"📖 {topic['short_desc']}",
                "intermediate": "اقرأ الصفحة الأصلية، ثم حدّد موضوع النص وغرضه، واربط بين العنوان وما ورد في المطلع والخاتمة.",
                "advanced": "قارن بين ما ذكره المنهج في عرض الموضوع وبين ما تقرؤه في الصفحة الأصلية، وسجّل الفرق بين عرض المعلومة وتحليلها."
            },
            "chemical_equations": [],
            "math_equations": [],
            "tts_text": f"{topic['title']}. {topic['short_desc']}",
            "source_note": "المحاور مضافة تعليمية لتسهيل القراءة، والعنوان والصفحة من الفهرس الرسمي."
        }
    return result


def build_literary_analyses():
    result = {}
    for topic in TOPICS:
        author_line = f" للكاتب {topic['author']}" if topic["author"] else ""
        result[f"ana-lit-{topic['id']}"] = {
            "id": f"ana-lit-{topic['id']}",
            "title": f"تحليل جمالي: {topic['title']}",
            "topicId": topic["id"],
            "page": topic["page_start"],
            "genre": topic["genre"],
            "author": topic["author"],
            "original_text": f"{topic['title']}{author_line} — {topic['genre']} — ص {topic['page_start']} إلى {topic['page_end']}.",
            "educational_note": "المحاور التالية إضافة تعليمية للقراءة والتحليل؛ النص الأصلي هو المرجع المعتمد.",
            "axes": [
                {"label": "المعنى الإجمالي", "prompt": "ما الفكرة التي يريد النص إيصالها؟ استشهد بعبارة من الصفحة الأصلية."},
                {"label": "الصورة والخيال", "prompt": "اختر صورة أو تشبيهاً أو استعارة من النص، وبيّن ما تضيفه إلى المعنى."},
                {"label": "الأسلوب والتركيب", "prompt": "لاحظ اختيار الألفاظ وطول الجمل وترتيب الأفكار، ثم اربط ذلك بالغرض من النص."},
                {"label": "القيمة الجمالية", "prompt": "ما الذي يجعل العبارة مؤثرة أو جميلة؟ اربط إجابتك بالموسيقى الداخلية أو بالإيقاع أو بالصورة."}
            ],
            "tts_text": f"تحليل {topic['title']}. اقرأ النص الأصلي، ثم أجب عن محاور المعنى والصورة والأسلوب والقيمة الجمالية."
        }
    return result


def build_author_cards():
    result = {}
    for topic in TOPICS:
        if not topic["author"]:
            continue
        result[f"card-lit-{topic['id']}"] = {
            "id": f"card-lit-{topic['id']}",
            "title": f"بطاقة النص: {topic['title']}",
            "topicId": topic["id"],
            "author": topic["author"],
            "work": topic["title"],
            "genre": topic["genre"],
            "page": topic["page_start"],
            "source_line": f"من فهرس الكتاب: {topic['title']} / {topic['author']} — {topic['genre']} — ص {topic['page_start']}.",
            "note": "الاسم والعنوان والنوع وصفحة البداية منقولة من الفهرس؛ أي ترجمة إضافية تُضاف بعد التحقق من الصفحة الأصلية."
        }
    return result


def build_interactions():
    ys = [0.06, 0.24, 0.42, 0.60]
    result = {}
    for book_page in range(6, 218):
        page_id = f"lit12-p{book_page:03d}"
        topic = topic_for_page(book_page)
        if topic:
            exp_ref = f"exp-lit-{topic['id']}"
            analysis_ref = f"ana-lit-{topic['id']}"
            card_ref = f"card-lit-{topic['id']}" if topic["author"] else ""
            quiz_ref = f"quiz-lit-{topic['sectionId']}"
        else:
            exp_ref = "exp-lit-t01"
            analysis_ref = "ana-lit-t01"
            card_ref = ""
            quiz_ref = "quiz-lit-s1"
        spots = [{
            "id": f"hs-{page_id}-reading",
            "type": "explainable_text",
            "explanation_ref": exp_ref,
            "indicator_label": "قراءة ميسّرة للصفحة",
            "highlight_color": "rgba(180, 83, 9, 0.13)",
            "bounds": {"x": 0.70, "y": ys[0], "w": 0.24, "h": 0.14}
        }, {
            "id": f"hs-{page_id}-analysis",
            "type": "literary_analysis",
            "analysis_ref": analysis_ref,
            "indicator_label": "تحليل جمالي تفاعلي",
            "highlight_color": "rgba(217, 119, 6, 0.16)",
            "bounds": {"x": 0.70, "y": ys[1], "w": 0.24, "h": 0.14}
        }]
        if card_ref:
            spots.append({
                "id": f"hs-{page_id}-card",
                "type": "author_card",
                "card_ref": card_ref,
                "indicator_label": "بطاقة النص والكاتب",
                "highlight_color": "rgba(180, 83, 9, 0.11)",
                "bounds": {"x": 0.70, "y": ys[2], "w": 0.24, "h": 0.14}
            })
        spots.append({
            "id": f"hs-{page_id}-quiz",
            "type": "assessment",
            "assessment_ref": quiz_ref,
            "indicator_label": "اختبر فهمك",
            "highlight_color": "rgba(180, 83, 9, 0.14)",
            "bounds": {"x": 0.70, "y": ys[3], "w": 0.24, "h": 0.14}
        })
        result[page_id] = spots
    return result


def make_question(seq, topic, prompt, correct, distractors, explain):
    entries = [(correct, None)] + list(distractors)
    shift = seq % len(entries)
    entries = entries[shift:] + entries[:shift]
    options = []
    answer = 0
    for idx, (text, why) in enumerate(entries):
        option = {"text": text}
        if why:
            option["why_wrong"] = why
        options.append(option)
        if why is None:
            answer = idx
    return {
        "id": f"ql-lit-{topic['sectionId']}-{seq + 1:02d}",
        "unitId": topic["sectionId"],
        "lessonId": topic["id"],
        "page": topic["page_start"],
        "difficulty": ["easy", "medium", "hard"][seq % 3],
        "skillId": ["recall", "recognition", "analysis", "application"][seq % 4],
        "q": prompt,
        "options": options,
        "answer": answer,
        "explain": explain
    }


def build_assessments():
    result = {}
    for section in SECTIONS:
        section_topics = [topic for topic in TOPICS if topic["sectionId"] == section["id"]]
        questions = []
        for seq, topic in enumerate(section_topics):
            others = [item for item in section_topics if item["id"] != topic["id"]]
            if seq % 3 == 0:
                prompt = f"ما عنوان الموضوع الذي يبدأ في ص {topic['page_start']}؟"
                correct = topic["title"]
                distractors = [(item["title"], "هذا عنوان موضوع آخر في الفهرس، صفحته مختلفة.") for item in others[:3]]
                explain = f"الفهرس يثبت أن {topic['title']} يبدأ في ص {topic['page_start']}."
            elif seq % 3 == 1:
                prompt = f"ما نوع نص «{topic['title']}» كما ورد في الفهرس؟"
                correct = topic["genre"]
                wrong_genres = [genre for genre in ["أدب", "شعر", "نثر", "نقد"] if genre != topic["genre"]]
                distractors = [(genre, "النوع المذكور في الفهرس لهذا الموضوع مختلف.") for genre in wrong_genres[:3]]
                explain = f"الفهرس يصنّف {topic['title']} ضمن {topic['genre']}."
            else:
                author = topic["author"] or "موضوع أدبي عام"
                prompt = f"بمن ترتبط عبارة «{topic['title']}» في الفهرس؟"
                correct = author
                distractors = [(item["author"] or "موضوع أدبي عام", "الاسم المرتبط بهذا العنوان في الفهرس مختلف.") for item in others[:3]]
                explain = f"الفهرس يربط {topic['title']} بـ {author}."
            questions.append(make_question(seq, topic, prompt, correct, distractors, explain))
        result[f"quiz-lit-{section['id']}"] = questions
    return result


def build_glossary():
    return [{
        "id": f"term-lit-{idx + 1:02d}",
        "term": term,
        "definition": definition,
        "source": "educational_addition"
    } for idx, (term, definition) in enumerate(GLOSSARY_ROWS)]


def dump_json(name, data):
    for directory in (DATA_DIR, ANDROID_DATA_DIR):
        os.makedirs(directory, exist_ok=True)
        with open(os.path.join(directory, name), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    payload = {
        "manifest": MANIFEST,
        "sections": SECTIONS,
        "pages": build_pages(),
        "topics": TOPICS,
        "lessons": build_lessons(),
        "interactions": build_interactions(),
        "explanations": build_explanations(),
        "literary_analyses": build_literary_analyses(),
        "author_cards": build_author_cards(),
        "assessments": build_assessments(),
        "glossary": build_glossary()
    }
    for name, data in payload.items():
        dump_json(f"{name}.json", data)
    for directory in (DATA_DIR, ANDROID_DATA_DIR):
        with open(os.path.join(directory, "data_bundle.js"), "w", encoding="utf-8") as f:
            f.write(f"{BUNDLE_VAR} = ")
            json.dump(payload, f, ensure_ascii=False, indent=2)
            f.write(";\n")
    total_questions = sum(len(v) for v in payload["assessments"].values())
    print(f"[✓] Arabic literature pack generated: {len(payload['pages'])} pages, {len(TOPICS)} topics, {total_questions} questions.")


if __name__ == "__main__":
    main()
