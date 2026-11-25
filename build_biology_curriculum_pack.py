#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder script for Grade 12 Biology Complete Curriculum Data Pack
Generates all standardized JSON/JS datasets for Thaker Interactive Textbook Engine v2.0
"""
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BIOLOGY_DATA_DIR = f"{BASE_DIR}/data/curriculum/grade12/biology"
os.makedirs(BIOLOGY_DATA_DIR, exist_ok=True)

# 1. MANIFEST
manifest = {
    "schema_version": "2.0.0",
    "pack_id": "bio-g12-interactive-2026",
    "subject": "biology",
    "grade": 12,
    "edition": {
        "title": "الأحياء - الصف الثالث الثانوي - القسم العلمي",
        "ministry": "الجمهورية اليمنية - وزارة التربية والتعليم - قطاع المناهج",
        "curriculum_version": "1447هـ - 2026م",
        "official_pdf": "الأحياء-للصف-الثالث-الثانوي.pdf",
        "total_pdf_pages": 221,
        "start_pdf_page": 4,
        "end_pdf_page": 221,
        "total_book_pages": 218
    },
    "features": {
        "original_page_rendering": True,
        "interactive_overlays": True,
        "smart_text_bottom_sheet": True,
        "explanation_levels_count": 3,
        "interactive_3d_anatomy_explorer": True,
        "biological_process_steppers": True,
        "simulated_activities": True,
        "remediation_mistake_review": True,
        "offline_audio_synthesis": True,
        "yemeni_companion_prompts": True,
        "multi_student_profiles": True
    },
    "data_files": [
        "pages.json", "units.json", "lessons.json", "interactions.json",
        "explanations.json", "diagrams.json", "activities.json",
        "assessments.json", "glossary.json"
    ]
}

# 2. UNITS
units = [
    {
        "id": "u1",
        "order": 1,
        "title": "الوحدة الأولى: الجهاز العصبي وأعضاء الحس",
        "short_desc": "التنظيم العصبي في اللافقاريات، تركيب العصبون والغراء العصبي، جهد الفعل والسيال والتشابك، ومستقبلات الرؤية والسمع والتذوق والشم",
        "page_start": 8,
        "page_end": 39,
        "pdf_start": 7,
        "pdf_end": 38,
        "key_concepts": [
            "الخلية العصبية (العصبون Neuron) هي وحدة بناء ووظيفة الجهاز العصبي",
            "جهد الراحة (-70mV) يعتمد على مضخة الصوديوم-بوتاسيوم والنفاذية الاختيارية",
            "جهد الفعل وموجة إزالة الاستقطاب ودخول أيونات Na+",
            "التشابك العصبي والنواقل الكيميائية (الأسيتيل كولين)",
            "المستقبلات الضوئية في شبكية العين (العصي للرؤية الليلية والمخاريط للألوان)",
            "المستقبلات الآلية في قوقعة الأذن الداخلية (عضو كورتي)"
        ],
        "real_world_apps": [
            "فهم أمراض الجهاز العصبي كالتصلب المتعدد وتلف غمد الميالين",
            "آلية عمل التخدير الموضعي في عيادات الأسنان بغلق قنوات الصوديوم",
            "فحوصات البصر والسمع وتصحيح عيوب الإبصار (قصر وطول النظر)"
        ],
        "lab_id": "lab-bio-u1-nervous"
    },
    {
        "id": "u2",
        "order": 2,
        "title": "الوحدة الثانية: التنظيم الهرموني وجهاز الغدد الصماء",
        "short_desc": "الهرمونات النباتية (الأكسينات والانتحاء)، جهاز الغدد الصماء البشري، النخامية، الدرقية، الكظرية، وجزر لانجرهانز وتنظيم السكر",
        "page_start": 40,
        "page_end": 60,
        "pdf_start": 39,
        "pdf_end": 59,
        "key_concepts": [
            "الأكسينات تسبب استطالة خلايا الجانب المظلم للبادرة النباتية فيحدث الانتحاء الضوئي",
            "الغدة النخامية (سيدة الغدد) تفرز هرمون النمو والموجهات للغدد الأخرى",
            "هرمون الثايروكسين من الغدة الدرقية ينظم معدل الأيض الأساسي",
            "تنظيم مستوى الجلوكوز في الدم (80-120 mg/dL) باتزان الإنسولين والجلوكاجون",
            "هرمونات الطوارئ (الأدرينالين والنورأدرينالين) من نخاع الكظرية"
        ],
        "real_world_apps": [
            "تشخيص وعلاج داء السكري واستخدام مضخات وحقن الإنسولين",
            "علاج اضطرابات هرمون النمو (العملقة والقزامة) والجويتر الناتج عن نقص اليود",
            "استخدام منظمات النمو والأكسينات في الزراعة اليمنية لتحسين المحاصيل"
        ],
        "lab_id": "lab-bio-u2-endocrine"
    },
    {
        "id": "u3",
        "order": 3,
        "title": "الوحدة الثالثة: التكاثر في الكائنات الحية",
        "short_desc": "صور التكاثر اللاجنسي، التكاثر الجنسي في النباتات الزهرية والإخصاب المزدوج، والتكاثر البشري وتكوين الأمشاج والجنين",
        "page_start": 61,
        "page_end": 95,
        "pdf_start": 60,
        "pdf_end": 94,
        "key_concepts": [
            "الانشطار الثنائي، التبرعم، التجرثم، والتجدد كصور للتكاثر اللاجنسي بالميتوزي",
            "تركيب الزهرة: الأسدية (المتوك وحبوب اللقاح) والكرابل (المبيض والبويضات)",
            "الإخصاب المزدوج في النباتات الزهرية (تكوين الجنين 2n والإندوسبيرم 3n)",
            "تكوين الحيوانات المنوية في الأنيبيبات المنوية وتكوين البويضة في حويصلة جراف",
            "الدورة الشهرية وتنظيم هرمونات FSH و LH والإستروجين والبروجسترون"
        ],
        "real_world_apps": [
            "تقنيات زراعة الأنسجة النباتية في الإكثار الزراعي السريع",
            "رعاية الأمومة والطفولة وصحة الجهاز التناسلي ومتابعة نمو الجنين بالسونار",
            "علاج حالات العقم وتأخر الإنجاب بالحقن المجهري (أطفال الأنابيب)"
        ],
        "lab_id": "lab-bio-u3-reproduction"
    },
    {
        "id": "u4",
        "order": 4,
        "title": "الوحدة الرابعة: أساسيات علم الوراثة المندلية",
        "short_desc": "تجارب مندل، قانون انعزال العوامل، قانون التوزيع الحر، مربع بانيت، فصائل الدم، وعامل الريسوس، وتحديد الجنس والصفات المرتبطة",
        "page_start": 96,
        "page_end": 130,
        "pdf_start": 95,
        "pdf_end": 129,
        "key_concepts": [
            "القانون الأول لمندل: تنعزل العوامل الوراثية (الأليلات) عند تكوين الأمشاج",
            "القانون الثاني لمندل: التوزيع الحر للجينات المحمولة على كروموسومات مختلفة",
            "الطراز الجيني (Genotype) والطراز المظهري (Phenotype)",
            "توارث فصائل الدم بنظام الجينات المتعددة والسيادة المشتركة (IA, IB, i)",
            "الصفات المرتبطة بالجنس المحمولة على الكروموسوم X (عمى الألوان والهيموفيليا)"
        ],
        "real_world_apps": [
            "فحوصات ما قبل الزواج لتجنب الأمراض الوراثية ونزف الدم الوراثي في اليمن",
            "فحوصات نقل الدم الآمنة واختبار عامل الريسوس Rh للحوامل",
            "تحسين السلالات الحيوانية والنباتية بالتهجين الوراثي المدروس"
        ],
        "lab_id": "lab-bio-u4-mendelian-genetics"
    },
    {
        "id": "u5",
        "order": 5,
        "title": "الوحدة الخامسة: الوراثة الجزيئية (DNA و RNA وتخليق البروتين)",
        "short_desc": "تركيب النيوكليوتيد ولولب DNA المزدوج، تضاعف DNA وشوكة التضاعف، عملية النسخ، شفرة الكودونات، والترجمة في الرايبوسوم والطفرات",
        "page_start": 131,
        "page_end": 150,
        "pdf_start": 130,
        "pdf_end": 149,
        "key_concepts": [
            "النموذج اللولبي المزدوج لواطسون وكريك: تكامل القواعد A=T و G≡C",
            "تضاعف DNA شبه المحافظ بواسطة إنزيمات فك الالتواء والبلمرة والربط",
            "النسخ: بناء جزيء mRNA من القالب في النواة بإنزيم بلمرة RNA",
            "الشفرة الوراثية: كودون ثلاثي يشفر لحمض أميني محدد (كودون البدء AUG)",
            "الترجمة: تعاون mRNA و tRNA والرايبوسوم لتكوين السلسلة الببتيدية"
        ],
        "real_world_apps": [
            "البصمة الوراثية (DNA Fingerprinting) في الطب الشرعي وإثبات النسب",
            "إنتاج الإنسولين البشري وهرمون النمو بتقنية الهندسة الوراثية و DNA معاد التركيب",
            "فهم أسباب الطفرات الجينية المستحدثة بالمسرطنات والإشعاعات"
        ],
        "lab_id": "lab-bio-u5-molecular-genetics"
    },
    {
        "id": "u6",
        "order": 6,
        "title": "الوحدة السادسة: التطور والتنوع الأحيائي",
        "short_desc": "أدلة التطور من التشريح المقارن والأجنة والأحافير، نظريات التكيف والانتخاب الطبيعي، والتنوع الوراثي والتكيف البيئي",
        "page_start": 151,
        "page_end": 170,
        "pdf_start": 150,
        "pdf_end": 169,
        "key_concepts": [
            "الأعضاء المتماثلة تشترك في الأصل وتختلف في الوظيفة كدليل تشريحي",
            "الانتخاب الطبيعي: بقاء الأفراد الأكثر تكيفاً مع بيئتهم لنقل جيناتهم للأجيال التالية",
            "التكيفات المورفولوجية والفسيولوجية والسلوكية للكائنات الحية"
        ],
        "real_world_apps": [
            "مقاومة البكتيريا للمضادات الحيوية كنموذج حي للانتخاب والتكيف السريع",
            "تكيف النباتات والحيوانات مع الجفاف في البيئات الصحراوية اليمنية"
        ],
        "lab_id": "lab-bio-u6-evolution"
    },
    {
        "id": "u7",
        "order": 7,
        "title": "الوحدة السابعة: البيئة والتوازن البيئي",
        "short_desc": "العلاقات الحيوية المتبادلة، دورات العناصر (الكربون، النيتروجين)، التلوث البيئي والاحتباس الحراري، وحماية المحميات في اليمن",
        "page_start": 171,
        "page_end": 186,
        "pdf_start": 170,
        "pdf_end": 185,
        "key_concepts": [
            "العلاقات الحيوية: التكافل (تبادل المنفعة والمعايشة)، التطفل، والافتراس",
            "دورة النيتروجين ودور بكتيريا تثبيت النيتروجين في العقد الجذرية للبقوليات",
            "أسباب اختلال التوازن البيئي والغازات الدفيئة المسببة للاحتباس الحراري",
            "المحميات الطبيعية اليمنية الفريدة (جزيرة سقطرى ومحمية عتمة)"
        ],
        "real_world_apps": [
            "مكافحة التصحر وترشيد استخدام المبيدات الحشرية والحفاظ على التنوع الحيوي",
            "إعادة التدوير واستخدام الطاقة المتجددة للحد من الانبعاثات الكربونية في اليمن"
        ],
        "lab_id": "lab-bio-u7-ecology"
    },
    {
        "id": "u8",
        "order": 8,
        "title": "الوحدة الثامنة: تاريخ الأرض وجيولوجيا اليمن",
        "short_desc": "الصخور الرسوبية، أنواع الأحافير وشروط التحفر، التأريخ النسبي والمطلق، السلم الجيولوجي، والطبقات الجيولوجية في اليمن",
        "page_start": 187,
        "page_end": 223,
        "pdf_start": 186,
        "pdf_end": 221,
        "key_concepts": [
            "شروط تكون الأحفورة: وجود هيكل صلب، والدفن السريع بمعزل عن الهواء",
            "الأحافير المرشدة تميز عصراً جيولوجياً محدداً لانتشارها الجغرافي الواسع ومداها الزمني القصير",
            "التأريخ الإشعاعي بنصف العمر لليورانيوم والبوتاسيوم والكربون-14",
            "تتابع الطبقات الجيولوجية في اليمن (تكوين كحلان، عمران، والطويلة الحاملة للمياه والنفط)"
        ],
        "real_world_apps": [
            "استكشاف خزانات النفط والغاز والمياه الجوفية في أحواض مأرب وشبوة والمسيلة",
            "استغلال صخور البناء والرخام والجرانيت والبازلت في العمارة التراثية والحديثة باليمن"
        ],
        "lab_id": "lab-bio-u8-geology-yemen"
    }
]

# 3. PAGES MAPPING
pages = []
for p in range(4, 222):
    pdf_num = p
    book_num = p + 2 # PDF 7 is book page 8
    
    cur_unit = None
    for u in units:
        if u["pdf_start"] <= pdf_num <= u["pdf_end"]:
            cur_unit = u
            break
            
    p_type = "lesson"
    if pdf_num in [4, 5, 6]:
        p_type = "contents"
        title = f"فهرس الموضوعات (الجزء {pdf_num - 3})"
    elif cur_unit and pdf_num == cur_unit["pdf_start"]:
        p_type = "unit_cover"
        title = f"{cur_unit['title']} — غلاف وأهداف الوحدة"
    elif cur_unit and pdf_num >= cur_unit["pdf_end"] - 1:
        p_type = "assessment"
        title = f"تقويم وأنشطة {cur_unit['title']}"
    else:
        title = f"أحياء 3 ثانوي — صفحة {book_num}" if cur_unit is None else f"{cur_unit['title']} — ص {book_num}"
        
    page_obj = {
        "page_id": f"bio12-p{pdf_num:03d}",
        "book_page": book_num if pdf_num >= 7 else pdf_num,
        "pdf_page": pdf_num,
        "type": p_type,
        "title": title,
        "unit_id": cur_unit["id"] if cur_unit else None,
        "image": f"assets/curriculum/grade12/biology/pages/page_{pdf_num:03d}_opt.jpg",
        "image_full": f"assets/curriculum/grade12/biology/pages/page_{pdf_num:03d}.jpg",
        "aspect_ratio": 0.7083
    }
    pages.append(page_obj)

# 4. LESSONS
lessons = [
    # Unit 1
    {"id": "bio-u1-l1", "unitId": "u1", "order": 1, "title": "الإحساس في وحيدة الخلية واللافقاريات (الهيدرا والدودة)", "pages": [9, 11], "pdf_pages": [8, 10]},
    {"id": "bio-u1-l2", "unitId": "u1", "order": 2, "title": "تركيب النسيج العصبي والخلايا العصبية والغراء العصبي", "pages": [12, 17], "pdf_pages": [11, 16]},
    {"id": "bio-u1-l3", "unitId": "u1", "order": 3, "title": "جهد الراحة وجهد الفعل وانتقال السيال العصبي والتشابك", "pages": [18, 25], "pdf_pages": [17, 24]},
    {"id": "bio-u1-l4", "unitId": "u1", "order": 4, "title": "المستقبلات الحسية: العين والرؤية والشم والتذوق والسمع", "pages": [26, 36], "pdf_pages": [25, 35]},
    {"id": "bio-u1-l5", "unitId": "u1", "order": 5, "title": "تقويم وتمارين الجهاز العصبي وأعضاء الحس", "pages": [37, 39], "pdf_pages": [36, 38]},

    # Unit 2
    {"id": "bio-u2-l1", "unitId": "u2", "order": 1, "title": "التنظيم الهرموني في النبات وحركات الانتحاء", "pages": [41, 44], "pdf_pages": [40, 43]},
    {"id": "bio-u2-l2", "unitId": "u2", "order": 2, "title": "جهاز الغدد الصماء في الإنسان والغدة النخامية", "pages": [46, 50], "pdf_pages": [45, 49]},
    {"id": "bio-u2-l3", "unitId": "u2", "order": 3, "title": "الغدة الدرقية وجارات الدرقية والكظرية والبنكرياس", "pages": [51, 57], "pdf_pages": [50, 56]},
    {"id": "bio-u2-l4", "unitId": "u2", "order": 4, "title": "أمراض الجهاز الهرموني وصحته وتقويم الوحدة", "pages": [58, 60], "pdf_pages": [57, 59]},

    # Unit 3
    {"id": "bio-u3-l1", "unitId": "u3", "order": 1, "title": "صور التكاثر اللاجنسي في الكائنات الحية", "pages": [62, 68], "pdf_pages": [61, 67]},
    {"id": "bio-u3-l2", "unitId": "u3", "order": 2, "title": "التكاثر الجنسي في البدائيات والنباتات الزهرية والإخصاب", "pages": [69, 78], "pdf_pages": [68, 77]},
    {"id": "bio-u3-l3", "unitId": "u3", "order": 3, "title": "الجهاز التناسلي في الإنسان وتكوين الأمشاج والإخصاب", "pages": [79, 92], "pdf_pages": [78, 91]},
    {"id": "bio-u3-l4", "unitId": "u3", "order": 4, "title": "تقويم وتمارين التكاثر في الكائنات الحية", "pages": [93, 95], "pdf_pages": [92, 94]},

    # Unit 4
    {"id": "bio-u4-l1", "unitId": "u4", "order": 1, "title": "تجارب مندل وقوانين الوراثة المندلية (القانون 1 و 2)", "pages": [97, 110], "pdf_pages": [96, 109]},
    {"id": "bio-u4-l2", "unitId": "u4", "order": 2, "title": "الكروموسومات وفصائل الدم وعامل الريسوس Rh", "pages": [111, 121], "pdf_pages": [110, 120]},
    {"id": "bio-u4-l3", "unitId": "u4", "order": 3, "title": "تحديد الجنس والصفات المرتبطة والمتأثرة بالجنس", "pages": [122, 128], "pdf_pages": [121, 127]},
    {"id": "bio-u4-l4", "unitId": "u4", "order": 4, "title": "تقويم ومسائل الوراثة المندلية وسجل النسب", "pages": [129, 130], "pdf_pages": [128, 129]},

    # Unit 5
    {"id": "bio-u5-l1", "unitId": "u5", "order": 1, "title": "تركيب لولب DNA المزدوج وتضاعف المادة الوراثية", "pages": [132, 139], "pdf_pages": [131, 138]},
    {"id": "bio-u5-l2", "unitId": "u5", "order": 2, "title": "أنواع RNA والنسخ الوراثي والشفرة الوراثية", "pages": [140, 144], "pdf_pages": [139, 143]},
    {"id": "bio-u5-l3", "unitId": "u5", "order": 3, "title": "ترجمة البروتين على الرايبوسوم والطفرات الوراثية", "pages": [145, 149], "pdf_pages": [144, 148]},
    {"id": "bio-u5-l4", "unitId": "u5", "order": 4, "title": "تقويم الوراثة الجزيئية والهندسة الوراثية", "pages": [150, 150], "pdf_pages": [149, 149]},

    # Unit 6
    {"id": "bio-u6-l1", "unitId": "u6", "order": 1, "title": "أدلة التطور من التشريح المقارن والأحافير", "pages": [152, 157], "pdf_pages": [151, 156]},
    {"id": "bio-u6-l2", "unitId": "u6", "order": 2, "title": "نظريات التطور والانتخاب الطبيعي والتكيفات", "pages": [158, 168], "pdf_pages": [157, 167]},
    {"id": "bio-u6-l3", "unitId": "u6", "order": 3, "title": "تقويم الوحدة السادسة للتطور والتنوع", "pages": [169, 170], "pdf_pages": [168, 169]},

    # Unit 7
    {"id": "bio-u7-l1", "unitId": "u7", "order": 1, "title": "العلاقات الحيوية المتبادلة في النظام البيئي", "pages": [172, 175], "pdf_pages": [171, 174]},
    {"id": "bio-u7-l2", "unitId": "u7", "order": 2, "title": "دورات العناصر (الكربون والنيتروجين) والتلوث البيئي", "pages": [176, 183], "pdf_pages": [175, 182]},
    {"id": "bio-u7-l3", "unitId": "u7", "order": 3, "title": "حماية البيئة ومحميات سقطرى وعتمة باليمن وتقويم الوحدة", "pages": [184, 186], "pdf_pages": [183, 185]},

    # Unit 8
    {"id": "bio-u8-l1", "unitId": "u8", "order": 1, "title": "الصخور الرسوبية وطرق تكون الأحافير وشروط التحفر", "pages": [188, 201], "pdf_pages": [187, 200]},
    {"id": "bio-u8-l2", "unitId": "u8", "order": 2, "title": "التأريخ النسبي والمطلق والسلم الجيولوجي", "pages": [202, 213], "pdf_pages": [201, 212]},
    {"id": "bio-u8-l3", "unitId": "u8", "order": 3, "title": "جيولوجيا الجمهورية اليمنية وتتابع الطبقات", "pages": [214, 219], "pdf_pages": [213, 218]},
    {"id": "bio-u8-l4", "unitId": "u8", "order": 4, "title": "تقويم الوحدة الثامنة وقاموس المصطلحات الأحيائية", "pages": [220, 223], "pdf_pages": [219, 221]}
]

# Write initial JSON datasets
with open(f"{BIOLOGY_DATA_DIR}/manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

with open(f"{BIOLOGY_DATA_DIR}/units.json", "w", encoding="utf-8") as f:
    json.dump(units, f, ensure_ascii=False, indent=2)

with open(f"{BIOLOGY_DATA_DIR}/pages.json", "w", encoding="utf-8") as f:
    json.dump(pages, f, ensure_ascii=False, indent=2)

with open(f"{BIOLOGY_DATA_DIR}/lessons.json", "w", encoding="utf-8") as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print("[✓] Biology manifest, units, pages, lessons generated successfully!")
