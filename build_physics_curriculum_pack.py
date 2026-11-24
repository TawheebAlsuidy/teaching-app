#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builder script for Grade 12 Physics Complete Curriculum Data Pack
Generates all 11 standardized JSON/JS datasets for Thaker Interactive Textbook Engine v2.0
"""
import os
import json

BASE_DIR = "/media/tawheeb/New Volume2/ذاكر/teaching-app"
PHYSICS_DATA_DIR = f"{BASE_DIR}/data/curriculum/grade12/physics"
os.makedirs(PHYSICS_DATA_DIR, exist_ok=True)

# 1. MANIFEST
manifest = {
    "schema_version": "2.0.0",
    "pack_id": "phys-g12-interactive-2026",
    "subject": "physics",
    "grade": 12,
    "edition": {
        "title": "الفيزياء - الصف الثالث الثانوي - القسم العلمي",
        "ministry": "الجمهورية اليمنية - وزارة التربية والتعليم - قطاع المناهج",
        "curriculum_version": "1447هـ - 2026م",
        "official_pdf": "كتاب-فيزياء-ثالث-ثانوي-اليمن.pdf",
        "total_pdf_pages": 219,
        "start_pdf_page": 6,
        "end_pdf_page": 219,
        "total_book_pages": 214
    },
    "features": {
        "original_page_rendering": True,
        "interactive_overlays": True,
        "smart_text_bottom_sheet": True,
        "explanation_levels_count": 3,
        "interactive_3d_physics_lab": True,
        "interactive_step_by_step_equations": True,
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
        "title": "الوحدة الأولى: كمية التحرك والمقذوفات",
        "short_desc": "كمية التحرك الخطي والزاوي، التصادم في بعدين، الصواريخ وسرعة الإفلات، والأقمار وحركة المقذوفات",
        "page_start": 9,
        "page_end": 28,
        "pdf_start": 10,
        "pdf_end": 29,
        "key_laws": [
            "قانون حفظ كمية التحرك: m1*v1 + m2*v2 = m1*v1' + m2*v2'",
            "سرعة الإفلات: v_esc = sqrt(2*G*M / R)",
            "السرعة المدارية للقمر: v_o = sqrt(G*M / r)",
            "كمية التحرك الزاوي: L = I * omega",
            "أقصى ارتفاع للمقذوف: H = (v0 * sin(theta))^2 / (2*g)",
            "المدى الأفقي: R = (v0^2 * sin(2*theta)) / g"
        ],
        "real_world_apps": [
            "إطلاق الصواريخ الفضائية ذاتية الدفع واستكشاف الفضاء",
            "مدارات الأقمار الصناعية للاتصالات والطقس والبث التلفزيوني",
            "تطبيقات حركة القذائف في الرياضة والملاحة والدفاع الجوي"
        ],
        "lab_id": "lab-phys-u1-projectiles"
    },
    {
        "id": "u2",
        "order": 2,
        "title": "الوحدة الثانية: التيار المتردد (المتناوب)",
        "short_desc": "توليد التيار المتردد (الدينامو)، الأميتر الحراري، ودوائر المقاومة والمكثف والملف (RLC) ودائرة الرنين والمهتزة",
        "page_start": 29,
        "page_end": 60,
        "pdf_start": 30,
        "pdf_end": 61,
        "key_laws": [
            "القوة الدافعة الحثية للدينامو: E = N * A * B * omega * sin(omega*t)",
            "القيمة الفعالة: I_eff = I_max / sqrt(2) = 0.707 * I_max",
            "المفاعلة السعوية: X_C = 1 / (2 * pi * f * C)",
            "المفاعلة الحثية: X_L = 2 * pi * f * L",
            "معاوقة دائرة RLC: Z = sqrt(R^2 + (X_L - X_C)^2)",
            "تردد الرنين: f_0 = 1 / (2 * pi * sqrt(L * C))"
        ],
        "real_world_apps": [
            "محطات ومولدات توليد الطاقة الكهربائية (الدينامو)",
            "شبكات نقل الكهرباء المنزلية والخطوط الوطنية باليمن (220V/50Hz)",
            "دوائر التوليف والراديو والمستقبلات اللاسلكية"
        ],
        "lab_id": "lab-phys-u2-ac-circuits"
    },
    {
        "id": "u3",
        "order": 3,
        "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات",
        "short_desc": "بلورة السيليكون النقية والمطعمة، الوصلة الثنائية (الدايود) وتقويم التيار، والترانزستور واستخداماته",
        "page_start": 61,
        "page_end": 84,
        "pdf_start": 62,
        "pdf_end": 85,
        "key_laws": [
            "تيار الترانزستور: I_e = I_b + I_c",
            "معامل التكبير للتيار: beta = I_c / I_b",
            "معامل التوزيع: alpha = I_c / I_e = beta / (1 + beta)",
            "جهد الحاجز للسيليكون = 0.7V وللجرمانيوم = 0.3V"
        ],
        "real_world_apps": [
            "المعالجات الدقيقة وشرائح الهواتف الذكية وأجهزة الحاسوب",
            "محولات الطاقة وشواحن الهواتف وخلايا الطاقة الشمسية",
            "مكبرات الصوت والمفاتيح الإلكترونية فائقة السرعة"
        ],
        "lab_id": "lab-phys-u3-semiconductors"
    },
    {
        "id": "u4",
        "order": 4,
        "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات",
        "short_desc": "أشعة المهبط، كاشف الذبذبات (الأوسيلوسكوب)، الرادار، والإرسال والاستقبال اللاسلكي والتلفاز الملون",
        "page_start": 85,
        "page_end": 113,
        "pdf_start": 86,
        "pdf_end": 114,
        "key_laws": [
            "طاقة حركة إلكترونات المهبط: 0.5 * m * v^2 = e * V",
            "معادلة انتشار الموجة: c = f * lambda  (حيث c = 3*10^8 m/s)",
            "حساب مسافة الهدف بالرادار: d = (c * t) / 2"
        ],
        "real_world_apps": [
            "أجهزة رسم القلب والموجات الطبية وشاشات العرض المخبرية",
            "الملاحة الجوية والبحرية ومراقبة الطيران بالرادار",
            "محطات البث الإذاعي والتلفزيوني والأقمار الرقمية"
        ],
        "lab_id": "lab-phys-u4-crt-radar"
    },
    {
        "id": "u5",
        "order": 5,
        "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور",
        "short_desc": "النماذج الذرية، طيف ذرة الهيدروجين، فرضية بلانك لتكميم الطاقة، ونظرية بور ومستويات الطاقة",
        "page_start": 114,
        "page_end": 143,
        "pdf_start": 115,
        "pdf_end": 144,
        "key_laws": [
            "تكميم الطاقة لبلانك: E = n * h * nu = n * h * (c / lambda)",
            "طاقة المستوى لذرة الهيدروجين: E_n = -13.6 / (n^2)  eV",
            "طاقة الفوتون المنبعث: Delta E = E_final - E_initial = h * nu",
            "نصف قطر مدار بور: r_n = r_1 * n^2 = 0.53 * 10^-10 * n^2  m"
        ],
        "real_world_apps": [
            "التحليل الطيفي الكيميائي لتحديد مكونات المواد والنجوم البعيدة",
            "مصابيح النيون وتفريغ الغازات الموفرة للطاقة",
            "المجاهر الإلكترونية وتقنيات النانو"
        ],
        "lab_id": "lab-phys-u5-bohr-atom"
    },
    {
        "id": "u6",
        "order": 6,
        "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر)",
        "short_desc": "الظاهرة الكهروضوئية وتفسير أينشتاين، تجربة مليكان، الأشعة السينية (X-rays)، وتوليد الليزر وتطبيقاته",
        "page_start": 144,
        "page_end": 172,
        "pdf_start": 145,
        "pdf_end": 173,
        "key_laws": [
            "معادلة أينشتاين الكهروضوئية: h * nu = Phi + KE_max",
            "دالة الشغل: Phi = h * nu_0",
            "جهد الإيقاف: KE_max = e * V_0",
            "أقصر طول موجي للأشعة السينية: lambda_min = (h * c) / (e * V)"
        ],
        "real_world_apps": [
            "أبواب المصاعد الآلية وأجهزة الإنذار والخلايا الضوئية",
            "أجهزة التصوير بالأشعة السينية في المستشفيات وأمن المطارات",
            "جراحة العيون بالفيمتو ليزر وقارئات الباركود والألياف الضوئية"
        ],
        "lab_id": "lab-phys-u6-photoelectric-laser"
    },
    {
        "id": "u7",
        "order": 7,
        "title": "الوحدة السابعة: الفيزياء النووية",
        "short_desc": "تركيب النواة، النشاط الإشعاعي (ألفا، بيتا، جاما)، قانون عمر النصف، طاقة الربط النووية، والانشطار والمفاعلات",
        "page_start": 173,
        "page_end": 184,
        "pdf_start": 174,
        "pdf_end": 185,
        "key_laws": [
            "معادلة تكافؤ الكتلة والطاقة لأينشتاين: E = Delta m * c^2",
            "طاقة الربط النووية: BE = Delta m (بوحدة amu) * 931.5  MeV",
            "نقص الكتلة: Delta m = [Z*m_p + N*m_n] - M_nucleus",
            "قانون النشاط الإشعاعي: N(t) = N_0 * (0.5)^(t / T_half)"
        ],
        "real_world_apps": [
            "توليد الكهرباء النظيفة بالمفاعلات النووية السلمية",
            "العلاج الإشعاعي للأورام والطب النووي والنظائر المشعة",
            "التأريخ الإشعاعي بالكربون-14 لتحديد أعمار الآثار والصخور"
        ],
        "lab_id": "lab-phys-u7-nuclear"
    },
    {
        "id": "u8",
        "order": 8,
        "title": "الوحدة الثامنة: الطاقة الشمسية وتطبيقاتها",
        "short_desc": "الطيف الشمسي، توليد الطاقة الحرارية الشمسية، توليد الكهرباء بالخلايا الضوئية واستخداماتها في اليمن",
        "page_start": 185,
        "page_end": 197,
        "pdf_start": 186,
        "pdf_end": 198,
        "key_laws": [
            "الثابت الشمسي = 1367 W/m^2 خارج الغلاف الجوي",
            "كفاءة الخلية الشمسية: eta = (P_out / P_in) * 100%",
            "الطاقة الحرارية الممتصة: Q = m * c_p * Delta T"
        ],
        "real_world_apps": [
            "منظومات الطاقة الشمسية الكهروضوئية المنزلية في كافة محافظات اليمن",
            "مضخات المياه الزراعية التي تعمل بالطاقة الشمسية في أرياف اليمن",
            "سخانات المياه الشمسية وتوليد البخار الحراري"
        ],
        "lab_id": "lab-phys-u8-solar-energy"
    },
    {
        "id": "u9",
        "order": 9,
        "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية",
        "short_desc": "نشأة الكون وتمدده، المجرات، تصنيف ودورة حياة النجوم (العمالقة والثقوب السوداء)، والمسافات الفلكية",
        "page_start": 198,
        "page_end": 219,
        "pdf_start": 199,
        "pdf_end": 220,
        "key_laws": [
            "قانون هابل لتمدد الكون: v = H_0 * d",
            "قانون فين لإزاحة الطيف: lambda_max * T = 2.898 * 10^-3  m*K",
            "السنة الضوئية = 9.46 * 10^12 km"
        ],
        "real_world_apps": [
            "التلسكوبات الفلكية الفضائية (جيمس ويب وهابل)",
            "تحديد درجات حرارة أسطح النجوم وتركيبها من ألوانها وأطيافها",
            "أنظمة الملاحة بالأقمار الفضائية وتتبع حركة الأجرام الكونية"
        ],
        "lab_id": "lab-phys-u9-cosmology"
    }
]

# 3. PAGES MAPPING
pages = []
for p in range(6, 220):
    pdf_num = p
    book_num = p - 1 # PDF 10 is book page 9
    
    # Identify unit
    cur_unit = None
    for u in units:
        if u["pdf_start"] <= pdf_num <= u["pdf_end"]:
            cur_unit = u
            break
            
    p_type = "lesson"
    if pdf_num in [6, 7, 8]:
        p_type = "contents"
        title = f"فهرس الموضوعات (الجزء {pdf_num - 5})"
    elif cur_unit and pdf_num == cur_unit["pdf_start"]:
        p_type = "unit_cover"
        title = f"{cur_unit['title']} — غلاف وأهداف الوحدة"
    elif cur_unit and pdf_num >= cur_unit["pdf_end"] - 1:
        p_type = "assessment"
        title = f"تقويم وتمارين ومسائل {cur_unit['title']}"
    else:
        title = f"فيزياء 3 ثانوي — صفحة {book_num}" if cur_unit is None else f"{cur_unit['title']} — ص {book_num}"
        
    page_obj = {
        "page_id": f"phys12-p{pdf_num:03d}",
        "book_page": book_num if pdf_num >= 10 else pdf_num,
        "pdf_page": pdf_num,
        "type": p_type,
        "title": title,
        "unit_id": cur_unit["id"] if cur_unit else None,
        "image": f"assets/curriculum/grade12/physics/pages/page_{pdf_num:03d}_opt.jpg",
        "image_full": f"assets/curriculum/grade12/physics/pages/page_{pdf_num:03d}.jpg",
        "aspect_ratio": 0.7083
    }
    pages.append(page_obj)

# 4. LESSONS
lessons = [
    # Unit 1
    {"id": "phys-u1-l1", "unitId": "u1", "order": 1, "title": "كمية التحرك والتصادم في بعدين", "pages": [10, 14], "pdf_pages": [11, 15]},
    {"id": "phys-u1-l2", "unitId": "u1", "order": 2, "title": "الصواريخ ذاتية الدفع وسرعة الإفلات", "pages": [14, 18], "pdf_pages": [15, 19]},
    {"id": "phys-u1-l3", "unitId": "u1", "order": 3, "title": "حركة الأقمار الصناعية وكمية التحرك الزاوي", "pages": [19, 22], "pdf_pages": [20, 23]},
    {"id": "phys-u1-l4", "unitId": "u1", "order": 4, "title": "حركة المقذوفات في مجال الجاذبية", "pages": [23, 26], "pdf_pages": [24, 27]},
    {"id": "phys-u1-l5", "unitId": "u1", "order": 5, "title": "تقويم ومسائل الوحدة الأولى", "pages": [27, 28], "pdf_pages": [28, 29]},

    # Unit 2
    {"id": "phys-u2-l1", "unitId": "u2", "order": 1, "title": "مفهوم التيار المتردد ومولد الدينامو", "pages": [30, 36], "pdf_pages": [31, 37]},
    {"id": "phys-u2-l2", "unitId": "u2", "order": 2, "title": "الأميتر الحراري وقانون أوم في دوائر المتردد", "pages": [37, 39], "pdf_pages": [38, 40]},
    {"id": "phys-u2-l3", "unitId": "u2", "order": 3, "title": "المكثف والملف في دوائر التيار المتردد والمفاعلة", "pages": [40, 46], "pdf_pages": [41, 47]},
    {"id": "phys-u2-l4", "unitId": "u2", "order": 4, "title": "دائرة RLC المتوالية والمعاوقة وزاوية الطور", "pages": [47, 50], "pdf_pages": [48, 51]},
    {"id": "phys-u2-l5", "unitId": "u2", "order": 5, "title": "دائرة الرنين والدائرة المهتزة وتوصيل المعاوقات", "pages": [51, 57], "pdf_pages": [52, 58]},
    {"id": "phys-u2-l6", "unitId": "u2", "order": 6, "title": "تقويم ومسائل التيار المتردد", "pages": [58, 60], "pdf_pages": [59, 61]},

    # Unit 3
    {"id": "phys-u3-l1", "unitId": "u3", "order": 1, "title": "أشباه الموصلات النقية وغير النقية (التطعيم)", "pages": [62, 66], "pdf_pages": [63, 67]},
    {"id": "phys-u3-l2", "unitId": "u3", "order": 2, "title": "الوصلة الثنائية (الدايود) وتقويم التيار", "pages": [67, 70], "pdf_pages": [68, 71]},
    {"id": "phys-u3-l3", "unitId": "u3", "order": 3, "title": "الترانزستور: تركيبه واستخداماته كمكبر ومفتاح", "pages": [71, 79], "pdf_pages": [72, 80]},
    {"id": "phys-u3-l4", "unitId": "u3", "order": 4, "title": "تقويم ومسائل الإلكترونيات", "pages": [80, 84], "pdf_pages": [81, 85]},

    # Unit 4
    {"id": "phys-u4-l1", "unitId": "u4", "order": 1, "title": "التفريغ الكهربائي في الغازات وأنبوبة أشعة المهبط", "pages": [87, 89], "pdf_pages": [88, 90]},
    {"id": "phys-u4-l2", "unitId": "u4", "order": 2, "title": "كاشف الذبذبات (الأوسيلوسكوب) والرادار", "pages": [90, 94], "pdf_pages": [91, 95]},
    {"id": "phys-u4-l3", "unitId": "u4", "order": 3, "title": "إرسال واستقبال الموجات اللاسلكية والتلفاز الملون", "pages": [95, 106], "pdf_pages": [96, 107]},
    {"id": "phys-u4-l4", "unitId": "u4", "order": 4, "title": "تقويم الأجهزة الإلكترونية والاتصالات", "pages": [107, 113], "pdf_pages": [108, 114]},

    # Unit 5
    {"id": "phys-u5-l1", "unitId": "u5", "order": 1, "title": "نماذج الذرة وأطياف الانبعاث وطيف الهيدروجين", "pages": [115, 122], "pdf_pages": [116, 123]},
    {"id": "phys-u5-l2", "unitId": "u5", "order": 2, "title": "إشعاع الجسم الأسود وتكميم الطاقة لبلانك", "pages": [123, 124], "pdf_pages": [124, 125]},
    {"id": "phys-u5-l3", "unitId": "u5", "order": 3, "title": "نظرية بور لذرة الهيدروجين ومستويات الطاقة", "pages": [125, 141], "pdf_pages": [126, 142]},
    {"id": "phys-u5-l4", "unitId": "u5", "order": 4, "title": "تقويم ومسائل الفيزياء الذرية", "pages": [142, 143], "pdf_pages": [143, 144]},

    # Unit 6
    {"id": "phys-u6-l1", "unitId": "u6", "order": 1, "title": "الظاهرة الكهروضوئية وتفسير أينشتاين الكمي", "pages": [145, 156], "pdf_pages": [146, 157]},
    {"id": "phys-u6-l2", "unitId": "u6", "order": 2, "title": "الأشعة السينية (أشعة إكس) وخصائصها وتوليدها", "pages": [157, 162], "pdf_pages": [158, 163]},
    {"id": "phys-u6-l3", "unitId": "u6", "order": 3, "title": "الليزر: فكرته، شروطه، وجهاز هيليوم - نيون", "pages": [163, 170], "pdf_pages": [164, 171]},
    {"id": "phys-u6-l4", "unitId": "u6", "order": 4, "title": "تقويم ومسائل الإشعاع والمادة", "pages": [171, 172], "pdf_pages": [172, 173]},

    # Unit 7
    {"id": "phys-u7-l1", "unitId": "u7", "order": 1, "title": "تركيب النواة والنشاط الإشعاعي الطبيعي", "pages": [174, 178], "pdf_pages": [175, 179]},
    {"id": "phys-u7-l2", "unitId": "u7", "order": 2, "title": "قانون عمر النصف وطاقة الربط النووية", "pages": [179, 180], "pdf_pages": [180, 181]},
    {"id": "phys-u7-l3", "unitId": "u7", "order": 3, "title": "الانشطار والتفاعل المتسلسل والمفاعلات النووية", "pages": [181, 182], "pdf_pages": [182, 183]},
    {"id": "phys-u7-l4", "unitId": "u7", "order": 4, "title": "تقويم ومسائل الفيزياء النووية", "pages": [183, 184], "pdf_pages": [184, 185]},

    # Unit 8
    {"id": "phys-u8-l1", "unitId": "u8", "order": 1, "title": "الشمس مصدر الطاقة وأنواع الإشعاعات الشمسية", "pages": [186, 188], "pdf_pages": [187, 189]},
    {"id": "phys-u8-l2", "unitId": "u8", "order": 2, "title": "تطبيقات الطاقة الشمسية وتوليد الحرارة والكهرباء", "pages": [189, 196], "pdf_pages": [190, 197]},
    {"id": "phys-u8-l3", "unitId": "u8", "order": 3, "title": "تقويم وتطبيقات الطاقة الشمسية في اليمن", "pages": [197, 197], "pdf_pages": [198, 198]},

    # Unit 9
    {"id": "phys-u9-l1", "unitId": "u9", "order": 1, "title": "مفهوم الكون ونظرية الانفجار العظيم والمجرات", "pages": [199, 203], "pdf_pages": [200, 204]},
    {"id": "phys-u9-l2", "unitId": "u9", "order": 2, "title": "النجوم ودورة حياتها والثقوب السوداء", "pages": [204, 207], "pdf_pages": [205, 208]},
    {"id": "phys-u9-l3", "unitId": "u9", "order": 3, "title": "المسافات الفلكية وتقدير حرارة النجوم من ألوانها", "pages": [208, 209], "pdf_pages": [209, 210]},
    {"id": "phys-u9-l4", "unitId": "u9", "order": 4, "title": "تقويم الوحدة وقاموس المصطلحات الفيزيائية", "pages": [210, 219], "pdf_pages": [211, 220]}
]

# Write initial JSON datasets
with open(f"{PHYSICS_DATA_DIR}/manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

with open(f"{PHYSICS_DATA_DIR}/units.json", "w", encoding="utf-8") as f:
    json.dump(units, f, ensure_ascii=False, indent=2)

with open(f"{PHYSICS_DATA_DIR}/pages.json", "w", encoding="utf-8") as f:
    json.dump(pages, f, ensure_ascii=False, indent=2)

with open(f"{PHYSICS_DATA_DIR}/lessons.json", "w", encoding="utf-8") as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print("[✓] Physics manifest, units, pages, lessons generated successfully!")
