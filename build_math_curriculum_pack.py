#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator for the Grade 12 Math interactive curriculum pack."""
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "curriculum", "grade12", "math")
ANDROID_DATA_DIR = os.path.join(BASE_DIR, "thaker-android-src", "assets", "data", "curriculum", "grade12", "math")

MANIFEST = {
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
        "original_page_rendering": True,
        "interactive_overlays": True,
        "smart_text_bottom_sheet": True,
        "explanation_levels_count": 3,
        "interactive_step_by_step_equations": True,
        "interactive_3d_geometry_lab": True,
        "simulated_activities": True,
        "remediation_mistake_review": True,
        "offline_audio_synthesis": True,
        "yemeni_companion_prompts": True,
        "multi_student_profiles": True
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
}

UNITS = [
    {
        "id": "u1", "order": 1, "title": "الوحدة الأولى: الأعداد المركبة",
        "short_desc": "مفهوم العدد المركب، تمثيله في مستوى أرغاند، القيمة المطلقة والزاوية، والصيغة القطبية",
        "page_start": 7, "page_end": 44, "pdf_start": 9, "pdf_end": 46,
        "workbook_start": 6, "workbook_end": 17,
        "key_laws": ["z = a + bi، i² = −1", "|z| = √(a² + b²)", "z = r(cos θ + i sin θ)"],
        "real_world_apps": ["التيار المتردد والهندسة الكهربائية", "الإشارات والدوائر الإلكترونية", "تحويل الإحداثيات في المستوى"]
    },
    {
        "id": "u2", "order": 2, "title": "الوحدة الثانية: مبرهنة دي موافر والتوسعة ذات الحدين",
        "short_desc": "مبرهنة دي موافر، الجذور النونية للعدد المركب، والتوسعة ذات الحدين وتطبيقاتها",
        "page_start": 45, "page_end": 73, "pdf_start": 47, "pdf_end": 75,
        "workbook_start": 18, "workbook_end": 30,
        "key_laws": ["[r(cos θ + i sin θ)]ⁿ = rⁿ(cos nθ + i sin nθ)", "zⁿ = rⁿ(cos nθ + i sin nθ)", "(a + b)ⁿ = Σ C(n,k)aⁿ⁻ᵏbᵏ"],
        "real_world_apps": ["حساب القوى للإشارات الدورية", "توزيع الاحتمالات ذو الحدين", "النماذج الهندسية الدوارة"]
    },
    {
        "id": "u3", "order": 3, "title": "الوحدة الثالثة: القطوع المخروطية",
        "short_desc": "القطع الناقص والقطع الزائد والقطع المكافئ ومعادلاتها القياسية وخصائصها",
        "page_start": 104, "page_end": 132, "pdf_start": 106, "pdf_end": 134,
        "workbook_start": 31, "workbook_end": 36,
        "key_laws": ["القطع الناقص: x²/a² + y²/b² = 1", "القطع الزائد: x²/a² − y²/b² = 1", "القطع المكافئ: y² = 4px"],
        "real_world_apps": ["أقمار الاتصالات ومدارات الكواكب", "أطباق التلسكوبات والهوائيات", "تصميم الجسور والأنفاق"]
    },
    {
        "id": "u4", "order": 4, "title": "الوحدة الرابعة: الهندسة في فضاء ثلاثي الأبعاد",
        "short_desc": "المستقيمات والمستويات، المسافات، والزوايا في الفراغ ثلاثي الأبعاد",
        "page_start": 133, "page_end": 153, "pdf_start": 135, "pdf_end": 155,
        "workbook_start": 37, "workbook_end": 44,
        "key_laws": ["مسافة نقطة من مستوى: |Ax₀ + By₀ + Cz₀ + D| / √(A²+B²+C²)", "cos φ = |n₁·n₂| / (|n₁||n₂|)", "طول القطر الفراغي لمكعب: d = a√3"],
        "real_world_apps": ["تحديد اتجاه الطائرات والسفن", "هندسة المباني والرافعات", "نمذجة الكاميرات والرسوم ثلاثية الأبعاد"]
    },
    {
        "id": "u5", "order": 5, "title": "الوحدة الخامسة: الاحتمالات",
        "short_desc": "التجارب العشوائية، قواعد الجمع والضرب، الاحتمال الشرطي، والتوزيع ذو الحدين",
        "page_start": 74, "page_end": 103, "pdf_start": 76, "pdf_end": 105,
        "workbook_start": 45, "workbook_end": 52,
        "key_laws": ["P(A∪B) = P(A) + P(B) − P(A∩B)", "P(A|B) = P(A∩B) / P(B)", "P(X=k) = C(n,k)pᵏ(1−p)ⁿ⁻ᵏ"],
        "real_world_apps": ["تقييم المخاطر في التأمين", "تحليل نتائج التجارب والاستطلاعات", "نمذجة جودة التصنيع"]
    },
    {
        "id": "u6", "order": 6, "title": "الوحدة السادسة: المشتقات",
        "short_desc": "مفهوم المشتقة، قواعد الاشتقاق، مشتقة الدوال المركبة، القيم القصوى ونظرية القيمة المتوسطة",
        "page_start": 154, "page_end": 209, "pdf_start": 156, "pdf_end": 211,
        "workbook_start": 53, "workbook_end": 67,
        "key_laws": ["f′(x) = limₕ→₀ [f(x+h) − f(x)] / h", "(xⁿ)′ = nxⁿ⁻¹", "(f∘g)′(x) = f′(g(x))g′(x)"],
        "real_world_apps": ["السرعة والتسارع في الفيزياء", "تحسين الربح والتكلفة في الاقتصاد", "ميول المنحنيات في التصميم"]
    },
    {
        "id": "u7", "order": 7, "title": "الوحدة السابعة: التكامل",
        "short_desc": "التكامل غير المحدد والمحدد، طرق التكامل، المساحات، وحجوم الدوران",
        "page_start": 210, "page_end": 256, "pdf_start": 212, "pdf_end": 258,
        "workbook_start": 68, "workbook_end": 80,
        "key_laws": ["∫xⁿdx = xⁿ⁺¹/(n+1) + C، n ≠ −1", "∫ₐᵇ f(x)dx = F(b) − F(a)", "V = π∫ₐᵇ [f(x)]²dx"],
        "real_world_apps": ["حساب المساحات غير المنتظمة", "حجوم الخزانات والأوعية الدوارة", "الشغل والطاقة في الفيزياء"]
    }
]

