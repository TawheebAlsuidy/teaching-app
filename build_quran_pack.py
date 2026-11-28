#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds the Grade 12 Quran & Its Sciences curriculum pack (Schema v2.0 + Tanzil & Husary verified)."""
import json
import os
import re
import html as py_html

from scripts.quran_text_engine import (
    BASMALA_UTHMANI,
    SURAH_NAMES,
    WAQF_MARKS,
    get_ayah,
    get_range,
    render_ayah_tajweed_html,
    UTHMANI_MAP,
)
from quran_lessons_p1 import SECTION1_LESSONS
from quran_lessons_p2_p3 import SECTION2_LESSONS, SECTION3_LESSONS
from quran_assessments import S1_QUIZ, S2_QUIZ, S3_QUIZ, build_taqwim_drills, build_hifz_drills

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "curriculum", "grade12", "quran")
ANDROID_DATA_DIR = os.path.join(BASE_DIR, "thaker-android-src", "assets", "data", "curriculum", "grade12", "quran")
AUDIO_DIR = os.path.join(BASE_DIR, "assets", "curriculum", "grade12", "quran", "audio")
PAGES_DIR = os.path.join(BASE_DIR, "assets", "curriculum", "grade12", "quran", "pages")
BUNDLE_VAR = "window.THAKER_CURRICULUM_G12_QURAN"

MANIFEST = {
    "schema_version": "2.0.0",
    "pack_id": "quran-g12-interactive-2026",
    "subject": "quran",
    "grade": 12,
    "edition": {
        "title": "القرآن الكريم وعلومه (الحفظ والتفسير - علوم القرآن - التلاوة)",
        "ministry": "الجمهورية اليمنية - وزارة التربية والتعليم - قطاع المناهج",
        "curriculum_version": "1435هـ / 2014م — طبعة التحقق 2026م",
        "official_pdf": "القرآن-ثالث ثانوي- (1).pdf",
        "total_pdf_pages": 190,
        "start_pdf_page": 2,
        "end_pdf_page": 189,
        "total_book_pages": 188,
        "page_offset": "book_page = pdf_page + 3",
        "text_source": "Tanzil Project (Quran Text, Uthmani & Simple, Hafs 'an Asim)",
        "reciter_source": "الشيخ محمود خليل الحصري — المصحف المعلم (قارئ بشري حقيقي مسجل أوفلاين)"
    },
    "features": {
        "original_page_rendering": True,
        "uthmani_mushaf_mode": True,
        "tajweed_color_layer": True,
        "real_reciter_offline_audio": True,
        "ai_assisted_scenes_respectful": True,
        "tts_lesson_narration": True,
        "interactive_taqwim_drills": True,
        "hifz_verse_tester": True
    },
    "data_files": [
        "manifest.json", "units.json", "pages.json", "lessons.json",
        "interactions.json", "explanations.json", "glossary.json",
        "assessments.json", "taqwim_drills.json", "hifz_drills.json",
        "scenes.json", "verses.json", "data_bundle.js"
    ]
}

SECTIONS_AS_UNITS = [
    {
        "id": "s1",
        "order": 1,
        "title": "أولاً: الحفظ والتفسير (سورة النور ١–٦٤)",
        "short_desc": "١٣ درساً في سورة النور: الزنى، القذف، حادثة الإفك ودروسها، آداب الاستئذان، غض البصر، تيسير الزواج، نور الإيمان، دلائل القدرة، النفاق، الاستخلاف، وعلاقة الأمة بقيادتها.",
        "page_start": 7,
        "page_end": 86,
        "concepts": ["الطهارة الاجتماعية", "منهج مواجهة الإشاعات", "آداب الاستئذان", "مشكاة نور الإيمان", "الاستخلاف والتمكين"],
        "real_world": "بناء الأسرة والمجتمع العفيف المتماسك وحماية الأعراض وطاعة القيادة."
    },
    {
        "id": "s2",
        "order": 2,
        "title": "ثانياً: علوم القرآن",
        "short_desc": "الإعجاز القرآني (البياني والغيبي والتشريعي والعلمي)، علم التفسير ومناهجه وشروط المفسر، وضوابط ترجمة معاني القرآن.",
        "page_start": 87,
        "page_end": 103,
        "concepts": ["الإعجاز البياني والتشريعي والعلمي", "التفسير التجزيئي والموضوعي", "الترجمة الحرفية وترجمة المعنى"],
        "real_world": "فهم وجوه الإعجاز المتجددة والتمييز بين التفسير المنضبط والترجمة المعتمدة."
    },
    {
        "id": "s3",
        "order": 3,
        "title": "ثالثاً: التلاوة (الأعراف · الأنفال · التوبة · يونس · هود)",
        "short_desc": "١٨ درس تلاوة تغطي ٦٤٢ آية مع التطبيق التفاعلي الملون لأحكام الراء والنون الساكنة والميم الساكنة والقلقلة والمدود والوقف والمخارج واللام.",
        "page_start": 104,
        "page_end": 192,
        "concepts": ["النون والميم الساكنتان", "أحكام المدود الستة", "مخارج الحروف السبعة عشر", "الوقف وأحكام الراء واللام"],
        "real_world": "تجويد التلاوة وضبط المخارج ومراتب المد وعلامات الوقف في المصحف الشريف."
    }
]


