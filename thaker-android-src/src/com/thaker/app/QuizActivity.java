package com.thaker.app;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class QuizActivity extends Activity {

    public static class Question {
        String text;
        String[] options;
        int correctIdx;
        String explanation;

        public Question(String text, String[] options, int correctIdx, String explanation) {
            this.text = text;
            this.options = options;
            this.correctIdx = correctIdx;
            this.explanation = explanation;
        }
    }

    private String quizSubject = "sci_p1";
    private List<Question> questions = new ArrayList<Question>();
    private int curIndex = 0;
    private int score = 0;
    private boolean answered = false;

    private TextView tvSubject;
    private TextView tvProgress;
    private TextView tvScoreTop;
    private TextView tvQuestion;
    private Button[] btnOpts = new Button[4];
    private LinearLayout cardExplain;
    private TextView tvExplainHeader;
    private TextView tvExplainBody;
    private Button btnNext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_quiz);

        quizSubject = getIntent().getStringExtra("quiz_subject");
        if (quizSubject == null) quizSubject = "sci_p1";

        tvSubject = findViewById(R.id.tv_quiz_subject);
        tvProgress = findViewById(R.id.tv_quiz_progress);
        tvScoreTop = findViewById(R.id.tv_quiz_score_top);
        tvQuestion = findViewById(R.id.tv_question_text);

        btnOpts[0] = findViewById(R.id.btn_opt_0);
        btnOpts[1] = findViewById(R.id.btn_opt_1);
        btnOpts[2] = findViewById(R.id.btn_opt_2);
        btnOpts[3] = findViewById(R.id.btn_opt_3);

        cardExplain = findViewById(R.id.card_explanation);
        tvExplainHeader = findViewById(R.id.tv_explain_header);
        tvExplainBody = findViewById(R.id.tv_explain_body);
        btnNext = findViewById(R.id.btn_quiz_next);

        findViewById(R.id.btn_quiz_back).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });

        loadQuestions();
        displayCurrentQuestion();
    }

    private void loadQuestions() {
        questions.clear();

        if ("sci_p1".equals(quizSubject) || "all_9th".equals(quizSubject)) {
            questions.add(new Question("المحلول الذي لا يستطيع إذابة أي كمية إضافية من المذاب عند درجة حرارة معينة يُسمى:",
                new String[]{"المحلول غير المشبع", "المحلول المشبع", "المحلول فوق المشبع", "المحلول المعلق"}, 1,
                "المحلول المشبع يحتوي على أقصى كمية ممكنة من المذاب عند ثبوت درجة الحرارة."));

            questions.add(new Question("تُقاس سرعة الصوت في الهواء الجاف عند درجة الصفر المئوي بحوالي:",
                new String[]{"331 م/ث", "500 م/ث", "1500 م/ث", "300000 كم/ث"}, 0,
                "سرعة الصوت في الهواء عند صفر مئوي هي 331 م/ث وتزداد بارتفاع درجة الحرارة."));

            questions.add(new Question("المرآة الكروية التي تُكوّن دائماً صورة تقديرية مصغرة ومعتدلة للأجسام هي:",
                new String[]{"المرآة المقعرة", "المرآة المحدبة", "المرآة المستوية", "المرآة الأسطوانية"}, 1,
                "المرآة المحدبة تفرق الأشعة وتُستخدم على جانبي السيارة لكشف مساحة أوسع."));

            questions.add(new Question("الوحدة الوظيفية الأساسية للإخراج وتنقية الدم في كلية الإنسان هي:",
                new String[]{"الحالب", "النفرون (الأنبوبة البولية)", "حوض الكلية", "المثانة"}, 1,
                "تحتوي كل كلية على حوالي مليون نفرون يقوم بترشيح الدم واستعادة المواد النافعة."));

            questions.add(new Question("التكاثر الخضري في النباتات يتميز بأنه:",
                new String[]{"ينتج أفراداً متطابقة مع النبات الأصلي", "يتطلب وجود حبوب اللقاح", "يؤدي لتنوع وراثي كبير", "يتم فقط عن طريق البذور"}, 0,
                "التكاثر الخضري هو تكاثر لا جنسي يُحافظ على الصفات الممتازة للنبات الأم."));
        }

        if ("sci_p2".equals(quizSubject) || "all_9th".equals(quizSubject)) {
            questions.add(new Question("ينص قانون أوم في الكهرباء على أن شدة التيار (ت) تتناسب طردياً مع فرق الجهد (جـ) وعكسياً مع:",
                new String[]{"المقاومة الكهربائية (م)", "القدرة الكهربائية", "الطاقة المستهلكة", "الشحنة الكهربائية"}, 0,
                "قانون أوم: جـ = ت × م، فكلما زادت المقاومة قلّ التيار الكهربائي."));

            questions.add(new Question("الجهاز الذي يحول الطاقة الميكانيكية الحركية إلى طاقة كهربائية هو:",
                new String[]{"المحرك الكهربائي", "المولد الكهربائي (الدينامو)", "المحول الكهربائي", "المكثف"}, 1,
                "المولد يعمل بظاهرة الحث الكهرومغناطيسي لفاراداي لتوليد التيار."));

            questions.add(new Question("أقرب الكواكب إلى الشمس في نظامنا الشمسي هو:",
                new String[]{"الزهرة", "المريخ", "عطارد", "الأرض"}, 2,
                "عطارد هو أصغر وأقرب الكواكب للشمس ويدور حولها في 88 يوماً."));

            questions.add(new Question("الصخور المتكونة من تبريد وتبلور الماغما في باطن الأرض أو اللابة على سطحها هي:",
                new String[]{"الصخور الرسوبية", "الصخور النارية", "الصخور المتحولة", "الصخور الطينية"}, 1,
                "الصخور النارية مثل البازلت والجرانيت هي أصل جميع الصخور في القشرة الأرضية."));
        }

        if ("math_p1".equals(quizSubject) || "all_9th".equals(quizSubject)) {
            questions.add(new Question("العلاقة التي تتصف بأنها انعكاسية ومتماثلة ومتعدية تُسمى:",
                new String[]{"علاقة ترتيب جزئي", "علاقة تكافؤ", "علاقة عكسية", "تطبيق شامل"}, 1,
                "علاقة التكافؤ تجمع الخواص الثلاث: الانعكاس والتماثل والتعدي."));

            questions.add(new Question("تحليل المقدار الجبري (س² − 25) هو:",
                new String[]{"(س − 5)(س − 5)", "(س + 5)(س − 5)", "(س + 25)(س − 1)", "س(س − 25)"}, 1,
                "الفرق بين مربعين: أ² − ب² = (أ − ب)(أ + ب)."));

            questions.add(new Question("تحليل مجموع المكعبين (س³ + 8) يساوي:",
                new String[]{"(س + 2)(س² − 2س + 4)", "(س + 2)(س² + 2س + 4)", "(س − 2)(س² + 2س + 4)", "(س + 2)³"}, 0,
                "مجموع مكعبين: (س + أ)(س² − أس + أ²)."));

            questions.add(new Question("مجموعة الأعداد الحقيقية R تتكون من اتحاد مجموعة الأعداد النسبية Q مع:",
                new String[]{"الأعداد الطبيعية", "الأعداد الصحيحة", "الأعداد غير النسبية (الجذور الصماء)", "الصفر فقط"}, 2,
                "ح = ن ∪ ن̄ (النسبية وغير النسبية مثل π وجذر 2)."));
        }

        if ("math_p2".equals(quizSubject) || "all_9th".equals(quizSubject)) {
            questions.add(new Question("العمود النازل من مركز الدائرة على أي وتر فيها:",
                new String[]{"يوازي الوتر", "ينصف الوتر", "يضاعف طول الوتر", "يمس الدائرة"}, 1,
                "مبرهنة هندسية أساسية: المستقيم المار بمركز الدائرة عمودياً على وتر ينصف ذلك الوتر."));

            questions.add(new Question("قياس الزاوية المحيطية يساوي دائماً:",
                new String[]{"ضعف قياس المركزية المشتركة معها في القوس", "نصف قياس المركزية المشتركة معها في القوس", "يساوي تماماً قياس المركزية", "180 درجة"}, 1,
                "الزاوية المحيطية = 1/2 الزاوية المركزية المشتركة معها في القوس نفسه."));

            questions.add(new Question("في أي شكل رباعي دائري، مجموع قياسي أي زاويتين متقابلتين يساوي:",
                new String[]{"90°", "180° (متكاملتان)", "360°", "270°"}, 1,
                "خاصية مميزة للرباعي الدائري: كل زاويتين متقابلتين متكاملتان (مجموعهما 180°)."));

            questions.add(new Question("قيمة النسبة المثلثية جيب تمام الزاوية 60° (جتا 60°) تساوي:",
                new String[]{"1/2", "جذر(3)/2", "1", "جذر(2)"}, 0,
                "جتا 60° = 1/2 = جا 30°، وظا 45° = 1."));

            questions.add(new Question("المتوسط الحسابي للقيم (4 ، 6 ، 8 ، 10 ، 12) يساوي:",
                new String[]{"6", "8", "10", "40"}, 1,
                "المتوسط الحسابي = مجموع القيم (40) / عددها (5) = 8."));
        }

        Collections.shuffle(questions);
    }

    private void displayCurrentQuestion() {
        if (curIndex >= questions.size()) {
            showFinalResults();
            return;
        }

        answered = false;
        Question q = questions.get(curIndex);

        tvSubject.setText(getQuizTitle(quizSubject));
        tvProgress.setText("السؤال " + (curIndex + 1) + " من " + questions.size());
        tvScoreTop.setText("النقاط: " + score);
        tvQuestion.setText(q.text);

        cardExplain.setVisibility(View.GONE);
        btnNext.setVisibility(View.GONE);

        for (int i = 0; i < 4; i++) {
            final int optIdx = i;
            btnOpts[i].setText(q.options[i]);
            btnOpts[i].setBackgroundResource(R.drawable.quiz_option_normal);
            btnOpts[i].setEnabled(true);
            btnOpts[i].setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    handleOptionClick(optIdx);
                }
            });
        }
    }

    private void handleOptionClick(int selectedIdx) {
        if (answered) return;
        answered = true;

        Question q = questions.get(curIndex);
        boolean isCorrect = (selectedIdx == q.correctIdx);

        for (int i = 0; i < 4; i++) {
            btnOpts[i].setEnabled(false);
            if (i == q.correctIdx) {
                btnOpts[i].setBackgroundResource(R.drawable.quiz_option_correct);
            } else if (i == selectedIdx) {
                btnOpts[i].setBackgroundResource(R.drawable.quiz_option_wrong);
            }
        }

        if (isCorrect) {
            score++;
            tvExplainHeader.setText("إجابة صحيحة وممتازة! ✅");
            tvExplainHeader.setTextColor(ThemeUtil.color(this, R.attr.thakerSuccess));
        } else {
            tvExplainHeader.setText("إجابة غير صحيحة ❌");
            tvExplainHeader.setTextColor(ThemeUtil.color(this, R.attr.thakerError));
        }

        tvExplainBody.setText(q.explanation);
        cardExplain.setVisibility(View.VISIBLE);

        btnNext.setVisibility(View.VISIBLE);
        btnNext.setText(curIndex + 1 < questions.size() ? "السؤال التالي ⬅" : "عرض النتيجة النهائية 🏆");
        btnNext.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                curIndex++;
                displayCurrentQuestion();
            }
        });
    }

    private void showFinalResults() {
        int pct = Math.round(((float) score / questions.size()) * 100);
        String msg = "حصلت على: " + score + " من " + questions.size() + " (" + pct + "%)\n\n";
        if (pct >= 85) msg += "🌟 ممتاز جداً! أداء متميز ومتقن في المنهج الوزاري!";
        else if (pct >= 65) msg += "👍 جيد جداً! واصل المراجعة لضمان الدرجة الكاملة.";
        else msg += "📚 ننصحك بمراجعة وحدات الكتاب والملخصات ثم إعادة الاختبار.";

        AlertDialog.Builder b = new AlertDialog.Builder(this);
        b.setTitle("نتيجة الاختبار الوزاري");
        b.setMessage(msg);
        b.setCancelable(false);
        b.setPositiveButton("إعادة الاختبار", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                curIndex = 0;
                score = 0;
                loadQuestions();
                displayCurrentQuestion();
            }
        });
        b.setNegativeButton("العودة للرئيسية", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                finish();
            }
        });
        b.show();
    }

    private String getQuizTitle(String key) {
        if ("sci_p1".equals(key)) return "اختبار علوم 9 - الجزء الأول";
        if ("sci_p2".equals(key)) return "اختبار علوم 9 - الجزء الثاني";
        if ("math_p1".equals(key)) return "اختبار رياضيات 9 - الجزء الأول";
        if ("math_p2".equals(key)) return "اختبار رياضيات 9 - الجزء الثاني";
        return "الاختبار الشامل للشهادة الأساسية (تاسع)";
    }
}