ANCHORS = [
    {"id": "math-u1-l1", "unitId": "u1", "order": 1, "title": "مفهوم العدد المركب والوحدة التخيلية", "pages": [7, 11], "formula": "i² = −1، z = a + bi", "summary": "العدد المركب يوسّع مجموعة الأعداد الحقيقية بإضافة الوحدة التخيلية i.", "insight": "يمثل z نقطة (a، b) في مستوى أرغاند.", "diagram_ref": "diag-math-complex", "activity_ref": "act-math-complex-add", "solution_ref": "sol-math-complex-add"},
    {"id": "math-u1-l2", "unitId": "u1", "order": 2, "title": "العمليات على الأعداد المركبة", "pages": [12, 15], "formula": "(a+bi)+(c+di)=(a+c)+(b+d)i", "summary": "تُجرى العمليات على الأعداد المركبة بمعاملة i كمتغير مع i² = −1.", "insight": "الجمع والطرح مكوّن ب مكوّن، والضرب يستخدم i².", "diagram_ref": "diag-math-complex", "activity_ref": "act-math-complex-add", "solution_ref": "sol-math-complex-add"},
    {"id": "math-u1-l3", "unitId": "u1", "order": 3, "title": "التمثيل الهندسي والقيمة المطلقة", "pages": [16, 22], "formula": "|z| = √(a² + b²)", "summary": "القيمة المطلقة للعدد المركب هي طول متجهه من مبدأ الإحداثيات.", "insight": "المسافة بين عددين مركبين هي |z₁ − z₂|.", "diagram_ref": "diag-math-complex", "activity_ref": "act-math-complex-modulus", "solution_ref": "sol-math-complex-modulus"},
    {"id": "math-u1-l4", "unitId": "u1", "order": 4, "title": "سعة العدد المركب وزاويته", "pages": [23, 32], "formula": "θ = tan⁻¹(b/a)", "summary": "تحدد السعة اتجاه متجه العدد المركب في المستوى.", "insight": "يجب مراعاة الربع الذي تقع فيه النقطة عند حساب θ.", "diagram_ref": "diag-math-complex", "activity_ref": "act-math-complex-modulus", "solution_ref": "sol-math-complex-modulus"},
    {"id": "math-u1-l5", "unitId": "u1", "order": 5, "title": "الصيغة القطبية للعدد المركب", "pages": [33, 39], "formula": "z = r(cos θ + i sin θ)", "summary": "تكتب الصيغة القطبية العدد المركب باستخدام الطول r والزاوية θ.", "insight": "الصيغة القطبية تبسّط الضرب والقسمة والرفع إلى قوة.", "diagram_ref": "diag-math-complex", "activity_ref": "act-math-polar", "solution_ref": "sol-math-polar"},
    {"id": "math-u1-l6", "unitId": "u1", "order": 6, "title": "التحويل بين الصيغتين الجبرية والقطبية", "pages": [40, 44], "formula": "a = r cos θ، b = r sin θ", "summary": "نحول من الجبرية للقطبية بحساب r وθ، وبالعكس بالإسقاطات.", "insight": "التمثيل الهندسي يفسر لماذا يتضاعف الطول ويُجمع θ عند الضرب.", "diagram_ref": "diag-math-complex", "activity_ref": "act-math-polar", "solution_ref": "sol-math-polar"},
    {"id": "math-u2-l1", "unitId": "u2", "order": 1, "title": "مبرهنة دي موافر", "pages": [45, 48], "formula": "(cos θ + i sin θ)ⁿ = cos nθ + i sin nθ", "summary": "تسمح المبرهنة برفع عدد مركب ذي قيمة مطلقة 1 إلى قوة n بسهولة.", "insight": "الصيغة العامة: zⁿ = rⁿ(cos nθ + i sin nθ).", "diagram_ref": "diag-math-complex", "activity_ref": "act-math-demoivre", "solution_ref": "sol-math-demoivre"},
    {"id": "math-u2-l2", "unitId": "u2", "order": 2, "title": "الجذور النونية للعدد المركب", "pages": [49, 54], "formula": "wₖ = r^(1/n)[cos((θ+2kπ)/n) + i sin((θ+2kπ)/n)]", "summary": "للعدد المركب n جذور نونية موزعة بالتساوي على دائرة نصف قطرها r^(1/n).", "insight": "الفرق بين زواوي جذرين متجاورين هو 2π/n.", "diagram_ref": "diag-math-complex", "activity_ref": "act-math-roots", "solution_ref": "sol-math-demoivre"},
    {"id": "math-u2-l3", "unitId": "u2", "order": 3, "title": "التوسعة ذات الحدين", "pages": [55, 64], "formula": "(a+b)ⁿ = Σ C(n,k)aⁿ⁻ᵏbᵏ", "summary": "معاملات التوسعة هي معاملات مثلث باسكال أو C(n,k).", "insight": "عدد الحدود في التوسعة هو n + 1.", "diagram_ref": "diag-math-complex", "activity_ref": "act-math-binomial", "solution_ref": "sol-math-binomial"},
    {"id": "math-u2-l4", "unitId": "u2", "order": 4, "title": "تطبيقات دي موافر والتوسعة", "pages": [65, 73], "formula": "cos nθ + i sin nθ = (cos θ + i sin θ)ⁿ", "summary": "تستخدم المبرهنة لإيجاد علاقات مثلية وتبسيط قوى الأعداد المركبة.", "insight": "ربط الجزء الحقيقي والجزء التخيلي يعطي متطابقات جيبية.", "diagram_ref": "diag-math-complex", "activity_ref": "act-math-demoivre", "solution_ref": "sol-math-demoivre"},
    {"id": "math-u3-l1", "unitId": "u3", "order": 1, "title": "التعريف العام للقطع المخروطي", "pages": [104, 109], "formula": "e = PF / PD", "summary": "القطع المخروطي مجموعة نقاط تتغير نسبة بعدها عن بؤرة إلى بعدها عن دليل ثابتاً.", "insight": "نوع القطع يحدد في e: ناقص e<1، مكافئ e=1، زائد e>1.", "diagram_ref": "diag-math-cone", "activity_ref": "act-math-cone", "solution_ref": "sol-math-ellipse"},
    {"id": "math-u3-l2", "unitId": "u3", "order": 2, "title": "القطع الناقص", "pages": [110, 117], "formula": "x²/a² + y²/b² = 1", "summary": "القطع الناقص مجموعة نقاط مجموع بعديها عن بؤرتين ثابتاً.", "insight": "مجموع البعدين = 2a، والبؤرتان على المحور الكبير.", "diagram_ref": "diag-math-ellipse", "activity_ref": "act-math-ellipse", "solution_ref": "sol-math-ellipse"},
    {"id": "math-u3-l3", "unitId": "u3", "order": 3, "title": "القطع الزائد", "pages": [118, 123], "formula": "x²/a² − y²/b² = 1", "summary": "القطع الزائد مجموعة نقاط الفرق المطلق لبعديها عن بؤرتين ثابتاً.", "insight": "الفرق المطلق = 2a، وله خطان مقاربان.", "diagram_ref": "diag-math-hyperbola", "activity_ref": "act-math-hyperbola", "solution_ref": "sol-math-hyperbola"},
    {"id": "math-u3-l4", "unitId": "u3", "order": 4, "title": "القطع المكافئ", "pages": [124, 129], "formula": "y² = 4px", "summary": "القطع المكافئ مجموعة نقاط متساوية البعد عن بؤرة ودليل.", "insight": "محور التماثل هو محور x، والبؤرة (p، 0).", "diagram_ref": "diag-math-parabola", "activity_ref": "act-math-parabola", "solution_ref": "sol-math-parabola"},
    {"id": "math-u3-l5", "unitId": "u3", "order": 5, "title": "تطبيقات القطوع المخروطية", "pages": [130, 132], "formula": "e = c/a", "summary": "تستخدم القطوع في المدارات والهوائيات والأنفاق.", "insight": "اختيار القطع المناسب يعتمد على قيمة الانحراف e.", "diagram_ref": "diag-math-cone", "activity_ref": "act-math-cone", "solution_ref": "sol-math-parabola"},
    {"id": "math-u4-l1", "unitId": "u4", "order": 1, "title": "المستقيم والمستوى في الفراغ", "pages": [133, 141], "formula": "Ax + By + Cz + D = 0", "summary": "يُمثّل المستوى في الفراغ بمعادلة خطية ويُمثّل المستقيم بمتجه اتجاه.", "insight": "المتجه الطبيعي للمستوى هو (A، B، C).", "diagram_ref": "diag-math-space", "activity_ref": "act-math-space-diagonal", "solution_ref": "sol-math-space-diagonal"},
    {"id": "math-u4-l2", "unitId": "u4", "order": 2, "title": "الزاوية بين مستقيم ومستوى", "pages": [142, 146], "formula": "sin θ = |u·n| / (|u||n|)", "summary": "تقاس الزاوية بين مستقيم ومستوى باستخدام متجه الاتجاه والمتجه الطبيعي.", "insight": "الزاوية بين المستقيم والمتجه الطبيعي مكمّلة للزاوية المطلوبة.", "diagram_ref": "diag-math-line-plane", "activity_ref": "act-math-line-plane", "solution_ref": "sol-math-line-plane"},
    {"id": "math-u4-l3", "unitId": "u4", "order": 3, "title": "الزاوية بين مستويين والمسافة في الفراغ", "pages": [147, 153], "formula": "cos φ = |n₁·n₂| / (|n₁||n₂|)", "summary": "توجد الزاوية بين مستويين من زاوية متجهيهما الطبيعيين.", "insight": "مسافة نقطة من مستوى تقاس بالإسقاط العمودي.", "diagram_ref": "diag-math-dihedral", "activity_ref": "act-math-dihedral", "solution_ref": "sol-math-dihedral"},
    {"id": "math-u5-l1", "unitId": "u5", "order": 1, "title": "التجارب العشوائية والاحتمال", "pages": [74, 78], "formula": "0 ≤ P(A) ≤ 1", "summary": "الاحتمال مقياس لحدوث حدث داخل فضاء عيني من نتجات متساوية الاحتمال غالباً.", "insight": "مجموع احتمالات كل النتجات الممكنة المتنافية = 1.", "diagram_ref": "diag-math-probability", "activity_ref": "act-math-prob-union", "solution_ref": "sol-math-prob-union"},
    {"id": "math-u5-l2", "unitId": "u5", "order": 2, "title": "قاعدتا الجمع والضرب", "pages": [79, 85], "formula": "P(A∪B)=P(A)+P(B)−P(A∩B)", "summary": "تُستخدم قاعدة الجمع للأحداث وقاعدة الضرب للأحداث المستقلة أو الشرطية.", "insight": "إذا كان الحدثان متنافيين فإن P(A∩B)=0.", "diagram_ref": "diag-math-probability", "activity_ref": "act-math-prob-union", "solution_ref": "sol-math-prob-union"},
    {"id": "math-u5-l3", "unitId": "u5", "order": 3, "title": "الاحتمال الشرطي والاستقلال", "pages": [86, 92], "formula": "P(A|B)=P(A∩B)/P(B)، P(B)>0", "summary": "الاحتمال الشرطي يضيّق فضاء العينة إلى الحدث B.", "insight": "الاستقلال يعني P(A|B)=P(A).", "diagram_ref": "diag-math-probability", "activity_ref": "act-math-prob-conditional", "solution_ref": "sol-math-prob-conditional"},
    {"id": "math-u5-l4", "unitId": "u5", "order": 4, "title": "الاحتمال ذو الحدين", "pages": [93, 97], "formula": "P(X=k)=C(n,k)pᵏ(1−p)ⁿ⁻ᵏ", "summary": "نموذج برنولي يتكرر n مرة بنجاح احتماله p في كل مرة.", "insight": "مجموع الاحتمالات لكل k من 0 إلى n يساوي 1.", "diagram_ref": "diag-math-probability", "activity_ref": "act-math-prob-binomial", "solution_ref": "sol-math-prob-binomial"},
    {"id": "math-u5-l5", "unitId": "u5", "order": 5, "title": "تطبيقات الاحتمالات", "pages": [98, 103], "formula": "P(Aᶜ)=1−P(A)", "summary": "تطبيق القواعد على مسائل القرعة والجودة والاختبارات.", "insight": "غالباً أسهل حساب احتمال المكمّل ثم طرحه من 1.", "diagram_ref": "diag-math-probability", "activity_ref": "act-math-prob-binomial", "solution_ref": "sol-math-prob-union"},
    {"id": "math-u6-l1", "unitId": "u6", "order": 1, "title": "مفهوم المشتقة وميل المماس", "pages": [154, 159], "formula": "f′(x)=limₕ→₀[f(x+h)−f(x)]/h", "summary": "المشتقة هي معدل التغير اللحظي وميل المماس للمنحنى.", "insight": "وجود النهاية يعني قابلية الدالة للاشتقاق عند النقطة.", "diagram_ref": "diag-math-derivative", "activity_ref": "act-math-power-rule", "solution_ref": "sol-math-power"},
    {"id": "math-u6-l2", "unitId": "u6", "order": 2, "title": "قواعد الاشتقاق الأساسية", "pages": [160, 165], "formula": "(xⁿ)′=nxⁿ⁻¹، (uv)′=u′v+uv′", "summary": "تُشتق الدوال الجبرية بقواعد القوة والجداء والقسمة والمجموع.", "insight": "مشتقة الثابت صفر ومشتقة kx هي k.", "diagram_ref": "diag-math-derivative", "activity_ref": "act-math-product-rule", "solution_ref": "sol-math-power"},
    {"id": "math-u6-l3", "unitId": "u6", "order": 3, "title": "مشتقة الدالة المركبة", "pages": [166, 170], "formula": "(f∘g)′(x)=f′(g(x))g′(x)", "summary": "تُشتق الدالة المركبة من الخارج إلى الداخل مع الضرب بمشتقة الداخل.", "insight": "تسمى أيضاً قاعدة السلسلة.", "diagram_ref": "diag-math-derivative", "activity_ref": "act-math-chain-rule", "solution_ref": "sol-math-chain"},
    {"id": "math-u6-l4", "unitId": "u6", "order": 4, "title": "اشتقاق الدوال الجبرية", "pages": [171, 174], "formula": "(√x)′=1/(2√x)، (1/x)′=−1/x²", "summary": "تكتب الدوال الجبرية بصورة قوى ثم تطبق قاعدة القوة.", "insight": "التحويل إلى صورة xⁿ يوحّد معالجة الجذور والمقامات.", "diagram_ref": "diag-math-derivative", "activity_ref": "act-math-power-rule", "solution_ref": "sol-math-power"},
    {"id": "math-u6-l5", "unitId": "u6", "order": 5, "title": "التطبيقات الهندسية للمشتقة", "pages": [175, 182], "formula": "y−y₀=f′(x₀)(x−x₀)", "summary": "تستخدم المشتقة لإيجاد مماس ومنحنى وحل مسائل الحركة.", "insight": "السرعة هي مشتقة الموضع بالنسبة للزمن.", "diagram_ref": "diag-math-derivative", "activity_ref": "act-math-chain-rule", "solution_ref": "sol-math-chain"},
    {"id": "math-u6-l6", "unitId": "u6", "order": 6, "title": "المشتقات الأعلى", "pages": [183, 186], "formula": "f″(x)=(f′(x))′", "summary": "المشتقة الثانية تصف تغير المشتقة الأولى وتساعد في التقرير.", "insight": "f″>0 يعني تقعراً للأعلى و f″<0 يعني تحدباً.", "diagram_ref": "diag-math-derivative", "activity_ref": "act-math-product-rule", "solution_ref": "sol-math-power"},
    {"id": "math-u6-l7", "unitId": "u6", "order": 7, "title": "القيم القصوى والتقرير", "pages": [187, 199], "formula": "f′(c)=0 شرط لازم للقيمة القصوى الداخلية", "summary": "توجد النقاط الحرجة ثم يحدد نوعها باختبار المشتقة الأولى أو الثانية.", "insight": "يجب فحص طرفي الفترة في مسائل القيم القصوى المغلقة.", "diagram_ref": "diag-math-derivative", "activity_ref": "act-math-extrema", "solution_ref": "sol-math-extrema"},
    {"id": "math-u6-l8", "unitId": "u6", "order": 8, "title": "نظريتا رول والقيمة المتوسطة", "pages": [200, 209], "formula": "f′(c)=[f(b)−f(a)]/(b−a)", "summary": "تضمن نظرية القيمة المتوسطة وجود نقطة ميلها يساوي ميل القطرة.", "insight": "رول حالة خاصة عندما f(a)=f(b).", "diagram_ref": "diag-math-derivative", "activity_ref": "act-math-mvt", "solution_ref": "sol-math-mvt"},
    {"id": "math-u7-l1", "unitId": "u7", "order": 1, "title": "التكامل غير المحدد", "pages": [210, 221], "formula": "∫xⁿdx=xⁿ⁺¹/(n+1)+C، n≠−1", "summary": "التكامل غير المحدد يعكس الاشتقاق ويُنتج عائلة دوال.", "insight": "ثابت التكامل C يختفي عند الاشتقاق.", "diagram_ref": "diag-math-integral", "activity_ref": "act-math-indefinite", "solution_ref": "sol-math-indefinite"},
    {"id": "math-u7-l2", "unitId": "u7", "order": 2, "title": "طرق التكامل", "pages": [222, 234], "formula": "∫(u±v)dx=∫udx±∫vdx", "summary": "تستخدم خطية التكامل والتعويض لتبسيط المسائل.", "insight": "التعويض يختار عادة دالة داخلية مشتقتها موجودة في التكامل.", "diagram_ref": "diag-math-integral", "activity_ref": "act-math-indefinite", "solution_ref": "sol-math-indefinite"},
    {"id": "math-u7-l3", "unitId": "u7", "order": 3, "title": "التكامل المحدد", "pages": [235, 239], "formula": "∫ₐᵇf(x)dx=F(b)−F(a)", "summary": "التكامل المحدد يعطي قيمة عددية باستخدام مبدأ Newton-Leibniz.", "insight": "لا يحتاج ثابت التكامل لأنه يُلغى عند الطرح.", "diagram_ref": "diag-math-integral", "activity_ref": "act-math-definite", "solution_ref": "sol-math-definite"},
    {"id": "math-u7-l4", "unitId": "u7", "order": 4, "title": "خصائص التكامل المحدد", "pages": [240, 243], "formula": "∫ₐᵇf(x)dx=−∫ᵇₐf(x)dx", "summary": "من خصائصها الجمعية وتبديل الحدود وتماثل الدوال.", "insight": "تكامل دالة فردية على فترة متماثلة حول الصفر يساوي صفراً.", "diagram_ref": "diag-math-integral", "activity_ref": "act-math-definite", "solution_ref": "sol-math-definite"},
    {"id": "math-u7-l5", "unitId": "u7", "order": 5, "title": "المساحة تحت المنحنى", "pages": [244, 247], "formula": "A=∫ₐᵇ|f(x)|dx", "summary": "المساحة المحصورة بين المنحنى ومحور x تُقاس بالتكامل المحدد.", "insight": "إذا كان المنحنى سالباً نأخذ القيمة المطلقة أو نعكس الإشارة.", "diagram_ref": "diag-math-area", "activity_ref": "act-math-area", "solution_ref": "sol-math-area"},
    {"id": "math-u7-l6", "unitId": "u7", "order": 6, "title": "حجم مجسم الدوران", "pages": [248, 251], "formula": "V=π∫ₐᵇ[f(x)]²dx", "summary": "يدور المنحنى حول محور x فينتج مجسم يمكن حساب حجمه بالأقراص.", "insight": "كل قرص نصف قطره f(x) وسمكه dx.", "diagram_ref": "diag-math-revolution", "activity_ref": "act-math-revolution", "solution_ref": "sol-math-revolution"},
    {"id": "math-u7-l7", "unitId": "u7", "order": 7, "title": "تطبيقات التكامل", "pages": [252, 256], "formula": "W=∫ₐᵇF(x)dx", "summary": "يستخدم التكامل في حساب المساحات والحجوم والشغل.", "insight": "الربط بين المشتقة والتكامل هو جوهر التحليل."}
]
DIAGRAMS = {
    "diag-math-complex": {"id": "diag-math-complex", "lab_exp": "lab-math-complex", "title": "مستوى أرغاند والعدد المركب", "sim_key": "math_complex", "formula": "z = a + bi، |z| = √(a²+b²)", "slider_label": "زاوية العدد المركب:", "slider_min": 0, "slider_max": 360, "slider_val": 45, "slider_unit": "°", "components": [{"id": "real", "name": "المحور الحقيقي", "role": "يمثل الجزء الحقيقي a."}, {"id": "imag", "name": "المحور التخيلي", "role": "يمثل الجزء التخيلي b."}, {"id": "point", "name": "النقطة z", "role": "تتحرك بدلالة الزاوية، وطولها هو القيمة المطلقة."}]},
    "diag-math-cone": {"id": "diag-math-cone", "lab_exp": "lab-math-cone", "title": "القطوع الناتجة من قطع المخروط", "sim_key": "math_cone_sections", "formula": "e = PF / PD", "slider_label": "ميل مستوى القطع:", "slider_min": 0, "slider_max": 90, "slider_val": 35, "slider_unit": "°", "components": [{"id": "cone", "name": "المخروط", "role": "السطح الذي يُقطع بمستوى."}, {"id": "plane", "name": "مستوى القطع", "role": "ميله يحدد نوع القطع."}, {"id": "curve", "name": "منحنى القطع", "role": "ناقص أو مكافئ أو زائد حسب زاوية المستوى."}]},
    "diag-math-ellipse": {"id": "diag-math-ellipse", "lab_exp": "lab-math-ellipse", "title": "القطع الناقص وبؤرتاه", "sim_key": "math_ellipse", "formula": "x²/a² + y²/b² = 1", "slider_label": "الانحراف e:", "slider_min": 10, "slider_max": 90, "slider_val": 55, "slider_unit": "%", "components": [{"id": "f1", "name": "البؤرة الأولى", "role": "أحد نقطتي تعريف القطع الناقص."}, {"id": "f2", "name": "البؤرة الثانية", "role": "مجموع البعدين عن البؤرتين يساوي 2a."}, {"id": "curve", "name": "المنحنى", "role": "يصبح دائرة عندما يقترب الانحراف من الصفر."}]},
    "diag-math-hyperbola": {"id": "diag-math-hyperbola", "lab_exp": "lab-math-hyperbola", "title": "القطع الزائد وخطاه المقاربان", "sim_key": "math_hyperbola", "formula": "x²/a² − y²/b² = 1", "slider_label": "المعلمة a:", "slider_min": 1, "slider_max": 5, "slider_val": 2, "slider_unit": "", "components": [{"id": "branches", "name": "الفرعان", "role": "ينفصلان على جانبي المحورين."}, {"id": "asymptote", "name": "الخطان المقاربان", "role": "يقترب منهما المنحنى دون أن يلمسهما."}]},
    "diag-math-parabola": {"id": "diag-math-parabola", "lab_exp": "lab-math-parabola", "title": "القطع المكافئ والبؤرة والدليل", "sim_key": "math_parabola", "formula": "y² = 4px", "slider_label": "المعلمة p:", "slider_min": 1, "slider_max": 6, "slider_val": 3, "slider_unit": "", "components": [{"id": "focus", "name": "البؤرة", "role": "النقطة (p، 0)."}, {"id": "directrix", "name": "الدليل", "role": "المستقيم x = −p."}, {"id": "curve", "name": "المنحنى", "role": "كل نقطة عليه متساوية البعد عن البؤرة والدليل."}]},
    "diag-math-space": {"id": "diag-math-space", "lab_exp": "lab-math-space", "title": "القطر الفراغي للمكعب", "sim_key": "math_3d_pythagoras", "formula": "d = a√3", "slider_label": "طول ضلع المكعب:", "slider_min": 1, "slider_max": 5, "slider_val": 3, "slider_unit": " وحدة", "components": [{"id": "cube", "name": "المكعب", "role": "نموذج ثلاثي الأبعاد يمكن دورانه."}, {"id": "diagonal", "name": "القطر الفراغي", "role": "يصل بين رأسين متقابلين وطوله a√3."}]},
    "diag-math-line-plane": {"id": "diag-math-line-plane", "lab_exp": "lab-math-line-plane", "title": "الزاوية بين مستقيم ومستوى", "sim_key": "math_line_plane", "formula": "sin θ = |u·n|/(|u||n|)", "slider_label": "زاوية المستقيم:", "slider_min": 0, "slider_max": 90, "slider_val": 35, "slider_unit": "°", "components": [{"id": "plane", "name": "المستوى", "role": "سطح أفقي يمثل المعادلة Ax+By+Cz+D=0."}, {"id": "line", "name": "المستقيم", "role": "اتجاهه u يحدد الزاوية مع المستوى."}, {"id": "normal", "name": "المتجه الطبيعي", "role": "العمود على المستوى."}]},
    "diag-math-dihedral": {"id": "diag-math-dihedral", "lab_exp": "lab-math-dihedral", "title": "الزاوية بين مستويين", "sim_key": "math_dihedral", "formula": "cos φ = |n₁·n₂|/(|n₁||n₂|)", "slider_label": "زاوية المستوى الثاني:", "slider_min": 0, "slider_max": 120, "slider_val": 60, "slider_unit": "°", "components": [{"id": "plane1", "name": "المستوى الأول", "role": "متجهه الطبيعي n₁."}, {"id": "plane2", "name": "المستوى الثاني", "role": "متجهه الطبيعي n₂."}, {"id": "edge", "name": "خط التقاطع", "role": "منه تُقاس الزاوية ثنائية الوجه."}]},
    "diag-math-probability": {"id": "diag-math-probability", "lab_exp": "lab-math-probability", "title": "فضاء العينة والاحتمالات", "sim_key": "math_probability_space", "formula": "P(A∪B)=P(A)+P(B)−P(A∩B)", "slider_label": "احتمال الحدث A:", "slider_min": 0, "slider_max": 100, "slider_val": 55, "slider_unit": "%", "components": [{"id": "space", "name": "فضاء العينة", "role": "كل النتجات الممكنة."}, {"id": "eventA", "name": "الحدث A", "role": "مجموعة نتجات جزئية."}, {"id": "eventB", "name": "الحدث B", "role": "يتداخل مع A في بعض المسائل."}]},
    "diag-math-derivative": {"id": "diag-math-derivative", "lab_exp": "lab-math-derivative", "title": "مماس المنحنى والمشتقة", "sim_key": "math_derivative", "formula": "f′(x)=lim[f(x+h)−f(x)]/h", "slider_label": "موضع نقطة المماس:", "slider_min": 1, "slider_max": 9, "slider_val": 4, "slider_unit": "", "components": [{"id": "curve", "name": "المنحنى", "role": "الدالة f(x)."}, {"id": "tangent", "name": "المماس", "role": "ميله يساوي f′(x)."}]},
    "diag-math-integral": {"id": "diag-math-integral", "lab_exp": "lab-math-integral", "title": "التكامل والمساحة تحت المنحنى", "sim_key": "math_integral", "formula": "∫ₐᵇf(x)dx=F(b)−F(a)", "slider_label": "حد التكامل العلوي:", "slider_min": 1, "slider_max": 10, "slider_val": 6, "slider_unit": "", "components": [{"id": "area", "name": "المساحة", "role": "تتراكم تحت المنحنى."}, {"id": "curve", "name": "الدالة", "role": "حدود التكامل تحدد الفترة."}]},
    "diag-math-area": {"id": "diag-math-area", "lab_exp": "lab-math-area", "title": "المساحة بين منحنيين", "sim_key": "math_area_between", "formula": "A=∫ₐᵇ|f(x)−g(x)|dx", "slider_label": "الحد العلوي:", "slider_min": 1, "slider_max": 10, "slider_val": 5, "slider_unit": "", "components": [{"id": "upper", "name": "المنحنى العلوي", "role": "f(x)."}, {"id": "lower", "name": "المنحنى السفلي", "role": "g(x)."}]},
    "diag-math-revolution": {"id": "diag-math-revolution", "lab_exp": "lab-math-revolution", "title": "حجم مجسم الدوران", "sim_key": "math_revolution", "formula": "V=π∫ₐᵇ[f(x)]²dx", "slider_label": "عدد الأقراص:", "slider_min": 4, "slider_max": 20, "slider_val": 10, "slider_unit": "", "components": [{"id": "discs", "name": "الأقراص", "role": "نصف القطر f(x) والسمك dx."}, {"id": "axis", "name": "محور الدوران", "role": "محور x غالباً."}]}
}
ACTIVITIES = {
    "act-math-complex-add": {"id": "act-math-complex-add", "title": "جمع الأعداد المركبة", "unit_id": "u1", "book_page": 13, "sim_type": "math_complex_add", "description": "غيّر المكوّنات الحقيقية والتخيلية ولاحظ نتيجة الجمع في مستوى أرغاند.", "controls": [{"id": "a", "label": "الجزء الحقيقي z₁", "min": -5, "max": 5, "step": 1, "default": 2}, {"id": "b", "label": "الجزء التخيلي z₁", "min": -5, "max": 5, "step": 1, "default": 3}, {"id": "c", "label": "الجزء الحقيقي z₂", "min": -5, "max": 5, "step": 1, "default": -1}, {"id": "d", "label": "الجزء التخيلي z₂", "min": -5, "max": 5, "step": 1, "default": 2}]},
    "act-math-complex-modulus": {"id": "act-math-complex-modulus", "title": "القيمة المطلقة والسعة", "unit_id": "u1", "book_page": 19, "sim_type": "math_complex_modulus", "description": "احسب طول متجه العدد المركب من مكوّناته.", "controls": [{"id": "a", "label": "الجزء الحقيقي a", "min": -6, "max": 6, "step": 1, "default": 3}, {"id": "b", "label": "الجزء التخيلي b", "min": -6, "max": 6, "step": 1, "default": 4}]},
    "act-math-polar": {"id": "act-math-polar", "title": "التحويل إلى الصيغة القطبية", "unit_id": "u1", "book_page": 38, "sim_type": "math_polar", "description": "حرك الطول r والزاوية θ ولاحظ الإحداثيات الجبرية.", "controls": [{"id": "r", "label": "القيمة المطلقة r", "min": 1, "max": 10, "step": 1, "default": 5}, {"id": "theta", "label": "الزاوية θ", "min": 0, "max": 360, "step": 5, "default": 60}]},
    "act-math-demoivre": {"id": "act-math-demoivre", "title": "مبرهنة دي موافر", "unit_id": "u2", "book_page": 46, "sim_type": "math_de_moivre", "description": "ارفع العدد المركب إلى القوة n ولاحظ تضاعف الطول والزاوية.", "controls": [{"id": "r", "label": "القيمة المطلقة r", "min": 1, "max": 4, "step": 1, "default": 2}, {"id": "theta", "label": "الزاوية θ", "min": 0, "max": 120, "step": 5, "default": 30}, {"id": "n", "label": "القوة n", "min": 1, "max": 8, "step": 1, "default": 3}]},
    "act-math-roots": {"id": "act-math-roots", "title": "الجذور النونية للعدد المركب", "unit_id": "u2", "book_page": 52, "sim_type": "math_roots", "description": "اعرض الجذور النونية موزعة على دائرة نصف قطرها r^(1/n).", "controls": [{"id": "r", "label": "القيمة المطلقة r", "min": 1, "max": 16, "step": 1, "default": 8}, {"id": "theta", "label": "زاوية العدد θ", "min": 0, "max": 360, "step": 15, "default": 60}, {"id": "n", "label": "درجة الجذر n", "min": 2, "max": 8, "step": 1, "default": 3}]},
    "act-math-binomial": {"id": "act-math-binomial", "title": "التوسعة ذات الحدين", "unit_id": "u2", "book_page": 58, "sim_type": "math_binomial", "description": "اختر n و k لحساب المعامل C(n,k) وحد التوسعة.", "controls": [{"id": "n", "label": "الأس n", "min": 2, "max": 12, "step": 1, "default": 6}, {"id": "k", "label": "رقم الحد k", "min": 0, "max": 12, "step": 1, "default": 2}]},
    "act-math-cone": {"id": "act-math-cone", "title": "قطع المخروط", "unit_id": "u3", "book_page": 106, "sim_type": "math_cone_sections", "description": "غيّر ميل مستوى القطع ولاحظ نوع القطع الناتج.", "controls": [{"id": "tilt", "label": "ميل مستوى القطع", "min": 0, "max": 90, "step": 5, "default": 35}]},
    "act-math-ellipse": {"id": "act-math-ellipse", "title": "القطع الناقص", "unit_id": "u3", "book_page": 112, "sim_type": "math_ellipse_lab", "description": "غيّر a و b ولاحظ شكل القطع الناقص وبؤرتيه.", "controls": [{"id": "a", "label": "نصف المحور الكبير a", "min": 2, "max": 8, "step": 1, "default": 5}, {"id": "b", "label": "نصف المحور الصغير b", "min": 1, "max": 7, "step": 1, "default": 3}]},
    "act-math-hyperbola": {"id": "act-math-hyperbola", "title": "القطع الزائد", "unit_id": "u3", "book_page": 120, "sim_type": "math_hyperbola_lab", "description": "غيّر a و b ولاحظ الفروع والخطين المقاربين.", "controls": [{"id": "a", "label": "المعلمة a", "min": 1, "max": 6, "step": 1, "default": 2}, {"id": "b", "label": "المعلمة b", "min": 1, "max": 6, "step": 1, "default": 3}]},
    "act-math-parabola": {"id": "act-math-parabola", "title": "القطع المكافئ", "unit_id": "u3", "book_page": 126, "sim_type": "math_parabola_lab", "description": "غيّر p ولاحظ حركة البؤرة والدليل.", "controls": [{"id": "p", "label": "المعلمة p", "min": 1, "max": 6, "step": 1, "default": 2}]},
    "act-math-space-diagonal": {"id": "act-math-space-diagonal", "title": "القطر الفراغي للمكعب", "unit_id": "u4", "book_page": 136, "sim_type": "math_space_diagonal", "description": "غيّر طول ضلع المكعب واحسب القطر الفراغي a√3.", "controls": [{"id": "a", "label": "طول الضلع a", "min": 1, "max": 10, "step": 1, "default": 4}]},
    "act-math-line-plane": {"id": "act-math-line-plane", "title": "الزاوية بين مستقيم ومستوى", "unit_id": "u4", "book_page": 144, "sim_type": "math_line_plane", "description": "غيّر زاوية المستقيم مع المتجه الطبيعي ولاحظ الزاوية مع المستوى.", "controls": [{"id": "alpha", "label": "زاوية المستقيم مع الطبيعي", "min": 0, "max": 90, "step": 5, "default": 40}]},
    "act-math-dihedral": {"id": "act-math-dihedral", "title": "الزاوية ثنائية الوجه", "unit_id": "u4", "book_page": 149, "sim_type": "math_dihedral", "description": "دور مستوى حول خط التقاطع ولاحظ الزاوية بين المتجهين الطبيعيين.", "controls": [{"id": "phi", "label": "زاوية المستوى الثاني", "min": 0, "max": 120, "step": 5, "default": 60}]},
    "act-math-prob-union": {"id": "act-math-prob-union", "title": "قاعدة جمع الاحتمالات", "unit_id": "u5", "book_page": 82, "sim_type": "math_prob_union", "description": "غيّر احتمالي الحدثين وتداخلهما ولاحظ P(A∪B).", "controls": [{"id": "pa", "label": "P(A)", "min": 0, "max": 100, "step": 5, "default": 55}, {"id": "pb", "label": "P(B)", "min": 0, "max": 100, "step": 5, "default": 40}, {"id": "inter", "label": "P(A∩B)", "min": 0, "max": 100, "step": 5, "default": 20}]},
    "act-math-prob-conditional": {"id": "act-math-prob-conditional", "title": "الاحتمال الشرطي", "unit_id": "u5", "book_page": 89, "sim_type": "math_prob_conditional", "description": "احسب احتمال A بشرط حدوث B.", "controls": [{"id": "pa", "label": "P(A∩B)", "min": 0, "max": 100, "step": 5, "default": 25}, {"id": "pb", "label": "P(B)", "min": 5, "max": 100, "step": 5, "default": 50}]},
    "act-math-prob-binomial": {"id": "act-math-prob-binomial", "title": "التوزيع ذو الحدين", "unit_id": "u5", "book_page": 96, "sim_type": "math_prob_binomial", "description": "احتمال k نجاحاً في n تجربة مستقلة.", "controls": [{"id": "n", "label": "عدد التجارب n", "min": 1, "max": 20, "step": 1, "default": 10}, {"id": "p", "label": "احتمال النجاح p", "min": 0, "max": 100, "step": 5, "default": 50}, {"id": "k", "label": "عدد النجاحات k", "min": 0, "max": 20, "step": 1, "default": 4}]},
    "act-math-power-rule": {"id": "act-math-power-rule", "title": "قاعدة القوة في الاشتقاق", "unit_id": "u6", "book_page": 162, "sim_type": "math_power_derivative", "description": "اشتق xⁿ ولاحظ قيمة المشتقة عند x.", "controls": [{"id": "x", "label": "القيمة x", "min": 1, "max": 8, "step": 1, "default": 3}, {"id": "n", "label": "الأس n", "min": 1, "max": 8, "step": 1, "default": 3}]},
    "act-math-product-rule": {"id": "act-math-product-rule", "title": "قاعدة الجداء", "unit_id": "u6", "book_page": 166, "sim_type": "math_product_rule", "description": "طبّق (uv)′ = u′v + uv′ على مثال بسيط.", "controls": [{"id": "x", "label": "القيمة x", "min": 1, "max": 8, "step": 1, "default": 2}, {"id": "a", "label": "معامل u", "min": 1, "max": 5, "step": 1, "default": 2}, {"id": "b", "label": "معامل v", "min": 1, "max": 5, "step": 1, "default": 3}]},
    "act-math-chain-rule": {"id": "act-math-chain-rule", "title": "قاعدة السلسلة", "unit_id": "u6", "book_page": 169, "sim_type": "math_chain_rule", "description": "اشتق (ax+b)ⁿ خطوة بخطوة.", "controls": [{"id": "x", "label": "القيمة x", "min": 0, "max": 6, "step": 1, "default": 2}, {"id": "a", "label": "المعامل a", "min": 1, "max": 4, "step": 1, "default": 2}, {"id": "n", "label": "الأس n", "min": 2, "max": 6, "step": 1, "default": 3}]},
    "act-math-extrema": {"id": "act-math-extrema", "title": "القيم القصوى", "unit_id": "u6", "book_page": 192, "sim_type": "math_extrema", "description": "ابحث عن النقطة الحرجة لدالة تربيعية.", "controls": [{"id": "a", "label": "المعامل a", "min": -5, "max": 5, "step": 1, "default": 1}, {"id": "b", "label": "المعامل b", "min": -10, "max": 10, "step": 1, "default": -4}, {"id": "c", "label": "الثابت c", "min": -10, "max": 10, "step": 1, "default": 3}]},
    "act-math-mvt": {"id": "act-math-mvt", "title": "نظرية القيمة المتوسطة", "unit_id": "u6", "book_page": 203, "sim_type": "math_mvt", "description": "قارن ميل القطرة بميل المماس عند نقطة داخل الفترة.", "controls": [{"id": "a", "label": "الحد الأدنى a", "min": 0, "max": 5, "step": 1, "default": 1}, {"id": "b", "label": "الحد الأعلى b", "min": 3, "max": 10, "step": 1, "default": 5}]},
    "act-math-indefinite": {"id": "act-math-indefinite", "title": "التكامل غير المحدد", "unit_id": "u7", "book_page": 214, "sim_type": "math_indefinite", "description": "طبّق قاعدة تكامل القوة.", "controls": [{"id": "n", "label": "الأس n", "min": 0, "max": 8, "step": 1, "default": 3}]},
    "act-math-definite": {"id": "act-math-definite", "title": "التكامل المحدد", "unit_id": "u7", "book_page": 237, "sim_type": "math_definite_integral", "description": "احسب ∫xⁿdx من a إلى b.", "controls": [{"id": "a", "label": "الحد الأدنى a", "min": 0, "max": 5, "step": 1, "default": 1}, {"id": "b", "label": "الحد الأعلى b", "min": 2, "max": 10, "step": 1, "default": 4}, {"id": "n", "label": "الأس n", "min": 0, "max": 6, "step": 1, "default": 2}]},
    "act-math-area": {"id": "act-math-area", "title": "المساحة تحت المنحنى", "unit_id": "u7", "book_page": 246, "sim_type": "math_area_between", "description": "احسب المساحة تحت xⁿ بين حدين.", "controls": [{"id": "a", "label": "الحد الأدنى a", "min": 0, "max": 5, "step": 1, "default": 0}, {"id": "b", "label": "الحد الأعلى b", "min": 2, "max": 10, "step": 1, "default": 3}, {"id": "n", "label": "الأس n", "min": 0, "max": 5, "step": 1, "default": 2}]},
    "act-math-revolution": {"id": "act-math-revolution", "title": "حجم مجسم الدوران", "unit_id": "u7", "book_page": 250, "sim_type": "math_revolution_volume", "description": "احسب حجم دوران y=xⁿ حول محور x.", "controls": [{"id": "a", "label": "الحد الأدنى a", "min": 0, "max": 4, "step": 1, "default": 0}, {"id": "b", "label": "الحد الأعلى b", "min": 1, "max": 6, "step": 1, "default": 2}, {"id": "n", "label": "الأس n", "min": 1, "max": 4, "step": 1, "default": 1}]}
}
SOLUTIONS = {
    "sol-math-complex-add": {"id": "sol-math-complex-add", "title": "جمع عددين مركبين", "source_page": 13, "prompt": "إذا كان z₁ = 2 + 3i و z₂ = −1 + 2i فاحسب z₁ + z₂.", "given": "z₁ = 2 + 3i، z₂ = −1 + 2i", "answer": "1 + 5i", "tolerance": 0.01, "hint": "اجمع الأجزاء الحقيقية معاً والتخيلية معاً.", "steps": [{"title": "اجمع الأجزاء الحقيقية", "detail": "2 + (−1) = 1", "formula": "Re(z₁+z₂)=Re(z₁)+Re(z₂)"}, {"title": "اجمع الأجزاء التخيلية", "detail": "3 + 2 = 5", "formula": "Im(z₁+z₂)=Im(z₁)+Im(z₂)"}, {"title": "اكتب النتيجة", "detail": "العدد المركب الناتج هو 1 + 5i.", "formula": "z₁+z₂=1+5i"}]},
    "sol-math-complex-modulus": {"id": "sol-math-complex-modulus", "title": "القيمة المطلقة لعدد مركب", "source_page": 19, "prompt": "احسب |3 + 4i|.", "given": "z = 3 + 4i", "answer": "5", "tolerance": 0.01, "hint": "استخدم نظرية فيثاغورس على مكوّنات العدد.", "steps": [{"title": "طبّق الصيغة", "detail": "|z| = √(3² + 4²)", "formula": "|a+bi|=√(a²+b²)"}, {"title": "احسب المجموع", "detail": "9 + 16 = 25", "formula": "|z|=√25"}, {"title": "النتيجة", "detail": "القيمة المطلقة تساوي 5.", "formula": "|3+4i|=5"}]},
    "sol-math-polar": {"id": "sol-math-polar", "title": "التحويل إلى الصيغة القطبية", "source_page": 38, "prompt": "اكتب z = 1 + √3 i بالصيغة القطبية.", "given": "a = 1، b = √3", "answer": "2(cos60° + i sin60°)", "tolerance": 0.01, "hint": "احسب r أولاً ثم الزاوية في الربع الصحيح.", "steps": [{"title": "القيمة المطلقة", "detail": "r = √(1 + 3) = 2", "formula": "r=√(a²+b²)"}, {"title": "الزاوية", "detail": "tan θ = √3/1، إذن θ = 60° لأن النقطة في الربع الأول.", "formula": "θ=tan⁻¹(b/a)"}, {"title": "الصيغة القطبية", "detail": "z = 2(cos60° + i sin60°).", "formula": "z=r(cosθ+i sinθ)"}]},
    "sol-math-demoivre": {"id": "sol-math-demoivre", "title": "تطبيق مبرهنة دي موافر", "source_page": 46, "prompt": "احسب (cos30° + i sin30°)³.", "given": "r = 1، θ = 30°، n = 3", "answer": "cos90° + i sin90° = i", "tolerance": 0.01, "hint": "اضرب الزاوية في الأس.", "steps": [{"title": "القيمة المطلقة", "detail": "1³ = 1", "formula": "rⁿ"}, {"title": "الزاوية", "detail": "3 × 30° = 90°", "formula": "nθ"}, {"title": "النتيجة", "detail": "cos90° + i sin90° = i.", "formula": "(cosθ+i sinθ)ⁿ=cos nθ+i sin nθ"}]},
    "sol-math-binomial": {"id": "sol-math-binomial", "title": "معامل في التوسعة ذات الحدين", "source_page": 58, "prompt": "احسب معامل الحد الذي يحتوي على b² في (a+b)⁶.", "given": "n = 6، k = 2", "answer": "15", "tolerance": 0.01, "hint": "استخدم C(n,k) = n! / (k!(n−k)!).", "steps": [{"title": "اكتب الصيغة", "detail": "C(6,2) = 6! / (2!4!)", "formula": "C(n,k)=n!/(k!(n−k)!)"}, {"title": "بسّط", "detail": "C(6,2) = (6×5)/(2×1) = 15", "formula": "C(6,2)=15"}, {"title": "النتيجة", "detail": "معامل الحد هو 15.", "formula": "15a⁴b²"}]},
    "sol-math-ellipse": {"id": "sol-math-ellipse", "title": "بؤرتا قطع ناقص", "source_page": 112, "prompt": "للقطع x²/25 + y²/9 = 1، أوجد البؤرتين.", "given": "a² = 25، b² = 9", "answer": "(−4، 0) و (4، 0)", "tolerance": 0.01, "hint": "a هي أكبر مقام، و c² = a² − b².", "steps": [{"title": "حدد a و b", "detail": "a = 5، b = 3 لأن 25 > 9.", "formula": "a>b"}, {"title": "احسب c", "detail": "c² = 25 − 9 = 16 إذن c = 4.", "formula": "c²=a²−b²"}, {"title": "البؤرتان", "detail": "تقعان على المحور x: (−4،0) و (4،0).", "formula": "(±c،0)"}]},
    "sol-math-hyperbola": {"id": "sol-math-hyperbola", "title": "خطا القطع الزائد المقاربان", "source_page": 120, "prompt": "أوجد خطي المقاربة للقطع x²/4 − y²/9 = 1.", "given": "a = 2، b = 3", "answer": "y = ±(3/2)x", "tolerance": 0.01, "hint": "خطا المقاربة يمران بنقطة الأصل.", "steps": [{"title": "حدد a و b", "detail": "a² = 4 إذن a = 2، b² = 9 إذن b = 3.", "formula": "x²/a²−y²/b²=1"}, {"title": "طبّق معادلة المقاربة", "detail": "y = ±(b/a)x", "formula": "y=±(b/a)x"}, {"title": "النتيجة", "detail": "y = ±(3/2)x.", "formula": "y=±1.5x"}]},
    "sol-math-parabola": {"id": "sol-math-parabola", "title": "بؤرة مكافئ", "source_page": 126, "prompt": "أوجد بؤرة القطع y² = 12x.", "given": "4p = 12", "answer": "(3، 0)", "tolerance": 0.01, "hint": "قارن المعادلة بصيغة y² = 4px.", "steps": [{"title": "احسب p", "detail": "4p = 12 إذن p = 3.", "formula": "y²=4px"}, {"title": "موضع البؤرة", "detail": "البؤرة هي (p، 0).", "formula": "F=(p،0)"}, {"title": "النتيجة", "detail": "F = (3، 0).", "formula": "F=(3،0)"}]},
    "sol-math-space-diagonal": {"id": "sol-math-space-diagonal", "title": "القطر الفراغي لمكعب", "source_page": 136, "prompt": "مكعب ضلعه 4، احسب قطره الفراغي.", "given": "a = 4", "answer": "4√3 ≈ 6.928", "tolerance": 0.01, "hint": "استخدم فيثاغورس مرتين.", "steps": [{"title": "قطر الوجه", "detail": "d_face = √(a²+a²) = a√2", "formula": "d_face=a√2"}, {"title": "القطر الفراغي", "detail": "d = √(d_face² + a²) = √(2a²+a²)", "formula": "d=a√3"}, {"title": "التعويض", "detail": "d = 4√3 ≈ 6.928.", "formula": "d≈6.928"}]},
    "sol-math-line-plane": {"id": "sol-math-line-plane", "title": "زاوية مستقيم مع مستوى", "source_page": 144, "prompt": "إذا كانت زاوية مستقيم مع المتجه الطبيعي لمستوى 40°، فما زاويته مع المستوى؟", "given": "α = 40°", "answer": "50°", "tolerance": 0.01, "hint": "الزاويتان مكمّلتان.", "steps": [{"title": "العلاقة", "detail": "θ = 90° − α", "formula": "θ=90°−α"}, {"title": "التعويض", "detail": "θ = 90° − 40° = 50°.", "formula": "θ=50°"}]},
    "sol-math-dihedral": {"id": "sol-math-dihedral", "title": "الزاوية بين مستويين", "source_page": 149, "prompt": "إذا كان المتجهان الطبيعيان متعامدين، فما الزاوية بين المستويين؟", "given": "n₁·n₂ = 0", "answer": "90°", "tolerance": 0.01, "hint": "استخدم جيب تمام الزاوية بين المتجهين.", "steps": [{"title": "حالة التعامد", "detail": "ناتج الجداء النقطة صفر يعني المتجهين متعامدين.", "formula": "n₁·n₂=0"}, {"title": "الزاوية", "detail": "إذن الزاوية بين المستويين 90°.", "formula": "φ=90°"}]},
    "sol-math-prob-union": {"id": "sol-math-prob-union", "title": "احتمال اتحاد حدثين", "source_page": 82, "prompt": "إذا كان P(A)=0.55 و P(B)=0.40 و P(A∩B)=0.20، فاحسب P(A∪B).", "given": "P(A)=0.55، P(B)=0.40، P(A∩B)=0.20", "answer": "0.75", "tolerance": 0.001, "hint": "اطرح التداخل حتى لا تحسبه مرتين.", "steps": [{"title": "قاعدة الجمع", "detail": "P(A∪B)=P(A)+P(B)−P(A∩B)", "formula": "P(A∪B)=P(A)+P(B)−P(A∩B)"}, {"title": "التعويض", "detail": "0.55 + 0.40 − 0.20 = 0.75", "formula": "=0.75"}]},
    "sol-math-prob-conditional": {"id": "sol-math-prob-conditional", "title": "احتمال شرطي", "source_page": 89, "prompt": "إذا كان P(A∩B)=0.25 و P(B)=0.50، فاحسب P(A|B).", "given": "P(A∩B)=0.25، P(B)=0.50", "answer": "0.5", "tolerance": 0.001, "hint": "قسّم على احتمال الشرط.", "steps": [{"title": "الصيغة", "detail": "P(A|B)=P(A∩B)/P(B)", "formula": "P(A|B)=P(A∩B)/P(B)"}, {"title": "التعويض", "detail": "0.25 / 0.50 = 0.5", "formula": "=0.5"}]},
    "sol-math-prob-binomial": {"id": "sol-math-prob-binomial", "title": "احتمال ذو حدين", "source_page": 96, "prompt": "في 10 تجارب احتمال النجاح 0.5، احتمال 4 نجاحات؟", "given": "n=10، p=0.5، k=4", "answer": "0.2051", "tolerance": 0.001, "hint": "استخدم C(n,k)pᵏ(1−p)ⁿ⁻ᵏ.", "steps": [{"title": "المعامل", "detail": "C(10,4)=210", "formula": "C(n,k)=n!/(k!(n−k)!)"}, {"title": "التعويض", "detail": "210(0.5)⁴(0.5)⁶ = 210/1024", "formula": "P(X=4)=210/1024"}, {"title": "النتيجة", "detail": "≈ 0.2051", "formula": "≈0.2051"}]},
    "sol-math-power": {"id": "sol-math-power", "title": "مشتقة دالة قوة", "source_page": 162, "prompt": "إذا كان f(x)=x³، احسب f′(2).", "given": "f(x)=x³، x=2", "answer": "12", "tolerance": 0.01, "hint": "انقص الأس بمقدار 1 ثم عوّض.", "steps": [{"title": "القاعدة", "detail": "(xⁿ)′=nxⁿ⁻¹", "formula": "(xⁿ)′=nxⁿ⁻¹"}, {"title": "المشتقة", "detail": "f′(x)=3x²", "formula": "f′(x)=3x²"}, {"title": "التعويض", "detail": "f′(2)=3×4=12", "formula": "12"}]},
    "sol-math-chain": {"id": "sol-math-chain", "title": "قاعدة السلسلة", "source_page": 169, "prompt": "اشتق f(x)=(2x+1)³.", "given": "g(x)=2x+1، n=3", "answer": "6(2x+1)²", "tolerance": 0.01, "hint": "اضرب مشتقة الخارج في مشتقة الداخل.", "steps": [{"title": "الخارج", "detail": "3(2x+1)²", "formula": "n[g(x)]ⁿ⁻¹"}, {"title": "الداخل", "detail": "(2x+1)′=2", "formula": "g′(x)=2"}, {"title": "النتيجة", "detail": "f′(x)=6(2x+1)²", "formula": "f′(x)=f′(g(x))g′(x)"}]},
    "sol-math-extrema": {"id": "sol-math-extrema", "title": "قيمة صغرى لدالة تربيعية", "source_page": 192, "prompt": "للدالة f(x)=x²−4x+3، أوجد النقطة الحرجة.", "given": "a=1، b=−4", "answer": "2", "tolerance": 0.01, "hint": "احل f′(x)=0.", "steps": [{"title": "المشتقة", "detail": "f′(x)=2x−4", "formula": "f′(x)=2ax+b"}, {"title": "المعادلة", "detail": "2x−4=0 إذن x=2", "formula": "x=−b/(2a)"}, {"title": "النوع", "detail": "لأن a>0 فالنقطة قيمة صغرى.", "formula": "f″(x)=2>0"}]},
    "sol-math-mvt": {"id": "sol-math-mvt", "title": "نظرية القيمة المتوسطة", "source_page": 203, "prompt": "للدالة f(x)=x² على [1،5]، أوجد c الذي يحقق المبرهنة.", "given": "f(x)=x²، a=1، b=5", "answer": "3", "tolerance": 0.01, "hint": "ميل القطرة = (f(b)−f(a))/(b−a).", "steps": [{"title": "ميل القطرة", "detail": "(25−1)/(5−1)=6", "formula": "[f(b)−f(a)]/(b−a)"}, {"title": "المشتقة", "detail": "f′(c)=2c", "formula": "2c=6"}, {"title": "النتيجة", "detail": "c=3 وهو داخل الفترة.", "formula": "c=3"}]},
    "sol-math-indefinite": {"id": "sol-math-indefinite", "title": "تكامل قوة", "source_page": 214, "prompt": "احسب ∫x³dx.", "given": "n=3", "answer": "x⁴/4 + C", "tolerance": 0.01, "hint": "زد الأس بمقدار 1 ثم اقسم على الأس الجديد.", "steps": [{"title": "القاعدة", "detail": "∫xⁿdx=xⁿ⁺¹/(n+1)+C", "formula": "n≠−1"}, {"title": "التعويض", "detail": "∫x³dx=x⁴/4+C", "formula": "=x⁴/4+C"}]},
    "sol-math-definite": {"id": "sol-math-definite", "title": "تكامل محدد", "source_page": 237, "prompt": "احسب ∫₁⁴ x² dx.", "given": "a=1، b=4، n=2", "answer": "21", "tolerance": 0.01, "hint": "استخدم F(b)−F(a).", "steps": [{"title": "المضاد", "detail": "F(x)=x³/3", "formula": "F(x)=x³/3"}, {"title": "التعويض", "detail": "64/3 − 1/3 = 63/3", "formula": "F(4)−F(1)"}, {"title": "النتيجة", "detail": "21", "formula": "=21"}]},
    "sol-math-area": {"id": "sol-math-area", "title": "مساحة تحت منحنى", "source_page": 246, "prompt": "احسب المساحة تحت y=x² من 0 إلى 3.", "given": "a=0، b=3، f(x)=x²", "answer": "9", "tolerance": 0.01, "hint": "المساحة هي التكامل المحدد للدالة.", "steps": [{"title": "التكامل", "detail": "A=∫₀³x²dx", "formula": "A=∫ₐᵇf(x)dx"}, {"title": "المضاد", "detail": "[x³/3]₀³=27/3", "formula": "=9"}]},
    "sol-math-revolution": {"id": "sol-math-revolution", "title": "حجم مجسم دوران", "source_page": 250, "prompt": "احسب حجم دوران y=x حول محور x من 0 إلى 2.", "given": "f(x)=x، a=0، b=2", "answer": "8π/3 ≈ 8.378", "tolerance": 0.01, "hint": "استخدم طريقة الأقراص V=π∫f²dx.", "steps": [{"title": "الصيغة", "detail": "V=π∫₀²x²dx", "formula": "V=π∫ₐᵇ[f(x)]²dx"}, {"title": "التكامل", "detail": "π[x³/3]₀²=8π/3", "formula": "=8π/3"}, {"title": "النتيجة", "detail": "≈ 8.378 وحدة مكعبة.", "formula": "≈8.378"}]}
}
GLOSSARY = {
    "v-complex": {"id": "v-complex", "term": "العدد المركب", "definition": "عدد على الصورة a + bi حيث a و b حقيقيان و i² = −1.", "unit_id": "u1", "page": 7},
    "v-imaginary": {"id": "v-imaginary", "term": "الوحدة التخيلية", "definition": "العدد i الذي يحقق i² = −1.", "unit_id": "u1", "page": 7},
    "v-argand": {"id": "v-argand", "term": "مستوى أرغاند", "definition": "مستوى إحداثيات يمثل فيه العدد المركب a + bi بالنقطة (a، b).", "unit_id": "u1", "page": 16},
    "v-modulus": {"id": "v-modulus", "term": "القيمة المطلقة", "definition": "طول متجه العدد المركب من مبدأ الإحداثيات: |z| = √(a²+b²).", "unit_id": "u1", "page": 19},
    "v-argument": {"id": "v-argument", "term": "سعة العدد المركب", "definition": "الزاوية بين متجه العدد المركب والمحور الحقيقي الموجب.", "unit_id": "u1", "page": 23},
    "v-polar": {"id": "v-polar", "term": "الصيغة القطبية", "definition": "كتابة العدد المركب على الصورة r(cosθ + i sinθ).", "unit_id": "u1", "page": 33},
    "v-demoivre": {"id": "v-demoivre", "term": "مبرهنة دي موافر", "definition": "قاعدة لرفع الأعداد المركبة المكتوبة بالصيغة القطبية إلى قوة n.", "unit_id": "u2", "page": 45},
    "v-root": {"id": "v-root", "term": "الجذر النوني", "definition": "أي عدد مركب w يحقق wⁿ = z.", "unit_id": "u2", "page": 49},
    "v-binomial": {"id": "v-binomial", "term": "التوسعة ذات الحدين", "definition": "صيغة لتوسيع (a+b)ⁿ باستخدام المعاملات C(n,k).", "unit_id": "u2", "page": 55},
    "v-conic": {"id": "v-conic", "term": "القطع المخروطي", "definition": "منحنى ينشأ من تقاطع مستوى مع مخروط دائري، أو بمجموع/فرق/nسبة بعدين ثابتة.", "unit_id": "u3", "page": 104},
    "v-focus": {"id": "v-focus", "term": "البؤرة", "definition": "نقطة ثابتة تستخدم في تعريف القطع المخروطي.", "unit_id": "u3", "page": 104},
    "v-directrix": {"id": "v-directrix", "term": "الدليل", "definition": "مستقيم ثابت يستخدم في تعريف القطع المخروطي.", "unit_id": "u3", "page": 104},
    "v-eccentricity": {"id": "v-eccentricity", "term": "الانحراف", "definition": "النسبة e = PF/PD، وتحدد نوع القطع المخروطي.", "unit_id": "u3", "page": 104},
    "v-ellipse": {"id": "v-ellipse", "term": "القطع الناقص", "definition": "مجموع بعدي أي نقطة فيه عن بؤرتين ثابت.",
    "unit_id": "u3", "page": 110},
    "v-hyperbola": {"id": "v-hyperbola", "term": "القطع الزائد", "definition": "الفرق المطلق لبعدي أي نقطة فيه عن بؤرتين ثابت.", "unit_id": "u3", "page": 118},
    "v-parabola": {"id": "v-parabola", "term": "القطع المكافئ", "definition": "مجموعة نقاط متساوية البعد عن بؤرة ودليل ثابتين.", "unit_id": "u3", "page": 124},
    "v-asymptote": {"id": "v-asymptote", "term": "الخط المقارب", "definition": "خط يقترب منه منحنى القطع الزائد دون أن يلمسه.", "unit_id": "u3", "page": 118},
    "v-plane": {"id": "v-plane", "term": "المستوى", "definition": "مجموعة نقاط تحقق معادلة خطية Ax + By + Cz + D = 0 في الفراغ.", "unit_id": "u4", "page": 133},
    "v-normal": {"id": "v-normal", "term": "المتجه الطبيعي", "definition": "متجه عمودي على المستوى ومعاملاته (A، B، C).", "unit_id": "u4", "page": 133},
    "v-space-diagonal": {"id": "v-space-diagonal", "term": "القطر الفراغي", "definition": "القط الواصل بين رأسين متقابلين في مكعب وطوله a√3.", "unit_id": "u4", "page": 136},
    "v-dihedral": {"id": "v-dihedral", "term": "الزاوية ثنائية الوجه", "definition": "الزاوية بين مستويين تقاس من متجهيهما الطبيعيين.", "unit_id": "u4", "page": 147},
    "v-probability": {"id": "v-probability", "term": "الاحتمال", "definition": "مقياس حدوث حدث عشوائي بين 0 و 1.", "unit_id": "u5", "page": 74},
    "v-sample-space": {"id": "v-sample-space", "term": "فضاء العينة", "definition": "مجموعة كل النتجات الممكنة للتجربة العشوائية.", "unit_id": "u5", "page": 74},
    "v-union": {"id": "v-union", "term": "اتحاد الحدثين", "definition": "حدث يحدث إذا تحقق A أو B أو كلاهما.", "unit_id": "u5", "page": 79},
    "v-intersection": {"id": "v-intersection", "term": "تقاطع الحدثين", "definition": "حدث يحدث إذا تحقق A و B معاً.", "unit_id": "u5", "page": 79},
    "v-conditional": {"id": "v-conditional", "term": "الاحتمال الشرطي", "definition": "احتمال حدوث A بشرط حدوث B ويُكتب P(A|B)=P(A∩B)/P(B).", "unit_id": "u5", "page": 86},
    "v-independent": {"id": "v-independent", "term": "حدثان مستقلان", "definition": "حدثان لا يؤثر أحدهما في احتمال الآخر، أي P(A|B)=P(A).", "unit_id": "u5", "page": 86},
    "v-derivative": {"id": "v-derivative", "term": "المشتقة", "definition": "معدل التغير اللحظي للدالة وميل مماس منحناها.", "unit_id": "u6", "page": 154},
    "v-chain": {"id": "v-chain", "term": "قاعدة السلسلة", "definition": "قاعدة اشتقاق الدوال المركبة: (f∘g)′=f′(g)g′.", "unit_id": "u6", "page": 166},
    "v-extremum": {"id": "v-extremum", "term": "القيمة القصوى", "definition": "أكبر أو أصغر قيمة للدالة على فترة أو عند نقطة حرجة.", "unit_id": "u6", "page": 187},
    "v-integral": {"id": "v-integral", "term": "التكامل", "definition": "عملية عكس الاشتقاق وتستخدم أيضاً لحساب المساحات والحجوم.", "unit_id": "u7", "page": 210},
    "v-definite": {"id": "v-definite", "term": "التكامل المحدد", "definition": "تكامل بين حدين يعطي قيمة عددية F(b)−F(a).", "unit_id": "u7", "page": 235},
    "v-revolution": {"id": "v-revolution", "term": "مجسم الدوران", "definition": "مجسم ناتج عن دوران منحنى حول محور، وحجمه π∫f²dx.", "unit_id": "u7", "page": 248}
}
GEOMETRY_LAB = {
    "title": "معمل الرياضيات التفاعلي - الصف الثالث الثانوي",
    "theme_color": "#00a859",
    "default_scene": "lab-math-complex",
    "scenes": [
        {"id": "lab-math-complex", "title": "مستوى أرغاند", "unit_id": "u1", "page": 16, "sim_key": "math_complex", "kind": "2d", "formula": "z = a + bi، |z| = √(a²+b²)", "prompt": "حرك r والزاوية θ ولاحظ أثرهما على موضع العدد المركب.", "controls": [{"id": "r", "label": "القيمة المطلقة r", "min": 1, "max": 10, "step": 1, "default": 5}, {"id": "theta", "label": "الزاوية θ", "min": 0, "max": 360, "step": 5, "default": 45}], "steps": [{"title": "الإسقاط على المحور الحقيقي", "detail": "a = r cos θ", "formula": "a=r cosθ"}, {"title": "الإسقاط على المحور التخيلي", "detail": "b = r sin θ", "formula": "b=r sinθ"}, {"title": "الطول", "detail": "القيمة المطلقة هي طول المتجه من المبدأ.", "formula": "|z|=r"}]},
        {"id": "lab-math-cone", "title": "قطوع المخروط", "unit_id": "u3", "page": 104, "sim_key": "math_cone_sections", "kind": "3d", "formula": "e = PF / PD", "prompt": "غيّر ميل مستوى القطع ولاحظ نوع المنحنى الناتج.", "controls": [{"id": "tilt", "label": "ميل المستوى", "min": 0, "max": 90, "step": 5, "default": 35}], "steps": [{"title": "مستوى مواز لقاعدة المخروط", "detail": "ينتج دائرة.", "formula": "e=0"}, {"title": "مستوى مائل", "detail": "ينتج قطعاً ناقصاً أو مكافئاً أو زائداً حسب الميل.", "formula": "e=PF/PD"}]},
        {"id": "lab-math-ellipse", "title": "القطع الناقص", "unit_id": "u3", "page": 110, "sim_key": "math_ellipse", "kind": "2d", "formula": "x²/a² + y²/b² = 1", "prompt": "غيّر a و b ولاحظ البؤرتين وشكل المنحنى.", "controls": [{"id": "a", "label": "نصف المحور a", "min": 2, "max": 8, "step": 1, "default": 5}, {"id": "b", "label": "نصف المحور b", "min": 1, "max": 7, "step": 1, "default": 3}], "steps": [{"title": "المحور الكبير", "detail": "a هي أكبر نصف محور.", "formula": "a>b"}, {"title": "البؤرتان", "detail": "c² = a² − b²", "formula": "c=√(a²−b²)"}]},
        {"id": "lab-math-hyperbola", "title": "القطع الزائد", "unit_id": "u3", "page": 118, "sim_key": "math_hyperbola", "kind": "2d", "formula": "x²/a² − y²/b² = 1", "prompt": "غيّر a و b ولاحظ الفروع والخطين المقاربين.", "controls": [{"id": "a", "label": "المعلمة a", "min": 1, "max": 6, "step": 1, "default": 2}, {"id": "b", "label": "المعلمة b", "min": 1, "max": 6, "step": 1, "default": 3}], "steps": [{"title": "الفروع", "detail": "الفرق المطلق للبعدين يساوي 2a.", "formula": "|PF₁−PF₂|=2a"}, {"title": "المقاربة", "detail": "y = ±(b/a)x", "formula": "y=±(b/a)x"}]},
        {"id": "lab-math-parabola", "title": "القطع المكافئ", "unit_id": "u3", "page": 124, "sim_key": "math_parabola", "kind": "2d", "formula": "y² = 4px", "prompt": "غيّر p ولاحظ البؤرة والدليل.", "controls": [{"id": "p", "label": "المعلمة p", "min": 1, "max": 6, "step": 1, "default": 2}], "steps": [{"title": "البؤرة", "detail": "F = (p، 0)", "formula": "F=(p،0)"}, {"title": "الدليل", "detail": "x = −p", "formula": "x=−p"}]},
        {"id": "lab-math-space", "title": "القطر الفراغي للمكعب", "unit_id": "u4", "page": 136, "sim_key": "math_3d_pythagoras", "kind": "3d", "formula": "d = a√3", "prompt": "دور المكعب وغيّر ضلعه لترى القطر الفراغي.", "controls": [{"id": "a", "label": "طول الضلع", "min": 1, "max": 10, "step": 1, "default": 4}], "steps": [{"title": "قطر الوجه", "detail": "a√2", "formula": "d_face=a√2"}, {"title": "القطر الفراغي", "detail": "a√3", "formula": "d=a√3"}]},
        {"id": "lab-math-line-plane", "title": "مستقيم ومستوى", "unit_id": "u4", "page": 142, "sim_key": "math_line_plane", "kind": "3d", "formula": "sin θ = |u·n|/(|u||n|)", "prompt": "غيّر زاوية المستقيم مع الطبيعي ولاحظ الزاوية مع المستوى.", "controls": [{"id": "alpha", "label": "الزاوية مع الطبيعي", "min": 0, "max": 90, "step": 5, "default": 40}], "steps": [{"title": "المتجه الطبيعي", "detail": "n يحدد العمود على المستوى.", "formula": "n=(A،B،C)"}, {"title": "الزاوية المطلوبة", "detail": "θ = 90° − α", "formula": "θ=90°−α"}]},
        {"id": "lab-math-dihedral", "title": "زاوية بين مستويين", "unit_id": "u4", "page": 147, "sim_key": "math_dihedral", "kind": "3d", "formula": "cos φ = |n₁·n₂|/(|n₁||n₂|)", "prompt": "دور المستوى الثاني حول خط التقاطع.", "controls": [{"id": "phi", "label": "زاوية الدوران", "min": 0, "max": 120, "step": 5, "default": 60}], "steps": [{"title": "المتجهان الطبيعيان", "detail": "ناتج الجداء يعطي جيب تمام الزاوية.", "formula": "cosφ=|n₁·n₂|/(|n₁||n₂|)"}]},
        {"id": "lab-math-probability", "title": "فضاء العينة", "unit_id": "u5", "page": 79, "sim_key": "math_probability_space", "kind": "2d", "formula": "P(A∪B)=P(A)+P(B)−P(A∩B)", "prompt": "غيّر احتمالي الحدثين والتقاطع.", "controls": [{"id": "pa", "label": "P(A)", "min": 0, "max": 100, "step": 5, "default": 55}, {"id": "pb", "label": "P(B)", "min": 0, "max": 100, "step": 5, "default": 40}, {"id": "inter", "label": "P(A∩B)", "min": 0, "max": 100, "step": 5, "default": 20}], "steps": [{"title": "الجمع", "detail": "اجمع الاحتمالين.", "formula": "P(A)+P(B)"}, {"title": "إزالة التداخل", "detail": "اطرح التقاطع حتى لا يُحسب مرتين.", "formula": "−P(A∩B)"}]},
        {"id": "lab-math-derivative", "title": "مماس المنحنى", "unit_id": "u6", "page": 154, "sim_key": "math_derivative", "kind": "2d", "formula": "f′(x)=lim[f(x+h)−f(x)]/h", "prompt": "حرك نقطة على المنحنى ولاحظ ميل المماس.", "controls": [{"id": "x", "label": "موضع النقطة", "min": 1, "max": 9, "step": 1, "default": 4}], "steps": [{"title": "المنحنى", "detail": "f(x)=x²/8", "formula": "f(x)=x²/8"}, {"title": "المشتقة", "detail": "f′(x)=x/4", "formula": "f′(x)=x/4"}]},
        {"id": "lab-math-integral", "title": "التكامل والمساحة", "unit_id": "u7", "page": 235, "sim_key": "math_integral", "kind": "2d", "formula": "∫ₐᵇf(x)dx=F(b)−F(a)", "prompt": "غيّر الحد العلوي ولاحظ تراكم المساحة.", "controls": [{"id": "b", "label": "الحد العلوي", "min": 1, "max": 10, "step": 1, "default": 6}], "steps": [{"title": "الدالة", "detail": "f(x)=x/4", "formula": "f(x)=x/4"}, {"title": "المساحة", "detail": "A=b²/8", "formula": "A=b²/8"}]},
        {"id": "lab-math-area", "title": "المساحة بين منحنيين", "unit_id": "u7", "page": 244, "sim_key": "math_area_between", "kind": "2d", "formula": "A=∫ₐᵇ|f(x)−g(x)|dx", "prompt": "غيّر الحد العلوي ولاحظ الفرق بين المنحنيين.", "controls": [{"id": "b", "label": "الحد العلوي", "min": 1, "max": 10, "step": 1, "default": 5}], "steps": [{"title": "المنحنى العلوي", "detail": "f(x)=2", "formula": "f(x)=2"}, {"title": "المنحنى السفلي", "detail": "g(x)=x/4", "formula": "g(x)=x/4"}]},
        {"id": "lab-math-revolution", "title": "مجسم الدوران", "unit_id": "u7", "page": 248, "sim_key": "math_revolution", "kind": "3d", "formula": "V=π∫ₐᵇ[f(x)]²dx", "prompt": "غيّر عدد الأقراص لتراكم حجم المجسم.", "controls": [{"id": "n", "label": "عدد الأقراص", "min": 4, "max": 20, "step": 1, "default": 10}], "steps": [{"title": "القرص", "detail": "نصف قطره f(x) وسمكه dx", "formula": "dV=π[f(x)]²dx"}, {"title": "الحجم", "detail": "مجموع الأقراص يقترب من التكامل.", "formula": "V=π∫[f(x)]²dx"}]}
    ]
}
for _scene in GEOMETRY_LAB["scenes"]:
    while len(_scene["steps"]) < 3:
        _step_no = len(_scene["steps"]) + 1
        _scene["steps"].append({"title": f"الخلاصة والتطبيق {_step_no}", "detail": _scene["prompt"], "formula": _scene["formula"]})