def _audio_filename_if_exists(surah: int, ayah: int) -> str:
    fn = f"{surah:03d}{ayah:03d}.mp3"
    if os.path.exists(os.path.join(AUDIO_DIR, fn)):
        return f"assets/curriculum/grade12/quran/audio/{fn}"
    return ""


def _enrich_verse_entry(surah: int, ayah: int) -> dict:
    v = get_ayah(surah, ayah)
    tj = render_ayah_tajweed_html(v["uthmani"])
    stripped = py_html.unescape(re.sub(r"<[^>]+>", "", tj))
    assert stripped == v["uthmani"], f"Verification assertion failed on {surah}:{ayah}"
    return {
        "key": v["key"],
        "surah": surah,
        "surah_name": v["surah_name"],
        "ayah": ayah,
        "uthmani": v["uthmani"],
        "tajweed_html": tj,
        "simple": v["simple"],
        "plain": v["plain"],
        "audio_src": _audio_filename_if_exists(surah, ayah),
    }


def build_verses_catalog():
    """Verify & bundle every Quranic verse referenced or recited in the curriculum (100% Tanzil)."""
    needed = set()
    for l in SECTION1_LESSONS:
        for a in range(l["ayah_start"], l["ayah_end"] + 1):
            needed.add((l["surah"], a))
        if l.get("intro"):
            for c in l["intro"].get("citations", []):
                needed.add((c["surah"], c["ayah"]))
        for ax in l["axes"]:
            for c in ax.get("citations", []):
                for a in range(c["start"], c["end"] + 1):
                    needed.add((c["surah"], a))
    for l in SECTION2_LESSONS:
        for ax in l["axes"]:
            for c in ax.get("citations", []):
                for a in range(c["start"], c["end"] + 1):
                    needed.add((c["surah"], a))
    for l in SECTION3_LESSONS:
        for a in range(l["ayah_start"], l["ayah_end"] + 1):
            needed.add((l["surah"], a))

    catalog = {}
    for surah, ayah in sorted(needed):
        catalog[f"{surah}:{ayah}"] = _enrich_verse_entry(surah, ayah)

    # Assert audio offline existence for ALL Section 1 verses + ALL Section 1 & 2 citations!
    missing_audio = []
    for l in SECTION1_LESSONS:
        for a in range(l["ayah_start"], l["ayah_end"] + 1):
            if not catalog[f"{l['surah']}:{a}"]["audio_src"]:
                missing_audio.append(f"{l['surah']}:{a}")
        for ax in l["axes"]:
            for c in ax.get("citations", []):
                for a in range(c["start"], c["end"] + 1):
                    if not catalog[f"{c['surah']}:{a}"]["audio_src"]:
                        missing_audio.append(f"{c['surah']}:{a}")
    for l in SECTION2_LESSONS:
        for ax in l["axes"]:
            for c in ax.get("citations", []):
                for a in range(c["start"], c["end"] + 1):
                    if not catalog[f"{c['surah']}:{a}"]["audio_src"]:
                        missing_audio.append(f"{c['surah']}:{a}")

    assert not missing_audio, f"Missing offline Husary MP3s for verses: {missing_audio}"
    return catalog


