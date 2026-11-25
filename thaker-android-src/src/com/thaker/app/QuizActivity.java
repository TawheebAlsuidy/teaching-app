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

        bank.add(new Question("p12_1", "متوسط · الفيزياء 12",
            "عند إطلاق مقذوف بنفس السرعة الابتدائية، فإنه يبلغ أقصى مدى أفقي عندما تكون زاوية الإطلاق:",
            new String[]{"30°", "45°", "60°", "90°"}, 1,
            "المدى الأفقي يعتمد على جا(2θ) وتبلغ قيمته العظمى (1) عندما 2θ = 90° أي θ = 45°.", "physics-12th-book.html", 24));
        bank.add(new Question("b12_1", "متوسط · الأحياء 12",
            "ما قيمة جهد الراحة لغشاء الليف العصبي (العصبون) في الحالة الطبيعية قبل الإثارة؟",
            new String[]{"+30 ملي فولت", "-70 ملي فولت", "صفر ملي فولت", "-120 ملي فولت"}, 1,
            "يكون السطح الخارجي موجباً والداخلي سالباً بفرق جهد قدره -70 mV بفضل مضخة Na+/K+.", "biology-12th-book.html", 14));
        bank.add(new Question("c12_1", "سهل · الكيمياء 12",
            "العناصر التي يتم فيها امتلاء المستوى الفرعي (d) بالإلكترونات بالتتابع هي عناصر الفئة:",
            new String[]{"العناصر الممثلة", "العناصر الانتقالية الرئيسية", "الغازات النبيلة", "اللانثانيدات"}, 1,
            "العناصر الانتقالية الرئيسية تقع وسط الجدول الدوري وتتميز بتعدد حالات تأكسدها.", "chem-lab-book.html", 1));
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

        String unitKey = "phys_12".equals(quizSubject) ? "phys_u1" : ("bio_12".equals(quizSubject) ? "bio_u1" : "u9");
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