QUESTION_SETS = {
    "u1": [
        ("ما الجزء الحقيقي في العدد 3 + 2i؟", "3", [("2", "هذا الجزء التخيلي، وليس الحقيقي."), ("5", "هذا مجموع المكوّنين، وليس الجزء الحقيقي."), ("√13", "هذه القيمة المطلقة للعدد، وليس جزأه الحقيقي.")], "الجزء الحقيقي هو المعامل الذي لا يضرب في i."),
        ("ما قيمة i²؟", "−1", [("1", "هذا ينتج من نسيان تعريف الوحدة التخيلية."), ("0", "الوحدة التخيلية ليست صفراً."), ("i", "تربيع i يعطي عدداً حقيقياً سالباً.")], "بالتعريف i² = −1."),
        ("احسب |3 + 4i|.", "5", [("7", "جمع المكوّنات لا يعطي القيمة المطلقة."), ("25", "هذا مربع القيمة المطلقة قبل أخذ الجذر."), ("√7", "استخدمت المجموع بدل مجموع المربعات.")], "|z| = √(3² + 4²) = 5."),
        ("احسب (2 + 3i) + (1 − i).", "3 + 2i", [("3 + 4i", "طرح 1 بدل جمعه في الجزء التخيلي."), ("1 + 2i", "نسيت جمع الجزء الحقيقي 2 + 1."), ("−1 + 4i", "خلطت بين الجمع والطرح.")], "نجمع الأجزاء الحقيقية والتخيلية على حدة."),
        ("احسب (2 + i)(1 − i).", "3 − i", [("1 − i", "نسيت حد i² عند التبسيط."), ("3 + i", "أخطأت في إشارة الحد التخيلي."), ("2 − 2i", "حذفت بعض حدود الضرب.")], "الضرب يعطي 2 − 2i + i − i² = 3 − i."),
        ("ما مرافق العدد 4 − 5i؟", "4 + 5i", [("−4 − 5i", "هذا عكس العدد، وليس مرافقه."), ("4 − 5i", "المرافق يغيّر إشارة الجزء التخيلي."), ("5 − 4i", "بادل بين الجزأين الحقيقي والتخيلي.")], "نغيّر إشارة الجزء التخيلي فقط."),
        ("ما سعة العدد 1 + i بالدرجات؟", "45°", [("30°", "tan θ = 1، فالزاوية 45° لا 30°."), ("90°", "الزاوية 90° تعني أن الجزء الحقيقي صفر."), ("135°", "النقطة في الربع الأول لا الثاني.")], "tan θ = 1/1، والنقطة تقع في الربع الأول."),
        ("ما القيمة المطلقة للعدد 1 + √3 i؟", "2", [("√3", "هذا الجزء التخيلي فقط."), ("4", "هذا مربع القيمة المطلقة."), ("√2", "استخدمت 1² + 1² بدل 1² + (√3)².")], "|z| = √(1 + 3) = 2."),
        ("اكتب −1 + i بالصيغة القطبية.", "√2(cos135° + i sin135°)", [("√2(cos45° + i sin45°)", "هذه زاوية الربع الأول، والعدد في الربع الثاني."), ("2(cos135° + i sin135°)", "القيمة المطلقة √2 وليست 2."), ("√2(cos225° + i sin225°)", "الزاوية 225° تعطي −1 − i.")], "r = √2 والزاوية 135° لأن النقطة في الربع الثاني."),
        ("احسب |6 + 8i|.", "10", [("14", "جمع المكوّنات لا يعطي الطول."), ("48", "هذا حاصل ضرب المكوّنين."), ("√10", "استخدمت المجموع بدل مجموع المربعات.")], "|z| = √(36 + 64) = 10."),
        ("اكتب 5(cos60° + i sin60°) بالصيغة الجبرية.", "5/2 + (5√3/2)i", [("5 + √3i", "لم تضرب r في cosθ و sinθ."), ("5/2 + 5i", "الجزء التخيلي يجب أن يكون (5√3)/2."), ("5√3 + (5/2)i", "بادل بين الإسقاطين.")], "a = 5cos60° = 5/2 و b = 5sin60° = 5√3/2."),
        ("احسب 2i + (−3i).", "−i", [("i", "أخطأت في إشارة المجموع."), ("5i", "جمعت القيم المطلقة بدل الإشارات."), ("−5i", "جمعت بوصفهما سالبين.")], "2i − 3i = −i."),
        ("ما المسافة بين 1 + 2i و 4 + 6i؟", "5", [("7", "جمعت الفروق بدل استخدام فيثاغورس."), ("√5", "استخدمت فرقاً واحداً فقط."), ("25", "هذا مربع المسافة.")], "المسافة = |(4+6i)−(1+2i)| = |3+4i| = 5."),
        ("إذا كان |a + bi| = 0 فماذا ينتج؟", "a = 0 و b = 0", [("a = 0 فقط", "يجب أن يصفر الجزء التخيلي أيضاً."), ("b = 0 فقط", "يجب أن يصفر الجزء الحقيقي أيضاً."), ("a = b = 1", "القيمة المطلقة حينها √2 لا صفر.")], "مجموع مربعين لا يساوي صفراً إلا إذا كان كلاهما صفراً."),
        ("احسب (1 + i)².", "2i", [("2", "نسيت أن 2i متبقٍ بعد إلغاء i²."), ("1 + 2i", "حذفت حد i² خطأً."), ("0", "النتيجة ليست صفراً؛ i² = −1.")], "(1+i)² = 1+2i+i² = 2i."),
    ],
    "u2": [
        ("احسب (cos30° + i sin30°)⁴.", "cos120° + i sin120°", [("cos34° + i sin34°", "قاعدة دي موافر تضرب الزاوية في الأس لا تجمعها."), ("cos120° − i sin120°", "إشارة الجزء التخيلي لا تتغير في الرفع."), ("cos60° + i sin60°", "4 × 30° = 120° وليس 60°.")], "نضرب الزاوية في الأس: nθ = 120°."),
        ("إذا كان z = 2(cos30° + i sin30°) فما z³؟", "8(cos90° + i sin90°)", [("6(cos90° + i sin90°)", "القيمة المطلقة تُرفع للأس: 2³ = 8."), ("8(cos10° + i sin10°)", "الزاوية تُضرب في الأس لا تُقسم."), ("2(cos90° + i sin90°)", "نسيت رفع r إلى القوة الثالثة.")], "z³ = 2³(cos 3×30° + i sin 3×30°)."),
        ("كم جذراً نونياً للعدد 1 من الدرجة الخامسة؟", "5", [("4", "عدد الجذور يساوي درجة الجذر لا نصفها."), ("10", "لا تضاعف الدرجة."), ("1", "لكل درجة n يوجد n جذراً مركباً.")], "معادلة z⁵ = 1 لها خمسة جذور مركبة."),
        ("ما الفرق في الزاوية بين جذرين متجاورين من جذور z⁶؟", "60°", [("90°", "الفرق هو 360°/6."), ("45°", "استخدمت 360°/8 بدل 360°/6."), ("30°", "نصف القيمة الصحيحة.")], "الفرق = 2π/n = 360°/6 = 60°."),
        ("احسب C(6,2).", "15", [("12", "حساب المعامل خاطئ؛ (6×5)/(2×1)=15."), ("30", "نسيت القسمة على 2!."), ("20", "هذه قيمة C(6,3).")], "C(6,2) = 6!/(2!4!) = 15."),
        ("ما معاملات (a+b)⁴؟", "1، 4، 6، 4، 1", [("1، 3، 3، 1", "هذه معاملات (a+b)³."), ("1، 4، 4، 1", "حذفت المعامل الأوسط 6."), ("1، 5، 10، 5، 1", "هذه معاملات الأس الخامس.")], "من مثلث باسكال للصف الرابع."),
        ("ما الحد الأوسط في توسعة (x+y)⁶؟", "20x³y³", [("15x²y⁴", "هذا ليس الحد الأوسط للأس 6."), ("6x³y³", "نسيت حساب C(6,3)=20."), ("20x⁴y²", "الأسود يجب أن يكونا 3 و 3.")], "الحد الأوسط C(6,3)x³y³ = 20x³y³."),
        ("احسب (1 + i)⁴.", "−4", [("4", "الزاوية 180° تعطي إشارة سالبة."), ("2", "القيمة المطلقة (√2)⁴ = 4."), ("−2", "نسيت رفع القيمة المطلقة للأس الرابع.")], "|1+i|=√2 والزاوية 45°، إذن النتيجة 4(cos180°+i sin180°)=−4."),
        ("ما قيمة r لأحد الجذور التكعيبية لـ 8(cos90° + i sin90°)؟", "2", [("8", "جذر القيمة المطلقة يُؤخذ: 8^(1/3)=2."), ("√8", "هذا جذر تربيعي لا تكعيبي."), ("6", "لا تُقسم القيمة المطلقة على الأس.")], "نصف قطر الجذور هو r^(1/n) = 2."),
        ("ما معامل x² في (1+x)⁵؟", "10", [("5", "هذا معامل x فقط."), ("20", "هذا معامل x³."), ("15", "حساب C(5,2) خاطئ.")], "المعامل C(5,2)=10."),
        ("كم عدد حدود توسعة (a+b)⁹؟", "10", [("9", "عدد الحدود n+1."), ("8", "طرحت واحداً بدل إضافة واحد."), ("11", "أضفت اثنين بدل واحد.")], "عدد الحدود = 9 + 1 = 10."),
        ("ما الصيغة المناسبة لتطبيق دي موافر مباشرة؟", "r(cosθ + i sinθ)", [("a + bi فقط", "تحتاج تحويلاً أولاً إلى الصيغة القطبية."), ("عدد حقيقي فقط", "المبرهنة للأعداد المركبة."), ("أي صيغة بزاوية بالراديان فقط", "الدرجات مقبولة طالما متسقة.")], "الصيغة القطبية تجعل الرفع إلى قوة بسيطاً."),
        ("احسب (−1 + i)².", "−2i", [("2i", "أخطأت في إشارة الحد التخيلي الناتج."), ("−2", "الحد 2i لا يلغي عند التربيع."), ("0", "القيمة المطلقة ليست صفراً.")], "(−1+i)² = 1−2i+i² = −2i."),
        ("احسب C(5,3).", "10", [("5", "هذا C(5,1)."), ("15", "هذا C(6,2)."), ("20", "حساب خاطئ للمعامل.")], "C(5,3)=C(5,2)=10."),
        ("ما مجموع معاملات (1+1)⁸؟", "256", [("128", "هذه 2⁷ لا 2⁸."), ("64", "هذه 2⁶."), ("8", "هذا الأس نفسه، لا مجموع المعاملات.")], "مجموع المعاملات = (1+1)⁸ = 2⁸ = 256."),
    ],
    "u3": [
        ("في القطع x²/16 + y²/9 = 1، ما طول المحور الكبير؟", "8", [("6", "هذا طول المحور الصغير."), ("3", "هذا نصف المحور الصغير."), ("4", "هذا نصف المحور الكبير.")], "a=4 إذن طول المحور الكبير 2a=8."),
        ("ما بُعد البؤرة عن المركز في x²/16 + y²/9 = 1؟", "√7", [("√5", "طرحت 16−9 خطأً."), ("7", "هذا c² وليس c."), ("5", "جمع المقامين بدل طرحهما.")], "c=√(16−9)=√7."),
        ("ما خطا مقاربة القطع x²/9 − y²/16 = 1؟", "y = ±(4/3)x", [("y = ±(3/4)x", "عكست b/a."), ("y = ±4x", "نسيت القسمة على a."), ("y = ±3x", "استخدمت a بدل b/a.")], "للقطع الأفقي y=±(b/a)x=±(4/3)x."),
        ("في y² = 20x، ما قيمة p؟", "5", [("20", "المعطى هو 4p لا p."), ("10", "قسمت على 2 بدل 4."), ("√20", "لا يوجد جذر هنا.")], "4p=20 إذن p=5."),
        ("أي قطع مخروطي انحرافه e أكبر من 1؟", "القطع الزائد", [("القطع الناقص", "القطع الناقص له e<1."), ("القطع المكافئ", "القطع المكافئ له e=1."), ("الدائرة", "الدائرة حالة خاصة بـ e=0.")], "e>1 يعطي القطع الزائد."),
        ("أي قطع مخروطي انحرافه e يساوي 1؟", "القطع المكافئ", [("القطع الناقص", "للقطع الناقص e<1."), ("القطع الزائد", "للقطع الزائد e>1."), ("الدائرة", "للدائرة e=0.")], "e=1 هو تعريف القطع المكافئ."),
        ("في x²/25 + y²/9 = 1، ما c؟", "4", [("5", "هذا a وليس c."), ("3", "هذا b."), ("√34", "جمعت المقامين بدل طرحهما.")], "c=√(25−9)=4."),
        ("إذا كان a=3 لقطع زائد، فما طول محوره القطعي؟", "6", [("3", "هذا نصف المحور."), ("9", "هذا a²."), ("8", "لا علاقة له بالمعطى.")], "طول المحور القطعي = 2a = 6."),
        ("ما دليل القطع y² = 12x؟", "x = −3", [("x = 3", "الدليل يقع في الجهة المعاكسة للبؤرة."), ("y = −3", "محور التماثل أفقي، فالدليل مستقيم رأسي."), ("x = −6", "12 = 4p إذن p=3 لا 6.")], "4p=12، p=3، والدليل x=−p."),
        ("ما مركز القطع x²/4 + y²/9 = 1؟", "(0، 0)", [("(2، 3)", "هذه قيم المقامات، لا إحداثيات المركز."), ("(4، 9)", "المقامات ليست إحداثيات."), ("(0، 1)", "لا يوجد إزاحة في المعادلة.")], "لا توجد حدود (x−h) أو (y−k)، فالمركز المبدأ."),
        ("ما مركز (x−1)²/9 + (y+2)²/4 = 1؟", "(1، −2)", [("(−1، 2)", "عكست الإشارتين."), ("(1، 2)", "y+2 تعطي k=−2."), ("(−1، −2)", "x−1 تعطي h=1.")], "المركز (h، k) = (1، −2)."),
        ("أي اتجاه يفتح له القطع x²/9 − y²/4 = 1؟", "أفقياً", [("رأسياً", "الحد الموجب هو x²، إذن المحور أفقي."), ("لأعلى فقط", "القطع الزائد له فرعان متقابلان."), ("دائرياً", "الإشارة سالبة في y²، فليس دائرة.")], "الإشارة الموجبة أمام x² تعني محوراً قطعياً أفقياً."),
        ("ما انحراف الدائرة؟", "0", [("1", "هذا انحراف القطع المكافئ."), ("∞", "لا يحدث للدائرة."), ("0.5", "ينتمي لقطع ناقص غير دائري.")], "الدائرة حالة خاصة من القطع الناقص بـ e=0."),
        ("ما رأس القطع (y−1)² = 8(x−2)؟", "(2، 1)", [("(1، 2)", "عكست الإحداثيات."), ("(−2، 1)", "x−2 تعطي h=2 لا −2."), ("(2، −1)", "y−1 تعطي k=1.")], "الصيغة (y−k)²=4p(x−h) تعطي الرأس (2،1)."),
        ("ما بؤرة القطع y² = 8x؟", "(2، 0)", [("(0، 2)", "بادل بين الإحداثيات."), ("(4، 0)", "8 = 4p إذن p=2."), ("(8، 0)", "8 هي 4p وليست p.")], "4p=8، p=2، فالبؤرة (2،0)."),
    ],
    "u4": [
        ("ما المتجه الطبيعي للمستوى Ax + By + Cz + D = 0؟", "(A، B، C)", [("(A، B، D)", "الثابت D لا يدخل المتجه الطبيعي."), ("(−D، −B، −A)", "ترتيب وإشارات خاطئة."), ("(1، 1، 1)", "غير صحيح إلا إذا كانت A=B=C=1.")], "معاملات x و y و z تمثل المتجه الطبيعي."),
        ("ما مسافة نقطة من مستوى؟", "|Ax₀+By₀+Cz₀+D| / √(A²+B²+C²)", [("|Ax₀+By₀+Cz₀+D| / (A²+B²+C²)", "حذفت الجذر من المقام."), ("|Ax₀+By₀+Cz₀+D| / D", "لا تُقسم على الثابت."), ("Ax₀+By₀+Cz₀+D فقط", " يجب أخذ القيمة المطلقة والقسمة على طول الطبيعي.")], "المسافة هي الإسقاط العمودي مقسوماً على |n|."),
        ("ما طول القطر الفراغي لمكعب ضلعه a؟", "a√3", [("a√2", "هذا قطر الوجه."), ("2a", "هذا ضعف الضلع."), ("3a", "لا يُجمع الضلع ثلاث مرات.")], "بفيثاغورس مرتين: d=√(a²+a²+a²)=a√3."),
        ("إذا كانت زاوية مستقيم مع الطبيعي 30°، فما زاويته مع المستوى؟", "60°", [("30°", "الزاويتان ليستا متساويتين."), ("120°", "الزاوية مع المستوى حادة مكمّلة."), ("45°", "المكمّل لـ 30° هو 60°.")], "θ = 90° − 30° = 60°."),
        ("متى يكون مستويان متعامدين؟", "عندما n₁·n₂ = 0", [("عندما n₁ = n₂", "هذا يعني مستويين متوازيين."), ("عندما n₁ = 2n₂", "مضاعفة المتجه تعني توازياً."), ("عندما |n₁| = |n₂|", "تساوي الطولين لا يحدد الزاوية.")], "تعامد المتجهين الطبيعيين يعطي تعامد المستويين."),
        ("ما cosφ بين المستوى xy والمستوى xz؟", "0", [("1", "المتجهان (0,0,1) و (0,1,0) متعامدان."), ("−1", "ليسا متعاكسين."), ("1/2", "الزاوية 90° لا 60°.")], "n₁=(0,0,1)، n₂=(0,1,0)، جيب تمام الزاوية صفر."),
        ("ما مسافة النقطة (1،2،5) من المستوى x = 3؟", "2", [("3", "هذا موضع المستوى من المبدأ."), ("4", "حسبت الإحداثي الخاطئ."), ("√30", "استخدمت طول متجه النقطة.")], "المسافة = |1−3| = 2."),
        ("ما زاوية المستقيم باتجاه (1،0،0) مع المستوى z = 0؟", "0°", [("90°", "هذا مع المتجه الطبيعي لا مع المستوى."), ("45°", "لا يوجد ميل رأسي."), ("180°", "الزاوية مع مستوى لا تُقاس هكذا.")], "المتجه موازٍ للمستوى، فالزاوية صفر."),
        ("ما الزاوية بين المستويين xy و xz؟", "90°", [("0°", "المستويان مختلفان و متعامدان."), ("45°", "لا يوجد ميل بمقدار 45°."), ("180°", "ليسا مستوى واحداً بعكس الاتجاه.")], "المتجهان الطبيعيان متعامدان."),
        ("ما معادلة المستوى المار بالمبدأ وبطبيعي (0،0،1)؟", "z = 0", [("x = 0", "هذا طبيعيته (1،0،0)."), ("y = 0", "هذا طبيعيته (0،1،0)."), ("x + y = 1", "لا يمر بالمبدأ ولا طبيعيته المطلوبة.")], "المعادلة 0x+0y+1z+0=0."),
        ("ما معادلة مستقيم يمر بـ P واتجاهه u؟", "r = P + tu", [("r = P·u", "هذا ناتج جداء لا معادلة مستقيم."), ("r = P/t", "لا تمثل هذه معادلة خط مستقيم."), ("r = u − tP", "النقطة والاتجاه معكوسان.")], "المعادلة المتجهية للمستقيم هي r=P+tu."),
        ("ما مسافة المبدأ من المستوى 3x + 4y + 12z − 13 = 0؟", "1", [("13", "هذا البسط قبل القسمة."), ("12", "هذا أكبر معامل."), ("1/13", "قلبت النسبة.")], "|−13|/√(9+16+144)=13/13=1."),
        ("إذا كان مستقيم موازياً لمستوى، فما زاويته مع الطبيعي؟", "90°", [("0°", "هذه الزاوية مع المستوى."), ("45°", "لا يوجد ميل رأسي."), ("180°", "الزاوية مع طبيعي扼 مستوى تكون قائمة.")], "الموازي للمستوى عمودي على متجهه الطبيعي."),
        ("ما قطر وجه مكعب ضلعه a؟", "a√2", [("a√3", "هذا القطر الفراغي."), ("2a", "ضعف الضلع."), ("a/√2", "قلبت العلاقة.")], "قطر الوجه = √(a²+a²)=a√2."),
        ("ما مسافة (1،1،1) من المستوى 2x − y + 2z − 4 = 0؟", "1/3", [("1", "المقام √(4+1+4)=3."), ("3", "هذا المقام لا المسافة."), ("2/3", "حساب البسط خاطئ؛ البسط 1.")], "|2−1+2−4|/3 = 1/3."),
    ],
    "u5": [
        ("إذا كان P(A)=0.3 فما P(Aᶜ)؟", "0.7", [("0.3", "المكمّل ليس الحدث نفسه."), ("0.5", "لا تُقسم الاحتمال على 2."), ("1.3", "الاحتمال لا يتجاوز 1.")], "P(Aᶜ)=1−P(A)=0.7."),
        ("إذا كان A و B متنافيين، P(A)=0.4 و P(B)=0.3، فما P(A∪B)؟", "0.7", [("0.12", "قاعدة الضرب للحدثين المستقلين، لا الجمع للمتنافيين."), ("0.1", "طرحت بدل جمعت."), ("1", "المجموع 0.7 وليس يقيناً.")], "للتنافي P(A∪B)=P(A)+P(B)."),
        ("إذا كان A و B مستقلين، P(A)=0.5 و P(B)=0.2، فما P(A∩B)؟", "0.1", [("0.7", "هذا الجمع، لا التقاطع."), ("0.3", "طرحت بدل ضربت."), ("0.25", "استخدمت P(B)=0.5.")], "للاستقلال P(A∩B)=P(A)P(B)=0.1."),
        ("إذا كان P(A)=0.5، P(B)=0.4 و P(A∩B)=0.2، فما P(A∪B)؟", "0.7", [("0.9", "حسبت التقاطع مرتين."), ("0.3", "طرحت التقاطع من حد واحد فقط."), ("1.1", "الاحتمال لا يتجاوز 1.")], "0.5+0.4−0.2=0.7."),
        ("إذا كان P(A∩B)=0.2 و P(B)=0.5، فما P(A|B)؟", "0.4", [("0.1", "ضربت بدل قسمت."), ("0.7", "جمعت بدل قسمت."), ("2.5", "قلبت البسط والمقام.")], "P(A|B)=0.2/0.5=0.4."),
        ("ما مجموع احتمالات كل النتجات المتنافية في فضاء العينة؟", "1", [("0", "هذا مستحيل لمجموع كامل."), ("∞", "الاحتمال محدود."), ("يعتمد على التجربة", "المجموع دائماً 1.")], "مجموع فضاء العينة يساوي 1."),
        ("عند رمي عملة مرتين، ما احتمال HH؟", "1/4", [("1/2", "هذا احتمال نتيجة واحدة في رمية واحدة."), ("1/3", "فضاء العينة له 4 نتجات متساوية."), ("1/8", "هذا لثلاث رميات.")], "النتجات: HH, HT, TH, TT، إذن 1/4."),
        ("عند رمي نرد عادل، ما احتمال ظهور عدد زوجي؟", "1/2", [("1/6", "هذا احتمال رقم واحد."), ("1/3", "الأعداد الزوجية 2 و 4 و 6 من أصل 6."), ("2/3", "هذا احتمال الفردي أو الزوجي معاً خطأً.")], "3 نتجات زوجية من 6."),
        ("في 5 تجارب برنولي p=0.5، ما احتمال نجاحين بالضبط؟", "10/32", [("5/32", "نسيت C(5,2)=10."), ("10/16", "المقام يجب أن يكون 2⁵=32."), ("1/32", "هذا احتمال حالة واحدة فقط.")], "C(5,2)(0.5)²(0.5)³=10/32."),
        ("إذا كان A و B مستقلين، فما P(A|B)؟", "P(A)", [("P(A∩B)", "هذا احتمال تقاطع، لا شرطي."), ("0", "الشرط لا يلغي الاحتمال."), ("1−P(A)", "هذا احتمال المكمّل.")], "الاستقلال يعني أن الشرط لا يغيّر الاحتمال."),
        ("أي علاقة صحيحة دائماً؟", "P(A∩B) ≤ P(A)", [("P(A∩B)=P(A) دائماً", "يحدث فقط إذا B يضم A."), ("P(A∩B)>P(A)", "التقاطع لا يمكن أن يتجاوز أحد الحدثين."), ("P(A∩B)=0 دائماً", "فقط للمتنافيين.")], "التقاطع جزء من A، فاحتماله لا يتجاوز احتمال A."),
        ("السحب دون إرجاع يجعل الحدثين", "غير مستقلين", [("مستقلين", "السحب يغيّر احتمال الثاني."), ("متنافيين دائماً", "قد يحصل كلاهما في سحبتين."), ("احتمال كل منهما 1", "ليس بالضرورة.")], "تغيّر فضاء العينة بعد السحب يلغي الاستقلال."),
        ("متى يساوي P(A∪B)=P(A)+P(B)؟", "عند تنافي A و B", [("عند استقلالهما", "الاستقلال يعطي ضرب التقاطع لا إلغاءه."), ("عند تساويهما", "لا علاقة لذلك."), ("عند كمالهما", "التكامل يعطي مجموع 1، لكن التقاطع معدوم فقط عند التنافي.")], "يُحذف الحد P(A∩B) فقط إذا كان التقاطع صفراً."),
        ("ما شرط التوزيع ذي الحدين؟", "تجارب مستقلة واحتمال نجاح ثابت", [("سحب مع إرجاع فقط", "ليس شرطاً حصرياً."), ("احتمال متغير في كل تجربة", "يجب أن يكون p ثابتاً."), ("تجارب مؤثرة", "يجب أن تكون مستقلة.")], "التوزيع ذو الحدين يتطلب n تجارب مستقلة و p ثابت."),
        ("في تجربتين مستقلتين p=0.5، ما احتمال نجاح واحدة على الأقل؟", "0.75", [("0.5", "هذا احتمال نجاح واحدة بالضبط في تجربة واحدة."), ("0.25", "هذا احتمال الفشل في التجربتين."), ("1", "لا يوجد يقين بالنجاح.")], "1−P(فشلان)=1−0.25=0.75."),
    ],
    "u6": [
        ("ما مشتقة x⁵؟", "5x⁴", [("x⁴", "نسيت ضرب الأس الأصلي."), ("5x⁵", "لم ينقص الأس."), ("4x⁴", "استخدمت ناتج التنقيص بدل الأس الأصلي.")], "(xⁿ)′=nxⁿ⁻¹."),
        ("ما مشتقة الثابت 7؟", "0", [("7", "الثابت لا يتغير."), ("1", "مشتقة x هي 1 لا مشتقة الثابت."), ("غير معرفة", "مشتقة الثابت معرفة وتساوي صفراً.")], "معدل تغير الثابت صفر."),
        ("إذا كان f(x)=x³، فما f′(2)؟", "12", [("8", "هذا f(2) لا المشتقة."), ("6", "حسبت 3×2 بدل 3×2²."), ("3", "هذا الأس فقط.")], "f′(x)=3x²، إذن f′(2)=12."),
        ("ما مشتقة x² sinx باستخدام قاعدة الجداء؟", "2x sinx + x² cosx", [("2x cosx", "حذفت حداً من قاعدة الجداء."), ("x² cosx فقط", "نسيت مشتقة العامل الأول."), ("2x sinx فقط", "نسيت مشتقة العامل الثاني.")], "(uv)′=u′v+uv′."),
        ("ما مشتقة (3x+1)⁴؟", "12(3x+1)³", [("4(3x+1)³", "نسيت مشتقة الداخل 3."), ("3(3x+1)⁴", "لم تنقص الأس."), ("(3x+1)³", "حذفت العاملين 4 و 3.")], "قاعدة السلسلة: 4(3x+1)³×3."),
        ("ما مشتقة 1/x؟", "−1/x²", [("1/x²", "أخطأت في الإشارة."), ("−1/x", "لم تطبق قاعدة القوة بشكل صحيح."), ("ln x", "هذا تكامل 1/x.")], "1/x = x⁻¹، فمشتقتها −x⁻²."),
        ("ما مشتقة √x؟", "1/(2√x)", [("1/√x", "نسيت العامل 2."), ("2√x", "هذا تكامل تقريبي خاطئ."), ("√x/2", "ليست الصيغة الصحيحة.")], "√x = x^(1/2)، فالمشتقة (1/2)x^(−1/2)."),
        ("ما ميل مماس f(x)=x² عند x=3؟", "6", [("3", "هذا موضع النقطة لا الميل."), ("9", "هذا قيمة الدالة."), ("2", "هذا الأس.")], "f′(x)=2x، إذن f′(3)=6."),
        ("ما النقطة الحرجة لـ f(x)=x²−6x+1؟", "x = 3", [("x = 6", "حللت المعادلة خطأً."), ("x = 1", "هذا الثابت."), ("x = −3", "أخطأت في إشارة b.")], "f′(x)=2x−6=0، إذن x=3."),
        ("ماذا يعني f″(x)>0 عند نقطة حرجة؟", "قيمة صغرى محلية", [("قيمة كبرى محلية", "التقعر للأعلى يعطي صغرى."), ("نقطة انعطاف دائماً", "تحتاج تغيّر إشارة المشتقة الثانية."), ("المشتقة الأولى معدومة دائماً", "ليس شرطاً كافياً.")], "اختبار المشتقة الثانية: f″>0 يعطي قيمة صغرى."),
        ("للدالة f(x)=x² على [1،4]، ما c في نظرية القيمة المتوسطة؟", "2.5", [("2", "ميل القطرة 5، و2c=5."), ("3", "ليس داخل الحل الصحيح."), ("5", "هذا ميل القطرة لا c.")], "(16−1)/(4−1)=5، و f′(c)=2c=5، إذن c=2.5."),
        ("ما مشتقة 5x³ − 2x؟", "15x² − 2", [("15x²", "نسيت مشتقة −2x."), ("5x³ − 2", "لم تشتق الحد الأول."), ("15x² + 2", "أخطأت في إشارة مشتقة −2x.")], "نشتق كل حد على حدة."),
        ("ما مشتقة (x+2)²؟", "2(x+2)", [("2x + 2", "التوسيع يعطي x²+4x+4، ومشتقته 2x+4."), ("(x+2)", "نسيت ضرب الأس."), ("2", "هذا الأس فقط.")], "قاعدة السلسلة تعطي 2(x+2)×1."),
        ("ماذا تمثل مشتقة الموضع بالنسبة للزمن؟", "السرعة", [("التكامل", "التكامل يعطي الموضع من السرعة."), ("التسارع", "التسارع مشتقة السرعة."), ("الزمن", "الزمن هو المتغير المستقل.")], "v(t)=ds/dt."),
        ("ما مماس f(x)=x² عند x=1؟", "y − 1 = 2(x − 1)", [("y = 2x", "هذا y=2x، لا يمر بنقطة (1،1)."), ("y − 1 = x − 1", "الميل يجب أن يكون 2."), ("y = x²", "هذا المنحنى نفسه.")], "الميل f′(1)=2، ويمر بـ (1،1)."),
    ],
    "u7": [
        ("ما ∫x³dx؟", "x⁴/4 + C", [("3x² + C", "هذه مشتقة x³ لا تكاملها."), ("x⁴ + C", "نسيت القسمة على الأس الجديد."), ("x⁴/3 + C", "قسمت على الأس القديم.")], "∫xⁿdx=xⁿ⁺¹/(n+1)+C."),
        ("ما ∫5dx؟", "5x + C", [("5 + C", "تكامل الثابت يعطي الثابت مضروباً في x."), ("x⁵/5 + C", "خلطت بين x⁵ والثابت 5."), ("0", "مشتقة الثابت صفر، لا تكامله.")], "∫k dx = kx + C."),
        ("ما ∫(2x+1)dx؟", "x² + x + C", [("x² + C", "نسيت تكامل الثابت 1."), ("2x² + x + C", "∫2x = x² لا 2x²."), ("x² + 1 + C", "∫1 = x وليس 1.")], "نكامل كل حد على حدة."),
        ("ما ∫₁³ x²dx؟", "26/3", [("9", "هذا 3²، لا التكامل."), ("26", "نسيت القسمة على 3."), ("8/3", "حسبت 3³−1 خطأً.")], "[x³/3]₁³=(27−1)/3=26/3."),
        ("ما ∫₀² 2xdx؟", "4", [("2", "هذا حاصل الضرب 2×1."), ("8", "حسبت 2³/1."), ("1", "نسيت الحدود.")], "[x²]₀²=4."),
        ("ما نص مبرهنة التحليل الأساسية للتكامل المحدد؟", "∫ₐᵇf(x)dx = F(b) − F(a)", [("F(a) − F(b)", "عكست الإشارة."), ("F(a) + F(b)", "ال طرح هو الصحيح."), ("f(b) − f(a)", "نستخدم المضاد F لا الدالة f.")], "التكامل المحدد = الفرق بين قيم المضاد عند الحدين."),
        ("لماذا لا يظهر ثابت التكامل C في التكامل المحدد؟", "لأنه يُلغى عند الطرح", [("لأنه يساوي صفراً دائماً", "C اختياري وليس صفراً بالضرورة."), ("لأن التكامل المحدد لا يملك مضاداً", "له مضاد، لكن الطرح يُلغي C."), ("لأن الحدود تجعله 1", "لا علاقة لهذا.")], "(F(b)+C)−(F(a)+C)=F(b)−F(a)."),
        ("ما المساحة تحت y=x من 0 إلى 2؟", "2", [("4", "هذا مربع الحد الأعلى."), ("1", "هذا نصف الحد الأعلى فقط."), ("8", "حسبت تكامل 2x.")], "∫₀²x dx=[x²/2]₀²=2."),
        ("ما ∫₀¹ x²dx؟", "1/3", [("1", "نسيت القسمة على 3."), ("3", "عكست القسمة."), ("2/3", "حسبت حداً آخر.")], "[x³/3]₀¹=1/3."),
        ("ما ∫(x²+3x)dx؟", "x³/3 + 3x²/2 + C", [("x³/3 + 3x² + C", "∫3x = 3x²/2."), ("x³ + 3x²/2 + C", "∫x² = x³/3."), ("2x + 3 + C", "هذا لا علاقة له بالتكامل.")], "نطبق خطية التكامل وقاعدة القوة."),
        ("ما صيغة حجم مجسم الدوران حول محور x؟", "V = π∫ₐᵇ[f(x)]²dx", [("V = ∫ₐᵇf(x)dx", "ينقص مربع نصف القطر وπ."), ("V = π∫ₐᵇf(x)dx", "يجب تربيع f(x)."), ("V = 2π∫ₐᵇf(x)dx", "هذه صيغة أخرى غير صحيحة هنا.")], "كل قرص حجمه π[f(x)]²dx."),
        ("ما حجم دوران y=x حول محور x من 0 إلى 1؟", "π/3", [("π", "نسيت التكامل الصحيح."), ("π/2", "حسبت ∫x بدل ∫x²."), ("3π", "عكست القسمة.")], "π∫₀¹x²dx=π/3."),
        ("ما قيمة ∫ₐᵇf(x)dx + ∫ᵇₐf(x)dx؟", "0", [("2∫ₐᵇf(x)dx", "الحدود المعكوسة تعطي الإشارة المعاكسة."), ("F(a)", "ليس طرفاً واحداً."), ("غير معرفة", "العلاقة معرفة.")], "تبديل الحدود يغير إشارة التكامل."),
        ("ما المساحة بين f(x)=2 و g(x)=x/2 من 0 إلى 2؟", "3", [("2", "حسبت مستطيلاً فقط."), ("4", "حسبت f(2)×2 دون طرح المثلث."), ("1", "هذا نصف المساحة.")], "∫₀²(2−x/2)dx=3."),
        ("إذا كانت f فردية على [−a،a]، فما ∫₋ₐᵃf(x)dx؟", "0", [("2∫₀ᵃf(x)dx", "هذه صحيحة للدوال الزوجية."), ("مساحة موجبة دائماً", "السالب والموجب يلغيان."), ("يعتمد على a", "النتيجة صفر لأي a.")], "تكامل الدالة الفردية على فترة متماثلة يساوي صفراً."),
    ]
}