def build_scenes():
    """Visual scenes (AI generated where available + rich animated Islamic SVG diagrams) with TTS narration scripts."""
    return {
        "scene-ifk-map": {
            "id": "scene-ifk-map",
            "lessonId": "q-s1-03",
            "title": "قصة حادثة الإفك ومسار العودة إلى المدينة المنورة",
            "subtitle": "من المريسيع (غزوة بني المصطلق) إلى مشارف المدينة — سورة النور (١١–٢٠)",
            "kind": "svg_ifk_caravan",
            "page": 24,
            "narration": "خلال العودة من غزوة بني المصطلق، عسكر جيش المسلمين ليلاً. وفي الفجر تأخرت أم المؤمنين عائشة رضي الله عنها بحثاً عن عقدها الساقط، فحمل الرجال هودجها ظناً أنها فيه. ثم مر صفوان بن المعطل السلمي فأناخ راحلته وحملها دون أن ينظر إليها وقاد الجمل حتى لحق بالجيش على مشارف المدينة. فاستغل المنافقون وعلى رأسهم عبد الله بن أبي بن سلول الواقعة، حتى نزل الوحي في سورة النور بتبرئتها وإرساء قواعد حسن الظن والتثبت ورد الإشاعات.",
            "badge": "إضافة تعليمية · شرح مصور وبصوت أوفلاين (بلا تجسيد لأي صحابي)"
        },
        "scene-nur-mishkah": {
            "id": "scene-nur-mishkah",
            "lessonId": "q-s1-08",
            "title": "مشكاة نور الإيمان وظلمات البحر اللجي",
            "subtitle": "المثال القرآني المعجز لنور الهداية في سورة النور (٣٥–٤٠)",
            "kind": "ai_image",
            "image_src": "assets/curriculum/grade12/quran/scenes/ayah_nur_mishkah.jpg",
            "page": 53,
            "narration": "ضرب الله لنوره مثل مشكاة أي كوّة في الحائط تحصر النور، فيها مصباح داخل زجاجة متلألئة كالكوكب الدري، يوقد من زيت شجرة زيتون مباركة لا يحجبها جبل شرقاً ولا غرباً، يكاد زيتها يضيء لصفائه؛ وذلك مثل قلب المؤمن المهتدي بالوحي، مقابل الكافر في ظلمات البحر اللجي تتراكم فوقه الأمواج والسحب لا يكاد يرى يده.",
            "badge": "لوحة توضيحية مولّدة بالذكاء الاصطناعي (خالية من الأشخاص)"
        },
        "scene-istiizan-house": {
            "id": "scene-istiizan-house",
            "lessonId": "q-s1-05",
            "title": "مخطط آداب الاستئذان في البيت المسلم",
            "subtitle": "استئذان الغرباء من الخارج (٣٥–٣٨) واستئذان أهل البيت في العورات الثلاث (٧٦–٨٠)",
            "kind": "svg_istiizan",
            "page": 35,
            "narration": "صان الإسلام حرمة البيت وجعل الاستئذان استئناساً لطيفاً: السلام والتعريف بالاسم، الوقوف على جانب الباب لا أمام الفتحة، الرفق بالطرق حتى ثلاث مرات، والانصراف عند الرفض أو خلو البيت. وفي داخل البيت يستأذن الأطفال والمماليك في الأوقات الثلاثة: قبل الفجر، وفي القيلولة بالظهيرة، وبعد العشاء.",
            "badge": "إضافة تعليمية · محاكي ومخطط تفاعلي"
        },
        "scene-cosmic-rain": {
            "id": "scene-cosmic-rain",
            "lessonId": "q-s1-09",
            "title": "دلائل قدرة الله: دورة السحب الركامية والبرد والبرق",
            "subtitle": "سورة النور (آية ٤٣) — يُزجي، يؤلف، ركاماً، الودق، سنا برقه",
            "kind": "svg_cosmic_rain",
            "page": 61,
            "narration": "تصف آية النور بدقة بالغة مراحل تكون المطر: تبخر المياه بحرارة الشمس، ثم تسوق الرياح الأبخرة بلطف (يزجي)، وتؤلف بين قطع السحاب، وترفعها طبقات متراكمة كالجبال (ركاماً)، ثم يخرج الودق قطرات ماء والبرد المتجمد، ويلمع البرق الذي يكاد سطوعه يخطف الأبصار، وكل شيء في السماوات والأرض يسبح بحمد الله.",
            "badge": "إضافة تعليمية · مخطط كوني متحرك"
        },
        "scene-ijaz-science": {
            "id": "scene-ijaz-science",
            "lessonId": "q-s2-01",
            "title": "محاور الإعجاز القرآني والسبق العلمي",
            "subtitle": "التحدي البلاغي، التوازن، الغيب، فتق الكون (الأنبياء ٣٠) وأطوار الجنين (المؤمنون ١٢–١٤)",
            "kind": "svg_ijaz",
            "page": 89,
            "narration": "تحدّى القرآن أفصح العرب بثلاث مراحل متدرجة فعجزوا. ومن أوجه إعجازه الإخبار بالغيب في الماضي والحاضر والمستقبل كغلبة الروم، والإعجاز التشريعي المحكم، والسبق العلمي في فتق الكون وجعل الماء أصل الأحياء، وتصوير أطوار خلق الإنسان بدقة في قرار مكين.",
            "badge": "إضافة تعليمية · خريطة الإعجاز العلمي والبياني"
        },
        "scene-makharij-tajweed": {
            "id": "scene-makharij-tajweed",
            "lessonId": "q-s3-12",
            "title": "خريطة مخارج الحروف وأحكام التجويد التفاعلية",
            "subtitle": "الجوف، الحلق، اللسان (١٠ مخارج)، الشفتان، والخيشوم — دروس التلاوة (١–١٨)",
            "kind": "svg_makharij",
            "page": 163,
            "narration": "تتوزع مخارج الحروف العربية الرئيسية على خمسة مواضع: الجوف لحروف المد الثلاثة، الحلق لستة حروف الإظهار، اللسان بعشرة مخارج لثمانية عشر حرفاً، الشفتان للباء والميم والواو والفاء، والخيشوم للغنة في النون والميم المشددتين والإدغام والإخفاء.",
            "badge": "إضافة تعليمية · خريطة مخارج الحروف"
        }
    }


