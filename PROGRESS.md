# PROGRESS.md — سجل التقدم التنفيذي لتحويل منهج الثالث الثانوي (اليمن)

**آخر تحديث:** 2026-11-25  
**المرحلة الحالية:** الكيمياء والرياضيات للثالث الثانوي العلمي مكتملتان؛ بقية المواد قيد التنفيذ، وبناء APK متوقف لغياب Android SDK

---

## ملخص المراحل العامة

- [x] **المرحلة 0: الفحص والتخطيط** (فحص 9 كتب PDF عبر `main` و`grade12-hq-backup`، فحص التطبيق `thaker-android-src` + `build_apk.py`، إنشاء `PLAN.md`, `PROGRESS.md`, `REVIEW_NEEDED.md`)
- [x] **تجهيز المحرك المشترك (`engine/`) والأصول المحلية أوفلاين (`KaTeX@0.19.1`, `Amiri@5.3.0`, `Cairo@5.3.0`, `mathjs@15.3.0`, `nerdamer@2.1.0`, `three@r128`) + المدقق `validate_book.py` وأداة المراجعة `_review.html`**
- [ ] **المرحلة 1: الدرسان التجريبيان (`1.1` و`1.4`)** — منفّذان ومُدققان بانتظار المراجعة والموافقة قبل بقية الإنجليزي (`QA/english/eng-u1-1_1_review.html` و`eng-u1-1_4_review.html`)
- [ ] **المادة 1: اللغة الإنجليزية** (Pupil's Book 6 + Workbook 6)
- [x] **المادة 2: الرياضيات** (250 صفحة + 75 صفحة تمارين، 105 أسئلة، 13 مشهد 3D؛ كتاب الطالب النظري متوفر ومستخدم)
- [ ] **المادة 3: اللغة العربية** (الأدب والنصوص والنقد + القراءة؛ النحو والصرف والبلاغة مسجل كفجوة)
- [ ] **المادة 4: الفيزياء**
- [ ] **المادة 5: الكيمياء**
- [ ] **المادة 6: الأحياء**
- [ ] **المادة 7: التربية الإسلامية (الإيمان)**
- [ ] **المرحلة 6: الربط الكامل بالتطبيق وبناء APK واختبارات التكامل (`docs/INTEGRATION.md`)** — كود الربط محدّث للكيمياء والرياضيات؛ بناء APK متوقف لغياب Android SDK

---

## تتبع تفصيلي حسب المادة والوحدة والدرس

### 1) اللغة الإنجليزية (`english`)
**المصادر:** `انجليزي-الطالب-للصف-الثالث-الثانوي.pdf` (77 ص) + `english_work_12th (1).pdf` (120 ص)

- **Unit 1: Describing things (PB pp. 1–8 / WB pp. 1–12)** — *(مكتمل: 12 درساً + QA + مراجعة + WebP)*
  - [x] `1.1` Shapes, coverings and materials (PB p. 1, WB p. 1)
  - [x] `1.2` Listening and describing (WB pp. 2–3)
  - [x] `1.3` Lost (PB p. 2, WB pp. 3–4)
  - [x] `1.4` An unusual animal (PB p. 3, WB pp. 4–5)
  - [x] `1.5` Language review 1 (PB p. 4, WB p. 5)
  - [x] `1.6` The countryside (PB p. 5, WB pp. 5–6)
  - [x] `1.7` Listening and map directions (WB pp. 6–7)
  - [x] `1.8` Vocabulary and comprehension (PB p. 6 / WB p. 8)
  - [x] `1.9` A drive in the countryside (PB p. 6, WB pp. 9–10)
  - [x] `1.10` Language review 2 (PB p. 7, WB pp. 10–11)
  - [x] `1.11` A view from a window (PB p. 8, WB pp. 11–12)
  - [x] `1.12` Write a description in your copybook (WB p. 12)
- **Unit 2: Reporting events (PB pp. 9–16 / WB pp. 13–28)** — *(مكتمل: 12 درساً + QA + مراجعة + WebP)*
  - [x] `2.1` Newspaper headlines (PB p. 9, WB pp. 13–14)
  - [x] `2.2` Today's news (PB p. 10, WB pp. 14–15)
  - [x] `2.3` Listening to news interviews (WB pp. 15–16)
  - [x] `2.4` Don and Debbie: dreamers (PB p. 11, WB pp. 16–17)
  - [x] `2.5` Language review 3 (PB p. 12, WB pp. 17–18)
  - [x] `2.6` Natural disasters (PB p. 13, WB pp. 18–19)
  - [x] `2.7` A newspaper report (PB p. 14, WB pp. 19–20)
  - [x] `2.8` Listening to the radio news (WB pp. 21–22)
  - [x] `2.9` Questions, intonation and interviewing (WB pp. 22–24)
  - [x] `2.10` Language review 4 (PB p. 15, WB pp. 24–26)
  - [x] `2.11` Armenia - 7, December 1988 (PB p. 16, WB pp. 26–27)
  - [x] `2.12` Planning and writing a newspaper report (WB pp. 27–28)
- **Unit 3: Looking for a job (PB pp. 17–24 / WB pp. 29–40)**
  - [x] `3.1` Getting work experience (PB p. 17, WB pp. 29–30)
  - [x] `3.2` Listening: worthwhile jobs & interview (WB pp. 30–31)
  - [x] `3.3` Thinking about the future (PB p. 18, WB pp. 31–32)
  - [x] `3.4` Getting careers advice (PB p. 19, WB p. 32)
  - [x] `3.5` Language review 5 (PB p. 20, WB pp. 32–33)
  - [x] `3.6` Job and qualities (PB p. 21, WB pp. 34–35)
  - [x] `3.7` Listening: job advertisements (WB pp. 35–36)
  - [x] `3.8` Applying for a job (PB p. 22, WB pp. 36–37)
  - [x] `3.9` Intonation and job interview roleplay (WB pp. 38–39)
  - [x] `3.10` Language review 6 (PB p. 23, WB pp. 39–40)
  - [x] `3.11` A business letter: layout and vocabulary (PB p. 24, WB p. 40)
  - [x] `3.12` Writing a letter of application (PB p. 24, WB p. 40)
- **Unit 4: Tables, flow charts and diagrams (PB pp. 25–32, WB pp. 41–54)**
  - [x] `4.1` Food (PB p. 25, WB p. 41)
  - [x] `4.2` Flow charts (WB pp. 41–42)
  - [x] `4.3` Learning to cook (PB p. 26, WB p. 43)
  - [x] `4.4` Agriculture in Yemen (PB p. 27, WB p. 44)
  - [x] `4.5` Tables and cooking conversations (WB pp. 44–45)
  - [x] `4.6` Language review 7 (PB p. 28, WB pp. 45–46)
  - [x] `4.7` Words and more words (PB p. 29, WB pp. 46–47)
  - [x] `4.8` Investigating the world around us (PB p. 30, WB p. 48)
  - [x] `4.9` Water displacement and Ahmed's experiment (WB pp. 49–50)
  - [x] `4.10` Language review 8 (PB p. 31, WB pp. 51–52)
  - [x] `4.11` Frozen peas (PB p. 32, WB pp. 52–53)
  - [x] `4.12` Stuffed olives: flow chart and process (PB p. 32, WB pp. 53–54)
- **Unit 5: Working things out (PB pp. 33–40, WB pp. 55–70)**
  - [x] `5.1` Word sets (PB p. 33, WB pp. 55–56)
  - [x] `5.2` Possibilities (PB p. 34, WB pp. 56–57)
  - [x] `5.3` Listening: Where are they? & The Coronation (WB pp. 57–58)
  - [x] `5.4` Puzzles and riddles (PB p. 35, WB pp. 59–60)
  - [x] `5.5` Language review 9 (PB p. 36, WB pp. 60–61)
  - [x] `5.6` The mystery of the Mary Celeste (PB p. 37, WB pp. 61–63)
  - [x] `5.7` What could have happened? (PB p. 38, WB pp. 63–64)
  - [x] `5.8` Listening: Fosdyke's story (WB pp. 64–65)
  - [x] `5.9` Language review 10 (PB p. 39, WB pp. 65–66)
  - [x] `5.10` Picture puzzle: What happened in the street? (WB pp. 67–68)
  - [x] `5.11` Tracks in the sand: reading and planning (PB p. 40, WB pp. 68–70)
  - [x] `5.12` Tracks in the sand: writing the ending (PB p. 40, WB p. 70)
- **Unit 6: Looking back (PB pp. 41–49 / WB pp. 71–80)**
  - [x] `6.1` Emergencies in the news (PB p. 41 / WB p. 71)
  - [x] `6.2` A lucky escape (PB p. 42 / WB pp. 72–73)
  - [x] `6.3` Accident at Jebel Kebir (PB p. 43 / WB pp. 73–74)
  - [x] `6.4` Saving Anwar: listening & vocabulary (PB p. 44 / WB pp. 74–75)
  - [x] `6.5` Saving Anwar: retelling the story (PB p. 44 / WB p. 75)
  - [x] `6.6` How a hospital works (PB p. 45 / WB p. 75)
  - [x] `6.7` Working in public service (PB p. 46 / WB p. 76)
  - [x] `6.8` Huge changes in Libyan health care: reading (PB p. 47)
  - [x] `6.9` Huge changes in Libyan health care: comprehension & vocabulary (PB p. 47 / WB pp. 77–78)
  - [x] `6.10` Discovering Yemen (PB p. 48 / WB p. 78)
  - [x] `6.11` Tourism and the future: reading (PB p. 49 / WB pp. 78–79)
  - [x] `6.12` Tourism and the future: writing about your future (PB p. 49 / WB pp. 79–80)
- **Arts Reader (PB pp. 50–62)**
  - [x] `arts-1` A difficult choice? (PB pp. 50–51 / WB pp. 81–82)
  - [x] `arts-2` Proverbs and idioms (PB p. 52 / WB pp. 82–83)
  - [x] `arts-3` Telford Hall Episode 1 (PB p. 53 / WB pp. 84–85)
  - [x] `arts-4` A famous play by Shakespeare (PB p. 54 / WB pp. 85–87)
  - [x] `arts-5` Telford Hall Episode 2 (PB pp. 55–56 / WB pp. 87–89)
  - [x] `arts-6` Critics and criticism (PB p. 57 / WB pp. 89–90)
  - [x] `arts-7` Telford Hall Episode 3 (PB pp. 58–59 / WB pp. 90–92)
  - [x] `arts-8` Calligraphy (PB p. 60 / WB pp. 92–93)
  - [x] `arts-9` A poem (PB p. 61 / WB pp. 93–94)
  - [x] `arts-10` Strange happenings (PB p. 62 / WB pp. 94–95)
- **Science Reader (PB pp. 64–74)**
  - [x] `sci-1` Acids and alkalis (PB pp. 63–65 / WB pp. 96–97)
  - [x] `sci-2` States of matter (PB p. 66 / WB pp. 97–98)
  - [x] `sci-3` Light (PB p. 67 / WB pp. 98–99)
  - [x] `sci-4` Sound (PB p. 68 / WB p. 100)
  - [x] `sci-5` Arab scientists (PB p. 69 / WB p. 101)
  - [x] `sci-6` Vaccinations (PB p. 70 / WB pp. 102–103)
  - [x] `sci-7` Experimental procedures (PB p. 71 / WB pp. 103–105)
  - [x] `sci-8` Internal combustion engine (p. 72)
  - [x] `sci-9` The Moon (p. 73)
  - [x] `sci-10` Radioactivity (p. 74)
- **QA & التغطية الكاملة للإنجليزي**
  - [x] مطابقة صفحة بصفحة مع PB (77 ص) وWB (120 ص) وقوائم المفردات (ص 112–118) + تقرير `QA/english/COVERAGE_REPORT.md`

---

### 2) الرياضيات (`math`) — مكتملة بالكامل ✅
**المصادر:** `الرياضيات-للصف-الثالث-الثانوي.pdf` (250 صفحة كتاب بعد الإزاحة) + `الرياضيات-التمارين-للصف-الثالث-الثانوي-القسم-العلمي.pdf` (75 صفحة تمارين بعد الإزاحة)
- [x] **حزمة البيانات Schema v2.0:** `manifest.json`, `units.json`, `pages.json`, `workbook_pages.json`, `lessons.json`, `interactions.json`, `explanations.json`, `diagrams.json`, `activities.json`, `assessments.json`, `glossary.json`, `solution_steps.json`, `geometry_lab.json`, `data_bundle.js`
- [x] **بنك الأسئلة:** 105 سؤالاً (15 سؤالاً لكل وحدة من الوحدات السبع) مع `unitId`, `lessonId`, `page`, و`why_wrong` لكل خيار خاطئ
- [x] **الطبقة التفاعلية:** 5 أنواع Hotspots، 22 حلاً خطوة بخطوة، 25 نشاطاً محاكى، و13 مجسماً في معمل 3D
- [x] **الكتاب والمعمل المستقلان:** `math-12th-book.html` و`math-12th-lab.html` أوفلاين 100% ومزامنان إلى `thaker-android-src/assets/`
- [x] **الربط بالتطبيق:** بطاقة «الرياضيات 3D»، عنصرا المكتبة، ملخصات، بنك أسئلة `m12_*`، وربط الأصول بـ `math_12`
- [x] الوحدة 1: الأعداد المركبة (كتاب ص 7–44 / تمارين ص 6–17) — [15 سؤالاً]
- [x] الوحدة 2: مبرهنة دي موافر والتوسعة ذات الحدين (كتاب ص 45–73 / تمارين ص 18–30) — [15 سؤالاً]
- [x] الوحدة 3: القطوع المخروطية (كتاب ص 104–132 / تمارين ص 31–36) — [15 سؤالاً]
- [x] الوحدة 4: الهندسة في فضاء ثلاثي الأبعاد (كتاب ص 133–153 / تمارين ص 37–44) — [15 سؤالاً]
- [x] الوحدة 5: الاحتمالات (كتاب ص 74–103 / تمارين ص 45–52) — [15 سؤالاً]
- [x] الوحدة 6: المشتقات وتطبيقاتها (كتاب ص 154–209 / تمارين ص 53–67) — [15 سؤالاً]
- [x] الوحدة 7: التكامل (كتاب ص 210–256 / تمارين ص 68–80) — [15 سؤالاً]

---

### 3) اللغة العربية (`arabic_lit` + `arabic_reading`)
**المصادر المتوفرة:** `الأدب-والنصوص-والنقد-للصف-الثالث-الثانوي.pdf` (218 ص) + `القراءة-ثالث-ثانوي.pdf` (115 ص) | *ملاحظة: كتاب النحو والصرف والبلاغة مفقود.*
- [x] **استخراج صور الصفحات فائقة الدقة:** تم توليد 424 صورة (200 DPI للأصل + 150 DPI للنسخ المحسّنة) من PDF ص 7–218 تحت `assets/curriculum/grade12/arabic_lit/pages/`
- [x] **حزمة البيانات المعيارية (Schema v2.0):** 212 صفحة، قسمان، 36 موضوعاً، 36 نقطة تحليل، بطاقات نصوص، و36 سؤالاً مع `why_wrong` لكل خيار خاطئ
- [x] **الكتاب التفاعلي:** `arabic-literature-12th-book.html` أوفلاين 100%، بخط Amiri المحلي ولوحة تحليل جمالي وبطاقات نصوص
- [x] **الربط بالتطبيق:** بطاقة «الأدب والنصوص»، عنصر المكتبة، ملخصات، بنك أسئلة `lit_*`، وربط الأصول بـ `arabic_lit`
- [x] الأدب والنصوص والنقد — أولاً: الأدب والنصوص (29 موضوعاً، ص 9–171)
- [x] الأدب والنصوص والنقد — ثانياً: النقد الأدبي (7 موضوعات، ص 173–217)
- [ ] القراءة والتعبير (15 موضوعاً، ص 7–110)

---

### 4) الفيزياء (`physics`)
**المصدر:** `كتاب-فيزياء-ثالث-ثانوي-اليمن.pdf` (219 ص)
- [ ] الوحدة 1: كمية التحرك والمقذوفات (ص 9–28)
- [ ] الوحدة 2: التيار المتردد (المتناوب) (ص 29–60)
- [ ] الوحدة 3: الإلكترونيات (ص 61–84)
- [ ] الوحدة 4: الأجهزة الإلكترونية (ص 85–113)
- [ ] الوحدة 5: الفيزياء الذرية (ص 114–143)
- [ ] الوحدة 6: الإشعاع والمادة (ص 144–172)
- [ ] الوحدة 7: الفيزياء النووية (ص 173–184)
- [ ] الوحدة 8: الطاقة الشمسية (ص 185–197)
- [ ] الوحدة 9: الفيزياء الكونية (ص 198–216)

---

### 5) الكيمياء (`chemistry`) — مكتملة بالكامل وموثقة ✅
**المصدر:** `كتاب-الكيمياء-ثالث-ثانوي.pdf` (187 صفحة كتاب، PDF 5..191)
- [x] **استخراج صور الصفحات فائقة الدقة:** تم توليد 374 صورة (240 DPI للأصل + 180 DPI للنسخ المحسنة) تحت `assets/curriculum/grade12/chemistry/pages/`
- [x] **حزمة البيانات المعيارية (Schema v2.0):** تم توليد جميع الملفات العشرة في `data/curriculum/grade12/chemistry/`:
  - `manifest.json` (بيانات المنهج، 187 صفحة كتاب، إزاحة الطباعة `book_page = pdf_page - 2`)
  - `units.json` (9 وحدات كاملة مع المفاهيم، القوانين، والتطبيقات الواقعية)
  - `pages.json` (187 كائناً لجميع صفحات الكتاب)
  - `lessons.json` (41 درساً مفصلاً)
  - `glossary.json` (34 مصطلحاً علمياً دقيقاً)
  - `explanations.json` (شروحات بـ3 مستويات: أساسي، متوسط، متقدم مع معادلات وتطبيقات)
  - `diagrams.json` (13 مجسماً تفاعلياً ثلاثي الأبعاد)
  - `activities.json` (22 نشاطاً: 12 مرتبطة مباشرة بمعمل الكيمياء 3D + 10 محاكيات تفاعلية داخل المودال)
  - `interactions.json` (178 صفحة مغطاة بـ 211 نقطة تفاعل Hotspot بدقة عالية وتداخل < 4%)
  - `assessments.json` (**135 سؤالاً وزارياً شاملاً** — 15 سؤالاً لكل وحدة من الوحدات التسع، مع `why_wrong` لكل خيار خاطئ و`explain` علمي شامل)
  - `data_bundle.js` (حزمة جافاسكريبت المستقلة أوفلاين)
- [x] **تكامل معمل الكيمياء الافتراضي 3D (`chem-lab-book.html`):**
  - دعم التنقل الثنائي (Deep Linking) عبر الهاش `#exp=exp-X&from=book&page=Y`
  - زر عودة مخصص في المعمل يعيد الطالب مباشرة إلى صفحته في الكتاب المدرسي التفاعلي
  - ربط كامل لجميع التجارب العشر:
    1. `exp-1`: الكشف عن أملاح الحديد (ص 21)
    2. `exp-2`: حرارة الذوبان طارد وماص (ص 31)
    3. `exp-3`: الأكسدة والاختزال التلقائي (ص 48)
    4. `exp-4`: خلية دانيال الجلفانية (ص 50)
    5. `exp-5`: فحص المركم الرصاصي (ص 56)
    6. `exp-6`: التحليل الكهربي للماء (ص 60)
    7. `exp-7`: الطلاء الكهربي بالفضة (ص 63)
    8. `exp-8`: كشف النشا والسكريات المختزلة (ص 110–112)
    9. `exp-9`: صناعة الصابون والتمليح (ص 158)
    10. `exp-10`: التقطير التجزيئي للنفط الخام (ص 131–133)
- [x] **الكتاب التفاعلي المستقل (`chemistry-12th-book.html`):** توليده بنجاح ومزامنته إلى جذر المشروع و`thaker-android-src/assets/`
- [x] **نظام البناء الموحد والجودة:**
  - `Makefile` متكامل لتشغيل `make all`, `make data`, `make books`, `make sync-assets`, `make test`, `make apk`
  - جناح اختبارات آلي `tests/test_curriculum_integrity.py` يمر بنجاح بنسبة 100%
- [x] **تكامل تطبيق أندرويد Native:** إضافة المادة إلى القائمة الرئيسية، شاشات الملخصات، بنك الأسئلة، ومعمل 3D.
- [x] الوحدة 1: العناصر الانتقالية (ص 11–21) — [15 سؤالاً]
- [x] الوحدة 2: الطاقة الحرارية المصاحبة لتغيرات المادة (ص 22–41) — [15 سؤالاً]
- [x] الوحدة 3: الطاقة الكهربائية وتفاعلات الأكسدة والاختزال (ص 42–68) — [15 سؤالاً]
- [x] الوحدة 4: الطاقة والتفاعلات النووية (ص 69–90) — [15 سؤالاً]
- [x] الوحدة 5: مركبات النيتروجين العضوية (ص 91–103) — [15 سؤالاً]
- [x] الوحدة 6: الكيمياء الحيوية (ص 104–122) — [15 سؤالاً]
- [x] الوحدة 7: الذهب الأسود (ص 123–137) — [15 سؤالاً]
- [x] الوحدة 8: صناعات كيميائية في خدمة الإنسان (ص 138–166) — [15 سؤالاً]
- [x] الوحدة 9: الكيمياء والبيئة (ص 167–183) + المصطلحات العلمية (ص 184+) — [15 سؤالاً]

---

### 6) الأحياء (`biology`)
**المصدر:** `الأحياء-للصف-الثالث-الثانوي.pdf` (221 ص)
- [ ] الوحدة 1: الجهاز العصبي (ص 8–39)
- [ ] الوحدة 2: التنظيم الهرموني (ص 40–60)
- [ ] الوحدة 3: التكاثر في الكائنات الحية (ص 61–95)
- [ ] الوحدة 4: أساسيات علم الوراثة (ص 96–130)
- [ ] الوحدة 5: الوراثة الجزيئية (ص 131–143)
- [ ] الوحدة 6: التقانة الحيوية (ص 144–161)
- [ ] الوحدة 7: البيئة ومشكلاتها (ص 162–186)
- [ ] الوحدة 8: تاريخ الأرض (ص 187–222) + المصطلحات العلمية (ص 223–224)

---

### 7) التربية الإسلامية — الإيمان (`iman`)
**المصدر:** `كتاب-الإيمان-ثالث-ثانوي-اليمن.pdf` (83 ص)
- [ ] الدروس 1 إلى 13 (ص 7–77)