PAGE_UNIT_RANGES = [
    (7, 44, "u1"),
    (45, 73, "u2"),
    (74, 103, "u5"),
    (104, 132, "u3"),
    (133, 153, "u4"),
    (154, 209, "u6"),
    (210, 256, "u7")
]

WORKBOOK_UNIT_RANGES = [
    (6, 17, "u1"),
    (18, 30, "u2"),
    (31, 36, "u3"),
    (37, 44, "u4"),
    (45, 52, "u5"),
    (53, 67, "u6"),
    (68, 80, "u7")
]


def unit_for_book_page(bp):
    for start, end, uid in PAGE_UNIT_RANGES:
        if start <= bp <= end:
            return uid
    return None


def unit_for_workbook_page(bp):
    for start, end, uid in WORKBOOK_UNIT_RANGES:
        if start <= bp <= end:
            return uid
    return None


def anchor_for_book_page(bp):
    for anchor in ANCHORS:
        if anchor["pages"][0] <= bp <= anchor["pages"][1]:
            return anchor
    return None


def build_pages():
    pages = []
    for bp in range(7, 257):
        pdf_page = bp + 2
        uid = unit_for_book_page(bp)
        pages.append({
            "page_id": f"math12-p{bp:03d}",
            "book_page": bp,
            "pdf_page": pdf_page,
            "type": "lesson",
            "title": f"الرياضيات — ص {bp}",
            "unit_id": uid,
            "image": f"assets/curriculum/grade12/math/pages/page_{pdf_page:03d}_opt.jpg",
            "image_full": f"assets/curriculum/grade12/math/pages/page_{pdf_page:03d}.jpg",
            "aspect_ratio": 0.7078
        })
    return pages