def build_glossary():
    """Official curriculum vocabulary keyed as a dict compatible with template GLOSSARY[vid]."""
    terms = {}
    idx = 0
    for l in SECTION1_LESSONS:
        for v in l["vocab"]:
            idx += 1
            gid = f"qg-{l['id']}-{idx:03d}"
            terms[gid] = {
                "id": gid,
                "term": v["phrase"],
                "definition": v["meaning"],
                "lessonId": l["id"],
                "ref": v["ref"],
                "page": l["p_start"],
                "source": "from_book"
            }
    extra_terms = [
        ("المعجزة", "أمر خارق للعادة مقرون بالتحدي سالم من المعارضة يظهره الله على يد نبي لتصديقه (ص ٨٨).", "q-s2-01", 88),
        ("التفسير التجزيئي", "منهج يتناول فيه المفسر بيان الآيات آية فآية حسب ترتيب المصحف الشريف (ص ٩٧).", "q-s2-02", 97),
        ("التفسير الموضوعي", "منهج يجمع الآيات الواردة في موضوع واحد ويدرسها مجتمعة (ص ٩٧).", "q-s2-02", 97),
        ("الترجمة الحرفية", "محاكاة نظم الأصل وترتيبه كلمة بكلمة، ولا تجوز للقرآن الكريم لأنها تفسد المعنى (ص ١٠١).", "q-s2-03", 101),
        ("الترجمة للمعنى", "نقل المضمون الإجمالي للآية بشروط منضبطة، وهي المقبولة ولا تقوم مقام القرآن في التعبد (ص ١٠١).", "q-s2-03", 101),
        ("القلقلة", "اضطراب المخرج عند النطق بأحرف «قطب جد» ساكنة (ص ١٢٨).", "q-s3-04", 128),
    ]
    for term, defn, lid, pg in extra_terms:
        idx += 1
        gid = f"qg-extra-{idx:03d}"
        terms[gid] = {
            "id": gid,
            "term": term,
            "definition": defn,
            "lessonId": lid,
            "page": pg,
            "source": "from_book"
        }
    return terms


def _lesson_for_page(book_page: int, all_lessons: list):
    for l in all_lessons:
        if l["p_start"] <= book_page <= l["p_end"]:
            return l
    if book_page < 8:
        return all_lessons[0]
    if book_page == 87:
        return SECTION2_LESSONS[0]
    if book_page == 104:
        return SECTION3_LESSONS[0]
    return all_lessons[-1]


