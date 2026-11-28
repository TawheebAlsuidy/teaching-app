package com.thaker.app;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.ProgressBar;
import android.widget.TextView;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class QuizActivity extends Activity {

    public static class Question {
        String id, unitBadge, text, explanation, reviewAsset;
        String[] options;
        int correctIdx, reviewPage;

        public Question(String id, String unitBadge, String text, String[] options, int correctIdx,
                        String explanation, String reviewAsset, int reviewPage) {
            this.id = id;
            this.unitBadge = unitBadge;
            this.text = text;
            this.options = options;
            this.correctIdx = correctIdx;
            this.explanation = explanation;
            this.reviewAsset = reviewAsset;
            this.reviewPage = reviewPage;
        }
    }

    private String quizSubject = "sci_p2";
    private boolean reviewWrongOnly = false;
    private final List<Question> questions = new ArrayList<Question>();
    private int curIndex = 0;
    private int score = 0;
    private boolean answered = false;

    private TextView tvSubject, tvProgress, tvScoreTop, tvUnitBadge, tvQuestion, tvExplainHeader, tvExplainBody;
    private ProgressBar progQuizBar;
    private final Button[] btnOpts = new Button[4];
    private LinearLayout cardExplain;
    private Button btnNext, btnReviewPage, btnTryLab;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_quiz);

        String sub = getIntent().getStringExtra("quiz_subject");
        if (sub != null && !sub.isEmpty()) quizSubject = sub;
        reviewWrongOnly = getIntent().getBooleanExtra("review_wrong", false);

        tvSubject = findViewById(R.id.tv_quiz_subject);
        tvProgress = findViewById(R.id.tv_quiz_progress);
        tvScoreTop = findViewById(R.id.tv_quiz_score_top);
        tvUnitBadge = findViewById(R.id.tv_quiz_unit_badge);
        tvQuestion = findViewById(R.id.tv_question_text);
        progQuizBar = findViewById(R.id.prog_quiz_bar);

        btnOpts[0] = findViewById(R.id.btn_opt_0);
        btnOpts[1] = findViewById(R.id.btn_opt_1);
        btnOpts[2] = findViewById(R.id.btn_opt_2);
        btnOpts[3] = findViewById(R.id.btn_opt_3);

        cardExplain = findViewById(R.id.card_explanation);
        tvExplainHeader = findViewById(R.id.tv_explain_header);
        tvExplainBody = findViewById(R.id.tv_explain_body);
        btnReviewPage = findViewById(R.id.btn_quiz_review_page);
        btnTryLab = findViewById(R.id.btn_quiz_try_lab);
        btnNext = findViewById(R.id.btn_quiz_next);

        findViewById(R.id.btn_quiz_back).setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) { finish(); }
        });

        for (int i = 0; i < 4; i++) {
            final int idx = i;
            btnOpts[i].setOnClickListener(new View.OnClickListener() {
                @Override public void onClick(View v) { handleAnswer(idx); }
            });
        }

        btnNext.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                curIndex++;
                displayCurrentQuestion();
            }
        });

        loadQuestions();
        displayCurrentQuestion();
    }

    private List<Question> buildAllQuestions() {
        List<Question> bank = new ArrayList<Question>();
        bank.add(new Question("sp2_1", "سهل · الوحدة 10: الهالوجينات",
            "ما الخاصية المشتركة بين جميع عناصر الهالوجينات (المجموعة 7A) في الجدول الدوري؟",
            new String[]{"لها 7 إلكترونات في المدار الأخير وتميل لاكتساب إلكترون", "غازات خاملة لا تتفاعل إطلاقاً", "فلزات قلوية موصلة جيدة جداً للكهرباء", "درجة انصهارها أعلى من الحديد"}, 0,
            "تمتلك الهالوجينات 7 إلكترونات تكافؤ فتسعى بقوة لاكتساب إلكترون واحد للوصول للاستقرار.", "thaker-interactive-book.html", 27));
        bank.add(new Question("sp2_2", "متوسط · تحضير الكلور",
            "عند تسخين ثاني أكسيد المنغنيز (MnO₂) مع حمض الهيدروكلوريك المركز يتصاعد غاز:",
            new String[]{"الهيدروجين", "الكلور الأصفر المخضر", "الأكسجين", "النيتروجين"}, 1,
            "MnO₂ + 4HCl → MnCl₂ + 2H₂O + Cl₂↑ ويُجمع غاز الكلور بإزاحة الهواء لأعلى.", "thaker-interactive-book.html", 31));
        bank.add(new Question("sp2_3", "سهل · الوحدة 11: خواص الأجسام",
            "السبب الفيزيائي لقدرة بعض الحشرات الخفيفة على المشي فوق سطح الماء دون أن تغوص هو:",
            new String[]{"ظاهرة التوتر السطحي", "انخفاض كثافة الهواء", "القوة النووية", "ضعف الجاذبية"}, 0,
            "تجذب جزيئات سطح السائل بعضها البعض للداخل فتشكّل طبقة تشبه الغشاء المشدود.", "thaker-interactive-book.html", 53));
        bank.add(new Question("sp2_4", "متوسط · الوحدة 12: الضغط والموائع",
            "إذا ضاعفنا عمق نقطة داخل سائل ساكن متجانس فإن ضغط السائل عند تلك النقطة:",
            new String[]{"يبقى ثابتاً", "يقل إلى النصف", "يتضاعف", "ينعدم"}, 2,
            "ضغط السائل يتناسب طردياً مع العمق حسب العلاقة: ض = ث × جـ × ل.", "thaker-interactive-book.html", 69));
        bank.add(new Question("sp2_5", "سهل · الوحدة 16: الوراثة ومندل",
            "إذا تزاوج نباتا بازلاء كلاهما طويل الساق هجين (Tt × Tt)، فنسبة النباتات قصيرة الساق في الجيل الناتج هي:",
            new String[]{"25% (1 من 4)", "50%", "75%", "100%"}, 0,
            "ينتج من التزاوج: TT , Tt , Tt , tt فتكون نسبة المتنحي (tt) 1 إلى 3 (25%).", "thaker-interactive-book.html", 136));

        bank.add(new Question("sp1_1", "سهل · المحاليل",
            "المحلول الذي لا يستطيع إذابة أي كمية إضافية من المذاب عند درجة حرارة معينة يُسمى:",
            new String[]{"المحلول غير المشبع", "المحلول المشبع", "المحلول المخفف", "المعلق"}, 1,
            "يصل المحلول للتشبع عندما تتوازن سرعة الذوبان مع سرعة الترسيب عند ثبوت الحرارة.", "science-9th-book.html", 1));
        bank.add(new Question("sp1_2", "سهل · الضوء والرؤية",
            "المرآة الكروية التي تُكوّن دائماً صورة تقديرية مصغرة ومعتدلة وتوضع على جانبي السيارة هي:",
            new String[]{"المرآة المقعرة", "المرآة المحدبة", "المرآة المستوية", "العدسة المحدبة"}, 1,
            "المرآة المحدبة تفرق الأشعة فتوسّع مجال الرؤية خلف السائق.", "science-9th-book.html", 1));
        bank.add(new Question("sp1_3", "متوسط · الإخراج",
            "الوحدة الوظيفية الأساسية لترشيح الدم وتكوين البول في كلية الإنسان هي:",
            new String[]{"الحالب", "النفرون (الأنبوبة البولية)", "المثانة", "حوض الكلية"}, 1,
            "تضم كل كلية قرابة مليون نفرون تقوم بترشيح الدم واستعادة المواد المفيدة.", "science-9th-book.html", 1));

        bank.add(new Question("mp1_1", "سهل · التحليل الجبري",
            "تحليل المقدار الجبري (س² − 25) تحليلاً كاملاً يساوي:",
            new String[]{"(س − 5)(س − 5)", "(س + 5)(س − 5)", "(س + 25)(س − 1)", "س(س − 25)"}, 1,
            "فرق بين مربعين: أ² − ب² = (أ − ب)(أ + ب).", "math-9th-book.html", 1));
        bank.add(new Question("mp1_2", "متوسط · مجموع المكعبين",
            "تحليل المقدار (س³ + 8) يساوي:",
            new String[]{"(س + 2)(س² − 2س + 4)", "(س + 2)(س² + 2س + 4)", "(س − 2)(س² + 2س + 4)", "(س + 2)³"}, 0,
            "مجموع مكعبين: (س + أ)(س² − أس + أ²) مع عكس إشارة الحد الأوسط.", "math-9th-book.html", 1));
        bank.add(new Question("mp2_1", "سهل · الدائرة",
            "قياس الزاوية المحيطية المرسومة في دائرة يساوي دائماً بالنسبة للمركزية المشتركة معها في القوس:",
            new String[]{"ضعف المركزية", "نصف المركزية", "يساوي المركزية", "90 درجة دائماً"}, 1,
            "مبرهنة أساسية: قياس الزاوية المحيطية = ½ قياس الزاوية المركزية المشتركة في نفس القوس.", "math-9th-book.html", 1));
        bank.add(new Question("mp2_2", "متوسط · حساب المثلثات",
            "في المثلث القائم، قيمة (جتا 60° + جا 30°) تساوي:",
            new String[]{"½", "1", "√3", "2"}, 1,
            "بما أن جا 30° = ½ وجتا 60° = ½، فإن مجموعهما = ½ + ½ = 1.", "math-9th-book.html", 1));

        bank.add(new Question("m12_1", "سهل · الأعداد المركبة 12",
            "القيمة المطلقة للعدد المركب 3 + 4i تساوي:",
            new String[]{"5", "7", "√7", "25"}, 0,
            "|3 + 4i| = √(3² + 4²) = √25 = 5، وهي طول المتجه في مستوى أرغاند.", "math-12th-book.html", 18));
        bank.add(new Question("m12_2", "متوسط · مبرهنة دي موافر",
            "إذا كان z = cosθ + i sinθ فإن z⁵ يساوي:",
            new String[]{"cos5θ − i sin5θ", "5cosθ + 5i sinθ", "cos5θ + i sin5θ", "cosθ⁵ + i sinθ⁵"}, 2,
            "تنص مبرهنة دي موافر على (cosθ + i sinθ)ⁿ = cos nθ + i sin nθ، إذن z⁵ = cos5θ + i sin5θ.", "math-12th-book.html", 67));
        bank.add(new Question("m12_3", "متوسط · القطوع المخروطية",
            "بؤرة القطع المكافئ y² = 20x تقع عند النقطة:",
            new String[]{"(5, 0)", "(10, 0)", "(0, 5)", "(−5, 0)"}, 0,
            "بمقارنة y² = 20x مع y² = 4px نجد 4p = 20 إذن p = 5، فالبؤرة (p,0) = (5,0).", "math-12th-book.html", 117));
        bank.add(new Question("m12_4", "سهل · المشتقات",
            "مشتقة الدالة f(x) = xⁿ بالنسبة إلى x هي:",
            new String[]{"nxⁿ", "nxⁿ⁻¹", "xⁿ⁻¹", "n⁻¹xⁿ⁺¹"}, 1,
            "قاعدة القوة تنص على أن (xⁿ)′ = nxⁿ⁻¹ لأي أس n ثابت.", "math-12th-book.html", 156));
        bank.add(new Question("m12_5", "متوسط · التكامل المحدد",
            "قيمة التكامل ∫₀² (2 − x/2) dx تساوي:",
            new String[]{"2", "3", "4", "5"}, 1,
            "المضاد هو 2x − x²/4، وبالتعويض: (4 − 1) − 0 = 3.", "math-12th-book.html", 246));
        bank.add(new Question("lit_1", "سهل · الأدب والنصوص",
            "أي عنوان نص شعري ارتبط بالشاعر شمس الدين الكوفي في الفهرس؟",
            new String[]{"في رثاء بغداد", "وصف السفينة", "الرجولة", "مسمار جحا"}, 0,
            "الفهرس يذكر «في رثاء بغداد / شمس الدين الكوفي / شعر» في ص 14.", "arabic-literature-12th-book.html", 14));
        bank.add(new Question("lit_2", "سهل · الأدب والنصوص",
            "ما نوع نص «وصف السفينة» كما ورد في الفهرس؟",
            new String[]{"شعر", "نثر", "مسرحية", "مقالة"}, 1,
            "الفهرس يصنّف «وصف السفينة / ابن حبيب الحلبي» ضمن النثر في ص 17.", "arabic-literature-12th-book.html", 17));
        bank.add(new Question("lit_3", "متوسط · النقد الأدبي",
            "أي موضوع يبدأ في الصفحة 173 من كتاب الأدب والنصوص؟",
            new String[]{"الأسلوب", "النقد الأدبي", "القصة", "المقالة"}, 1,
            "الفهرس يثبت أن «النقد الأدبي» يبدأ في ص 173.", "arabic-literature-12th-book.html", 173));
        bank.add(new Question("lit_4", "متوسط · النقد الأدبي",
            "ما الموضوع الذي يلي «الأسلوب» مباشرة في فهرس النقد الأدبي؟",
            new String[]{"الشكل والمضمون", "التجربة الشعرية", "النص المسرحي", "النقد الأدبي"}, 0,
            "الفهرس يرتب الموضوعات: النقد الأدبي ص 173، الأسلوب ص 180، ثم الشكل والمضمون ص 184.", "arabic-literature-12th-book.html", 184));
        bank.add(new Question("lit_5", "متوسط · الأدب والنصوص",
            "بمن ارتبط عنوان «مسمار جحا» في فهرس الكتاب؟",
            new String[]{"نجيب الكيلاني", "فدوى طوقان", "علي أحمد باكثير", "ميخائيل نعيمة"}, 2,
            "الفهرس يذكر «مسمار جحا / علي أحمد باكثير / نثر» في ص 164.", "arabic-literature-12th-book.html", 164));
        bank.add(new Question("p12_1", "متوسط · الفيزياء 12",
            "عند إطلاق مقذوف بنفس السرعة الابتدائية، فإنه يبلغ أقصى مدى أفقي عندما تكون زاوية الإطلاق:",
            new String[]{"30°", "45°", "60°", "90°"}, 1,
            "المدى الأفقي يعتمد على جا(2θ) وتبلغ قيمته العظمى (1) عندما 2θ = 90° أي θ = 45°.", "physics-12th-book.html", 24));
        bank.add(new Question("p12_2", "متوسط · التيار المتردد",
            "في دائرة RLC على التوالي عند تردد الرنين الكهربائي (f₀)، تكون المعاوقة الكلية للدائرة:",
            new String[]{"أكبر ما يمكن وتساوي XL + Xc", "أقل ما يمكن وتساوي المقاومة الأومية فقط (R)", "مساوية للصفر دائماً", "سعوية خالصة"}, 1,
            "عند الرنين تتساوى XL و Xc وتلغي كل منهما الأخرى فتصبح M = R ويمر أعظم تيار كهربائي.", "physics-12th-book.html", 51));
        bank.add(new Question("p12_3", "سهل · الإلكترونيات",
            "في الترانزستور npn، إذا كان تيار القاعدة 50 ميكروأمبير ومعامل التكبير β = 100 فإن تيار المجمع يساوي:",
            new String[]{"0.5 مللي أمبير", "5 مللي أمبير", "50 مللي أمبير", "500 أمبير"}, 1,
            "ت_مجمع = β × ت_قاعدة = 100 × 50 μA = 5000 μA = 5 mA.", "physics-12th-book.html", 75));
        bank.add(new Question("b12_1", "متوسط · الأحياء 12",
            "ما قيمة جهد الراحة لغشاء الليف العصبي (العصبون) في الحالة الطبيعية قبل الإثارة؟",
            new String[]{"+30 ملي فولت", "-70 ملي فولت", "صفر ملي فولت", "-120 ملي فولت"}, 1,
            "يكون السطح الخارجي موجباً والداخلي سالباً بفرق جهد قدره -70 mV بفضل مضخة Na+/K+.", "biology-12th-book.html", 15));
        bank.add(new Question("b12_2", "سهل · التقانة الحيوية",
            "تُنتَج البكتيريا المعدلة وراثياً هرمون الإنسولين البشري بعد إدخال جين الإنسولين إلى حلقة الحمض النووي المسماة:",
            new String[]{"الريبوسوم", "البلازميد البكتيري", "الميتوكندريا", "الجدار الخلوي"}, 1,
            "تُستخدم البلازميدات البكتيرية كنواقل جينية لإدخال الجين البشري وإنتاج الإنسولين بكميات نقية.", "biology-12th-book.html", 152));
        bank.add(new Question("b12_3", "متوسط · الوراثة الجزيئية",
            "أي من القواعد النيتروجينية الآتية توجد في جزيء RNA بدلاً من الثايمين (T) في DNA؟",
            new String[]{"الأدينين (A)", "الجوانين (G)", "اليوراسيل (U)", "السيتوسين (C)"}, 2,
            "يتميز حمض RNA بوجود قاعدة اليوراسيل (U) بدلاً من الثايمين (T) وسكر الريبوز بدلاً من الريبوز منقوص الأكسجين.", "biology-12th-book.html", 136));
        bank.add(new Question("c12_1", "سهل · الكيمياء 12",
            "العناصر التي يتم فيها امتلاء المستوى الفرعي (d) بالإلكترونات بالتتابع هي عناصر الفئة:",
            new String[]{"العناصر الممثلة", "العناصر الانتقالية الرئيسية", "الغازات النبيلة", "اللانثانيدات"}, 1,
            "العناصر الانتقالية الرئيسية تقع وسط الجدول الدوري وتتميز بتعدد حالات تأكسدها.", "chemistry-12th-book.html", 12));
        bank.add(new Question("c12_2", "متوسط · الكيمياء الحرارية",
            "عند إذابة ملح نترات الأمونيوم (NH₄NO₃) في الماء تنخفض درجة حرارة المحلول لأن الذوبان:",
            new String[]{"طارد للحرارة ΔH < 0", "ماص للحرارة ΔH > 0", "متعادل حرارياً", "لا يغير طاقة الروابط"}, 1,
            "ذوبان NH₄NO₃ ماص للحرارة (ΔH = +25.7 kJ/mol) فيمتص الحرارة من المحيط ويبرد الإناء.", "chemistry-12th-book.html", 31));
        bank.add(new Question("c12_3", "متوسط · الكيمياء الكهربائية",
            "في الخلية الجلفانية (خلية دانيال Zn/Cu) تحدث عملية الأكسدة عند:",
            new String[]{"قطب النحاس (الكاثود)", "قطب الخارصين (الأنود السالب)", "القنطرة الملحية", "داخل المصباح"}, 1,
            "يتأكسد الخارصين عند المصعد Zn → Zn²⁺ + 2e⁻ وتختزل أيونات النحاس عند المهبط بجهد 1.10V.", "chemistry-12th-book.html", 49));
        bank.add(new Question("c12_4", "متوسط · الكيمياء الحيوية",
            "للكشف المخبري عن النشا على البارد والتمييز بين الجلوكوز والسكروز نستخدم على التوالي:",
            new String[]{"محلول اليود للنشا ومحلول فهلنج للسكريات", "محلول الملح NaCl والأسيتون", "الأمونيا وكبريتات النحاس فقط", "برمنجنات البوتاسيوم"}, 0,
            "يعطي اليود لوناً أزرق داكناً مع النشا، ويختزل الجلوكوز فهلنج لراسب أحمر طوبي Cu₂O دون السكروز.", "chemistry-12th-book.html", 111));
        bank.add(new Question("c12_5", "سهل · الذهب الأسود والصناعات",
            "المبدأ العلمي الذي تُفصل به مكونات النفط الخام داخل برج التقطير التجزيئي هو:",
            new String[]{"الاختلاف في درجات الغليان والأوزان الجزيئية", "تفاعل التصبّن بالقلويات", "الاندماج النووي", "الطلاء بالفضة"}, 0,
            "تتصاعد الغازات والجازولين إلى القمة لانخفاض درجة غليانها وتتكثف الأجزاء الثقيلة كالإسفلت أسفل البرج.", "chemistry-12th-book.html", 131));
        bank.add(new Question("qur_1", "سهل · سورة النور",
            "كم جلدة حُدِّدَتْ عقوبةً لقاذف المحصنات الغافلات إذا لم يأتِ بأربعة شهداء في مطلع سورة النور؟",
            new String[]{"أربعون جلدة", "ثمانون جلدة", "مائة جلدة", "ستون جلدة"}, 1,
            "فرض الله في آية القذف من سورة النور عقوبة ثمانين جلدة وردَّ شهادة القاذف حتى يتوب صيانةً للأعراض.", "quran-12th-book.html", 11));
        bank.add(new Question("qur_2", "متوسط · حادثة الإفك",
            "في طريق العودة من أي غزوة وقعت حادثة الإفك التي برَّأ الله أمَّ المؤمنين عائشة رضي الله عنها من فوق سبع سماوات؟",
            new String[]{"غزوة تبوك", "غزوة بني المصطلق (المريسيع)", "غزوة خيبر", "غزوة حنين"}, 1,
            "وقعت حادثة الإفك أثناء عودة الجيش من غزوة بني المصطلق (المريسيع) في السنة الخامسة أو السادسة للهجرة.", "quran-12th-book.html", 21));
        bank.add(new Question("qur_3", "سهل · آداب الاستئذان",
            "كم مرة يُشرع الاستئذان عند دخول البيوت غير المسكونة أو بيوت الغير قبل الرجوع إذا لم يُؤذن؟",
            new String[]{"مرة واحدة", "مرتان", "ثلاث مرات", "خمس مرات"}, 2,
            "الاستئذان ثلاث مرات، فإن أُذن وإلا رجع كما صح عن النبي ﷺ وشُرح في آداب سورة النور.", "quran-12th-book.html", 40));
        bank.add(new Question("qur_4", "متوسط · علوم القرآن",
            "الصحابي الذي أشار على الخليفة أبي بكر الصديق رضي الله عنه بجمع القرآن بعد استشهاد القرّاء في اليمامة هو:",
            new String[]{"عثمان بن عفان", "عمر بن الخطاب", "زيد بن ثابت", "معاذ بن جبل"}, 1,
            "أشار عمر بن الخطاب على أبي بكر الصديق رضي الله عنهما بجمع القرآن، وكلّف أبو بكر زيد بن ثابت رضي الله عنه بهذه المهمة.", "quran-12th-book.html", 88));
        bank.add(new Question("qur_5", "متوسط · التلاوة والتجويد",
            "تتميز سورة التوبة في مطلعها ضمن منهج التلاوة بأنها:",
            new String[]{"تُفتتح بسكتة طويلة قبل البسملة", "تخلو من البسملة في أولها", "تُقرأ بالإمالة الكاملة في فواتحها", "تُختم بسجدة تلاوة واجبة"}, 1,
            "سورة التوبة هي السورة الوحيدة التي تُقرأ من أولها دون البسملة، وتبدأ مباشرة بالبراءة.", "quran-12th-book.html", 139));
        return bank;
    }

    private void loadQuestions() {
        questions.clear();
        List<Question> all = buildAllQuestions();
        if (reviewWrongOnly) {
            List<String> wrongIds = ThakerStore.getWrongIds(this);
            tvSubject.setText("مراجعة أخطائي (" + wrongIds.size() + ")");
            for (Question q : all) {
                if (wrongIds.contains(q.id)) questions.add(q);
            }
        }
        if (questions.isEmpty()) {
            String prefix = null;
            if ("sci_p2".equals(quizSubject)) prefix = "sp2_";
            else if ("sci_p1".equals(quizSubject)) prefix = "sp1_";
            else if ("math_p1".equals(quizSubject) || "math_p2".equals(quizSubject)) prefix = "mp";
            else if ("math_12".equals(quizSubject)) prefix = "m12_";
            else if ("arabic_lit".equals(quizSubject)) prefix = "lit_";
            else if ("quran".equals(quizSubject)) prefix = "qur_";
            else if ("phys_12".equals(quizSubject)) prefix = "p12_";
            else if ("bio_12".equals(quizSubject)) prefix = "b12_";
            else if ("chem_12".equals(quizSubject)) prefix = "c12_";

            for (Question q : all) {
                if (prefix == null || q.id.startsWith(prefix)) questions.add(q);
            }
            if (questions.size() < 4) {
                for (Question q : all) {
                    if (!questions.contains(q)) questions.add(q);
                    if (questions.size() >= 6) break;
                }
            }
            Collections.shuffle(questions);
        }
    }

    private void displayCurrentQuestion() {
        if (curIndex >= questions.size()) {
            showFinalResults();
            return;
        }
        answered = false;
        final Question q = questions.get(curIndex);

        if (!reviewWrongOnly) tvSubject.setText("اختبر نفسك · تدريب");
        tvProgress.setText((curIndex + 1) + " / " + questions.size());
        tvScoreTop.setText("النقاط: " + score);
        tvUnitBadge.setText(q.unitBadge);
        tvQuestion.setText(q.text);
        progQuizBar.setProgress((int) (((curIndex + 1) * 100f) / Math.max(1, questions.size())));

        cardExplain.setVisibility(View.GONE);
        btnNext.setVisibility(View.GONE);

        String[] letters = {"أ", "ب", "ج", "د"};
        int textColor = ThakerStore.isDarkMode(this) ? 0xFFECFAF2 : 0xFF0F291E;
        for (int i = 0; i < 4; i++) {
            btnOpts[i].setEnabled(true);
            btnOpts[i].setBackgroundResource(R.drawable.quiz_opt_default);
            btnOpts[i].setTextColor(textColor);
            btnOpts[i].setText(letters[i] + " )  " + q.options[i]);
        }

        btnReviewPage.setText("📖 راجع ص " + q.reviewPage);
        View.OnClickListener goBook = new View.OnClickListener() {
            @Override public void onClick(View v) {
                Intent i = new Intent(QuizActivity.this, LabActivity.class);
                i.putExtra("html_asset", q.reviewAsset);
                i.putExtra("start_page", q.reviewPage);
                i.putExtra("start_tab", "reader");
                startActivity(i);
            }
        };
        btnReviewPage.setOnClickListener(goBook);
        btnTryLab.setOnClickListener(goBook);
    }

    private void handleAnswer(int selectedIdx) {
        if (answered) return;
        answered = true;
        Question q = questions.get(curIndex);

        for (Button b : btnOpts) b.setEnabled(false);

        if (selectedIdx == q.correctIdx) {
            score++;
            ThakerStore.removeWrongId(this, q.id);
            btnOpts[selectedIdx].setBackgroundResource(R.drawable.quiz_opt_right);
            btnOpts[selectedIdx].setTextColor(0xFF065F46);
            btnOpts[selectedIdx].setText("✓  " + btnOpts[selectedIdx].getText());
            tvExplainHeader.setText("✓ إجابة صحيحة! أحسنت");
            tvExplainHeader.setTextColor(0xFF065F46);
        } else {
            ThakerStore.addWrongId(this, q.id);
            btnOpts[selectedIdx].setBackgroundResource(R.drawable.quiz_opt_wrong);
            btnOpts[selectedIdx].setTextColor(0xFF991B1B);
            btnOpts[selectedIdx].setText("✕  " + btnOpts[selectedIdx].getText());

            btnOpts[q.correctIdx].setBackgroundResource(R.drawable.quiz_opt_right);
            btnOpts[q.correctIdx].setTextColor(0xFF065F46);
            btnOpts[q.correctIdx].setText("✓  " + btnOpts[q.correctIdx].getText());
            tvExplainHeader.setText("✕ لماذا أخطأت؟ · الحل الصحيح");
            tvExplainHeader.setTextColor(0xFF991B1B);
        }

        tvScoreTop.setText("النقاط: " + score);
        tvExplainBody.setText(q.explanation);
        cardExplain.setVisibility(View.VISIBLE);
        btnNext.setVisibility(View.VISIBLE);
        btnNext.setText(curIndex == questions.size() - 1 ? "عرض النتيجة النهائية 🏆" : "السؤال التالي  ←");
    }

    private void showFinalResults() {
        int total = Math.max(1, questions.size());
        int pct = (score * 100) / total;
        ThakerStore.setTaskDone(this, 2, true);
        ThakerStore.bumpStudyStreak(this);

        String unitKey = "phys_12".equals(quizSubject) ? "phys_u1" : ("bio_12".equals(quizSubject) ? "bio_u1" : ("quran".equals(quizSubject) ? "quran_s1" : "u9"));
        ThakerStore.setUnitMastery(this, unitKey, pct >= 80 ? 3 : (pct >= 50 ? 2 : 1));

        String gradeMsg = pct >= 85 ? "ممتاز! إتقان رائع 🌟" : (pct >= 60 ? "جيد جداً! واصل التقدم 👍" : "تحتاج مراجعة بسيطة، أخطاؤك محفوظة للتدرب 💪");
        new AlertDialog.Builder(this)
            .setTitle("النتيجة النهائية 🏆")
            .setMessage("درجتك: " + score + " من " + total + " (" + pct + "%)\n\n" + gradeMsg)
            .setPositiveButton("إعادة التدريب", new DialogInterface.OnClickListener() {
                @Override public void onClick(DialogInterface dialog, int which) {
                    curIndex = 0; score = 0; loadQuestions(); displayCurrentQuestion();
                }
            })
            .setNegativeButton("عودة", new DialogInterface.OnClickListener() {
                @Override public void onClick(DialogInterface dialog, int which) { finish(); }
            }).setCancelable(false).show();
    }
}
