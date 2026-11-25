package com.thaker.app;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

public class SubjectActivity extends Activity {

    private String subjectKey = "science";
    private LinearLayout partsContainer;
    private TextView tvTitle, tvMeta, tvGradePill, tvMistakesTitle;
    private ImageView ivIcon;
    private float dp;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_subject);
        dp = getResources().getDisplayMetrics().density;

        String k = getIntent().getStringExtra("subject_key");
        if (k != null && !k.isEmpty()) subjectKey = k;

        tvTitle = findViewById(R.id.tv_subj_title);
        tvMeta = findViewById(R.id.tv_subj_meta);
        tvGradePill = findViewById(R.id.tv_subj_grade_pill);
        ivIcon = findViewById(R.id.iv_subj_icon);
        partsContainer = findViewById(R.id.subj_parts_container);
        tvMistakesTitle = findViewById(R.id.tv_subj_mistakes_title);

        findViewById(R.id.btn_subj_back).setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) { finish(); }
        });

        NavBarHelper.setup(this, "subjects", null);
        renderSubject();
    }

    @Override
    protected void onResume() {
        super.onResume();
        renderSubject();
    }

    private void renderSubject() {
        partsContainer.removeAllViews();
        int wrongCnt = ThakerStore.getWrongIds(this).size();
        tvMistakesTitle.setText("أخطائي · " + wrongCnt);

        String quizKey = "sci_p1";
        if ("science".equals(subjectKey)) {
            tvTitle.setText("العلوم");
            tvMeta.setText("جزءان · 15 وحدة · تفاعلي + PDF");
            tvGradePill.setText("الصف التاسع");
            ivIcon.setImageResource(R.drawable.ic_subj_science);
            quizKey = "sci_p2";

            addPartCard("الجزء الأول", "المحاليل، التفاعلات الكيميائية، الصوت، الضوء، الإخراج والتكاثر",
                ThakerStore.getBookPct(this, "sci_p1", 68), "168 صفحة", "معمل 3D + كتاب PDF",
                "📖 افتح الكتاب المدرسي", "pdf", "sci_p1",
                "🧪 المعمل التفاعلي 3D للجزء 1", "science-9th-book.html");

            addPartCard("الجزء الثاني", "الهالوجينات، خواص المادة، الضغط، الطاقة الشمسية، الوراثة ومندل",
                ThakerStore.getBookPct(this, "sci_p2", 38), "148 صفحة تفاعلية", "أنشطة 3D وشروحات ذكية",
                "📖 افتح الكتاب التفاعلي", "html", "thaker-interactive-book.html",
                "📄 عرض الكتاب الرسمي PDF", "pdf:sci_p2");
        } else if ("math".equals(subjectKey)) {
            tvTitle.setText("الرياضيات");
            tvMeta.setText("جزءان · 8 وحدات · جبر وهندسة ومثلثات");
            tvGradePill.setText("الصف التاسع");
            ivIcon.setImageResource(R.drawable.ic_subj_math);
            quizKey = "math_p1";

            addPartCard("الجزء الأول", "المجموعات والعلاقات، التطبيقات، الأعداد الحقيقية، تحليل المقادير",
                ThakerStore.getBookPct(this, "math_p1", 45), "165 صفحة", "PDF رسمي + جبر",
                "📖 تصفح الجزء الأول PDF", "pdf", "math_p1",
                "📐 مختبر الرياضيات التفاعلي 3D", "math-9th-book.html");

            addPartCard("الجزء الثاني", "الدائرة ومبرهناتها، حساب المثلثات، التحويلات الهندسية، الإحصاء",
                ThakerStore.getBookPct(this, "math_p2", 20), "140 صفحة", "هندسة وتفاعلات",
                "📖 تصفح الجزء الثاني PDF", "pdf", "math_p2",
                "📐 استكشاف الأشكال الهندسية 3D", "math-9th-book.html");
        } else if ("physics".equals(subjectKey)) {
            tvTitle.setText("الفيزياء 3D");
            tvMeta.setText("9 وحدات · 213 صفحة · 18 مختبراً تفاعلياً");
            tvGradePill.setText("الثالث الثانوي");
            ivIcon.setImageResource(R.drawable.ic_subj_physics);
            quizKey = "phys_12";

            addPartCard("الكتاب التفاعلي الشامل", "كمية التحرك، التيار المتردد، الإلكترونيات، الفيزياء الذرية والنووية",
                ThakerStore.getBookPct(this, "phys_12", 25), "213 صفحة تفاعلية", "18 تجربة + فهرس ذكي",
                "⚡ افتح كتاب الفيزياء التفاعلي", "html", "physics-12th-book.html",
                "🔬 معمل الفيزياء التفاعلي 3D (18 تجربة)", "physics-12th-lab.html");
        } else if ("biology".equals(subjectKey)) {
            tvTitle.setText("الأحياء 3D");
            tvMeta.setText("8 وحدات · 219 صفحة · 18 مختبراً تفاعلياً");
            tvGradePill.setText("الثالث الثانوي");
            ivIcon.setImageResource(R.drawable.ic_subj_bio);
            quizKey = "bio_12";

            addPartCard("الكتاب التفاعلي الشامل", "التنظيم العصبي، الهرمونات، التكاثر، الوراثة وDNA والتقانة الحيوية والأرض",
                ThakerStore.getBookPct(this, "bio_12", 20), "219 صفحة تفاعلية", "18 تجربة + رسومات 3D",
                "🧬 افتح كتاب الأحياء التفاعلي", "html", "biology-12th-book.html",
                "🧪 معمل الأحياء التفاعلي 3D (18 تجربة)", "biology-12th-lab.html");
        } else {
            tvTitle.setText("الكيمياء 3D");
            tvMeta.setText("مختبر العناصر والتفاعلات · الثالث الثانوي");
            tvGradePill.setText("الثالث الثانوي");
            ivIcon.setImageResource(R.drawable.ic_subj_chem);
            quizKey = "chem_12";

            addPartCard("معمل الكيمياء ثلاثي الأبعاد", "جدول مندليف، العناصر الانتقالية، الكيمياء الحرارية والعضوية",
                ThakerStore.getBookPct(this, "chem_12", 30), "معمل 3D شامل", "محاكاة تفاعلية",
                "⚗️ افتح مختبر الكيمياء 3D", "html", "chem-lab-book.html", null, null);
        }

        final String finalQuizKey = quizKey;
        findViewById(R.id.card_subj_exam).setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                Intent i = new Intent(SubjectActivity.this, QuizActivity.class);
                i.putExtra("quiz_subject", finalQuizKey);
                startActivity(i);
            }
        });
        findViewById(R.id.card_subj_mistakes).setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                if (ThakerStore.getWrongIds(SubjectActivity.this).isEmpty()) {
                    Toast.makeText(SubjectActivity.this, "ممتاز! ليس لديك أخطاء مسجلة للمراجعة بعد.", Toast.LENGTH_SHORT).show();
                    return;
                }
                Intent i = new Intent(SubjectActivity.this, QuizActivity.class);
                i.putExtra("quiz_subject", finalQuizKey);
                i.putExtra("review_wrong", true);
                startActivity(i);
            }
        });
        findViewById(R.id.card_subj_summary).setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                Intent i = new Intent(SubjectActivity.this, SummaryActivity.class);
                i.putExtra("summary_subject", subjectKey);
                startActivity(i);
            }
        });
    }

    private void addPartCard(final String title, final String topics, final int pct, String pagesPill, String extraPill,
                             String ctaText, final String primaryType, final String primaryTarget,
                             String secondaryText, final String secondaryTarget) {
        LinearLayout card = new LinearLayout(this);
        card.setOrientation(LinearLayout.VERTICAL);
        card.setBackgroundResource(R.drawable.card_white_rounded);
        card.setElevation(3 * dp);
        int pad = (int) (16 * dp);
        card.setPadding(pad, pad, pad, pad);
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-1, -2);
        lp.bottomMargin = (int) (12 * dp);
        card.setLayoutParams(lp);

        LinearLayout topRow = new LinearLayout(this);
        topRow.setOrientation(LinearLayout.HORIZONTAL);
        topRow.setGravity(Gravity.CENTER_VERTICAL);

        LinearLayout info = new LinearLayout(this);
        info.setOrientation(LinearLayout.VERTICAL);
        info.setLayoutParams(new LinearLayout.LayoutParams(0, -2, 1f));
        info.setPadding(0, 0, (int) (10 * dp), 0);

        TextView tvT = new TextView(this);
        tvT.setText(title);
        tvT.setTextColor(ThakerStore.isDarkMode(this) ? 0xFFECFAF2 : 0xFF0F291E);
        tvT.setTextSize(17);
        tvT.getPaint().setFakeBoldText(true);
        info.addView(tvT);

        TextView tvTop = new TextView(this);
        tvTop.setText(topics);
        tvTop.setTextColor(ThakerStore.isDarkMode(this) ? 0xFF9BC4B0 : 0xFF5A7267);
        tvTop.setTextSize(12);
        tvTop.setPadding(0, (int) (3 * dp), 0, 0);
        info.addView(tvTop);
        topRow.addView(info);

        RingProgressView ring = new RingProgressView(this);
        int ringSz = (int) (60 * dp);
        ring.setLayoutParams(new FrameLayout.LayoutParams(ringSz, ringSz));
        ring.configure(pct, 100, pct + "%", 0xFF059669, ThakerStore.isDarkMode(this) ? 0xFFECFAF2 : 0xFF0F291E);
        topRow.addView(ring);
        card.addView(topRow);

        LinearLayout pills = new LinearLayout(this);
        pills.setOrientation(LinearLayout.HORIZONTAL);
        pills.setPadding(0, (int) (10 * dp), 0, (int) (12 * dp));
        pills.addView(makeChip("📄 " + pagesPill, R.drawable.pill_mint, 0xFF065F46));
        View sp = new View(this);
        sp.setLayoutParams(new LinearLayout.LayoutParams((int) (8 * dp), 1));
        pills.addView(sp);
        pills.addView(makeChip("🧪 " + extraPill, R.drawable.pill_gold, 0xFF92400E));
        card.addView(pills);

        Button cta = new Button(this);
        cta.setBackgroundResource(R.drawable.pill_emerald_btn);
        cta.setText(ctaText);
        cta.setTextColor(0xFFFFFFFF);
        cta.setTextSize(14);
        cta.getPaint().setFakeBoldText(true);
        cta.setLayoutParams(new LinearLayout.LayoutParams(-1, (int) (46 * dp)));
        cta.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                launchTarget(primaryType, primaryTarget, title);
            }
        });
        card.addView(cta);

        if (secondaryText != null && secondaryTarget != null) {
            Button sec = new Button(this);
            sec.setBackgroundResource(R.drawable.pill_emerald_outline);
            sec.setText(secondaryText);
            sec.setTextColor(0xFF059669);
            sec.setTextSize(13);
            sec.getPaint().setFakeBoldText(true);
            LinearLayout.LayoutParams slp = new LinearLayout.LayoutParams(-1, (int) (40 * dp));
            slp.topMargin = (int) (8 * dp);
            sec.setLayoutParams(slp);
            sec.setOnClickListener(new View.OnClickListener() {
                @Override public void onClick(View v) {
                    if (secondaryTarget.startsWith("pdf:")) {
                        launchTarget("pdf", secondaryTarget.substring(4), title);
                    } else {
                        launchTarget("html", secondaryTarget, title);
                    }
                }
            });
            card.addView(sec);
        }

        partsContainer.addView(card);
    }

    private void launchTarget(String type, String target, String title) {
        ThakerStore.saveReadingProgress(this, target, tvTitle.getText() + " - " + title, "متابعة الدراسة", type, target, 1, 15);
        if ("pdf".equals(type)) {
            Intent i = new Intent(this, BookViewerActivity.class);
            i.putExtra("book_key", target);
            startActivity(i);
        } else {
            Intent i = new Intent(this, LabActivity.class);
            i.putExtra("html_asset", target);
            startActivity(i);
        }
    }

    private TextView makeChip(String text, int bg, int fg) {
        TextView t = new TextView(this);
        t.setText(text);
        t.setBackgroundResource(bg);
        t.setTextColor(fg);
        t.setTextSize(11);
        t.getPaint().setFakeBoldText(true);
        t.setPadding((int) (10 * dp), (int) (4 * dp), (int) (10 * dp), (int) (4 * dp));
        return t;
    }
}