def build_workbook_pages():
    pages = []
    for bp in range(6, 81):
        pdf_page = bp + 2
        pages.append({
            "page_id": f"math12-w{pdf_page:03d}",
            "book_page": bp,
            "pdf_page": pdf_page,
            "unit_id": unit_for_workbook_page(bp),
            "role": "practice_only",
            "image": f"assets/curriculum/grade12/math/workbook_pages/workbook_page_{pdf_page:03d}.jpg",
            "image_full": f"assets/curriculum/grade12/math/workbook_pages/workbook_page_{pdf_page:03d}.jpg"
        })
    return pages


def build_lessons():
    return [
        {
            "id": a["id"],
            "unitId": a["unitId"],
            "order": a["order"],
            "title": a["title"],
            "pages": a["pages"],
            "pdf_pages": [a["pages"][0] + 2, a["pages"][1] + 2]
        }
        for a in ANCHORS
    ]


def build_interactions():
    result = {}
    ys = [0.06, 0.24, 0.42, 0.60, 0.78]
    fallback_activities = {
        "u1": "act-math-complex-add",
        "u2": "act-math-demoivre",
        "u3": "act-math-cone",
        "u4": "act-math-space-diagonal",
        "u5": "act-math-prob-union",
        "u6": "act-math-power-rule",
        "u7": "act-math-definite"
    }
    fallback_solutions = {
        "u1": "sol-math-complex-add",
        "u2": "sol-math-demoivre",
        "u3": "sol-math-ellipse",
        "u4": "sol-math-space-diagonal",
        "u5": "sol-math-prob-union",
        "u6": "sol-math-power",
        "u7": "sol-math-definite"
    }
    fallback_diagrams = {
        "u1": "diag-math-complex",
        "u2": "diag-math-complex",
        "u3": "diag-math-cone",
        "u4": "diag-math-space",
        "u5": "diag-math-probability",
        "u6": "diag-math-derivative",
        "u7": "diag-math-integral"
    }
    for bp in range(7, 257):
        page_id = f"math12-p{bp:03d}"
        uid = unit_for_book_page(bp) or "u1"
        anchor = anchor_for_book_page(bp)
        exp_ref = anchor["id"] if anchor else f"exp-math-{uid}-overview"
        sol_ref = anchor["solution_ref"] if anchor and anchor.get("solution_ref") else fallback_solutions[uid]
        diag_ref = anchor["diagram_ref"] if anchor and anchor.get("diagram_ref") else fallback_diagrams[uid]
        act_ref = anchor["activity_ref"] if anchor and anchor.get("activity_ref") else fallback_activities[uid]
        quiz_ref = f"quiz-math-{uid}"
        spots = [
            {
                "id": f"hs-{page_id}-concept",
                "type": "explainable_text",
                "explanation_ref": exp_ref,
                "indicator_label": "📌 شرح المفهوم والصيغة",
                "highlight_color": "rgba(0, 168, 89, 0.13)",
                "bounds": {"x": 0.70, "y": ys[0], "w": 0.24, "h": 0.14}
            },
            {
                "id": f"hs-{page_id}-solution",
                "type": "step_by_step_equation",
                "solution_ref": sol_ref,
                "indicator_label": "🧮 حل مسألة خطوة بخطوة",
                "highlight_color": "rgba(0, 168, 89, 0.10)",
                "bounds": {"x": 0.70, "y": ys[1], "w": 0.24, "h": 0.14}
            },
            {
                "id": f"hs-{page_id}-activity",
                "type": "activity",
                "activity_ref": act_ref,
                "indicator_label": "🎮 نشاط تفاعلي",
                "highlight_color": "rgba(0, 168, 89, 0.16)",
                "bounds": {"x": 0.70, "y": ys[2], "w": 0.24, "h": 0.14}
            },
            {
                "id": f"hs-{page_id}-3d",
                "type": "interactive_3d",
                "diagram_ref": diag_ref,
                "indicator_label": "🧊 مجسم هندسي تفاعلي",
                "highlight_color": "rgba(0, 168, 89, 0.12)",
                "bounds": {"x": 0.70, "y": ys[3], "w": 0.24, "h": 0.14}
            },
            {
                "id": f"hs-{page_id}-quiz",
                "type": "assessment",
                "assessment_ref": quiz_ref,
                "indicator_label": "✅ اختبر نفسك",
                "highlight_color": "rgba(0, 168, 89, 0.14)",
                "bounds": {"x": 0.70, "y": ys[4], "w": 0.24, "h": 0.14}
            }
        ]
        result[page_id] = spots
    return result