def build_pages_and_interactions(all_lessons: list, scenes: dict, glossary: dict):
    pages = []
    interactions = {}
    explanations = {}

    vocab_ids_by_lesson = {}
    for gid, gobj in glossary.items():
        vocab_ids_by_lesson.setdefault(gobj["lessonId"], []).append(gid)

    # Index scene by lessonId
    scene_by_lesson = {sc["lessonId"]: sc for sc in scenes.values()}
    scene_by_lesson["q-s1-04"] = scenes["scene-ifk-map"]
    scene_by_lesson["q-s1-12"] = scenes["scene-istiizan-house"]
    for sl in SECTION3_LESSONS:
        scene_by_lesson.setdefault(sl["id"], scenes["scene-makharij-tajweed"])

    for l in SECTION1_LESSONS:
        tts_lines = [f"{l['title']}."]
        if l.get("intro"):
            tts_lines.extend(l["intro"]["paragraphs"])
        for ax in l["axes"]:
            tts_lines.append(ax["heading"] + ":")
            tts_lines.extend(ax["paragraphs"])
        basic_txt = " ".join(tts_lines[:4])
        inter_txt = " ".join(tts_lines[:8])
        deep_txt = " ".join(tts_lines)
        explanations[f"exp-{l['id']}"] = {
            "id": f"exp-{l['id']}",
            "title": l["title"],
            "original_text": f"سورة النور — الآيات ({l['ayah_start']}–{l['ayah_end']}) · ص {l['p_start']}–{l['p_end']}",
            "page": l["p_start"],
            "sectionId": l["sectionId"],
            "objectives": l["objectives"],
            "axes": l["axes"],
            "vocab": l["vocab"],
            "vocabulary_ids": vocab_ids_by_lesson.get(l["id"], []),
            "editorial_notes": l.get("editorial_notes", []),
            "simple_explanation": basic_txt,
            "deep_explanation": deep_txt,
            "levels": {"basic": basic_txt, "intermediate": inter_txt, "advanced": deep_txt},
        }

    for l in SECTION2_LESSONS:
        tts_lines = [f"{l['title']}."]
        for ax in l["axes"]:
            tts_lines.append(ax["heading"] + ":")
            tts_lines.extend(ax["paragraphs"])
        basic_txt = " ".join(tts_lines[:4])
        inter_txt = " ".join(tts_lines[:8])
        deep_txt = " ".join(tts_lines)
        explanations[f"exp-{l['id']}"] = {
            "id": f"exp-{l['id']}",
            "title": l["title"],
            "original_text": f"ثانياً: علوم القرآن — {l['title']} · ص {l['p_start']}–{l['p_end']}",
            "page": l["p_start"],
            "sectionId": l["sectionId"],
            "objectives": l["objectives"],
            "axes": l["axes"],
            "vocabulary_ids": vocab_ids_by_lesson.get(l["id"], []),
            "editorial_notes": l.get("editorial_notes", []),
            "simple_explanation": basic_txt,
            "deep_explanation": deep_txt,
            "levels": {"basic": basic_txt, "intermediate": inter_txt, "advanced": deep_txt},
        }

    for l in SECTION3_LESSONS:
        simple_txt = f"{l['title']}. التركيز التجويدي: {l['tajweed_rule']}. {l['tajweed_desc']}"
        deep_txt = f"{l['official_note']} القاعدة التفصيلية: {l['tajweed_desc']}"
        explanations[f"exp-{l['id']}"] = {
            "id": f"exp-{l['id']}",
            "title": l["title"],
            "original_text": f"تلاوة الآيات ({l['ayah_start']}–{l['ayah_end']}) سورة {l['surah_name']} · ص {l['p_start']}–{l['p_end']}",
            "page": l["p_start"],
            "sectionId": l["sectionId"],
            "tajweed_rule": l["tajweed_rule"],
            "tajweed_desc": l["tajweed_desc"],
            "official_note": l["official_note"],
            "vocabulary_ids": vocab_ids_by_lesson.get(l["id"], []),
            "simple_explanation": simple_txt,
            "deep_explanation": deep_txt,
            "levels": {"basic": simple_txt, "intermediate": deep_txt, "advanced": deep_txt},
        }

    # Pages PDF 2..189 -> Book 5..192
    for pdf_page in range(2, 190):
        book_page = pdf_page + 3
        opt_fn = f"page_{pdf_page:03d}_opt.jpg"
        full_fn = f"page_{pdf_page:03d}.jpg"
        assert os.path.exists(os.path.join(PAGES_DIR, opt_fn)), f"Missing {opt_fn}"
        assert os.path.exists(os.path.join(PAGES_DIR, full_fn)), f"Missing {full_fn}"

        lesson = _lesson_for_page(book_page, all_lessons)
        sec_id = lesson["sectionId"]
        page_id = f"qur12-p{book_page:03d}"

        if book_page in (5, 6):
            p_title = "فهرس محتويات كتاب القرآن الكريم وعلومه"
        elif book_page == 7:
            p_title = "أولاً: الحفظ والتفسير"
        elif book_page == 87:
            p_title = "ثانياً: علوم القرآن"
        elif book_page == 104:
            p_title = "ثالثاً: التلاوة"
        else:
            p_title = f"{lesson['title']} (ص {book_page})"

        pages.append({
            "page_id": page_id,
            "pdf_page": pdf_page,
            "book_page": book_page,
            "unit_id": sec_id,
            "lesson_id": lesson["id"],
            "title": p_title,
            "image": f"assets/curriculum/grade12/quran/pages/{opt_fn}",
            "image_full": f"assets/curriculum/grade12/quran/pages/{full_fn}",
        })

        # Clean margin-placed hotspots leaving central textbook text 100% unobstructed
        spots = []
        quiz_ref = f"quiz-qur-{sec_id}"
        exp_ref = f"exp-{lesson['id']}"
        sc = scene_by_lesson.get(lesson["id"])

        if sec_id == "s1":
            spots.append({
                "id": f"hs-{page_id}-recite",
                "type": "quran_reader",
                "lesson_ref": lesson["id"],
                "indicator_label": "🎧 الحصري والمصحف",
                "highlight_color": "rgba(5, 150, 105, 0.12)",
                "bounds": {"x": 0.67, "y": 0.012, "w": 0.30, "h": 0.055}
            })
            spots.append({
                "id": f"hs-{page_id}-explain",
                "type": "explainable_text",
                "explanation_ref": exp_ref,
                "indicator_label": "📖 الشرح والمعاني",
                "highlight_color": "rgba(180, 83, 9, 0.12)",
                "bounds": {"x": 0.34, "y": 0.012, "w": 0.30, "h": 0.055}
            })
            if sc:
                spots.append({
                    "id": f"hs-{page_id}-scene",
                    "type": "quran_scene",
                    "scene_ref": sc["id"],
                    "indicator_label": "🕌 القصة بالصوت",
                    "highlight_color": "rgba(14, 165, 233, 0.12)",
                    "bounds": {"x": 0.03, "y": 0.012, "w": 0.28, "h": 0.055}
                })
                spots.append({
                    "id": f"hs-{page_id}-taqwim",
                    "type": "quran_taqwim",
                    "lesson_ref": lesson["id"],
                    "indicator_label": "✍️ التقويم والحفظ",
                    "highlight_color": "rgba(16, 185, 129, 0.12)",
                    "bounds": {"x": 0.34, "y": 0.915, "w": 0.32, "h": 0.055}
                })
            else:
                spots.append({
                    "id": f"hs-{page_id}-taqwim",
                    "type": "quran_taqwim",
                    "lesson_ref": lesson["id"],
                    "indicator_label": "✍️ التقويم والحفظ",
                    "highlight_color": "rgba(16, 185, 129, 0.12)",
                    "bounds": {"x": 0.03, "y": 0.012, "w": 0.28, "h": 0.055}
                })
        elif sec_id == "s2":
            spots.append({
                "id": f"hs-{page_id}-explain",
                "type": "explainable_text",
                "explanation_ref": exp_ref,
                "indicator_label": "📖 الشرح والشواهد",
                "highlight_color": "rgba(5, 150, 105, 0.12)",
                "bounds": {"x": 0.67, "y": 0.012, "w": 0.30, "h": 0.055}
            })
            if sc:
                spots.append({
                    "id": f"hs-{page_id}-scene",
                    "type": "quran_scene",
                    "scene_ref": sc["id"],
                    "indicator_label": "✨ لوحة الإعجاز",
                    "highlight_color": "rgba(180, 83, 9, 0.12)",
                    "bounds": {"x": 0.35, "y": 0.012, "w": 0.29, "h": 0.055}
                })
            spots.append({
                "id": f"hs-{page_id}-taqwim",
                "type": "quran_taqwim",
                "lesson_ref": lesson["id"],
                "indicator_label": "✍️ التقويم الرسمي",
                "highlight_color": "rgba(14, 165, 233, 0.12)",
                "bounds": {"x": 0.03, "y": 0.012, "w": 0.29, "h": 0.055}
            })
        else:
            spots.append({
                "id": f"hs-{page_id}-tilawa",
                "type": "quran_reader",
                "lesson_ref": lesson["id"],
                "indicator_label": "📜 التجويد الملوّن",
                "highlight_color": "rgba(5, 150, 105, 0.12)",
                "bounds": {"x": 0.67, "y": 0.012, "w": 0.30, "h": 0.055}
            })
            spots.append({
                "id": f"hs-{page_id}-tajweed",
                "type": "explainable_text",
                "explanation_ref": exp_ref,
                "indicator_label": f"🏷️ {lesson['tajweed_rule']}",
                "highlight_color": "rgba(180, 83, 9, 0.12)",
                "bounds": {"x": 0.34, "y": 0.012, "w": 0.30, "h": 0.055}
            })
            spots.append({
                "id": f"hs-{page_id}-quiz",
                "type": "assessment",
                "assessment_ref": quiz_ref,
                "indicator_label": "📝 اختبار التجويد",
                "highlight_color": "rgba(16, 185, 129, 0.12)",
                "bounds": {"x": 0.03, "y": 0.012, "w": 0.28, "h": 0.055}
            })
        interactions[page_id] = spots

    return pages, interactions, explanations


