window.THAKER_CURRICULUM_G12_MATH = {
  "manifest": {
    "schema_version": "2.0.0",
    "pack_id": "math-g12-interactive-2026",
    "subject": "math",
    "grade": 12,
    "edition": {
      "title": "الرياضيات - الصف الثالث الثانوي - القسم العلمي",
      "ministry": "الجمهورية اليمنية - وزارة التربية والتعليم - قطاع المناهج",
      "curriculum_version": "1447هـ - 2026م",
      "official_pdf": "الرياضيات-للصف-الثالث-الثانوي.pdf",
      "practice_pdf": "الرياضيات-التمارين-للصف-الثالث-الثانوي-القسم-العلمي.pdf",
      "total_pdf_pages": 259,
      "start_pdf_page": 9,
      "end_pdf_page": 258,
      "total_book_pages": 250,
      "page_offset": "book_page = pdf_page - 2",
      "workbook_start_pdf_page": 8,
      "workbook_end_pdf_page": 82
    },
    "features": {
      "original_page_rendering": true,
      "interactive_overlays": true,
      "smart_text_bottom_sheet": true,
      "explanation_levels_count": 3,
      "interactive_step_by_step_equations": true,
      "interactive_3d_geometry_lab": true,
      "simulated_activities": true,
      "remediation_mistake_review": true,
      "offline_audio_synthesis": true,
      "yemeni_companion_prompts": true,
      "multi_student_profiles": true
    },
    "data_files": [
      "manifest.json",
      "pages.json",
      "workbook_pages.json",
      "units.json",
      "lessons.json",
      "interactions.json",
      "explanations.json",
      "diagrams.json",
      "activities.json",
      "assessments.json",
      "glossary.json",
      "solution_steps.json",
      "geometry_lab.json",
      "data_bundle.js"
    ]
  },
  "units": [
    {
      "id": "u1",
      "order": 1,
      "title": "الوحدة الأولى: الأعداد المركبة",
      "short_desc": "مفهوم العدد المركب، تمثيله في مستوى أرغاند، القيمة المطلقة والزاوية، والصيغة القطبية",
      "page_start": 7,
      "page_end": 44,
      "pdf_start": 9,
      "pdf_end": 46,
      "workbook_start": 6,
      "workbook_end": 17,
      "key_laws": [
        "z = a + bi، i² = −1",
        "|z| = √(a² + b²)",
        "z = r(cos θ + i sin θ)"
      ],
      "real_world_apps": [
        "التيار المتردد والهندسة الكهربائية",
        "الإشارات والدوائر الإلكترونية",
        "تحويل الإحداثيات في المستوى"
      ]
    },
    {
      "id": "u2",
      "order": 2,
      "title": "الوحدة الثانية: مبرهنة دي موافر والتوسعة ذات الحدين",
      "short_desc": "مبرهنة دي موافر، الجذور النونية للعدد المركب، والتوسعة ذات الحدين وتطبيقاتها",
      "page_start": 45,
      "page_end": 73,
      "pdf_start": 47,
      "pdf_end": 75,
      "workbook_start": 18,
      "workbook_end": 30,
      "key_laws": [
        "[r(cos θ + i sin θ)]ⁿ = rⁿ(cos nθ + i sin nθ)",
        "zⁿ = rⁿ(cos nθ + i sin nθ)",
        "(a + b)ⁿ = Σ C(n,k)aⁿ⁻ᵏbᵏ"
      ],
      "real_world_apps": [
        "حساب القوى للإشارات الدورية",
        "توزيع الاحتمالات ذو الحدين",
        "النماذج الهندسية الدوارة"
      ]
    },
    {
      "id": "u3",
      "order": 3,
      "title": "الوحدة الثالثة: القطوع المخروطية",
      "short_desc": "القطع الناقص والقطع الزائد والقطع المكافئ ومعادلاتها القياسية وخصائصها",
      "page_start": 104,
      "page_end": 132,
      "pdf_start": 106,
      "pdf_end": 134,
      "workbook_start": 31,
      "workbook_end": 36,
      "key_laws": [
        "القطع الناقص: x²/a² + y²/b² = 1",
        "القطع الزائد: x²/a² − y²/b² = 1",
        "القطع المكافئ: y² = 4px"
      ],
      "real_world_apps": [
        "أقمار الاتصالات ومدارات الكواكب",
        "أطباق التلسكوبات والهوائيات",
        "تصميم الجسور والأنفاق"
      ]
    },
    {
      "id": "u4",
      "order": 4,
      "title": "الوحدة الرابعة: الهندسة في فضاء ثلاثي الأبعاد",
      "short_desc": "المستقيمات والمستويات، المسافات، والزوايا في الفراغ ثلاثي الأبعاد",
      "page_start": 133,
      "page_end": 153,
      "pdf_start": 135,
      "pdf_end": 155,
      "workbook_start": 37,
      "workbook_end": 44,
      "key_laws": [
        "مسافة نقطة من مستوى: |Ax₀ + By₀ + Cz₀ + D| / √(A²+B²+C²)",
        "cos φ = |n₁·n₂| / (|n₁||n₂|)",
        "طول القطر الفراغي لمكعب: d = a√3"
      ],
      "real_world_apps": [
        "تحديد اتجاه الطائرات والسفن",
        "هندسة المباني والرافعات",
        "نمذجة الكاميرات والرسوم ثلاثية الأبعاد"
      ]
    },
    {
      "id": "u5",
      "order": 5,
      "title": "الوحدة الخامسة: الاحتمالات",
      "short_desc": "التجارب العشوائية، قواعد الجمع والضرب، الاحتمال الشرطي، والتوزيع ذو الحدين",
      "page_start": 74,
      "page_end": 103,
      "pdf_start": 76,
      "pdf_end": 105,
      "workbook_start": 45,
      "workbook_end": 52,
      "key_laws": [
        "P(A∪B) = P(A) + P(B) − P(A∩B)",
        "P(A|B) = P(A∩B) / P(B)",
        "P(X=k) = C(n,k)pᵏ(1−p)ⁿ⁻ᵏ"
      ],
      "real_world_apps": [
        "تقييم المخاطر في التأمين",
        "تحليل نتائج التجارب والاستطلاعات",
        "نمذجة جودة التصنيع"
      ]
    },
    {
      "id": "u6",
      "order": 6,
      "title": "الوحدة السادسة: المشتقات",
      "short_desc": "مفهوم المشتقة، قواعد الاشتقاق، مشتقة الدوال المركبة، القيم القصوى ونظرية القيمة المتوسطة",
      "page_start": 154,
      "page_end": 209,
      "pdf_start": 156,
      "pdf_end": 211,
      "workbook_start": 53,
      "workbook_end": 67,
      "key_laws": [
        "f′(x) = limₕ→₀ [f(x+h) − f(x)] / h",
        "(xⁿ)′ = nxⁿ⁻¹",
        "(f∘g)′(x) = f′(g(x))g′(x)"
      ],
      "real_world_apps": [
        "السرعة والتسارع في الفيزياء",
        "تحسين الربح والتكلفة في الاقتصاد",
        "ميول المنحنيات في التصميم"
      ]
    },
    {
      "id": "u7",
      "order": 7,
      "title": "الوحدة السابعة: التكامل",
      "short_desc": "التكامل غير المحدد والمحدد، طرق التكامل، المساحات، وحجوم الدوران",
      "page_start": 210,
      "page_end": 256,
      "pdf_start": 212,
      "pdf_end": 258,
      "workbook_start": 68,
      "workbook_end": 80,
      "key_laws": [
        "∫xⁿdx = xⁿ⁺¹/(n+1) + C، n ≠ −1",
        "∫ₐᵇ f(x)dx = F(b) − F(a)",
        "V = π∫ₐᵇ [f(x)]²dx"
      ],
      "real_world_apps": [
        "حساب المساحات غير المنتظمة",
        "حجوم الخزانات والأوعية الدوارة",
        "الشغل والطاقة في الفيزياء"
      ]
    }
  ],
  "pages": [
    {
      "page_id": "math12-p007",
      "book_page": 7,
      "pdf_page": 9,
      "type": "lesson",
      "title": "الرياضيات — ص 7",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_009_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_009.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p008",
      "book_page": 8,
      "pdf_page": 10,
      "type": "lesson",
      "title": "الرياضيات — ص 8",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_010_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_010.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p009",
      "book_page": 9,
      "pdf_page": 11,
      "type": "lesson",
      "title": "الرياضيات — ص 9",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_011_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_011.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p010",
      "book_page": 10,
      "pdf_page": 12,
      "type": "lesson",
      "title": "الرياضيات — ص 10",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_012_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_012.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p011",
      "book_page": 11,
      "pdf_page": 13,
      "type": "lesson",
      "title": "الرياضيات — ص 11",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_013_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_013.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p012",
      "book_page": 12,
      "pdf_page": 14,
      "type": "lesson",
      "title": "الرياضيات — ص 12",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_014_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_014.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p013",
      "book_page": 13,
      "pdf_page": 15,
      "type": "lesson",
      "title": "الرياضيات — ص 13",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_015_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_015.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p014",
      "book_page": 14,
      "pdf_page": 16,
      "type": "lesson",
      "title": "الرياضيات — ص 14",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_016_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_016.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p015",
      "book_page": 15,
      "pdf_page": 17,
      "type": "lesson",
      "title": "الرياضيات — ص 15",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_017_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_017.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p016",
      "book_page": 16,
      "pdf_page": 18,
      "type": "lesson",
      "title": "الرياضيات — ص 16",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_018_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_018.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p017",
      "book_page": 17,
      "pdf_page": 19,
      "type": "lesson",
      "title": "الرياضيات — ص 17",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_019_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_019.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p018",
      "book_page": 18,
      "pdf_page": 20,
      "type": "lesson",
      "title": "الرياضيات — ص 18",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_020_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_020.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p019",
      "book_page": 19,
      "pdf_page": 21,
      "type": "lesson",
      "title": "الرياضيات — ص 19",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_021_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_021.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p020",
      "book_page": 20,
      "pdf_page": 22,
      "type": "lesson",
      "title": "الرياضيات — ص 20",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_022_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_022.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p021",
      "book_page": 21,
      "pdf_page": 23,
      "type": "lesson",
      "title": "الرياضيات — ص 21",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_023_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_023.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p022",
      "book_page": 22,
      "pdf_page": 24,
      "type": "lesson",
      "title": "الرياضيات — ص 22",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_024_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_024.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p023",
      "book_page": 23,
      "pdf_page": 25,
      "type": "lesson",
      "title": "الرياضيات — ص 23",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_025_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_025.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p024",
      "book_page": 24,
      "pdf_page": 26,
      "type": "lesson",
      "title": "الرياضيات — ص 24",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_026_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_026.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p025",
      "book_page": 25,
      "pdf_page": 27,
      "type": "lesson",
      "title": "الرياضيات — ص 25",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_027_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_027.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p026",
      "book_page": 26,
      "pdf_page": 28,
      "type": "lesson",
      "title": "الرياضيات — ص 26",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_028_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_028.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p027",
      "book_page": 27,
      "pdf_page": 29,
      "type": "lesson",
      "title": "الرياضيات — ص 27",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_029_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_029.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p028",
      "book_page": 28,
      "pdf_page": 30,
      "type": "lesson",
      "title": "الرياضيات — ص 28",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_030_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_030.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p029",
      "book_page": 29,
      "pdf_page": 31,
      "type": "lesson",
      "title": "الرياضيات — ص 29",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_031_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_031.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p030",
      "book_page": 30,
      "pdf_page": 32,
      "type": "lesson",
      "title": "الرياضيات — ص 30",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_032_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_032.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p031",
      "book_page": 31,
      "pdf_page": 33,
      "type": "lesson",
      "title": "الرياضيات — ص 31",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_033_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_033.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p032",
      "book_page": 32,
      "pdf_page": 34,
      "type": "lesson",
      "title": "الرياضيات — ص 32",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_034_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_034.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p033",
      "book_page": 33,
      "pdf_page": 35,
      "type": "lesson",
      "title": "الرياضيات — ص 33",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_035_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_035.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p034",
      "book_page": 34,
      "pdf_page": 36,
      "type": "lesson",
      "title": "الرياضيات — ص 34",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_036_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_036.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p035",
      "book_page": 35,
      "pdf_page": 37,
      "type": "lesson",
      "title": "الرياضيات — ص 35",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_037_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_037.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p036",
      "book_page": 36,
      "pdf_page": 38,
      "type": "lesson",
      "title": "الرياضيات — ص 36",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_038_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_038.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p037",
      "book_page": 37,
      "pdf_page": 39,
      "type": "lesson",
      "title": "الرياضيات — ص 37",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_039_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_039.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p038",
      "book_page": 38,
      "pdf_page": 40,
      "type": "lesson",
      "title": "الرياضيات — ص 38",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_040_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_040.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p039",
      "book_page": 39,
      "pdf_page": 41,
      "type": "lesson",
      "title": "الرياضيات — ص 39",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_041_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_041.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p040",
      "book_page": 40,
      "pdf_page": 42,
      "type": "lesson",
      "title": "الرياضيات — ص 40",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_042_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_042.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p041",
      "book_page": 41,
      "pdf_page": 43,
      "type": "lesson",
      "title": "الرياضيات — ص 41",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_043_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_043.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p042",
      "book_page": 42,
      "pdf_page": 44,
      "type": "lesson",
      "title": "الرياضيات — ص 42",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_044_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_044.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p043",
      "book_page": 43,
      "pdf_page": 45,
      "type": "lesson",
      "title": "الرياضيات — ص 43",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_045_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_045.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p044",
      "book_page": 44,
      "pdf_page": 46,
      "type": "lesson",
      "title": "الرياضيات — ص 44",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/math/pages/page_046_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_046.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p045",
      "book_page": 45,
      "pdf_page": 47,
      "type": "lesson",
      "title": "الرياضيات — ص 45",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_047_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_047.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p046",
      "book_page": 46,
      "pdf_page": 48,
      "type": "lesson",
      "title": "الرياضيات — ص 46",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_048_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_048.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p047",
      "book_page": 47,
      "pdf_page": 49,
      "type": "lesson",
      "title": "الرياضيات — ص 47",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_049_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_049.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p048",
      "book_page": 48,
      "pdf_page": 50,
      "type": "lesson",
      "title": "الرياضيات — ص 48",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_050_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_050.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p049",
      "book_page": 49,
      "pdf_page": 51,
      "type": "lesson",
      "title": "الرياضيات — ص 49",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_051_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_051.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p050",
      "book_page": 50,
      "pdf_page": 52,
      "type": "lesson",
      "title": "الرياضيات — ص 50",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_052_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_052.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p051",
      "book_page": 51,
      "pdf_page": 53,
      "type": "lesson",
      "title": "الرياضيات — ص 51",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_053_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_053.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p052",
      "book_page": 52,
      "pdf_page": 54,
      "type": "lesson",
      "title": "الرياضيات — ص 52",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_054_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_054.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p053",
      "book_page": 53,
      "pdf_page": 55,
      "type": "lesson",
      "title": "الرياضيات — ص 53",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_055_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_055.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p054",
      "book_page": 54,
      "pdf_page": 56,
      "type": "lesson",
      "title": "الرياضيات — ص 54",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_056_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_056.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p055",
      "book_page": 55,
      "pdf_page": 57,
      "type": "lesson",
      "title": "الرياضيات — ص 55",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_057_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_057.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p056",
      "book_page": 56,
      "pdf_page": 58,
      "type": "lesson",
      "title": "الرياضيات — ص 56",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_058_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_058.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p057",
      "book_page": 57,
      "pdf_page": 59,
      "type": "lesson",
      "title": "الرياضيات — ص 57",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_059_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_059.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p058",
      "book_page": 58,
      "pdf_page": 60,
      "type": "lesson",
      "title": "الرياضيات — ص 58",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_060_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_060.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p059",
      "book_page": 59,
      "pdf_page": 61,
      "type": "lesson",
      "title": "الرياضيات — ص 59",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_061_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_061.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p060",
      "book_page": 60,
      "pdf_page": 62,
      "type": "lesson",
      "title": "الرياضيات — ص 60",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_062_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_062.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p061",
      "book_page": 61,
      "pdf_page": 63,
      "type": "lesson",
      "title": "الرياضيات — ص 61",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_063_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_063.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p062",
      "book_page": 62,
      "pdf_page": 64,
      "type": "lesson",
      "title": "الرياضيات — ص 62",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_064_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_064.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p063",
      "book_page": 63,
      "pdf_page": 65,
      "type": "lesson",
      "title": "الرياضيات — ص 63",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_065_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_065.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p064",
      "book_page": 64,
      "pdf_page": 66,
      "type": "lesson",
      "title": "الرياضيات — ص 64",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_066_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_066.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p065",
      "book_page": 65,
      "pdf_page": 67,
      "type": "lesson",
      "title": "الرياضيات — ص 65",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_067_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_067.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p066",
      "book_page": 66,
      "pdf_page": 68,
      "type": "lesson",
      "title": "الرياضيات — ص 66",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_068_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_068.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p067",
      "book_page": 67,
      "pdf_page": 69,
      "type": "lesson",
      "title": "الرياضيات — ص 67",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_069_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_069.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p068",
      "book_page": 68,
      "pdf_page": 70,
      "type": "lesson",
      "title": "الرياضيات — ص 68",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_070_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_070.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p069",
      "book_page": 69,
      "pdf_page": 71,
      "type": "lesson",
      "title": "الرياضيات — ص 69",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_071_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_071.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p070",
      "book_page": 70,
      "pdf_page": 72,
      "type": "lesson",
      "title": "الرياضيات — ص 70",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_072_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_072.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p071",
      "book_page": 71,
      "pdf_page": 73,
      "type": "lesson",
      "title": "الرياضيات — ص 71",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_073_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_073.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p072",
      "book_page": 72,
      "pdf_page": 74,
      "type": "lesson",
      "title": "الرياضيات — ص 72",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_074_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_074.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p073",
      "book_page": 73,
      "pdf_page": 75,
      "type": "lesson",
      "title": "الرياضيات — ص 73",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/math/pages/page_075_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_075.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p074",
      "book_page": 74,
      "pdf_page": 76,
      "type": "lesson",
      "title": "الرياضيات — ص 74",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_076_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_076.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p075",
      "book_page": 75,
      "pdf_page": 77,
      "type": "lesson",
      "title": "الرياضيات — ص 75",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_077_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_077.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p076",
      "book_page": 76,
      "pdf_page": 78,
      "type": "lesson",
      "title": "الرياضيات — ص 76",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_078_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_078.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p077",
      "book_page": 77,
      "pdf_page": 79,
      "type": "lesson",
      "title": "الرياضيات — ص 77",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_079_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_079.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p078",
      "book_page": 78,
      "pdf_page": 80,
      "type": "lesson",
      "title": "الرياضيات — ص 78",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_080_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_080.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p079",
      "book_page": 79,
      "pdf_page": 81,
      "type": "lesson",
      "title": "الرياضيات — ص 79",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_081_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_081.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p080",
      "book_page": 80,
      "pdf_page": 82,
      "type": "lesson",
      "title": "الرياضيات — ص 80",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_082_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_082.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p081",
      "book_page": 81,
      "pdf_page": 83,
      "type": "lesson",
      "title": "الرياضيات — ص 81",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_083_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_083.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p082",
      "book_page": 82,
      "pdf_page": 84,
      "type": "lesson",
      "title": "الرياضيات — ص 82",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_084_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_084.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p083",
      "book_page": 83,
      "pdf_page": 85,
      "type": "lesson",
      "title": "الرياضيات — ص 83",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_085_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_085.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p084",
      "book_page": 84,
      "pdf_page": 86,
      "type": "lesson",
      "title": "الرياضيات — ص 84",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_086_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_086.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p085",
      "book_page": 85,
      "pdf_page": 87,
      "type": "lesson",
      "title": "الرياضيات — ص 85",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_087_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_087.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p086",
      "book_page": 86,
      "pdf_page": 88,
      "type": "lesson",
      "title": "الرياضيات — ص 86",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_088_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_088.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p087",
      "book_page": 87,
      "pdf_page": 89,
      "type": "lesson",
      "title": "الرياضيات — ص 87",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_089_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_089.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p088",
      "book_page": 88,
      "pdf_page": 90,
      "type": "lesson",
      "title": "الرياضيات — ص 88",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_090_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_090.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p089",
      "book_page": 89,
      "pdf_page": 91,
      "type": "lesson",
      "title": "الرياضيات — ص 89",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_091_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_091.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p090",
      "book_page": 90,
      "pdf_page": 92,
      "type": "lesson",
      "title": "الرياضيات — ص 90",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_092_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_092.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p091",
      "book_page": 91,
      "pdf_page": 93,
      "type": "lesson",
      "title": "الرياضيات — ص 91",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_093_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_093.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p092",
      "book_page": 92,
      "pdf_page": 94,
      "type": "lesson",
      "title": "الرياضيات — ص 92",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_094_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_094.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p093",
      "book_page": 93,
      "pdf_page": 95,
      "type": "lesson",
      "title": "الرياضيات — ص 93",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_095_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_095.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p094",
      "book_page": 94,
      "pdf_page": 96,
      "type": "lesson",
      "title": "الرياضيات — ص 94",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_096_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_096.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p095",
      "book_page": 95,
      "pdf_page": 97,
      "type": "lesson",
      "title": "الرياضيات — ص 95",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_097_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_097.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p096",
      "book_page": 96,
      "pdf_page": 98,
      "type": "lesson",
      "title": "الرياضيات — ص 96",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_098_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_098.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p097",
      "book_page": 97,
      "pdf_page": 99,
      "type": "lesson",
      "title": "الرياضيات — ص 97",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_099_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_099.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p098",
      "book_page": 98,
      "pdf_page": 100,
      "type": "lesson",
      "title": "الرياضيات — ص 98",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_100_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_100.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p099",
      "book_page": 99,
      "pdf_page": 101,
      "type": "lesson",
      "title": "الرياضيات — ص 99",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_101_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_101.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p100",
      "book_page": 100,
      "pdf_page": 102,
      "type": "lesson",
      "title": "الرياضيات — ص 100",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_102_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_102.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p101",
      "book_page": 101,
      "pdf_page": 103,
      "type": "lesson",
      "title": "الرياضيات — ص 101",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_103_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_103.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p102",
      "book_page": 102,
      "pdf_page": 104,
      "type": "lesson",
      "title": "الرياضيات — ص 102",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_104_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_104.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p103",
      "book_page": 103,
      "pdf_page": 105,
      "type": "lesson",
      "title": "الرياضيات — ص 103",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/math/pages/page_105_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_105.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p104",
      "book_page": 104,
      "pdf_page": 106,
      "type": "lesson",
      "title": "الرياضيات — ص 104",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_106_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_106.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p105",
      "book_page": 105,
      "pdf_page": 107,
      "type": "lesson",
      "title": "الرياضيات — ص 105",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_107_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_107.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p106",
      "book_page": 106,
      "pdf_page": 108,
      "type": "lesson",
      "title": "الرياضيات — ص 106",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_108_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_108.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p107",
      "book_page": 107,
      "pdf_page": 109,
      "type": "lesson",
      "title": "الرياضيات — ص 107",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_109_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_109.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p108",
      "book_page": 108,
      "pdf_page": 110,
      "type": "lesson",
      "title": "الرياضيات — ص 108",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_110_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_110.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p109",
      "book_page": 109,
      "pdf_page": 111,
      "type": "lesson",
      "title": "الرياضيات — ص 109",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_111_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_111.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p110",
      "book_page": 110,
      "pdf_page": 112,
      "type": "lesson",
      "title": "الرياضيات — ص 110",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_112_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_112.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p111",
      "book_page": 111,
      "pdf_page": 113,
      "type": "lesson",
      "title": "الرياضيات — ص 111",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_113_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_113.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p112",
      "book_page": 112,
      "pdf_page": 114,
      "type": "lesson",
      "title": "الرياضيات — ص 112",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_114_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_114.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p113",
      "book_page": 113,
      "pdf_page": 115,
      "type": "lesson",
      "title": "الرياضيات — ص 113",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_115_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_115.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p114",
      "book_page": 114,
      "pdf_page": 116,
      "type": "lesson",
      "title": "الرياضيات — ص 114",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_116_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_116.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p115",
      "book_page": 115,
      "pdf_page": 117,
      "type": "lesson",
      "title": "الرياضيات — ص 115",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_117_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_117.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p116",
      "book_page": 116,
      "pdf_page": 118,
      "type": "lesson",
      "title": "الرياضيات — ص 116",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_118_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_118.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p117",
      "book_page": 117,
      "pdf_page": 119,
      "type": "lesson",
      "title": "الرياضيات — ص 117",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_119_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_119.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p118",
      "book_page": 118,
      "pdf_page": 120,
      "type": "lesson",
      "title": "الرياضيات — ص 118",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_120_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_120.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p119",
      "book_page": 119,
      "pdf_page": 121,
      "type": "lesson",
      "title": "الرياضيات — ص 119",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_121_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_121.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p120",
      "book_page": 120,
      "pdf_page": 122,
      "type": "lesson",
      "title": "الرياضيات — ص 120",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_122_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_122.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p121",
      "book_page": 121,
      "pdf_page": 123,
      "type": "lesson",
      "title": "الرياضيات — ص 121",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_123_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_123.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p122",
      "book_page": 122,
      "pdf_page": 124,
      "type": "lesson",
      "title": "الرياضيات — ص 122",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_124_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_124.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p123",
      "book_page": 123,
      "pdf_page": 125,
      "type": "lesson",
      "title": "الرياضيات — ص 123",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_125_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_125.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p124",
      "book_page": 124,
      "pdf_page": 126,
      "type": "lesson",
      "title": "الرياضيات — ص 124",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_126_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_126.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p125",
      "book_page": 125,
      "pdf_page": 127,
      "type": "lesson",
      "title": "الرياضيات — ص 125",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_127_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_127.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p126",
      "book_page": 126,
      "pdf_page": 128,
      "type": "lesson",
      "title": "الرياضيات — ص 126",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_128_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_128.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p127",
      "book_page": 127,
      "pdf_page": 129,
      "type": "lesson",
      "title": "الرياضيات — ص 127",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_129_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_129.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p128",
      "book_page": 128,
      "pdf_page": 130,
      "type": "lesson",
      "title": "الرياضيات — ص 128",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_130_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_130.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p129",
      "book_page": 129,
      "pdf_page": 131,
      "type": "lesson",
      "title": "الرياضيات — ص 129",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_131_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_131.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p130",
      "book_page": 130,
      "pdf_page": 132,
      "type": "lesson",
      "title": "الرياضيات — ص 130",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_132_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_132.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p131",
      "book_page": 131,
      "pdf_page": 133,
      "type": "lesson",
      "title": "الرياضيات — ص 131",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_133_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_133.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p132",
      "book_page": 132,
      "pdf_page": 134,
      "type": "lesson",
      "title": "الرياضيات — ص 132",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/math/pages/page_134_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_134.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p133",
      "book_page": 133,
      "pdf_page": 135,
      "type": "lesson",
      "title": "الرياضيات — ص 133",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_135_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_135.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p134",
      "book_page": 134,
      "pdf_page": 136,
      "type": "lesson",
      "title": "الرياضيات — ص 134",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_136_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_136.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p135",
      "book_page": 135,
      "pdf_page": 137,
      "type": "lesson",
      "title": "الرياضيات — ص 135",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_137_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_137.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p136",
      "book_page": 136,
      "pdf_page": 138,
      "type": "lesson",
      "title": "الرياضيات — ص 136",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_138_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_138.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p137",
      "book_page": 137,
      "pdf_page": 139,
      "type": "lesson",
      "title": "الرياضيات — ص 137",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_139_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_139.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p138",
      "book_page": 138,
      "pdf_page": 140,
      "type": "lesson",
      "title": "الرياضيات — ص 138",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_140_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_140.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p139",
      "book_page": 139,
      "pdf_page": 141,
      "type": "lesson",
      "title": "الرياضيات — ص 139",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_141_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_141.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p140",
      "book_page": 140,
      "pdf_page": 142,
      "type": "lesson",
      "title": "الرياضيات — ص 140",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_142_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_142.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p141",
      "book_page": 141,
      "pdf_page": 143,
      "type": "lesson",
      "title": "الرياضيات — ص 141",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_143_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_143.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p142",
      "book_page": 142,
      "pdf_page": 144,
      "type": "lesson",
      "title": "الرياضيات — ص 142",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_144_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_144.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p143",
      "book_page": 143,
      "pdf_page": 145,
      "type": "lesson",
      "title": "الرياضيات — ص 143",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_145_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_145.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p144",
      "book_page": 144,
      "pdf_page": 146,
      "type": "lesson",
      "title": "الرياضيات — ص 144",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_146_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_146.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p145",
      "book_page": 145,
      "pdf_page": 147,
      "type": "lesson",
      "title": "الرياضيات — ص 145",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_147_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_147.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p146",
      "book_page": 146,
      "pdf_page": 148,
      "type": "lesson",
      "title": "الرياضيات — ص 146",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_148_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_148.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p147",
      "book_page": 147,
      "pdf_page": 149,
      "type": "lesson",
      "title": "الرياضيات — ص 147",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_149_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_149.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p148",
      "book_page": 148,
      "pdf_page": 150,
      "type": "lesson",
      "title": "الرياضيات — ص 148",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_150_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_150.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p149",
      "book_page": 149,
      "pdf_page": 151,
      "type": "lesson",
      "title": "الرياضيات — ص 149",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_151_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_151.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p150",
      "book_page": 150,
      "pdf_page": 152,
      "type": "lesson",
      "title": "الرياضيات — ص 150",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_152_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_152.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p151",
      "book_page": 151,
      "pdf_page": 153,
      "type": "lesson",
      "title": "الرياضيات — ص 151",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_153_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_153.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p152",
      "book_page": 152,
      "pdf_page": 154,
      "type": "lesson",
      "title": "الرياضيات — ص 152",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_154_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_154.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p153",
      "book_page": 153,
      "pdf_page": 155,
      "type": "lesson",
      "title": "الرياضيات — ص 153",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/math/pages/page_155_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_155.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p154",
      "book_page": 154,
      "pdf_page": 156,
      "type": "lesson",
      "title": "الرياضيات — ص 154",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_156_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_156.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p155",
      "book_page": 155,
      "pdf_page": 157,
      "type": "lesson",
      "title": "الرياضيات — ص 155",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_157_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_157.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p156",
      "book_page": 156,
      "pdf_page": 158,
      "type": "lesson",
      "title": "الرياضيات — ص 156",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_158_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_158.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p157",
      "book_page": 157,
      "pdf_page": 159,
      "type": "lesson",
      "title": "الرياضيات — ص 157",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_159_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_159.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p158",
      "book_page": 158,
      "pdf_page": 160,
      "type": "lesson",
      "title": "الرياضيات — ص 158",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_160_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_160.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p159",
      "book_page": 159,
      "pdf_page": 161,
      "type": "lesson",
      "title": "الرياضيات — ص 159",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_161_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_161.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p160",
      "book_page": 160,
      "pdf_page": 162,
      "type": "lesson",
      "title": "الرياضيات — ص 160",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_162_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_162.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p161",
      "book_page": 161,
      "pdf_page": 163,
      "type": "lesson",
      "title": "الرياضيات — ص 161",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_163_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_163.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p162",
      "book_page": 162,
      "pdf_page": 164,
      "type": "lesson",
      "title": "الرياضيات — ص 162",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_164_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_164.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p163",
      "book_page": 163,
      "pdf_page": 165,
      "type": "lesson",
      "title": "الرياضيات — ص 163",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_165_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_165.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p164",
      "book_page": 164,
      "pdf_page": 166,
      "type": "lesson",
      "title": "الرياضيات — ص 164",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_166_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_166.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p165",
      "book_page": 165,
      "pdf_page": 167,
      "type": "lesson",
      "title": "الرياضيات — ص 165",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_167_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_167.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p166",
      "book_page": 166,
      "pdf_page": 168,
      "type": "lesson",
      "title": "الرياضيات — ص 166",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_168_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_168.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p167",
      "book_page": 167,
      "pdf_page": 169,
      "type": "lesson",
      "title": "الرياضيات — ص 167",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_169_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_169.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p168",
      "book_page": 168,
      "pdf_page": 170,
      "type": "lesson",
      "title": "الرياضيات — ص 168",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_170_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_170.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p169",
      "book_page": 169,
      "pdf_page": 171,
      "type": "lesson",
      "title": "الرياضيات — ص 169",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_171_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_171.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p170",
      "book_page": 170,
      "pdf_page": 172,
      "type": "lesson",
      "title": "الرياضيات — ص 170",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_172_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_172.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p171",
      "book_page": 171,
      "pdf_page": 173,
      "type": "lesson",
      "title": "الرياضيات — ص 171",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_173_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_173.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p172",
      "book_page": 172,
      "pdf_page": 174,
      "type": "lesson",
      "title": "الرياضيات — ص 172",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_174_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_174.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p173",
      "book_page": 173,
      "pdf_page": 175,
      "type": "lesson",
      "title": "الرياضيات — ص 173",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_175_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_175.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p174",
      "book_page": 174,
      "pdf_page": 176,
      "type": "lesson",
      "title": "الرياضيات — ص 174",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_176_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_176.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p175",
      "book_page": 175,
      "pdf_page": 177,
      "type": "lesson",
      "title": "الرياضيات — ص 175",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_177_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_177.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p176",
      "book_page": 176,
      "pdf_page": 178,
      "type": "lesson",
      "title": "الرياضيات — ص 176",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_178_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_178.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p177",
      "book_page": 177,
      "pdf_page": 179,
      "type": "lesson",
      "title": "الرياضيات — ص 177",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_179_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_179.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p178",
      "book_page": 178,
      "pdf_page": 180,
      "type": "lesson",
      "title": "الرياضيات — ص 178",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_180_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_180.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p179",
      "book_page": 179,
      "pdf_page": 181,
      "type": "lesson",
      "title": "الرياضيات — ص 179",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_181_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_181.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p180",
      "book_page": 180,
      "pdf_page": 182,
      "type": "lesson",
      "title": "الرياضيات — ص 180",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_182_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_182.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p181",
      "book_page": 181,
      "pdf_page": 183,
      "type": "lesson",
      "title": "الرياضيات — ص 181",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_183_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_183.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p182",
      "book_page": 182,
      "pdf_page": 184,
      "type": "lesson",
      "title": "الرياضيات — ص 182",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_184_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_184.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p183",
      "book_page": 183,
      "pdf_page": 185,
      "type": "lesson",
      "title": "الرياضيات — ص 183",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_185_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_185.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p184",
      "book_page": 184,
      "pdf_page": 186,
      "type": "lesson",
      "title": "الرياضيات — ص 184",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_186_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_186.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p185",
      "book_page": 185,
      "pdf_page": 187,
      "type": "lesson",
      "title": "الرياضيات — ص 185",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_187_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_187.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p186",
      "book_page": 186,
      "pdf_page": 188,
      "type": "lesson",
      "title": "الرياضيات — ص 186",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_188_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_188.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p187",
      "book_page": 187,
      "pdf_page": 189,
      "type": "lesson",
      "title": "الرياضيات — ص 187",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_189_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_189.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p188",
      "book_page": 188,
      "pdf_page": 190,
      "type": "lesson",
      "title": "الرياضيات — ص 188",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_190_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_190.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p189",
      "book_page": 189,
      "pdf_page": 191,
      "type": "lesson",
      "title": "الرياضيات — ص 189",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_191_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_191.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p190",
      "book_page": 190,
      "pdf_page": 192,
      "type": "lesson",
      "title": "الرياضيات — ص 190",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_192_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_192.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p191",
      "book_page": 191,
      "pdf_page": 193,
      "type": "lesson",
      "title": "الرياضيات — ص 191",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_193_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_193.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p192",
      "book_page": 192,
      "pdf_page": 194,
      "type": "lesson",
      "title": "الرياضيات — ص 192",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_194_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_194.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p193",
      "book_page": 193,
      "pdf_page": 195,
      "type": "lesson",
      "title": "الرياضيات — ص 193",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_195_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_195.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p194",
      "book_page": 194,
      "pdf_page": 196,
      "type": "lesson",
      "title": "الرياضيات — ص 194",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_196_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_196.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p195",
      "book_page": 195,
      "pdf_page": 197,
      "type": "lesson",
      "title": "الرياضيات — ص 195",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_197_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_197.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p196",
      "book_page": 196,
      "pdf_page": 198,
      "type": "lesson",
      "title": "الرياضيات — ص 196",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_198_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_198.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p197",
      "book_page": 197,
      "pdf_page": 199,
      "type": "lesson",
      "title": "الرياضيات — ص 197",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_199_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_199.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p198",
      "book_page": 198,
      "pdf_page": 200,
      "type": "lesson",
      "title": "الرياضيات — ص 198",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_200_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_200.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p199",
      "book_page": 199,
      "pdf_page": 201,
      "type": "lesson",
      "title": "الرياضيات — ص 199",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_201_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_201.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p200",
      "book_page": 200,
      "pdf_page": 202,
      "type": "lesson",
      "title": "الرياضيات — ص 200",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_202_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_202.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p201",
      "book_page": 201,
      "pdf_page": 203,
      "type": "lesson",
      "title": "الرياضيات — ص 201",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_203_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_203.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p202",
      "book_page": 202,
      "pdf_page": 204,
      "type": "lesson",
      "title": "الرياضيات — ص 202",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_204_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_204.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p203",
      "book_page": 203,
      "pdf_page": 205,
      "type": "lesson",
      "title": "الرياضيات — ص 203",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_205_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_205.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p204",
      "book_page": 204,
      "pdf_page": 206,
      "type": "lesson",
      "title": "الرياضيات — ص 204",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_206_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_206.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p205",
      "book_page": 205,
      "pdf_page": 207,
      "type": "lesson",
      "title": "الرياضيات — ص 205",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_207_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_207.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p206",
      "book_page": 206,
      "pdf_page": 208,
      "type": "lesson",
      "title": "الرياضيات — ص 206",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_208_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_208.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p207",
      "book_page": 207,
      "pdf_page": 209,
      "type": "lesson",
      "title": "الرياضيات — ص 207",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_209_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_209.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p208",
      "book_page": 208,
      "pdf_page": 210,
      "type": "lesson",
      "title": "الرياضيات — ص 208",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_210_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_210.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p209",
      "book_page": 209,
      "pdf_page": 211,
      "type": "lesson",
      "title": "الرياضيات — ص 209",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/math/pages/page_211_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_211.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p210",
      "book_page": 210,
      "pdf_page": 212,
      "type": "lesson",
      "title": "الرياضيات — ص 210",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_212_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_212.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p211",
      "book_page": 211,
      "pdf_page": 213,
      "type": "lesson",
      "title": "الرياضيات — ص 211",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_213_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_213.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p212",
      "book_page": 212,
      "pdf_page": 214,
      "type": "lesson",
      "title": "الرياضيات — ص 212",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_214_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_214.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p213",
      "book_page": 213,
      "pdf_page": 215,
      "type": "lesson",
      "title": "الرياضيات — ص 213",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_215_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_215.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p214",
      "book_page": 214,
      "pdf_page": 216,
      "type": "lesson",
      "title": "الرياضيات — ص 214",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_216_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_216.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p215",
      "book_page": 215,
      "pdf_page": 217,
      "type": "lesson",
      "title": "الرياضيات — ص 215",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_217_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_217.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p216",
      "book_page": 216,
      "pdf_page": 218,
      "type": "lesson",
      "title": "الرياضيات — ص 216",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_218_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_218.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p217",
      "book_page": 217,
      "pdf_page": 219,
      "type": "lesson",
      "title": "الرياضيات — ص 217",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_219_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_219.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p218",
      "book_page": 218,
      "pdf_page": 220,
      "type": "lesson",
      "title": "الرياضيات — ص 218",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_220_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_220.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p219",
      "book_page": 219,
      "pdf_page": 221,
      "type": "lesson",
      "title": "الرياضيات — ص 219",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_221_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_221.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p220",
      "book_page": 220,
      "pdf_page": 222,
      "type": "lesson",
      "title": "الرياضيات — ص 220",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_222_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_222.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p221",
      "book_page": 221,
      "pdf_page": 223,
      "type": "lesson",
      "title": "الرياضيات — ص 221",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_223_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_223.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p222",
      "book_page": 222,
      "pdf_page": 224,
      "type": "lesson",
      "title": "الرياضيات — ص 222",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_224_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_224.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p223",
      "book_page": 223,
      "pdf_page": 225,
      "type": "lesson",
      "title": "الرياضيات — ص 223",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_225_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_225.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p224",
      "book_page": 224,
      "pdf_page": 226,
      "type": "lesson",
      "title": "الرياضيات — ص 224",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_226_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_226.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p225",
      "book_page": 225,
      "pdf_page": 227,
      "type": "lesson",
      "title": "الرياضيات — ص 225",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_227_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_227.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p226",
      "book_page": 226,
      "pdf_page": 228,
      "type": "lesson",
      "title": "الرياضيات — ص 226",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_228_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_228.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p227",
      "book_page": 227,
      "pdf_page": 229,
      "type": "lesson",
      "title": "الرياضيات — ص 227",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_229_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_229.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p228",
      "book_page": 228,
      "pdf_page": 230,
      "type": "lesson",
      "title": "الرياضيات — ص 228",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_230_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_230.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p229",
      "book_page": 229,
      "pdf_page": 231,
      "type": "lesson",
      "title": "الرياضيات — ص 229",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_231_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_231.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p230",
      "book_page": 230,
      "pdf_page": 232,
      "type": "lesson",
      "title": "الرياضيات — ص 230",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_232_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_232.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p231",
      "book_page": 231,
      "pdf_page": 233,
      "type": "lesson",
      "title": "الرياضيات — ص 231",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_233_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_233.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p232",
      "book_page": 232,
      "pdf_page": 234,
      "type": "lesson",
      "title": "الرياضيات — ص 232",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_234_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_234.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p233",
      "book_page": 233,
      "pdf_page": 235,
      "type": "lesson",
      "title": "الرياضيات — ص 233",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_235_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_235.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p234",
      "book_page": 234,
      "pdf_page": 236,
      "type": "lesson",
      "title": "الرياضيات — ص 234",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_236_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_236.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p235",
      "book_page": 235,
      "pdf_page": 237,
      "type": "lesson",
      "title": "الرياضيات — ص 235",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_237_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_237.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p236",
      "book_page": 236,
      "pdf_page": 238,
      "type": "lesson",
      "title": "الرياضيات — ص 236",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_238_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_238.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p237",
      "book_page": 237,
      "pdf_page": 239,
      "type": "lesson",
      "title": "الرياضيات — ص 237",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_239_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_239.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p238",
      "book_page": 238,
      "pdf_page": 240,
      "type": "lesson",
      "title": "الرياضيات — ص 238",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_240_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_240.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p239",
      "book_page": 239,
      "pdf_page": 241,
      "type": "lesson",
      "title": "الرياضيات — ص 239",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_241_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_241.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p240",
      "book_page": 240,
      "pdf_page": 242,
      "type": "lesson",
      "title": "الرياضيات — ص 240",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_242_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_242.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p241",
      "book_page": 241,
      "pdf_page": 243,
      "type": "lesson",
      "title": "الرياضيات — ص 241",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_243_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_243.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p242",
      "book_page": 242,
      "pdf_page": 244,
      "type": "lesson",
      "title": "الرياضيات — ص 242",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_244_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_244.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p243",
      "book_page": 243,
      "pdf_page": 245,
      "type": "lesson",
      "title": "الرياضيات — ص 243",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_245_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_245.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p244",
      "book_page": 244,
      "pdf_page": 246,
      "type": "lesson",
      "title": "الرياضيات — ص 244",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_246_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_246.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p245",
      "book_page": 245,
      "pdf_page": 247,
      "type": "lesson",
      "title": "الرياضيات — ص 245",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_247_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_247.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p246",
      "book_page": 246,
      "pdf_page": 248,
      "type": "lesson",
      "title": "الرياضيات — ص 246",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_248_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_248.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p247",
      "book_page": 247,
      "pdf_page": 249,
      "type": "lesson",
      "title": "الرياضيات — ص 247",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_249_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_249.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p248",
      "book_page": 248,
      "pdf_page": 250,
      "type": "lesson",
      "title": "الرياضيات — ص 248",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_250_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_250.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p249",
      "book_page": 249,
      "pdf_page": 251,
      "type": "lesson",
      "title": "الرياضيات — ص 249",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_251_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_251.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p250",
      "book_page": 250,
      "pdf_page": 252,
      "type": "lesson",
      "title": "الرياضيات — ص 250",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_252_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_252.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p251",
      "book_page": 251,
      "pdf_page": 253,
      "type": "lesson",
      "title": "الرياضيات — ص 251",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_253_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_253.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p252",
      "book_page": 252,
      "pdf_page": 254,
      "type": "lesson",
      "title": "الرياضيات — ص 252",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_254_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_254.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p253",
      "book_page": 253,
      "pdf_page": 255,
      "type": "lesson",
      "title": "الرياضيات — ص 253",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_255_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_255.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p254",
      "book_page": 254,
      "pdf_page": 256,
      "type": "lesson",
      "title": "الرياضيات — ص 254",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_256_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_256.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p255",
      "book_page": 255,
      "pdf_page": 257,
      "type": "lesson",
      "title": "الرياضيات — ص 255",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_257_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_257.jpg",
      "aspect_ratio": 0.7078
    },
    {
      "page_id": "math12-p256",
      "book_page": 256,
      "pdf_page": 258,
      "type": "lesson",
      "title": "الرياضيات — ص 256",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/math/pages/page_258_opt.jpg",
      "image_full": "assets/curriculum/grade12/math/pages/page_258.jpg",
      "aspect_ratio": 0.7078
    }
  ],
  "workbook_pages": [
    {
      "page_id": "math12-w008",
      "book_page": 6,
      "pdf_page": 8,
      "unit_id": "u1",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_008.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_008.jpg"
    },
    {
      "page_id": "math12-w009",
      "book_page": 7,
      "pdf_page": 9,
      "unit_id": "u1",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_009.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_009.jpg"
    },
    {
      "page_id": "math12-w010",
      "book_page": 8,
      "pdf_page": 10,
      "unit_id": "u1",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_010.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_010.jpg"
    },
    {
      "page_id": "math12-w011",
      "book_page": 9,
      "pdf_page": 11,
      "unit_id": "u1",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_011.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_011.jpg"
    },
    {
      "page_id": "math12-w012",
      "book_page": 10,
      "pdf_page": 12,
      "unit_id": "u1",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_012.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_012.jpg"
    },
    {
      "page_id": "math12-w013",
      "book_page": 11,
      "pdf_page": 13,
      "unit_id": "u1",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_013.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_013.jpg"
    },
    {
      "page_id": "math12-w014",
      "book_page": 12,
      "pdf_page": 14,
      "unit_id": "u1",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_014.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_014.jpg"
    },
    {
      "page_id": "math12-w015",
      "book_page": 13,
      "pdf_page": 15,
      "unit_id": "u1",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_015.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_015.jpg"
    },
    {
      "page_id": "math12-w016",
      "book_page": 14,
      "pdf_page": 16,
      "unit_id": "u1",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_016.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_016.jpg"
    },
    {
      "page_id": "math12-w017",
      "book_page": 15,
      "pdf_page": 17,
      "unit_id": "u1",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_017.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_017.jpg"
    },
    {
      "page_id": "math12-w018",
      "book_page": 16,
      "pdf_page": 18,
      "unit_id": "u1",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_018.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_018.jpg"
    },
    {
      "page_id": "math12-w019",
      "book_page": 17,
      "pdf_page": 19,
      "unit_id": "u1",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_019.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_019.jpg"
    },
    {
      "page_id": "math12-w020",
      "book_page": 18,
      "pdf_page": 20,
      "unit_id": "u2",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_020.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_020.jpg"
    },
    {
      "page_id": "math12-w021",
      "book_page": 19,
      "pdf_page": 21,
      "unit_id": "u2",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_021.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_021.jpg"
    },
    {
      "page_id": "math12-w022",
      "book_page": 20,
      "pdf_page": 22,
      "unit_id": "u2",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_022.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_022.jpg"
    },
    {
      "page_id": "math12-w023",
      "book_page": 21,
      "pdf_page": 23,
      "unit_id": "u2",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_023.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_023.jpg"
    },
    {
      "page_id": "math12-w024",
      "book_page": 22,
      "pdf_page": 24,
      "unit_id": "u2",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_024.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_024.jpg"
    },
    {
      "page_id": "math12-w025",
      "book_page": 23,
      "pdf_page": 25,
      "unit_id": "u2",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_025.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_025.jpg"
    },
    {
      "page_id": "math12-w026",
      "book_page": 24,
      "pdf_page": 26,
      "unit_id": "u2",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_026.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_026.jpg"
    },
    {
      "page_id": "math12-w027",
      "book_page": 25,
      "pdf_page": 27,
      "unit_id": "u2",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_027.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_027.jpg"
    },
    {
      "page_id": "math12-w028",
      "book_page": 26,
      "pdf_page": 28,
      "unit_id": "u2",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_028.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_028.jpg"
    },
    {
      "page_id": "math12-w029",
      "book_page": 27,
      "pdf_page": 29,
      "unit_id": "u2",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_029.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_029.jpg"
    },
    {
      "page_id": "math12-w030",
      "book_page": 28,
      "pdf_page": 30,
      "unit_id": "u2",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_030.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_030.jpg"
    },
    {
      "page_id": "math12-w031",
      "book_page": 29,
      "pdf_page": 31,
      "unit_id": "u2",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_031.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_031.jpg"
    },
    {
      "page_id": "math12-w032",
      "book_page": 30,
      "pdf_page": 32,
      "unit_id": "u2",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_032.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_032.jpg"
    },
    {
      "page_id": "math12-w033",
      "book_page": 31,
      "pdf_page": 33,
      "unit_id": "u3",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_033.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_033.jpg"
    },
    {
      "page_id": "math12-w034",
      "book_page": 32,
      "pdf_page": 34,
      "unit_id": "u3",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_034.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_034.jpg"
    },
    {
      "page_id": "math12-w035",
      "book_page": 33,
      "pdf_page": 35,
      "unit_id": "u3",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_035.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_035.jpg"
    },
    {
      "page_id": "math12-w036",
      "book_page": 34,
      "pdf_page": 36,
      "unit_id": "u3",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_036.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_036.jpg"
    },
    {
      "page_id": "math12-w037",
      "book_page": 35,
      "pdf_page": 37,
      "unit_id": "u3",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_037.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_037.jpg"
    },
    {
      "page_id": "math12-w038",
      "book_page": 36,
      "pdf_page": 38,
      "unit_id": "u3",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_038.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_038.jpg"
    },
    {
      "page_id": "math12-w039",
      "book_page": 37,
      "pdf_page": 39,
      "unit_id": "u4",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_039.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_039.jpg"
    },
    {
      "page_id": "math12-w040",
      "book_page": 38,
      "pdf_page": 40,
      "unit_id": "u4",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_040.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_040.jpg"
    },
    {
      "page_id": "math12-w041",
      "book_page": 39,
      "pdf_page": 41,
      "unit_id": "u4",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_041.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_041.jpg"
    },
    {
      "page_id": "math12-w042",
      "book_page": 40,
      "pdf_page": 42,
      "unit_id": "u4",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_042.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_042.jpg"
    },
    {
      "page_id": "math12-w043",
      "book_page": 41,
      "pdf_page": 43,
      "unit_id": "u4",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_043.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_043.jpg"
    },
    {
      "page_id": "math12-w044",
      "book_page": 42,
      "pdf_page": 44,
      "unit_id": "u4",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_044.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_044.jpg"
    },
    {
      "page_id": "math12-w045",
      "book_page": 43,
      "pdf_page": 45,
      "unit_id": "u4",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_045.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_045.jpg"
    },
    {
      "page_id": "math12-w046",
      "book_page": 44,
      "pdf_page": 46,
      "unit_id": "u4",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_046.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_046.jpg"
    },
    {
      "page_id": "math12-w047",
      "book_page": 45,
      "pdf_page": 47,
      "unit_id": "u5",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_047.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_047.jpg"
    },
    {
      "page_id": "math12-w048",
      "book_page": 46,
      "pdf_page": 48,
      "unit_id": "u5",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_048.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_048.jpg"
    },
    {
      "page_id": "math12-w049",
      "book_page": 47,
      "pdf_page": 49,
      "unit_id": "u5",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_049.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_049.jpg"
    },
    {
      "page_id": "math12-w050",
      "book_page": 48,
      "pdf_page": 50,
      "unit_id": "u5",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_050.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_050.jpg"
    },
    {
      "page_id": "math12-w051",
      "book_page": 49,
      "pdf_page": 51,
      "unit_id": "u5",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_051.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_051.jpg"
    },
    {
      "page_id": "math12-w052",
      "book_page": 50,
      "pdf_page": 52,
      "unit_id": "u5",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_052.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_052.jpg"
    },
    {
      "page_id": "math12-w053",
      "book_page": 51,
      "pdf_page": 53,
      "unit_id": "u5",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_053.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_053.jpg"
    },
    {
      "page_id": "math12-w054",
      "book_page": 52,
      "pdf_page": 54,
      "unit_id": "u5",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_054.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_054.jpg"
    },
    {
      "page_id": "math12-w055",
      "book_page": 53,
      "pdf_page": 55,
      "unit_id": "u6",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_055.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_055.jpg"
    },
    {
      "page_id": "math12-w056",
      "book_page": 54,
      "pdf_page": 56,
      "unit_id": "u6",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_056.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_056.jpg"
    },
    {
      "page_id": "math12-w057",
      "book_page": 55,
      "pdf_page": 57,
      "unit_id": "u6",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_057.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_057.jpg"
    },
    {
      "page_id": "math12-w058",
      "book_page": 56,
      "pdf_page": 58,
      "unit_id": "u6",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_058.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_058.jpg"
    },
    {
      "page_id": "math12-w059",
      "book_page": 57,
      "pdf_page": 59,
      "unit_id": "u6",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_059.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_059.jpg"
    },
    {
      "page_id": "math12-w060",
      "book_page": 58,
      "pdf_page": 60,
      "unit_id": "u6",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_060.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_060.jpg"
    },
    {
      "page_id": "math12-w061",
      "book_page": 59,
      "pdf_page": 61,
      "unit_id": "u6",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_061.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_061.jpg"
    },
    {
      "page_id": "math12-w062",
      "book_page": 60,
      "pdf_page": 62,
      "unit_id": "u6",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_062.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_062.jpg"
    },
    {
      "page_id": "math12-w063",
      "book_page": 61,
      "pdf_page": 63,
      "unit_id": "u6",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_063.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_063.jpg"
    },
    {
      "page_id": "math12-w064",
      "book_page": 62,
      "pdf_page": 64,
      "unit_id": "u6",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_064.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_064.jpg"
    },
    {
      "page_id": "math12-w065",
      "book_page": 63,
      "pdf_page": 65,
      "unit_id": "u6",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_065.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_065.jpg"
    },
    {
      "page_id": "math12-w066",
      "book_page": 64,
      "pdf_page": 66,
      "unit_id": "u6",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_066.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_066.jpg"
    },
    {
      "page_id": "math12-w067",
      "book_page": 65,
      "pdf_page": 67,
      "unit_id": "u6",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_067.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_067.jpg"
    },
    {
      "page_id": "math12-w068",
      "book_page": 66,
      "pdf_page": 68,
      "unit_id": "u6",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_068.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_068.jpg"
    },
    {
      "page_id": "math12-w069",
      "book_page": 67,
      "pdf_page": 69,
      "unit_id": "u6",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_069.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_069.jpg"
    },
    {
      "page_id": "math12-w070",
      "book_page": 68,
      "pdf_page": 70,
      "unit_id": "u7",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_070.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_070.jpg"
    },
    {
      "page_id": "math12-w071",
      "book_page": 69,
      "pdf_page": 71,
      "unit_id": "u7",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_071.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_071.jpg"
    },
    {
      "page_id": "math12-w072",
      "book_page": 70,
      "pdf_page": 72,
      "unit_id": "u7",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_072.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_072.jpg"
    },
    {
      "page_id": "math12-w073",
      "book_page": 71,
      "pdf_page": 73,
      "unit_id": "u7",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_073.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_073.jpg"
    },
    {
      "page_id": "math12-w074",
      "book_page": 72,
      "pdf_page": 74,
      "unit_id": "u7",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_074.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_074.jpg"
    },
    {
      "page_id": "math12-w075",
      "book_page": 73,
      "pdf_page": 75,
      "unit_id": "u7",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_075.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_075.jpg"
    },
    {
      "page_id": "math12-w076",
      "book_page": 74,
      "pdf_page": 76,
      "unit_id": "u7",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_076.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_076.jpg"
    },
    {
      "page_id": "math12-w077",
      "book_page": 75,
      "pdf_page": 77,
      "unit_id": "u7",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_077.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_077.jpg"
    },
    {
      "page_id": "math12-w078",
      "book_page": 76,
      "pdf_page": 78,
      "unit_id": "u7",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_078.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_078.jpg"
    },
    {
      "page_id": "math12-w079",
      "book_page": 77,
      "pdf_page": 79,
      "unit_id": "u7",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_079.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_079.jpg"
    },
    {
      "page_id": "math12-w080",
      "book_page": 78,
      "pdf_page": 80,
      "unit_id": "u7",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_080.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_080.jpg"
    },
    {
      "page_id": "math12-w081",
      "book_page": 79,
      "pdf_page": 81,
      "unit_id": "u7",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_081.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_081.jpg"
    },
    {
      "page_id": "math12-w082",
      "book_page": 80,
      "pdf_page": 82,
      "unit_id": "u7",
      "role": "practice_only",
      "image": "assets/curriculum/grade12/math/workbook_pages/workbook_page_082.jpg",
      "image_full": "assets/curriculum/grade12/math/workbook_pages/workbook_page_082.jpg"
    }
  ],
  "lessons": [
    {
      "id": "math-u1-l1",
      "unitId": "u1",
      "order": 1,
      "title": "مفهوم العدد المركب والوحدة التخيلية",
      "pages": [
        7,
        11
      ],
      "pdf_pages": [
        9,
        13
      ]
    },
    {
      "id": "math-u1-l2",
      "unitId": "u1",
      "order": 2,
      "title": "العمليات على الأعداد المركبة",
      "pages": [
        12,
        15
      ],
      "pdf_pages": [
        14,
        17
      ]
    },
    {
      "id": "math-u1-l3",
      "unitId": "u1",
      "order": 3,
      "title": "التمثيل الهندسي والقيمة المطلقة",
      "pages": [
        16,
        22
      ],
      "pdf_pages": [
        18,
        24
      ]
    },
    {
      "id": "math-u1-l4",
      "unitId": "u1",
      "order": 4,
      "title": "سعة العدد المركب وزاويته",
      "pages": [
        23,
        32
      ],
      "pdf_pages": [
        25,
        34
      ]
    },
    {
      "id": "math-u1-l5",
      "unitId": "u1",
      "order": 5,
      "title": "الصيغة القطبية للعدد المركب",
      "pages": [
        33,
        39
      ],
      "pdf_pages": [
        35,
        41
      ]
    },
    {
      "id": "math-u1-l6",
      "unitId": "u1",
      "order": 6,
      "title": "التحويل بين الصيغتين الجبرية والقطبية",
      "pages": [
        40,
        44
      ],
      "pdf_pages": [
        42,
        46
      ]
    },
    {
      "id": "math-u2-l1",
      "unitId": "u2",
      "order": 1,
      "title": "مبرهنة دي موافر",
      "pages": [
        45,
        48
      ],
      "pdf_pages": [
        47,
        50
      ]
    },
    {
      "id": "math-u2-l2",
      "unitId": "u2",
      "order": 2,
      "title": "الجذور النونية للعدد المركب",
      "pages": [
        49,
        54
      ],
      "pdf_pages": [
        51,
        56
      ]
    },
    {
      "id": "math-u2-l3",
      "unitId": "u2",
      "order": 3,
      "title": "التوسعة ذات الحدين",
      "pages": [
        55,
        64
      ],
      "pdf_pages": [
        57,
        66
      ]
    },
    {
      "id": "math-u2-l4",
      "unitId": "u2",
      "order": 4,
      "title": "تطبيقات دي موافر والتوسعة",
      "pages": [
        65,
        73
      ],
      "pdf_pages": [
        67,
        75
      ]
    },
    {
      "id": "math-u3-l1",
      "unitId": "u3",
      "order": 1,
      "title": "التعريف العام للقطع المخروطي",
      "pages": [
        104,
        109
      ],
      "pdf_pages": [
        106,
        111
      ]
    },
    {
      "id": "math-u3-l2",
      "unitId": "u3",
      "order": 2,
      "title": "القطع الناقص",
      "pages": [
        110,
        117
      ],
      "pdf_pages": [
        112,
        119
      ]
    },
    {
      "id": "math-u3-l3",
      "unitId": "u3",
      "order": 3,
      "title": "القطع الزائد",
      "pages": [
        118,
        123
      ],
      "pdf_pages": [
        120,
        125
      ]
    },
    {
      "id": "math-u3-l4",
      "unitId": "u3",
      "order": 4,
      "title": "القطع المكافئ",
      "pages": [
        124,
        129
      ],
      "pdf_pages": [
        126,
        131
      ]
    },
    {
      "id": "math-u3-l5",
      "unitId": "u3",
      "order": 5,
      "title": "تطبيقات القطوع المخروطية",
      "pages": [
        130,
        132
      ],
      "pdf_pages": [
        132,
        134
      ]
    },
    {
      "id": "math-u4-l1",
      "unitId": "u4",
      "order": 1,
      "title": "المستقيم والمستوى في الفراغ",
      "pages": [
        133,
        141
      ],
      "pdf_pages": [
        135,
        143
      ]
    },
    {
      "id": "math-u4-l2",
      "unitId": "u4",
      "order": 2,
      "title": "الزاوية بين مستقيم ومستوى",
      "pages": [
        142,
        146
      ],
      "pdf_pages": [
        144,
        148
      ]
    },
    {
      "id": "math-u4-l3",
      "unitId": "u4",
      "order": 3,
      "title": "الزاوية بين مستويين والمسافة في الفراغ",
      "pages": [
        147,
        153
      ],
      "pdf_pages": [
        149,
        155
      ]
    },
    {
      "id": "math-u5-l1",
      "unitId": "u5",
      "order": 1,
      "title": "التجارب العشوائية والاحتمال",
      "pages": [
        74,
        78
      ],
      "pdf_pages": [
        76,
        80
      ]
    },
    {
      "id": "math-u5-l2",
      "unitId": "u5",
      "order": 2,
      "title": "قاعدتا الجمع والضرب",
      "pages": [
        79,
        85
      ],
      "pdf_pages": [
        81,
        87
      ]
    },
    {
      "id": "math-u5-l3",
      "unitId": "u5",
      "order": 3,
      "title": "الاحتمال الشرطي والاستقلال",
      "pages": [
        86,
        92
      ],
      "pdf_pages": [
        88,
        94
      ]
    },
    {
      "id": "math-u5-l4",
      "unitId": "u5",
      "order": 4,
      "title": "الاحتمال ذو الحدين",
      "pages": [
        93,
        97
      ],
      "pdf_pages": [
        95,
        99
      ]
    },
    {
      "id": "math-u5-l5",
      "unitId": "u5",
      "order": 5,
      "title": "تطبيقات الاحتمالات",
      "pages": [
        98,
        103
      ],
      "pdf_pages": [
        100,
        105
      ]
    },
    {
      "id": "math-u6-l1",
      "unitId": "u6",
      "order": 1,
      "title": "مفهوم المشتقة وميل المماس",
      "pages": [
        154,
        159
      ],
      "pdf_pages": [
        156,
        161
      ]
    },
    {
      "id": "math-u6-l2",
      "unitId": "u6",
      "order": 2,
      "title": "قواعد الاشتقاق الأساسية",
      "pages": [
        160,
        165
      ],
      "pdf_pages": [
        162,
        167
      ]
    },
    {
      "id": "math-u6-l3",
      "unitId": "u6",
      "order": 3,
      "title": "مشتقة الدالة المركبة",
      "pages": [
        166,
        170
      ],
      "pdf_pages": [
        168,
        172
      ]
    },
    {
      "id": "math-u6-l4",
      "unitId": "u6",
      "order": 4,
      "title": "اشتقاق الدوال الجبرية",
      "pages": [
        171,
        174
      ],
      "pdf_pages": [
        173,
        176
      ]
    },
    {
      "id": "math-u6-l5",
      "unitId": "u6",
      "order": 5,
      "title": "التطبيقات الهندسية للمشتقة",
      "pages": [
        175,
        182
      ],
      "pdf_pages": [
        177,
        184
      ]
    },
    {
      "id": "math-u6-l6",
      "unitId": "u6",
      "order": 6,
      "title": "المشتقات الأعلى",
      "pages": [
        183,
        186
      ],
      "pdf_pages": [
        185,
        188
      ]
    },
    {
      "id": "math-u6-l7",
      "unitId": "u6",
      "order": 7,
      "title": "القيم القصوى والتقرير",
      "pages": [
        187,
        199
      ],
      "pdf_pages": [
        189,
        201
      ]
    },
    {
      "id": "math-u6-l8",
      "unitId": "u6",
      "order": 8,
      "title": "نظريتا رول والقيمة المتوسطة",
      "pages": [
        200,
        209
      ],
      "pdf_pages": [
        202,
        211
      ]
    },
    {
      "id": "math-u7-l1",
      "unitId": "u7",
      "order": 1,
      "title": "التكامل غير المحدد",
      "pages": [
        210,
        221
      ],
      "pdf_pages": [
        212,
        223
      ]
    },
    {
      "id": "math-u7-l2",
      "unitId": "u7",
      "order": 2,
      "title": "طرق التكامل",
      "pages": [
        222,
        234
      ],
      "pdf_pages": [
        224,
        236
      ]
    },
    {
      "id": "math-u7-l3",
      "unitId": "u7",
      "order": 3,
      "title": "التكامل المحدد",
      "pages": [
        235,
        239
      ],
      "pdf_pages": [
        237,
        241
      ]
    },
    {
      "id": "math-u7-l4",
      "unitId": "u7",
      "order": 4,
      "title": "خصائص التكامل المحدد",
      "pages": [
        240,
        243
      ],
      "pdf_pages": [
        242,
        245
      ]
    },
    {
      "id": "math-u7-l5",
      "unitId": "u7",
      "order": 5,
      "title": "المساحة تحت المنحنى",
      "pages": [
        244,
        247
      ],
      "pdf_pages": [
        246,
        249
      ]
    },
    {
      "id": "math-u7-l6",
      "unitId": "u7",
      "order": 6,
      "title": "حجم مجسم الدوران",
      "pages": [
        248,
        251
      ],
      "pdf_pages": [
        250,
        253
      ]
    },
    {
      "id": "math-u7-l7",
      "unitId": "u7",
      "order": 7,
      "title": "تطبيقات التكامل",
      "pages": [
        252,
        256
      ],
      "pdf_pages": [
        254,
        258
      ]
    }
  ],
  "interactions": {
    "math12-p007": [
      {
        "id": "hs-math12-p007-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p007-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-add",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p007-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-add",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p007-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p007-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p008": [
      {
        "id": "hs-math12-p008-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p008-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-add",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p008-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-add",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p008-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p008-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p009": [
      {
        "id": "hs-math12-p009-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p009-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-add",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p009-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-add",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p009-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p009-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p010": [
      {
        "id": "hs-math12-p010-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p010-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-add",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p010-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-add",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p010-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p010-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p011": [
      {
        "id": "hs-math12-p011-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p011-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-add",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p011-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-add",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p011-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p011-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p012": [
      {
        "id": "hs-math12-p012-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p012-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-add",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p012-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-add",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p012-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p012-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p013": [
      {
        "id": "hs-math12-p013-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p013-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-add",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p013-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-add",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p013-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p013-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p014": [
      {
        "id": "hs-math12-p014-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p014-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-add",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p014-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-add",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p014-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p014-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p015": [
      {
        "id": "hs-math12-p015-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p015-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-add",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p015-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-add",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p015-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p015-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p016": [
      {
        "id": "hs-math12-p016-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p016-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p016-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p016-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p016-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p017": [
      {
        "id": "hs-math12-p017-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p017-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p017-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p017-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p017-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p018": [
      {
        "id": "hs-math12-p018-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p018-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p018-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p018-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p018-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p019": [
      {
        "id": "hs-math12-p019-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p019-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p019-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p019-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p019-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p020": [
      {
        "id": "hs-math12-p020-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p020-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p020-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p020-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p020-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p021": [
      {
        "id": "hs-math12-p021-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p021-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p021-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p021-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p021-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p022": [
      {
        "id": "hs-math12-p022-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p022-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p022-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p022-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p022-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p023": [
      {
        "id": "hs-math12-p023-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p023-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p023-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p023-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p023-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p024": [
      {
        "id": "hs-math12-p024-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p024-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p024-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p024-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p024-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p025": [
      {
        "id": "hs-math12-p025-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p025-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p025-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p025-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p025-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p026": [
      {
        "id": "hs-math12-p026-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p026-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p026-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p026-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p026-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p027": [
      {
        "id": "hs-math12-p027-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p027-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p027-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p027-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p027-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p028": [
      {
        "id": "hs-math12-p028-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p028-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p028-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p028-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p028-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p029": [
      {
        "id": "hs-math12-p029-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p029-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p029-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p029-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p029-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p030": [
      {
        "id": "hs-math12-p030-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p030-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p030-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p030-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p030-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p031": [
      {
        "id": "hs-math12-p031-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p031-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p031-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p031-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p031-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p032": [
      {
        "id": "hs-math12-p032-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p032-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-complex-modulus",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p032-activity",
        "type": "activity",
        "activity_ref": "act-math-complex-modulus",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p032-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p032-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p033": [
      {
        "id": "hs-math12-p033-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p033-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-polar",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p033-activity",
        "type": "activity",
        "activity_ref": "act-math-polar",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p033-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p033-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p034": [
      {
        "id": "hs-math12-p034-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p034-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-polar",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p034-activity",
        "type": "activity",
        "activity_ref": "act-math-polar",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p034-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p034-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p035": [
      {
        "id": "hs-math12-p035-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p035-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-polar",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p035-activity",
        "type": "activity",
        "activity_ref": "act-math-polar",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p035-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p035-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p036": [
      {
        "id": "hs-math12-p036-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p036-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-polar",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p036-activity",
        "type": "activity",
        "activity_ref": "act-math-polar",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p036-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p036-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p037": [
      {
        "id": "hs-math12-p037-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p037-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-polar",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p037-activity",
        "type": "activity",
        "activity_ref": "act-math-polar",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p037-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p037-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p038": [
      {
        "id": "hs-math12-p038-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p038-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-polar",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p038-activity",
        "type": "activity",
        "activity_ref": "act-math-polar",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p038-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p038-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p039": [
      {
        "id": "hs-math12-p039-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p039-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-polar",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p039-activity",
        "type": "activity",
        "activity_ref": "act-math-polar",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p039-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p039-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p040": [
      {
        "id": "hs-math12-p040-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l6",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p040-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-polar",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p040-activity",
        "type": "activity",
        "activity_ref": "act-math-polar",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p040-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p040-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p041": [
      {
        "id": "hs-math12-p041-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l6",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p041-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-polar",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p041-activity",
        "type": "activity",
        "activity_ref": "act-math-polar",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p041-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p041-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p042": [
      {
        "id": "hs-math12-p042-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l6",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p042-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-polar",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p042-activity",
        "type": "activity",
        "activity_ref": "act-math-polar",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p042-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p042-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p043": [
      {
        "id": "hs-math12-p043-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l6",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p043-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-polar",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p043-activity",
        "type": "activity",
        "activity_ref": "act-math-polar",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p043-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p043-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p044": [
      {
        "id": "hs-math12-p044-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u1-l6",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p044-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-polar",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p044-activity",
        "type": "activity",
        "activity_ref": "act-math-polar",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p044-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p044-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u1",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p045": [
      {
        "id": "hs-math12-p045-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p045-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p045-activity",
        "type": "activity",
        "activity_ref": "act-math-demoivre",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p045-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p045-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p046": [
      {
        "id": "hs-math12-p046-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p046-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p046-activity",
        "type": "activity",
        "activity_ref": "act-math-demoivre",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p046-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p046-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p047": [
      {
        "id": "hs-math12-p047-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p047-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p047-activity",
        "type": "activity",
        "activity_ref": "act-math-demoivre",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p047-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p047-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p048": [
      {
        "id": "hs-math12-p048-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p048-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p048-activity",
        "type": "activity",
        "activity_ref": "act-math-demoivre",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p048-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p048-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p049": [
      {
        "id": "hs-math12-p049-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p049-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p049-activity",
        "type": "activity",
        "activity_ref": "act-math-roots",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p049-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p049-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p050": [
      {
        "id": "hs-math12-p050-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p050-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p050-activity",
        "type": "activity",
        "activity_ref": "act-math-roots",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p050-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p050-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p051": [
      {
        "id": "hs-math12-p051-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p051-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p051-activity",
        "type": "activity",
        "activity_ref": "act-math-roots",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p051-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p051-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p052": [
      {
        "id": "hs-math12-p052-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p052-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p052-activity",
        "type": "activity",
        "activity_ref": "act-math-roots",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p052-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p052-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p053": [
      {
        "id": "hs-math12-p053-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p053-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p053-activity",
        "type": "activity",
        "activity_ref": "act-math-roots",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p053-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p053-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p054": [
      {
        "id": "hs-math12-p054-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p054-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p054-activity",
        "type": "activity",
        "activity_ref": "act-math-roots",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p054-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p054-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p055": [
      {
        "id": "hs-math12-p055-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p055-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-binomial",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p055-activity",
        "type": "activity",
        "activity_ref": "act-math-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p055-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p055-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p056": [
      {
        "id": "hs-math12-p056-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p056-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-binomial",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p056-activity",
        "type": "activity",
        "activity_ref": "act-math-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p056-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p056-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p057": [
      {
        "id": "hs-math12-p057-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p057-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-binomial",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p057-activity",
        "type": "activity",
        "activity_ref": "act-math-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p057-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p057-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p058": [
      {
        "id": "hs-math12-p058-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p058-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-binomial",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p058-activity",
        "type": "activity",
        "activity_ref": "act-math-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p058-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p058-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p059": [
      {
        "id": "hs-math12-p059-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p059-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-binomial",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p059-activity",
        "type": "activity",
        "activity_ref": "act-math-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p059-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p059-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p060": [
      {
        "id": "hs-math12-p060-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p060-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-binomial",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p060-activity",
        "type": "activity",
        "activity_ref": "act-math-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p060-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p060-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p061": [
      {
        "id": "hs-math12-p061-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p061-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-binomial",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p061-activity",
        "type": "activity",
        "activity_ref": "act-math-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p061-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p061-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p062": [
      {
        "id": "hs-math12-p062-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p062-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-binomial",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p062-activity",
        "type": "activity",
        "activity_ref": "act-math-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p062-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p062-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p063": [
      {
        "id": "hs-math12-p063-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p063-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-binomial",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p063-activity",
        "type": "activity",
        "activity_ref": "act-math-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p063-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p063-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p064": [
      {
        "id": "hs-math12-p064-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p064-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-binomial",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p064-activity",
        "type": "activity",
        "activity_ref": "act-math-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p064-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p064-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p065": [
      {
        "id": "hs-math12-p065-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p065-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p065-activity",
        "type": "activity",
        "activity_ref": "act-math-demoivre",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p065-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p065-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p066": [
      {
        "id": "hs-math12-p066-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p066-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p066-activity",
        "type": "activity",
        "activity_ref": "act-math-demoivre",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p066-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p066-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p067": [
      {
        "id": "hs-math12-p067-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p067-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p067-activity",
        "type": "activity",
        "activity_ref": "act-math-demoivre",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p067-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p067-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p068": [
      {
        "id": "hs-math12-p068-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p068-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p068-activity",
        "type": "activity",
        "activity_ref": "act-math-demoivre",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p068-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p068-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p069": [
      {
        "id": "hs-math12-p069-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p069-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p069-activity",
        "type": "activity",
        "activity_ref": "act-math-demoivre",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p069-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p069-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p070": [
      {
        "id": "hs-math12-p070-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p070-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p070-activity",
        "type": "activity",
        "activity_ref": "act-math-demoivre",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p070-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p070-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p071": [
      {
        "id": "hs-math12-p071-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p071-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p071-activity",
        "type": "activity",
        "activity_ref": "act-math-demoivre",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p071-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p071-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p072": [
      {
        "id": "hs-math12-p072-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p072-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p072-activity",
        "type": "activity",
        "activity_ref": "act-math-demoivre",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p072-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p072-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p073": [
      {
        "id": "hs-math12-p073-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u2-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p073-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-demoivre",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p073-activity",
        "type": "activity",
        "activity_ref": "act-math-demoivre",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p073-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-complex",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p073-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u2",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p074": [
      {
        "id": "hs-math12-p074-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p074-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p074-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-union",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p074-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p074-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p075": [
      {
        "id": "hs-math12-p075-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p075-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p075-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-union",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p075-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p075-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p076": [
      {
        "id": "hs-math12-p076-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p076-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p076-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-union",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p076-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p076-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p077": [
      {
        "id": "hs-math12-p077-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p077-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p077-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-union",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p077-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p077-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p078": [
      {
        "id": "hs-math12-p078-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p078-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p078-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-union",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p078-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p078-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p079": [
      {
        "id": "hs-math12-p079-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p079-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p079-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-union",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p079-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p079-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p080": [
      {
        "id": "hs-math12-p080-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p080-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p080-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-union",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p080-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p080-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p081": [
      {
        "id": "hs-math12-p081-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p081-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p081-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-union",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p081-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p081-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p082": [
      {
        "id": "hs-math12-p082-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p082-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p082-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-union",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p082-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p082-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p083": [
      {
        "id": "hs-math12-p083-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p083-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p083-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-union",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p083-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p083-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p084": [
      {
        "id": "hs-math12-p084-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p084-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p084-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-union",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p084-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p084-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p085": [
      {
        "id": "hs-math12-p085-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p085-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p085-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-union",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p085-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p085-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p086": [
      {
        "id": "hs-math12-p086-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p086-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-conditional",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p086-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-conditional",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p086-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p086-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p087": [
      {
        "id": "hs-math12-p087-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p087-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-conditional",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p087-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-conditional",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p087-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p087-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p088": [
      {
        "id": "hs-math12-p088-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p088-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-conditional",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p088-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-conditional",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p088-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p088-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p089": [
      {
        "id": "hs-math12-p089-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p089-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-conditional",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p089-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-conditional",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p089-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p089-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p090": [
      {
        "id": "hs-math12-p090-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p090-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-conditional",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p090-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-conditional",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p090-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p090-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p091": [
      {
        "id": "hs-math12-p091-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p091-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-conditional",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p091-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-conditional",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p091-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p091-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p092": [
      {
        "id": "hs-math12-p092-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p092-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-conditional",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p092-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-conditional",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p092-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p092-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p093": [
      {
        "id": "hs-math12-p093-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p093-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-binomial",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p093-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p093-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p093-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p094": [
      {
        "id": "hs-math12-p094-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p094-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-binomial",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p094-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p094-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p094-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p095": [
      {
        "id": "hs-math12-p095-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p095-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-binomial",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p095-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p095-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p095-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p096": [
      {
        "id": "hs-math12-p096-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p096-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-binomial",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p096-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p096-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p096-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p097": [
      {
        "id": "hs-math12-p097-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p097-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-binomial",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p097-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p097-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p097-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p098": [
      {
        "id": "hs-math12-p098-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p098-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p098-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p098-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p098-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p099": [
      {
        "id": "hs-math12-p099-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p099-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p099-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p099-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p099-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p100": [
      {
        "id": "hs-math12-p100-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p100-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p100-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p100-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p100-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p101": [
      {
        "id": "hs-math12-p101-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p101-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p101-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p101-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p101-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p102": [
      {
        "id": "hs-math12-p102-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p102-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p102-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p102-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p102-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p103": [
      {
        "id": "hs-math12-p103-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u5-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p103-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-prob-union",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p103-activity",
        "type": "activity",
        "activity_ref": "act-math-prob-binomial",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p103-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-probability",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p103-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u5",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p104": [
      {
        "id": "hs-math12-p104-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p104-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-ellipse",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p104-activity",
        "type": "activity",
        "activity_ref": "act-math-cone",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p104-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-cone",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p104-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p105": [
      {
        "id": "hs-math12-p105-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p105-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-ellipse",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p105-activity",
        "type": "activity",
        "activity_ref": "act-math-cone",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p105-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-cone",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p105-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p106": [
      {
        "id": "hs-math12-p106-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p106-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-ellipse",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p106-activity",
        "type": "activity",
        "activity_ref": "act-math-cone",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p106-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-cone",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p106-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p107": [
      {
        "id": "hs-math12-p107-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p107-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-ellipse",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p107-activity",
        "type": "activity",
        "activity_ref": "act-math-cone",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p107-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-cone",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p107-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p108": [
      {
        "id": "hs-math12-p108-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p108-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-ellipse",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p108-activity",
        "type": "activity",
        "activity_ref": "act-math-cone",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p108-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-cone",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p108-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p109": [
      {
        "id": "hs-math12-p109-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p109-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-ellipse",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p109-activity",
        "type": "activity",
        "activity_ref": "act-math-cone",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p109-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-cone",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p109-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p110": [
      {
        "id": "hs-math12-p110-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p110-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-ellipse",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p110-activity",
        "type": "activity",
        "activity_ref": "act-math-ellipse",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p110-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-ellipse",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p110-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p111": [
      {
        "id": "hs-math12-p111-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p111-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-ellipse",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p111-activity",
        "type": "activity",
        "activity_ref": "act-math-ellipse",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p111-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-ellipse",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p111-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p112": [
      {
        "id": "hs-math12-p112-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p112-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-ellipse",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p112-activity",
        "type": "activity",
        "activity_ref": "act-math-ellipse",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p112-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-ellipse",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p112-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p113": [
      {
        "id": "hs-math12-p113-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p113-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-ellipse",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p113-activity",
        "type": "activity",
        "activity_ref": "act-math-ellipse",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p113-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-ellipse",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p113-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p114": [
      {
        "id": "hs-math12-p114-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p114-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-ellipse",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p114-activity",
        "type": "activity",
        "activity_ref": "act-math-ellipse",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p114-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-ellipse",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p114-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p115": [
      {
        "id": "hs-math12-p115-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p115-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-ellipse",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p115-activity",
        "type": "activity",
        "activity_ref": "act-math-ellipse",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p115-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-ellipse",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p115-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p116": [
      {
        "id": "hs-math12-p116-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p116-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-ellipse",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p116-activity",
        "type": "activity",
        "activity_ref": "act-math-ellipse",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p116-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-ellipse",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p116-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p117": [
      {
        "id": "hs-math12-p117-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p117-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-ellipse",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p117-activity",
        "type": "activity",
        "activity_ref": "act-math-ellipse",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p117-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-ellipse",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p117-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p118": [
      {
        "id": "hs-math12-p118-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p118-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-hyperbola",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p118-activity",
        "type": "activity",
        "activity_ref": "act-math-hyperbola",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p118-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-hyperbola",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p118-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p119": [
      {
        "id": "hs-math12-p119-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p119-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-hyperbola",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p119-activity",
        "type": "activity",
        "activity_ref": "act-math-hyperbola",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p119-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-hyperbola",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p119-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p120": [
      {
        "id": "hs-math12-p120-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p120-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-hyperbola",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p120-activity",
        "type": "activity",
        "activity_ref": "act-math-hyperbola",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p120-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-hyperbola",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p120-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p121": [
      {
        "id": "hs-math12-p121-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p121-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-hyperbola",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p121-activity",
        "type": "activity",
        "activity_ref": "act-math-hyperbola",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p121-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-hyperbola",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p121-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p122": [
      {
        "id": "hs-math12-p122-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p122-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-hyperbola",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p122-activity",
        "type": "activity",
        "activity_ref": "act-math-hyperbola",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p122-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-hyperbola",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p122-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p123": [
      {
        "id": "hs-math12-p123-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p123-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-hyperbola",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p123-activity",
        "type": "activity",
        "activity_ref": "act-math-hyperbola",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p123-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-hyperbola",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p123-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p124": [
      {
        "id": "hs-math12-p124-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p124-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-parabola",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p124-activity",
        "type": "activity",
        "activity_ref": "act-math-parabola",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p124-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-parabola",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p124-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p125": [
      {
        "id": "hs-math12-p125-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p125-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-parabola",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p125-activity",
        "type": "activity",
        "activity_ref": "act-math-parabola",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p125-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-parabola",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p125-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p126": [
      {
        "id": "hs-math12-p126-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p126-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-parabola",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p126-activity",
        "type": "activity",
        "activity_ref": "act-math-parabola",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p126-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-parabola",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p126-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p127": [
      {
        "id": "hs-math12-p127-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p127-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-parabola",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p127-activity",
        "type": "activity",
        "activity_ref": "act-math-parabola",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p127-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-parabola",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p127-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p128": [
      {
        "id": "hs-math12-p128-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p128-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-parabola",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p128-activity",
        "type": "activity",
        "activity_ref": "act-math-parabola",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p128-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-parabola",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p128-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p129": [
      {
        "id": "hs-math12-p129-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p129-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-parabola",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p129-activity",
        "type": "activity",
        "activity_ref": "act-math-parabola",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p129-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-parabola",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p129-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p130": [
      {
        "id": "hs-math12-p130-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p130-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-parabola",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p130-activity",
        "type": "activity",
        "activity_ref": "act-math-cone",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p130-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-cone",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p130-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p131": [
      {
        "id": "hs-math12-p131-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p131-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-parabola",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p131-activity",
        "type": "activity",
        "activity_ref": "act-math-cone",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p131-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-cone",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p131-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p132": [
      {
        "id": "hs-math12-p132-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u3-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p132-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-parabola",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p132-activity",
        "type": "activity",
        "activity_ref": "act-math-cone",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p132-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-cone",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p132-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u3",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p133": [
      {
        "id": "hs-math12-p133-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p133-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-space-diagonal",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p133-activity",
        "type": "activity",
        "activity_ref": "act-math-space-diagonal",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p133-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-space",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p133-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p134": [
      {
        "id": "hs-math12-p134-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p134-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-space-diagonal",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p134-activity",
        "type": "activity",
        "activity_ref": "act-math-space-diagonal",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p134-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-space",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p134-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p135": [
      {
        "id": "hs-math12-p135-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p135-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-space-diagonal",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p135-activity",
        "type": "activity",
        "activity_ref": "act-math-space-diagonal",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p135-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-space",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p135-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p136": [
      {
        "id": "hs-math12-p136-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p136-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-space-diagonal",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p136-activity",
        "type": "activity",
        "activity_ref": "act-math-space-diagonal",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p136-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-space",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p136-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p137": [
      {
        "id": "hs-math12-p137-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p137-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-space-diagonal",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p137-activity",
        "type": "activity",
        "activity_ref": "act-math-space-diagonal",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p137-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-space",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p137-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p138": [
      {
        "id": "hs-math12-p138-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p138-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-space-diagonal",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p138-activity",
        "type": "activity",
        "activity_ref": "act-math-space-diagonal",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p138-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-space",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p138-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p139": [
      {
        "id": "hs-math12-p139-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p139-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-space-diagonal",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p139-activity",
        "type": "activity",
        "activity_ref": "act-math-space-diagonal",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p139-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-space",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p139-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p140": [
      {
        "id": "hs-math12-p140-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p140-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-space-diagonal",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p140-activity",
        "type": "activity",
        "activity_ref": "act-math-space-diagonal",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p140-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-space",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p140-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p141": [
      {
        "id": "hs-math12-p141-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p141-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-space-diagonal",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p141-activity",
        "type": "activity",
        "activity_ref": "act-math-space-diagonal",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p141-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-space",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p141-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p142": [
      {
        "id": "hs-math12-p142-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p142-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-line-plane",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p142-activity",
        "type": "activity",
        "activity_ref": "act-math-line-plane",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p142-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-line-plane",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p142-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p143": [
      {
        "id": "hs-math12-p143-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p143-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-line-plane",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p143-activity",
        "type": "activity",
        "activity_ref": "act-math-line-plane",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p143-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-line-plane",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p143-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p144": [
      {
        "id": "hs-math12-p144-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p144-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-line-plane",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p144-activity",
        "type": "activity",
        "activity_ref": "act-math-line-plane",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p144-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-line-plane",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p144-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p145": [
      {
        "id": "hs-math12-p145-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p145-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-line-plane",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p145-activity",
        "type": "activity",
        "activity_ref": "act-math-line-plane",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p145-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-line-plane",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p145-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p146": [
      {
        "id": "hs-math12-p146-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p146-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-line-plane",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p146-activity",
        "type": "activity",
        "activity_ref": "act-math-line-plane",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p146-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-line-plane",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p146-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p147": [
      {
        "id": "hs-math12-p147-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p147-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-dihedral",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p147-activity",
        "type": "activity",
        "activity_ref": "act-math-dihedral",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p147-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-dihedral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p147-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p148": [
      {
        "id": "hs-math12-p148-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p148-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-dihedral",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p148-activity",
        "type": "activity",
        "activity_ref": "act-math-dihedral",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p148-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-dihedral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p148-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p149": [
      {
        "id": "hs-math12-p149-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p149-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-dihedral",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p149-activity",
        "type": "activity",
        "activity_ref": "act-math-dihedral",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p149-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-dihedral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p149-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p150": [
      {
        "id": "hs-math12-p150-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p150-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-dihedral",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p150-activity",
        "type": "activity",
        "activity_ref": "act-math-dihedral",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p150-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-dihedral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p150-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p151": [
      {
        "id": "hs-math12-p151-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p151-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-dihedral",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p151-activity",
        "type": "activity",
        "activity_ref": "act-math-dihedral",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p151-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-dihedral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p151-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p152": [
      {
        "id": "hs-math12-p152-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p152-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-dihedral",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p152-activity",
        "type": "activity",
        "activity_ref": "act-math-dihedral",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p152-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-dihedral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p152-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p153": [
      {
        "id": "hs-math12-p153-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u4-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p153-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-dihedral",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p153-activity",
        "type": "activity",
        "activity_ref": "act-math-dihedral",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p153-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-dihedral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p153-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u4",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p154": [
      {
        "id": "hs-math12-p154-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p154-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p154-activity",
        "type": "activity",
        "activity_ref": "act-math-power-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p154-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p154-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p155": [
      {
        "id": "hs-math12-p155-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p155-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p155-activity",
        "type": "activity",
        "activity_ref": "act-math-power-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p155-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p155-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p156": [
      {
        "id": "hs-math12-p156-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p156-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p156-activity",
        "type": "activity",
        "activity_ref": "act-math-power-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p156-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p156-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p157": [
      {
        "id": "hs-math12-p157-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p157-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p157-activity",
        "type": "activity",
        "activity_ref": "act-math-power-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p157-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p157-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p158": [
      {
        "id": "hs-math12-p158-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p158-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p158-activity",
        "type": "activity",
        "activity_ref": "act-math-power-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p158-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p158-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p159": [
      {
        "id": "hs-math12-p159-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p159-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p159-activity",
        "type": "activity",
        "activity_ref": "act-math-power-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p159-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p159-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p160": [
      {
        "id": "hs-math12-p160-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p160-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p160-activity",
        "type": "activity",
        "activity_ref": "act-math-product-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p160-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p160-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p161": [
      {
        "id": "hs-math12-p161-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p161-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p161-activity",
        "type": "activity",
        "activity_ref": "act-math-product-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p161-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p161-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p162": [
      {
        "id": "hs-math12-p162-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p162-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p162-activity",
        "type": "activity",
        "activity_ref": "act-math-product-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p162-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p162-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p163": [
      {
        "id": "hs-math12-p163-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p163-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p163-activity",
        "type": "activity",
        "activity_ref": "act-math-product-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p163-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p163-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p164": [
      {
        "id": "hs-math12-p164-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p164-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p164-activity",
        "type": "activity",
        "activity_ref": "act-math-product-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p164-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p164-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p165": [
      {
        "id": "hs-math12-p165-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p165-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p165-activity",
        "type": "activity",
        "activity_ref": "act-math-product-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p165-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p165-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p166": [
      {
        "id": "hs-math12-p166-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p166-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-chain",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p166-activity",
        "type": "activity",
        "activity_ref": "act-math-chain-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p166-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p166-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p167": [
      {
        "id": "hs-math12-p167-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p167-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-chain",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p167-activity",
        "type": "activity",
        "activity_ref": "act-math-chain-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p167-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p167-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p168": [
      {
        "id": "hs-math12-p168-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p168-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-chain",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p168-activity",
        "type": "activity",
        "activity_ref": "act-math-chain-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p168-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p168-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p169": [
      {
        "id": "hs-math12-p169-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p169-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-chain",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p169-activity",
        "type": "activity",
        "activity_ref": "act-math-chain-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p169-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p169-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p170": [
      {
        "id": "hs-math12-p170-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p170-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-chain",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p170-activity",
        "type": "activity",
        "activity_ref": "act-math-chain-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p170-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p170-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p171": [
      {
        "id": "hs-math12-p171-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p171-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p171-activity",
        "type": "activity",
        "activity_ref": "act-math-power-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p171-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p171-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p172": [
      {
        "id": "hs-math12-p172-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p172-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p172-activity",
        "type": "activity",
        "activity_ref": "act-math-power-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p172-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p172-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p173": [
      {
        "id": "hs-math12-p173-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p173-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p173-activity",
        "type": "activity",
        "activity_ref": "act-math-power-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p173-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p173-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p174": [
      {
        "id": "hs-math12-p174-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p174-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p174-activity",
        "type": "activity",
        "activity_ref": "act-math-power-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p174-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p174-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p175": [
      {
        "id": "hs-math12-p175-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p175-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-chain",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p175-activity",
        "type": "activity",
        "activity_ref": "act-math-chain-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p175-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p175-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p176": [
      {
        "id": "hs-math12-p176-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p176-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-chain",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p176-activity",
        "type": "activity",
        "activity_ref": "act-math-chain-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p176-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p176-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p177": [
      {
        "id": "hs-math12-p177-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p177-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-chain",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p177-activity",
        "type": "activity",
        "activity_ref": "act-math-chain-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p177-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p177-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p178": [
      {
        "id": "hs-math12-p178-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p178-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-chain",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p178-activity",
        "type": "activity",
        "activity_ref": "act-math-chain-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p178-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p178-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p179": [
      {
        "id": "hs-math12-p179-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p179-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-chain",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p179-activity",
        "type": "activity",
        "activity_ref": "act-math-chain-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p179-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p179-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p180": [
      {
        "id": "hs-math12-p180-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p180-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-chain",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p180-activity",
        "type": "activity",
        "activity_ref": "act-math-chain-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p180-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p180-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p181": [
      {
        "id": "hs-math12-p181-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p181-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-chain",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p181-activity",
        "type": "activity",
        "activity_ref": "act-math-chain-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p181-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p181-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p182": [
      {
        "id": "hs-math12-p182-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p182-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-chain",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p182-activity",
        "type": "activity",
        "activity_ref": "act-math-chain-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p182-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p182-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p183": [
      {
        "id": "hs-math12-p183-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l6",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p183-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p183-activity",
        "type": "activity",
        "activity_ref": "act-math-product-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p183-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p183-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p184": [
      {
        "id": "hs-math12-p184-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l6",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p184-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p184-activity",
        "type": "activity",
        "activity_ref": "act-math-product-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p184-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p184-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p185": [
      {
        "id": "hs-math12-p185-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l6",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p185-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p185-activity",
        "type": "activity",
        "activity_ref": "act-math-product-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p185-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p185-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p186": [
      {
        "id": "hs-math12-p186-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l6",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p186-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-power",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p186-activity",
        "type": "activity",
        "activity_ref": "act-math-product-rule",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p186-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p186-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p187": [
      {
        "id": "hs-math12-p187-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p187-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-extrema",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p187-activity",
        "type": "activity",
        "activity_ref": "act-math-extrema",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p187-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p187-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p188": [
      {
        "id": "hs-math12-p188-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p188-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-extrema",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p188-activity",
        "type": "activity",
        "activity_ref": "act-math-extrema",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p188-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p188-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p189": [
      {
        "id": "hs-math12-p189-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p189-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-extrema",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p189-activity",
        "type": "activity",
        "activity_ref": "act-math-extrema",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p189-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p189-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p190": [
      {
        "id": "hs-math12-p190-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p190-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-extrema",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p190-activity",
        "type": "activity",
        "activity_ref": "act-math-extrema",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p190-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p190-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p191": [
      {
        "id": "hs-math12-p191-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p191-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-extrema",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p191-activity",
        "type": "activity",
        "activity_ref": "act-math-extrema",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p191-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p191-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p192": [
      {
        "id": "hs-math12-p192-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p192-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-extrema",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p192-activity",
        "type": "activity",
        "activity_ref": "act-math-extrema",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p192-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p192-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p193": [
      {
        "id": "hs-math12-p193-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p193-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-extrema",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p193-activity",
        "type": "activity",
        "activity_ref": "act-math-extrema",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p193-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p193-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p194": [
      {
        "id": "hs-math12-p194-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p194-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-extrema",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p194-activity",
        "type": "activity",
        "activity_ref": "act-math-extrema",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p194-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p194-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p195": [
      {
        "id": "hs-math12-p195-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p195-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-extrema",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p195-activity",
        "type": "activity",
        "activity_ref": "act-math-extrema",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p195-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p195-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p196": [
      {
        "id": "hs-math12-p196-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p196-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-extrema",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p196-activity",
        "type": "activity",
        "activity_ref": "act-math-extrema",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p196-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p196-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p197": [
      {
        "id": "hs-math12-p197-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p197-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-extrema",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p197-activity",
        "type": "activity",
        "activity_ref": "act-math-extrema",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p197-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p197-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p198": [
      {
        "id": "hs-math12-p198-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p198-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-extrema",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p198-activity",
        "type": "activity",
        "activity_ref": "act-math-extrema",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p198-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p198-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p199": [
      {
        "id": "hs-math12-p199-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p199-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-extrema",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p199-activity",
        "type": "activity",
        "activity_ref": "act-math-extrema",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p199-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p199-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p200": [
      {
        "id": "hs-math12-p200-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l8",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p200-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-mvt",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p200-activity",
        "type": "activity",
        "activity_ref": "act-math-mvt",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p200-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p200-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p201": [
      {
        "id": "hs-math12-p201-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l8",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p201-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-mvt",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p201-activity",
        "type": "activity",
        "activity_ref": "act-math-mvt",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p201-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p201-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p202": [
      {
        "id": "hs-math12-p202-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l8",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p202-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-mvt",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p202-activity",
        "type": "activity",
        "activity_ref": "act-math-mvt",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p202-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p202-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p203": [
      {
        "id": "hs-math12-p203-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l8",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p203-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-mvt",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p203-activity",
        "type": "activity",
        "activity_ref": "act-math-mvt",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p203-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p203-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p204": [
      {
        "id": "hs-math12-p204-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l8",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p204-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-mvt",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p204-activity",
        "type": "activity",
        "activity_ref": "act-math-mvt",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p204-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p204-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p205": [
      {
        "id": "hs-math12-p205-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l8",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p205-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-mvt",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p205-activity",
        "type": "activity",
        "activity_ref": "act-math-mvt",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p205-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p205-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p206": [
      {
        "id": "hs-math12-p206-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l8",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p206-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-mvt",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p206-activity",
        "type": "activity",
        "activity_ref": "act-math-mvt",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p206-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p206-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p207": [
      {
        "id": "hs-math12-p207-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l8",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p207-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-mvt",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p207-activity",
        "type": "activity",
        "activity_ref": "act-math-mvt",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p207-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p207-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p208": [
      {
        "id": "hs-math12-p208-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l8",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p208-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-mvt",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p208-activity",
        "type": "activity",
        "activity_ref": "act-math-mvt",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p208-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p208-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p209": [
      {
        "id": "hs-math12-p209-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u6-l8",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p209-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-mvt",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p209-activity",
        "type": "activity",
        "activity_ref": "act-math-mvt",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p209-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-derivative",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p209-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u6",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p210": [
      {
        "id": "hs-math12-p210-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p210-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p210-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p210-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p210-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p211": [
      {
        "id": "hs-math12-p211-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p211-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p211-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p211-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p211-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p212": [
      {
        "id": "hs-math12-p212-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p212-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p212-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p212-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p212-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p213": [
      {
        "id": "hs-math12-p213-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p213-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p213-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p213-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p213-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p214": [
      {
        "id": "hs-math12-p214-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p214-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p214-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p214-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p214-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p215": [
      {
        "id": "hs-math12-p215-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p215-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p215-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p215-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p215-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p216": [
      {
        "id": "hs-math12-p216-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p216-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p216-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p216-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p216-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p217": [
      {
        "id": "hs-math12-p217-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p217-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p217-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p217-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p217-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p218": [
      {
        "id": "hs-math12-p218-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p218-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p218-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p218-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p218-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p219": [
      {
        "id": "hs-math12-p219-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p219-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p219-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p219-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p219-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p220": [
      {
        "id": "hs-math12-p220-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p220-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p220-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p220-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p220-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p221": [
      {
        "id": "hs-math12-p221-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l1",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p221-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p221-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p221-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p221-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p222": [
      {
        "id": "hs-math12-p222-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p222-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p222-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p222-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p222-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p223": [
      {
        "id": "hs-math12-p223-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p223-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p223-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p223-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p223-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p224": [
      {
        "id": "hs-math12-p224-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p224-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p224-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p224-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p224-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p225": [
      {
        "id": "hs-math12-p225-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p225-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p225-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p225-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p225-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p226": [
      {
        "id": "hs-math12-p226-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p226-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p226-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p226-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p226-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p227": [
      {
        "id": "hs-math12-p227-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p227-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p227-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p227-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p227-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p228": [
      {
        "id": "hs-math12-p228-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p228-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p228-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p228-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p228-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p229": [
      {
        "id": "hs-math12-p229-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p229-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p229-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p229-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p229-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p230": [
      {
        "id": "hs-math12-p230-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p230-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p230-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p230-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p230-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p231": [
      {
        "id": "hs-math12-p231-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p231-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p231-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p231-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p231-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p232": [
      {
        "id": "hs-math12-p232-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p232-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p232-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p232-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p232-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p233": [
      {
        "id": "hs-math12-p233-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p233-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p233-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p233-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p233-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p234": [
      {
        "id": "hs-math12-p234-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l2",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p234-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-indefinite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p234-activity",
        "type": "activity",
        "activity_ref": "act-math-indefinite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p234-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p234-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p235": [
      {
        "id": "hs-math12-p235-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p235-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-definite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p235-activity",
        "type": "activity",
        "activity_ref": "act-math-definite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p235-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p235-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p236": [
      {
        "id": "hs-math12-p236-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p236-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-definite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p236-activity",
        "type": "activity",
        "activity_ref": "act-math-definite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p236-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p236-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p237": [
      {
        "id": "hs-math12-p237-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p237-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-definite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p237-activity",
        "type": "activity",
        "activity_ref": "act-math-definite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p237-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p237-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p238": [
      {
        "id": "hs-math12-p238-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p238-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-definite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p238-activity",
        "type": "activity",
        "activity_ref": "act-math-definite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p238-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p238-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p239": [
      {
        "id": "hs-math12-p239-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l3",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p239-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-definite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p239-activity",
        "type": "activity",
        "activity_ref": "act-math-definite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p239-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p239-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p240": [
      {
        "id": "hs-math12-p240-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p240-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-definite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p240-activity",
        "type": "activity",
        "activity_ref": "act-math-definite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p240-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p240-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p241": [
      {
        "id": "hs-math12-p241-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p241-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-definite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p241-activity",
        "type": "activity",
        "activity_ref": "act-math-definite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p241-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p241-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p242": [
      {
        "id": "hs-math12-p242-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p242-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-definite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p242-activity",
        "type": "activity",
        "activity_ref": "act-math-definite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p242-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p242-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p243": [
      {
        "id": "hs-math12-p243-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l4",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p243-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-definite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p243-activity",
        "type": "activity",
        "activity_ref": "act-math-definite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p243-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p243-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p244": [
      {
        "id": "hs-math12-p244-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p244-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-area",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p244-activity",
        "type": "activity",
        "activity_ref": "act-math-area",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p244-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-area",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p244-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p245": [
      {
        "id": "hs-math12-p245-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p245-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-area",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p245-activity",
        "type": "activity",
        "activity_ref": "act-math-area",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p245-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-area",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p245-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p246": [
      {
        "id": "hs-math12-p246-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p246-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-area",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p246-activity",
        "type": "activity",
        "activity_ref": "act-math-area",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p246-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-area",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p246-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p247": [
      {
        "id": "hs-math12-p247-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l5",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p247-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-area",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p247-activity",
        "type": "activity",
        "activity_ref": "act-math-area",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p247-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-area",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p247-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p248": [
      {
        "id": "hs-math12-p248-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l6",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p248-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-revolution",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p248-activity",
        "type": "activity",
        "activity_ref": "act-math-revolution",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p248-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-revolution",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p248-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p249": [
      {
        "id": "hs-math12-p249-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l6",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p249-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-revolution",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p249-activity",
        "type": "activity",
        "activity_ref": "act-math-revolution",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p249-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-revolution",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p249-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p250": [
      {
        "id": "hs-math12-p250-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l6",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p250-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-revolution",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p250-activity",
        "type": "activity",
        "activity_ref": "act-math-revolution",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p250-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-revolution",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p250-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p251": [
      {
        "id": "hs-math12-p251-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l6",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p251-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-revolution",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p251-activity",
        "type": "activity",
        "activity_ref": "act-math-revolution",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p251-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-revolution",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p251-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p252": [
      {
        "id": "hs-math12-p252-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p252-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-definite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p252-activity",
        "type": "activity",
        "activity_ref": "act-math-definite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p252-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p252-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p253": [
      {
        "id": "hs-math12-p253-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p253-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-definite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p253-activity",
        "type": "activity",
        "activity_ref": "act-math-definite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p253-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p253-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p254": [
      {
        "id": "hs-math12-p254-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p254-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-definite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p254-activity",
        "type": "activity",
        "activity_ref": "act-math-definite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p254-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p254-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p255": [
      {
        "id": "hs-math12-p255-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p255-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-definite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p255-activity",
        "type": "activity",
        "activity_ref": "act-math-definite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p255-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p255-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ],
    "math12-p256": [
      {
        "id": "hs-math12-p256-concept",
        "type": "explainable_text",
        "explanation_ref": "math-u7-l7",
        "indicator_label": "📌 شرح المفهوم والصيغة",
        "highlight_color": "rgba(0, 168, 89, 0.13)",
        "bounds": {
          "x": 0.7,
          "y": 0.06,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p256-solution",
        "type": "step_by_step_equation",
        "solution_ref": "sol-math-definite",
        "indicator_label": "🧮 حل مسألة خطوة بخطوة",
        "highlight_color": "rgba(0, 168, 89, 0.10)",
        "bounds": {
          "x": 0.7,
          "y": 0.24,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p256-activity",
        "type": "activity",
        "activity_ref": "act-math-definite",
        "indicator_label": "🎮 نشاط تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.16)",
        "bounds": {
          "x": 0.7,
          "y": 0.42,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p256-3d",
        "type": "interactive_3d",
        "diagram_ref": "diag-math-integral",
        "indicator_label": "🧊 مجسم هندسي تفاعلي",
        "highlight_color": "rgba(0, 168, 89, 0.12)",
        "bounds": {
          "x": 0.7,
          "y": 0.6,
          "w": 0.24,
          "h": 0.14
        }
      },
      {
        "id": "hs-math12-p256-quiz",
        "type": "assessment",
        "assessment_ref": "quiz-math-u7",
        "indicator_label": "✅ اختبر نفسك",
        "highlight_color": "rgba(0, 168, 89, 0.14)",
        "bounds": {
          "x": 0.7,
          "y": 0.78,
          "w": 0.24,
          "h": 0.14
        }
      }
    ]
  },
  "explanations": {
    "exp-math-u1-overview": {
      "id": "exp-math-u1-overview",
      "title": "مقدمة وأهداف الوحدة الأولى: الأعداد المركبة",
      "original_text": "الوحدة الأولى: الأعداد المركبة (ص 7 - 44): مفهوم العدد المركب، تمثيله في مستوى أرغاند، القيمة المطلقة والزاوية، والصيغة القطبية",
      "levels": {
        "basic": "🎯 أهلاً بك في الوحدة الأولى: الأعداد المركبة. الفكرة الأساسية: مفهوم العدد المركب، تمثيله في مستوى أرغاند، القيمة المطلقة والزاوية، والصيغة القطبية",
        "intermediate": "📘 اقرأ الصفحة الأصلية، ثم حدد المطلوب، واكتب الصيغة المناسبة قبل التعويض. اربط كل خطوة بمعنى هندسي أو فيزيائي.",
        "advanced": "🚀 تطبيقات واقعية:\n• التيار المتردد والهندسة الكهربائية\n• الإشارات والدوائر الإلكترونية\n• تحويل الإحداثيات في المستوى"
      },
      "chemical_equations": [
        {
          "label": "قاعدة 1",
          "eq": "z = a + bi، i² = −1"
        },
        {
          "label": "قاعدة 2",
          "eq": "|z| = √(a² + b²)"
        },
        {
          "label": "قاعدة 3",
          "eq": "z = r(cos θ + i sin θ)"
        }
      ],
      "math_equations": [
        {
          "label": "قاعدة 1",
          "eq": "z = a + bi، i² = −1"
        },
        {
          "label": "قاعدة 2",
          "eq": "|z| = √(a² + b²)"
        },
        {
          "label": "قاعدة 3",
          "eq": "z = r(cos θ + i sin θ)"
        }
      ],
      "tts_text": "الوحدة الأولى: الأعداد المركبة. مفهوم العدد المركب، تمثيله في مستوى أرغاند، القيمة المطلقة والزاوية، والصيغة القطبية"
    },
    "exp-math-u2-overview": {
      "id": "exp-math-u2-overview",
      "title": "مقدمة وأهداف الوحدة الثانية: مبرهنة دي موافر والتوسعة ذات الحدين",
      "original_text": "الوحدة الثانية: مبرهنة دي موافر والتوسعة ذات الحدين (ص 45 - 73): مبرهنة دي موافر، الجذور النونية للعدد المركب، والتوسعة ذات الحدين وتطبيقاتها",
      "levels": {
        "basic": "🎯 أهلاً بك في الوحدة الثانية: مبرهنة دي موافر والتوسعة ذات الحدين. الفكرة الأساسية: مبرهنة دي موافر، الجذور النونية للعدد المركب، والتوسعة ذات الحدين وتطبيقاتها",
        "intermediate": "📘 اقرأ الصفحة الأصلية، ثم حدد المطلوب، واكتب الصيغة المناسبة قبل التعويض. اربط كل خطوة بمعنى هندسي أو فيزيائي.",
        "advanced": "🚀 تطبيقات واقعية:\n• حساب القوى للإشارات الدورية\n• توزيع الاحتمالات ذو الحدين\n• النماذج الهندسية الدوارة"
      },
      "chemical_equations": [
        {
          "label": "قاعدة 1",
          "eq": "[r(cos θ + i sin θ)]ⁿ = rⁿ(cos nθ + i sin nθ)"
        },
        {
          "label": "قاعدة 2",
          "eq": "zⁿ = rⁿ(cos nθ + i sin nθ)"
        },
        {
          "label": "قاعدة 3",
          "eq": "(a + b)ⁿ = Σ C(n,k)aⁿ⁻ᵏbᵏ"
        }
      ],
      "math_equations": [
        {
          "label": "قاعدة 1",
          "eq": "[r(cos θ + i sin θ)]ⁿ = rⁿ(cos nθ + i sin nθ)"
        },
        {
          "label": "قاعدة 2",
          "eq": "zⁿ = rⁿ(cos nθ + i sin nθ)"
        },
        {
          "label": "قاعدة 3",
          "eq": "(a + b)ⁿ = Σ C(n,k)aⁿ⁻ᵏbᵏ"
        }
      ],
      "tts_text": "الوحدة الثانية: مبرهنة دي موافر والتوسعة ذات الحدين. مبرهنة دي موافر، الجذور النونية للعدد المركب، والتوسعة ذات الحدين وتطبيقاتها"
    },
    "exp-math-u3-overview": {
      "id": "exp-math-u3-overview",
      "title": "مقدمة وأهداف الوحدة الثالثة: القطوع المخروطية",
      "original_text": "الوحدة الثالثة: القطوع المخروطية (ص 104 - 132): القطع الناقص والقطع الزائد والقطع المكافئ ومعادلاتها القياسية وخصائصها",
      "levels": {
        "basic": "🎯 أهلاً بك في الوحدة الثالثة: القطوع المخروطية. الفكرة الأساسية: القطع الناقص والقطع الزائد والقطع المكافئ ومعادلاتها القياسية وخصائصها",
        "intermediate": "📘 اقرأ الصفحة الأصلية، ثم حدد المطلوب، واكتب الصيغة المناسبة قبل التعويض. اربط كل خطوة بمعنى هندسي أو فيزيائي.",
        "advanced": "🚀 تطبيقات واقعية:\n• أقمار الاتصالات ومدارات الكواكب\n• أطباق التلسكوبات والهوائيات\n• تصميم الجسور والأنفاق"
      },
      "chemical_equations": [
        {
          "label": "قاعدة 1",
          "eq": "القطع الناقص: x²/a² + y²/b² = 1"
        },
        {
          "label": "قاعدة 2",
          "eq": "القطع الزائد: x²/a² − y²/b² = 1"
        },
        {
          "label": "قاعدة 3",
          "eq": "القطع المكافئ: y² = 4px"
        }
      ],
      "math_equations": [
        {
          "label": "قاعدة 1",
          "eq": "القطع الناقص: x²/a² + y²/b² = 1"
        },
        {
          "label": "قاعدة 2",
          "eq": "القطع الزائد: x²/a² − y²/b² = 1"
        },
        {
          "label": "قاعدة 3",
          "eq": "القطع المكافئ: y² = 4px"
        }
      ],
      "tts_text": "الوحدة الثالثة: القطوع المخروطية. القطع الناقص والقطع الزائد والقطع المكافئ ومعادلاتها القياسية وخصائصها"
    },
    "exp-math-u4-overview": {
      "id": "exp-math-u4-overview",
      "title": "مقدمة وأهداف الوحدة الرابعة: الهندسة في فضاء ثلاثي الأبعاد",
      "original_text": "الوحدة الرابعة: الهندسة في فضاء ثلاثي الأبعاد (ص 133 - 153): المستقيمات والمستويات، المسافات، والزوايا في الفراغ ثلاثي الأبعاد",
      "levels": {
        "basic": "🎯 أهلاً بك في الوحدة الرابعة: الهندسة في فضاء ثلاثي الأبعاد. الفكرة الأساسية: المستقيمات والمستويات، المسافات، والزوايا في الفراغ ثلاثي الأبعاد",
        "intermediate": "📘 اقرأ الصفحة الأصلية، ثم حدد المطلوب، واكتب الصيغة المناسبة قبل التعويض. اربط كل خطوة بمعنى هندسي أو فيزيائي.",
        "advanced": "🚀 تطبيقات واقعية:\n• تحديد اتجاه الطائرات والسفن\n• هندسة المباني والرافعات\n• نمذجة الكاميرات والرسوم ثلاثية الأبعاد"
      },
      "chemical_equations": [
        {
          "label": "قاعدة 1",
          "eq": "مسافة نقطة من مستوى: |Ax₀ + By₀ + Cz₀ + D| / √(A²+B²+C²)"
        },
        {
          "label": "قاعدة 2",
          "eq": "cos φ = |n₁·n₂| / (|n₁||n₂|)"
        },
        {
          "label": "قاعدة 3",
          "eq": "طول القطر الفراغي لمكعب: d = a√3"
        }
      ],
      "math_equations": [
        {
          "label": "قاعدة 1",
          "eq": "مسافة نقطة من مستوى: |Ax₀ + By₀ + Cz₀ + D| / √(A²+B²+C²)"
        },
        {
          "label": "قاعدة 2",
          "eq": "cos φ = |n₁·n₂| / (|n₁||n₂|)"
        },
        {
          "label": "قاعدة 3",
          "eq": "طول القطر الفراغي لمكعب: d = a√3"
        }
      ],
      "tts_text": "الوحدة الرابعة: الهندسة في فضاء ثلاثي الأبعاد. المستقيمات والمستويات، المسافات، والزوايا في الفراغ ثلاثي الأبعاد"
    },
    "exp-math-u5-overview": {
      "id": "exp-math-u5-overview",
      "title": "مقدمة وأهداف الوحدة الخامسة: الاحتمالات",
      "original_text": "الوحدة الخامسة: الاحتمالات (ص 74 - 103): التجارب العشوائية، قواعد الجمع والضرب، الاحتمال الشرطي، والتوزيع ذو الحدين",
      "levels": {
        "basic": "🎯 أهلاً بك في الوحدة الخامسة: الاحتمالات. الفكرة الأساسية: التجارب العشوائية، قواعد الجمع والضرب، الاحتمال الشرطي، والتوزيع ذو الحدين",
        "intermediate": "📘 اقرأ الصفحة الأصلية، ثم حدد المطلوب، واكتب الصيغة المناسبة قبل التعويض. اربط كل خطوة بمعنى هندسي أو فيزيائي.",
        "advanced": "🚀 تطبيقات واقعية:\n• تقييم المخاطر في التأمين\n• تحليل نتائج التجارب والاستطلاعات\n• نمذجة جودة التصنيع"
      },
      "chemical_equations": [
        {
          "label": "قاعدة 1",
          "eq": "P(A∪B) = P(A) + P(B) − P(A∩B)"
        },
        {
          "label": "قاعدة 2",
          "eq": "P(A|B) = P(A∩B) / P(B)"
        },
        {
          "label": "قاعدة 3",
          "eq": "P(X=k) = C(n,k)pᵏ(1−p)ⁿ⁻ᵏ"
        }
      ],
      "math_equations": [
        {
          "label": "قاعدة 1",
          "eq": "P(A∪B) = P(A) + P(B) − P(A∩B)"
        },
        {
          "label": "قاعدة 2",
          "eq": "P(A|B) = P(A∩B) / P(B)"
        },
        {
          "label": "قاعدة 3",
          "eq": "P(X=k) = C(n,k)pᵏ(1−p)ⁿ⁻ᵏ"
        }
      ],
      "tts_text": "الوحدة الخامسة: الاحتمالات. التجارب العشوائية، قواعد الجمع والضرب، الاحتمال الشرطي، والتوزيع ذو الحدين"
    },
    "exp-math-u6-overview": {
      "id": "exp-math-u6-overview",
      "title": "مقدمة وأهداف الوحدة السادسة: المشتقات",
      "original_text": "الوحدة السادسة: المشتقات (ص 154 - 209): مفهوم المشتقة، قواعد الاشتقاق، مشتقة الدوال المركبة، القيم القصوى ونظرية القيمة المتوسطة",
      "levels": {
        "basic": "🎯 أهلاً بك في الوحدة السادسة: المشتقات. الفكرة الأساسية: مفهوم المشتقة، قواعد الاشتقاق، مشتقة الدوال المركبة، القيم القصوى ونظرية القيمة المتوسطة",
        "intermediate": "📘 اقرأ الصفحة الأصلية، ثم حدد المطلوب، واكتب الصيغة المناسبة قبل التعويض. اربط كل خطوة بمعنى هندسي أو فيزيائي.",
        "advanced": "🚀 تطبيقات واقعية:\n• السرعة والتسارع في الفيزياء\n• تحسين الربح والتكلفة في الاقتصاد\n• ميول المنحنيات في التصميم"
      },
      "chemical_equations": [
        {
          "label": "قاعدة 1",
          "eq": "f′(x) = limₕ→₀ [f(x+h) − f(x)] / h"
        },
        {
          "label": "قاعدة 2",
          "eq": "(xⁿ)′ = nxⁿ⁻¹"
        },
        {
          "label": "قاعدة 3",
          "eq": "(f∘g)′(x) = f′(g(x))g′(x)"
        }
      ],
      "math_equations": [
        {
          "label": "قاعدة 1",
          "eq": "f′(x) = limₕ→₀ [f(x+h) − f(x)] / h"
        },
        {
          "label": "قاعدة 2",
          "eq": "(xⁿ)′ = nxⁿ⁻¹"
        },
        {
          "label": "قاعدة 3",
          "eq": "(f∘g)′(x) = f′(g(x))g′(x)"
        }
      ],
      "tts_text": "الوحدة السادسة: المشتقات. مفهوم المشتقة، قواعد الاشتقاق، مشتقة الدوال المركبة، القيم القصوى ونظرية القيمة المتوسطة"
    },
    "exp-math-u7-overview": {
      "id": "exp-math-u7-overview",
      "title": "مقدمة وأهداف الوحدة السابعة: التكامل",
      "original_text": "الوحدة السابعة: التكامل (ص 210 - 256): التكامل غير المحدد والمحدد، طرق التكامل، المساحات، وحجوم الدوران",
      "levels": {
        "basic": "🎯 أهلاً بك في الوحدة السابعة: التكامل. الفكرة الأساسية: التكامل غير المحدد والمحدد، طرق التكامل، المساحات، وحجوم الدوران",
        "intermediate": "📘 اقرأ الصفحة الأصلية، ثم حدد المطلوب، واكتب الصيغة المناسبة قبل التعويض. اربط كل خطوة بمعنى هندسي أو فيزيائي.",
        "advanced": "🚀 تطبيقات واقعية:\n• حساب المساحات غير المنتظمة\n• حجوم الخزانات والأوعية الدوارة\n• الشغل والطاقة في الفيزياء"
      },
      "chemical_equations": [
        {
          "label": "قاعدة 1",
          "eq": "∫xⁿdx = xⁿ⁺¹/(n+1) + C، n ≠ −1"
        },
        {
          "label": "قاعدة 2",
          "eq": "∫ₐᵇ f(x)dx = F(b) − F(a)"
        },
        {
          "label": "قاعدة 3",
          "eq": "V = π∫ₐᵇ [f(x)]²dx"
        }
      ],
      "math_equations": [
        {
          "label": "قاعدة 1",
          "eq": "∫xⁿdx = xⁿ⁺¹/(n+1) + C، n ≠ −1"
        },
        {
          "label": "قاعدة 2",
          "eq": "∫ₐᵇ f(x)dx = F(b) − F(a)"
        },
        {
          "label": "قاعدة 3",
          "eq": "V = π∫ₐᵇ [f(x)]²dx"
        }
      ],
      "tts_text": "الوحدة السابعة: التكامل. التكامل غير المحدد والمحدد، طرق التكامل، المساحات، وحجوم الدوران"
    },
    "math-u1-l1": {
      "id": "math-u1-l1",
      "title": "مفهوم العدد المركب والوحدة التخيلية",
      "original_text": "من كتاب الطالب، الصفحات 7 إلى 11: مفهوم العدد المركب والوحدة التخيلية.",
      "levels": {
        "basic": "📌 مفهوم العدد المركب والوحدة التخيلية: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 العدد المركب يوسّع مجموعة الأعداد الحقيقية بإضافة الوحدة التخيلية i. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 يمثل z نقطة (a، b) في مستوى أرغاند."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "i² = −1، z = a + bi"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "i² = −1، z = a + bi"
        }
      ],
      "tts_text": "مفهوم العدد المركب والوحدة التخيلية. العدد المركب يوسّع مجموعة الأعداد الحقيقية بإضافة الوحدة التخيلية i."
    },
    "math-u1-l2": {
      "id": "math-u1-l2",
      "title": "العمليات على الأعداد المركبة",
      "original_text": "من كتاب الطالب، الصفحات 12 إلى 15: العمليات على الأعداد المركبة.",
      "levels": {
        "basic": "📌 العمليات على الأعداد المركبة: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 تُجرى العمليات على الأعداد المركبة بمعاملة i كمتغير مع i² = −1. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 الجمع والطرح مكوّن ب مكوّن، والضرب يستخدم i²."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "(a+bi)+(c+di)=(a+c)+(b+d)i"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "(a+bi)+(c+di)=(a+c)+(b+d)i"
        }
      ],
      "tts_text": "العمليات على الأعداد المركبة. تُجرى العمليات على الأعداد المركبة بمعاملة i كمتغير مع i² = −1."
    },
    "math-u1-l3": {
      "id": "math-u1-l3",
      "title": "التمثيل الهندسي والقيمة المطلقة",
      "original_text": "من كتاب الطالب، الصفحات 16 إلى 22: التمثيل الهندسي والقيمة المطلقة.",
      "levels": {
        "basic": "📌 التمثيل الهندسي والقيمة المطلقة: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 القيمة المطلقة للعدد المركب هي طول متجهه من مبدأ الإحداثيات. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 المسافة بين عددين مركبين هي |z₁ − z₂|."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "|z| = √(a² + b²)"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "|z| = √(a² + b²)"
        }
      ],
      "tts_text": "التمثيل الهندسي والقيمة المطلقة. القيمة المطلقة للعدد المركب هي طول متجهه من مبدأ الإحداثيات."
    },
    "math-u1-l4": {
      "id": "math-u1-l4",
      "title": "سعة العدد المركب وزاويته",
      "original_text": "من كتاب الطالب، الصفحات 23 إلى 32: سعة العدد المركب وزاويته.",
      "levels": {
        "basic": "📌 سعة العدد المركب وزاويته: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 تحدد السعة اتجاه متجه العدد المركب في المستوى. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 يجب مراعاة الربع الذي تقع فيه النقطة عند حساب θ."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "θ = tan⁻¹(b/a)"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "θ = tan⁻¹(b/a)"
        }
      ],
      "tts_text": "سعة العدد المركب وزاويته. تحدد السعة اتجاه متجه العدد المركب في المستوى."
    },
    "math-u1-l5": {
      "id": "math-u1-l5",
      "title": "الصيغة القطبية للعدد المركب",
      "original_text": "من كتاب الطالب، الصفحات 33 إلى 39: الصيغة القطبية للعدد المركب.",
      "levels": {
        "basic": "📌 الصيغة القطبية للعدد المركب: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 تكتب الصيغة القطبية العدد المركب باستخدام الطول r والزاوية θ. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 الصيغة القطبية تبسّط الضرب والقسمة والرفع إلى قوة."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "z = r(cos θ + i sin θ)"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "z = r(cos θ + i sin θ)"
        }
      ],
      "tts_text": "الصيغة القطبية للعدد المركب. تكتب الصيغة القطبية العدد المركب باستخدام الطول r والزاوية θ."
    },
    "math-u1-l6": {
      "id": "math-u1-l6",
      "title": "التحويل بين الصيغتين الجبرية والقطبية",
      "original_text": "من كتاب الطالب، الصفحات 40 إلى 44: التحويل بين الصيغتين الجبرية والقطبية.",
      "levels": {
        "basic": "📌 التحويل بين الصيغتين الجبرية والقطبية: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 نحول من الجبرية للقطبية بحساب r وθ، وبالعكس بالإسقاطات. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 التمثيل الهندسي يفسر لماذا يتضاعف الطول ويُجمع θ عند الضرب."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "a = r cos θ، b = r sin θ"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "a = r cos θ، b = r sin θ"
        }
      ],
      "tts_text": "التحويل بين الصيغتين الجبرية والقطبية. نحول من الجبرية للقطبية بحساب r وθ، وبالعكس بالإسقاطات."
    },
    "math-u2-l1": {
      "id": "math-u2-l1",
      "title": "مبرهنة دي موافر",
      "original_text": "من كتاب الطالب، الصفحات 45 إلى 48: مبرهنة دي موافر.",
      "levels": {
        "basic": "📌 مبرهنة دي موافر: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 تسمح المبرهنة برفع عدد مركب ذي قيمة مطلقة 1 إلى قوة n بسهولة. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 الصيغة العامة: zⁿ = rⁿ(cos nθ + i sin nθ)."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "(cos θ + i sin θ)ⁿ = cos nθ + i sin nθ"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "(cos θ + i sin θ)ⁿ = cos nθ + i sin nθ"
        }
      ],
      "tts_text": "مبرهنة دي موافر. تسمح المبرهنة برفع عدد مركب ذي قيمة مطلقة 1 إلى قوة n بسهولة."
    },
    "math-u2-l2": {
      "id": "math-u2-l2",
      "title": "الجذور النونية للعدد المركب",
      "original_text": "من كتاب الطالب، الصفحات 49 إلى 54: الجذور النونية للعدد المركب.",
      "levels": {
        "basic": "📌 الجذور النونية للعدد المركب: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 للعدد المركب n جذور نونية موزعة بالتساوي على دائرة نصف قطرها r^(1/n). اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 الفرق بين زواوي جذرين متجاورين هو 2π/n."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "wₖ = r^(1/n)[cos((θ+2kπ)/n) + i sin((θ+2kπ)/n)]"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "wₖ = r^(1/n)[cos((θ+2kπ)/n) + i sin((θ+2kπ)/n)]"
        }
      ],
      "tts_text": "الجذور النونية للعدد المركب. للعدد المركب n جذور نونية موزعة بالتساوي على دائرة نصف قطرها r^(1/n)."
    },
    "math-u2-l3": {
      "id": "math-u2-l3",
      "title": "التوسعة ذات الحدين",
      "original_text": "من كتاب الطالب، الصفحات 55 إلى 64: التوسعة ذات الحدين.",
      "levels": {
        "basic": "📌 التوسعة ذات الحدين: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 معاملات التوسعة هي معاملات مثلث باسكال أو C(n,k). اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 عدد الحدود في التوسعة هو n + 1."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "(a+b)ⁿ = Σ C(n,k)aⁿ⁻ᵏbᵏ"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "(a+b)ⁿ = Σ C(n,k)aⁿ⁻ᵏbᵏ"
        }
      ],
      "tts_text": "التوسعة ذات الحدين. معاملات التوسعة هي معاملات مثلث باسكال أو C(n,k)."
    },
    "math-u2-l4": {
      "id": "math-u2-l4",
      "title": "تطبيقات دي موافر والتوسعة",
      "original_text": "من كتاب الطالب، الصفحات 65 إلى 73: تطبيقات دي موافر والتوسعة.",
      "levels": {
        "basic": "📌 تطبيقات دي موافر والتوسعة: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 تستخدم المبرهنة لإيجاد علاقات مثلية وتبسيط قوى الأعداد المركبة. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 ربط الجزء الحقيقي والجزء التخيلي يعطي متطابقات جيبية."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "cos nθ + i sin nθ = (cos θ + i sin θ)ⁿ"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "cos nθ + i sin nθ = (cos θ + i sin θ)ⁿ"
        }
      ],
      "tts_text": "تطبيقات دي موافر والتوسعة. تستخدم المبرهنة لإيجاد علاقات مثلية وتبسيط قوى الأعداد المركبة."
    },
    "math-u3-l1": {
      "id": "math-u3-l1",
      "title": "التعريف العام للقطع المخروطي",
      "original_text": "من كتاب الطالب، الصفحات 104 إلى 109: التعريف العام للقطع المخروطي.",
      "levels": {
        "basic": "📌 التعريف العام للقطع المخروطي: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 القطع المخروطي مجموعة نقاط تتغير نسبة بعدها عن بؤرة إلى بعدها عن دليل ثابتاً. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 نوع القطع يحدد في e: ناقص e<1، مكافئ e=1، زائد e>1."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "e = PF / PD"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "e = PF / PD"
        }
      ],
      "tts_text": "التعريف العام للقطع المخروطي. القطع المخروطي مجموعة نقاط تتغير نسبة بعدها عن بؤرة إلى بعدها عن دليل ثابتاً."
    },
    "math-u3-l2": {
      "id": "math-u3-l2",
      "title": "القطع الناقص",
      "original_text": "من كتاب الطالب، الصفحات 110 إلى 117: القطع الناقص.",
      "levels": {
        "basic": "📌 القطع الناقص: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 القطع الناقص مجموعة نقاط مجموع بعديها عن بؤرتين ثابتاً. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 مجموع البعدين = 2a، والبؤرتان على المحور الكبير."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "x²/a² + y²/b² = 1"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "x²/a² + y²/b² = 1"
        }
      ],
      "tts_text": "القطع الناقص. القطع الناقص مجموعة نقاط مجموع بعديها عن بؤرتين ثابتاً."
    },
    "math-u3-l3": {
      "id": "math-u3-l3",
      "title": "القطع الزائد",
      "original_text": "من كتاب الطالب، الصفحات 118 إلى 123: القطع الزائد.",
      "levels": {
        "basic": "📌 القطع الزائد: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 القطع الزائد مجموعة نقاط الفرق المطلق لبعديها عن بؤرتين ثابتاً. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 الفرق المطلق = 2a، وله خطان مقاربان."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "x²/a² − y²/b² = 1"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "x²/a² − y²/b² = 1"
        }
      ],
      "tts_text": "القطع الزائد. القطع الزائد مجموعة نقاط الفرق المطلق لبعديها عن بؤرتين ثابتاً."
    },
    "math-u3-l4": {
      "id": "math-u3-l4",
      "title": "القطع المكافئ",
      "original_text": "من كتاب الطالب، الصفحات 124 إلى 129: القطع المكافئ.",
      "levels": {
        "basic": "📌 القطع المكافئ: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 القطع المكافئ مجموعة نقاط متساوية البعد عن بؤرة ودليل. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 محور التماثل هو محور x، والبؤرة (p، 0)."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "y² = 4px"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "y² = 4px"
        }
      ],
      "tts_text": "القطع المكافئ. القطع المكافئ مجموعة نقاط متساوية البعد عن بؤرة ودليل."
    },
    "math-u3-l5": {
      "id": "math-u3-l5",
      "title": "تطبيقات القطوع المخروطية",
      "original_text": "من كتاب الطالب، الصفحات 130 إلى 132: تطبيقات القطوع المخروطية.",
      "levels": {
        "basic": "📌 تطبيقات القطوع المخروطية: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 تستخدم القطوع في المدارات والهوائيات والأنفاق. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 اختيار القطع المناسب يعتمد على قيمة الانحراف e."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "e = c/a"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "e = c/a"
        }
      ],
      "tts_text": "تطبيقات القطوع المخروطية. تستخدم القطوع في المدارات والهوائيات والأنفاق."
    },
    "math-u4-l1": {
      "id": "math-u4-l1",
      "title": "المستقيم والمستوى في الفراغ",
      "original_text": "من كتاب الطالب، الصفحات 133 إلى 141: المستقيم والمستوى في الفراغ.",
      "levels": {
        "basic": "📌 المستقيم والمستوى في الفراغ: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 يُمثّل المستوى في الفراغ بمعادلة خطية ويُمثّل المستقيم بمتجه اتجاه. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 المتجه الطبيعي للمستوى هو (A، B، C)."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "Ax + By + Cz + D = 0"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "Ax + By + Cz + D = 0"
        }
      ],
      "tts_text": "المستقيم والمستوى في الفراغ. يُمثّل المستوى في الفراغ بمعادلة خطية ويُمثّل المستقيم بمتجه اتجاه."
    },
    "math-u4-l2": {
      "id": "math-u4-l2",
      "title": "الزاوية بين مستقيم ومستوى",
      "original_text": "من كتاب الطالب، الصفحات 142 إلى 146: الزاوية بين مستقيم ومستوى.",
      "levels": {
        "basic": "📌 الزاوية بين مستقيم ومستوى: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 تقاس الزاوية بين مستقيم ومستوى باستخدام متجه الاتجاه والمتجه الطبيعي. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 الزاوية بين المستقيم والمتجه الطبيعي مكمّلة للزاوية المطلوبة."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "sin θ = |u·n| / (|u||n|)"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "sin θ = |u·n| / (|u||n|)"
        }
      ],
      "tts_text": "الزاوية بين مستقيم ومستوى. تقاس الزاوية بين مستقيم ومستوى باستخدام متجه الاتجاه والمتجه الطبيعي."
    },
    "math-u4-l3": {
      "id": "math-u4-l3",
      "title": "الزاوية بين مستويين والمسافة في الفراغ",
      "original_text": "من كتاب الطالب، الصفحات 147 إلى 153: الزاوية بين مستويين والمسافة في الفراغ.",
      "levels": {
        "basic": "📌 الزاوية بين مستويين والمسافة في الفراغ: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 توجد الزاوية بين مستويين من زاوية متجهيهما الطبيعيين. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 مسافة نقطة من مستوى تقاس بالإسقاط العمودي."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "cos φ = |n₁·n₂| / (|n₁||n₂|)"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "cos φ = |n₁·n₂| / (|n₁||n₂|)"
        }
      ],
      "tts_text": "الزاوية بين مستويين والمسافة في الفراغ. توجد الزاوية بين مستويين من زاوية متجهيهما الطبيعيين."
    },
    "math-u5-l1": {
      "id": "math-u5-l1",
      "title": "التجارب العشوائية والاحتمال",
      "original_text": "من كتاب الطالب، الصفحات 74 إلى 78: التجارب العشوائية والاحتمال.",
      "levels": {
        "basic": "📌 التجارب العشوائية والاحتمال: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 الاحتمال مقياس لحدوث حدث داخل فضاء عيني من نتجات متساوية الاحتمال غالباً. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 مجموع احتمالات كل النتجات الممكنة المتنافية = 1."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "0 ≤ P(A) ≤ 1"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "0 ≤ P(A) ≤ 1"
        }
      ],
      "tts_text": "التجارب العشوائية والاحتمال. الاحتمال مقياس لحدوث حدث داخل فضاء عيني من نتجات متساوية الاحتمال غالباً."
    },
    "math-u5-l2": {
      "id": "math-u5-l2",
      "title": "قاعدتا الجمع والضرب",
      "original_text": "من كتاب الطالب، الصفحات 79 إلى 85: قاعدتا الجمع والضرب.",
      "levels": {
        "basic": "📌 قاعدتا الجمع والضرب: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 تُستخدم قاعدة الجمع للأحداث وقاعدة الضرب للأحداث المستقلة أو الشرطية. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 إذا كان الحدثان متنافيين فإن P(A∩B)=0."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "P(A∪B)=P(A)+P(B)−P(A∩B)"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "P(A∪B)=P(A)+P(B)−P(A∩B)"
        }
      ],
      "tts_text": "قاعدتا الجمع والضرب. تُستخدم قاعدة الجمع للأحداث وقاعدة الضرب للأحداث المستقلة أو الشرطية."
    },
    "math-u5-l3": {
      "id": "math-u5-l3",
      "title": "الاحتمال الشرطي والاستقلال",
      "original_text": "من كتاب الطالب، الصفحات 86 إلى 92: الاحتمال الشرطي والاستقلال.",
      "levels": {
        "basic": "📌 الاحتمال الشرطي والاستقلال: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 الاحتمال الشرطي يضيّق فضاء العينة إلى الحدث B. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 الاستقلال يعني P(A|B)=P(A)."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "P(A|B)=P(A∩B)/P(B)، P(B)>0"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "P(A|B)=P(A∩B)/P(B)، P(B)>0"
        }
      ],
      "tts_text": "الاحتمال الشرطي والاستقلال. الاحتمال الشرطي يضيّق فضاء العينة إلى الحدث B."
    },
    "math-u5-l4": {
      "id": "math-u5-l4",
      "title": "الاحتمال ذو الحدين",
      "original_text": "من كتاب الطالب، الصفحات 93 إلى 97: الاحتمال ذو الحدين.",
      "levels": {
        "basic": "📌 الاحتمال ذو الحدين: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 نموذج برنولي يتكرر n مرة بنجاح احتماله p في كل مرة. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 مجموع الاحتمالات لكل k من 0 إلى n يساوي 1."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "P(X=k)=C(n,k)pᵏ(1−p)ⁿ⁻ᵏ"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "P(X=k)=C(n,k)pᵏ(1−p)ⁿ⁻ᵏ"
        }
      ],
      "tts_text": "الاحتمال ذو الحدين. نموذج برنولي يتكرر n مرة بنجاح احتماله p في كل مرة."
    },
    "math-u5-l5": {
      "id": "math-u5-l5",
      "title": "تطبيقات الاحتمالات",
      "original_text": "من كتاب الطالب، الصفحات 98 إلى 103: تطبيقات الاحتمالات.",
      "levels": {
        "basic": "📌 تطبيقات الاحتمالات: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 تطبيق القواعد على مسائل القرعة والجودة والاختبارات. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 غالباً أسهل حساب احتمال المكمّل ثم طرحه من 1."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "P(Aᶜ)=1−P(A)"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "P(Aᶜ)=1−P(A)"
        }
      ],
      "tts_text": "تطبيقات الاحتمالات. تطبيق القواعد على مسائل القرعة والجودة والاختبارات."
    },
    "math-u6-l1": {
      "id": "math-u6-l1",
      "title": "مفهوم المشتقة وميل المماس",
      "original_text": "من كتاب الطالب، الصفحات 154 إلى 159: مفهوم المشتقة وميل المماس.",
      "levels": {
        "basic": "📌 مفهوم المشتقة وميل المماس: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 المشتقة هي معدل التغير اللحظي وميل المماس للمنحنى. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 وجود النهاية يعني قابلية الدالة للاشتقاق عند النقطة."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "f′(x)=limₕ→₀[f(x+h)−f(x)]/h"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "f′(x)=limₕ→₀[f(x+h)−f(x)]/h"
        }
      ],
      "tts_text": "مفهوم المشتقة وميل المماس. المشتقة هي معدل التغير اللحظي وميل المماس للمنحنى."
    },
    "math-u6-l2": {
      "id": "math-u6-l2",
      "title": "قواعد الاشتقاق الأساسية",
      "original_text": "من كتاب الطالب، الصفحات 160 إلى 165: قواعد الاشتقاق الأساسية.",
      "levels": {
        "basic": "📌 قواعد الاشتقاق الأساسية: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 تُشتق الدوال الجبرية بقواعد القوة والجداء والقسمة والمجموع. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 مشتقة الثابت صفر ومشتقة kx هي k."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "(xⁿ)′=nxⁿ⁻¹، (uv)′=u′v+uv′"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "(xⁿ)′=nxⁿ⁻¹، (uv)′=u′v+uv′"
        }
      ],
      "tts_text": "قواعد الاشتقاق الأساسية. تُشتق الدوال الجبرية بقواعد القوة والجداء والقسمة والمجموع."
    },
    "math-u6-l3": {
      "id": "math-u6-l3",
      "title": "مشتقة الدالة المركبة",
      "original_text": "من كتاب الطالب، الصفحات 166 إلى 170: مشتقة الدالة المركبة.",
      "levels": {
        "basic": "📌 مشتقة الدالة المركبة: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 تُشتق الدالة المركبة من الخارج إلى الداخل مع الضرب بمشتقة الداخل. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 تسمى أيضاً قاعدة السلسلة."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "(f∘g)′(x)=f′(g(x))g′(x)"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "(f∘g)′(x)=f′(g(x))g′(x)"
        }
      ],
      "tts_text": "مشتقة الدالة المركبة. تُشتق الدالة المركبة من الخارج إلى الداخل مع الضرب بمشتقة الداخل."
    },
    "math-u6-l4": {
      "id": "math-u6-l4",
      "title": "اشتقاق الدوال الجبرية",
      "original_text": "من كتاب الطالب، الصفحات 171 إلى 174: اشتقاق الدوال الجبرية.",
      "levels": {
        "basic": "📌 اشتقاق الدوال الجبرية: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 تكتب الدوال الجبرية بصورة قوى ثم تطبق قاعدة القوة. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 التحويل إلى صورة xⁿ يوحّد معالجة الجذور والمقامات."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "(√x)′=1/(2√x)، (1/x)′=−1/x²"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "(√x)′=1/(2√x)، (1/x)′=−1/x²"
        }
      ],
      "tts_text": "اشتقاق الدوال الجبرية. تكتب الدوال الجبرية بصورة قوى ثم تطبق قاعدة القوة."
    },
    "math-u6-l5": {
      "id": "math-u6-l5",
      "title": "التطبيقات الهندسية للمشتقة",
      "original_text": "من كتاب الطالب، الصفحات 175 إلى 182: التطبيقات الهندسية للمشتقة.",
      "levels": {
        "basic": "📌 التطبيقات الهندسية للمشتقة: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 تستخدم المشتقة لإيجاد مماس ومنحنى وحل مسائل الحركة. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 السرعة هي مشتقة الموضع بالنسبة للزمن."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "y−y₀=f′(x₀)(x−x₀)"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "y−y₀=f′(x₀)(x−x₀)"
        }
      ],
      "tts_text": "التطبيقات الهندسية للمشتقة. تستخدم المشتقة لإيجاد مماس ومنحنى وحل مسائل الحركة."
    },
    "math-u6-l6": {
      "id": "math-u6-l6",
      "title": "المشتقات الأعلى",
      "original_text": "من كتاب الطالب، الصفحات 183 إلى 186: المشتقات الأعلى.",
      "levels": {
        "basic": "📌 المشتقات الأعلى: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 المشتقة الثانية تصف تغير المشتقة الأولى وتساعد في التقرير. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 f″>0 يعني تقعراً للأعلى و f″<0 يعني تحدباً."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "f″(x)=(f′(x))′"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "f″(x)=(f′(x))′"
        }
      ],
      "tts_text": "المشتقات الأعلى. المشتقة الثانية تصف تغير المشتقة الأولى وتساعد في التقرير."
    },
    "math-u6-l7": {
      "id": "math-u6-l7",
      "title": "القيم القصوى والتقرير",
      "original_text": "من كتاب الطالب، الصفحات 187 إلى 199: القيم القصوى والتقرير.",
      "levels": {
        "basic": "📌 القيم القصوى والتقرير: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 توجد النقاط الحرجة ثم يحدد نوعها باختبار المشتقة الأولى أو الثانية. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 يجب فحص طرفي الفترة في مسائل القيم القصوى المغلقة."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "f′(c)=0 شرط لازم للقيمة القصوى الداخلية"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "f′(c)=0 شرط لازم للقيمة القصوى الداخلية"
        }
      ],
      "tts_text": "القيم القصوى والتقرير. توجد النقاط الحرجة ثم يحدد نوعها باختبار المشتقة الأولى أو الثانية."
    },
    "math-u6-l8": {
      "id": "math-u6-l8",
      "title": "نظريتا رول والقيمة المتوسطة",
      "original_text": "من كتاب الطالب، الصفحات 200 إلى 209: نظريتا رول والقيمة المتوسطة.",
      "levels": {
        "basic": "📌 نظريتا رول والقيمة المتوسطة: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 تضمن نظرية القيمة المتوسطة وجود نقطة ميلها يساوي ميل القطرة. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 رول حالة خاصة عندما f(a)=f(b)."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "f′(c)=[f(b)−f(a)]/(b−a)"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "f′(c)=[f(b)−f(a)]/(b−a)"
        }
      ],
      "tts_text": "نظريتا رول والقيمة المتوسطة. تضمن نظرية القيمة المتوسطة وجود نقطة ميلها يساوي ميل القطرة."
    },
    "math-u7-l1": {
      "id": "math-u7-l1",
      "title": "التكامل غير المحدد",
      "original_text": "من كتاب الطالب، الصفحات 210 إلى 221: التكامل غير المحدد.",
      "levels": {
        "basic": "📌 التكامل غير المحدد: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 التكامل غير المحدد يعكس الاشتقاق ويُنتج عائلة دوال. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 ثابت التكامل C يختفي عند الاشتقاق."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "∫xⁿdx=xⁿ⁺¹/(n+1)+C، n≠−1"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "∫xⁿdx=xⁿ⁺¹/(n+1)+C، n≠−1"
        }
      ],
      "tts_text": "التكامل غير المحدد. التكامل غير المحدد يعكس الاشتقاق ويُنتج عائلة دوال."
    },
    "math-u7-l2": {
      "id": "math-u7-l2",
      "title": "طرق التكامل",
      "original_text": "من كتاب الطالب، الصفحات 222 إلى 234: طرق التكامل.",
      "levels": {
        "basic": "📌 طرق التكامل: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 تستخدم خطية التكامل والتعويض لتبسيط المسائل. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 التعويض يختار عادة دالة داخلية مشتقتها موجودة في التكامل."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "∫(u±v)dx=∫udx±∫vdx"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "∫(u±v)dx=∫udx±∫vdx"
        }
      ],
      "tts_text": "طرق التكامل. تستخدم خطية التكامل والتعويض لتبسيط المسائل."
    },
    "math-u7-l3": {
      "id": "math-u7-l3",
      "title": "التكامل المحدد",
      "original_text": "من كتاب الطالب، الصفحات 235 إلى 239: التكامل المحدد.",
      "levels": {
        "basic": "📌 التكامل المحدد: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 التكامل المحدد يعطي قيمة عددية باستخدام مبدأ Newton-Leibniz. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 لا يحتاج ثابت التكامل لأنه يُلغى عند الطرح."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "∫ₐᵇf(x)dx=F(b)−F(a)"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "∫ₐᵇf(x)dx=F(b)−F(a)"
        }
      ],
      "tts_text": "التكامل المحدد. التكامل المحدد يعطي قيمة عددية باستخدام مبدأ Newton-Leibniz."
    },
    "math-u7-l4": {
      "id": "math-u7-l4",
      "title": "خصائص التكامل المحدد",
      "original_text": "من كتاب الطالب، الصفحات 240 إلى 243: خصائص التكامل المحدد.",
      "levels": {
        "basic": "📌 خصائص التكامل المحدد: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 من خصائصها الجمعية وتبديل الحدود وتماثل الدوال. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 تكامل دالة فردية على فترة متماثلة حول الصفر يساوي صفراً."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "∫ₐᵇf(x)dx=−∫ᵇₐf(x)dx"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "∫ₐᵇf(x)dx=−∫ᵇₐf(x)dx"
        }
      ],
      "tts_text": "خصائص التكامل المحدد. من خصائصها الجمعية وتبديل الحدود وتماثل الدوال."
    },
    "math-u7-l5": {
      "id": "math-u7-l5",
      "title": "المساحة تحت المنحنى",
      "original_text": "من كتاب الطالب، الصفحات 244 إلى 247: المساحة تحت المنحنى.",
      "levels": {
        "basic": "📌 المساحة تحت المنحنى: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 المساحة المحصورة بين المنحنى ومحور x تُقاس بالتكامل المحدد. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 إذا كان المنحنى سالباً نأخذ القيمة المطلقة أو نعكس الإشارة."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "A=∫ₐᵇ|f(x)|dx"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "A=∫ₐᵇ|f(x)|dx"
        }
      ],
      "tts_text": "المساحة تحت المنحنى. المساحة المحصورة بين المنحنى ومحور x تُقاس بالتكامل المحدد."
    },
    "math-u7-l6": {
      "id": "math-u7-l6",
      "title": "حجم مجسم الدوران",
      "original_text": "من كتاب الطالب، الصفحات 248 إلى 251: حجم مجسم الدوران.",
      "levels": {
        "basic": "📌 حجم مجسم الدوران: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 يدور المنحنى حول محور x فينتج مجسم يمكن حساب حجمه بالأقراص. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 كل قرص نصف قطره f(x) وسمكه dx."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "V=π∫ₐᵇ[f(x)]²dx"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "V=π∫ₐᵇ[f(x)]²dx"
        }
      ],
      "tts_text": "حجم مجسم الدوران. يدور المنحنى حول محور x فينتج مجسم يمكن حساب حجمه بالأقراص."
    },
    "math-u7-l7": {
      "id": "math-u7-l7",
      "title": "تطبيقات التكامل",
      "original_text": "من كتاب الطالب، الصفحات 252 إلى 256: تطبيقات التكامل.",
      "levels": {
        "basic": "📌 تطبيقات التكامل: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
        "intermediate": "📘 يستخدم التكامل في حساب المساحات والحجوم والشغل. اكتب الصيغة المناسبة ثم عوّض بوضوح.",
        "advanced": "🚀 الربط بين المشتقة والتكامل هو جوهر التحليل."
      },
      "chemical_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "W=∫ₐᵇF(x)dx"
        }
      ],
      "math_equations": [
        {
          "label": "الصيغة المرتبطة",
          "eq": "W=∫ₐᵇF(x)dx"
        }
      ],
      "tts_text": "تطبيقات التكامل. يستخدم التكامل في حساب المساحات والحجوم والشغل."
    }
  },
  "diagrams": {
    "diag-math-complex": {
      "id": "diag-math-complex",
      "lab_exp": "lab-math-complex",
      "title": "مستوى أرغاند والعدد المركب",
      "sim_key": "math_complex",
      "formula": "z = a + bi، |z| = √(a²+b²)",
      "slider_label": "زاوية العدد المركب:",
      "slider_min": 0,
      "slider_max": 360,
      "slider_val": 45,
      "slider_unit": "°",
      "components": [
        {
          "id": "real",
          "name": "المحور الحقيقي",
          "role": "يمثل الجزء الحقيقي a."
        },
        {
          "id": "imag",
          "name": "المحور التخيلي",
          "role": "يمثل الجزء التخيلي b."
        },
        {
          "id": "point",
          "name": "النقطة z",
          "role": "تتحرك بدلالة الزاوية، وطولها هو القيمة المطلقة."
        }
      ]
    },
    "diag-math-cone": {
      "id": "diag-math-cone",
      "lab_exp": "lab-math-cone",
      "title": "القطوع الناتجة من قطع المخروط",
      "sim_key": "math_cone_sections",
      "formula": "e = PF / PD",
      "slider_label": "ميل مستوى القطع:",
      "slider_min": 0,
      "slider_max": 90,
      "slider_val": 35,
      "slider_unit": "°",
      "components": [
        {
          "id": "cone",
          "name": "المخروط",
          "role": "السطح الذي يُقطع بمستوى."
        },
        {
          "id": "plane",
          "name": "مستوى القطع",
          "role": "ميله يحدد نوع القطع."
        },
        {
          "id": "curve",
          "name": "منحنى القطع",
          "role": "ناقص أو مكافئ أو زائد حسب زاوية المستوى."
        }
      ]
    },
    "diag-math-ellipse": {
      "id": "diag-math-ellipse",
      "lab_exp": "lab-math-ellipse",
      "title": "القطع الناقص وبؤرتاه",
      "sim_key": "math_ellipse",
      "formula": "x²/a² + y²/b² = 1",
      "slider_label": "الانحراف e:",
      "slider_min": 10,
      "slider_max": 90,
      "slider_val": 55,
      "slider_unit": "%",
      "components": [
        {
          "id": "f1",
          "name": "البؤرة الأولى",
          "role": "أحد نقطتي تعريف القطع الناقص."
        },
        {
          "id": "f2",
          "name": "البؤرة الثانية",
          "role": "مجموع البعدين عن البؤرتين يساوي 2a."
        },
        {
          "id": "curve",
          "name": "المنحنى",
          "role": "يصبح دائرة عندما يقترب الانحراف من الصفر."
        }
      ]
    },
    "diag-math-hyperbola": {
      "id": "diag-math-hyperbola",
      "lab_exp": "lab-math-hyperbola",
      "title": "القطع الزائد وخطاه المقاربان",
      "sim_key": "math_hyperbola",
      "formula": "x²/a² − y²/b² = 1",
      "slider_label": "المعلمة a:",
      "slider_min": 1,
      "slider_max": 5,
      "slider_val": 2,
      "slider_unit": "",
      "components": [
        {
          "id": "branches",
          "name": "الفرعان",
          "role": "ينفصلان على جانبي المحورين."
        },
        {
          "id": "asymptote",
          "name": "الخطان المقاربان",
          "role": "يقترب منهما المنحنى دون أن يلمسهما."
        }
      ]
    },
    "diag-math-parabola": {
      "id": "diag-math-parabola",
      "lab_exp": "lab-math-parabola",
      "title": "القطع المكافئ والبؤرة والدليل",
      "sim_key": "math_parabola",
      "formula": "y² = 4px",
      "slider_label": "المعلمة p:",
      "slider_min": 1,
      "slider_max": 6,
      "slider_val": 3,
      "slider_unit": "",
      "components": [
        {
          "id": "focus",
          "name": "البؤرة",
          "role": "النقطة (p، 0)."
        },
        {
          "id": "directrix",
          "name": "الدليل",
          "role": "المستقيم x = −p."
        },
        {
          "id": "curve",
          "name": "المنحنى",
          "role": "كل نقطة عليه متساوية البعد عن البؤرة والدليل."
        }
      ]
    },
    "diag-math-space": {
      "id": "diag-math-space",
      "lab_exp": "lab-math-space",
      "title": "القطر الفراغي للمكعب",
      "sim_key": "math_3d_pythagoras",
      "formula": "d = a√3",
      "slider_label": "طول ضلع المكعب:",
      "slider_min": 1,
      "slider_max": 5,
      "slider_val": 3,
      "slider_unit": " وحدة",
      "components": [
        {
          "id": "cube",
          "name": "المكعب",
          "role": "نموذج ثلاثي الأبعاد يمكن دورانه."
        },
        {
          "id": "diagonal",
          "name": "القطر الفراغي",
          "role": "يصل بين رأسين متقابلين وطوله a√3."
        }
      ]
    },
    "diag-math-line-plane": {
      "id": "diag-math-line-plane",
      "lab_exp": "lab-math-line-plane",
      "title": "الزاوية بين مستقيم ومستوى",
      "sim_key": "math_line_plane",
      "formula": "sin θ = |u·n|/(|u||n|)",
      "slider_label": "زاوية المستقيم:",
      "slider_min": 0,
      "slider_max": 90,
      "slider_val": 35,
      "slider_unit": "°",
      "components": [
        {
          "id": "plane",
          "name": "المستوى",
          "role": "سطح أفقي يمثل المعادلة Ax+By+Cz+D=0."
        },
        {
          "id": "line",
          "name": "المستقيم",
          "role": "اتجاهه u يحدد الزاوية مع المستوى."
        },
        {
          "id": "normal",
          "name": "المتجه الطبيعي",
          "role": "العمود على المستوى."
        }
      ]
    },
    "diag-math-dihedral": {
      "id": "diag-math-dihedral",
      "lab_exp": "lab-math-dihedral",
      "title": "الزاوية بين مستويين",
      "sim_key": "math_dihedral",
      "formula": "cos φ = |n₁·n₂|/(|n₁||n₂|)",
      "slider_label": "زاوية المستوى الثاني:",
      "slider_min": 0,
      "slider_max": 120,
      "slider_val": 60,
      "slider_unit": "°",
      "components": [
        {
          "id": "plane1",
          "name": "المستوى الأول",
          "role": "متجهه الطبيعي n₁."
        },
        {
          "id": "plane2",
          "name": "المستوى الثاني",
          "role": "متجهه الطبيعي n₂."
        },
        {
          "id": "edge",
          "name": "خط التقاطع",
          "role": "منه تُقاس الزاوية ثنائية الوجه."
        }
      ]
    },
    "diag-math-probability": {
      "id": "diag-math-probability",
      "lab_exp": "lab-math-probability",
      "title": "فضاء العينة والاحتمالات",
      "sim_key": "math_probability_space",
      "formula": "P(A∪B)=P(A)+P(B)−P(A∩B)",
      "slider_label": "احتمال الحدث A:",
      "slider_min": 0,
      "slider_max": 100,
      "slider_val": 55,
      "slider_unit": "%",
      "components": [
        {
          "id": "space",
          "name": "فضاء العينة",
          "role": "كل النتجات الممكنة."
        },
        {
          "id": "eventA",
          "name": "الحدث A",
          "role": "مجموعة نتجات جزئية."
        },
        {
          "id": "eventB",
          "name": "الحدث B",
          "role": "يتداخل مع A في بعض المسائل."
        }
      ]
    },
    "diag-math-derivative": {
      "id": "diag-math-derivative",
      "lab_exp": "lab-math-derivative",
      "title": "مماس المنحنى والمشتقة",
      "sim_key": "math_derivative",
      "formula": "f′(x)=lim[f(x+h)−f(x)]/h",
      "slider_label": "موضع نقطة المماس:",
      "slider_min": 1,
      "slider_max": 9,
      "slider_val": 4,
      "slider_unit": "",
      "components": [
        {
          "id": "curve",
          "name": "المنحنى",
          "role": "الدالة f(x)."
        },
        {
          "id": "tangent",
          "name": "المماس",
          "role": "ميله يساوي f′(x)."
        }
      ]
    },
    "diag-math-integral": {
      "id": "diag-math-integral",
      "lab_exp": "lab-math-integral",
      "title": "التكامل والمساحة تحت المنحنى",
      "sim_key": "math_integral",
      "formula": "∫ₐᵇf(x)dx=F(b)−F(a)",
      "slider_label": "حد التكامل العلوي:",
      "slider_min": 1,
      "slider_max": 10,
      "slider_val": 6,
      "slider_unit": "",
      "components": [
        {
          "id": "area",
          "name": "المساحة",
          "role": "تتراكم تحت المنحنى."
        },
        {
          "id": "curve",
          "name": "الدالة",
          "role": "حدود التكامل تحدد الفترة."
        }
      ]
    },
    "diag-math-area": {
      "id": "diag-math-area",
      "lab_exp": "lab-math-area",
      "title": "المساحة بين منحنيين",
      "sim_key": "math_area_between",
      "formula": "A=∫ₐᵇ|f(x)−g(x)|dx",
      "slider_label": "الحد العلوي:",
      "slider_min": 1,
      "slider_max": 10,
      "slider_val": 5,
      "slider_unit": "",
      "components": [
        {
          "id": "upper",
          "name": "المنحنى العلوي",
          "role": "f(x)."
        },
        {
          "id": "lower",
          "name": "المنحنى السفلي",
          "role": "g(x)."
        }
      ]
    },
    "diag-math-revolution": {
      "id": "diag-math-revolution",
      "lab_exp": "lab-math-revolution",
      "title": "حجم مجسم الدوران",
      "sim_key": "math_revolution",
      "formula": "V=π∫ₐᵇ[f(x)]²dx",
      "slider_label": "عدد الأقراص:",
      "slider_min": 4,
      "slider_max": 20,
      "slider_val": 10,
      "slider_unit": "",
      "components": [
        {
          "id": "discs",
          "name": "الأقراص",
          "role": "نصف القطر f(x) والسمك dx."
        },
        {
          "id": "axis",
          "name": "محور الدوران",
          "role": "محور x غالباً."
        }
      ]
    }
  },
  "activities": {
    "act-math-complex-add": {
      "id": "act-math-complex-add",
      "title": "جمع الأعداد المركبة",
      "unit_id": "u1",
      "book_page": 13,
      "sim_type": "math_complex_add",
      "description": "غيّر المكوّنات الحقيقية والتخيلية ولاحظ نتيجة الجمع في مستوى أرغاند.",
      "controls": [
        {
          "id": "a",
          "label": "الجزء الحقيقي z₁",
          "min": -5,
          "max": 5,
          "step": 1,
          "default": 2
        },
        {
          "id": "b",
          "label": "الجزء التخيلي z₁",
          "min": -5,
          "max": 5,
          "step": 1,
          "default": 3
        },
        {
          "id": "c",
          "label": "الجزء الحقيقي z₂",
          "min": -5,
          "max": 5,
          "step": 1,
          "default": -1
        },
        {
          "id": "d",
          "label": "الجزء التخيلي z₂",
          "min": -5,
          "max": 5,
          "step": 1,
          "default": 2
        }
      ]
    },
    "act-math-complex-modulus": {
      "id": "act-math-complex-modulus",
      "title": "القيمة المطلقة والسعة",
      "unit_id": "u1",
      "book_page": 19,
      "sim_type": "math_complex_modulus",
      "description": "احسب طول متجه العدد المركب من مكوّناته.",
      "controls": [
        {
          "id": "a",
          "label": "الجزء الحقيقي a",
          "min": -6,
          "max": 6,
          "step": 1,
          "default": 3
        },
        {
          "id": "b",
          "label": "الجزء التخيلي b",
          "min": -6,
          "max": 6,
          "step": 1,
          "default": 4
        }
      ]
    },
    "act-math-polar": {
      "id": "act-math-polar",
      "title": "التحويل إلى الصيغة القطبية",
      "unit_id": "u1",
      "book_page": 38,
      "sim_type": "math_polar",
      "description": "حرك الطول r والزاوية θ ولاحظ الإحداثيات الجبرية.",
      "controls": [
        {
          "id": "r",
          "label": "القيمة المطلقة r",
          "min": 1,
          "max": 10,
          "step": 1,
          "default": 5
        },
        {
          "id": "theta",
          "label": "الزاوية θ",
          "min": 0,
          "max": 360,
          "step": 5,
          "default": 60
        }
      ]
    },
    "act-math-demoivre": {
      "id": "act-math-demoivre",
      "title": "مبرهنة دي موافر",
      "unit_id": "u2",
      "book_page": 46,
      "sim_type": "math_de_moivre",
      "description": "ارفع العدد المركب إلى القوة n ولاحظ تضاعف الطول والزاوية.",
      "controls": [
        {
          "id": "r",
          "label": "القيمة المطلقة r",
          "min": 1,
          "max": 4,
          "step": 1,
          "default": 2
        },
        {
          "id": "theta",
          "label": "الزاوية θ",
          "min": 0,
          "max": 120,
          "step": 5,
          "default": 30
        },
        {
          "id": "n",
          "label": "القوة n",
          "min": 1,
          "max": 8,
          "step": 1,
          "default": 3
        }
      ]
    },
    "act-math-roots": {
      "id": "act-math-roots",
      "title": "الجذور النونية للعدد المركب",
      "unit_id": "u2",
      "book_page": 52,
      "sim_type": "math_roots",
      "description": "اعرض الجذور النونية موزعة على دائرة نصف قطرها r^(1/n).",
      "controls": [
        {
          "id": "r",
          "label": "القيمة المطلقة r",
          "min": 1,
          "max": 16,
          "step": 1,
          "default": 8
        },
        {
          "id": "theta",
          "label": "زاوية العدد θ",
          "min": 0,
          "max": 360,
          "step": 15,
          "default": 60
        },
        {
          "id": "n",
          "label": "درجة الجذر n",
          "min": 2,
          "max": 8,
          "step": 1,
          "default": 3
        }
      ]
    },
    "act-math-binomial": {
      "id": "act-math-binomial",
      "title": "التوسعة ذات الحدين",
      "unit_id": "u2",
      "book_page": 58,
      "sim_type": "math_binomial",
      "description": "اختر n و k لحساب المعامل C(n,k) وحد التوسعة.",
      "controls": [
        {
          "id": "n",
          "label": "الأس n",
          "min": 2,
          "max": 12,
          "step": 1,
          "default": 6
        },
        {
          "id": "k",
          "label": "رقم الحد k",
          "min": 0,
          "max": 12,
          "step": 1,
          "default": 2
        }
      ]
    },
    "act-math-cone": {
      "id": "act-math-cone",
      "title": "قطع المخروط",
      "unit_id": "u3",
      "book_page": 106,
      "sim_type": "math_cone_sections",
      "description": "غيّر ميل مستوى القطع ولاحظ نوع القطع الناتج.",
      "controls": [
        {
          "id": "tilt",
          "label": "ميل مستوى القطع",
          "min": 0,
          "max": 90,
          "step": 5,
          "default": 35
        }
      ]
    },
    "act-math-ellipse": {
      "id": "act-math-ellipse",
      "title": "القطع الناقص",
      "unit_id": "u3",
      "book_page": 112,
      "sim_type": "math_ellipse_lab",
      "description": "غيّر a و b ولاحظ شكل القطع الناقص وبؤرتيه.",
      "controls": [
        {
          "id": "a",
          "label": "نصف المحور الكبير a",
          "min": 2,
          "max": 8,
          "step": 1,
          "default": 5
        },
        {
          "id": "b",
          "label": "نصف المحور الصغير b",
          "min": 1,
          "max": 7,
          "step": 1,
          "default": 3
        }
      ]
    },
    "act-math-hyperbola": {
      "id": "act-math-hyperbola",
      "title": "القطع الزائد",
      "unit_id": "u3",
      "book_page": 120,
      "sim_type": "math_hyperbola_lab",
      "description": "غيّر a و b ولاحظ الفروع والخطين المقاربين.",
      "controls": [
        {
          "id": "a",
          "label": "المعلمة a",
          "min": 1,
          "max": 6,
          "step": 1,
          "default": 2
        },
        {
          "id": "b",
          "label": "المعلمة b",
          "min": 1,
          "max": 6,
          "step": 1,
          "default": 3
        }
      ]
    },
    "act-math-parabola": {
      "id": "act-math-parabola",
      "title": "القطع المكافئ",
      "unit_id": "u3",
      "book_page": 126,
      "sim_type": "math_parabola_lab",
      "description": "غيّر p ولاحظ حركة البؤرة والدليل.",
      "controls": [
        {
          "id": "p",
          "label": "المعلمة p",
          "min": 1,
          "max": 6,
          "step": 1,
          "default": 2
        }
      ]
    },
    "act-math-space-diagonal": {
      "id": "act-math-space-diagonal",
      "title": "القطر الفراغي للمكعب",
      "unit_id": "u4",
      "book_page": 136,
      "sim_type": "math_space_diagonal",
      "description": "غيّر طول ضلع المكعب واحسب القطر الفراغي a√3.",
      "controls": [
        {
          "id": "a",
          "label": "طول الضلع a",
          "min": 1,
          "max": 10,
          "step": 1,
          "default": 4
        }
      ]
    },
    "act-math-line-plane": {
      "id": "act-math-line-plane",
      "title": "الزاوية بين مستقيم ومستوى",
      "unit_id": "u4",
      "book_page": 144,
      "sim_type": "math_line_plane",
      "description": "غيّر زاوية المستقيم مع المتجه الطبيعي ولاحظ الزاوية مع المستوى.",
      "controls": [
        {
          "id": "alpha",
          "label": "زاوية المستقيم مع الطبيعي",
          "min": 0,
          "max": 90,
          "step": 5,
          "default": 40
        }
      ]
    },
    "act-math-dihedral": {
      "id": "act-math-dihedral",
      "title": "الزاوية ثنائية الوجه",
      "unit_id": "u4",
      "book_page": 149,
      "sim_type": "math_dihedral",
      "description": "دور مستوى حول خط التقاطع ولاحظ الزاوية بين المتجهين الطبيعيين.",
      "controls": [
        {
          "id": "phi",
          "label": "زاوية المستوى الثاني",
          "min": 0,
          "max": 120,
          "step": 5,
          "default": 60
        }
      ]
    },
    "act-math-prob-union": {
      "id": "act-math-prob-union",
      "title": "قاعدة جمع الاحتمالات",
      "unit_id": "u5",
      "book_page": 82,
      "sim_type": "math_prob_union",
      "description": "غيّر احتمالي الحدثين وتداخلهما ولاحظ P(A∪B).",
      "controls": [
        {
          "id": "pa",
          "label": "P(A)",
          "min": 0,
          "max": 100,
          "step": 5,
          "default": 55
        },
        {
          "id": "pb",
          "label": "P(B)",
          "min": 0,
          "max": 100,
          "step": 5,
          "default": 40
        },
        {
          "id": "inter",
          "label": "P(A∩B)",
          "min": 0,
          "max": 100,
          "step": 5,
          "default": 20
        }
      ]
    },
    "act-math-prob-conditional": {
      "id": "act-math-prob-conditional",
      "title": "الاحتمال الشرطي",
      "unit_id": "u5",
      "book_page": 89,
      "sim_type": "math_prob_conditional",
      "description": "احسب احتمال A بشرط حدوث B.",
      "controls": [
        {
          "id": "pa",
          "label": "P(A∩B)",
          "min": 0,
          "max": 100,
          "step": 5,
          "default": 25
        },
        {
          "id": "pb",
          "label": "P(B)",
          "min": 5,
          "max": 100,
          "step": 5,
          "default": 50
        }
      ]
    },
    "act-math-prob-binomial": {
      "id": "act-math-prob-binomial",
      "title": "التوزيع ذو الحدين",
      "unit_id": "u5",
      "book_page": 96,
      "sim_type": "math_prob_binomial",
      "description": "احتمال k نجاحاً في n تجربة مستقلة.",
      "controls": [
        {
          "id": "n",
          "label": "عدد التجارب n",
          "min": 1,
          "max": 20,
          "step": 1,
          "default": 10
        },
        {
          "id": "p",
          "label": "احتمال النجاح p",
          "min": 0,
          "max": 100,
          "step": 5,
          "default": 50
        },
        {
          "id": "k",
          "label": "عدد النجاحات k",
          "min": 0,
          "max": 20,
          "step": 1,
          "default": 4
        }
      ]
    },
    "act-math-power-rule": {
      "id": "act-math-power-rule",
      "title": "قاعدة القوة في الاشتقاق",
      "unit_id": "u6",
      "book_page": 162,
      "sim_type": "math_power_derivative",
      "description": "اشتق xⁿ ولاحظ قيمة المشتقة عند x.",
      "controls": [
        {
          "id": "x",
          "label": "القيمة x",
          "min": 1,
          "max": 8,
          "step": 1,
          "default": 3
        },
        {
          "id": "n",
          "label": "الأس n",
          "min": 1,
          "max": 8,
          "step": 1,
          "default": 3
        }
      ]
    },
    "act-math-product-rule": {
      "id": "act-math-product-rule",
      "title": "قاعدة الجداء",
      "unit_id": "u6",
      "book_page": 166,
      "sim_type": "math_product_rule",
      "description": "طبّق (uv)′ = u′v + uv′ على مثال بسيط.",
      "controls": [
        {
          "id": "x",
          "label": "القيمة x",
          "min": 1,
          "max": 8,
          "step": 1,
          "default": 2
        },
        {
          "id": "a",
          "label": "معامل u",
          "min": 1,
          "max": 5,
          "step": 1,
          "default": 2
        },
        {
          "id": "b",
          "label": "معامل v",
          "min": 1,
          "max": 5,
          "step": 1,
          "default": 3
        }
      ]
    },
    "act-math-chain-rule": {
      "id": "act-math-chain-rule",
      "title": "قاعدة السلسلة",
      "unit_id": "u6",
      "book_page": 169,
      "sim_type": "math_chain_rule",
      "description": "اشتق (ax+b)ⁿ خطوة بخطوة.",
      "controls": [
        {
          "id": "x",
          "label": "القيمة x",
          "min": 0,
          "max": 6,
          "step": 1,
          "default": 2
        },
        {
          "id": "a",
          "label": "المعامل a",
          "min": 1,
          "max": 4,
          "step": 1,
          "default": 2
        },
        {
          "id": "n",
          "label": "الأس n",
          "min": 2,
          "max": 6,
          "step": 1,
          "default": 3
        }
      ]
    },
    "act-math-extrema": {
      "id": "act-math-extrema",
      "title": "القيم القصوى",
      "unit_id": "u6",
      "book_page": 192,
      "sim_type": "math_extrema",
      "description": "ابحث عن النقطة الحرجة لدالة تربيعية.",
      "controls": [
        {
          "id": "a",
          "label": "المعامل a",
          "min": -5,
          "max": 5,
          "step": 1,
          "default": 1
        },
        {
          "id": "b",
          "label": "المعامل b",
          "min": -10,
          "max": 10,
          "step": 1,
          "default": -4
        },
        {
          "id": "c",
          "label": "الثابت c",
          "min": -10,
          "max": 10,
          "step": 1,
          "default": 3
        }
      ]
    },
    "act-math-mvt": {
      "id": "act-math-mvt",
      "title": "نظرية القيمة المتوسطة",
      "unit_id": "u6",
      "book_page": 203,
      "sim_type": "math_mvt",
      "description": "قارن ميل القطرة بميل المماس عند نقطة داخل الفترة.",
      "controls": [
        {
          "id": "a",
          "label": "الحد الأدنى a",
          "min": 0,
          "max": 5,
          "step": 1,
          "default": 1
        },
        {
          "id": "b",
          "label": "الحد الأعلى b",
          "min": 3,
          "max": 10,
          "step": 1,
          "default": 5
        }
      ]
    },
    "act-math-indefinite": {
      "id": "act-math-indefinite",
      "title": "التكامل غير المحدد",
      "unit_id": "u7",
      "book_page": 214,
      "sim_type": "math_indefinite",
      "description": "طبّق قاعدة تكامل القوة.",
      "controls": [
        {
          "id": "n",
          "label": "الأس n",
          "min": 0,
          "max": 8,
          "step": 1,
          "default": 3
        }
      ]
    },
    "act-math-definite": {
      "id": "act-math-definite",
      "title": "التكامل المحدد",
      "unit_id": "u7",
      "book_page": 237,
      "sim_type": "math_definite_integral",
      "description": "احسب ∫xⁿdx من a إلى b.",
      "controls": [
        {
          "id": "a",
          "label": "الحد الأدنى a",
          "min": 0,
          "max": 5,
          "step": 1,
          "default": 1
        },
        {
          "id": "b",
          "label": "الحد الأعلى b",
          "min": 2,
          "max": 10,
          "step": 1,
          "default": 4
        },
        {
          "id": "n",
          "label": "الأس n",
          "min": 0,
          "max": 6,
          "step": 1,
          "default": 2
        }
      ]
    },
    "act-math-area": {
      "id": "act-math-area",
      "title": "المساحة تحت المنحنى",
      "unit_id": "u7",
      "book_page": 246,
      "sim_type": "math_area_between",
      "description": "احسب المساحة تحت xⁿ بين حدين.",
      "controls": [
        {
          "id": "a",
          "label": "الحد الأدنى a",
          "min": 0,
          "max": 5,
          "step": 1,
          "default": 0
        },
        {
          "id": "b",
          "label": "الحد الأعلى b",
          "min": 2,
          "max": 10,
          "step": 1,
          "default": 3
        },
        {
          "id": "n",
          "label": "الأس n",
          "min": 0,
          "max": 5,
          "step": 1,
          "default": 2
        }
      ]
    },
    "act-math-revolution": {
      "id": "act-math-revolution",
      "title": "حجم مجسم الدوران",
      "unit_id": "u7",
      "book_page": 250,
      "sim_type": "math_revolution_volume",
      "description": "احسب حجم دوران y=xⁿ حول محور x.",
      "controls": [
        {
          "id": "a",
          "label": "الحد الأدنى a",
          "min": 0,
          "max": 4,
          "step": 1,
          "default": 0
        },
        {
          "id": "b",
          "label": "الحد الأعلى b",
          "min": 1,
          "max": 6,
          "step": 1,
          "default": 2
        },
        {
          "id": "n",
          "label": "الأس n",
          "min": 1,
          "max": 4,
          "step": 1,
          "default": 1
        }
      ]
    }
  },
  "assessments": {
    "quiz-math-u1": [
      {
        "id": "qm-u1-01",
        "unitId": "u1",
        "lessonId": "math-u1-l1",
        "page": 7,
        "difficulty": "easy",
        "skillId": "recall",
        "q": "ما الجزء الحقيقي في العدد 3 + 2i؟",
        "options": [
          {
            "text": "3"
          },
          {
            "text": "2",
            "why_wrong": "هذا الجزء التخيلي، وليس الحقيقي."
          },
          {
            "text": "5",
            "why_wrong": "هذا مجموع المكوّنين، وليس الجزء الحقيقي."
          },
          {
            "text": "√13",
            "why_wrong": "هذه القيمة المطلقة للعدد، وليس جزأه الحقيقي."
          }
        ],
        "answer": 0,
        "explain": "الجزء الحقيقي هو المعامل الذي لا يضرب في i."
      },
      {
        "id": "qm-u1-02",
        "unitId": "u1",
        "lessonId": "math-u1-l2",
        "page": 13,
        "difficulty": "medium",
        "skillId": "calculation",
        "q": "ما قيمة i²؟",
        "options": [
          {
            "text": "1",
            "why_wrong": "هذا ينتج من نسيان تعريف الوحدة التخيلية."
          },
          {
            "text": "0",
            "why_wrong": "الوحدة التخيلية ليست صفراً."
          },
          {
            "text": "i",
            "why_wrong": "تربيع i يعطي عدداً حقيقياً سالباً."
          },
          {
            "text": "−1"
          }
        ],
        "answer": 3,
        "explain": "بالتعريف i² = −1."
      },
      {
        "id": "qm-u1-03",
        "unitId": "u1",
        "lessonId": "math-u1-l3",
        "page": 18,
        "difficulty": "hard",
        "skillId": "analysis",
        "q": "احسب |3 + 4i|.",
        "options": [
          {
            "text": "25",
            "why_wrong": "هذا مربع القيمة المطلقة قبل أخذ الجذر."
          },
          {
            "text": "√7",
            "why_wrong": "استخدمت المجموع بدل مجموع المربعات."
          },
          {
            "text": "5"
          },
          {
            "text": "7",
            "why_wrong": "جمع المكوّنات لا يعطي القيمة المطلقة."
          }
        ],
        "answer": 2,
        "explain": "|z| = √(3² + 4²) = 5."
      },
      {
        "id": "qm-u1-04",
        "unitId": "u1",
        "lessonId": "math-u1-l4",
        "page": 26,
        "difficulty": "easy",
        "skillId": "application",
        "q": "احسب (2 + 3i) + (1 − i).",
        "options": [
          {
            "text": "−1 + 4i",
            "why_wrong": "خلطت بين الجمع والطرح."
          },
          {
            "text": "3 + 2i"
          },
          {
            "text": "3 + 4i",
            "why_wrong": "طرح 1 بدل جمعه في الجزء التخيلي."
          },
          {
            "text": "1 + 2i",
            "why_wrong": "نسيت جمع الجزء الحقيقي 2 + 1."
          }
        ],
        "answer": 1,
        "explain": "نجمع الأجزاء الحقيقية والتخيلية على حدة."
      },
      {
        "id": "qm-u1-05",
        "unitId": "u1",
        "lessonId": "math-u1-l5",
        "page": 37,
        "difficulty": "medium",
        "skillId": "recall",
        "q": "احسب (2 + i)(1 − i).",
        "options": [
          {
            "text": "3 − i"
          },
          {
            "text": "1 − i",
            "why_wrong": "نسيت حد i² عند التبسيط."
          },
          {
            "text": "3 + i",
            "why_wrong": "أخطأت في إشارة الحد التخيلي."
          },
          {
            "text": "2 − 2i",
            "why_wrong": "حذفت بعض حدود الضرب."
          }
        ],
        "answer": 0,
        "explain": "الضرب يعطي 2 − 2i + i − i² = 3 − i."
      },
      {
        "id": "qm-u1-06",
        "unitId": "u1",
        "lessonId": "math-u1-l6",
        "page": 40,
        "difficulty": "hard",
        "skillId": "calculation",
        "q": "ما مرافق العدد 4 − 5i؟",
        "options": [
          {
            "text": "−4 − 5i",
            "why_wrong": "هذا عكس العدد، وليس مرافقه."
          },
          {
            "text": "4 − 5i",
            "why_wrong": "المرافق يغيّر إشارة الجزء التخيلي."
          },
          {
            "text": "5 − 4i",
            "why_wrong": "بادل بين الجزأين الحقيقي والتخيلي."
          },
          {
            "text": "4 + 5i"
          }
        ],
        "answer": 3,
        "explain": "نغيّر إشارة الجزء التخيلي فقط."
      },
      {
        "id": "qm-u1-07",
        "unitId": "u1",
        "lessonId": "math-u1-l1",
        "page": 8,
        "difficulty": "easy",
        "skillId": "analysis",
        "q": "ما سعة العدد 1 + i بالدرجات؟",
        "options": [
          {
            "text": "90°",
            "why_wrong": "الزاوية 90° تعني أن الجزء الحقيقي صفر."
          },
          {
            "text": "135°",
            "why_wrong": "النقطة في الربع الأول لا الثاني."
          },
          {
            "text": "45°"
          },
          {
            "text": "30°",
            "why_wrong": "tan θ = 1، فالزاوية 45° لا 30°."
          }
        ],
        "answer": 2,
        "explain": "tan θ = 1/1، والنقطة تقع في الربع الأول."
      },
      {
        "id": "qm-u1-08",
        "unitId": "u1",
        "lessonId": "math-u1-l2",
        "page": 15,
        "difficulty": "medium",
        "skillId": "application",
        "q": "ما القيمة المطلقة للعدد 1 + √3 i؟",
        "options": [
          {
            "text": "√2",
            "why_wrong": "استخدمت 1² + 1² بدل 1² + (√3)²."
          },
          {
            "text": "2"
          },
          {
            "text": "√3",
            "why_wrong": "هذا الجزء التخيلي فقط."
          },
          {
            "text": "4",
            "why_wrong": "هذا مربع القيمة المطلقة."
          }
        ],
        "answer": 1,
        "explain": "|z| = √(1 + 3) = 2."
      },
      {
        "id": "qm-u1-09",
        "unitId": "u1",
        "lessonId": "math-u1-l3",
        "page": 17,
        "difficulty": "hard",
        "skillId": "recall",
        "q": "اكتب −1 + i بالصيغة القطبية.",
        "options": [
          {
            "text": "√2(cos135° + i sin135°)"
          },
          {
            "text": "√2(cos45° + i sin45°)",
            "why_wrong": "هذه زاوية الربع الأول، والعدد في الربع الثاني."
          },
          {
            "text": "2(cos135° + i sin135°)",
            "why_wrong": "القيمة المطلقة √2 وليست 2."
          },
          {
            "text": "√2(cos225° + i sin225°)",
            "why_wrong": "الزاوية 225° تعطي −1 − i."
          }
        ],
        "answer": 0,
        "explain": "r = √2 والزاوية 135° لأن النقطة في الربع الثاني."
      },
      {
        "id": "qm-u1-10",
        "unitId": "u1",
        "lessonId": "math-u1-l4",
        "page": 32,
        "difficulty": "easy",
        "skillId": "calculation",
        "q": "احسب |6 + 8i|.",
        "options": [
          {
            "text": "14",
            "why_wrong": "جمع المكوّنات لا يعطي الطول."
          },
          {
            "text": "48",
            "why_wrong": "هذا حاصل ضرب المكوّنين."
          },
          {
            "text": "√10",
            "why_wrong": "استخدمت المجموع بدل مجموع المربعات."
          },
          {
            "text": "10"
          }
        ],
        "answer": 3,
        "explain": "|z| = √(36 + 64) = 10."
      },
      {
        "id": "qm-u1-11",
        "unitId": "u1",
        "lessonId": "math-u1-l5",
        "page": 36,
        "difficulty": "medium",
        "skillId": "analysis",
        "q": "اكتب 5(cos60° + i sin60°) بالصيغة الجبرية.",
        "options": [
          {
            "text": "5/2 + 5i",
            "why_wrong": "الجزء التخيلي يجب أن يكون (5√3)/2."
          },
          {
            "text": "5√3 + (5/2)i",
            "why_wrong": "بادل بين الإسقاطين."
          },
          {
            "text": "5/2 + (5√3/2)i"
          },
          {
            "text": "5 + √3i",
            "why_wrong": "لم تضرب r في cosθ و sinθ."
          }
        ],
        "answer": 2,
        "explain": "a = 5cos60° = 5/2 و b = 5sin60° = 5√3/2."
      },
      {
        "id": "qm-u1-12",
        "unitId": "u1",
        "lessonId": "math-u1-l6",
        "page": 41,
        "difficulty": "hard",
        "skillId": "application",
        "q": "احسب 2i + (−3i).",
        "options": [
          {
            "text": "−5i",
            "why_wrong": "جمعت بوصفهما سالبين."
          },
          {
            "text": "−i"
          },
          {
            "text": "i",
            "why_wrong": "أخطأت في إشارة المجموع."
          },
          {
            "text": "5i",
            "why_wrong": "جمعت القيم المطلقة بدل الإشارات."
          }
        ],
        "answer": 1,
        "explain": "2i − 3i = −i."
      },
      {
        "id": "qm-u1-13",
        "unitId": "u1",
        "lessonId": "math-u1-l1",
        "page": 9,
        "difficulty": "easy",
        "skillId": "recall",
        "q": "ما المسافة بين 1 + 2i و 4 + 6i؟",
        "options": [
          {
            "text": "5"
          },
          {
            "text": "7",
            "why_wrong": "جمعت الفروق بدل استخدام فيثاغورس."
          },
          {
            "text": "√5",
            "why_wrong": "استخدمت فرقاً واحداً فقط."
          },
          {
            "text": "25",
            "why_wrong": "هذا مربع المسافة."
          }
        ],
        "answer": 0,
        "explain": "المسافة = |(4+6i)−(1+2i)| = |3+4i| = 5."
      },
      {
        "id": "qm-u1-14",
        "unitId": "u1",
        "lessonId": "math-u1-l2",
        "page": 13,
        "difficulty": "medium",
        "skillId": "calculation",
        "q": "إذا كان |a + bi| = 0 فماذا ينتج؟",
        "options": [
          {
            "text": "a = 0 فقط",
            "why_wrong": "يجب أن يصفر الجزء التخيلي أيضاً."
          },
          {
            "text": "b = 0 فقط",
            "why_wrong": "يجب أن يصفر الجزء الحقيقي أيضاً."
          },
          {
            "text": "a = b = 1",
            "why_wrong": "القيمة المطلقة حينها √2 لا صفر."
          },
          {
            "text": "a = 0 و b = 0"
          }
        ],
        "answer": 3,
        "explain": "مجموع مربعين لا يساوي صفراً إلا إذا كان كلاهما صفراً."
      },
      {
        "id": "qm-u1-15",
        "unitId": "u1",
        "lessonId": "math-u1-l3",
        "page": 16,
        "difficulty": "hard",
        "skillId": "analysis",
        "q": "احسب (1 + i)².",
        "options": [
          {
            "text": "1 + 2i",
            "why_wrong": "حذفت حد i² خطأً."
          },
          {
            "text": "0",
            "why_wrong": "النتيجة ليست صفراً؛ i² = −1."
          },
          {
            "text": "2i"
          },
          {
            "text": "2",
            "why_wrong": "نسيت أن 2i متبقٍ بعد إلغاء i²."
          }
        ],
        "answer": 2,
        "explain": "(1+i)² = 1+2i+i² = 2i."
      }
    ],
    "quiz-math-u2": [
      {
        "id": "qm-u2-01",
        "unitId": "u2",
        "lessonId": "math-u2-l1",
        "page": 45,
        "difficulty": "easy",
        "skillId": "recall",
        "q": "احسب (cos30° + i sin30°)⁴.",
        "options": [
          {
            "text": "cos120° + i sin120°"
          },
          {
            "text": "cos34° + i sin34°",
            "why_wrong": "قاعدة دي موافر تضرب الزاوية في الأس لا تجمعها."
          },
          {
            "text": "cos120° − i sin120°",
            "why_wrong": "إشارة الجزء التخيلي لا تتغير في الرفع."
          },
          {
            "text": "cos60° + i sin60°",
            "why_wrong": "4 × 30° = 120° وليس 60°."
          }
        ],
        "answer": 0,
        "explain": "نضرب الزاوية في الأس: nθ = 120°."
      },
      {
        "id": "qm-u2-02",
        "unitId": "u2",
        "lessonId": "math-u2-l2",
        "page": 50,
        "difficulty": "medium",
        "skillId": "calculation",
        "q": "إذا كان z = 2(cos30° + i sin30°) فما z³؟",
        "options": [
          {
            "text": "6(cos90° + i sin90°)",
            "why_wrong": "القيمة المطلقة تُرفع للأس: 2³ = 8."
          },
          {
            "text": "8(cos10° + i sin10°)",
            "why_wrong": "الزاوية تُضرب في الأس لا تُقسم."
          },
          {
            "text": "2(cos90° + i sin90°)",
            "why_wrong": "نسيت رفع r إلى القوة الثالثة."
          },
          {
            "text": "8(cos90° + i sin90°)"
          }
        ],
        "answer": 3,
        "explain": "z³ = 2³(cos 3×30° + i sin 3×30°)."
      },
      {
        "id": "qm-u2-03",
        "unitId": "u2",
        "lessonId": "math-u2-l3",
        "page": 57,
        "difficulty": "hard",
        "skillId": "analysis",
        "q": "كم جذراً نونياً للعدد 1 من الدرجة الخامسة؟",
        "options": [
          {
            "text": "10",
            "why_wrong": "لا تضاعف الدرجة."
          },
          {
            "text": "1",
            "why_wrong": "لكل درجة n يوجد n جذراً مركباً."
          },
          {
            "text": "5"
          },
          {
            "text": "4",
            "why_wrong": "عدد الجذور يساوي درجة الجذر لا نصفها."
          }
        ],
        "answer": 2,
        "explain": "معادلة z⁵ = 1 لها خمسة جذور مركبة."
      },
      {
        "id": "qm-u2-04",
        "unitId": "u2",
        "lessonId": "math-u2-l4",
        "page": 68,
        "difficulty": "easy",
        "skillId": "application",
        "q": "ما الفرق في الزاوية بين جذرين متجاورين من جذور z⁶؟",
        "options": [
          {
            "text": "30°",
            "why_wrong": "نصف القيمة الصحيحة."
          },
          {
            "text": "60°"
          },
          {
            "text": "90°",
            "why_wrong": "الفرق هو 360°/6."
          },
          {
            "text": "45°",
            "why_wrong": "استخدمت 360°/8 بدل 360°/6."
          }
        ],
        "answer": 1,
        "explain": "الفرق = 2π/n = 360°/6 = 60°."
      },
      {
        "id": "qm-u2-05",
        "unitId": "u2",
        "lessonId": "math-u2-l1",
        "page": 45,
        "difficulty": "medium",
        "skillId": "recall",
        "q": "احسب C(6,2).",
        "options": [
          {
            "text": "15"
          },
          {
            "text": "12",
            "why_wrong": "حساب المعامل خاطئ؛ (6×5)/(2×1)=15."
          },
          {
            "text": "30",
            "why_wrong": "نسيت القسمة على 2!."
          },
          {
            "text": "20",
            "why_wrong": "هذه قيمة C(6,3)."
          }
        ],
        "answer": 0,
        "explain": "C(6,2) = 6!/(2!4!) = 15."
      },
      {
        "id": "qm-u2-06",
        "unitId": "u2",
        "lessonId": "math-u2-l2",
        "page": 54,
        "difficulty": "hard",
        "skillId": "calculation",
        "q": "ما معاملات (a+b)⁴؟",
        "options": [
          {
            "text": "1، 3، 3، 1",
            "why_wrong": "هذه معاملات (a+b)³."
          },
          {
            "text": "1، 4، 4، 1",
            "why_wrong": "حذفت المعامل الأوسط 6."
          },
          {
            "text": "1، 5، 10، 5، 1",
            "why_wrong": "هذه معاملات الأس الخامس."
          },
          {
            "text": "1، 4، 6، 4، 1"
          }
        ],
        "answer": 3,
        "explain": "من مثلث باسكال للصف الرابع."
      },
      {
        "id": "qm-u2-07",
        "unitId": "u2",
        "lessonId": "math-u2-l3",
        "page": 61,
        "difficulty": "easy",
        "skillId": "analysis",
        "q": "ما الحد الأوسط في توسعة (x+y)⁶؟",
        "options": [
          {
            "text": "6x³y³",
            "why_wrong": "نسيت حساب C(6,3)=20."
          },
          {
            "text": "20x⁴y²",
            "why_wrong": "الأسود يجب أن يكونا 3 و 3."
          },
          {
            "text": "20x³y³"
          },
          {
            "text": "15x²y⁴",
            "why_wrong": "هذا ليس الحد الأوسط للأس 6."
          }
        ],
        "answer": 2,
        "explain": "الحد الأوسط C(6,3)x³y³ = 20x³y³."
      },
      {
        "id": "qm-u2-08",
        "unitId": "u2",
        "lessonId": "math-u2-l4",
        "page": 72,
        "difficulty": "medium",
        "skillId": "application",
        "q": "احسب (1 + i)⁴.",
        "options": [
          {
            "text": "−2",
            "why_wrong": "نسيت رفع القيمة المطلقة للأس الرابع."
          },
          {
            "text": "−4"
          },
          {
            "text": "4",
            "why_wrong": "الزاوية 180° تعطي إشارة سالبة."
          },
          {
            "text": "2",
            "why_wrong": "القيمة المطلقة (√2)⁴ = 4."
          }
        ],
        "answer": 1,
        "explain": "|1+i|=√2 والزاوية 45°، إذن النتيجة 4(cos180°+i sin180°)=−4."
      },
      {
        "id": "qm-u2-09",
        "unitId": "u2",
        "lessonId": "math-u2-l1",
        "page": 45,
        "difficulty": "hard",
        "skillId": "recall",
        "q": "ما قيمة r لأحد الجذور التكعيبية لـ 8(cos90° + i sin90°)؟",
        "options": [
          {
            "text": "2"
          },
          {
            "text": "8",
            "why_wrong": "جذر القيمة المطلقة يُؤخذ: 8^(1/3)=2."
          },
          {
            "text": "√8",
            "why_wrong": "هذا جذر تربيعي لا تكعيبي."
          },
          {
            "text": "6",
            "why_wrong": "لا تُقسم القيمة المطلقة على الأس."
          }
        ],
        "answer": 0,
        "explain": "نصف قطر الجذور هو r^(1/n) = 2."
      },
      {
        "id": "qm-u2-10",
        "unitId": "u2",
        "lessonId": "math-u2-l2",
        "page": 52,
        "difficulty": "easy",
        "skillId": "calculation",
        "q": "ما معامل x² في (1+x)⁵؟",
        "options": [
          {
            "text": "5",
            "why_wrong": "هذا معامل x فقط."
          },
          {
            "text": "20",
            "why_wrong": "هذا معامل x³."
          },
          {
            "text": "15",
            "why_wrong": "حساب C(5,2) خاطئ."
          },
          {
            "text": "10"
          }
        ],
        "answer": 3,
        "explain": "المعامل C(5,2)=10."
      },
      {
        "id": "qm-u2-11",
        "unitId": "u2",
        "lessonId": "math-u2-l3",
        "page": 55,
        "difficulty": "medium",
        "skillId": "analysis",
        "q": "كم عدد حدود توسعة (a+b)⁹؟",
        "options": [
          {
            "text": "8",
            "why_wrong": "طرحت واحداً بدل إضافة واحد."
          },
          {
            "text": "11",
            "why_wrong": "أضفت اثنين بدل واحد."
          },
          {
            "text": "10"
          },
          {
            "text": "9",
            "why_wrong": "عدد الحدود n+1."
          }
        ],
        "answer": 2,
        "explain": "عدد الحدود = 9 + 1 = 10."
      },
      {
        "id": "qm-u2-12",
        "unitId": "u2",
        "lessonId": "math-u2-l4",
        "page": 67,
        "difficulty": "hard",
        "skillId": "application",
        "q": "ما الصيغة المناسبة لتطبيق دي موافر مباشرة؟",
        "options": [
          {
            "text": "أي صيغة بزاوية بالراديان فقط",
            "why_wrong": "الدرجات مقبولة طالما متسقة."
          },
          {
            "text": "r(cosθ + i sinθ)"
          },
          {
            "text": "a + bi فقط",
            "why_wrong": "تحتاج تحويلاً أولاً إلى الصيغة القطبية."
          },
          {
            "text": "عدد حقيقي فقط",
            "why_wrong": "المبرهنة للأعداد المركبة."
          }
        ],
        "answer": 1,
        "explain": "الصيغة القطبية تجعل الرفع إلى قوة بسيطاً."
      },
      {
        "id": "qm-u2-13",
        "unitId": "u2",
        "lessonId": "math-u2-l1",
        "page": 45,
        "difficulty": "easy",
        "skillId": "recall",
        "q": "احسب (−1 + i)².",
        "options": [
          {
            "text": "−2i"
          },
          {
            "text": "2i",
            "why_wrong": "أخطأت في إشارة الحد التخيلي الناتج."
          },
          {
            "text": "−2",
            "why_wrong": "الحد 2i لا يلغي عند التربيع."
          },
          {
            "text": "0",
            "why_wrong": "القيمة المطلقة ليست صفراً."
          }
        ],
        "answer": 0,
        "explain": "(−1+i)² = 1−2i+i² = −2i."
      },
      {
        "id": "qm-u2-14",
        "unitId": "u2",
        "lessonId": "math-u2-l2",
        "page": 50,
        "difficulty": "medium",
        "skillId": "calculation",
        "q": "احسب C(5,3).",
        "options": [
          {
            "text": "5",
            "why_wrong": "هذا C(5,1)."
          },
          {
            "text": "15",
            "why_wrong": "هذا C(6,2)."
          },
          {
            "text": "20",
            "why_wrong": "حساب خاطئ للمعامل."
          },
          {
            "text": "10"
          }
        ],
        "answer": 3,
        "explain": "C(5,3)=C(5,2)=10."
      },
      {
        "id": "qm-u2-15",
        "unitId": "u2",
        "lessonId": "math-u2-l3",
        "page": 59,
        "difficulty": "hard",
        "skillId": "analysis",
        "q": "ما مجموع معاملات (1+1)⁸؟",
        "options": [
          {
            "text": "64",
            "why_wrong": "هذه 2⁶."
          },
          {
            "text": "8",
            "why_wrong": "هذا الأس نفسه، لا مجموع المعاملات."
          },
          {
            "text": "256"
          },
          {
            "text": "128",
            "why_wrong": "هذه 2⁷ لا 2⁸."
          }
        ],
        "answer": 2,
        "explain": "مجموع المعاملات = (1+1)⁸ = 2⁸ = 256."
      }
    ],
    "quiz-math-u3": [
      {
        "id": "qm-u3-01",
        "unitId": "u3",
        "lessonId": "math-u3-l1",
        "page": 104,
        "difficulty": "easy",
        "skillId": "recall",
        "q": "في القطع x²/16 + y²/9 = 1، ما طول المحور الكبير؟",
        "options": [
          {
            "text": "8"
          },
          {
            "text": "6",
            "why_wrong": "هذا طول المحور الصغير."
          },
          {
            "text": "3",
            "why_wrong": "هذا نصف المحور الصغير."
          },
          {
            "text": "4",
            "why_wrong": "هذا نصف المحور الكبير."
          }
        ],
        "answer": 0,
        "explain": "a=4 إذن طول المحور الكبير 2a=8."
      },
      {
        "id": "qm-u3-02",
        "unitId": "u3",
        "lessonId": "math-u3-l2",
        "page": 111,
        "difficulty": "medium",
        "skillId": "calculation",
        "q": "ما بُعد البؤرة عن المركز في x²/16 + y²/9 = 1؟",
        "options": [
          {
            "text": "√5",
            "why_wrong": "طرحت 16−9 خطأً."
          },
          {
            "text": "7",
            "why_wrong": "هذا c² وليس c."
          },
          {
            "text": "5",
            "why_wrong": "جمع المقامين بدل طرحهما."
          },
          {
            "text": "√7"
          }
        ],
        "answer": 3,
        "explain": "c=√(16−9)=√7."
      },
      {
        "id": "qm-u3-03",
        "unitId": "u3",
        "lessonId": "math-u3-l3",
        "page": 120,
        "difficulty": "hard",
        "skillId": "analysis",
        "q": "ما خطا مقاربة القطع x²/9 − y²/16 = 1؟",
        "options": [
          {
            "text": "y = ±4x",
            "why_wrong": "نسيت القسمة على a."
          },
          {
            "text": "y = ±3x",
            "why_wrong": "استخدمت a بدل b/a."
          },
          {
            "text": "y = ±(4/3)x"
          },
          {
            "text": "y = ±(3/4)x",
            "why_wrong": "عكست b/a."
          }
        ],
        "answer": 2,
        "explain": "للقطع الأفقي y=±(b/a)x=±(4/3)x."
      },
      {
        "id": "qm-u3-04",
        "unitId": "u3",
        "lessonId": "math-u3-l4",
        "page": 127,
        "difficulty": "easy",
        "skillId": "application",
        "q": "في y² = 20x، ما قيمة p؟",
        "options": [
          {
            "text": "√20",
            "why_wrong": "لا يوجد جذر هنا."
          },
          {
            "text": "5"
          },
          {
            "text": "20",
            "why_wrong": "المعطى هو 4p لا p."
          },
          {
            "text": "10",
            "why_wrong": "قسمت على 2 بدل 4."
          }
        ],
        "answer": 1,
        "explain": "4p=20 إذن p=5."
      },
      {
        "id": "qm-u3-05",
        "unitId": "u3",
        "lessonId": "math-u3-l5",
        "page": 131,
        "difficulty": "medium",
        "skillId": "recall",
        "q": "أي قطع مخروطي انحرافه e أكبر من 1؟",
        "options": [
          {
            "text": "القطع الزائد"
          },
          {
            "text": "القطع الناقص",
            "why_wrong": "القطع الناقص له e<1."
          },
          {
            "text": "القطع المكافئ",
            "why_wrong": "القطع المكافئ له e=1."
          },
          {
            "text": "الدائرة",
            "why_wrong": "الدائرة حالة خاصة بـ e=0."
          }
        ],
        "answer": 0,
        "explain": "e>1 يعطي القطع الزائد."
      },
      {
        "id": "qm-u3-06",
        "unitId": "u3",
        "lessonId": "math-u3-l1",
        "page": 109,
        "difficulty": "hard",
        "skillId": "calculation",
        "q": "أي قطع مخروطي انحرافه e يساوي 1؟",
        "options": [
          {
            "text": "القطع الناقص",
            "why_wrong": "للقطع الناقص e<1."
          },
          {
            "text": "القطع الزائد",
            "why_wrong": "للقطع الزائد e>1."
          },
          {
            "text": "الدائرة",
            "why_wrong": "للدائرة e=0."
          },
          {
            "text": "القطع المكافئ"
          }
        ],
        "answer": 3,
        "explain": "e=1 هو تعريف القطع المكافئ."
      },
      {
        "id": "qm-u3-07",
        "unitId": "u3",
        "lessonId": "math-u3-l2",
        "page": 116,
        "difficulty": "easy",
        "skillId": "analysis",
        "q": "في x²/25 + y²/9 = 1، ما c؟",
        "options": [
          {
            "text": "3",
            "why_wrong": "هذا b."
          },
          {
            "text": "√34",
            "why_wrong": "جمعت المقامين بدل طرحهما."
          },
          {
            "text": "4"
          },
          {
            "text": "5",
            "why_wrong": "هذا a وليس c."
          }
        ],
        "answer": 2,
        "explain": "c=√(25−9)=4."
      },
      {
        "id": "qm-u3-08",
        "unitId": "u3",
        "lessonId": "math-u3-l3",
        "page": 119,
        "difficulty": "medium",
        "skillId": "application",
        "q": "إذا كان a=3 لقطع زائد، فما طول محوره القطعي؟",
        "options": [
          {
            "text": "8",
            "why_wrong": "لا علاقة له بالمعطى."
          },
          {
            "text": "6"
          },
          {
            "text": "3",
            "why_wrong": "هذا نصف المحور."
          },
          {
            "text": "9",
            "why_wrong": "هذا a²."
          }
        ],
        "answer": 1,
        "explain": "طول المحور القطعي = 2a = 6."
      },
      {
        "id": "qm-u3-09",
        "unitId": "u3",
        "lessonId": "math-u3-l4",
        "page": 126,
        "difficulty": "hard",
        "skillId": "recall",
        "q": "ما دليل القطع y² = 12x؟",
        "options": [
          {
            "text": "x = −3"
          },
          {
            "text": "x = 3",
            "why_wrong": "الدليل يقع في الجهة المعاكسة للبؤرة."
          },
          {
            "text": "y = −3",
            "why_wrong": "محور التماثل أفقي، فالدليل مستقيم رأسي."
          },
          {
            "text": "x = −6",
            "why_wrong": "12 = 4p إذن p=3 لا 6."
          }
        ],
        "answer": 0,
        "explain": "4p=12، p=3، والدليل x=−p."
      },
      {
        "id": "qm-u3-10",
        "unitId": "u3",
        "lessonId": "math-u3-l5",
        "page": 130,
        "difficulty": "easy",
        "skillId": "calculation",
        "q": "ما مركز القطع x²/4 + y²/9 = 1؟",
        "options": [
          {
            "text": "(2، 3)",
            "why_wrong": "هذه قيم المقامات، لا إحداثيات المركز."
          },
          {
            "text": "(4، 9)",
            "why_wrong": "المقامات ليست إحداثيات."
          },
          {
            "text": "(0، 1)",
            "why_wrong": "لا يوجد إزاحة في المعادلة."
          },
          {
            "text": "(0، 0)"
          }
        ],
        "answer": 3,
        "explain": "لا توجد حدود (x−h) أو (y−k)، فالمركز المبدأ."
      },
      {
        "id": "qm-u3-11",
        "unitId": "u3",
        "lessonId": "math-u3-l1",
        "page": 108,
        "difficulty": "medium",
        "skillId": "analysis",
        "q": "ما مركز (x−1)²/9 + (y+2)²/4 = 1؟",
        "options": [
          {
            "text": "(1، 2)",
            "why_wrong": "y+2 تعطي k=−2."
          },
          {
            "text": "(−1، −2)",
            "why_wrong": "x−1 تعطي h=1."
          },
          {
            "text": "(1، −2)"
          },
          {
            "text": "(−1، 2)",
            "why_wrong": "عكست الإشارتين."
          }
        ],
        "answer": 2,
        "explain": "المركز (h، k) = (1، −2)."
      },
      {
        "id": "qm-u3-12",
        "unitId": "u3",
        "lessonId": "math-u3-l2",
        "page": 113,
        "difficulty": "hard",
        "skillId": "application",
        "q": "أي اتجاه يفتح له القطع x²/9 − y²/4 = 1؟",
        "options": [
          {
            "text": "دائرياً",
            "why_wrong": "الإشارة سالبة في y²، فليس دائرة."
          },
          {
            "text": "أفقياً"
          },
          {
            "text": "رأسياً",
            "why_wrong": "الحد الموجب هو x²، إذن المحور أفقي."
          },
          {
            "text": "لأعلى فقط",
            "why_wrong": "القطع الزائد له فرعان متقابلان."
          }
        ],
        "answer": 1,
        "explain": "الإشارة الموجبة أمام x² تعني محوراً قطعياً أفقياً."
      },
      {
        "id": "qm-u3-13",
        "unitId": "u3",
        "lessonId": "math-u3-l3",
        "page": 118,
        "difficulty": "easy",
        "skillId": "recall",
        "q": "ما انحراف الدائرة؟",
        "options": [
          {
            "text": "0"
          },
          {
            "text": "1",
            "why_wrong": "هذا انحراف القطع المكافئ."
          },
          {
            "text": "∞",
            "why_wrong": "لا يحدث للدائرة."
          },
          {
            "text": "0.5",
            "why_wrong": "ينتمي لقطع ناقص غير دائري."
          }
        ],
        "answer": 0,
        "explain": "الدائرة حالة خاصة من القطع الناقص بـ e=0."
      },
      {
        "id": "qm-u3-14",
        "unitId": "u3",
        "lessonId": "math-u3-l4",
        "page": 125,
        "difficulty": "medium",
        "skillId": "calculation",
        "q": "ما رأس القطع (y−1)² = 8(x−2)؟",
        "options": [
          {
            "text": "(1، 2)",
            "why_wrong": "عكست الإحداثيات."
          },
          {
            "text": "(−2، 1)",
            "why_wrong": "x−2 تعطي h=2 لا −2."
          },
          {
            "text": "(2، −1)",
            "why_wrong": "y−1 تعطي k=1."
          },
          {
            "text": "(2، 1)"
          }
        ],
        "answer": 3,
        "explain": "الصيغة (y−k)²=4p(x−h) تعطي الرأس (2،1)."
      },
      {
        "id": "qm-u3-15",
        "unitId": "u3",
        "lessonId": "math-u3-l5",
        "page": 132,
        "difficulty": "hard",
        "skillId": "analysis",
        "q": "ما بؤرة القطع y² = 8x؟",
        "options": [
          {
            "text": "(4، 0)",
            "why_wrong": "8 = 4p إذن p=2."
          },
          {
            "text": "(8، 0)",
            "why_wrong": "8 هي 4p وليست p."
          },
          {
            "text": "(2، 0)"
          },
          {
            "text": "(0، 2)",
            "why_wrong": "بادل بين الإحداثيات."
          }
        ],
        "answer": 2,
        "explain": "4p=8، p=2، فالبؤرة (2،0)."
      }
    ],
    "quiz-math-u4": [
      {
        "id": "qm-u4-01",
        "unitId": "u4",
        "lessonId": "math-u4-l1",
        "page": 133,
        "difficulty": "easy",
        "skillId": "recall",
        "q": "ما المتجه الطبيعي للمستوى Ax + By + Cz + D = 0؟",
        "options": [
          {
            "text": "(A، B، C)"
          },
          {
            "text": "(A، B، D)",
            "why_wrong": "الثابت D لا يدخل المتجه الطبيعي."
          },
          {
            "text": "(−D، −B، −A)",
            "why_wrong": "ترتيب وإشارات خاطئة."
          },
          {
            "text": "(1، 1، 1)",
            "why_wrong": "غير صحيح إلا إذا كانت A=B=C=1."
          }
        ],
        "answer": 0,
        "explain": "معاملات x و y و z تمثل المتجه الطبيعي."
      },
      {
        "id": "qm-u4-02",
        "unitId": "u4",
        "lessonId": "math-u4-l2",
        "page": 143,
        "difficulty": "medium",
        "skillId": "calculation",
        "q": "ما مسافة نقطة من مستوى؟",
        "options": [
          {
            "text": "|Ax₀+By₀+Cz₀+D| / (A²+B²+C²)",
            "why_wrong": "حذفت الجذر من المقام."
          },
          {
            "text": "|Ax₀+By₀+Cz₀+D| / D",
            "why_wrong": "لا تُقسم على الثابت."
          },
          {
            "text": "Ax₀+By₀+Cz₀+D فقط",
            "why_wrong": " يجب أخذ القيمة المطلقة والقسمة على طول الطبيعي."
          },
          {
            "text": "|Ax₀+By₀+Cz₀+D| / √(A²+B²+C²)"
          }
        ],
        "answer": 3,
        "explain": "المسافة هي الإسقاط العمودي مقسوماً على |n|."
      },
      {
        "id": "qm-u4-03",
        "unitId": "u4",
        "lessonId": "math-u4-l3",
        "page": 149,
        "difficulty": "hard",
        "skillId": "analysis",
        "q": "ما طول القطر الفراغي لمكعب ضلعه a؟",
        "options": [
          {
            "text": "2a",
            "why_wrong": "هذا ضعف الضلع."
          },
          {
            "text": "3a",
            "why_wrong": "لا يُجمع الضلع ثلاث مرات."
          },
          {
            "text": "a√3"
          },
          {
            "text": "a√2",
            "why_wrong": "هذا قطر الوجه."
          }
        ],
        "answer": 2,
        "explain": "بفيثاغورس مرتين: d=√(a²+a²+a²)=a√3."
      },
      {
        "id": "qm-u4-04",
        "unitId": "u4",
        "lessonId": "math-u4-l1",
        "page": 136,
        "difficulty": "easy",
        "skillId": "application",
        "q": "إذا كانت زاوية مستقيم مع الطبيعي 30°، فما زاويته مع المستوى؟",
        "options": [
          {
            "text": "45°",
            "why_wrong": "المكمّل لـ 30° هو 60°."
          },
          {
            "text": "60°"
          },
          {
            "text": "30°",
            "why_wrong": "الزاويتان ليستا متساويتين."
          },
          {
            "text": "120°",
            "why_wrong": "الزاوية مع المستوى حادة مكمّلة."
          }
        ],
        "answer": 1,
        "explain": "θ = 90° − 30° = 60°."
      },
      {
        "id": "qm-u4-05",
        "unitId": "u4",
        "lessonId": "math-u4-l2",
        "page": 146,
        "difficulty": "medium",
        "skillId": "recall",
        "q": "متى يكون مستويان متعامدين؟",
        "options": [
          {
            "text": "عندما n₁·n₂ = 0"
          },
          {
            "text": "عندما n₁ = n₂",
            "why_wrong": "هذا يعني مستويين متوازيين."
          },
          {
            "text": "عندما n₁ = 2n₂",
            "why_wrong": "مضاعفة المتجه تعني توازياً."
          },
          {
            "text": "عندما |n₁| = |n₂|",
            "why_wrong": "تساوي الطولين لا يحدد الزاوية."
          }
        ],
        "answer": 0,
        "explain": "تعامد المتجهين الطبيعيين يعطي تعامد المستويين."
      },
      {
        "id": "qm-u4-06",
        "unitId": "u4",
        "lessonId": "math-u4-l3",
        "page": 152,
        "difficulty": "hard",
        "skillId": "calculation",
        "q": "ما cosφ بين المستوى xy والمستوى xz؟",
        "options": [
          {
            "text": "1",
            "why_wrong": "المتجهان (0,0,1) و (0,1,0) متعامدان."
          },
          {
            "text": "−1",
            "why_wrong": "ليسا متعاكسين."
          },
          {
            "text": "1/2",
            "why_wrong": "الزاوية 90° لا 60°."
          },
          {
            "text": "0"
          }
        ],
        "answer": 3,
        "explain": "n₁=(0,0,1)، n₂=(0,1,0)، جيب تمام الزاوية صفر."
      },
      {
        "id": "qm-u4-07",
        "unitId": "u4",
        "lessonId": "math-u4-l1",
        "page": 139,
        "difficulty": "easy",
        "skillId": "analysis",
        "q": "ما مسافة النقطة (1،2،5) من المستوى x = 3؟",
        "options": [
          {
            "text": "4",
            "why_wrong": "حسبت الإحداثي الخاطئ."
          },
          {
            "text": "√30",
            "why_wrong": "استخدمت طول متجه النقطة."
          },
          {
            "text": "2"
          },
          {
            "text": "3",
            "why_wrong": "هذا موضع المستوى من المبدأ."
          }
        ],
        "answer": 2,
        "explain": "المسافة = |1−3| = 2."
      },
      {
        "id": "qm-u4-08",
        "unitId": "u4",
        "lessonId": "math-u4-l2",
        "page": 144,
        "difficulty": "medium",
        "skillId": "application",
        "q": "ما زاوية المستقيم باتجاه (1،0،0) مع المستوى z = 0؟",
        "options": [
          {
            "text": "180°",
            "why_wrong": "الزاوية مع مستوى لا تُقاس هكذا."
          },
          {
            "text": "0°"
          },
          {
            "text": "90°",
            "why_wrong": "هذا مع المتجه الطبيعي لا مع المستوى."
          },
          {
            "text": "45°",
            "why_wrong": "لا يوجد ميل رأسي."
          }
        ],
        "answer": 1,
        "explain": "المتجه موازٍ للمستوى، فالزاوية صفر."
      },
      {
        "id": "qm-u4-09",
        "unitId": "u4",
        "lessonId": "math-u4-l3",
        "page": 148,
        "difficulty": "hard",
        "skillId": "recall",
        "q": "ما الزاوية بين المستويين xy و xz؟",
        "options": [
          {
            "text": "90°"
          },
          {
            "text": "0°",
            "why_wrong": "المستويان مختلفان و متعامدان."
          },
          {
            "text": "45°",
            "why_wrong": "لا يوجد ميل بمقدار 45°."
          },
          {
            "text": "180°",
            "why_wrong": "ليسا مستوى واحداً بعكس الاتجاه."
          }
        ],
        "answer": 0,
        "explain": "المتجهان الطبيعيان متعامدان."
      },
      {
        "id": "qm-u4-10",
        "unitId": "u4",
        "lessonId": "math-u4-l1",
        "page": 133,
        "difficulty": "easy",
        "skillId": "calculation",
        "q": "ما معادلة المستوى المار بالمبدأ وبطبيعي (0،0،1)؟",
        "options": [
          {
            "text": "x = 0",
            "why_wrong": "هذا طبيعيته (1،0،0)."
          },
          {
            "text": "y = 0",
            "why_wrong": "هذا طبيعيته (0،1،0)."
          },
          {
            "text": "x + y = 1",
            "why_wrong": "لا يمر بالمبدأ ولا طبيعيته المطلوبة."
          },
          {
            "text": "z = 0"
          }
        ],
        "answer": 3,
        "explain": "المعادلة 0x+0y+1z+0=0."
      },
      {
        "id": "qm-u4-11",
        "unitId": "u4",
        "lessonId": "math-u4-l2",
        "page": 142,
        "difficulty": "medium",
        "skillId": "analysis",
        "q": "ما معادلة مستقيم يمر بـ P واتجاهه u؟",
        "options": [
          {
            "text": "r = P/t",
            "why_wrong": "لا تمثل هذه معادلة خط مستقيم."
          },
          {
            "text": "r = u − tP",
            "why_wrong": "النقطة والاتجاه معكوسان."
          },
          {
            "text": "r = P + tu"
          },
          {
            "text": "r = P·u",
            "why_wrong": "هذا ناتج جداء لا معادلة مستقيم."
          }
        ],
        "answer": 2,
        "explain": "المعادلة المتجهية للمستقيم هي r=P+tu."
      },
      {
        "id": "qm-u4-12",
        "unitId": "u4",
        "lessonId": "math-u4-l3",
        "page": 151,
        "difficulty": "hard",
        "skillId": "application",
        "q": "ما مسافة المبدأ من المستوى 3x + 4y + 12z − 13 = 0؟",
        "options": [
          {
            "text": "1/13",
            "why_wrong": "قلبت النسبة."
          },
          {
            "text": "1"
          },
          {
            "text": "13",
            "why_wrong": "هذا البسط قبل القسمة."
          },
          {
            "text": "12",
            "why_wrong": "هذا أكبر معامل."
          }
        ],
        "answer": 1,
        "explain": "|−13|/√(9+16+144)=13/13=1."
      },
      {
        "id": "qm-u4-13",
        "unitId": "u4",
        "lessonId": "math-u4-l1",
        "page": 136,
        "difficulty": "easy",
        "skillId": "recall",
        "q": "إذا كان مستقيم موازياً لمستوى، فما زاويته مع الطبيعي؟",
        "options": [
          {
            "text": "90°"
          },
          {
            "text": "0°",
            "why_wrong": "هذه الزاوية مع المستوى."
          },
          {
            "text": "45°",
            "why_wrong": "لا يوجد ميل رأسي."
          },
          {
            "text": "180°",
            "why_wrong": "الزاوية مع طبيعي扼 مستوى تكون قائمة."
          }
        ],
        "answer": 0,
        "explain": "الموازي للمستوى عمودي على متجهه الطبيعي."
      },
      {
        "id": "qm-u4-14",
        "unitId": "u4",
        "lessonId": "math-u4-l2",
        "page": 145,
        "difficulty": "medium",
        "skillId": "calculation",
        "q": "ما قطر وجه مكعب ضلعه a؟",
        "options": [
          {
            "text": "a√3",
            "why_wrong": "هذا القطر الفراغي."
          },
          {
            "text": "2a",
            "why_wrong": "ضعف الضلع."
          },
          {
            "text": "a/√2",
            "why_wrong": "قلبت العلاقة."
          },
          {
            "text": "a√2"
          }
        ],
        "answer": 3,
        "explain": "قطر الوجه = √(a²+a²)=a√2."
      },
      {
        "id": "qm-u4-15",
        "unitId": "u4",
        "lessonId": "math-u4-l3",
        "page": 147,
        "difficulty": "hard",
        "skillId": "analysis",
        "q": "ما مسافة (1،1،1) من المستوى 2x − y + 2z − 4 = 0؟",
        "options": [
          {
            "text": "3",
            "why_wrong": "هذا المقام لا المسافة."
          },
          {
            "text": "2/3",
            "why_wrong": "حساب البسط خاطئ؛ البسط 1."
          },
          {
            "text": "1/3"
          },
          {
            "text": "1",
            "why_wrong": "المقام √(4+1+4)=3."
          }
        ],
        "answer": 2,
        "explain": "|2−1+2−4|/3 = 1/3."
      }
    ],
    "quiz-math-u5": [
      {
        "id": "qm-u5-01",
        "unitId": "u5",
        "lessonId": "math-u5-l1",
        "page": 74,
        "difficulty": "easy",
        "skillId": "recall",
        "q": "إذا كان P(A)=0.3 فما P(Aᶜ)؟",
        "options": [
          {
            "text": "0.7"
          },
          {
            "text": "0.3",
            "why_wrong": "المكمّل ليس الحدث نفسه."
          },
          {
            "text": "0.5",
            "why_wrong": "لا تُقسم الاحتمال على 2."
          },
          {
            "text": "1.3",
            "why_wrong": "الاحتمال لا يتجاوز 1."
          }
        ],
        "answer": 0,
        "explain": "P(Aᶜ)=1−P(A)=0.7."
      },
      {
        "id": "qm-u5-02",
        "unitId": "u5",
        "lessonId": "math-u5-l2",
        "page": 80,
        "difficulty": "medium",
        "skillId": "calculation",
        "q": "إذا كان A و B متنافيين، P(A)=0.4 و P(B)=0.3، فما P(A∪B)؟",
        "options": [
          {
            "text": "0.12",
            "why_wrong": "قاعدة الضرب للحدثين المستقلين، لا الجمع للمتنافيين."
          },
          {
            "text": "0.1",
            "why_wrong": "طرحت بدل جمعت."
          },
          {
            "text": "1",
            "why_wrong": "المجموع 0.7 وليس يقيناً."
          },
          {
            "text": "0.7"
          }
        ],
        "answer": 3,
        "explain": "للتنافي P(A∪B)=P(A)+P(B)."
      },
      {
        "id": "qm-u5-03",
        "unitId": "u5",
        "lessonId": "math-u5-l3",
        "page": 88,
        "difficulty": "hard",
        "skillId": "analysis",
        "q": "إذا كان A و B مستقلين، P(A)=0.5 و P(B)=0.2، فما P(A∩B)؟",
        "options": [
          {
            "text": "0.3",
            "why_wrong": "طرحت بدل ضربت."
          },
          {
            "text": "0.25",
            "why_wrong": "استخدمت P(B)=0.5."
          },
          {
            "text": "0.1"
          },
          {
            "text": "0.7",
            "why_wrong": "هذا الجمع، لا التقاطع."
          }
        ],
        "answer": 2,
        "explain": "للاستقلال P(A∩B)=P(A)P(B)=0.1."
      },
      {
        "id": "qm-u5-04",
        "unitId": "u5",
        "lessonId": "math-u5-l4",
        "page": 96,
        "difficulty": "easy",
        "skillId": "application",
        "q": "إذا كان P(A)=0.5، P(B)=0.4 و P(A∩B)=0.2، فما P(A∪B)؟",
        "options": [
          {
            "text": "1.1",
            "why_wrong": "الاحتمال لا يتجاوز 1."
          },
          {
            "text": "0.7"
          },
          {
            "text": "0.9",
            "why_wrong": "حسبت التقاطع مرتين."
          },
          {
            "text": "0.3",
            "why_wrong": "طرحت التقاطع من حد واحد فقط."
          }
        ],
        "answer": 1,
        "explain": "0.5+0.4−0.2=0.7."
      },
      {
        "id": "qm-u5-05",
        "unitId": "u5",
        "lessonId": "math-u5-l5",
        "page": 102,
        "difficulty": "medium",
        "skillId": "recall",
        "q": "إذا كان P(A∩B)=0.2 و P(B)=0.5، فما P(A|B)؟",
        "options": [
          {
            "text": "0.4"
          },
          {
            "text": "0.1",
            "why_wrong": "ضربت بدل قسمت."
          },
          {
            "text": "0.7",
            "why_wrong": "جمعت بدل قسمت."
          },
          {
            "text": "2.5",
            "why_wrong": "قلبت البسط والمقام."
          }
        ],
        "answer": 0,
        "explain": "P(A|B)=0.2/0.5=0.4."
      },
      {
        "id": "qm-u5-06",
        "unitId": "u5",
        "lessonId": "math-u5-l1",
        "page": 74,
        "difficulty": "hard",
        "skillId": "calculation",
        "q": "ما مجموع احتمالات كل النتجات المتنافية في فضاء العينة؟",
        "options": [
          {
            "text": "0",
            "why_wrong": "هذا مستحيل لمجموع كامل."
          },
          {
            "text": "∞",
            "why_wrong": "الاحتمال محدود."
          },
          {
            "text": "يعتمد على التجربة",
            "why_wrong": "المجموع دائماً 1."
          },
          {
            "text": "1"
          }
        ],
        "answer": 3,
        "explain": "مجموع فضاء العينة يساوي 1."
      },
      {
        "id": "qm-u5-07",
        "unitId": "u5",
        "lessonId": "math-u5-l2",
        "page": 85,
        "difficulty": "easy",
        "skillId": "analysis",
        "q": "عند رمي عملة مرتين، ما احتمال HH؟",
        "options": [
          {
            "text": "1/3",
            "why_wrong": "فضاء العينة له 4 نتجات متساوية."
          },
          {
            "text": "1/8",
            "why_wrong": "هذا لثلاث رميات."
          },
          {
            "text": "1/4"
          },
          {
            "text": "1/2",
            "why_wrong": "هذا احتمال نتيجة واحدة في رمية واحدة."
          }
        ],
        "answer": 2,
        "explain": "النتجات: HH, HT, TH, TT، إذن 1/4."
      },
      {
        "id": "qm-u5-08",
        "unitId": "u5",
        "lessonId": "math-u5-l3",
        "page": 86,
        "difficulty": "medium",
        "skillId": "application",
        "q": "عند رمي نرد عادل، ما احتمال ظهور عدد زوجي؟",
        "options": [
          {
            "text": "2/3",
            "why_wrong": "هذا احتمال الفردي أو الزوجي معاً خطأً."
          },
          {
            "text": "1/2"
          },
          {
            "text": "1/6",
            "why_wrong": "هذا احتمال رقم واحد."
          },
          {
            "text": "1/3",
            "why_wrong": "الأعداد الزوجية 2 و 4 و 6 من أصل 6."
          }
        ],
        "answer": 1,
        "explain": "3 نتجات زوجية من 6."
      },
      {
        "id": "qm-u5-09",
        "unitId": "u5",
        "lessonId": "math-u5-l4",
        "page": 96,
        "difficulty": "hard",
        "skillId": "recall",
        "q": "في 5 تجارب برنولي p=0.5، ما احتمال نجاحين بالضبط؟",
        "options": [
          {
            "text": "10/32"
          },
          {
            "text": "5/32",
            "why_wrong": "نسيت C(5,2)=10."
          },
          {
            "text": "10/16",
            "why_wrong": "المقام يجب أن يكون 2⁵=32."
          },
          {
            "text": "1/32",
            "why_wrong": "هذا احتمال حالة واحدة فقط."
          }
        ],
        "answer": 0,
        "explain": "C(5,2)(0.5)²(0.5)³=10/32."
      },
      {
        "id": "qm-u5-10",
        "unitId": "u5",
        "lessonId": "math-u5-l5",
        "page": 101,
        "difficulty": "easy",
        "skillId": "calculation",
        "q": "إذا كان A و B مستقلين، فما P(A|B)؟",
        "options": [
          {
            "text": "P(A∩B)",
            "why_wrong": "هذا احتمال تقاطع، لا شرطي."
          },
          {
            "text": "0",
            "why_wrong": "الشرط لا يلغي الاحتمال."
          },
          {
            "text": "1−P(A)",
            "why_wrong": "هذا احتمال المكمّل."
          },
          {
            "text": "P(A)"
          }
        ],
        "answer": 3,
        "explain": "الاستقلال يعني أن الشرط لا يغيّر الاحتمال."
      },
      {
        "id": "qm-u5-11",
        "unitId": "u5",
        "lessonId": "math-u5-l1",
        "page": 74,
        "difficulty": "medium",
        "skillId": "analysis",
        "q": "أي علاقة صحيحة دائماً؟",
        "options": [
          {
            "text": "P(A∩B)>P(A)",
            "why_wrong": "التقاطع لا يمكن أن يتجاوز أحد الحدثين."
          },
          {
            "text": "P(A∩B)=0 دائماً",
            "why_wrong": "فقط للمتنافيين."
          },
          {
            "text": "P(A∩B) ≤ P(A)"
          },
          {
            "text": "P(A∩B)=P(A) دائماً",
            "why_wrong": "يحدث فقط إذا B يضم A."
          }
        ],
        "answer": 2,
        "explain": "التقاطع جزء من A، فاحتماله لا يتجاوز احتمال A."
      },
      {
        "id": "qm-u5-12",
        "unitId": "u5",
        "lessonId": "math-u5-l2",
        "page": 83,
        "difficulty": "hard",
        "skillId": "application",
        "q": "السحب دون إرجاع يجعل الحدثين",
        "options": [
          {
            "text": "احتمال كل منهما 1",
            "why_wrong": "ليس بالضرورة."
          },
          {
            "text": "غير مستقلين"
          },
          {
            "text": "مستقلين",
            "why_wrong": "السحب يغيّر احتمال الثاني."
          },
          {
            "text": "متنافيين دائماً",
            "why_wrong": "قد يحصل كلاهما في سحبتين."
          }
        ],
        "answer": 1,
        "explain": "تغيّر فضاء العينة بعد السحب يلغي الاستقلال."
      },
      {
        "id": "qm-u5-13",
        "unitId": "u5",
        "lessonId": "math-u5-l3",
        "page": 91,
        "difficulty": "easy",
        "skillId": "recall",
        "q": "متى يساوي P(A∪B)=P(A)+P(B)؟",
        "options": [
          {
            "text": "عند تنافي A و B"
          },
          {
            "text": "عند استقلالهما",
            "why_wrong": "الاستقلال يعطي ضرب التقاطع لا إلغاءه."
          },
          {
            "text": "عند تساويهما",
            "why_wrong": "لا علاقة لذلك."
          },
          {
            "text": "عند كمالهما",
            "why_wrong": "التكامل يعطي مجموع 1، لكن التقاطع معدوم فقط عند التنافي."
          }
        ],
        "answer": 0,
        "explain": "يُحذف الحد P(A∩B) فقط إذا كان التقاطع صفراً."
      },
      {
        "id": "qm-u5-14",
        "unitId": "u5",
        "lessonId": "math-u5-l4",
        "page": 96,
        "difficulty": "medium",
        "skillId": "calculation",
        "q": "ما شرط التوزيع ذي الحدين؟",
        "options": [
          {
            "text": "سحب مع إرجاع فقط",
            "why_wrong": "ليس شرطاً حصرياً."
          },
          {
            "text": "احتمال متغير في كل تجربة",
            "why_wrong": "يجب أن يكون p ثابتاً."
          },
          {
            "text": "تجارب مؤثرة",
            "why_wrong": "يجب أن تكون مستقلة."
          },
          {
            "text": "تجارب مستقلة واحتمال نجاح ثابت"
          }
        ],
        "answer": 3,
        "explain": "التوزيع ذو الحدين يتطلب n تجارب مستقلة و p ثابت."
      },
      {
        "id": "qm-u5-15",
        "unitId": "u5",
        "lessonId": "math-u5-l5",
        "page": 100,
        "difficulty": "hard",
        "skillId": "analysis",
        "q": "في تجربتين مستقلتين p=0.5، ما احتمال نجاح واحدة على الأقل؟",
        "options": [
          {
            "text": "0.25",
            "why_wrong": "هذا احتمال الفشل في التجربتين."
          },
          {
            "text": "1",
            "why_wrong": "لا يوجد يقين بالنجاح."
          },
          {
            "text": "0.75"
          },
          {
            "text": "0.5",
            "why_wrong": "هذا احتمال نجاح واحدة بالضبط في تجربة واحدة."
          }
        ],
        "answer": 2,
        "explain": "1−P(فشلان)=1−0.25=0.75."
      }
    ],
    "quiz-math-u6": [
      {
        "id": "qm-u6-01",
        "unitId": "u6",
        "lessonId": "math-u6-l1",
        "page": 154,
        "difficulty": "easy",
        "skillId": "recall",
        "q": "ما مشتقة x⁵؟",
        "options": [
          {
            "text": "5x⁴"
          },
          {
            "text": "x⁴",
            "why_wrong": "نسيت ضرب الأس الأصلي."
          },
          {
            "text": "5x⁵",
            "why_wrong": "لم ينقص الأس."
          },
          {
            "text": "4x⁴",
            "why_wrong": "استخدمت ناتج التنقيص بدل الأس الأصلي."
          }
        ],
        "answer": 0,
        "explain": "(xⁿ)′=nxⁿ⁻¹."
      },
      {
        "id": "qm-u6-02",
        "unitId": "u6",
        "lessonId": "math-u6-l2",
        "page": 161,
        "difficulty": "medium",
        "skillId": "calculation",
        "q": "ما مشتقة الثابت 7؟",
        "options": [
          {
            "text": "7",
            "why_wrong": "الثابت لا يتغير."
          },
          {
            "text": "1",
            "why_wrong": "مشتقة x هي 1 لا مشتقة الثابت."
          },
          {
            "text": "غير معرفة",
            "why_wrong": "مشتقة الثابت معرفة وتساوي صفراً."
          },
          {
            "text": "0"
          }
        ],
        "answer": 3,
        "explain": "معدل تغير الثابت صفر."
      },
      {
        "id": "qm-u6-03",
        "unitId": "u6",
        "lessonId": "math-u6-l3",
        "page": 168,
        "difficulty": "hard",
        "skillId": "analysis",
        "q": "إذا كان f(x)=x³، فما f′(2)؟",
        "options": [
          {
            "text": "6",
            "why_wrong": "حسبت 3×2 بدل 3×2²."
          },
          {
            "text": "3",
            "why_wrong": "هذا الأس فقط."
          },
          {
            "text": "12"
          },
          {
            "text": "8",
            "why_wrong": "هذا f(2) لا المشتقة."
          }
        ],
        "answer": 2,
        "explain": "f′(x)=3x²، إذن f′(2)=12."
      },
      {
        "id": "qm-u6-04",
        "unitId": "u6",
        "lessonId": "math-u6-l4",
        "page": 174,
        "difficulty": "easy",
        "skillId": "application",
        "q": "ما مشتقة x² sinx باستخدام قاعدة الجداء؟",
        "options": [
          {
            "text": "2x sinx فقط",
            "why_wrong": "نسيت مشتقة العامل الثاني."
          },
          {
            "text": "2x sinx + x² cosx"
          },
          {
            "text": "2x cosx",
            "why_wrong": "حذفت حداً من قاعدة الجداء."
          },
          {
            "text": "x² cosx فقط",
            "why_wrong": "نسيت مشتقة العامل الأول."
          }
        ],
        "answer": 1,
        "explain": "(uv)′=u′v+uv′."
      },
      {
        "id": "qm-u6-05",
        "unitId": "u6",
        "lessonId": "math-u6-l5",
        "page": 179,
        "difficulty": "medium",
        "skillId": "recall",
        "q": "ما مشتقة (3x+1)⁴؟",
        "options": [
          {
            "text": "12(3x+1)³"
          },
          {
            "text": "4(3x+1)³",
            "why_wrong": "نسيت مشتقة الداخل 3."
          },
          {
            "text": "3(3x+1)⁴",
            "why_wrong": "لم تنقص الأس."
          },
          {
            "text": "(3x+1)³",
            "why_wrong": "حذفت العاملين 4 و 3."
          }
        ],
        "answer": 0,
        "explain": "قاعدة السلسلة: 4(3x+1)³×3."
      },
      {
        "id": "qm-u6-06",
        "unitId": "u6",
        "lessonId": "math-u6-l6",
        "page": 184,
        "difficulty": "hard",
        "skillId": "calculation",
        "q": "ما مشتقة 1/x؟",
        "options": [
          {
            "text": "1/x²",
            "why_wrong": "أخطأت في الإشارة."
          },
          {
            "text": "−1/x",
            "why_wrong": "لم تطبق قاعدة القوة بشكل صحيح."
          },
          {
            "text": "ln x",
            "why_wrong": "هذا تكامل 1/x."
          },
          {
            "text": "−1/x²"
          }
        ],
        "answer": 3,
        "explain": "1/x = x⁻¹، فمشتقتها −x⁻²."
      },
      {
        "id": "qm-u6-07",
        "unitId": "u6",
        "lessonId": "math-u6-l7",
        "page": 193,
        "difficulty": "easy",
        "skillId": "analysis",
        "q": "ما مشتقة √x؟",
        "options": [
          {
            "text": "2√x",
            "why_wrong": "هذا تكامل تقريبي خاطئ."
          },
          {
            "text": "√x/2",
            "why_wrong": "ليست الصيغة الصحيحة."
          },
          {
            "text": "1/(2√x)"
          },
          {
            "text": "1/√x",
            "why_wrong": "نسيت العامل 2."
          }
        ],
        "answer": 2,
        "explain": "√x = x^(1/2)، فالمشتقة (1/2)x^(−1/2)."
      },
      {
        "id": "qm-u6-08",
        "unitId": "u6",
        "lessonId": "math-u6-l8",
        "page": 207,
        "difficulty": "medium",
        "skillId": "application",
        "q": "ما ميل مماس f(x)=x² عند x=3؟",
        "options": [
          {
            "text": "2",
            "why_wrong": "هذا الأس."
          },
          {
            "text": "6"
          },
          {
            "text": "3",
            "why_wrong": "هذا موضع النقطة لا الميل."
          },
          {
            "text": "9",
            "why_wrong": "هذا قيمة الدالة."
          }
        ],
        "answer": 1,
        "explain": "f′(x)=2x، إذن f′(3)=6."
      },
      {
        "id": "qm-u6-09",
        "unitId": "u6",
        "lessonId": "math-u6-l1",
        "page": 156,
        "difficulty": "hard",
        "skillId": "recall",
        "q": "ما النقطة الحرجة لـ f(x)=x²−6x+1؟",
        "options": [
          {
            "text": "x = 3"
          },
          {
            "text": "x = 6",
            "why_wrong": "حللت المعادلة خطأً."
          },
          {
            "text": "x = 1",
            "why_wrong": "هذا الثابت."
          },
          {
            "text": "x = −3",
            "why_wrong": "أخطأت في إشارة b."
          }
        ],
        "answer": 0,
        "explain": "f′(x)=2x−6=0، إذن x=3."
      },
      {
        "id": "qm-u6-10",
        "unitId": "u6",
        "lessonId": "math-u6-l2",
        "page": 163,
        "difficulty": "easy",
        "skillId": "calculation",
        "q": "ماذا يعني f″(x)>0 عند نقطة حرجة؟",
        "options": [
          {
            "text": "قيمة كبرى محلية",
            "why_wrong": "التقعر للأعلى يعطي صغرى."
          },
          {
            "text": "نقطة انعطاف دائماً",
            "why_wrong": "تحتاج تغيّر إشارة المشتقة الثانية."
          },
          {
            "text": "المشتقة الأولى معدومة دائماً",
            "why_wrong": "ليس شرطاً كافياً."
          },
          {
            "text": "قيمة صغرى محلية"
          }
        ],
        "answer": 3,
        "explain": "اختبار المشتقة الثانية: f″>0 يعطي قيمة صغرى."
      },
      {
        "id": "qm-u6-11",
        "unitId": "u6",
        "lessonId": "math-u6-l3",
        "page": 166,
        "difficulty": "medium",
        "skillId": "analysis",
        "q": "للدالة f(x)=x² على [1،4]، ما c في نظرية القيمة المتوسطة؟",
        "options": [
          {
            "text": "3",
            "why_wrong": "ليس داخل الحل الصحيح."
          },
          {
            "text": "5",
            "why_wrong": "هذا ميل القطرة لا c."
          },
          {
            "text": "2.5"
          },
          {
            "text": "2",
            "why_wrong": "ميل القطرة 5، و2c=5."
          }
        ],
        "answer": 2,
        "explain": "(16−1)/(4−1)=5، و f′(c)=2c=5، إذن c=2.5."
      },
      {
        "id": "qm-u6-12",
        "unitId": "u6",
        "lessonId": "math-u6-l4",
        "page": 174,
        "difficulty": "hard",
        "skillId": "application",
        "q": "ما مشتقة 5x³ − 2x؟",
        "options": [
          {
            "text": "15x² + 2",
            "why_wrong": "أخطأت في إشارة مشتقة −2x."
          },
          {
            "text": "15x² − 2"
          },
          {
            "text": "15x²",
            "why_wrong": "نسيت مشتقة −2x."
          },
          {
            "text": "5x³ − 2",
            "why_wrong": "لم تشتق الحد الأول."
          }
        ],
        "answer": 1,
        "explain": "نشتق كل حد على حدة."
      },
      {
        "id": "qm-u6-13",
        "unitId": "u6",
        "lessonId": "math-u6-l5",
        "page": 179,
        "difficulty": "easy",
        "skillId": "recall",
        "q": "ما مشتقة (x+2)²؟",
        "options": [
          {
            "text": "2(x+2)"
          },
          {
            "text": "2x + 2",
            "why_wrong": "التوسيع يعطي x²+4x+4، ومشتقته 2x+4."
          },
          {
            "text": "(x+2)",
            "why_wrong": "نسيت ضرب الأس."
          },
          {
            "text": "2",
            "why_wrong": "هذا الأس فقط."
          }
        ],
        "answer": 0,
        "explain": "قاعدة السلسلة تعطي 2(x+2)×1."
      },
      {
        "id": "qm-u6-14",
        "unitId": "u6",
        "lessonId": "math-u6-l6",
        "page": 184,
        "difficulty": "medium",
        "skillId": "calculation",
        "q": "ماذا تمثل مشتقة الموضع بالنسبة للزمن؟",
        "options": [
          {
            "text": "التكامل",
            "why_wrong": "التكامل يعطي الموضع من السرعة."
          },
          {
            "text": "التسارع",
            "why_wrong": "التسارع مشتقة السرعة."
          },
          {
            "text": "الزمن",
            "why_wrong": "الزمن هو المتغير المستقل."
          },
          {
            "text": "السرعة"
          }
        ],
        "answer": 3,
        "explain": "v(t)=ds/dt."
      },
      {
        "id": "qm-u6-15",
        "unitId": "u6",
        "lessonId": "math-u6-l7",
        "page": 188,
        "difficulty": "hard",
        "skillId": "analysis",
        "q": "ما مماس f(x)=x² عند x=1؟",
        "options": [
          {
            "text": "y − 1 = x − 1",
            "why_wrong": "الميل يجب أن يكون 2."
          },
          {
            "text": "y = x²",
            "why_wrong": "هذا المنحنى نفسه."
          },
          {
            "text": "y − 1 = 2(x − 1)"
          },
          {
            "text": "y = 2x",
            "why_wrong": "هذا y=2x، لا يمر بنقطة (1،1)."
          }
        ],
        "answer": 2,
        "explain": "الميل f′(1)=2، ويمر بـ (1،1)."
      }
    ],
    "quiz-math-u7": [
      {
        "id": "qm-u7-01",
        "unitId": "u7",
        "lessonId": "math-u7-l1",
        "page": 210,
        "difficulty": "easy",
        "skillId": "recall",
        "q": "ما ∫x³dx؟",
        "options": [
          {
            "text": "x⁴/4 + C"
          },
          {
            "text": "3x² + C",
            "why_wrong": "هذه مشتقة x³ لا تكاملها."
          },
          {
            "text": "x⁴ + C",
            "why_wrong": "نسيت القسمة على الأس الجديد."
          },
          {
            "text": "x⁴/3 + C",
            "why_wrong": "قسمت على الأس القديم."
          }
        ],
        "answer": 0,
        "explain": "∫xⁿdx=xⁿ⁺¹/(n+1)+C."
      },
      {
        "id": "qm-u7-02",
        "unitId": "u7",
        "lessonId": "math-u7-l2",
        "page": 223,
        "difficulty": "medium",
        "skillId": "calculation",
        "q": "ما ∫5dx؟",
        "options": [
          {
            "text": "5 + C",
            "why_wrong": "تكامل الثابت يعطي الثابت مضروباً في x."
          },
          {
            "text": "x⁵/5 + C",
            "why_wrong": "خلطت بين x⁵ والثابت 5."
          },
          {
            "text": "0",
            "why_wrong": "مشتقة الثابت صفر، لا تكامله."
          },
          {
            "text": "5x + C"
          }
        ],
        "answer": 3,
        "explain": "∫k dx = kx + C."
      },
      {
        "id": "qm-u7-03",
        "unitId": "u7",
        "lessonId": "math-u7-l3",
        "page": 237,
        "difficulty": "hard",
        "skillId": "analysis",
        "q": "ما ∫(2x+1)dx؟",
        "options": [
          {
            "text": "2x² + x + C",
            "why_wrong": "∫2x = x² لا 2x²."
          },
          {
            "text": "x² + 1 + C",
            "why_wrong": "∫1 = x وليس 1."
          },
          {
            "text": "x² + x + C"
          },
          {
            "text": "x² + C",
            "why_wrong": "نسيت تكامل الثابت 1."
          }
        ],
        "answer": 2,
        "explain": "نكامل كل حد على حدة."
      },
      {
        "id": "qm-u7-04",
        "unitId": "u7",
        "lessonId": "math-u7-l4",
        "page": 243,
        "difficulty": "easy",
        "skillId": "application",
        "q": "ما ∫₁³ x²dx؟",
        "options": [
          {
            "text": "8/3",
            "why_wrong": "حسبت 3³−1 خطأً."
          },
          {
            "text": "26/3"
          },
          {
            "text": "9",
            "why_wrong": "هذا 3²، لا التكامل."
          },
          {
            "text": "26",
            "why_wrong": "نسيت القسمة على 3."
          }
        ],
        "answer": 1,
        "explain": "[x³/3]₁³=(27−1)/3=26/3."
      },
      {
        "id": "qm-u7-05",
        "unitId": "u7",
        "lessonId": "math-u7-l5",
        "page": 244,
        "difficulty": "medium",
        "skillId": "recall",
        "q": "ما ∫₀² 2xdx؟",
        "options": [
          {
            "text": "4"
          },
          {
            "text": "2",
            "why_wrong": "هذا حاصل الضرب 2×1."
          },
          {
            "text": "8",
            "why_wrong": "حسبت 2³/1."
          },
          {
            "text": "1",
            "why_wrong": "نسيت الحدود."
          }
        ],
        "answer": 0,
        "explain": "[x²]₀²=4."
      },
      {
        "id": "qm-u7-06",
        "unitId": "u7",
        "lessonId": "math-u7-l6",
        "page": 249,
        "difficulty": "hard",
        "skillId": "calculation",
        "q": "ما نص مبرهنة التحليل الأساسية للتكامل المحدد؟",
        "options": [
          {
            "text": "F(a) − F(b)",
            "why_wrong": "عكست الإشارة."
          },
          {
            "text": "F(a) + F(b)",
            "why_wrong": "ال طرح هو الصحيح."
          },
          {
            "text": "f(b) − f(a)",
            "why_wrong": "نستخدم المضاد F لا الدالة f."
          },
          {
            "text": "∫ₐᵇf(x)dx = F(b) − F(a)"
          }
        ],
        "answer": 3,
        "explain": "التكامل المحدد = الفرق بين قيم المضاد عند الحدين."
      },
      {
        "id": "qm-u7-07",
        "unitId": "u7",
        "lessonId": "math-u7-l7",
        "page": 253,
        "difficulty": "easy",
        "skillId": "analysis",
        "q": "لماذا لا يظهر ثابت التكامل C في التكامل المحدد؟",
        "options": [
          {
            "text": "لأن التكامل المحدد لا يملك مضاداً",
            "why_wrong": "له مضاد، لكن الطرح يُلغي C."
          },
          {
            "text": "لأن الحدود تجعله 1",
            "why_wrong": "لا علاقة لهذا."
          },
          {
            "text": "لأنه يُلغى عند الطرح"
          },
          {
            "text": "لأنه يساوي صفراً دائماً",
            "why_wrong": "C اختياري وليس صفراً بالضرورة."
          }
        ],
        "answer": 2,
        "explain": "(F(b)+C)−(F(a)+C)=F(b)−F(a)."
      },
      {
        "id": "qm-u7-08",
        "unitId": "u7",
        "lessonId": "math-u7-l1",
        "page": 217,
        "difficulty": "medium",
        "skillId": "application",
        "q": "ما المساحة تحت y=x من 0 إلى 2؟",
        "options": [
          {
            "text": "8",
            "why_wrong": "حسبت تكامل 2x."
          },
          {
            "text": "2"
          },
          {
            "text": "4",
            "why_wrong": "هذا مربع الحد الأعلى."
          },
          {
            "text": "1",
            "why_wrong": "هذا نصف الحد الأعلى فقط."
          }
        ],
        "answer": 1,
        "explain": "∫₀²x dx=[x²/2]₀²=2."
      },
      {
        "id": "qm-u7-09",
        "unitId": "u7",
        "lessonId": "math-u7-l2",
        "page": 230,
        "difficulty": "hard",
        "skillId": "recall",
        "q": "ما ∫₀¹ x²dx؟",
        "options": [
          {
            "text": "1/3"
          },
          {
            "text": "1",
            "why_wrong": "نسيت القسمة على 3."
          },
          {
            "text": "3",
            "why_wrong": "عكست القسمة."
          },
          {
            "text": "2/3",
            "why_wrong": "حسبت حداً آخر."
          }
        ],
        "answer": 0,
        "explain": "[x³/3]₀¹=1/3."
      },
      {
        "id": "qm-u7-10",
        "unitId": "u7",
        "lessonId": "math-u7-l3",
        "page": 239,
        "difficulty": "easy",
        "skillId": "calculation",
        "q": "ما ∫(x²+3x)dx؟",
        "options": [
          {
            "text": "x³/3 + 3x² + C",
            "why_wrong": "∫3x = 3x²/2."
          },
          {
            "text": "x³ + 3x²/2 + C",
            "why_wrong": "∫x² = x³/3."
          },
          {
            "text": "2x + 3 + C",
            "why_wrong": "هذا لا علاقة له بالتكامل."
          },
          {
            "text": "x³/3 + 3x²/2 + C"
          }
        ],
        "answer": 3,
        "explain": "نطبق خطية التكامل وقاعدة القوة."
      },
      {
        "id": "qm-u7-11",
        "unitId": "u7",
        "lessonId": "math-u7-l4",
        "page": 242,
        "difficulty": "medium",
        "skillId": "analysis",
        "q": "ما صيغة حجم مجسم الدوران حول محور x؟",
        "options": [
          {
            "text": "V = π∫ₐᵇf(x)dx",
            "why_wrong": "يجب تربيع f(x)."
          },
          {
            "text": "V = 2π∫ₐᵇf(x)dx",
            "why_wrong": "هذه صيغة أخرى غير صحيحة هنا."
          },
          {
            "text": "V = π∫ₐᵇ[f(x)]²dx"
          },
          {
            "text": "V = ∫ₐᵇf(x)dx",
            "why_wrong": "ينقص مربع نصف القطر وπ."
          }
        ],
        "answer": 2,
        "explain": "كل قرص حجمه π[f(x)]²dx."
      },
      {
        "id": "qm-u7-12",
        "unitId": "u7",
        "lessonId": "math-u7-l5",
        "page": 247,
        "difficulty": "hard",
        "skillId": "application",
        "q": "ما حجم دوران y=x حول محور x من 0 إلى 1؟",
        "options": [
          {
            "text": "3π",
            "why_wrong": "عكست القسمة."
          },
          {
            "text": "π/3"
          },
          {
            "text": "π",
            "why_wrong": "نسيت التكامل الصحيح."
          },
          {
            "text": "π/2",
            "why_wrong": "حسبت ∫x بدل ∫x²."
          }
        ],
        "answer": 1,
        "explain": "π∫₀¹x²dx=π/3."
      },
      {
        "id": "qm-u7-13",
        "unitId": "u7",
        "lessonId": "math-u7-l6",
        "page": 248,
        "difficulty": "easy",
        "skillId": "recall",
        "q": "ما قيمة ∫ₐᵇf(x)dx + ∫ᵇₐf(x)dx؟",
        "options": [
          {
            "text": "0"
          },
          {
            "text": "2∫ₐᵇf(x)dx",
            "why_wrong": "الحدود المعكوسة تعطي الإشارة المعاكسة."
          },
          {
            "text": "F(a)",
            "why_wrong": "ليس طرفاً واحداً."
          },
          {
            "text": "غير معرفة",
            "why_wrong": "العلاقة معرفة."
          }
        ],
        "answer": 0,
        "explain": "تبديل الحدود يغير إشارة التكامل."
      },
      {
        "id": "qm-u7-14",
        "unitId": "u7",
        "lessonId": "math-u7-l7",
        "page": 255,
        "difficulty": "medium",
        "skillId": "calculation",
        "q": "ما المساحة بين f(x)=2 و g(x)=x/2 من 0 إلى 2؟",
        "options": [
          {
            "text": "2",
            "why_wrong": "حسبت مستطيلاً فقط."
          },
          {
            "text": "4",
            "why_wrong": "حسبت f(2)×2 دون طرح المثلث."
          },
          {
            "text": "1",
            "why_wrong": "هذا نصف المساحة."
          },
          {
            "text": "3"
          }
        ],
        "answer": 3,
        "explain": "∫₀²(2−x/2)dx=3."
      },
      {
        "id": "qm-u7-15",
        "unitId": "u7",
        "lessonId": "math-u7-l1",
        "page": 212,
        "difficulty": "hard",
        "skillId": "analysis",
        "q": "إذا كانت f فردية على [−a،a]، فما ∫₋ₐᵃf(x)dx؟",
        "options": [
          {
            "text": "مساحة موجبة دائماً",
            "why_wrong": "السالب والموجب يلغيان."
          },
          {
            "text": "يعتمد على a",
            "why_wrong": "النتيجة صفر لأي a."
          },
          {
            "text": "0"
          },
          {
            "text": "2∫₀ᵃf(x)dx",
            "why_wrong": "هذه صحيحة للدوال الزوجية."
          }
        ],
        "answer": 2,
        "explain": "تكامل الدالة الفردية على فترة متماثلة يساوي صفراً."
      }
    ]
  },
  "glossary": {
    "v-complex": {
      "id": "v-complex",
      "term": "العدد المركب",
      "definition": "عدد على الصورة a + bi حيث a و b حقيقيان و i² = −1.",
      "unit_id": "u1",
      "page": 7
    },
    "v-imaginary": {
      "id": "v-imaginary",
      "term": "الوحدة التخيلية",
      "definition": "العدد i الذي يحقق i² = −1.",
      "unit_id": "u1",
      "page": 7
    },
    "v-argand": {
      "id": "v-argand",
      "term": "مستوى أرغاند",
      "definition": "مستوى إحداثيات يمثل فيه العدد المركب a + bi بالنقطة (a، b).",
      "unit_id": "u1",
      "page": 16
    },
    "v-modulus": {
      "id": "v-modulus",
      "term": "القيمة المطلقة",
      "definition": "طول متجه العدد المركب من مبدأ الإحداثيات: |z| = √(a²+b²).",
      "unit_id": "u1",
      "page": 19
    },
    "v-argument": {
      "id": "v-argument",
      "term": "سعة العدد المركب",
      "definition": "الزاوية بين متجه العدد المركب والمحور الحقيقي الموجب.",
      "unit_id": "u1",
      "page": 23
    },
    "v-polar": {
      "id": "v-polar",
      "term": "الصيغة القطبية",
      "definition": "كتابة العدد المركب على الصورة r(cosθ + i sinθ).",
      "unit_id": "u1",
      "page": 33
    },
    "v-demoivre": {
      "id": "v-demoivre",
      "term": "مبرهنة دي موافر",
      "definition": "قاعدة لرفع الأعداد المركبة المكتوبة بالصيغة القطبية إلى قوة n.",
      "unit_id": "u2",
      "page": 45
    },
    "v-root": {
      "id": "v-root",
      "term": "الجذر النوني",
      "definition": "أي عدد مركب w يحقق wⁿ = z.",
      "unit_id": "u2",
      "page": 49
    },
    "v-binomial": {
      "id": "v-binomial",
      "term": "التوسعة ذات الحدين",
      "definition": "صيغة لتوسيع (a+b)ⁿ باستخدام المعاملات C(n,k).",
      "unit_id": "u2",
      "page": 55
    },
    "v-conic": {
      "id": "v-conic",
      "term": "القطع المخروطي",
      "definition": "منحنى ينشأ من تقاطع مستوى مع مخروط دائري، أو بمجموع/فرق/nسبة بعدين ثابتة.",
      "unit_id": "u3",
      "page": 104
    },
    "v-focus": {
      "id": "v-focus",
      "term": "البؤرة",
      "definition": "نقطة ثابتة تستخدم في تعريف القطع المخروطي.",
      "unit_id": "u3",
      "page": 104
    },
    "v-directrix": {
      "id": "v-directrix",
      "term": "الدليل",
      "definition": "مستقيم ثابت يستخدم في تعريف القطع المخروطي.",
      "unit_id": "u3",
      "page": 104
    },
    "v-eccentricity": {
      "id": "v-eccentricity",
      "term": "الانحراف",
      "definition": "النسبة e = PF/PD، وتحدد نوع القطع المخروطي.",
      "unit_id": "u3",
      "page": 104
    },
    "v-ellipse": {
      "id": "v-ellipse",
      "term": "القطع الناقص",
      "definition": "مجموع بعدي أي نقطة فيه عن بؤرتين ثابت.",
      "unit_id": "u3",
      "page": 110
    },
    "v-hyperbola": {
      "id": "v-hyperbola",
      "term": "القطع الزائد",
      "definition": "الفرق المطلق لبعدي أي نقطة فيه عن بؤرتين ثابت.",
      "unit_id": "u3",
      "page": 118
    },
    "v-parabola": {
      "id": "v-parabola",
      "term": "القطع المكافئ",
      "definition": "مجموعة نقاط متساوية البعد عن بؤرة ودليل ثابتين.",
      "unit_id": "u3",
      "page": 124
    },
    "v-asymptote": {
      "id": "v-asymptote",
      "term": "الخط المقارب",
      "definition": "خط يقترب منه منحنى القطع الزائد دون أن يلمسه.",
      "unit_id": "u3",
      "page": 118
    },
    "v-plane": {
      "id": "v-plane",
      "term": "المستوى",
      "definition": "مجموعة نقاط تحقق معادلة خطية Ax + By + Cz + D = 0 في الفراغ.",
      "unit_id": "u4",
      "page": 133
    },
    "v-normal": {
      "id": "v-normal",
      "term": "المتجه الطبيعي",
      "definition": "متجه عمودي على المستوى ومعاملاته (A، B، C).",
      "unit_id": "u4",
      "page": 133
    },
    "v-space-diagonal": {
      "id": "v-space-diagonal",
      "term": "القطر الفراغي",
      "definition": "القط الواصل بين رأسين متقابلين في مكعب وطوله a√3.",
      "unit_id": "u4",
      "page": 136
    },
    "v-dihedral": {
      "id": "v-dihedral",
      "term": "الزاوية ثنائية الوجه",
      "definition": "الزاوية بين مستويين تقاس من متجهيهما الطبيعيين.",
      "unit_id": "u4",
      "page": 147
    },
    "v-probability": {
      "id": "v-probability",
      "term": "الاحتمال",
      "definition": "مقياس حدوث حدث عشوائي بين 0 و 1.",
      "unit_id": "u5",
      "page": 74
    },
    "v-sample-space": {
      "id": "v-sample-space",
      "term": "فضاء العينة",
      "definition": "مجموعة كل النتجات الممكنة للتجربة العشوائية.",
      "unit_id": "u5",
      "page": 74
    },
    "v-union": {
      "id": "v-union",
      "term": "اتحاد الحدثين",
      "definition": "حدث يحدث إذا تحقق A أو B أو كلاهما.",
      "unit_id": "u5",
      "page": 79
    },
    "v-intersection": {
      "id": "v-intersection",
      "term": "تقاطع الحدثين",
      "definition": "حدث يحدث إذا تحقق A و B معاً.",
      "unit_id": "u5",
      "page": 79
    },
    "v-conditional": {
      "id": "v-conditional",
      "term": "الاحتمال الشرطي",
      "definition": "احتمال حدوث A بشرط حدوث B ويُكتب P(A|B)=P(A∩B)/P(B).",
      "unit_id": "u5",
      "page": 86
    },
    "v-independent": {
      "id": "v-independent",
      "term": "حدثان مستقلان",
      "definition": "حدثان لا يؤثر أحدهما في احتمال الآخر، أي P(A|B)=P(A).",
      "unit_id": "u5",
      "page": 86
    },
    "v-derivative": {
      "id": "v-derivative",
      "term": "المشتقة",
      "definition": "معدل التغير اللحظي للدالة وميل مماس منحناها.",
      "unit_id": "u6",
      "page": 154
    },
    "v-chain": {
      "id": "v-chain",
      "term": "قاعدة السلسلة",
      "definition": "قاعدة اشتقاق الدوال المركبة: (f∘g)′=f′(g)g′.",
      "unit_id": "u6",
      "page": 166
    },
    "v-extremum": {
      "id": "v-extremum",
      "term": "القيمة القصوى",
      "definition": "أكبر أو أصغر قيمة للدالة على فترة أو عند نقطة حرجة.",
      "unit_id": "u6",
      "page": 187
    },
    "v-integral": {
      "id": "v-integral",
      "term": "التكامل",
      "definition": "عملية عكس الاشتقاق وتستخدم أيضاً لحساب المساحات والحجوم.",
      "unit_id": "u7",
      "page": 210
    },
    "v-definite": {
      "id": "v-definite",
      "term": "التكامل المحدد",
      "definition": "تكامل بين حدين يعطي قيمة عددية F(b)−F(a).",
      "unit_id": "u7",
      "page": 235
    },
    "v-revolution": {
      "id": "v-revolution",
      "term": "مجسم الدوران",
      "definition": "مجسم ناتج عن دوران منحنى حول محور، وحجمه π∫f²dx.",
      "unit_id": "u7",
      "page": 248
    }
  },
  "solution_steps": {
    "sol-math-complex-add": {
      "id": "sol-math-complex-add",
      "title": "جمع عددين مركبين",
      "source_page": 13,
      "prompt": "إذا كان z₁ = 2 + 3i و z₂ = −1 + 2i فاحسب z₁ + z₂.",
      "given": "z₁ = 2 + 3i، z₂ = −1 + 2i",
      "answer": "1 + 5i",
      "tolerance": 0.01,
      "hint": "اجمع الأجزاء الحقيقية معاً والتخيلية معاً.",
      "steps": [
        {
          "title": "اجمع الأجزاء الحقيقية",
          "detail": "2 + (−1) = 1",
          "formula": "Re(z₁+z₂)=Re(z₁)+Re(z₂)"
        },
        {
          "title": "اجمع الأجزاء التخيلية",
          "detail": "3 + 2 = 5",
          "formula": "Im(z₁+z₂)=Im(z₁)+Im(z₂)"
        },
        {
          "title": "اكتب النتيجة",
          "detail": "العدد المركب الناتج هو 1 + 5i.",
          "formula": "z₁+z₂=1+5i"
        }
      ]
    },
    "sol-math-complex-modulus": {
      "id": "sol-math-complex-modulus",
      "title": "القيمة المطلقة لعدد مركب",
      "source_page": 19,
      "prompt": "احسب |3 + 4i|.",
      "given": "z = 3 + 4i",
      "answer": "5",
      "tolerance": 0.01,
      "hint": "استخدم نظرية فيثاغورس على مكوّنات العدد.",
      "steps": [
        {
          "title": "طبّق الصيغة",
          "detail": "|z| = √(3² + 4²)",
          "formula": "|a+bi|=√(a²+b²)"
        },
        {
          "title": "احسب المجموع",
          "detail": "9 + 16 = 25",
          "formula": "|z|=√25"
        },
        {
          "title": "النتيجة",
          "detail": "القيمة المطلقة تساوي 5.",
          "formula": "|3+4i|=5"
        }
      ]
    },
    "sol-math-polar": {
      "id": "sol-math-polar",
      "title": "التحويل إلى الصيغة القطبية",
      "source_page": 38,
      "prompt": "اكتب z = 1 + √3 i بالصيغة القطبية.",
      "given": "a = 1، b = √3",
      "answer": "2(cos60° + i sin60°)",
      "tolerance": 0.01,
      "hint": "احسب r أولاً ثم الزاوية في الربع الصحيح.",
      "steps": [
        {
          "title": "القيمة المطلقة",
          "detail": "r = √(1 + 3) = 2",
          "formula": "r=√(a²+b²)"
        },
        {
          "title": "الزاوية",
          "detail": "tan θ = √3/1، إذن θ = 60° لأن النقطة في الربع الأول.",
          "formula": "θ=tan⁻¹(b/a)"
        },
        {
          "title": "الصيغة القطبية",
          "detail": "z = 2(cos60° + i sin60°).",
          "formula": "z=r(cosθ+i sinθ)"
        }
      ]
    },
    "sol-math-demoivre": {
      "id": "sol-math-demoivre",
      "title": "تطبيق مبرهنة دي موافر",
      "source_page": 46,
      "prompt": "احسب (cos30° + i sin30°)³.",
      "given": "r = 1، θ = 30°، n = 3",
      "answer": "cos90° + i sin90° = i",
      "tolerance": 0.01,
      "hint": "اضرب الزاوية في الأس.",
      "steps": [
        {
          "title": "القيمة المطلقة",
          "detail": "1³ = 1",
          "formula": "rⁿ"
        },
        {
          "title": "الزاوية",
          "detail": "3 × 30° = 90°",
          "formula": "nθ"
        },
        {
          "title": "النتيجة",
          "detail": "cos90° + i sin90° = i.",
          "formula": "(cosθ+i sinθ)ⁿ=cos nθ+i sin nθ"
        }
      ]
    },
    "sol-math-binomial": {
      "id": "sol-math-binomial",
      "title": "معامل في التوسعة ذات الحدين",
      "source_page": 58,
      "prompt": "احسب معامل الحد الذي يحتوي على b² في (a+b)⁶.",
      "given": "n = 6، k = 2",
      "answer": "15",
      "tolerance": 0.01,
      "hint": "استخدم C(n,k) = n! / (k!(n−k)!).",
      "steps": [
        {
          "title": "اكتب الصيغة",
          "detail": "C(6,2) = 6! / (2!4!)",
          "formula": "C(n,k)=n!/(k!(n−k)!)"
        },
        {
          "title": "بسّط",
          "detail": "C(6,2) = (6×5)/(2×1) = 15",
          "formula": "C(6,2)=15"
        },
        {
          "title": "النتيجة",
          "detail": "معامل الحد هو 15.",
          "formula": "15a⁴b²"
        }
      ]
    },
    "sol-math-ellipse": {
      "id": "sol-math-ellipse",
      "title": "بؤرتا قطع ناقص",
      "source_page": 112,
      "prompt": "للقطع x²/25 + y²/9 = 1، أوجد البؤرتين.",
      "given": "a² = 25، b² = 9",
      "answer": "(−4، 0) و (4، 0)",
      "tolerance": 0.01,
      "hint": "a هي أكبر مقام، و c² = a² − b².",
      "steps": [
        {
          "title": "حدد a و b",
          "detail": "a = 5، b = 3 لأن 25 > 9.",
          "formula": "a>b"
        },
        {
          "title": "احسب c",
          "detail": "c² = 25 − 9 = 16 إذن c = 4.",
          "formula": "c²=a²−b²"
        },
        {
          "title": "البؤرتان",
          "detail": "تقعان على المحور x: (−4،0) و (4،0).",
          "formula": "(±c،0)"
        }
      ]
    },
    "sol-math-hyperbola": {
      "id": "sol-math-hyperbola",
      "title": "خطا القطع الزائد المقاربان",
      "source_page": 120,
      "prompt": "أوجد خطي المقاربة للقطع x²/4 − y²/9 = 1.",
      "given": "a = 2، b = 3",
      "answer": "y = ±(3/2)x",
      "tolerance": 0.01,
      "hint": "خطا المقاربة يمران بنقطة الأصل.",
      "steps": [
        {
          "title": "حدد a و b",
          "detail": "a² = 4 إذن a = 2، b² = 9 إذن b = 3.",
          "formula": "x²/a²−y²/b²=1"
        },
        {
          "title": "طبّق معادلة المقاربة",
          "detail": "y = ±(b/a)x",
          "formula": "y=±(b/a)x"
        },
        {
          "title": "النتيجة",
          "detail": "y = ±(3/2)x.",
          "formula": "y=±1.5x"
        }
      ]
    },
    "sol-math-parabola": {
      "id": "sol-math-parabola",
      "title": "بؤرة مكافئ",
      "source_page": 126,
      "prompt": "أوجد بؤرة القطع y² = 12x.",
      "given": "4p = 12",
      "answer": "(3، 0)",
      "tolerance": 0.01,
      "hint": "قارن المعادلة بصيغة y² = 4px.",
      "steps": [
        {
          "title": "احسب p",
          "detail": "4p = 12 إذن p = 3.",
          "formula": "y²=4px"
        },
        {
          "title": "موضع البؤرة",
          "detail": "البؤرة هي (p، 0).",
          "formula": "F=(p،0)"
        },
        {
          "title": "النتيجة",
          "detail": "F = (3، 0).",
          "formula": "F=(3،0)"
        }
      ]
    },
    "sol-math-space-diagonal": {
      "id": "sol-math-space-diagonal",
      "title": "القطر الفراغي لمكعب",
      "source_page": 136,
      "prompt": "مكعب ضلعه 4، احسب قطره الفراغي.",
      "given": "a = 4",
      "answer": "4√3 ≈ 6.928",
      "tolerance": 0.01,
      "hint": "استخدم فيثاغورس مرتين.",
      "steps": [
        {
          "title": "قطر الوجه",
          "detail": "d_face = √(a²+a²) = a√2",
          "formula": "d_face=a√2"
        },
        {
          "title": "القطر الفراغي",
          "detail": "d = √(d_face² + a²) = √(2a²+a²)",
          "formula": "d=a√3"
        },
        {
          "title": "التعويض",
          "detail": "d = 4√3 ≈ 6.928.",
          "formula": "d≈6.928"
        }
      ]
    },
    "sol-math-line-plane": {
      "id": "sol-math-line-plane",
      "title": "زاوية مستقيم مع مستوى",
      "source_page": 144,
      "prompt": "إذا كانت زاوية مستقيم مع المتجه الطبيعي لمستوى 40°، فما زاويته مع المستوى؟",
      "given": "α = 40°",
      "answer": "50°",
      "tolerance": 0.01,
      "hint": "الزاويتان مكمّلتان.",
      "steps": [
        {
          "title": "العلاقة",
          "detail": "θ = 90° − α",
          "formula": "θ=90°−α"
        },
        {
          "title": "التعويض",
          "detail": "θ = 90° − 40° = 50°.",
          "formula": "θ=50°"
        }
      ]
    },
    "sol-math-dihedral": {
      "id": "sol-math-dihedral",
      "title": "الزاوية بين مستويين",
      "source_page": 149,
      "prompt": "إذا كان المتجهان الطبيعيان متعامدين، فما الزاوية بين المستويين؟",
      "given": "n₁·n₂ = 0",
      "answer": "90°",
      "tolerance": 0.01,
      "hint": "استخدم جيب تمام الزاوية بين المتجهين.",
      "steps": [
        {
          "title": "حالة التعامد",
          "detail": "ناتج الجداء النقطة صفر يعني المتجهين متعامدين.",
          "formula": "n₁·n₂=0"
        },
        {
          "title": "الزاوية",
          "detail": "إذن الزاوية بين المستويين 90°.",
          "formula": "φ=90°"
        }
      ]
    },
    "sol-math-prob-union": {
      "id": "sol-math-prob-union",
      "title": "احتمال اتحاد حدثين",
      "source_page": 82,
      "prompt": "إذا كان P(A)=0.55 و P(B)=0.40 و P(A∩B)=0.20، فاحسب P(A∪B).",
      "given": "P(A)=0.55، P(B)=0.40، P(A∩B)=0.20",
      "answer": "0.75",
      "tolerance": 0.001,
      "hint": "اطرح التداخل حتى لا تحسبه مرتين.",
      "steps": [
        {
          "title": "قاعدة الجمع",
          "detail": "P(A∪B)=P(A)+P(B)−P(A∩B)",
          "formula": "P(A∪B)=P(A)+P(B)−P(A∩B)"
        },
        {
          "title": "التعويض",
          "detail": "0.55 + 0.40 − 0.20 = 0.75",
          "formula": "=0.75"
        }
      ]
    },
    "sol-math-prob-conditional": {
      "id": "sol-math-prob-conditional",
      "title": "احتمال شرطي",
      "source_page": 89,
      "prompt": "إذا كان P(A∩B)=0.25 و P(B)=0.50، فاحسب P(A|B).",
      "given": "P(A∩B)=0.25، P(B)=0.50",
      "answer": "0.5",
      "tolerance": 0.001,
      "hint": "قسّم على احتمال الشرط.",
      "steps": [
        {
          "title": "الصيغة",
          "detail": "P(A|B)=P(A∩B)/P(B)",
          "formula": "P(A|B)=P(A∩B)/P(B)"
        },
        {
          "title": "التعويض",
          "detail": "0.25 / 0.50 = 0.5",
          "formula": "=0.5"
        }
      ]
    },
    "sol-math-prob-binomial": {
      "id": "sol-math-prob-binomial",
      "title": "احتمال ذو حدين",
      "source_page": 96,
      "prompt": "في 10 تجارب احتمال النجاح 0.5، احتمال 4 نجاحات؟",
      "given": "n=10، p=0.5، k=4",
      "answer": "0.2051",
      "tolerance": 0.001,
      "hint": "استخدم C(n,k)pᵏ(1−p)ⁿ⁻ᵏ.",
      "steps": [
        {
          "title": "المعامل",
          "detail": "C(10,4)=210",
          "formula": "C(n,k)=n!/(k!(n−k)!)"
        },
        {
          "title": "التعويض",
          "detail": "210(0.5)⁴(0.5)⁶ = 210/1024",
          "formula": "P(X=4)=210/1024"
        },
        {
          "title": "النتيجة",
          "detail": "≈ 0.2051",
          "formula": "≈0.2051"
        }
      ]
    },
    "sol-math-power": {
      "id": "sol-math-power",
      "title": "مشتقة دالة قوة",
      "source_page": 162,
      "prompt": "إذا كان f(x)=x³، احسب f′(2).",
      "given": "f(x)=x³، x=2",
      "answer": "12",
      "tolerance": 0.01,
      "hint": "انقص الأس بمقدار 1 ثم عوّض.",
      "steps": [
        {
          "title": "القاعدة",
          "detail": "(xⁿ)′=nxⁿ⁻¹",
          "formula": "(xⁿ)′=nxⁿ⁻¹"
        },
        {
          "title": "المشتقة",
          "detail": "f′(x)=3x²",
          "formula": "f′(x)=3x²"
        },
        {
          "title": "التعويض",
          "detail": "f′(2)=3×4=12",
          "formula": "12"
        }
      ]
    },
    "sol-math-chain": {
      "id": "sol-math-chain",
      "title": "قاعدة السلسلة",
      "source_page": 169,
      "prompt": "اشتق f(x)=(2x+1)³.",
      "given": "g(x)=2x+1، n=3",
      "answer": "6(2x+1)²",
      "tolerance": 0.01,
      "hint": "اضرب مشتقة الخارج في مشتقة الداخل.",
      "steps": [
        {
          "title": "الخارج",
          "detail": "3(2x+1)²",
          "formula": "n[g(x)]ⁿ⁻¹"
        },
        {
          "title": "الداخل",
          "detail": "(2x+1)′=2",
          "formula": "g′(x)=2"
        },
        {
          "title": "النتيجة",
          "detail": "f′(x)=6(2x+1)²",
          "formula": "f′(x)=f′(g(x))g′(x)"
        }
      ]
    },
    "sol-math-extrema": {
      "id": "sol-math-extrema",
      "title": "قيمة صغرى لدالة تربيعية",
      "source_page": 192,
      "prompt": "للدالة f(x)=x²−4x+3، أوجد النقطة الحرجة.",
      "given": "a=1، b=−4",
      "answer": "2",
      "tolerance": 0.01,
      "hint": "احل f′(x)=0.",
      "steps": [
        {
          "title": "المشتقة",
          "detail": "f′(x)=2x−4",
          "formula": "f′(x)=2ax+b"
        },
        {
          "title": "المعادلة",
          "detail": "2x−4=0 إذن x=2",
          "formula": "x=−b/(2a)"
        },
        {
          "title": "النوع",
          "detail": "لأن a>0 فالنقطة قيمة صغرى.",
          "formula": "f″(x)=2>0"
        }
      ]
    },
    "sol-math-mvt": {
      "id": "sol-math-mvt",
      "title": "نظرية القيمة المتوسطة",
      "source_page": 203,
      "prompt": "للدالة f(x)=x² على [1،5]، أوجد c الذي يحقق المبرهنة.",
      "given": "f(x)=x²، a=1، b=5",
      "answer": "3",
      "tolerance": 0.01,
      "hint": "ميل القطرة = (f(b)−f(a))/(b−a).",
      "steps": [
        {
          "title": "ميل القطرة",
          "detail": "(25−1)/(5−1)=6",
          "formula": "[f(b)−f(a)]/(b−a)"
        },
        {
          "title": "المشتقة",
          "detail": "f′(c)=2c",
          "formula": "2c=6"
        },
        {
          "title": "النتيجة",
          "detail": "c=3 وهو داخل الفترة.",
          "formula": "c=3"
        }
      ]
    },
    "sol-math-indefinite": {
      "id": "sol-math-indefinite",
      "title": "تكامل قوة",
      "source_page": 214,
      "prompt": "احسب ∫x³dx.",
      "given": "n=3",
      "answer": "x⁴/4 + C",
      "tolerance": 0.01,
      "hint": "زد الأس بمقدار 1 ثم اقسم على الأس الجديد.",
      "steps": [
        {
          "title": "القاعدة",
          "detail": "∫xⁿdx=xⁿ⁺¹/(n+1)+C",
          "formula": "n≠−1"
        },
        {
          "title": "التعويض",
          "detail": "∫x³dx=x⁴/4+C",
          "formula": "=x⁴/4+C"
        }
      ]
    },
    "sol-math-definite": {
      "id": "sol-math-definite",
      "title": "تكامل محدد",
      "source_page": 237,
      "prompt": "احسب ∫₁⁴ x² dx.",
      "given": "a=1، b=4، n=2",
      "answer": "21",
      "tolerance": 0.01,
      "hint": "استخدم F(b)−F(a).",
      "steps": [
        {
          "title": "المضاد",
          "detail": "F(x)=x³/3",
          "formula": "F(x)=x³/3"
        },
        {
          "title": "التعويض",
          "detail": "64/3 − 1/3 = 63/3",
          "formula": "F(4)−F(1)"
        },
        {
          "title": "النتيجة",
          "detail": "21",
          "formula": "=21"
        }
      ]
    },
    "sol-math-area": {
      "id": "sol-math-area",
      "title": "مساحة تحت منحنى",
      "source_page": 246,
      "prompt": "احسب المساحة تحت y=x² من 0 إلى 3.",
      "given": "a=0، b=3، f(x)=x²",
      "answer": "9",
      "tolerance": 0.01,
      "hint": "المساحة هي التكامل المحدد للدالة.",
      "steps": [
        {
          "title": "التكامل",
          "detail": "A=∫₀³x²dx",
          "formula": "A=∫ₐᵇf(x)dx"
        },
        {
          "title": "المضاد",
          "detail": "[x³/3]₀³=27/3",
          "formula": "=9"
        }
      ]
    },
    "sol-math-revolution": {
      "id": "sol-math-revolution",
      "title": "حجم مجسم دوران",
      "source_page": 250,
      "prompt": "احسب حجم دوران y=x حول محور x من 0 إلى 2.",
      "given": "f(x)=x، a=0، b=2",
      "answer": "8π/3 ≈ 8.378",
      "tolerance": 0.01,
      "hint": "استخدم طريقة الأقراص V=π∫f²dx.",
      "steps": [
        {
          "title": "الصيغة",
          "detail": "V=π∫₀²x²dx",
          "formula": "V=π∫ₐᵇ[f(x)]²dx"
        },
        {
          "title": "التكامل",
          "detail": "π[x³/3]₀²=8π/3",
          "formula": "=8π/3"
        },
        {
          "title": "النتيجة",
          "detail": "≈ 8.378 وحدة مكعبة.",
          "formula": "≈8.378"
        }
      ]
    }
  },
  "geometry_lab": {
    "title": "معمل الرياضيات التفاعلي - الصف الثالث الثانوي",
    "theme_color": "#00a859",
    "default_scene": "lab-math-complex",
    "scenes": [
      {
        "id": "lab-math-complex",
        "title": "مستوى أرغاند",
        "unit_id": "u1",
        "page": 16,
        "sim_key": "math_complex",
        "kind": "2d",
        "formula": "z = a + bi، |z| = √(a²+b²)",
        "prompt": "حرك r والزاوية θ ولاحظ أثرهما على موضع العدد المركب.",
        "controls": [
          {
            "id": "r",
            "label": "القيمة المطلقة r",
            "min": 1,
            "max": 10,
            "step": 1,
            "default": 5
          },
          {
            "id": "theta",
            "label": "الزاوية θ",
            "min": 0,
            "max": 360,
            "step": 5,
            "default": 45
          }
        ],
        "steps": [
          {
            "title": "الإسقاط على المحور الحقيقي",
            "detail": "a = r cos θ",
            "formula": "a=r cosθ"
          },
          {
            "title": "الإسقاط على المحور التخيلي",
            "detail": "b = r sin θ",
            "formula": "b=r sinθ"
          },
          {
            "title": "الطول",
            "detail": "القيمة المطلقة هي طول المتجه من المبدأ.",
            "formula": "|z|=r"
          }
        ]
      },
      {
        "id": "lab-math-cone",
        "title": "قطوع المخروط",
        "unit_id": "u3",
        "page": 104,
        "sim_key": "math_cone_sections",
        "kind": "3d",
        "formula": "e = PF / PD",
        "prompt": "غيّر ميل مستوى القطع ولاحظ نوع المنحنى الناتج.",
        "controls": [
          {
            "id": "tilt",
            "label": "ميل المستوى",
            "min": 0,
            "max": 90,
            "step": 5,
            "default": 35
          }
        ],
        "steps": [
          {
            "title": "مستوى مواز لقاعدة المخروط",
            "detail": "ينتج دائرة.",
            "formula": "e=0"
          },
          {
            "title": "مستوى مائل",
            "detail": "ينتج قطعاً ناقصاً أو مكافئاً أو زائداً حسب الميل.",
            "formula": "e=PF/PD"
          },
          {
            "title": "الخلاصة والتطبيق 3",
            "detail": "غيّر ميل مستوى القطع ولاحظ نوع المنحنى الناتج.",
            "formula": "e = PF / PD"
          }
        ]
      },
      {
        "id": "lab-math-ellipse",
        "title": "القطع الناقص",
        "unit_id": "u3",
        "page": 110,
        "sim_key": "math_ellipse",
        "kind": "2d",
        "formula": "x²/a² + y²/b² = 1",
        "prompt": "غيّر a و b ولاحظ البؤرتين وشكل المنحنى.",
        "controls": [
          {
            "id": "a",
            "label": "نصف المحور a",
            "min": 2,
            "max": 8,
            "step": 1,
            "default": 5
          },
          {
            "id": "b",
            "label": "نصف المحور b",
            "min": 1,
            "max": 7,
            "step": 1,
            "default": 3
          }
        ],
        "steps": [
          {
            "title": "المحور الكبير",
            "detail": "a هي أكبر نصف محور.",
            "formula": "a>b"
          },
          {
            "title": "البؤرتان",
            "detail": "c² = a² − b²",
            "formula": "c=√(a²−b²)"
          },
          {
            "title": "الخلاصة والتطبيق 3",
            "detail": "غيّر a و b ولاحظ البؤرتين وشكل المنحنى.",
            "formula": "x²/a² + y²/b² = 1"
          }
        ]
      },
      {
        "id": "lab-math-hyperbola",
        "title": "القطع الزائد",
        "unit_id": "u3",
        "page": 118,
        "sim_key": "math_hyperbola",
        "kind": "2d",
        "formula": "x²/a² − y²/b² = 1",
        "prompt": "غيّر a و b ولاحظ الفروع والخطين المقاربين.",
        "controls": [
          {
            "id": "a",
            "label": "المعلمة a",
            "min": 1,
            "max": 6,
            "step": 1,
            "default": 2
          },
          {
            "id": "b",
            "label": "المعلمة b",
            "min": 1,
            "max": 6,
            "step": 1,
            "default": 3
          }
        ],
        "steps": [
          {
            "title": "الفروع",
            "detail": "الفرق المطلق للبعدين يساوي 2a.",
            "formula": "|PF₁−PF₂|=2a"
          },
          {
            "title": "المقاربة",
            "detail": "y = ±(b/a)x",
            "formula": "y=±(b/a)x"
          },
          {
            "title": "الخلاصة والتطبيق 3",
            "detail": "غيّر a و b ولاحظ الفروع والخطين المقاربين.",
            "formula": "x²/a² − y²/b² = 1"
          }
        ]
      },
      {
        "id": "lab-math-parabola",
        "title": "القطع المكافئ",
        "unit_id": "u3",
        "page": 124,
        "sim_key": "math_parabola",
        "kind": "2d",
        "formula": "y² = 4px",
        "prompt": "غيّر p ولاحظ البؤرة والدليل.",
        "controls": [
          {
            "id": "p",
            "label": "المعلمة p",
            "min": 1,
            "max": 6,
            "step": 1,
            "default": 2
          }
        ],
        "steps": [
          {
            "title": "البؤرة",
            "detail": "F = (p، 0)",
            "formula": "F=(p،0)"
          },
          {
            "title": "الدليل",
            "detail": "x = −p",
            "formula": "x=−p"
          },
          {
            "title": "الخلاصة والتطبيق 3",
            "detail": "غيّر p ولاحظ البؤرة والدليل.",
            "formula": "y² = 4px"
          }
        ]
      },
      {
        "id": "lab-math-space",
        "title": "القطر الفراغي للمكعب",
        "unit_id": "u4",
        "page": 136,
        "sim_key": "math_3d_pythagoras",
        "kind": "3d",
        "formula": "d = a√3",
        "prompt": "دور المكعب وغيّر ضلعه لترى القطر الفراغي.",
        "controls": [
          {
            "id": "a",
            "label": "طول الضلع",
            "min": 1,
            "max": 10,
            "step": 1,
            "default": 4
          }
        ],
        "steps": [
          {
            "title": "قطر الوجه",
            "detail": "a√2",
            "formula": "d_face=a√2"
          },
          {
            "title": "القطر الفراغي",
            "detail": "a√3",
            "formula": "d=a√3"
          },
          {
            "title": "الخلاصة والتطبيق 3",
            "detail": "دور المكعب وغيّر ضلعه لترى القطر الفراغي.",
            "formula": "d = a√3"
          }
        ]
      },
      {
        "id": "lab-math-line-plane",
        "title": "مستقيم ومستوى",
        "unit_id": "u4",
        "page": 142,
        "sim_key": "math_line_plane",
        "kind": "3d",
        "formula": "sin θ = |u·n|/(|u||n|)",
        "prompt": "غيّر زاوية المستقيم مع الطبيعي ولاحظ الزاوية مع المستوى.",
        "controls": [
          {
            "id": "alpha",
            "label": "الزاوية مع الطبيعي",
            "min": 0,
            "max": 90,
            "step": 5,
            "default": 40
          }
        ],
        "steps": [
          {
            "title": "المتجه الطبيعي",
            "detail": "n يحدد العمود على المستوى.",
            "formula": "n=(A،B،C)"
          },
          {
            "title": "الزاوية المطلوبة",
            "detail": "θ = 90° − α",
            "formula": "θ=90°−α"
          },
          {
            "title": "الخلاصة والتطبيق 3",
            "detail": "غيّر زاوية المستقيم مع الطبيعي ولاحظ الزاوية مع المستوى.",
            "formula": "sin θ = |u·n|/(|u||n|)"
          }
        ]
      },
      {
        "id": "lab-math-dihedral",
        "title": "زاوية بين مستويين",
        "unit_id": "u4",
        "page": 147,
        "sim_key": "math_dihedral",
        "kind": "3d",
        "formula": "cos φ = |n₁·n₂|/(|n₁||n₂|)",
        "prompt": "دور المستوى الثاني حول خط التقاطع.",
        "controls": [
          {
            "id": "phi",
            "label": "زاوية الدوران",
            "min": 0,
            "max": 120,
            "step": 5,
            "default": 60
          }
        ],
        "steps": [
          {
            "title": "المتجهان الطبيعيان",
            "detail": "ناتج الجداء يعطي جيب تمام الزاوية.",
            "formula": "cosφ=|n₁·n₂|/(|n₁||n₂|)"
          },
          {
            "title": "الخلاصة والتطبيق 2",
            "detail": "دور المستوى الثاني حول خط التقاطع.",
            "formula": "cos φ = |n₁·n₂|/(|n₁||n₂|)"
          },
          {
            "title": "الخلاصة والتطبيق 3",
            "detail": "دور المستوى الثاني حول خط التقاطع.",
            "formula": "cos φ = |n₁·n₂|/(|n₁||n₂|)"
          }
        ]
      },
      {
        "id": "lab-math-probability",
        "title": "فضاء العينة",
        "unit_id": "u5",
        "page": 79,
        "sim_key": "math_probability_space",
        "kind": "2d",
        "formula": "P(A∪B)=P(A)+P(B)−P(A∩B)",
        "prompt": "غيّر احتمالي الحدثين والتقاطع.",
        "controls": [
          {
            "id": "pa",
            "label": "P(A)",
            "min": 0,
            "max": 100,
            "step": 5,
            "default": 55
          },
          {
            "id": "pb",
            "label": "P(B)",
            "min": 0,
            "max": 100,
            "step": 5,
            "default": 40
          },
          {
            "id": "inter",
            "label": "P(A∩B)",
            "min": 0,
            "max": 100,
            "step": 5,
            "default": 20
          }
        ],
        "steps": [
          {
            "title": "الجمع",
            "detail": "اجمع الاحتمالين.",
            "formula": "P(A)+P(B)"
          },
          {
            "title": "إزالة التداخل",
            "detail": "اطرح التقاطع حتى لا يُحسب مرتين.",
            "formula": "−P(A∩B)"
          },
          {
            "title": "الخلاصة والتطبيق 3",
            "detail": "غيّر احتمالي الحدثين والتقاطع.",
            "formula": "P(A∪B)=P(A)+P(B)−P(A∩B)"
          }
        ]
      },
      {
        "id": "lab-math-derivative",
        "title": "مماس المنحنى",
        "unit_id": "u6",
        "page": 154,
        "sim_key": "math_derivative",
        "kind": "2d",
        "formula": "f′(x)=lim[f(x+h)−f(x)]/h",
        "prompt": "حرك نقطة على المنحنى ولاحظ ميل المماس.",
        "controls": [
          {
            "id": "x",
            "label": "موضع النقطة",
            "min": 1,
            "max": 9,
            "step": 1,
            "default": 4
          }
        ],
        "steps": [
          {
            "title": "المنحنى",
            "detail": "f(x)=x²/8",
            "formula": "f(x)=x²/8"
          },
          {
            "title": "المشتقة",
            "detail": "f′(x)=x/4",
            "formula": "f′(x)=x/4"
          },
          {
            "title": "الخلاصة والتطبيق 3",
            "detail": "حرك نقطة على المنحنى ولاحظ ميل المماس.",
            "formula": "f′(x)=lim[f(x+h)−f(x)]/h"
          }
        ]
      },
      {
        "id": "lab-math-integral",
        "title": "التكامل والمساحة",
        "unit_id": "u7",
        "page": 235,
        "sim_key": "math_integral",
        "kind": "2d",
        "formula": "∫ₐᵇf(x)dx=F(b)−F(a)",
        "prompt": "غيّر الحد العلوي ولاحظ تراكم المساحة.",
        "controls": [
          {
            "id": "b",
            "label": "الحد العلوي",
            "min": 1,
            "max": 10,
            "step": 1,
            "default": 6
          }
        ],
        "steps": [
          {
            "title": "الدالة",
            "detail": "f(x)=x/4",
            "formula": "f(x)=x/4"
          },
          {
            "title": "المساحة",
            "detail": "A=b²/8",
            "formula": "A=b²/8"
          },
          {
            "title": "الخلاصة والتطبيق 3",
            "detail": "غيّر الحد العلوي ولاحظ تراكم المساحة.",
            "formula": "∫ₐᵇf(x)dx=F(b)−F(a)"
          }
        ]
      },
      {
        "id": "lab-math-area",
        "title": "المساحة بين منحنيين",
        "unit_id": "u7",
        "page": 244,
        "sim_key": "math_area_between",
        "kind": "2d",
        "formula": "A=∫ₐᵇ|f(x)−g(x)|dx",
        "prompt": "غيّر الحد العلوي ولاحظ الفرق بين المنحنيين.",
        "controls": [
          {
            "id": "b",
            "label": "الحد العلوي",
            "min": 1,
            "max": 10,
            "step": 1,
            "default": 5
          }
        ],
        "steps": [
          {
            "title": "المنحنى العلوي",
            "detail": "f(x)=2",
            "formula": "f(x)=2"
          },
          {
            "title": "المنحنى السفلي",
            "detail": "g(x)=x/4",
            "formula": "g(x)=x/4"
          },
          {
            "title": "الخلاصة والتطبيق 3",
            "detail": "غيّر الحد العلوي ولاحظ الفرق بين المنحنيين.",
            "formula": "A=∫ₐᵇ|f(x)−g(x)|dx"
          }
        ]
      },
      {
        "id": "lab-math-revolution",
        "title": "مجسم الدوران",
        "unit_id": "u7",
        "page": 248,
        "sim_key": "math_revolution",
        "kind": "3d",
        "formula": "V=π∫ₐᵇ[f(x)]²dx",
        "prompt": "غيّر عدد الأقراص لتراكم حجم المجسم.",
        "controls": [
          {
            "id": "n",
            "label": "عدد الأقراص",
            "min": 4,
            "max": 20,
            "step": 1,
            "default": 10
          }
        ],
        "steps": [
          {
            "title": "القرص",
            "detail": "نصف قطره f(x) وسمكه dx",
            "formula": "dV=π[f(x)]²dx"
          },
          {
            "title": "الحجم",
            "detail": "مجموع الأقراص يقترب من التكامل.",
            "formula": "V=π∫[f(x)]²dx"
          },
          {
            "title": "الخلاصة والتطبيق 3",
            "detail": "غيّر عدد الأقراص لتراكم حجم المجسم.",
            "formula": "V=π∫ₐᵇ[f(x)]²dx"
          }
        ]
      }
    ]
  }
};