def build_explanations():
    result = {}
    for unit in UNITS:
        uid = unit["id"]
        result[f"exp-math-{uid}-overview"] = {
            "id": f"exp-math-{uid}-overview",
            "title": f"مقدمة وأهداف {unit['title']}",
            "original_text": f"{unit['title']} (ص {unit['page_start']} - {unit['page_end']}): {unit['short_desc']}",
            "levels": {
                "basic": f"🎯 أهلاً بك في {unit['title']}. الفكرة الأساسية: {unit['short_desc']}",
                "intermediate": "📘 اقرأ الصفحة الأصلية، ثم حدد المطلوب، واكتب الصيغة المناسبة قبل التعويض. اربط كل خطوة بمعنى هندسي أو فيزيائي.",
                "advanced": "🚀 تطبيقات واقعية:\n• " + "\n• ".join(unit["real_world_apps"])
            },
            "chemical_equations": [{"label": f"قاعدة {i+1}", "eq": law} for i, law in enumerate(unit["key_laws"])],
            "math_equations": [{"label": f"قاعدة {i+1}", "eq": law} for i, law in enumerate(unit["key_laws"])],
            "tts_text": f"{unit['title']}. {unit['short_desc']}"
        }
    for a in ANCHORS:
        result[a["id"]] = {
            "id": a["id"],
            "title": a["title"],
            "original_text": f"من كتاب الطالب، الصفحات {a['pages'][0]} إلى {a['pages'][1]}: {a['title']}.",
            "levels": {
                "basic": f"📌 {a['title']}: ابدأ بتحديد المعطيات والمطلوب من نص الصفحة.",
                "intermediate": f"📘 {a.get('summary', '')} اكتب الصيغة المناسبة ثم عوّض بوضوح.",
                "advanced": f"🚀 {a.get('insight', 'اربط الفكرة بتطبيق عملي واختبر فهمك بالأسئلة.')}"
            },
            "chemical_equations": [{"label": "الصيغة المرتبطة", "eq": a.get("formula", "")}],
            "math_equations": [{"label": "الصيغة المرتبطة", "eq": a.get("formula", "")}],
            "tts_text": f"{a['title']}. {a.get('summary', '')}"
        }
    return result


