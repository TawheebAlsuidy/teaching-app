package com.thaker.app;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;
import java.util.ArrayList;
import java.util.List;

public class SummaryActivity extends Activity {

    private String subject = "science";
    private int selectedFilter = 0;
    private LinearLayout cardsContainer, pillsContainer;
    private TextView tvTitle, btnBookmark;
    private float dp;

    private static class SummaryGroup {
        String unitChip, unitTitle, defTitle, defBody, defPage;
        String ruleTitle, ruleFormula, ruleBody, rulePage;
        String factorTitle, factorBody, factorPage;
        String errTitle, errBody;
        SummaryGroup(String unitChip, String unitTitle,
                     String defTitle, String defBody, String defPage,
                     String ruleTitle, String ruleFormula, String ruleBody, String rulePage,
                     String factorTitle, String factorBody, String factorPage,
                     String errTitle, String errBody) {
            this.unitChip = unitChip; this.unitTitle = unitTitle;
            this.defTitle = defTitle; this.defBody = defBody; this.defPage = defPage;
            this.ruleTitle = ruleTitle; this.ruleFormula = ruleFormula; this.ruleBody = ruleBody; this.rulePage = rulePage;
            this.factorTitle = factorTitle; this.factorBody = factorBody; this.factorPage = factorPage;
            this.errTitle = errTitle; this.errBody = errBody;
        }
    }

