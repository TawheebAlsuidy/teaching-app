window.THAKER_CURRICULUM_G12_PHYSICS = {
  "manifest": {
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
      "original_page_rendering": true,
      "interactive_overlays": true,
      "smart_text_bottom_sheet": true,
      "explanation_levels_count": 3,
      "interactive_3d_physics_lab": true,
      "interactive_step_by_step_equations": true,
      "simulated_activities": true,
      "remediation_mistake_review": true,
      "offline_audio_synthesis": true,
      "yemeni_companion_prompts": true,
      "multi_student_profiles": true
    },
    "data_files": [
      "pages.json",
      "units.json",
      "lessons.json",
      "interactions.json",
      "explanations.json",
      "diagrams.json",
      "activities.json",
      "assessments.json",
      "glossary.json"
    ]
  },
  "units": [
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
  ],
  "pages": [
    {
      "page_id": "phys12-p006",
      "book_page": 6,
      "pdf_page": 6,
      "type": "contents",
      "title": "فهرس الموضوعات (الجزء 1)",
      "unit_id": null,
      "image": "assets/curriculum/grade12/physics/pages/page_006_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_006.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p007",
      "book_page": 7,
      "pdf_page": 7,
      "type": "contents",
      "title": "فهرس الموضوعات (الجزء 2)",
      "unit_id": null,
      "image": "assets/curriculum/grade12/physics/pages/page_007_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_007.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p008",
      "book_page": 8,
      "pdf_page": 8,
      "type": "contents",
      "title": "فهرس الموضوعات (الجزء 3)",
      "unit_id": null,
      "image": "assets/curriculum/grade12/physics/pages/page_008_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_008.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p009",
      "book_page": 9,
      "pdf_page": 9,
      "type": "lesson",
      "title": "فيزياء 3 ثانوي — صفحة 8",
      "unit_id": null,
      "image": "assets/curriculum/grade12/physics/pages/page_009_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_009.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p010",
      "book_page": 9,
      "pdf_page": 10,
      "type": "unit_cover",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — غلاف وأهداف الوحدة",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_010_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_010.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p011",
      "book_page": 10,
      "pdf_page": 11,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 10",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_011_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_011.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p012",
      "book_page": 11,
      "pdf_page": 12,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 11",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_012_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_012.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p013",
      "book_page": 12,
      "pdf_page": 13,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 12",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_013_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_013.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p014",
      "book_page": 13,
      "pdf_page": 14,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 13",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_014_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_014.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p015",
      "book_page": 14,
      "pdf_page": 15,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 14",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_015_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_015.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p016",
      "book_page": 15,
      "pdf_page": 16,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 15",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_016_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_016.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p017",
      "book_page": 16,
      "pdf_page": 17,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 16",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_017_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_017.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p018",
      "book_page": 17,
      "pdf_page": 18,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 17",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_018_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_018.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p019",
      "book_page": 18,
      "pdf_page": 19,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 18",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_019_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_019.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p020",
      "book_page": 19,
      "pdf_page": 20,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 19",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_020_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_020.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p021",
      "book_page": 20,
      "pdf_page": 21,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 20",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_021_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_021.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p022",
      "book_page": 21,
      "pdf_page": 22,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 21",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_022_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_022.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p023",
      "book_page": 22,
      "pdf_page": 23,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 22",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_023_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_023.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p024",
      "book_page": 23,
      "pdf_page": 24,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 23",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_024_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_024.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p025",
      "book_page": 24,
      "pdf_page": 25,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 24",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_025_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_025.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p026",
      "book_page": 25,
      "pdf_page": 26,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 25",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_026_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_026.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p027",
      "book_page": 26,
      "pdf_page": 27,
      "type": "lesson",
      "title": "الوحدة الأولى: كمية التحرك والمقذوفات — ص 26",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_027_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_027.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p028",
      "book_page": 27,
      "pdf_page": 28,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة الأولى: كمية التحرك والمقذوفات",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_028_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_028.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p029",
      "book_page": 28,
      "pdf_page": 29,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة الأولى: كمية التحرك والمقذوفات",
      "unit_id": "u1",
      "image": "assets/curriculum/grade12/physics/pages/page_029_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_029.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p030",
      "book_page": 29,
      "pdf_page": 30,
      "type": "unit_cover",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — غلاف وأهداف الوحدة",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_030_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_030.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p031",
      "book_page": 30,
      "pdf_page": 31,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 30",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_031_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_031.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p032",
      "book_page": 31,
      "pdf_page": 32,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 31",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_032_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_032.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p033",
      "book_page": 32,
      "pdf_page": 33,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 32",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_033_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_033.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p034",
      "book_page": 33,
      "pdf_page": 34,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 33",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_034_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_034.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p035",
      "book_page": 34,
      "pdf_page": 35,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 34",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_035_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_035.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p036",
      "book_page": 35,
      "pdf_page": 36,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 35",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_036_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_036.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p037",
      "book_page": 36,
      "pdf_page": 37,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 36",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_037_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_037.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p038",
      "book_page": 37,
      "pdf_page": 38,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 37",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_038_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_038.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p039",
      "book_page": 38,
      "pdf_page": 39,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 38",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_039_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_039.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p040",
      "book_page": 39,
      "pdf_page": 40,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 39",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_040_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_040.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p041",
      "book_page": 40,
      "pdf_page": 41,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 40",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_041_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_041.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p042",
      "book_page": 41,
      "pdf_page": 42,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 41",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_042_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_042.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p043",
      "book_page": 42,
      "pdf_page": 43,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 42",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_043_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_043.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p044",
      "book_page": 43,
      "pdf_page": 44,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 43",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_044_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_044.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p045",
      "book_page": 44,
      "pdf_page": 45,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 44",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_045_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_045.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p046",
      "book_page": 45,
      "pdf_page": 46,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 45",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_046_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_046.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p047",
      "book_page": 46,
      "pdf_page": 47,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 46",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_047_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_047.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p048",
      "book_page": 47,
      "pdf_page": 48,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 47",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_048_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_048.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p049",
      "book_page": 48,
      "pdf_page": 49,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 48",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_049_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_049.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p050",
      "book_page": 49,
      "pdf_page": 50,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 49",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_050_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_050.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p051",
      "book_page": 50,
      "pdf_page": 51,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 50",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_051_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_051.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p052",
      "book_page": 51,
      "pdf_page": 52,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 51",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_052_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_052.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p053",
      "book_page": 52,
      "pdf_page": 53,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 52",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_053_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_053.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p054",
      "book_page": 53,
      "pdf_page": 54,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 53",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_054_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_054.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p055",
      "book_page": 54,
      "pdf_page": 55,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 54",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_055_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_055.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p056",
      "book_page": 55,
      "pdf_page": 56,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 55",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_056_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_056.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p057",
      "book_page": 56,
      "pdf_page": 57,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 56",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_057_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_057.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p058",
      "book_page": 57,
      "pdf_page": 58,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 57",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_058_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_058.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p059",
      "book_page": 58,
      "pdf_page": 59,
      "type": "lesson",
      "title": "الوحدة الثانية: التيار المتردد (المتناوب) — ص 58",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_059_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_059.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p060",
      "book_page": 59,
      "pdf_page": 60,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة الثانية: التيار المتردد (المتناوب)",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_060_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_060.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p061",
      "book_page": 60,
      "pdf_page": 61,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة الثانية: التيار المتردد (المتناوب)",
      "unit_id": "u2",
      "image": "assets/curriculum/grade12/physics/pages/page_061_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_061.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p062",
      "book_page": 61,
      "pdf_page": 62,
      "type": "unit_cover",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — غلاف وأهداف الوحدة",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_062_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_062.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p063",
      "book_page": 62,
      "pdf_page": 63,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 62",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_063_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_063.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p064",
      "book_page": 63,
      "pdf_page": 64,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 63",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_064_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_064.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p065",
      "book_page": 64,
      "pdf_page": 65,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 64",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_065_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_065.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p066",
      "book_page": 65,
      "pdf_page": 66,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 65",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_066_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_066.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p067",
      "book_page": 66,
      "pdf_page": 67,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 66",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_067_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_067.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p068",
      "book_page": 67,
      "pdf_page": 68,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 67",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_068_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_068.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p069",
      "book_page": 68,
      "pdf_page": 69,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 68",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_069_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_069.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p070",
      "book_page": 69,
      "pdf_page": 70,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 69",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_070_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_070.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p071",
      "book_page": 70,
      "pdf_page": 71,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 70",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_071_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_071.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p072",
      "book_page": 71,
      "pdf_page": 72,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 71",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_072_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_072.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p073",
      "book_page": 72,
      "pdf_page": 73,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 72",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_073_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_073.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p074",
      "book_page": 73,
      "pdf_page": 74,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 73",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_074_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_074.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p075",
      "book_page": 74,
      "pdf_page": 75,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 74",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_075_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_075.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p076",
      "book_page": 75,
      "pdf_page": 76,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 75",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_076_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_076.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p077",
      "book_page": 76,
      "pdf_page": 77,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 76",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_077_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_077.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p078",
      "book_page": 77,
      "pdf_page": 78,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 77",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_078_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_078.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p079",
      "book_page": 78,
      "pdf_page": 79,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 78",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_079_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_079.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p080",
      "book_page": 79,
      "pdf_page": 80,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 79",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_080_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_080.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p081",
      "book_page": 80,
      "pdf_page": 81,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 80",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_081_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_081.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p082",
      "book_page": 81,
      "pdf_page": 82,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 81",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_082_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_082.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p083",
      "book_page": 82,
      "pdf_page": 83,
      "type": "lesson",
      "title": "الوحدة الثالثة: الإلكترونيات وأشباه الموصلات — ص 82",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_083_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_083.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p084",
      "book_page": 83,
      "pdf_page": 84,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة الثالثة: الإلكترونيات وأشباه الموصلات",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_084_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_084.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p085",
      "book_page": 84,
      "pdf_page": 85,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة الثالثة: الإلكترونيات وأشباه الموصلات",
      "unit_id": "u3",
      "image": "assets/curriculum/grade12/physics/pages/page_085_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_085.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p086",
      "book_page": 85,
      "pdf_page": 86,
      "type": "unit_cover",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — غلاف وأهداف الوحدة",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_086_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_086.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p087",
      "book_page": 86,
      "pdf_page": 87,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 86",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_087_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_087.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p088",
      "book_page": 87,
      "pdf_page": 88,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 87",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_088_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_088.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p089",
      "book_page": 88,
      "pdf_page": 89,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 88",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_089_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_089.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p090",
      "book_page": 89,
      "pdf_page": 90,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 89",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_090_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_090.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p091",
      "book_page": 90,
      "pdf_page": 91,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 90",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_091_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_091.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p092",
      "book_page": 91,
      "pdf_page": 92,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 91",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_092_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_092.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p093",
      "book_page": 92,
      "pdf_page": 93,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 92",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_093_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_093.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p094",
      "book_page": 93,
      "pdf_page": 94,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 93",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_094_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_094.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p095",
      "book_page": 94,
      "pdf_page": 95,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 94",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_095_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_095.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p096",
      "book_page": 95,
      "pdf_page": 96,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 95",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_096_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_096.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p097",
      "book_page": 96,
      "pdf_page": 97,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 96",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_097_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_097.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p098",
      "book_page": 97,
      "pdf_page": 98,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 97",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_098_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_098.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p099",
      "book_page": 98,
      "pdf_page": 99,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 98",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_099_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_099.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p100",
      "book_page": 99,
      "pdf_page": 100,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 99",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_100_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_100.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p101",
      "book_page": 100,
      "pdf_page": 101,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 100",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_101_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_101.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p102",
      "book_page": 101,
      "pdf_page": 102,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 101",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_102_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_102.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p103",
      "book_page": 102,
      "pdf_page": 103,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 102",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_103_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_103.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p104",
      "book_page": 103,
      "pdf_page": 104,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 103",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_104_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_104.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p105",
      "book_page": 104,
      "pdf_page": 105,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 104",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_105_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_105.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p106",
      "book_page": 105,
      "pdf_page": 106,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 105",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_106_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_106.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p107",
      "book_page": 106,
      "pdf_page": 107,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 106",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_107_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_107.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p108",
      "book_page": 107,
      "pdf_page": 108,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 107",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_108_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_108.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p109",
      "book_page": 108,
      "pdf_page": 109,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 108",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_109_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_109.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p110",
      "book_page": 109,
      "pdf_page": 110,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 109",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_110_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_110.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p111",
      "book_page": 110,
      "pdf_page": 111,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 110",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_111_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_111.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p112",
      "book_page": 111,
      "pdf_page": 112,
      "type": "lesson",
      "title": "الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات — ص 111",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_112_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_112.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p113",
      "book_page": 112,
      "pdf_page": 113,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_113_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_113.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p114",
      "book_page": 113,
      "pdf_page": 114,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة الرابعة: الأجهزة الإلكترونية والاتصالات",
      "unit_id": "u4",
      "image": "assets/curriculum/grade12/physics/pages/page_114_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_114.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p115",
      "book_page": 114,
      "pdf_page": 115,
      "type": "unit_cover",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — غلاف وأهداف الوحدة",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_115_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_115.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p116",
      "book_page": 115,
      "pdf_page": 116,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 115",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_116_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_116.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p117",
      "book_page": 116,
      "pdf_page": 117,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 116",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_117_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_117.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p118",
      "book_page": 117,
      "pdf_page": 118,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 117",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_118_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_118.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p119",
      "book_page": 118,
      "pdf_page": 119,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 118",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_119_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_119.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p120",
      "book_page": 119,
      "pdf_page": 120,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 119",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_120_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_120.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p121",
      "book_page": 120,
      "pdf_page": 121,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 120",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_121_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_121.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p122",
      "book_page": 121,
      "pdf_page": 122,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 121",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_122_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_122.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p123",
      "book_page": 122,
      "pdf_page": 123,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 122",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_123_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_123.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p124",
      "book_page": 123,
      "pdf_page": 124,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 123",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_124_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_124.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p125",
      "book_page": 124,
      "pdf_page": 125,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 124",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_125_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_125.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p126",
      "book_page": 125,
      "pdf_page": 126,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 125",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_126_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_126.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p127",
      "book_page": 126,
      "pdf_page": 127,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 126",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_127_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_127.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p128",
      "book_page": 127,
      "pdf_page": 128,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 127",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_128_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_128.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p129",
      "book_page": 128,
      "pdf_page": 129,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 128",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_129_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_129.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p130",
      "book_page": 129,
      "pdf_page": 130,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 129",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_130_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_130.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p131",
      "book_page": 130,
      "pdf_page": 131,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 130",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_131_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_131.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p132",
      "book_page": 131,
      "pdf_page": 132,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 131",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_132_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_132.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p133",
      "book_page": 132,
      "pdf_page": 133,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 132",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_133_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_133.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p134",
      "book_page": 133,
      "pdf_page": 134,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 133",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_134_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_134.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p135",
      "book_page": 134,
      "pdf_page": 135,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 134",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_135_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_135.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p136",
      "book_page": 135,
      "pdf_page": 136,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 135",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_136_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_136.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p137",
      "book_page": 136,
      "pdf_page": 137,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 136",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_137_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_137.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p138",
      "book_page": 137,
      "pdf_page": 138,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 137",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_138_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_138.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p139",
      "book_page": 138,
      "pdf_page": 139,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 138",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_139_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_139.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p140",
      "book_page": 139,
      "pdf_page": 140,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 139",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_140_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_140.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p141",
      "book_page": 140,
      "pdf_page": 141,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 140",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_141_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_141.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p142",
      "book_page": 141,
      "pdf_page": 142,
      "type": "lesson",
      "title": "الوحدة الخامسة: الفيزياء الذرية ونظرية بور — ص 141",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_142_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_142.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p143",
      "book_page": 142,
      "pdf_page": 143,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة الخامسة: الفيزياء الذرية ونظرية بور",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_143_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_143.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p144",
      "book_page": 143,
      "pdf_page": 144,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة الخامسة: الفيزياء الذرية ونظرية بور",
      "unit_id": "u5",
      "image": "assets/curriculum/grade12/physics/pages/page_144_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_144.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p145",
      "book_page": 144,
      "pdf_page": 145,
      "type": "unit_cover",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — غلاف وأهداف الوحدة",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_145_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_145.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p146",
      "book_page": 145,
      "pdf_page": 146,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 145",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_146_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_146.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p147",
      "book_page": 146,
      "pdf_page": 147,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 146",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_147_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_147.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p148",
      "book_page": 147,
      "pdf_page": 148,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 147",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_148_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_148.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p149",
      "book_page": 148,
      "pdf_page": 149,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 148",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_149_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_149.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p150",
      "book_page": 149,
      "pdf_page": 150,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 149",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_150_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_150.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p151",
      "book_page": 150,
      "pdf_page": 151,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 150",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_151_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_151.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p152",
      "book_page": 151,
      "pdf_page": 152,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 151",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_152_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_152.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p153",
      "book_page": 152,
      "pdf_page": 153,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 152",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_153_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_153.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p154",
      "book_page": 153,
      "pdf_page": 154,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 153",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_154_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_154.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p155",
      "book_page": 154,
      "pdf_page": 155,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 154",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_155_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_155.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p156",
      "book_page": 155,
      "pdf_page": 156,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 155",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_156_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_156.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p157",
      "book_page": 156,
      "pdf_page": 157,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 156",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_157_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_157.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p158",
      "book_page": 157,
      "pdf_page": 158,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 157",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_158_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_158.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p159",
      "book_page": 158,
      "pdf_page": 159,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 158",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_159_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_159.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p160",
      "book_page": 159,
      "pdf_page": 160,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 159",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_160_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_160.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p161",
      "book_page": 160,
      "pdf_page": 161,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 160",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_161_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_161.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p162",
      "book_page": 161,
      "pdf_page": 162,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 161",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_162_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_162.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p163",
      "book_page": 162,
      "pdf_page": 163,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 162",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_163_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_163.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p164",
      "book_page": 163,
      "pdf_page": 164,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 163",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_164_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_164.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p165",
      "book_page": 164,
      "pdf_page": 165,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 164",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_165_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_165.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p166",
      "book_page": 165,
      "pdf_page": 166,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 165",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_166_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_166.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p167",
      "book_page": 166,
      "pdf_page": 167,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 166",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_167_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_167.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p168",
      "book_page": 167,
      "pdf_page": 168,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 167",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_168_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_168.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p169",
      "book_page": 168,
      "pdf_page": 169,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 168",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_169_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_169.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p170",
      "book_page": 169,
      "pdf_page": 170,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 169",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_170_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_170.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p171",
      "book_page": 170,
      "pdf_page": 171,
      "type": "lesson",
      "title": "الوحدة السادسة: الإشعاع والمادة (الكمية والليزر) — ص 170",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_171_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_171.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p172",
      "book_page": 171,
      "pdf_page": 172,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة السادسة: الإشعاع والمادة (الكمية والليزر)",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_172_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_172.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p173",
      "book_page": 172,
      "pdf_page": 173,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة السادسة: الإشعاع والمادة (الكمية والليزر)",
      "unit_id": "u6",
      "image": "assets/curriculum/grade12/physics/pages/page_173_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_173.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p174",
      "book_page": 173,
      "pdf_page": 174,
      "type": "unit_cover",
      "title": "الوحدة السابعة: الفيزياء النووية — غلاف وأهداف الوحدة",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/physics/pages/page_174_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_174.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p175",
      "book_page": 174,
      "pdf_page": 175,
      "type": "lesson",
      "title": "الوحدة السابعة: الفيزياء النووية — ص 174",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/physics/pages/page_175_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_175.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p176",
      "book_page": 175,
      "pdf_page": 176,
      "type": "lesson",
      "title": "الوحدة السابعة: الفيزياء النووية — ص 175",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/physics/pages/page_176_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_176.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p177",
      "book_page": 176,
      "pdf_page": 177,
      "type": "lesson",
      "title": "الوحدة السابعة: الفيزياء النووية — ص 176",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/physics/pages/page_177_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_177.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p178",
      "book_page": 177,
      "pdf_page": 178,
      "type": "lesson",
      "title": "الوحدة السابعة: الفيزياء النووية — ص 177",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/physics/pages/page_178_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_178.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p179",
      "book_page": 178,
      "pdf_page": 179,
      "type": "lesson",
      "title": "الوحدة السابعة: الفيزياء النووية — ص 178",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/physics/pages/page_179_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_179.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p180",
      "book_page": 179,
      "pdf_page": 180,
      "type": "lesson",
      "title": "الوحدة السابعة: الفيزياء النووية — ص 179",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/physics/pages/page_180_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_180.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p181",
      "book_page": 180,
      "pdf_page": 181,
      "type": "lesson",
      "title": "الوحدة السابعة: الفيزياء النووية — ص 180",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/physics/pages/page_181_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_181.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p182",
      "book_page": 181,
      "pdf_page": 182,
      "type": "lesson",
      "title": "الوحدة السابعة: الفيزياء النووية — ص 181",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/physics/pages/page_182_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_182.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p183",
      "book_page": 182,
      "pdf_page": 183,
      "type": "lesson",
      "title": "الوحدة السابعة: الفيزياء النووية — ص 182",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/physics/pages/page_183_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_183.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p184",
      "book_page": 183,
      "pdf_page": 184,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة السابعة: الفيزياء النووية",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/physics/pages/page_184_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_184.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p185",
      "book_page": 184,
      "pdf_page": 185,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة السابعة: الفيزياء النووية",
      "unit_id": "u7",
      "image": "assets/curriculum/grade12/physics/pages/page_185_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_185.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p186",
      "book_page": 185,
      "pdf_page": 186,
      "type": "unit_cover",
      "title": "الوحدة الثامنة: الطاقة الشمسية وتطبيقاتها — غلاف وأهداف الوحدة",
      "unit_id": "u8",
      "image": "assets/curriculum/grade12/physics/pages/page_186_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_186.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p187",
      "book_page": 186,
      "pdf_page": 187,
      "type": "lesson",
      "title": "الوحدة الثامنة: الطاقة الشمسية وتطبيقاتها — ص 186",
      "unit_id": "u8",
      "image": "assets/curriculum/grade12/physics/pages/page_187_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_187.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p188",
      "book_page": 187,
      "pdf_page": 188,
      "type": "lesson",
      "title": "الوحدة الثامنة: الطاقة الشمسية وتطبيقاتها — ص 187",
      "unit_id": "u8",
      "image": "assets/curriculum/grade12/physics/pages/page_188_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_188.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p189",
      "book_page": 188,
      "pdf_page": 189,
      "type": "lesson",
      "title": "الوحدة الثامنة: الطاقة الشمسية وتطبيقاتها — ص 188",
      "unit_id": "u8",
      "image": "assets/curriculum/grade12/physics/pages/page_189_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_189.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p190",
      "book_page": 189,
      "pdf_page": 190,
      "type": "lesson",
      "title": "الوحدة الثامنة: الطاقة الشمسية وتطبيقاتها — ص 189",
      "unit_id": "u8",
      "image": "assets/curriculum/grade12/physics/pages/page_190_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_190.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p191",
      "book_page": 190,
      "pdf_page": 191,
      "type": "lesson",
      "title": "الوحدة الثامنة: الطاقة الشمسية وتطبيقاتها — ص 190",
      "unit_id": "u8",
      "image": "assets/curriculum/grade12/physics/pages/page_191_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_191.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p192",
      "book_page": 191,
      "pdf_page": 192,
      "type": "lesson",
      "title": "الوحدة الثامنة: الطاقة الشمسية وتطبيقاتها — ص 191",
      "unit_id": "u8",
      "image": "assets/curriculum/grade12/physics/pages/page_192_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_192.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p193",
      "book_page": 192,
      "pdf_page": 193,
      "type": "lesson",
      "title": "الوحدة الثامنة: الطاقة الشمسية وتطبيقاتها — ص 192",
      "unit_id": "u8",
      "image": "assets/curriculum/grade12/physics/pages/page_193_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_193.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p194",
      "book_page": 193,
      "pdf_page": 194,
      "type": "lesson",
      "title": "الوحدة الثامنة: الطاقة الشمسية وتطبيقاتها — ص 193",
      "unit_id": "u8",
      "image": "assets/curriculum/grade12/physics/pages/page_194_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_194.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p195",
      "book_page": 194,
      "pdf_page": 195,
      "type": "lesson",
      "title": "الوحدة الثامنة: الطاقة الشمسية وتطبيقاتها — ص 194",
      "unit_id": "u8",
      "image": "assets/curriculum/grade12/physics/pages/page_195_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_195.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p196",
      "book_page": 195,
      "pdf_page": 196,
      "type": "lesson",
      "title": "الوحدة الثامنة: الطاقة الشمسية وتطبيقاتها — ص 195",
      "unit_id": "u8",
      "image": "assets/curriculum/grade12/physics/pages/page_196_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_196.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p197",
      "book_page": 196,
      "pdf_page": 197,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة الثامنة: الطاقة الشمسية وتطبيقاتها",
      "unit_id": "u8",
      "image": "assets/curriculum/grade12/physics/pages/page_197_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_197.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p198",
      "book_page": 197,
      "pdf_page": 198,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة الثامنة: الطاقة الشمسية وتطبيقاتها",
      "unit_id": "u8",
      "image": "assets/curriculum/grade12/physics/pages/page_198_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_198.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p199",
      "book_page": 198,
      "pdf_page": 199,
      "type": "unit_cover",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — غلاف وأهداف الوحدة",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_199_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_199.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p200",
      "book_page": 199,
      "pdf_page": 200,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 199",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_200_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_200.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p201",
      "book_page": 200,
      "pdf_page": 201,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 200",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_201_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_201.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p202",
      "book_page": 201,
      "pdf_page": 202,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 201",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_202_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_202.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p203",
      "book_page": 202,
      "pdf_page": 203,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 202",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_203_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_203.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p204",
      "book_page": 203,
      "pdf_page": 204,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 203",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_204_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_204.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p205",
      "book_page": 204,
      "pdf_page": 205,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 204",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_205_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_205.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p206",
      "book_page": 205,
      "pdf_page": 206,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 205",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_206_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_206.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p207",
      "book_page": 206,
      "pdf_page": 207,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 206",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_207_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_207.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p208",
      "book_page": 207,
      "pdf_page": 208,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 207",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_208_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_208.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p209",
      "book_page": 208,
      "pdf_page": 209,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 208",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_209_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_209.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p210",
      "book_page": 209,
      "pdf_page": 210,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 209",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_210_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_210.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p211",
      "book_page": 210,
      "pdf_page": 211,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 210",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_211_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_211.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p212",
      "book_page": 211,
      "pdf_page": 212,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 211",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_212_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_212.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p213",
      "book_page": 212,
      "pdf_page": 213,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 212",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_213_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_213.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p214",
      "book_page": 213,
      "pdf_page": 214,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 213",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_214_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_214.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p215",
      "book_page": 214,
      "pdf_page": 215,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 214",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_215_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_215.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p216",
      "book_page": 215,
      "pdf_page": 216,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 215",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_216_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_216.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p217",
      "book_page": 216,
      "pdf_page": 217,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 216",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_217_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_217.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p218",
      "book_page": 217,
      "pdf_page": 218,
      "type": "lesson",
      "title": "الوحدة التاسعة: الفيزياء الكونية والفلكية — ص 217",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_218_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_218.jpg",
      "aspect_ratio": 0.7083
    },
    {
      "page_id": "phys12-p219",
      "book_page": 218,
      "pdf_page": 219,
      "type": "assessment",
      "title": "تقويم وتمارين ومسائل الوحدة التاسعة: الفيزياء الكونية والفلكية",
      "unit_id": "u9",
      "image": "assets/curriculum/grade12/physics/pages/page_219_opt.jpg",
      "image_full": "assets/curriculum/grade12/physics/pages/page_219.jpg",
      "aspect_ratio": 0.7083
    }
  ],
  "lessons": [
    {
      "id": "phys-u1-l1",
      "unitId": "u1",
      "order": 1,
      "title": "كمية التحرك والتصادم في بعدين",
      "pages": [
        10,
        14
      ],
      "pdf_pages": [
        11,
        15
      ]
    },
    {
      "id": "phys-u1-l2",
      "unitId": "u1",
      "order": 2,
      "title": "الصواريخ ذاتية الدفع وسرعة الإفلات",
      "pages": [
        14,
        18
      ],
      "pdf_pages": [
        15,
        19
      ]
    },
    {
      "id": "phys-u1-l3",
      "unitId": "u1",
      "order": 3,
      "title": "حركة الأقمار الصناعية وكمية التحرك الزاوي",
      "pages": [
        19,
        22
      ],
      "pdf_pages": [
        20,
        23
      ]
    },
    {
      "id": "phys-u1-l4",
      "unitId": "u1",
      "order": 4,
      "title": "حركة المقذوفات في مجال الجاذبية",
      "pages": [
        23,
        26
      ],
      "pdf_pages": [
        24,
        27
      ]
    },
    {
      "id": "phys-u1-l5",
      "unitId": "u1",
      "order": 5,
      "title": "تقويم ومسائل الوحدة الأولى",
      "pages": [
        27,
        28
      ],
      "pdf_pages": [
        28,
        29
      ]
    },
    {
      "id": "phys-u2-l1",
      "unitId": "u2",
      "order": 1,
      "title": "مفهوم التيار المتردد ومولد الدينامو",
      "pages": [
        30,
        36
      ],
      "pdf_pages": [
        31,
        37
      ]
    },
    {
      "id": "phys-u2-l2",
      "unitId": "u2",
      "order": 2,
      "title": "الأميتر الحراري وقانون أوم في دوائر المتردد",
      "pages": [
        37,
        39
      ],
      "pdf_pages": [
        38,
        40
      ]
    },
    {
      "id": "phys-u2-l3",
      "unitId": "u2",
      "order": 3,
      "title": "المكثف والملف في دوائر التيار المتردد والمفاعلة",
      "pages": [
        40,
        46
      ],
      "pdf_pages": [
        41,
        47
      ]
    },
    {
      "id": "phys-u2-l4",
      "unitId": "u2",
      "order": 4,
      "title": "دائرة RLC المتوالية والمعاوقة وزاوية الطور",
      "pages": [
        47,
        50
      ],
      "pdf_pages": [
        48,
        51
      ]
    },
    {
      "id": "phys-u2-l5",
      "unitId": "u2",
      "order": 5,
      "title": "دائرة الرنين والدائرة المهتزة وتوصيل المعاوقات",
      "pages": [
        51,
        57
      ],
      "pdf_pages": [
        52,
        58
      ]
    },
    {
      "id": "phys-u2-l6",
      "unitId": "u2",
      "order": 6,
      "title": "تقويم ومسائل التيار المتردد",
      "pages": [
        58,
        60
      ],
      "pdf_pages": [
        59,
        61
      ]
    },
    {
      "id": "phys-u3-l1",
      "unitId": "u3",
      "order": 1,
      "title": "أشباه الموصلات النقية وغير النقية (التطعيم)",
      "pages": [
        62,
        66
      ],
      "pdf_pages": [
        63,
        67
      ]
    },
    {
      "id": "phys-u3-l2",
      "unitId": "u3",
      "order": 2,
      "title": "الوصلة الثنائية (الدايود) وتقويم التيار",
      "pages": [
        67,
        70
      ],
      "pdf_pages": [
        68,
        71
      ]
    },
    {
      "id": "phys-u3-l3",
      "unitId": "u3",
      "order": 3,
      "title": "الترانزستور: تركيبه واستخداماته كمكبر ومفتاح",
      "pages": [
        71,
        79
      ],
      "pdf_pages": [
        72,
        80
      ]
    },
    {
      "id": "phys-u3-l4",
      "unitId": "u3",
      "order": 4,
      "title": "تقويم ومسائل الإلكترونيات",
      "pages": [
        80,
        84
      ],
      "pdf_pages": [
        81,
        85
      ]
    },
    {
      "id": "phys-u4-l1",
      "unitId": "u4",
      "order": 1,
      "title": "التفريغ الكهربائي في الغازات وأنبوبة أشعة المهبط",
      "pages": [
        87,
        89
      ],
      "pdf_pages": [
        88,
        90
      ]
    },
    {
      "id": "phys-u4-l2",
      "unitId": "u4",
      "order": 2,
      "title": "كاشف الذبذبات (الأوسيلوسكوب) والرادار",
      "pages": [
        90,
        94
      ],
      "pdf_pages": [
        91,
        95
      ]
    },
    {
      "id": "phys-u4-l3",
      "unitId": "u4",
      "order": 3,
      "title": "إرسال واستقبال الموجات اللاسلكية والتلفاز الملون",
      "pages": [
        95,
        106
      ],
      "pdf_pages": [
        96,
        107
      ]
    },
    {
      "id": "phys-u4-l4",
      "unitId": "u4",
      "order": 4,
      "title": "تقويم الأجهزة الإلكترونية والاتصالات",
      "pages": [
        107,
        113
      ],
      "pdf_pages": [
        108,
        114
      ]
    },
    {
      "id": "phys-u5-l1",
      "unitId": "u5",
      "order": 1,
      "title": "نماذج الذرة وأطياف الانبعاث وطيف الهيدروجين",
      "pages": [
        115,
        122
      ],
      "pdf_pages": [
        116,
        123
      ]
    },
    {
      "id": "phys-u5-l2",
      "unitId": "u5",
      "order": 2,
      "title": "إشعاع الجسم الأسود وتكميم الطاقة لبلانك",
      "pages": [
        123,
        124
      ],
      "pdf_pages": [
        124,
        125
      ]
    },
    {
      "id": "phys-u5-l3",
      "unitId": "u5",
      "order": 3,
      "title": "نظرية بور لذرة الهيدروجين ومستويات الطاقة",
      "pages": [
        125,
        141
      ],
      "pdf_pages": [
        126,
        142
      ]
    },
    {
      "id": "phys-u5-l4",
      "unitId": "u5",
      "order": 4,
      "title": "تقويم ومسائل الفيزياء الذرية",
      "pages": [
        142,
        143
      ],
      "pdf_pages": [
        143,
        144
      ]
    },
    {
      "id": "phys-u6-l1",
      "unitId": "u6",
      "order": 1,
      "title": "الظاهرة الكهروضوئية وتفسير أينشتاين الكمي",
      "pages": [
        145,
        156
      ],
      "pdf_pages": [
        146,
        157
      ]
    },
    {
      "id": "phys-u6-l2",
      "unitId": "u6",
      "order": 2,
      "title": "الأشعة السينية (أشعة إكس) وخصائصها وتوليدها",
      "pages": [
        157,
        162
      ],
      "pdf_pages": [
        158,
        163
      ]
    },
    {
      "id": "phys-u6-l3",
      "unitId": "u6",
      "order": 3,
      "title": "الليزر: فكرته، شروطه، وجهاز هيليوم - نيون",
      "pages": [
        163,
        170
      ],
      "pdf_pages": [
        164,
        171
      ]
    },
    {
      "id": "phys-u6-l4",
      "unitId": "u6",
      "order": 4,
      "title": "تقويم ومسائل الإشعاع والمادة",
      "pages": [
        171,
        172
      ],
      "pdf_pages": [
        172,
        173
      ]
    },
    {
      "id": "phys-u7-l1",
      "unitId": "u7",
      "order": 1,
      "title": "تركيب النواة والنشاط الإشعاعي الطبيعي",
      "pages": [
        174,
        178
      ],
      "pdf_pages": [
        175,
        179
      ]
    },
    {
      "id": "phys-u7-l2",
      "unitId": "u7",
      "order": 2,
      "title": "قانون عمر النصف وطاقة الربط النووية",
      "pages": [
        179,
        180
      ],
      "pdf_pages": [
        180,
        181
      ]
    },
    {
      "id": "phys-u7-l3",
      "unitId": "u7",
      "order": 3,
      "title": "الانشطار والتفاعل المتسلسل والمفاعلات النووية",
      "pages": [
        181,
        182
      ],
      "pdf_pages": [
        182,
        183
      ]
    },
    {
      "id": "phys-u7-l4",
      "unitId": "u7",
      "order": 4,
      "title": "تقويم ومسائل الفيزياء النووية",
      "pages": [
        183,
        184
      ],
      "pdf_pages": [
        184,
        185
      ]
    },
    {
      "id": "phys-u8-l1",
      "unitId": "u8",
      "order": 1,
      "title": "الشمس مصدر الطاقة وأنواع الإشعاعات الشمسية",
      "pages": [
        186,
        188
      ],
      "pdf_pages": [
        187,
        189
      ]
    },
    {
      "id": "phys-u8-l2",
      "unitId": "u8",
      "order": 2,
      "title": "تطبيقات الطاقة الشمسية وتوليد الحرارة والكهرباء",
      "pages": [
        189,
        196
      ],
      "pdf_pages": [
        190,
        197
      ]
    },
    {
      "id": "phys-u8-l3",
      "unitId": "u8",
      "order": 3,
      "title": "تقويم وتطبيقات الطاقة الشمسية في اليمن",
      "pages": [
        197,
        197
      ],
      "pdf_pages": [
        198,
        198
      ]
    },
    {
      "id": "phys-u9-l1",
      "unitId": "u9",
      "order": 1,
      "title": "مفهوم الكون ونظرية الانفجار العظيم والمجرات",
      "pages": [
        199,
        203
      ],
      "pdf_pages": [
        200,
        204
      ]
    },
    {
      "id": "phys-u9-l2",
      "unitId": "u9",
      "order": 2,
      "title": "النجوم ودورة حياتها والثقوب السوداء",
      "pages": [
        204,
        207
      ],
      "pdf_pages": [
        205,
        208
      ]
    },
    {
      "id": "phys-u9-l3",
      "unitId": "u9",
      "order": 3,
      "title": "المسافات الفلكية وتقدير حرارة النجوم من ألوانها",
      "pages": [
        208,
        209
      ],
      "pdf_pages": [
        209,
        210
      ]
    },
    {
      "id": "phys-u9-l4",
      "unitId": "u9",
      "order": 4,
      "title": "تقويم الوحدة وقاموس المصطلحات الفيزيائية",
      "pages": [
        210,
        219
      ],
      "pdf_pages": [
        211,
        220
      ]
    }
  ],
  "interactions": {
    "phys12-p011": [
      {
        "id": "elem-phys-p11-def-p",
        "type": "explainable_text",
        "title": "قانون كمية التحرك الخطي P = mv",
        "bounds": {
          "x": 0.12,
          "y": 0.18,
          "w": 0.76,
          "h": 0.16
        },
        "explanation_ref": "exp-phys-u1-momentum",
        "highlight_color": "rgba(0, 168, 89, 0.22)",
        "indicator_label": "📌 قانون فيزيائي أساسي"
      },
      {
        "id": "elem-phys-p11-collision-sim",
        "type": "interactive_3d",
        "title": "محاكاة تصادم الأجسام في بعدين",
        "bounds": {
          "x": 0.12,
          "y": 0.42,
          "w": 0.76,
          "h": 0.28
        },
        "diagram_ref": "diag-phys-projectiles-3d",
        "highlight_color": "rgba(2, 132, 199, 0.25)",
        "indicator_label": "🔍 استكشاف التصادم 3D"
      },
      {
        "id": "elem-phys-p11-quiz-btn",
        "type": "assessment",
        "title": "اختبر نفسك: كمية التحرك والتصادم",
        "bounds": {
          "x": 0.12,
          "y": 0.75,
          "w": 0.76,
          "h": 0.08
        },
        "assessment_ref": "quiz-phys-u1",
        "highlight_color": "rgba(245, 158, 11, 0.22)",
        "indicator_label": "❓ اختبر فهمك فورا"
      }
    ],
    "phys12-p018": [
      {
        "id": "elem-phys-p18-esc-vel",
        "type": "explainable_text",
        "title": "سرعة الإفلات من الجاذبية الأرضية",
        "bounds": {
          "x": 0.12,
          "y": 0.2,
          "w": 0.76,
          "h": 0.22
        },
        "explanation_ref": "exp-phys-u1-escape-velocity",
        "highlight_color": "rgba(0, 168, 89, 0.22)",
        "indicator_label": "📌 سرعة الإفلات 11.2 كم/ث"
      }
    ],
    "phys12-p024": [
      {
        "id": "elem-phys-p24-projectiles-law",
        "type": "explainable_text",
        "title": "حركة المقذوفات في بعدين وزاوية 45°",
        "bounds": {
          "x": 0.12,
          "y": 0.15,
          "w": 0.76,
          "h": 0.2
        },
        "explanation_ref": "exp-phys-u1-projectiles",
        "highlight_color": "rgba(0, 168, 89, 0.22)",
        "indicator_label": "📌 قوانين المقذوفات"
      },
      {
        "id": "elem-phys-p24-proj-act",
        "type": "activity",
        "title": "نشاط تفاعلي: اختبار زوايا الإطلاق",
        "bounds": {
          "x": 0.12,
          "y": 0.4,
          "w": 0.76,
          "h": 0.1
        },
        "activity_ref": "act-phys-projectiles-angle",
        "highlight_color": "rgba(245, 158, 11, 0.25)",
        "indicator_label": "🧪 نشاط عملي تفاعلي"
      },
      {
        "id": "elem-phys-p24-proj-3d",
        "type": "interactive_3d",
        "title": "مختبر المقذوفات ثلاثي الأبعاد",
        "bounds": {
          "x": 0.12,
          "y": 0.55,
          "w": 0.76,
          "h": 0.26
        },
        "diagram_ref": "diag-phys-projectiles-3d",
        "highlight_color": "rgba(139, 92, 246, 0.25)",
        "indicator_label": "🔍 مختبر المقذوفات 3D"
      }
    ],
    "phys12-p033": [
      {
        "id": "elem-phys-p33-dynamo-law",
        "type": "explainable_text",
        "title": "مولد الدينامو والقوة الدافعة الحثية",
        "bounds": {
          "x": 0.12,
          "y": 0.15,
          "w": 0.76,
          "h": 0.2
        },
        "explanation_ref": "exp-phys-u2-dynamo",
        "highlight_color": "rgba(0, 168, 89, 0.22)",
        "indicator_label": "📌 قانون الدينامو E_max"
      },
      {
        "id": "elem-phys-p33-dynamo-act",
        "type": "activity",
        "title": "نشاط تفاعلي: دوران ملف الدينامو وتوليد التيار",
        "bounds": {
          "x": 0.12,
          "y": 0.38,
          "w": 0.76,
          "h": 0.1
        },
        "activity_ref": "act-phys-dynamo-induction",
        "highlight_color": "rgba(245, 158, 11, 0.25)",
        "indicator_label": "🧪 نشاط عملي تفاعلي"
      },
      {
        "id": "elem-phys-p33-dynamo-3d",
        "type": "interactive_3d",
        "title": "نموذج الدينامو ثلاثي الأبعاد 3D",
        "bounds": {
          "x": 0.12,
          "y": 0.52,
          "w": 0.76,
          "h": 0.28
        },
        "diagram_ref": "diag-phys-dynamo-3d",
        "highlight_color": "rgba(2, 132, 199, 0.25)",
        "indicator_label": "🔍 استكشاف الدينامو 3D"
      }
    ],
    "phys12-p051": [
      {
        "id": "elem-phys-p51-rlc-law",
        "type": "explainable_text",
        "title": "دائرة الرنين RLC والمعاوقة الكلية",
        "bounds": {
          "x": 0.12,
          "y": 0.18,
          "w": 0.76,
          "h": 0.22
        },
        "explanation_ref": "exp-phys-u2-rlc-resonance",
        "highlight_color": "rgba(0, 168, 89, 0.22)",
        "indicator_label": "📌 دائرة الرنين والمعاوقة"
      },
      {
        "id": "elem-phys-p51-rlc-sim",
        "type": "interactive_3d",
        "title": "مختبر دوائر RLC الافتراضي",
        "bounds": {
          "x": 0.12,
          "y": 0.45,
          "w": 0.76,
          "h": 0.28
        },
        "diagram_ref": "diag-phys-rlc-circuit",
        "highlight_color": "rgba(2, 132, 199, 0.25)",
        "indicator_label": "🔍 محاكي دوائر RLC"
      }
    ],
    "phys12-p126": [
      {
        "id": "elem-phys-p126-bohr-law",
        "type": "explainable_text",
        "title": "فروض نظرية بور لذرة الهيدروجين",
        "bounds": {
          "x": 0.12,
          "y": 0.18,
          "w": 0.76,
          "h": 0.22
        },
        "explanation_ref": "exp-phys-u5-bohr-atom",
        "highlight_color": "rgba(0, 168, 89, 0.22)",
        "indicator_label": "📌 نظرية بور لذرة الهيدروجين"
      },
      {
        "id": "elem-phys-p126-bohr-3d",
        "type": "interactive_3d",
        "title": "نموذج بور الذري ثلاثي الأبعاد",
        "bounds": {
          "x": 0.12,
          "y": 0.45,
          "w": 0.76,
          "h": 0.28
        },
        "diagram_ref": "diag-phys-bohr-atom-3d",
        "highlight_color": "rgba(139, 92, 246, 0.25)",
        "indicator_label": "🔍 نموذج ذرة الهيدروجين 3D"
      }
    ],
    "phys12-p146": [
      {
        "id": "elem-phys-p146-photo-law",
        "type": "explainable_text",
        "title": "الظاهرة الكهروضوئية وتفسير أينشتاين",
        "bounds": {
          "x": 0.12,
          "y": 0.18,
          "w": 0.76,
          "h": 0.22
        },
        "explanation_ref": "exp-phys-u6-photoelectric",
        "highlight_color": "rgba(0, 168, 89, 0.22)",
        "indicator_label": "📌 معادلة أينشتاين الكهروضوئية"
      },
      {
        "id": "elem-phys-p146-photo-act",
        "type": "activity",
        "title": "نشاط تعيين تردد العتبة ودالة الشغل",
        "bounds": {
          "x": 0.12,
          "y": 0.44,
          "w": 0.76,
          "h": 0.1
        },
        "activity_ref": "act-phys-photoelectric-threshold",
        "highlight_color": "rgba(245, 158, 11, 0.25)",
        "indicator_label": "🧪 نشاط عملي تفاعلي"
      },
      {
        "id": "elem-phys-p146-photo-lab",
        "type": "interactive_3d",
        "title": "معمل الظاهرة الكهروضوئية التفاعلي",
        "bounds": {
          "x": 0.12,
          "y": 0.58,
          "w": 0.76,
          "h": 0.26
        },
        "diagram_ref": "diag-phys-photoelectric-lab",
        "highlight_color": "rgba(2, 132, 199, 0.25)",
        "indicator_label": "🔍 معمل مليكان الكهروضوئي"
      }
    ]
  },
  "explanations": {
    "exp-phys-u1-momentum": {
      "title": "كمية التحرك الخطي وحفظ كمية التحرك",
      "original_text": "كمية التحرك لجسم متحرك هي حاصل ضرب كتلته في سرعته المتجهة (P = m * v). وفي أي نظام مغلق ومعزول، يظل المجموع الكلي لكمية التحرك للأجسام المتصادمة ثابتاً قبل التصادم وبعده.",
      "levels": {
        "basic": "كمية التحرك هي مقياس لمدى صعوبة إيقاف جسم متحرك، وتعتمد على شيئين: ثقل الجسم (كتلته) وسرعته. كلما زادت الكتلة أو السرعة، صعب إيقافه.",
        "intermediate": "كمية التحرك كمية متجهة يكون اتجاهها دائماً في نفس اتجاه متجه السرعة. في التصادمات، ما يفقده جسم من كمية تحرك يكتسبه الجسم الآخر تماماً دون أي ضياع.",
        "advanced": "يشتق قانون حفظ كمية التحرك مباشرة من قانون نيوتن الثالث (لكل فعل رد فعل مساوٍ له في المقدار ومضاد له في الاتجاه)، حيث F_net = dP/dt، وعند انعدام القوى الخارجية المحصلة يكون dP/dt = 0 وبالتالي P_total = ثابت."
      },
      "equations": [
        {
          "label": "قانون كمية التحرك الخطي",
          "eq": "P = m · v",
          "symbols": {
            "P": "كمية التحرك (kg·m/s)",
            "m": "كتلة الجسم (kg)",
            "v": "سرعة الجسم (m/s)"
          }
        },
        {
          "label": "حفظ كمية التحرك في التصادم",
          "eq": "m₁v₁ + m₂v₂ = m₁v₁' + m₂v₂'",
          "symbols": {
            "v₁, v₂": "السرعات قبل التصادم",
            "v₁', v₂'": "السرعات بعد التصادم"
          }
        }
      ],
      "vocabulary_ids": [
        "vocab-linear-momentum",
        "vocab-elastic-collision"
      ],
      "real_world_example": "شاحنة نقل بضائع ثقيلة تتحرك ببطء في نقيل يسلح تمتلك كمية تحرك هائلة تجعل فرملتها وإيقافها يتطلب مسافة أطول بكثير من سيارة صالون صغيرة تسير بنفس السرعة.",
      "tts_text": "كمية التحرك هي حاصل ضرب كتلة الجسم في سرعته المتجهة، وفي أي تصادم ضمن نظام معزول تظل كمية التحرك الكلية ثابتة ومحفوظة."
    },
    "exp-phys-u1-escape-velocity": {
      "title": "سرعة الإفلات من الجاذبية الأرضية",
      "original_text": "سرعة الإفلات هي أقل سرعة ابتدائية ينطلق بها جسم رأسياً إلى أعلى ليتخلص نهائياً من مجال جاذبية الأرض دون العودة إليها، وقيمتها للأرض تساوي تقريباً 11.2 كم/ث.",
      "levels": {
        "basic": "هي أسرع انطلاقة يحتاجها الصاروخ حتى يهرب من جاذبية الأرض ولا يسقط عليها مرة ثانية.",
        "intermediate": "لكي يفلت الجسم، يجب أن تكون طاقة حركته الابتدائية مساوية على الأقل للشغل اللازم للتغلب على قوة الجذب من سطح الأرض إلى ما لا نهاية (حيث طاقة الوضع تساوي صفراً).",
        "advanced": "من مبدأ حفظ الطاقة الميكانيكية: E = KE + PE = 0 في اللانهاية، إذن 0.5 * m * v_esc^2 - (G * M * m / R) = 0، ومنها v_esc = sqrt(2 * G * M / R) = sqrt(2 * g * R)، وهي لا تعتمد إطلاقاً على كتلة الجسم المقذوف."
      },
      "equations": [
        {
          "label": "معادلة سرعة الإفلات",
          "eq": "v_esc = √(2GM / R) = √(2gR)",
          "symbols": {
            "G": "ثابت الجذب العام",
            "M": "كتلة الكوكب (kg)",
            "R": "نصف قطر الكوكب (m)",
            "g": "تسارع الجاذبية"
          }
        }
      ],
      "vocabulary_ids": [
        "vocab-escape-velocity",
        "vocab-gravitational-field"
      ],
      "real_world_example": "صواريخ مركبات الفضاء مثل رحلات أبولو أو مسبار الأمل تنطلق بسرعات تتجاوز 11.2 كم/ث لتتمكن من مغادرة مدار الأرض نحو القمر أو المريخ.",
      "tts_text": "سرعة الإفلات هي أقل سرعة ابتدائية تمكن الجسم من الإفلات التام من جاذبية الأرض وتبلغ 11.2 كيلومتر في الثانية."
    },
    "exp-phys-u1-projectiles": {
      "title": "حركة المقذوفات وزاوية الإطلاق",
      "original_text": "حركة المقذوف في بعدين هي تركيب لحركتين مستقلتين متعامدتين: حركة أفقية منتظمة السرعة (تسارعها صفر)، وحركة رأسية منتظمة التغير تحت تأثير تسارع الجاذبية الأرضية.",
      "levels": {
        "basic": "عندما تقذف كرة بزاوية، تتحرك للأمام بسرعة ثابتة، بينما ترتفع للأعلى وتبطئ ثم تسقط وتسرع بفعل الجاذبية، فيكون مسارها منحنياً (قطع مكافئ).",
        "intermediate": "يتحلل متجه السرعة الابتدائية v0 إلى مركبتين: أفقية v_x = v0 * cos(theta) ورأسية v_y = v0 * sin(theta). المدى الأفقي يكون أقصى ما يمكن عند زاوية إطلاق 45 درجة.",
        "advanced": "معادلة المسار خالية من الزمن: y = x * tan(theta) - (g * x^2) / (2 * v0^2 * cos^2(theta)) وهي معادلة قطع مكافئ. أقصى ارتفاع H = (v0*sin(theta))^2 / (2g)، وزمن التحليق الكلي T = 2*v0*sin(theta) / g."
      },
      "equations": [
        {
          "label": "أقصى ارتفاع للمقذوف",
          "eq": "H = (v₀ · sin θ)² / (2g)",
          "symbols": {
            "H": "أقصى ارتفاع (m)",
            "v₀": "السرعة الابتدائية (m/s)",
            "θ": "زاوية الإطلاق",
            "g": "عجلة الجاذبية"
          }
        },
        {
          "label": "المدى الأفقي للمقذوف",
          "eq": "R = (v₀² · sin 2θ) / g",
          "symbols": {
            "R": "أقصى مدى أفقي (m)"
          }
        }
      ],
      "vocabulary_ids": [
        "vocab-projectile-motion",
        "vocab-trajectory-angle"
      ],
      "real_world_example": "لاعب كرة القدم يسدد الكرة بزاوية تقارب 45 درجة لضمان قطع الكرة لأكبر مسافة أفقية ممكنة عبر الملعب.",
      "tts_text": "تتركب حركة المقذوف من سرعة أفقية ثابتة وسرعة رأسية متغيرة بعجلة الجاذبية، وتكون زاوية الإطلاق خمسة وأربعين درجة هي التي تحقق أقصى مدى أفقي."
    },
    "exp-phys-u2-dynamo": {
      "title": "مولد التيار المتردد (الدينامو) وقانون فاراداي",
      "original_text": "يعمل الدينامو على تحويل الطاقة الميكانيكية الدورانية إلى طاقة كهربائية بالحث الكهرومغناطيسي، حيث يدور ملف موصل في مجال مغناطيسي منتظم فتتولد بين طرفيه قوة دافعة حثية جيبية متغيرة القيمة والاتجاه.",
      "levels": {
        "basic": "الدينامو جهاز يدور فيه ملف بين قطبي مغناطيس ليولد تياراً كهربائياً يتغير اتجاهه باستمرار مثل تيار المنازل.",
        "intermediate": "عند دوران الملف بسرعة زاوية ثابتة omega، يتغير الفيض المغناطيسي الذي يقطع لفات الملف جيبيّاً بالنسبة للزمن: Phi = B * A * cos(omega*t)، فيتولد جهد حثي متغير: E = E_max * sin(omega*t).",
        "advanced": "حسب قانون فاراداي: E = -N * (dPhi/dt) = N * B * A * omega * sin(omega*t). تصل القوة الدافعة لقيمتها العظمى E_max = N * B * A * omega عندما يكون مستوى الملف موازياً لخطوط المجال المغناطيسي (زاوية الطور 90 درجة)."
      },
      "equations": [
        {
          "label": "القوة الدافعة اللحظية للدينامو",
          "eq": "E = N · A · B · ω · sin(ωt) = E_max · sin(θ)",
          "symbols": {
            "N": "عدد اللفات",
            "A": "مساحة الملف (m²)",
            "B": "كثافة الفيض (Tesla)",
            "ω": "السرعة الزاوية (rad/s)"
          }
        },
        {
          "label": "القيمة الفعالة للتيار المتردد",
          "eq": "I_eff = I_max / √2 ≈ 0.707 · I_max",
          "symbols": {
            "I_eff": "شدة التيار الفعالة",
            "I_max": "شدة التيار العظمى"
          }
        }
      ],
      "vocabulary_ids": [
        "vocab-ac-dynamo",
        "vocab-effective-value"
      ],
      "real_world_example": "مولدات محطة كهرباء مأرب الغازية أو مولدات الديزل المنزلية تعتمد جميعها على دوران ملفات عملاقة لتوليد جهد متردد بتردد 50 هرتز.",
      "tts_text": "يعتمد مولد الدينامو على ظاهرة الحث الكهرومغناطيسي لتوليد جهد متردد جيبي قيمته العظمى تساوي حاصل ضرب عدد اللفات والمساحة والفيض والسرعة الزاوية."
    },
    "exp-phys-u2-rlc-resonance": {
      "title": "دائرة التيار المتردد RLC وحالة الرنين الكهربائي",
      "original_text": "في دائرة التوالي RLC، تتقدم فولتية الملف على التيار بزاوية 90 درجة بينما تتأخر فولتية المكثف بزاوية 90 درجة. وتتحقق حالة الرنين عندما تتساوى المفاعلة الحثية مع المفاعلة السعوية (X_L = X_C).",
      "levels": {
        "basic": "في دائرة الرنين، تلغي مقاومة الملف مقاومة المكثف تماماً، فتصبح مقاومة الدائرة في أقل قيمة لها، ويمر أكبر تيار ممكن، وهو السر في التقاط محطات الراديو.",
        "intermediate": "المعاوقة الكلية Z = sqrt(R^2 + (X_L - X_C)^2). عند الرنين X_L = X_C فتكون Z = R فقط، وزاوية الطور صفر، ويكون معامل القدرة مساوياً للواحد الصحيح.",
        "advanced": "من مساواة 2*pi*f*L = 1/(2*pi*f*C) نجد تردد الرنين الطبيعي f_0 = 1 / (2 * pi * sqrt(L * C)). عند هذا التردد تكون استجابة الدائرة للإشارات الخارجية بأقصى اتساع ممكن ويصل تيار الدائرة لقيمته العظمى."
      },
      "equations": [
        {
          "label": "معاوقة دائرة التوالي RLC",
          "eq": "Z = √[ R² + (X_L - X_C)² ]",
          "symbols": {
            "Z": "المعاوقة الكلية (Ω)",
            "R": "المقاومة الأومية (Ω)",
            "X_L": "المفاعلة الحثية",
            "X_C": "المفاعلة السعوية"
          }
        },
        {
          "label": "تردد الرنين الكهربائي",
          "eq": "f₀ = 1 / (2π · √(L · C))",
          "symbols": {
            "f₀": "تردد الرنين (Hz)",
            "L": "معامل الحث الذاتي (Henry)",
            "C": "سعة المكثف (Farad)"
          }
        }
      ],
      "vocabulary_ids": [
        "vocab-impedance",
        "vocab-electrical-resonance"
      ],
      "real_world_example": "عند تدوير مقبض الراديو لاختيار إذاعة صنعاء، نقوم بتغيير سعة المكثف المتغير C حتى يتساوى تردد دائرة الرنين مع تردد الإذاعة تماماً فتسمع الصوت بنقاء.",
      "tts_text": "تحدث حالة الرنين في دائرة التيار المتردد عندما تتساوى المفاعلة الحثية مع المفاعلة السعوية فتصبح المعاوقة مساوية للمقاومة الأومية فقط ويمر أكبر تيار."
    },
    "exp-phys-u3-diode-transistor": {
      "title": "الوصلة الثنائية (الدايود) والترانزستور",
      "original_text": "تتكون الوصلة الثنائية من بلورتين شبه موصلتين من النوع p والنوع n متلاصقتين، وتسمح بمرور التيار في اتجاه واحد فقط (الانحياز الأمامي). بينما يعمل الترانزستور (npn أو pnp) كمكبر للجهد والتيار والقدرة ومفتاح إلكتروني فائق السرعة.",
      "levels": {
        "basic": "الدايود صمام يسمح للكهرباء بالمرور في طريق واحد ويمنع رجوعها، والترانزستور صنبور إلكتروني يتحكم بتيار كبير عبر إشارة تيار صغيرة جداً.",
        "intermediate": "في الانحياز الأمامي للدايود يقل جهد الحاجز وتتدفق الشحنات، وفي الانحياز العكسي يتسع الحاجز وينعدم التيار تقريباً. في الترانزستور npn، تيار الباعث I_e يتوزع بين تيار القاعدة الصغير I_b وتيار المجمع I_c: I_e = I_b + I_c.",
        "advanced": "معامل تكبير التيار للترانزستور بطريقة الباعث المشترك beta = delta(I_c) / delta(I_b)، وتتراوح قيمته عادة بين 50 و 300. يستخدم الدايود في دوائر التقويم لتحويل التيار المتردد المتناوب إلى تيار مستمر موحد الاتجاه."
      },
      "equations": [
        {
          "label": "قانون تيارات الترانزستور",
          "eq": "I_e = I_b + I_c",
          "symbols": {
            "I_e": "تيار الباعث",
            "I_b": "تيار القاعدة",
            "I_c": "تيار المجمع"
          }
        },
        {
          "label": "معامل تكبير التيار",
          "eq": "β = I_c / I_b",
          "symbols": {
            "β": "معامل التكبير (بدون وحدة)"
          }
        }
      ],
      "vocabulary_ids": [
        "vocab-pn-junction",
        "vocab-transistor-amplifier"
      ],
      "real_world_example": "شاحن الهاتف الصغير يحتوي على وصلات ثنائية تحول كهرباء المنزل 220 فولت متردد إلى تيار مستمر 5 فولت، وترانزستورات تنظم الجهد وتحمي البطارية.",
      "tts_text": "تسمح الوصلة الثنائية بمرور التيار في الانحياز الأمامي فقط وتستخدم لتقويم التيار، بينما يضخم الترانزستور الإشارات الضعيفة ويعمل كمفتاح رقمي سريع."
    },
    "exp-phys-u5-bohr-atom": {
      "title": "نموذج بور لذرة الهيدروجين ومستويات الطاقة",
      "original_text": "افترض نيلز بور أن الإلكترون يدور حول النواة في مدارات دائرية محددة وثابتة دون أن يشع طاقة، ولا تنبعث الطاقة من الذرة إلا عندما يقفز الإلكترون من مستوى طاقة أعلى إلى مستوى طاقة أدنى على هيئة فوتون ضوئي (Delta E = h * nu).",
      "levels": {
        "basic": "الإلكترونات داخل الذرة تسكن في درجات أو طوابق تسمى مستويات الطاقة، ولا يمكنها التواجد بين الدرجات، وعندما تهبط من طابق مرتفع لطابق منخفض تطلق فوتوناً من الضوء.",
        "intermediate": "طاقة المستوى n لذرة الهيدروجين معطاة بالعلاقة E_n = -13.6 / n^2 إلكترون فولت. إشارة السالب تعني أن الإلكترون مقيد بالنواة ويلزمه 13.6 إلكترون فولت لكي يتحرر تماماً (طاقة التأين).",
        "advanced": "كمم بور كمية التحرك الزاوي: m*v*r = n * (h / 2*pi). انبعاث فوتونات الهيدروجين يفسر متسلسلات الطيف: ليمان (العودة لـ n=1 بالأشعة فوق البنفسجية)، بالمر (العودة لـ n=2 بالضوء المرئي)، وباشن (العودة لـ n=3 بالأشعة تحت الحمراء)."
      },
      "equations": [
        {
          "label": "طاقة المستوى لذرة الهيدروجين",
          "eq": "E_n = -13.6 / n²  [eV]",
          "symbols": {
            "E_n": "طاقة المستوى (eV)",
            "n": "رقم المدار الرئيسي (1, 2, 3...)"
          }
        },
        {
          "label": "طاقة الفوتون المنبعث",
          "eq": "ΔE = E₂ - E₁ = h · ν = h · (c / λ)",
          "symbols": {
            "h": "ثابت بلانك (6.63*10^-34 J·s)",
            "ν": "تردد الفوتون (Hz)",
            "λ": "طول الموجة (m)"
          }
        }
      ],
      "vocabulary_ids": [
        "vocab-bohr-model",
        "vocab-spectral-series"
      ],
      "real_world_example": "الضوء الوردي المميز لأنابيب إعلانات النيون وغاز الهيدروجين ناتج عن قفز مليارات الإلكترونات بين مستويات الطاقة المحددة في ذرات الغاز.",
      "tts_text": "ينص نموذج بور على أن طاقة مدارات الذرة مكممة، وينبعث الضوء كفوتونات محددة الطاقة عند قفز الإلكترون من مدار أعلى إلى مدار أدنى."
    },
    "exp-phys-u6-photoelectric": {
      "title": "الظاهرة الكهروضوئية وتفسير أينشتاين الكمي",
      "original_text": "الظاهرة الكهروضوئية هي انبعاث إلكترونات من سطح فلز عند سقوط ضوء ذي تردد مناسب عليه. فسرها أينشتاين بافتراض أن الضوء يتكون من حزم كمية مركزة من الطاقة تسمى فوتونات، طاقة كل فوتون E = h * nu.",
      "levels": {
        "basic": "عندما يسقط شعاع ضوء بتردد مناسب على لوح معدني، يصطدم فوتون الضوء بإلكترون ويخرجه من المعدن فوراً ليتحول إلى تيار كهربائي.",
        "intermediate": "لكي ينبعث إلكترون يجب أن يكون تردد الضوء الساقط مساوياً أو أكبر من تردد العتبة nu_0 الخاص بالفلز. زيادة شدة الضوء تزيد عدد الإلكترونات المنبعثة لكنها لا تزيد طاقتها الحركية؛ طاقة الإلكترون تعتمد فقط على تردد الضوء الساقط.",
        "advanced": "معادلة أينشتاين: h * nu = Phi + KE_max، حيث Phi = h * nu_0 هي دالة شغل الفلز (أقل طاقة تلزم لتحرير الإلكترون دون إكسابه طاقة حركة). طاقة الحركة العظمى KE_max = e * V_0، حيث V_0 هو جهد الإيقاف."
      },
      "equations": [
        {
          "label": "معادلة أينشتاين الكهروضوئية",
          "eq": "hν = Φ + KE_max = hν₀ + e · V₀",
          "symbols": {
            "hν": "طاقة الفوتون الساقط",
            "Φ": "دالة الشغل للفلز",
            "V₀": "جهد الإيقاف"
          }
        }
      ],
      "vocabulary_ids": [
        "vocab-photoelectric-effect",
        "vocab-work-function"
      ],
      "real_world_example": "أبواب المجمعات التجارية التي تفتح تلقائياً عند اقترابك تعمل بخلايا كهروضوئية تحس بانقطاع حزمة الضوء فتعطي أمراً للمحرك بفتح الباب.",
      "tts_text": "فسر أينشتاين انبعاث الإلكترونات الضوئية بأن طاقة فوتون الضوء الساقط تنقسم بين تحرير الإلكترون والتغلب على دالة الشغل، وما يتبقى يتحول لطاقة حركة."
    },
    "exp-phys-u7-nuclear-binding": {
      "title": "طاقة الربط النووية وتكافؤ الكتلة والطاقة",
      "original_text": "كتلة أي نواة متماسكة تكون دائماً أقل من مجموع كتل مكوناتها المفردة وهي حرة. ويتحول هذا النقص في الكتلة (Delta m) إلى طاقة هائلة تربط النيوكلونات ببعضها داخل النواة طبقاً لمعادلة أينشتاين E = Delta m * c^2.",
      "levels": {
        "basic": "النواة تفقد جزءاً صغيراً جداً من وزنها ليتحول إلى غراء طاقة نووية قوي جداً يحفظ البروتونات والنيوترونات متماسكة معاً.",
        "intermediate": "القوة النووية القوية هي أقوى قوة في الكون وتتغلب على التنافر الكهربائي الشديد بين البروتونات الموجبة. لحساب طاقة الربط بوحدة مليون إلكترون فولت: BE = Delta m (بوحدة كتل ذرية amu) * 931.5 MeV.",
        "advanced": "طاقة الربط لكل نيوكلون (BE / A) هي المقياس الحقيقي لمدى استقرار النواة، وتصل إلى قيمتها العظمى (حوالي 8.8 MeV) في أنوية الحديد والنيكل المتوسطة، مما يفسر حدوث الاندماج في الأنوية الخفيفة والانشطار في الأنوية الثقيلة للاقتراب من قمة الاستقرار."
      },
      "equations": [
        {
          "label": "طاقة الربط النووية",
          "eq": "BE = Δm · 931.5  [MeV]",
          "symbols": {
            "BE": "طاقة الربط النووية",
            "Δm": "نقص الكتلة (amu)"
          }
        },
        {
          "label": "نقص الكتلة النووي",
          "eq": "Δm = [ Z · m_p + (A - Z) · m_n ] - M_nucleus",
          "symbols": {
            "Z": "العدد الذري",
            "A": "العدد الكتلي",
            "m_p": "كتلة البروتون",
            "m_n": "كتلة النيوترون"
          }
        }
      ],
      "vocabulary_ids": [
        "vocab-nuclear-binding-energy",
        "vocab-mass-defect"
      ],
      "real_world_example": "الطاقة الهائلة المنبعثة من الشمس والنجوم مصدرها تحول جزء يسير من كتلة ذرات الهيدروجين إلى طاقة ضوئية وحرارية أثناء اندماجها لتكوين الهيليوم.",
      "tts_text": "طاقة الربط النووية ناتجة عن تحول نقص الكتلة بين النواة ومكوناتها المنفردة إلى طاقة متكافئة تحافظ على استقرار النواة وتماسكها."
    }
  },
  "diagrams": {
    "diag-phys-projectiles-3d": {
      "id": "diag-phys-projectiles-3d",
      "title": "محاكي المقذوفات الفيزيائي ثلاثي الأبعاد",
      "type": "canvas_3d_physics",
      "description": "تجربة إطلاق المقذوفات بالمدفع ثلاثي الأبعاد مع التحكم بزاوية الإطلاق والسرعة الابتدائية وملاحظة الارتفاع والمدى والزمن الحقيقي.",
      "parameters": [
        {
          "id": "v0",
          "label": "السرعة الابتدائية v₀ (m/s)",
          "min": 10,
          "max": 100,
          "default": 40,
          "step": 1
        },
        {
          "id": "theta",
          "label": "زاوية الإطلاق θ (درجة)",
          "min": 15,
          "max": 85,
          "default": 45,
          "step": 1
        },
        {
          "id": "g",
          "label": "عجلة الجاذبية g (m/s²)",
          "min": 1.6,
          "max": 15.0,
          "default": 9.8,
          "step": 0.1
        }
      ],
      "readouts": [
        "أقصى ارتفاع H",
        "المدى الأفقي R",
        "زمن التحليق الكلي T"
      ]
    },
    "diag-phys-dynamo-3d": {
      "id": "diag-phys-dynamo-3d",
      "title": "نموذج مولد الدينامو ثلاثي الأبعاد (Three.js)",
      "type": "threejs_interactive",
      "description": "نموذج ثلاثي الأبعاد لمولد التيار المتردد، يدور فيه ملف نحاسي بين قطبي مغناطيس دائم، متصل بحلقتين انزلاقيتين وفرشتين كربونيتين، مع راسم موجة جيبي حي.",
      "parts": [
        {
          "id": "magnet",
          "name": "المغناطيس الدائم (شمالي N وجنوبي S)",
          "desc": "يولد مجالاً مغناطيسياً منتظماً وثابتاً بين القطبين."
        },
        {
          "id": "armature",
          "name": "الملف النحاسي (عضو الإنتاج)",
          "desc": "يدور حول محور عمودي على خطوط المجال فيقطع الفيض المغناطيسي."
        },
        {
          "id": "slip_rings",
          "name": "حلقتا الانزلاق",
          "desc": "تدوران مع الملف لنقل التيار الحثي المتولد."
        },
        {
          "id": "carbon_brushes",
          "name": "الفرشتان الكربونيتان",
          "desc": "تلامسان الحلقتين لنقل التيار إلى الدائرة الخارجية."
        }
      ]
    },
    "diag-phys-rlc-circuit": {
      "id": "diag-phys-rlc-circuit",
      "title": "مختبر دوائر التيار المتردد RLC ورسم متجهات الطور",
      "type": "canvas_circuit",
      "description": "دائرة كهربائية تفاعلية لمقاومة أومية وملف حثي ومكثف مع راسم إشارة لفرق الجهد وزاوية الطور واكتشاف تردد الرنين.",
      "parameters": [
        {
          "id": "R",
          "label": "المقاومة R (Ω)",
          "min": 10,
          "max": 200,
          "default": 50,
          "step": 5
        },
        {
          "id": "L",
          "label": "الحث L (mH)",
          "min": 10,
          "max": 500,
          "default": 100,
          "step": 10
        },
        {
          "id": "C",
          "label": "السعة C (µF)",
          "min": 1,
          "max": 50,
          "default": 10,
          "step": 1
        },
        {
          "id": "f",
          "label": "التردد f (Hz)",
          "min": 20,
          "max": 500,
          "default": 160,
          "step": 5
        }
      ]
    },
    "diag-phys-bohr-atom-3d": {
      "id": "diag-phys-bohr-atom-3d",
      "title": "نموذج بور الذري ثلاثي الأبعاد وقفزات الطاقة",
      "type": "threejs_interactive",
      "description": "ذرة الهيدروجين ثلاثية الأبعاد، تظهر النواة والمدارات الكمية (n=1 إلى n=6). اختر المستوى ليقفز الإلكترون ويصدر فوتوناً بلونه الطيفي الدقيق.",
      "levels": [
        {
          "n": 1,
          "energy": "-13.60 eV",
          "name": "المستوى الأرضي الأول (K)"
        },
        {
          "n": 2,
          "energy": "-3.40 eV",
          "name": "المستوى الثاني (L) - متسلسلة بالمر"
        },
        {
          "n": 3,
          "energy": "-1.51 eV",
          "name": "المستوى الثالث (M) - متسلسلة باشن"
        },
        {
          "n": 4,
          "energy": "-0.85 eV",
          "name": "المستوى الرابع (N)"
        },
        {
          "n": 5,
          "energy": "-0.54 eV",
          "name": "المستوى الخامس (O)"
        }
      ]
    },
    "diag-phys-photoelectric-lab": {
      "id": "diag-phys-photoelectric-lab",
      "title": "معمل الظاهرة الكهروضوئية وتجربة مليكان",
      "type": "canvas_photoelectric",
      "description": "خلية كهروضوئية مفرغة متصلة ببطارية وجلفانومتر حساس. أسقط أشعة ضوئية مختلفة الألوان (أحمر، أخضر، بنفسجي، فوق بنفسجي) ولاحظ انبعاث الإلكترونات وتعيين جهد الإيقاف.",
      "targets": [
        {
          "metal": "السيزيوم (Cs)",
          "work_function": 2.14,
          "color": "#f59e0b"
        },
        {
          "metal": "البوتاسيوم (K)",
          "work_function": 2.3,
          "color": "#3b82f6"
        },
        {
          "metal": "الصوديوم (Na)",
          "work_function": 2.75,
          "color": "#10b981"
        },
        {
          "metal": "الزنك (Zn)",
          "work_function": 4.3,
          "color": "#8b5cf6"
        }
      ]
    }
  },
  "activities": {
    "act-phys-projectiles-angle": {
      "id": "act-phys-projectiles-angle",
      "title": "نشاط استكشافي: تحديد زاوية الإطلاق لأقصى مدى أفقي",
      "target_page": "phys12-p025",
      "learning_goal": "استنتاج أن زاوية 45 درجة تعطي أقصى مدى أفقي وأن الزوايا المتتامة تعطي نفس المدى الأفقي.",
      "steps": [
        {
          "step_num": 1,
          "instruction": "اضبط سرعة القاذف على 30 م/ث واختر زاوية 30 درجة ثم أطلق القذيفة.",
          "action": "fire_30",
          "feedback": "أحسنت! قطعت القذيفة مدى أفقياً مقداره 79.5 متراً."
        },
        {
          "step_num": 2,
          "instruction": "غيّر الزاوية إلى 45 درجة وأطلق المقذوف بنفس السرعة.",
          "action": "fire_45",
          "feedback": "رائع! وصل المدى الأفقي إلى 91.8 متراً (أقصى مدى ممكن)."
        },
        {
          "step_num": 3,
          "instruction": "غيّر الزاوية إلى 60 درجة (متممة الـ 30) ولاحظ موضع السقوط.",
          "action": "fire_60",
          "feedback": "مذهل! سقطت القذيفة عند 79.5 متراً تماماً كزاوية 30 درجة لأن sin(2*30) = sin(2*60)."
        }
      ],
      "conclusion": "المدى الأفقي للمقذوف يصل لذروته عند زاوية 45 درجة، والزاويتان المتتامتان (مجموعهما 90 درجة) تعطيان نفس المدى الأفقي لنفس السرعة الابتدائية."
    },
    "act-phys-dynamo-induction": {
      "id": "act-phys-dynamo-induction",
      "title": "نشاط عملي تفاعلي: مبدأ عمل الدينامو وتغير اتجاه التيار",
      "target_page": "phys12-p033",
      "learning_goal": "استنتاج كيف ينعكس اتجاه التيار الحثي كل نصف دورة عند تبادل أضلاع الملف لمواقعها.",
      "steps": [
        {
          "step_num": 1,
          "instruction": "ابدأ تدوير ملف الدينامو من الوضع العمودي على خطوط المجال (زاوية صفر).",
          "action": "rotate_quarter",
          "feedback": "القوة الدافعة تبدأ من الصفر وتزداد تدريجياً لتبلغ قمتها العظمى عند الوضع الموازي (زاوية 90)."
        },
        {
          "step_num": 2,
          "instruction": "واصل التدوير حتى يكمل الملف نصف دورة كاملة (زاوية 180).",
          "action": "rotate_half",
          "feedback": "تعود القوة الدافعة للصفر مرة أخرى."
        },
        {
          "step_num": 3,
          "instruction": "أكمل الدورة إلى زاوية 270 ثم 360 درجة.",
          "action": "rotate_full",
          "feedback": "انعكس اتجاه التيار في النصف الثاني ووصل لقمته العظمى السالبة، مما يثبت توليد تيار متردد جيبي."
        }
      ],
      "conclusion": "القوة الدافعة المتولدة في الدينامو تتغير جيبياً، وتنعكس قطبيتها كل نصف دورة بسبب دوران أضلاع الملف وقانون اليد اليمنى لفلمنج."
    },
    "act-phys-photoelectric-threshold": {
      "id": "act-phys-photoelectric-threshold",
      "title": "نشاط استكشافي: تعيين تردد العتبة ودالة الشغل لمهبط السيزيوم",
      "target_page": "phys12-p148",
      "learning_goal": "إثبات أن الضوء الأحمر مهما زادت شدته لا يحرر إلكترونات من السيزيوم، بينما الضوء الأزرق يحررها فوراً.",
      "steps": [
        {
          "step_num": 1,
          "instruction": "سلّط ضوءاً أحمر شديداً (طول موجة 700 نانومتر) على مهبط السيزيوم.",
          "action": "shine_red",
          "feedback": "تيار الجلفانومتر صفر! طاقة فوتون الضوء الأحمر أقل من دالة شغل السيزيوم فلا يتحرر أي إلكترون مهما زادت الشدة."
        },
        {
          "step_num": 2,
          "instruction": "غيّر مصدر الضوء إلى ضوء أصفر ثم أخضر.",
          "action": "shine_green",
          "feedback": "بدأت الإلكترونات بالانبعاث ببطء لأن تردد الضوء قارب تردد العتبة."
        },
        {
          "step_num": 3,
          "instruction": "سلّط ضوءاً بنفسجياً (400 نانومتر) أو فوق بنفسجي.",
          "action": "shine_uv",
          "feedback": "انبعاث فوري للإلكترونات وتدفق تيار كهروضوئي كبير وطاقة حركة عظمى عالية!"
        }
      ],
      "conclusion": "انبعاث الإلكترونات الكهروضوئية يعتمد حصراً على تردد الضوء الساقط وليس على شدته، ولا يحدث أي انبعاث إذا كان التردد أقل من تردد العتبة."
    }
  },
  "assessments": {
    "quiz-phys-u1": [
      {
        "id": "q-phys-u1-001",
        "q": "إذا تضاعفت سرعة جسم متحرك كتلته ثابتة إلى الضعف، فإن كمية تحركه:",
        "options": [
          {
            "id": "a",
            "text": "تزداد إلى الضعف"
          },
          {
            "id": "b",
            "text": "تزداد إلى أربعة أمثال",
            "why_wrong": "هذا ينطبق على طاقة الحركة لأنها تتناسب مع مربع السرعة (KE = 0.5mv²)، أما كمية التحرك فتتناسب طردياً مع السرعة فقط (P = mv)."
          },
          {
            "id": "c",
            "text": "تقل إلى النصف",
            "why_wrong": "العلاقة طردية وليست عكسية."
          },
          {
            "id": "d",
            "text": "تظل ثابتة",
            "why_wrong": "تغير السرعة يغير كمية التحرك حتماً."
          }
        ],
        "answer": 0,
        "explain": "حسب القانون P = m · v، تتناسب كمية التحرك طردياً مع السرعة الخطية عند ثبات الكتلة؛ فمضاعفة السرعة تضاعف كمية التحرك إلى الضعف.",
        "page": 10
      },
      {
        "id": "q-phys-u1-002",
        "q": "الزاوية التي تحقق أقصى مدى أفقي لمقذوف أُطلق بنفس السرعة الابتدائية هي:",
        "options": [
          {
            "id": "a",
            "text": "30 درجة",
            "why_wrong": "زاوية 30 درجة تعطي مدى أقل من 45 درجة."
          },
          {
            "id": "b",
            "text": "45 درجة"
          },
          {
            "id": "c",
            "text": "60 درجة",
            "why_wrong": "زاوية 60 درجة تعطي نفس مدى زاوية 30 درجة وهو أقل من مدى 45."
          },
          {
            "id": "d",
            "text": "90 درجة",
            "why_wrong": "الإطلاق بزاوية 90 درجة يجعل المدى الأفقي صفراً لأن المقذوف يصعد رأسياً ويسقط في مكانه."
          }
        ],
        "answer": 1,
        "explain": "المدى الأفقي R = (v₀² · sin 2θ) / g، وقيمة sin(2θ) تصل لقيمتها العظمى (1) عندما يكون 2θ = 90°، أي θ = 45°.",
        "page": 24
      },
      {
        "id": "q-phys-u1-003",
        "q": "سرعة الإفلات من الجاذبية الأرضية لجسم كتلته 100 كجم مقارنة بجسم كتلته 1 كجم:",
        "options": [
          {
            "id": "a",
            "text": "متساوية تماماً وتساوي 11.2 كم/ث"
          },
          {
            "id": "b",
            "text": "أكبر 100 مرة للجسم الثقيل",
            "why_wrong": "سرعة الإفلات لا تعتمد إطلاقاً على كتلة الجسم المقذوف بل على كتلة الكوكب ونصف قطره."
          },
          {
            "id": "c",
            "text": "أقل 100 مرة للجسم الثقيل",
            "why_wrong": "الكتلة لا تدخل في قانون سرعة الإفلات v_esc = √(2GM/R)."
          },
          {
            "id": "d",
            "text": "تعتمد على شكل الجسم فقط",
            "why_wrong": "في الفراغ خارج الغلاف الجوي لا يؤثر شكل الجسم."
          }
        ],
        "answer": 0,
        "explain": "قانون سرعة الإفلات v_esc = √(2GM / R)؛ نلاحظ أن كتلة الجسم المقذوف لا تظهر في المعادلة، فالسرعة ثابتة لجميع الأجسام وتساوي 11.2 كم/ث للأرض.",
        "page": 18
      }
    ],
    "quiz-phys-u2": [
      {
        "id": "q-phys-u2-001",
        "q": "تكون القوة الدافعة الكهربائية الحثية المتولدة في ملف الدينامو مساوية للصفر عندما يكون مستوى الملف:",
        "options": [
          {
            "id": "a",
            "text": "عمودياً على خطوط المجال المغناطيسي"
          },
          {
            "id": "b",
            "text": "موازياً لخطوط المجال المغناطيسي",
            "why_wrong": "في الوضع الموازي تكون القوة الدافعة عظمى (E = E_max) لأن سرعة قطع الخطوط تكون في أقصاها."
          },
          {
            "id": "c",
            "text": "يميل بزاوية 45 درجة",
            "why_wrong": "عند زاوية 45 تكون القيمة = 0.707 من القيمة العظمى."
          },
          {
            "id": "d",
            "text": "يميل بزاوية 60 درجة",
            "why_wrong": "تكون القوة الدافعة مساوية لنصف القيمة العظمى أو أكثر."
          }
        ],
        "answer": 0,
        "explain": "عندما يكون مستوى الملف عمودياً على خطوط المجال، يكون العمودي على مستوى الملف موازياً لخطوط المجال فتكون زاوية الطور θ = 0، ويكون sin(0) = 0، وبالتالي E = 0.",
        "page": 34
      },
      {
        "id": "q-phys-u2-002",
        "q": "في دائرة تيار متردد تحتوي على مكثف نقي فقط، فإن فرق الجهد بين طرفي المكثف:",
        "options": [
          {
            "id": "a",
            "text": "يتأخر عن شدة التيار بزاوية طور 90 درجة (π/2)"
          },
          {
            "id": "b",
            "text": "يتقدم على شدة التيار بزاوية 90 درجة",
            "why_wrong": "تقدم الجهد على التيار يحدث في الملف الحثي وليس المكثف."
          },
          {
            "id": "c",
            "text": "يتفق في الطور تماماً مع شدة التيار",
            "why_wrong": "اتفاق الطور يحدث في المقاومة الأومية الصرفة فقط."
          },
          {
            "id": "d",
            "text": "يتأخر عن التيار بزاوية 180 درجة",
            "why_wrong": "زاوية التأخر في المكثف النقي هي ربع دورة (90 درجة)."
          }
        ],
        "answer": 0,
        "explain": "في المكثف، يجب أن تتدفق الشحنات أولاً (يمر التيار) ليتراكم الجهد تدريجياً بين اللوحين، لذلك يتأخر فرق الجهد عن التيار بزاوية 90 درجة.",
        "page": 42
      },
      {
        "id": "q-phys-u2-003",
        "q": "إذا تضاعف تردد التيار المار في ملف حثي نقي إلى الضعف، فإن مفاعلته الحثية:",
        "options": [
          {
            "id": "a",
            "text": "تتضاعف إلى الضعف"
          },
          {
            "id": "b",
            "text": "تقل إلى النصف",
            "why_wrong": "العلاقة بين التردد والمفاعلة الحثية طردية وليست عكسية (X_L = 2πfL)."
          },
          {
            "id": "c",
            "text": "تزداد إلى أربعة أمثال",
            "why_wrong": "المفاعلة لا تعتمد على مربع التردد بل على التردد مباشرة."
          },
          {
            "id": "d",
            "text": "تظل ثابتة دون تغيير",
            "why_wrong": "المفاعلة تتغير طردياً مع تغير التردد."
          }
        ],
        "answer": 0,
        "explain": "حسب القانون X_L = 2π · f · L، تتناسب المفاعلة الحثية طردياً مع التردد؛ فمضاعفة التردد يضاعف المفاعلة الحثية للملف للضعف.",
        "page": 46
      }
    ],
    "quiz-phys-u6": [
      {
        "id": "q-phys-u6-001",
        "q": "العامل الذي يحدد الطاقة الحركية العظمى للإلكترونات الضوئية المنبعثة في الظاهرة الكهروضوئية هو:",
        "options": [
          {
            "id": "a",
            "text": "تردد الضوء الساقط"
          },
          {
            "id": "b",
            "text": "شدة الضوء الساقط",
            "why_wrong": "زيادة شدة الضوء تزيد عدد الإلكترونات المنبعثة (شدة التيار) ولا تؤثر مطلقاً على طاقة حركة الإلكترون الواحد."
          },
          {
            "id": "c",
            "text": "مساحة سطح الفلز",
            "why_wrong": "المساحة تزيد عدد الفوتونات الساقطة ولا تغير طاقة الفوتون الفردي."
          },
          {
            "id": "d",
            "text": "زمن تسليط الضوء",
            "why_wrong": "الانبعاث الكهروضوئي لحظي يتم خلال أقل من جزء من بليون من الثانية."
          }
        ],
        "answer": 0,
        "explain": "حسب معادلة أينشتاين KE_max = hν - Φ، تعتمد الطاقة الحركية العظمى فقط على تردد الضوء الساقط (ν) ونوع مادة الفلز (دالة الشغل Φ).",
        "page": 152
      }
    ]
  },
  "glossary": {
    "vocab-linear-momentum": {
      "id": "vocab-linear-momentum",
      "term": "كمية التحرك الخطي (Linear Momentum)",
      "definition": "كمية فيزيائية متجهة تساوي حاصل ضرب كتلة الجسم في سرعته المتجهة (P = m·v)، وتقاس بوحدة kg·m/s.",
      "example": "اندفاع قذيفة المدفع للأمام مصحوب بارتداد المدفع للخلف بحفظ كمية التحرك.",
      "category": "ميكانيكا المقذوفات"
    },
    "vocab-escape-velocity": {
      "id": "vocab-escape-velocity",
      "term": "سرعة الإفلات (Escape Velocity)",
      "definition": "أقل سرعة ابتدائية ينطلق بها جسم للتغلب التام على حقل جاذبية الكوكب والوصول إلى اللانهاية دون الحاجة لدفع إضافي.",
      "example": "سرعة الإفلات للأرض تساوي 11.2 كم/ث، بينما للقمر 2.4 كم/ث لقلة كتلته.",
      "category": "ميكانيكا الفضاء"
    },
    "vocab-ac-dynamo": {
      "id": "vocab-ac-dynamo",
      "term": "مولد التيار المتردد (AC Generator / Dynamo)",
      "definition": "جهاز كهروميكانيكي يحول الطاقة الحركية الدورانية إلى طاقة كهربائية متغيرة القيمة والاتجاه بالحث الكهرومغناطيسي.",
      "example": "دينامو الدراجة الهوائية الذي يضيء المصباح أثناء تدوير العجلات.",
      "category": "كهرومغناطيسية"
    },
    "vocab-electrical-resonance": {
      "id": "vocab-electrical-resonance",
      "term": "الرنين الكهربائي (Electrical Resonance)",
      "definition": "حالة في دائرة التيار المتردد RLC تتساوى فيها المفاعلة الحثية للملف مع المفاعلة السعوية للمكثف، فتكون المعاوقة أقل ما يمكن والتيار في قيمته العظمى.",
      "example": "دائرة اختيار وتوليف المحطات في أجهزة الراديو والاتصالات.",
      "category": "دوائر التيار المتردد"
    },
    "vocab-pn-junction": {
      "id": "vocab-pn-junction",
      "term": "الوصلة الثنائية (الدايود - PN Junction)",
      "definition": "عنصر إلكتروني شبه موصل يتكون من بلورة موجبة ملتصقة ببلورة سالبة، يسمح بمرور التيار الكهربائي في اتجاه واحد فقط.",
      "example": "دايودات تقويم التيار في شواحن الهواتف ومصابيح LED الموفرة للطاقة.",
      "category": "إلكترونيات"
    },
    "vocab-photoelectric-effect": {
      "id": "vocab-photoelectric-effect",
      "term": "الظاهرة الكهروضوئية (Photoelectric Effect)",
      "definition": "ظاهرة انبعاث إلكترونات من سطوح الفلزات عند سقوط فوتونات ضوئية ذات تردد أعلى من تردد العتبة للفلز.",
      "example": "الخلايا الشمسية التي تولد كهرباء المنازل من ضوء الشمس الساقط.",
      "category": "فيزياء حديثة وكمية"
    },
    "vocab-nuclear-binding-energy": {
      "id": "vocab-nuclear-binding-energy",
      "term": "طاقة الربط النووية (Nuclear Binding Energy)",
      "definition": "الطاقة اللازمة لتفكيك نواة الذرة كلياً إلى مكوناتها المفردة من بروتونات ونيوترونات، وتنتج عن تحول نقص الكتلة إلى طاقة.",
      "example": "الطاقة الناتجة في المفاعلات النووية والقنابل الذرية والشمس.",
      "category": "فيزياء نووية"
    }
  }
};
