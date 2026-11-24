package com.thaker.app;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;

public class SummaryActivity extends Activity {

    private LinearLayout cardsContainer;
    private Button tabMath1, tabMath2, tabSci1, tabSci2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_summary);

        cardsContainer = findViewById(R.id.summary_cards_container);
        tabMath1 = findViewById(R.id.tab_sum_math1);
        tabMath2 = findViewById(R.id.tab_sum_math2);
        tabSci1 = findViewById(R.id.tab_sum_sci1);
        tabSci2 = findViewById(R.id.tab_sum_sci2);

        findViewById(R.id.btn_summary_back).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });

        tabMath1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                selectTab("math_p1");
            }
        });
        tabMath2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                selectTab("math_p2");
            }
        });
        tabSci1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                selectTab("sci_p1");
            }
        });
        tabSci2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                selectTab("sci_p2");
            }
        });

        String active = getIntent().getStringExtra("active_tab");
        if (active == null) active = "math_p1";
        selectTab(active);
    }

    private void selectTab(String key) {
        resetTabs();
        cardsContainer.removeAllViews();

        if ("math_p1".equals(key)) {
            tabMath1.setBackgroundResource(R.drawable.tab_active);
            tabMath1.setTextColor(ThemeUtil.color(this, R.attr.thakerTextPrimary));
            populateMath1();
        } else if ("math_p2".equals(key)) {
            tabMath2.setBackgroundResource(R.drawable.tab_active);
            tabMath2.setTextColor(ThemeUtil.color(this, R.attr.thakerTextPrimary));
            populateMath2();
        } else if ("sci_p1".equals(key)) {
            tabSci1.setBackgroundResource(R.drawable.tab_active);
            tabSci1.setTextColor(ThemeUtil.color(this, R.attr.thakerTextPrimary));
            populateSci1();
        } else {
            tabSci2.setBackgroundResource(R.drawable.tab_active);
            tabSci2.setTextColor(ThemeUtil.color(this, R.attr.thakerTextPrimary));
            populateSci2();
        }
    }

    private void resetTabs() {
        tabMath1.setBackgroundResource(R.drawable.tab_inactive);
        tabMath1.setTextColor(ThemeUtil.color(this, R.attr.thakerTextSecondary));
        tabMath2.setBackgroundResource(R.drawable.tab_inactive);
        tabMath2.setTextColor(ThemeUtil.color(this, R.attr.thakerTextSecondary));
        tabSci1.setBackgroundResource(R.drawable.tab_inactive);
        tabSci1.setTextColor(ThemeUtil.color(this, R.attr.thakerTextSecondary));
        tabSci2.setBackgroundResource(R.drawable.tab_inactive);
        tabSci2.setTextColor(ThemeUtil.color(this, R.attr.thakerTextSecondary));
    }

    private void addCard(String title, String body, String badge) {
        LinearLayout card = new LinearLayout(this);
        card.setOrientation(LinearLayout.VERTICAL);
        card.setBackgroundResource(R.drawable.card_bg);
        card.setPadding(24, 20, 24, 20);

        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(
            LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);
        lp.setMargins(0, 0, 0, 20);
        card.setLayoutParams(lp);

        TextView tvTitle = new TextView(this);
        tvTitle.setText(title + (badge != null ? " (" + badge + ")" : ""));
        tvTitle.setTextColor(ThemeUtil.color(this, R.attr.thakerPrimary));
        tvTitle.setTextSize(15);
        tvTitle.setTypeface(null, android.graphics.Typeface.BOLD);
        tvTitle.setPadding(0, 0, 0, 8);

        TextView tvBody = new TextView(this);
        tvBody.setText(body);
        tvBody.setTextColor(0xFFFFFFFF);
        tvBody.setTextSize(13);
        tvBody.setLineSpacing(6, 1);

        card.addView(tvTitle);
        card.addView(tvBody);
        cardsContainer.addView(card);
    }

    private void populateMath1() {
        addCard("طرق تحليل المقادير الجبرية الست",
            "1. إخراج العامل المشترك الأعلى (ع.م.أ): مثل 3س + 6 = 3(س + 2).\n" +
            "2. الفرق بين مربعين: س² − ص² = (س − ص)(س + ص).\n" +
            "3. مجموع مكعبين: س³ + ص³ = (س + ص)(س² − س ص + ص²).\n" +
            "4. الفرق بين مكعبين: س³ − ص³ = (س − ص)(س² + س ص + ص²).\n" +
            "5. المقدار الثلاثي البسيط: س² + ب س + جـ = (س + م)(س + ن) حيث م+ن=ب وم×ن=جـ.\n" +
            "6. التحليل بالتقسيم وإكمال المربع للمقادير الرباعية والخاصة.", "الوحدة 4");

        addCard("العلاقات والتطبيقات",
            "• العلاقة الانعكاسية: (أ ، أ) ينتمي للعلاقة لكل أ.\n" +
            "• العلاقة المتماثلة: إذا كان (أ ، ب) ينتمي للعلاقة فإن (ب ، أ) ينتمي لها.\n" +
            "• العلاقة المتعدية: إذا كان (أ ، ب) و(ب ، جـ) ينتميان فإن (أ ، جـ) ينتمي لها.\n" +
            "• علاقة التكافؤ: هي العلاقة التي تكون انعكاسية ومتماثلة ومتعدية معاً.\n" +
            "• التطبيق: علاقة يرتبط فيها كل عنصر من المجال بعنصر واحد فقط في المجال المقابل.\n" +
            "• أنواع التطبيقات: شامل (المدى = المجال المقابل)، متباين (عناصر مختلفة لها صور مختلفة)، تقابل (شامل ومتباين معاً).", "الوحدة 1 و 2");

        addCard("الأعداد الحقيقية R والعمليات عليها",
            "• ح = ن ∪ ن̄ (مجموعة الأعداد النسبية وغير النسبية).\n" +
            "• إنطاق المقام: ضرب البسط والمقام في مرافق المقام للتخلص من الجذور في المقام.\n" +
            "• الفترات: المغلقة [أ ، ب]، المفتوحة ]أ ، ب[، ونصف المغلقة.\n" +
            "• القيمة المطلقة: |س| ≥ 0 دائماً، وتُعبر عن المسافة على خط الأعداد.", "الوحدة 3");
    }

    private void populateMath2() {
        addCard("نظريات ومبرهنات الدائرة",
            "• مبرهنة الوتر والعمود: المستقيم المار بمركز الدائرة عمودياً على وتر فيها ينصف ذلك الوتر وينصف قوسه.\n" +
            "• مبرهنة الأوتار المتطابقة: في الدائرة الواحدة أو الدوائر المتطابقة، الأوتار المتطابقة تكون على أبعاد متساوية من المركز.\n" +
            "• الزاوية المركزية والمحيطية: قياس الزاوية المحيطية = نصف قياس الزاوية المركزية المشتركة معها في نفس القوس.\n" +
            "• زوايا في نفس القوس: جميع الزوايا المحيطية المقامة على قوس واحد في دائرة متطابقة.\n" +
            "• مبرهنة الرباعي الدائري: كل زاويتين متقابلتين في أي شكل رباعي دائري متكاملتان (مجموعهما = 180°).\n" +
            "• مبرهنة المماس: مماس الدائرة عمودي على نصف القطر عند نقطة التماس.", "الوحدة 5");

        addCard("حساب المثلثات والزوايا",
            "في المثلث القائم الزاوية:\n" +
            "• جيب الزاوية (جا هـ) = المقابل / الوتر\n" +
            "• جيب تمام الزاوية (جتا هـ) = المجاور / الوتر\n" +
            "• ظل الزاوية (ظا هـ) = المقابل / المجاور = جا هـ / جتا هـ\n" +
            "• المتطابقة الأساسية: جا² هـ + جتا² هـ = 1\n\n" +
            "النسب للزوايا الخاصة:\n" +
            "• جا 30° = 1/2 ، جتا 30° = √3/2 ، ظا 30° = 1/√3\n" +
            "• جا 45° = 1/√2 ، جتا 45° = 1/√2 ، ظا 45° = 1\n" +
            "• جا 60° = √3/2 ، جتا 60° = 1/2 ، ظا 60° = √3", "الوحدة 6");

        addCard("الإحصاء والاحتمالات",
            "• المتوسط الحسابي: مجموع القيم مقسوماً على عددها (س̄ = مجـ س / ن).\n" +
            "• المنوال: القيمة الأكثر تكراراً أو شيوعاً بين البيانات.\n" +
            "• الوسيط: القيمة التي تقسم البيانات المرتبة (تصاعدياً أو تنازلياً) إلى نصفين متساويين.\n" +
            "• المدى: الفرق بين أكبر قيمة وأصغر قيمة في مجموعة البيانات.", "الوحدة 8");
    }

    private void populateSci1() {
        addCard("المحاليل والتفاعلات الكيميائية",
            "• المحلول المشبع: يحتوي على أقصى كمية مذاب عند ثبوت درجة الحرارة.\n" +
            "• النسبة المئوية الكتلية = (كتلة المذاب / كتلة المحلول) × 100%.\n" +
            "• تفاعلات الترسيب: تفاعلات كيميائية ينتج عنها مادة صلبة غير ذائبة في المحلول.\n" +
            "• العوامل المؤثرة في سرعة التفاعل: طبيعة المواد المتفاعلة، التركيز، درجة الحرارة، والمحفزات.", "الوحدة 1 و 2");

        addCard("الصوت والضوء",
            "• سرعة الصوت: 331 م/ث عند 0° مئوية في الهواء وتزداد مع زيادة الحرارة والكثافة.\n" +
            "• صدى الصوت: تكرار سماع الصوت نتيجة انعكاسه على حاجز على بعد لا يقل عن 17 متراً.\n" +
            "• قانونا الانعكاس في الضوء:\n" +
            "  1. زاوية السقوط = زاوية الانعكاس.\n" +
            "  2. الشعاع الساقط والمنعكس والعمود المقام تقع جميعها في مستوى واحد عمودي على السطح العاكس.\n" +
            "• المرايا المقعرة تجمّع الأشعة (مجمعة)، بينما المحدبة تفرق الأشعة وتكون صوراً مصغرة.", "الوحدة 3 و 4");

        addCard("الإخراج والتكاثر وأجهزة الجسم",
            "• الكلية والنفرونات: ترشيح الدم، التخلص من الفضلات النيتروجينية كاليوريا والأملاح الزائدة.\n" +
            "• الجلد: الإخراج عن طريق الغدد العرقية وتنظيم درجة حرارة الجسم.\n" +
            "• التكاثر في النبات: التلقيح (ذاتي وخلطي) يتبعه الإخصاب لتكوين البذور والثمار.\n" +
            "• أمراض الجهازين البولي والتناسلي: حصوات الكلى، بلهارسيا المجاري البولية، والتهابات المسالك البولية وطرق الوقاية منها.", "الوحدة 5 و 6 و 7");
    }

    private void populateSci2() {
        addCard("الكهرباء والمغناطيسية",
            "• قانون أوم: جـ = ت × م (فرق الجهد = شدة التيار × المقاومة).\n" +
            "• التوصيل على التوالي: شدة التيار ثابتة، والمقاومة الكلية = م1 + م2 + ...\n" +
            "• التوصيل على التوازي: فرق الجهد ثابت، و 1/م الكلية = 1/م1 + 1/م2 + ...\n" +
            "• الحث الكهرومغناطيسي: توليد تيار كهربائي في موصل عند تغير المجال المغناطيسي القاطع له.\n" +
            "• المحول الكهربائي: جهاز لرفع أو خفض الجهد المتردد (جـ2 / جـ1 = ن2 / ن1).", "الوحدة 8 و 9");

        addCard("الطاقة والبيئة",
            "• قانون بقاء الطاقة: الطاقة لا تفنى ولا تستحدث من العدم بل تتحول من شكل إلى آخر.\n" +
            "• الطاقة الحركية طح = 1/2 ك ع² ، طاقة الوضع طو = ك × جـ × ف.\n" +
            "• التوازن البيئي: التفاعل المتوازن بين المكونات الحية (المنتجات، المستهلكات، المحللات) وغير الحية.\n" +
            "• الاحتباس الحراري: زيادة تركيز غازات الدفيئة (مثل CO₂) تحبس الأشعة تحت الحمراء في الجو.", "الوحدة 10 و 11");

        addCard("علوم الأرض والفضاء",
            "• طبقات الأرض: القشرة الأرضية، الوشاح (الستار)، واللب (الداخلي والخارجي).\n" +
            "• الصخور: نارية (بازلت، جرانيت)، رسوبية (حجر رملي، جيري)، ومتحولة (رخام).\n" +
            "• النظام الشمسي: الشمس و8 كواكب: عطارد، الزهرة، الأرض، المريخ (داخلية)، المشتري، زحل، أورانوس، نبتون (خارجية).\n" +
            "• السنة الضوئية: المسافة التي يقطعها الضوء في سنة كاملة وتساوي حوالي 9.46 تريليون كم.", "الوحدة 12 و 13");
    }
}