def main():
    all_lessons = []
    for l in SECTION1_LESSONS:
        all_lessons.append(dict(l, pages=list(range(l["p_start"], l["p_end"] + 1))))
    for l in SECTION2_LESSONS:
        all_lessons.append(dict(l, pages=list(range(l["p_start"], l["p_end"] + 1))))
    for l in SECTION3_LESSONS:
        all_lessons.append(dict(l, pages=list(range(l["p_start"], l["p_end"] + 1))))

    verses_catalog = build_verses_catalog()
    scenes = build_scenes()
    glossary = build_glossary()
    pages, interactions, explanations = build_pages_and_interactions(all_lessons, scenes, glossary)
    assessments = {
        "quiz-qur-s1": S1_QUIZ,
        "quiz-qur-s2": S2_QUIZ,
        "quiz-qur-s3": S3_QUIZ,
    }
    taqwim_drills = build_taqwim_drills()
    hifz_drills = build_hifz_drills()

    payload = {
        "manifest": MANIFEST,
        "units": SECTIONS_AS_UNITS,
        "pages": pages,
        "lessons": all_lessons,
        "interactions": interactions,
        "explanations": explanations,
        "glossary": glossary,
        "assessments": assessments,
        "taqwim_drills": taqwim_drills,
        "hifz_drills": hifz_drills,
        "scenes": scenes,
        "verses": verses_catalog,
        "waqf_marks": {k: {"symbol": sym, "desc": desc} for k, (sym, desc) in WAQF_MARKS.items()},
        "basmala": BASMALA_UTHMANI,
    }

    for directory in (DATA_DIR, ANDROID_DATA_DIR):
        os.makedirs(directory, exist_ok=True)
        for key in [
            "manifest", "units", "pages", "lessons", "interactions", "explanations",
            "glossary", "assessments", "taqwim_drills", "hifz_drills", "scenes", "verses"
        ]:
            with open(os.path.join(directory, f"{key}.json"), "w", encoding="utf-8") as f:
                json.dump(payload[key], f, ensure_ascii=False, indent=2)
        with open(os.path.join(directory, "data_bundle.js"), "w", encoding="utf-8") as f:
            f.write(f"{BUNDLE_VAR} = ")
            json.dump(payload, f, ensure_ascii=False)
            f.write(";\n")

    total_qs = sum(len(v) for v in assessments.values())
    total_tq_mcqs = sum(len(v) for v in taqwim_drills.values())
    bundle_kb = os.path.getsize(os.path.join(DATA_DIR, "data_bundle.js")) // 1024
    print(f"[✓] Precision Quran Curriculum Pack built!")
    print(f"    - Pages: {len(pages)} (PDF 2..189 -> Book 5..192), Lessons: {len(all_lessons)} (13+3+18)")
    print(f"    - Verified Tanzil verses: {len(verses_catalog)}, Offline Husary MP3s attached")
    print(f"    - Section Assessments: {total_qs} Qs | Lesson Taqwim MCQs: {total_tq_mcqs} Qs | Hifz Drills: {len(hifz_drills)}")
    print(f"    - Offline data_bundle.js size: {bundle_kb} KB")


if __name__ == "__main__":
    main()