def make_question(uid, seq, lesson_id, page, prompt, correct, distractors, explain):
    entries = [(correct, None)] + list(distractors)
    shift = seq % len(entries)
    entries = entries[shift:] + entries[:shift]
    options = []
    answer = 0
    for idx, (text, why) in enumerate(entries):
        opt = {"text": text}
        if why:
            opt["why_wrong"] = why
        options.append(opt)
        if why is None:
            answer = idx
    return {
        "id": f"qm-{uid}-{seq+1:02d}",
        "unitId": uid,
        "lessonId": lesson_id,
        "page": page,
        "difficulty": ["easy", "medium", "hard"][seq % 3],
        "skillId": ["recall", "calculation", "analysis", "application"][seq % 4],
        "q": prompt,
        "options": options,
        "answer": answer,
        "explain": explain
    }


def build_assessments():
    result = {}
    for unit in UNITS:
        uid = unit["id"]
        anchors = [a for a in ANCHORS if a["unitId"] == uid]
        questions = []
        for seq, item in enumerate(QUESTION_SETS[uid]):
            prompt, correct, distractors, explain = item
            anchor = anchors[seq % len(anchors)]
            span = anchor["pages"][1] - anchor["pages"][0] + 1
            page = anchor["pages"][0] + (seq % span)
            questions.append(make_question(uid, seq, anchor["id"], page, prompt, correct, distractors, explain))
        result[f"quiz-math-{uid}"] = questions
    return result