    private final List<SummaryGroup> groups = new ArrayList<SummaryGroup>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_summary);
        dp = getResources().getDisplayMetrics().density;

        String sub = getIntent().getStringExtra("summary_subject");
        if (sub != null && !sub.isEmpty()) subject = sub;

        tvTitle = findViewById(R.id.tv_summary_title);
        btnBookmark = findViewById(R.id.btn_summary_bookmark);
        pillsContainer = findViewById(R.id.summary_unit_pills);
        cardsContainer = findViewById(R.id.summary_cards_container);

        findViewById(R.id.btn_summary_back).setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) { finish(); }
        });

        btnBookmark.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                String entry = "ملخص: " + tvTitle.getText() + "|summary|" + subject + "|1";
                boolean added = ThakerStore.toggleBookmark(SummaryActivity.this, entry);
                Toast.makeText(SummaryActivity.this, added ? "تم الحفظ في المفضلة ⭐" : "تمت الإزالة من المفضلة", Toast.LENGTH_SHORT).show();
                updateBookmarkLabel();
            }
        });

        findViewById(R.id.btn_summary_quiz).setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                Intent i = new Intent(SummaryActivity.this, QuizActivity.class);
                i.putExtra("quiz_subject", mapSummaryToQuiz(subject));
                startActivity(i);
            }
        });

        loadSummaryGroups();
        renderFilterPills();
        renderSelectedGroup();
        updateBookmarkLabel();
    }

    private void updateBookmarkLabel() {
        String entry = "ملخص: " + tvTitle.getText() + "|summary|" + subject + "|1";
        boolean saved = ThakerStore.getBookmarks(this).contains(entry);
        btnBookmark.setText(saved ? "★ محفوظ" : "⭐ احفظ");
    }

    private String mapSummaryToQuiz(String s) {
        if ("math".equals(s) || "math_p1".equals(s)) return "math_p1";
        if ("math_p2".equals(s)) return "math_p2";
        if ("math12".equals(s)) return "math_12";
        if ("arabic_lit".equals(s)) return "arabic_lit";
        if ("quran".equals(s)) return "quran";
        if ("physics".equals(s)) return "phys_12";
        if ("biology".equals(s)) return "bio_12";
        if ("chemistry".equals(s)) return "chem_12";
        return "sci_p2";
    }

    private void loadSummaryGroups() {
        groups.clear();
        if ("math".equals(subject) || "math_p1".equals(subject) || "math_p2".equals(subject)) {
            tvTitle.setText("الرياضيات · المبرهنات والقوانين");
            groups.add(new SummaryGroup(
                "الجبر والتحليل", "الوحدة 4: تحليل المقادير الجبرية",
                "💡 طرق التحليل الأساسية", "• العامل المشترك الأعلى: إخراج أكبر عامل يقبل جميع الحدود القسمة عليه.\n• الفرق بين مربعين والفرق بين مكعبين.", "ص 61",
                "📐 القاعدة والصيغ الجبرية", "س² − ص² = (س − ص)(س + ص)\nس³ + ص³ = (س + ص)(س² − س ص + ص²)", "تُستخدم هذه الصيغ في تبسيط الكسور الجبرية وحل المعادلات.", "ص 66",
                "🧪 شروط المقدار الثلاثي المربع الكامل", "• الحد الأول والثالث مربعان موجبان.\n• الحد الأوسط = ± 2 × √الأول × √الثالث.", "ص 72",
                "⚠️ خطأ شائع", "اعتقاد أن مجموع المربعين (س² + ص²) يُحلّل إلى (س + ص)² — والصحيح أنه لا يُحلّل في R."
            ));
            groups.add(new SummaryGroup(
                "الدائرة", "الوحدة 5: الهندسة المستوية (الدائرة)",
                "💡 الزاوية المركزية والمحيطية", "• الزاوية المركزية رأسها مركز الدائرة، والمحيطية رأسها على محيط الدائرة.", "ص 18",
                "📐 القاعدة والمبرهنة", "الزاوية المحيطية = ½ الزاوية المركزية المشتركة في نفس القوس\nالرباعي الدائري: أ + جـ = 180°", "العمود النازل من المركز على أي وتر ينصّف ذلك الوتر.", "ص 24",
                "🧪 شروط الشكل الرباعي الدائري", "• إذا تكاملت زاويتان متقابلتان، أو تساوت زاوية خارجة مع المقابلة للمجاورة لها.", "ص 36",
                "⚠️ خطأ شائع", "الخلط بين قياس الزاوية المحيطية المقابلة لنصف دائرة — قياسها دائماً 90° (قائمة)."
            ));
            groups.add(new SummaryGroup(
                "حساب المثلثات", "الوحدة 6: النسب المثلثية",
                "💡 النسب في المثلث القائم", "• الجيب (جا) = المقابل / الوتر\n• جيب التمام (جتا) = المجاور / الوتر\n• الظل (ظا) = المقابل / المجاور", "ص 48",
                "📐 المتطابقة الأساسية", "جا² هـ + جتا² هـ = 1   |   ظا هـ = جا هـ / جتا هـ", "جا 30° = ½  |  جا 60° = √3/2  |  ظا 45° = 1", "ص 54",
                "🧪 علاقة الزاويتين المتتامتين", "• جا(90° − هـ) = جتا هـ ، مثل: جا 30° = جتا 60° = ½.", "ص 60",
                "⚠️ خطأ شائع", "التبديل بين المقابل والمجاور عند تغيير الزاوية الحادة داخل المثلث القائم."
            ));
        } else if ("math12".equals(subject)) {
            tvTitle.setText("الرياضيات 3D · الثالث الثانوي");
            groups.add(new SummaryGroup(
                "الأعداد المركبة", "الوحدتان 1 و2: الأعداد المركبة ودي موافر والتوسعة ذات الحدين",
                "💡 الشكل القطبي والقيمة المطلقة", "• z = a + bi = r(cosθ + i sinθ)\n• |z| = √(a²+b²) و arg(z) = θ.", "ص 7",
                "📐 دي موافر والتوسعة", "zⁿ = rⁿ(cos nθ + i sin nθ)\n(a + bi)ⁿ = Σ C(n,k) aⁿ⁻ᵏ (bi)ᵏ", "تحوّل دي موافر القوى إلى ضرب في الزاوية، والتوسعة توزّع الحدود حسب معاملات ذات الحدين.", "ص 45",
                "🧪 جمع الأعداد المركبة", "• تُجمع الأجزاء الحقيقية معاً والتخيلية معاً: (a+bi)+(c+di)=(a+c)+(b+d)i.", "ص 13",
                "⚠️ خطأ شائع", "اعتبار i² = +1 — الصحيح i² = −1، ولذلك (3+4i)(3−4i)=25 لا −7."
            ));
            groups.add(new SummaryGroup(
                "القطوع والهندسة الفضائية", "الوحدتان 3 و4: القطوع المخروطية والهندسة في فضاء ثلاثي الأبعاد",
                "💡 معادلات القطوع", "• y² = 4px: بؤرتها (p,0) ودليلها x = −p.\n• x² = 4py: بؤرتها (0,p) ودليلها y = −p.", "ص 104",
                "📐 القطع الناقص والزائد", "x²/a² + y²/b² = 1  |  x²/a² − y²/b² = 1\ne = c/a، وفي الزائد c² = a² + b².", "الفارق الجوهري: في الناقص e < 1 وفي الزائد e > 1.", "ص 113",
                "🧪 قطر صندوق وعلاقة مستقيم بمستوى", "• قطر متوازي المستطيلات = √(ط² + ع² + ار²).", "ص 133",
                "⚠️ خطأ شائع", "تطبيق علاقة e < 1 على القطع الزائد — الصحيح أن e > 1."
            ));
            groups.add(new SummaryGroup(
                "الاحتمالات والتحليل", "الوحدات 5–7: الاحتمالات، المشتقات، التكامل",
                "💡 قواعد الاحتمال", "• P(A∪B) = P(A) + P(B) − P(A∩B)\n• P(A|B) = P(A∩B) / P(B)، بشرط P(B) ≠ 0.", "ص 74",
                "📐 المشتقة والتكامل", "f′(x) = limₕ→₀ [f(x+h)−f(x)]/h\n(xⁿ)′ = nxⁿ⁻¹  |  ∫xⁿdx = xⁿ⁺¹/(n+1) + C", "قاعدة التكامل تستثنى n = −1؛ ونتيجة التكامل المحدد F(b) − F(a).", "ص 154",
                "🧪 حجم مجسم الدوران", "• V = π∫ₐᵇ [f(x)]² dx عند الدوران حول محور x.", "ص 210",
                "⚠️ خطأ شائع", "نسيان ثابت التكامل C في التكامل غير المحدد، أو استخدام F(a)−F(b) بدل F(b)−F(a)."
            ));
        } else if ("arabic_lit".equals(subject)) {
            tvTitle.setText("الأدب والنصوص · الثالث الثانوي");
            groups.add(new SummaryGroup(
                "الأدب والنصوص", "القسم الأول: من ص 9 إلى ص 171",
                "الموضوعات الأدبية", "• الأدب في العصرين المملوكي والعثماني يبدأ ص 9.\n• النهضة الأدبية في العصر الحديث تبدأ ص 23.\n• المدرسة الرومنسية تبدأ ص 82، والواقعية تبدأ ص 121.", "ص 9",
                "الشعر والنثر", "• شعر: في رثاء بغداد، فراق وشوق، ثمن الحرية، أمتي.\n• نثر: وصف السفينة، الإسراء والمعراج، الرجولة، مسمار جحا.", "ص 14",
                "بطاقات النصوص", "اربط كل عنوان بصاحبه ونوعه وصفحة بدايته من الفهرس الرسمي.",
                "خطأ شائع", "خلط عنوان النص بنوعه؛ راجع الفهرس قبل تحديد الشعر أو النثر."
            ));
            groups.add(new SummaryGroup(
                "النقد الأدبي", "القسم الثاني: من ص 173 إلى ص 217",
                "مفاهيم النقد", "• النقد الأدبي يبدأ ص 173.\n• الأسلوب يبدأ ص 180، والشكل والمضمون يبدأ ص 184.", "ص 173",
                "التطبيقات النقدية", "• التجربة الشعرية ص 189.\n• القصة ص 198، والنص المسرحي ص 200، والمقالة ص 202.", "ص 189",
                "طريقة التطبيق", "طبّق المفهوم النقدي على نص من الكتاب، واربط الحكم بالشاهد النصي.",
                "خطأ شائع", "اعتبار القصة والنص المسرحي والمقالة نوعاً واحداً؛ لكل منها خصائصه الخاصة."
            ));
        } else if ("quran".equals(subject)) {
            tvTitle.setText("القرآن الكريم وعلومه · الثالث الثانوي");
            groups.add(new SummaryGroup(
                "سورة النور (القسم الأول)", "ص 8–86: أحكام الأسرة والمجتمع وآداب الاستئذان",
                "💡 محاور السورة", "• حماية الأعراض وحد القذف واللعان وحادثة الإفك.\n• آداب الاستئذان والبيوت وغض البصر والحجاب والزواج.", "ص 8",
                "📖 آيات ومفاهيم أساسية", "من ص 8 إلى ص 86: 13 درس تفسير (الآيات 24:1–64) مع المعاني والتلاوة أوفلاين بصوت الحصري المعلم.", "افتح أي درس داخل كتاب القرآن التفاعلي للاستماع للتلاوة ومشاهدة التحليل التجويدي.", "ص 24",
                "🎧 التلاوة والقصص المرئية", "• قصة حادثة الإفك عبر 6 محطات موثقة بالصوت والصورة، وتطبيق آداب الاستئذان.", "ص 22",
                "⚠️ تنبيه علمي", "التحقق من الأخبار بالبينة قبل نشرها هو أساس الوقاية من الشائعات كما قررت آيات الإفك."
            ));
            groups.add(new SummaryGroup(
                "علوم القرآن الكريم (القسم الثاني)", "ص 88–103: جمع القرآن، الإعجاز، ومخارج الحروف",
                "💡 محاور علوم القرآن", "• جمع القرآن الكريم في عهد النبي ﷺ وأبي بكر وعثمان رضي الله عنهم.\n• وجوه إعجاز القرآن الكريم والضوابط الأربعة للتفسير العلمي الصحيح.", "ص 88",
                "📐 المخارج الرئيسية الخمسة", "الجوف · الحلق · اللسان · الشفتان · الخيشوم", "تمتد عليها سبعة عشر مخرجاً خاصاً عند ابن الجزري وجمهور القراء.", "ص 100",
                "🧪 الضبط المنهجي للإعجاز", "• التمييز بين الحقيقة العلمية القطعية والنظرية الظنية قبل ربطها بالآية الكريمة.", "ص 94",
                "⚠️ خطأ شائع", "الاكتفاء بالملاحظات الإملائية في كتب التفسير دون التمييز بين الرسم العثماني والرسم الإملائي."
            ));
            groups.add(new SummaryGroup(
                "التلاوة والتجويد (القسم الثالث)", "ص 105–192: الأعراف، الأنفال، التوبة، يونس، هود",
                "💡 السور المقررة للتلاوة", "• 18 حصة تلاوة بالرسم العثماني الموثق من مصحف المدينة.\n• إبراز أحكام التجويد الملونة وعلامات الوقف في القارئ الذكي.", "ص 105",
                "🗣️ قواعد الوصل والابتداء", "لا بِسْمِ اللَّهِ في مفتتح سورة التوبة (ص 139)، مع تطبيق التفخيم والترقيق والمدود والغنة.", "تشمل الحصص تطبيقات: قلقلة، إدغام، إخفاء، مد لازم، ومواضع الإمالة في سورة هود.", "ص 175",
                "🧪 مراجعة الحصص والتقاويم", "• جميع التقاويم الرسمية الـ16 مدمجة بإجاباتها النموذجية واختبار الحفظ التفاعلي.", "ص 188",
                "⚠️ خطأ شائع", "قراءة البسملة عند البدء بسورة التوبة، أو إهمال علامات الوقف المانعة."
            ));
        } else if ("physics".equals(subject)) {
            tvTitle.setText("الفيزياء 3D · الثالث الثانوي");
            groups.add(new SummaryGroup(
                "كمية التحرك والمقذوفات", "الوحدة 1: التصادم والمقذوفات والصواريخ",
                "💡 كمية التحرك الخطي والزاوي", "• كمية التحرك الخطي (كم): حاصل ضرب الكتلة في السرعة وهو كمية متجهة.\n• يبلغ المقذوف أقصى مدى أفقي عند زاوية 45°.", "ص 10",
                "📐 القوانين الحاكمة", "كم = ك × ع   |   v_esc = √(2GM / R)", "كمية التحرك محفوظة في التصادم المرن وغير المرن بغياب القوى الخارجية.", "ص 18",
                "🧪 عوامل المدى الأفقي للمقذوف", "• يبلغ المقذوف أقصى مدى أفقي عند زاوية إطلاق 45°.", "ص 24",
                "⚠️ خطأ شائع", "إهمال الإشارة السالبة عند عكس اتجاه السرعة بعد التصادم."
            ));
            groups.add(new SummaryGroup(
                "التيار المتردد", "الوحدة 2: الدينامو ودوائر RLC والرنين",
                "💡 الحث الكهرومغناطيسي والرنين", "• يتولد تيار متردد بتغير الفيض المغناطيسي خلال ملف الدينامو.\n• عند الرنين تتساوى المفاعلة الحثية والسعوية.", "ص 32",
                "📐 قوانين الرنين والمفاعلة", "XL = 2πfL  |  Xc = 1/(2πfC)  |  f₀ = 1/(2π√(LC))", "عند الرنين تكون المعاوقة الكلية أقل ما يمكن (Z = R) ويمر أعظم تيار.", "ص 51",
                "🧪 القيمة الفعالة للتيار", "• I_eff = I_max / √2 ≈ 0.707 I_max، ويقيسها الأميتر الحراري.", "ص 38",
                "⚠️ خطأ شائع", "الخلط بين المفاعلة الحثية (طردية مع التردد) والسعوية (عكسية مع التردد)."
            ));
        } else if ("biology".equals(subject)) {
            tvTitle.setText("الأحياء 3D · الثالث الثانوي");
            groups.add(new SummaryGroup(
                "الجهاز العصبي", "الوحدة 1: العصبون والسيال العصبي",
                "💡 الخلية العصبية (العصبون)", "• وحدة البناء والوظيفة؛ تنقل الإشارات العصبية من المستقبلات إلى المراكز العصبية.", "ص 9",
                "📐 أرقام وجهود أساسية", "جهد الراحة = -70 mV  |  عتبة الإثارة = -55 mV  |  الذروة = +40 mV", "تعمل مضخة الصوديوم-بوتاسيوم على إخراج 3 Na+ وإدخال 2 K+.", "ص 16",
                "🧪 عوامل سرعة السيال العصبي", "• وجود الغمد الميليني (النقل القافز عبر عقد رانفييه) وزيادة قطر المحور.", "ص 20",
                "⚠️ خطأ شائع", "الخلط بين دور أيونات الصوديوم (إزالة الاستقطاب) وأيونات البوتاسيوم (إعادة الاستقطاب)."
            ));
            groups.add(new SummaryGroup(
                "التقانة الحيوية", "الوحدة 6: الهندسة الوراثية والغذاء والبيوجاز",
                "💡 مجالات التقانة الحيوية", "• توظيف الكائنات الدقيقة والإنزيمات لإنتاج الألبان والجبن والأدوية ومعالجة المخلفات لإنتاج غاز الميثان (البيوجاز).", "ص 144",
                "📐 مراحل الهندسة الوراثية للإنسولين", "عزل الجين البشري ← إنزيم القطع ← بلازميد بكتيري ← بكتيريا منتجة للإنسولين", "التخمر اللبني يحوّل سكر اللاكتوز إلى حمض لاكتيك عبر بكتيريا نافعة.", "ص 152",
                "🧪 عوامل نجاح التخمر الغذائي", "• التعقيم وضبط الحرارة ونشاط بادئات التخمير الحيوية.", "ص 149",
                "⚠️ خطأ شائع", "الاعتقاد بأن كل البكتيريا ضارة — الصحيح أن كثيراً منها أساسي لصناعة الألبان والإنسولين الحيوي."
            ));
        } else if ("chemistry".equals(subject)) {
            tvTitle.setText("الكيمياء 3D · الثالث الثانوي");
            groups.add(new SummaryGroup(
                "العناصر الانتقالية", "الوحدة 1: الحديد والكشف عن أملاحه",
                "💡 الخواص والكشف النوعي", "• عناصر الفئة (d) تتعدد حالات تأكسدها؛ يتميز Fe³⁺ باللون الأحمر الدموي مع ثيوسيانات البوتاسيوم KSCN.", "ص 14",
                "📐 معادلات الفرن العالي والكشف", "3Fe₂O₃ + CO → 2Fe₃O₄ + CO₂  |  FeO + CO → Fe + CO₂\nFe³⁺ + 3SCN⁻ → [Fe(SCN)₃] (أحمر دموي)", "يحمي الخمول الكيميائي الحديد من أحماض النيتريك والكبريتيك المركزين.", "ص 18",
                "🧪 الفرق بين الحديد II والحديد III", "• مع NaOH: يعطي Fe²⁺ راسباً أخضر باهتاً Fe(OH)₂ ويعطي Fe³⁺ راسباً بنياً محمراً Fe(OH)₃.", "ص 21",
                "⚠️ خطأ شائع", "اعتقاد أن Fe²⁺ يعطي لوناً أحمر دموياً مع KSCN — الصحيح أن هذا الكشف خاص بالحديد الثلاثي Fe³⁺ فقط."
            ));
            groups.add(new SummaryGroup(
                "الكيمياء الحرارية", "الوحدة 2: التغيرات الحرارية وقانون هس",
                "💡 التفاعلات الطاردة والماصة", "• التفاعل الطارد تخرج منه حرارة (ΔH < 0) مثل NaOH بالماء؛ والماص يمتص حرارة (ΔH > 0) مثل NH₄NO₃.", "ص 31",
                "📐 قانون الحرارة النوعية وهس", "q = m · c · ΔT  |  ΔH°rxn = ΣΔH°f(نواتج) − ΣΔH°f(متفاعلات)", "حرارة التكوين القياسية لأي عنصر نقي في حالته القياسية تساوي صفراً.", "ص 36",
                "🧪 ثبات المركب حرارياً", "• كلما زادت سالبية حرارة التكوين ΔH°f زاد الثبات الحراري للمركب.", "ص 35",
                "⚠️ خطأ شائع", "نسيان عكس إشارة ΔH عند عكس اتجاه المعادلة الحرارية أثناء تطبيق قانون هس."
            ));
            groups.add(new SummaryGroup(
                "الكهربية والعضوية", "الوحدات 3، 6، 7، 8: الخلايا والتقطير والصابون",
                "💡 الخلية الجلفانية والتقطير", "• في خلية دانيال (E°=1.10V): Zn أنود (أكسدة −) و Cu كاثود (اختزال +)؛ ويُفصل النفط بتفاوت درجات الغليان.", "ص 49",
                "📐 قوانين فاراداي والتصبّن", "1 فاراداي = 96,500 كولوم  |  تريستيرين + 3NaOH → صابون + جلسرين", "إضافة محلول NaCl المركز (التمليح) تفصل الصابون وتجعله يطفو فوق الجلسرين.", "ص 158",
                "🧪 الكواشف الحيوية المهمة", "• يكشف عن النشا باليود (أزرق داكن) وعن السكريات المختزلة بفهلنج (راسب Cu₂O أحمر طوبي).", "ص 111",
                "⚠️ خطأ شائع", "الخلط بين شحنة القطب في الجلفانية (المصعد سالب) وفي التحليل الكهربي (المصعد موجب) — الأكسدة عند المصعد دائماً."
            ));
        } else {
            tvTitle.setText("العلوم 9 · الجزء الثاني والأول");
            groups.add(new SummaryGroup(
                "الهالوجينات", "الوحدة 9 و 10: التفاعلات والهالوجينات",
                "💡 مجموعة الهالوجينات (المجموعة 7A)", "• عناصر لافلزية نشطة جداً (الفلور، الكلور، البروم، اليود) تسعى لاكتساب إلكترون واحد.", "ص 26",
                "📐 معادلة تحضير الكلور", "MnO₂ + 4HCl → MnCl₂ + 2H₂O + Cl₂↑", "غاز الكلور أصفر مخضر أثقل من الهواء يُجمع بالإزاحة لأعلى.", "ص 31",
                "🧪 تدرج النشاط في الهالوجينات", "• يقل النشاط الكيميائي كلما اتجهنا لأسفل المجموعة (F > Cl > Br > I).", "ص 34",
                "⚠️ خطأ شائع", "تخيل أن اليود أنشط من الكلور — الصحيح أن الكلور يحل محل البروم واليود في محاليل أملاحهما."
            ));
            groups.add(new SummaryGroup(
                "خواص المادة والضغط", "الوحدة 11 و 12: المرونة، اللزوجة، والضغط",
                "💡 التوتر السطحي والخاصة الشعرية", "• التوتر السطحي يجعل سطح السائل كغشاء مشدود، وتُفسر به حركة الحشرات فوق الماء.", "ص 52",
                "📐 قانون الضغط ومبدأ باسكال", "ض = ق / س (نيوتن/م² = باسكال)\nق₁ / س₁ = ق₂ / س₂", "ضغط السائل يزداد بزيادة العمق والكثافة: ض = ث × جـ × ل.", "ص 68",
                "🧪 عوامل تقليل اللزوجة", "• يقل احتكاك طبقات السائل (اللزوجة) برفع درجة الحرارة مثل تسخين الزيت.", "ص 58",
                "⚠️ خطأ شائع", "الاعتقاد بأن ضغط السائل يعتمد على شكل أو سعة الإناء — الصحيح أنه يعتمد على العمق والكثافة فقط."
            ));
            groups.add(new SummaryGroup(
                "الطاقة والوراثة", "الوحدة 13 و 16: الطاقة الشمسية والوراثة",
                "💡 الخلايا الشمسية وتطبيقات المرايا المقعرة", "• تحول الخلية الضوئية الطاقة الشمسية مباشرة إلى طاقة كهربائية؛ وتُجمع المرايا المقعرة الأشعة في البؤرة.", "ص 92",
                "📐 نسب مندل في الجيلين", "الجيل الأول: 100% سائد هجين (Tt)\nالجيل الثاني: 3 سائد : 1 متنحي", "الجين السائد يظهر أثره بوجود جين واحد فقط.", "ص 136",
                "🧪 عوامل حفظ التوازن الوراثي والبيئي", "• التلقيح الذاتي والخلطي المدروس واستثمار الموارد الحية دون استنزاف.", "ص 110",
                "⚠️ خطأ شائع", "الخلط بين الطراز الجيني (مثل Tt) والطراز المظهري (مثل نبات طويل الساق)."
            ));
        }
    }

    private void renderFilterPills() {
        pillsContainer.removeAllViews();
        for (int i = 0; i < groups.size(); i++) {
            final int idx = i;
            TextView pill = new TextView(this);
            pill.setText(groups.get(i).unitChip);
            boolean active = (i == selectedFilter);
            pill.setBackgroundResource(active ? R.drawable.pill_emerald_btn : R.drawable.card_white_rounded);
            pill.setTextColor(active ? 0xFFFFFFFF : (ThakerStore.isDarkMode(this) ? 0xFFECFAF2 : 0xFF0F291E));
            pill.setTextSize(12);
            pill.getPaint().setFakeBoldText(true);
            pill.setPadding((int) (14 * dp), (int) (7 * dp), (int) (14 * dp), (int) (7 * dp));
            LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-2, -2);
            lp.setMarginEnd((int) (8 * dp));
            pill.setLayoutParams(lp);
            pill.setOnClickListener(new View.OnClickListener() {
                @Override public void onClick(View v) {
                    selectedFilter = idx;
                    renderFilterPills();
                    renderSelectedGroup();
                }
            });
            pillsContainer.addView(pill);
        }
    }

    private void renderSelectedGroup() {
        cardsContainer.removeAllViews();
        if (groups.isEmpty()) return;
        SummaryGroup g = groups.get(Math.min(selectedFilter, groups.size() - 1));
        tvTitle.setText(g.unitTitle);

        addStripedCard(g.defTitle, g.defBody, g.defPage, null, Color.parseColor("#7C3AED"));
        addStripedCard(g.ruleTitle, g.ruleBody, g.rulePage, g.ruleFormula, Color.parseColor("#0284C7"));
        addStripedCard(g.factorTitle, g.factorBody, g.factorPage, null, Color.parseColor("#D97706"));
        addStripedCard(g.errTitle, g.errBody, null, null, Color.parseColor("#EF4444"));
    }

    private void addStripedCard(String title, String body, String pageBadge, String formulaBox, int stripeColor) {
        LinearLayout card = new LinearLayout(this);
        card.setOrientation(LinearLayout.HORIZONTAL);
        card.setBackgroundResource(R.drawable.card_white_rounded);
        card.setElevation(2 * dp);
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-1, -2);
        lp.bottomMargin = (int) (12 * dp);
        card.setLayoutParams(lp);

        View stripe = new View(this);
        stripe.setBackgroundColor(stripeColor);
        stripe.setLayoutParams(new LinearLayout.LayoutParams((int) (6 * dp), -1));
        card.addView(stripe);

        LinearLayout inner = new LinearLayout(this);
        inner.setOrientation(LinearLayout.VERTICAL);
        int pad = (int) (14 * dp);
        inner.setPadding(pad, pad, pad, pad);
        inner.setLayoutParams(new LinearLayout.LayoutParams(0, -2, 1f));

        LinearLayout header = new LinearLayout(this);
        header.setOrientation(LinearLayout.HORIZONTAL);
        header.setGravity(Gravity.CENTER_VERTICAL);

        TextView tvT = new TextView(this);
        tvT.setText(title);
        tvT.setTextColor(stripeColor);
        tvT.setTextSize(15);
        tvT.getPaint().setFakeBoldText(true);
        tvT.setLayoutParams(new LinearLayout.LayoutParams(0, -2, 1f));
        header.addView(tvT);

        if (pageBadge != null && !pageBadge.isEmpty()) {
            TextView tvP = new TextView(this);
            tvP.setText(pageBadge);
            tvP.setBackgroundResource(R.drawable.pill_mint);
            tvP.setTextColor(0xFF065F46);
            tvP.setTextSize(11);
            tvP.getPaint().setFakeBoldText(true);
            tvP.setPadding((int) (9 * dp), (int) (3 * dp), (int) (9 * dp), (int) (3 * dp));
            header.addView(tvP);
        }
        inner.addView(header);

        if (formulaBox != null && !formulaBox.isEmpty()) {
            TextView tvF = new TextView(this);
            tvF.setText(formulaBox);
            tvF.setBackgroundResource(R.drawable.pill_blue_soft);
            tvF.setTextColor(0xFF0C4A6E);
            tvF.setTextSize(14);
            tvF.getPaint().setFakeBoldText(true);
            tvF.setGravity(Gravity.CENTER);
            int fp = (int) (10 * dp);
            tvF.setPadding(fp, fp, fp, fp);
            LinearLayout.LayoutParams flp = new LinearLayout.LayoutParams(-1, -2);
            flp.topMargin = (int) (8 * dp);
            tvF.setLayoutParams(flp);
            inner.addView(tvF);
        }

        if (body != null && !body.isEmpty()) {
            TextView tvB = new TextView(this);
            tvB.setText(body);
            tvB.setTextColor(ThakerStore.isDarkMode(this) ? 0xFFE2E8F0 : 0xFF334155);
            tvB.setTextSize(14);
            tvB.setLineSpacing(4 * dp, 1f);
            tvB.setPadding(0, (int) (8 * dp), 0, 0);
            inner.addView(tvB);
        }

        card.addView(inner);
        cardsContainer.addView(card);
    }
}
