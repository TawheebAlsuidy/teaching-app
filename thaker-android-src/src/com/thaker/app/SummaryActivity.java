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
        } else if ("physics".equals(subject)) {
            tvTitle.setText("الفيزياء 3D · الثالث الثانوي");
            groups.add(new SummaryGroup(
                "كمية التحرك", "الوحدة 1: التصادم والمقذوفات والصواريخ",
                "💡 كمية التحرك الخطي والزاوي", "• كمية التحرك الخطي (كم): حاصل ضرب الكتلة في السرعة وهو كمية متجهة.", "ص 10",
                "📐 القوانين الحاكمة", "كم = ك × ع   |   v_esc = √(2GM / R)", "كمية التحرك محفوظة في التصادم المرن وغير المرن بغياب القوى الخارجية.", "ص 18",
                "🧪 عوامل المدى الأفقي للمقذوف", "• يبلغ المقذوف أقصى مدى أفقي عند زاوية إطلاق 45°.", "ص 24",
                "⚠️ خطأ شائع", "إهمال الإشارة السالبة عند عكس اتجاه السرعة بعد التصادم."
            ));
        } else if ("biology".equals(subject)) {
            tvTitle.setText("الأحياء 3D · الثالث الثانوي");
            groups.add(new SummaryGroup(
                "الجهاز العصبي", "الوحدة 1: العصبون والسيال العصبي",
                "💡 الخلية العصبية (العصبون)", "• وحدة البناء والوظيفة؛ تنقل الإشارات العصبية من المستقبلات إلى المراكز العصبية.", "ص 9",
                "📐 أرقام وجهود أساسية", "جهد الراحة = -70 mV  |  عتبة الإزالة = +30 mV", "تعمل مضخة الصوديوم-بوتاسيوم على إخراج 3 Na+ وإدخال 2 K+.", "ص 16",
                "🧪 عوامل سرعة السيال العصبي", "• وجود الغمد الميليني (النقل القافز) وزيادة قطر المحور.", "ص 20",
                "⚠️ خطأ شائع", "الخلط بين دور أيونات الصوديوم (إزالة الاستقطاب) وأيونات البوتاسيوم (إعادة الاستقطاب)."
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