def dump_json(name, data):
    for directory in (DATA_DIR, ANDROID_DATA_DIR):
        os.makedirs(directory, exist_ok=True)
        with open(os.path.join(directory, name), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    payload = {
        "manifest": MANIFEST,
        "units": UNITS,
        "pages": build_pages(),
        "workbook_pages": build_workbook_pages(),
        "lessons": build_lessons(),
        "interactions": build_interactions(),
        "explanations": build_explanations(),
        "diagrams": DIAGRAMS,
        "activities": ACTIVITIES,
        "assessments": build_assessments(),
        "glossary": GLOSSARY,
        "solution_steps": SOLUTIONS,
        "geometry_lab": GEOMETRY_LAB
    }
    for name, data in payload.items():
        dump_json(f"{name}.json", data)
    with open(os.path.join(DATA_DIR, "data_bundle.js"), "w", encoding="utf-8") as f:
        f.write("window.THAKER_CURRICULUM_G12_MATH = ")
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    with open(os.path.join(ANDROID_DATA_DIR, "data_bundle.js"), "w", encoding="utf-8") as f:
        f.write("window.THAKER_CURRICULUM_G12_MATH = ")
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    total_questions = sum(len(v) for v in payload["assessments"].values())
    print(f"[✓] Math curriculum pack generated: {len(payload['pages'])} pages, {len(UNITS)} units, {total_questions} questions.")


if __name__ == "__main__":
    main()
