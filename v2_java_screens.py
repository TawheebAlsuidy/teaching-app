#!/usr/bin/env python3
"""
V2 Screen Activities for Thaker (ذاكر):
- MainActivity.java (03-home + موادي + المكتبة + المفضلة + الإعدادات)
- SubjectActivity.java (04-subject + Part RingProgress + Exam/Mistakes/Summary actions)
- ProgressActivity.java (11-progress + Weekly Goal Ring + Mastery Grid + Mistake Reminder + Badges)
- SummaryActivity.java (09-summary + Color-Striped Concept/Formula/Factors/Mistake cards)
- QuizActivity.java (10-quiz + Instant Feedback + Why Wrong + Review Page + Lab shortcut)
"""
import os


def _w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.lstrip("\n"))


def write_v2_screens_java(base_dir):
    src = f"{base_dir}/src/com/thaker/app"

    # 1. MainActivity.java
    _w(f"{src}/MainActivity.java", r"""package com.thaker.app;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ProgressBar;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;
import java.util.Calendar;
import java.util.List;

public class MainActivity extends Activity {

    private String currentTab = "home";
    private View pageHome, pageSubjects, pageLibrary, pageBookmarks, pageSettings;
    private TextView tvGreeting, tvCountdown, tvResumeTitle, tvResumeSubtitle, tvResumePct, btnStreakPill;
    private ProgressBar progResume;
    private TextView chkTask1, chkTask2;
    private LinearLayout homeSubjectsContainer, allSubjectsContainer, libraryContainer, bookmarksContainer, settingsContainer;
    private float dp;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        dp = getResources().getDisplayMetrics().density;

        pageHome = findViewById(R.id.page_home);
        pageSubjects = findViewById(R.id.page_subjects);
        pageLibrary = findViewById(R.id.page_library);
        pageBookmarks = findViewById(R.id.page_bookmarks);
        pageSettings = findViewById(R.id.page_settings);

        tvGreeting = findViewById(R.id.tv_home_greeting);
        tvCountdown = findViewById(R.id.tv_home_countdown);
        tvResumeTitle = findViewById(R.id.tv_resume_title);
        tvResumeSubtitle = findViewById(R.id.tv_resume_subtitle);
        tvResumePct = findViewById(R.id.tv_resume_pct);
        progResume = findViewById(R.id.prog_resume_bar);
        btnStreakPill = findViewById(R.id.btn_home_streak_pill);

        chkTask1 = findViewById(R.id.chk_task_1);
        chkTask2 = findViewById(R.id.chk_task_2);

        homeSubjectsContainer = findViewById(R.id.home_subjects_container);
        allSubjectsContainer = findViewById(R.id.all_subjects_container);
        libraryContainer = findViewById(R.id.library_container);
        bookmarksContainer = findViewById(R.id.bookmarks_container);
        settingsContainer = findViewById(R.id.settings_container);

        View.OnClickListener openProgress = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, ProgressActivity.class));
            }
        };
        findViewById(R.id.btn_home_avatar).setOnClickListener(openProgress);
        findViewById(R.id.btn_home_progress_bell).setOnClickListener(openProgress);
        btnStreakPill.setOnClickListener(openProgress);

        findViewById(R.id.btn_resume_reading).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openLastRead();
            }
        });

        findViewById(R.id.card_task_1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                boolean next = !ThakerStore.isTaskDone(MainActivity.this, 1);
                ThakerStore.setTaskDone(MainActivity.this, 1, next);
                if (next) ThakerStore.bumpStudyStreak(MainActivity.this);
                refreshHomeHeaderAndTasks();
            }
        });
        findViewById(R.id.card_task_2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                boolean next = !ThakerStore.isTaskDone(MainActivity.this, 2);
                ThakerStore.setTaskDone(MainActivity.this, 2, next);
                if (next) ThakerStore.bumpStudyStreak(MainActivity.this);
                refreshHomeHeaderAndTasks();
            }
        });

        findViewById(R.id.btn_view_all_subjects).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                switchTab("subjects");
            }
        });

        String reqTab = getIntent().getStringExtra("open_tab");
        if (reqTab != null && !reqTab.isEmpty()) currentTab = reqTab;
        refreshAllTabs();
        switchTab(currentTab);
    }

    @Override
    protected void onNewIntent(Intent intent) {
        super.onNewIntent(intent);
        setIntent(intent);
        String reqTab = intent.getStringExtra("open_tab");
        if (reqTab != null && !reqTab.isEmpty()) {
            switchTab(reqTab);
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        refreshAllTabs();
    }

    private void switchTab(String tab) {
        currentTab = tab;
        pageHome.setVisibility("home".equals(tab) ? View.VISIBLE : View.GONE);
        pageSubjects.setVisibility("subjects".equals(tab) ? View.VISIBLE : View.GONE);
        pageLibrary.setVisibility("library".equals(tab) ? View.VISIBLE : View.GONE);
        pageBookmarks.setVisibility("bookmarks".equals(tab) ? View.VISIBLE : View.GONE);
        pageSettings.setVisibility("settings".equals(tab) ? View.VISIBLE : View.GONE);

        NavBarHelper.setup(this, tab, new NavBarHelper.TabListener() {
            @Override
            public void onTabSelected(String tabKey) {
                switchTab(tabKey);
            }
        });
    }

    private void refreshAllTabs() {
        refreshHomeHeaderAndTasks();
        buildHomeSubjectsGrid();
        buildAllSubjectsTab();
        buildLibraryTab();
        buildBookmarksTab();
        buildSettingsTab();
    }

    private void refreshHomeHeaderAndTasks() {
        int hour = Calendar.getInstance().get(Calendar.HOUR_OF_DAY);
        String salutation = (hour >= 4 && hour < 12) ? "صباح الخير يا " : "مساء الخير يا ";
        tvGreeting.setText(salutation + ThakerStore.getStudentName(this));

        String cert = ThakerStore.getStage(this) == 1 ? "امتحان الثانوية العامة" : "امتحان الشهادة الأساسية";
        tvCountdown.setText("📅 باقي " + ThakerStore.getExamDaysLeft(this) + " يوماً على " + cert);

        tvResumeTitle.setText(ThakerStore.getLastTitle(this));
        tvResumeSubtitle.setText(ThakerStore.getLastSubtitle(this));
        int pct = ThakerStore.getLastPct(this);
        progResume.setProgress(pct);
        tvResumePct.setText(pct + "% من الجزء");

        btnStreakPill.setText("🔥 " + ThakerStore.getStreakDays(this) + " من " + ThakerStore.getWeeklyGoal(this) + " أيام");

        boolean t1 = ThakerStore.isTaskDone(this, 1);
        chkTask1.setBackgroundResource(t1 ? R.drawable.pill_mint : R.drawable.pill_gray);
        chkTask1.setText(t1 ? "✓" : "");

        boolean t2 = ThakerStore.isTaskDone(this, 2);
        chkTask2.setBackgroundResource(t2 ? R.drawable.pill_mint : R.drawable.pill_gray);
        chkTask2.setText(t2 ? "✓" : "");
    }

    private void openLastRead() {
        String type = ThakerStore.getLastType(this);
        String target = ThakerStore.getLastAsset(this);
        int pg = ThakerStore.getLastPage(this);
        if ("pdf".equals(type)) {
            Intent i = new Intent(this, BookViewerActivity.class);
            i.putExtra("book_key", target);
            i.putExtra("start_page", Math.max(0, pg - 1));
            startActivity(i);
        } else {
            Intent i = new Intent(this, LabActivity.class);
            i.putExtra("html_asset", target);
            i.putExtra("start_page", pg);
            i.putExtra("start_tab", "reader");
            startActivity(i);
        }
    }

    private void buildHomeSubjectsGrid() {
        homeSubjectsContainer.removeAllViews();
        if (ThakerStore.getStage(this) == 0) {
            LinearLayout row = makeRow();
            row.addView(makeSubjectTile("العلوم", "جزءان · تفاعلي 3D", R.drawable.ic_subj_science, R.drawable.card_mint_tint, "science", true));
            row.addView(makeSpace(10));
            row.addView(makeSubjectTile("الرياضيات", "جزءان · هندسة وجبر", R.drawable.ic_subj_math, R.drawable.card_cream_tint, "math", true));
            homeSubjectsContainer.addView(row);
        } else {
            LinearLayout row1 = makeRow();
            row1.addView(makeSubjectTile("الكيمياء 3D", "كتاب + معمل 10 تجارب", R.drawable.ic_subj_chem, R.drawable.card_mint_tint, "chemistry", true));
            row1.addView(makeSpace(10));
            row1.addView(makeSubjectTile("الفيزياء 3D", "منهج تفاعلي", R.drawable.ic_subj_physics, R.drawable.card_cream_tint, "physics", true));
            homeSubjectsContainer.addView(row1);

            LinearLayout row2 = makeRow();
            row2.setPadding(0, (int) (10 * dp), 0, 0);
            row2.addView(makeSubjectTile("الأحياء 3D", "منهج تفاعلي", R.drawable.ic_subj_bio, R.drawable.card_mint_tint, "biology", true));
            row2.addView(makeSpace(10));
            row2.addView(makeSubjectTile("الرياضيات 3D", "250 صفحة + 13 مجسماً", R.drawable.ic_subj_math, R.drawable.card_white_rounded, "math12", true));
            homeSubjectsContainer.addView(row2);

            LinearLayout row3 = makeRow();
            row3.setPadding(0, (int) (10 * dp), 0, 0);
            row3.addView(makeSubjectTile("الأدب والنصوص", "212 صفحة + تحليل جمالي", R.drawable.ic_subj_literature, R.drawable.card_cream_tint, "arabic_lit", true));
            row3.addView(makeSpace(10));
            row3.addView(makeSubjectTile("القرآن الكريم", "188 ص + الحصري + تقويمات", R.drawable.ic_subj_quran, R.drawable.card_mint_tint, "quran", true));
            homeSubjectsContainer.addView(row3);
        }
    }

    private void buildAllSubjectsTab() {
        allSubjectsContainer.removeAllViews();
        addSectionTitle(allSubjectsContainer, "📚 موادي الدراسية");
        addMutedSub(allSubjectsContainer, "اختر أي مادة لفتح كتبها وملخصاتها واختباراتها");

        addSubSectionLabel(allSubjectsContainer, "المرحلة الإعدادية (الصف التاسع)");
        LinearLayout r1 = makeRow();
        r1.addView(makeSubjectTile("العلوم", "15 وحدة · تفاعلي + PDF", R.drawable.ic_subj_science, R.drawable.card_mint_tint, "science", true));
        r1.addView(makeSpace(10));
        r1.addView(makeSubjectTile("الرياضيات", "الجبر + الدائرة والمثلثات", R.drawable.ic_subj_math, R.drawable.card_cream_tint, "math", true));
        allSubjectsContainer.addView(r1);

        addSubSectionLabel(allSubjectsContainer, "المرحلة الثانوية (الثالث الثانوي العلمي)");
        LinearLayout r2 = makeRow();
        r2.addView(makeSubjectTile("الكيمياء 3D", "187 صفحة + معمل 10 تجارب", R.drawable.ic_subj_chem, R.drawable.card_mint_tint, "chemistry", true));
        r2.addView(makeSpace(10));
        r2.addView(makeSubjectTile("الفيزياء 3D", "213 صفحة + معمل 18 تجربة", R.drawable.ic_subj_physics, R.drawable.card_cream_tint, "physics", true));
        allSubjectsContainer.addView(r2);

        LinearLayout r3 = makeRow();
        r3.setPadding(0, (int) (10 * dp), 0, 0);
        r3.addView(makeSubjectTile("الأحياء 3D", "219 صفحة + معمل 18 تجربة", R.drawable.ic_subj_bio, R.drawable.card_mint_tint, "biology", true));
        r3.addView(makeSpace(10));
        r3.addView(makeSubjectTile("الرياضيات 3D", "250 صفحة + معمل 13 مجسماً", R.drawable.ic_subj_math, R.drawable.card_white_rounded, "math12", true));
        allSubjectsContainer.addView(r3);

        LinearLayout r4 = makeRow();
        r4.setPadding(0, (int) (10 * dp), 0, 0);
        r4.addView(makeSubjectTile("الأدب والنصوص", "212 صفحة + 36 تحليلاً جمالياً", R.drawable.ic_subj_literature, R.drawable.card_cream_tint, "arabic_lit", true));
        r4.addView(makeSpace(10));
        r4.addView(makeSubjectTile("القرآن الكريم", "188 ص + 120 تلاوة للحصري", R.drawable.ic_subj_quran, R.drawable.card_mint_tint, "quran", true));
        allSubjectsContainer.addView(r4);
    }

    private void buildLibraryTab() {
        libraryContainer.removeAllViews();
        addSectionTitle(libraryContainer, "📖 المكتبة الشاملة");
        addMutedSub(libraryContainer, "جميع الكتب التفاعلية 3D والملفات الرسمية بلا إنترنت");

        LinearLayout progBanner = makeListCard("📊 تقدمي وخريطة الإتقان", "تابع هدفك الأسبوعي، وحداتك المتقنة، وأخطاءك للمراجعة", R.drawable.card_mint_tint);
        progBanner.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) { startActivity(new Intent(MainActivity.this, ProgressActivity.class)); }
        });
        libraryContainer.addView(progBanner);

        addSubSectionLabel(libraryContainer, "الكتب التفاعلية المطوّرة 3D (إصدار 2.0)");
        addHtmlBookItem("🧪 العلوم 9 - الجزء الثاني التفاعلي (148 صفحة)", "شروح مفصلة، تجارب 3D متحركة، ملخصات واختبارات", "thaker-interactive-book.html");
        addHtmlBookItem("⚗️ الكيمياء 12 التفاعلي (187 صفحة + معمل)", "العناصر الانتقالية، الكيمياء الحرارية والكهربية، النووية والعضوية", "chemistry-12th-book.html");
        addHtmlBookItem("⚡ الفيزياء 12 التفاعلي (213 صفحة)", "كمية التحرك، التيار المتردد، الذرة والفيزياء النووية", "physics-12th-book.html");
        addHtmlBookItem("🔬 معمل الفيزياء التفاعلي 3D (18 تجربة)", "تطبيقات تفاعلية متدرجة الخطوات لجميع وحدات الفيزياء 1–9", "physics-12th-lab.html");
        addHtmlBookItem("🧬 الأحياء 12 التفاعلي (219 صفحة)", "الجهاز العصبي، الوراثة، DNA والتقانة الحيوية", "biology-12th-book.html");
        addHtmlBookItem("🧪 معمل الأحياء التفاعلي 3D (18 تجربة)", "تطبيقات تفاعلية متدرجة الخطوات لجميع وحدات الأحياء 1–8", "biology-12th-lab.html");
        addHtmlBookItem("📐 الرياضيات 12 التفاعلي (250 صفحة + حلول)", "الأعداد المركبة، القطوع، الهندسة الفضائية، الاحتمالات، المشتقات والتكامل", "math-12th-book.html");
        addHtmlBookItem("🧊 معمل الرياضيات التفاعلي 3D (13 مجسماً)", "مستوى أرغاند، القطوع، المجسمات، الاحتمالات، المشتقات والتكامل", "math-12th-lab.html");
        addHtmlBookItem("الأدب والنصوص 12 التفاعلي (212 صفحة)", "36 موضوعاً، تحليل جمالي، بطاقات نصوص، وفهرس النقد الأدبي", "arabic-literature-12th-book.html");
        addHtmlBookItem("🕌 القرآن الكريم وعلومه 12 التفاعلي (188 صفحة)", "سورة النور، علوم القرآن، التلاوة والتجويد، 120 تلاوة للحصري", "quran-12th-book.html");
        addHtmlBookItem("⚗️ مختبر الكيمياء 3D (10 تجارب تفاعلية)", "معمل كيمياء ثلاثي الأبعاد مربوط مباشرة بكتاب الكيمياء", "chem-lab-book.html");
        addHtmlBookItem("🔬 المعمل التفاعلي 3D لعلوم التاسع", "13 درساً وتجربة علمية ثلاثية الأبعاد", "science-9th-book.html");
        addHtmlBookItem("📐 كتاب الرياضيات التفاعلي 3D (التاسع)", "نماذج هندسية تفاعلية للمبرهنات والدائرة", "math-9th-book.html");

        addSubSectionLabel(libraryContainer, "الكتب المدرسية الرسمية الكاملة (PDF)");
        addPdfBookItem("📘 العلوم 9 - الجزء الأول (PDF الرسمي)", "sci_p1");
        addPdfBookItem("📗 العلوم 9 - الجزء الثاني (PDF الرسمي)", "sci_p2");
        addPdfBookItem("📙 الرياضيات 9 - الجزء الأول (PDF الرسمي)", "math_p1");
        addPdfBookItem("📕 الرياضيات 9 - الجزء الثاني (PDF الرسمي)", "math_p2");
    }

    private void buildBookmarksTab() {
        bookmarksContainer.removeAllViews();
        addSectionTitle(bookmarksContainer, "⭐ المفضلة");
        addMutedSub(bookmarksContainer, "الدروس والملخصات التي حفظتها للوصول السريع");

        List<String> list = ThakerStore.getBookmarks(this);
        if (list.isEmpty()) {
            LinearLayout empty = makeListCard("لا توجد عناصر محفوظة بعد", "اضغط على زر (⭐ احفظ) في صفحة أي ملخص أو كتاب لإضافتها هنا.", R.drawable.card_white_rounded);
            empty.setOnClickListener(new View.OnClickListener() {
                @Override public void onClick(View v) {
                    Intent i = new Intent(MainActivity.this, SummaryActivity.class);
                    i.putExtra("summary_subject", "science");
                    startActivity(i);
                }
            });
            bookmarksContainer.addView(empty);
        } else {
            for (String item : list) {
                final String[] parts = item.split("\\|");
                String label = parts.length > 0 ? parts[0] : item;
                final String kind = parts.length > 1 ? parts[1] : "summary";
                final String target = parts.length > 2 ? parts[2] : "science";
                LinearLayout card = makeListCard("⭐ " + label, "اضغط للفتح مباشرة", R.drawable.card_white_rounded);
                card.setOnClickListener(new View.OnClickListener() {
                    @Override public void onClick(View v) {
                        if ("html".equals(kind)) {
                            Intent i = new Intent(MainActivity.this, LabActivity.class);
                            i.putExtra("html_asset", target);
                            startActivity(i);
                        } else {
                            Intent i = new Intent(MainActivity.this, SummaryActivity.class);
                            i.putExtra("summary_subject", target);
                            startActivity(i);
                        }
                    }
                });
                bookmarksContainer.addView(card);
            }
        }
    }

    private void buildSettingsTab() {
        settingsContainer.removeAllViews();
        addSectionTitle(settingsContainer, "⚙️ الإعدادات");
        addMutedSub(settingsContainer, "تخصيص الحساب الدراسي والمظهر");

        LinearLayout profCard = makeListCard("👤 الملف الشخصي: " + ThakerStore.getStudentName(this),
            ThakerStore.getGradeLabel(this) + " · متبقي " + ThakerStore.getExamDaysLeft(this) + " يوماً للامتحان", R.drawable.card_white_rounded);
        profCard.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                final EditText et = new EditText(MainActivity.this);
                et.setText(ThakerStore.getStudentName(MainActivity.this));
                new AlertDialog.Builder(MainActivity.this)
                    .setTitle("تعديل اسم الطالب")
                    .setView(et)
                    .setPositiveButton("حفظ", new DialogInterface.OnClickListener() {
                        @Override public void onClick(DialogInterface dialog, int which) {
                            ThakerStore.setStudentName(MainActivity.this, et.getText().toString());
                            refreshAllTabs();
                        }
                    }).setNegativeButton("إلغاء", null).show();
            }
        });
        settingsContainer.addView(profCard);

        LinearLayout themeRow = new LinearLayout(this);
        themeRow.setBackgroundResource(R.drawable.card_white_rounded);
        themeRow.setGravity(Gravity.CENTER_VERTICAL);
        themeRow.setOrientation(LinearLayout.HORIZONTAL);
        int p = (int) (14 * dp);
        themeRow.setPadding(p, p, p, p);
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-1, -2);
        lp.topMargin = (int) (10 * dp);
        themeRow.setLayoutParams(lp);
        TextView tvTheme = new TextView(this);
        tvTheme.setText("🌙 الوضع الليلي الداكن");
        tvTheme.setTextColor(ThakerStore.isDarkMode(this) ? 0xFFECFAF2 : 0xFF0F291E);
        tvTheme.setTextSize(15);
        tvTheme.setLayoutParams(new LinearLayout.LayoutParams(0, -2, 1f));
        Switch sw = new Switch(this);
        sw.setChecked(ThakerStore.isDarkMode(this));
        sw.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                ThemeUtil.toggleDarkMode(MainActivity.this, isChecked);
            }
        });
        themeRow.addView(tvTheme);
        themeRow.addView(sw);
        settingsContainer.addView(themeRow);

        LinearLayout stageCard = makeListCard("🎓 تغيير المرحلة والصف والهدف", "إعادة فتح شاشة الإعداد الترحيبية", R.drawable.card_white_rounded);
        stageCard.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, OnboardingActivity.class));
            }
        });
        settingsContainer.addView(stageCard);

        LinearLayout resetCard = makeListCard("🔄 إعادة تعيين التقدم والأخطاء", "مسح إحصائيات المذاكرة الحالية والبدء من جديد", R.drawable.card_white_rounded);
        resetCard.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                new AlertDialog.Builder(MainActivity.this)
                    .setTitle("تأكيد المسح")
                    .setMessage("هل تريد إعادة تعيين جميع نقاط التقدم وسجل الأخطاء؟")
                    .setPositiveButton("نعم، امسح", new DialogInterface.OnClickListener() {
                        @Override public void onClick(DialogInterface dialog, int which) {
                            ThakerStore.resetAll(MainActivity.this);
                            ThakerStore.setOnboarded(MainActivity.this, true);
                            refreshAllTabs();
                            Toast.makeText(MainActivity.this, "تمت إعادة التعيين", Toast.LENGTH_SHORT).show();
                        }
                    }).setNegativeButton("إلغاء", null).show();
            }
        });
        settingsContainer.addView(resetCard);

        LinearLayout about = makeListCard("💚 عن تطبيق ذاكر (الإصدار 2.0)", "تطبيق تعليمي يمني شامل وتفاعلي ثلاثي الأبعاد يعمل بالكامل بلا إنترنت.", R.drawable.card_mint_tint);
        settingsContainer.addView(about);
    }

    private LinearLayout makeRow() {
        LinearLayout r = new LinearLayout(this);
        r.setOrientation(LinearLayout.HORIZONTAL);
        return r;
    }

    private View makeSpace(int widthDp) {
        View v = new View(this);
        v.setLayoutParams(new LinearLayout.LayoutParams((int) (widthDp * dp), 1));
        return v;
    }

    private LinearLayout makeSubjectTile(String title, String sub, int iconRes, int bgRes, final String subjectKey, boolean weighted) {
        LinearLayout card = new LinearLayout(this);
        card.setOrientation(LinearLayout.VERTICAL);
        card.setGravity(Gravity.CENTER_HORIZONTAL);
        card.setBackgroundResource(bgRes);
        card.setElevation(2 * dp);
        int pad = (int) (14 * dp);
        card.setPadding(pad, pad, pad, pad);
        card.setLayoutParams(weighted ? new LinearLayout.LayoutParams(0, -2, 1f) : new LinearLayout.LayoutParams(-1, -2));

        ImageView iv = new ImageView(this);
        int sz = (int) (56 * dp);
        iv.setLayoutParams(new LinearLayout.LayoutParams(sz, sz));
        iv.setImageResource(iconRes);
        card.addView(iv);

        TextView tvT = new TextView(this);
        tvT.setText(title);
        tvT.setTextColor(ThakerStore.isDarkMode(this) ? 0xFFECFAF2 : 0xFF0F291E);
        tvT.setTextSize(16);
        tvT.setGravity(Gravity.CENTER);
        tvT.setPadding(0, (int) (8 * dp), 0, 0);
        tvT.getPaint().setFakeBoldText(true);
        card.addView(tvT);

        TextView tvS = new TextView(this);
        tvS.setText(sub);
        tvS.setTextColor(ThakerStore.isDarkMode(this) ? 0xFF9BC4B0 : 0xFF5A7267);
        tvS.setTextSize(11);
        tvS.setGravity(Gravity.CENTER);
        tvS.setPadding(0, (int) (2 * dp), 0, 0);
        card.addView(tvS);

        card.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                Intent i = new Intent(MainActivity.this, SubjectActivity.class);
                i.putExtra("subject_key", subjectKey);
                startActivity(i);
            }
        });
        return card;
    }

    private void addHtmlBookItem(String title, String sub, final String assetName) {
        LinearLayout c = makeListCard(title, sub, R.drawable.card_white_rounded);
        c.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                Intent i = new Intent(MainActivity.this, LabActivity.class);
                i.putExtra("html_asset", assetName);
                startActivity(i);
            }
        });
        libraryContainer.addView(c);
    }

    private void addPdfBookItem(String title, final String bookKey) {
        LinearLayout c = makeListCard(title, "عرض فوري بلا إنترنت مع تقريب وفهرس وحدات", R.drawable.card_white_rounded);
        c.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                Intent i = new Intent(MainActivity.this, BookViewerActivity.class);
                i.putExtra("book_key", bookKey);
                startActivity(i);
            }
        });
        libraryContainer.addView(c);
    }

    private LinearLayout makeListCard(String title, String sub, int bgRes) {
        LinearLayout card = new LinearLayout(this);
        card.setOrientation(LinearLayout.VERTICAL);
        card.setBackgroundResource(bgRes);
        card.setElevation(2 * dp);
        int p = (int) (14 * dp);
        card.setPadding(p, p, p, p);
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(-1, -2);
        lp.topMargin = (int) (10 * dp);
        card.setLayoutParams(lp);

        TextView t = new TextView(this);
        t.setText(title);
        t.setTextColor(ThakerStore.isDarkMode(this) ? 0xFFECFAF2 : 0xFF0F291E);
        t.setTextSize(15);
        t.getPaint().setFakeBoldText(true);
        card.addView(t);

        TextView s = new TextView(this);
        s.setText(sub);
        s.setTextColor(ThakerStore.isDarkMode(this) ? 0xFF9BC4B0 : 0xFF5A7267);
        s.setTextSize(12);
        s.setPadding(0, (int) (3 * dp), 0, 0);
        card.addView(s);
        return card;
    }

    private void addSectionTitle(LinearLayout parent, String text) {
        TextView t = new TextView(this);
        t.setText(text);
        t.setTextColor(ThakerStore.isDarkMode(this) ? 0xFFECFAF2 : 0xFF0F291E);
        t.setTextSize(22);
        t.getPaint().setFakeBoldText(true);
        parent.addView(t);
    }

    private void addMutedSub(LinearLayout parent, String text) {
        TextView t = new TextView(this);
        t.setText(text);
        t.setTextColor(ThakerStore.isDarkMode(this) ? 0xFF9BC4B0 : 0xFF5A7267);
        t.setTextSize(13);
        t.setPadding(0, (int) (2 * dp), 0, (int) (8 * dp));
        parent.addView(t);
    }

    private void addSubSectionLabel(LinearLayout parent, String text) {
        TextView t = new TextView(this);
        t.setText(text);
        t.setTextColor(0xFF059669);
        t.setTextSize(14);
        t.getPaint().setFakeBoldText(true);
        t.setPadding(0, (int) (16 * dp), 0, (int) (8 * dp));
        parent.addView(t);
    }
}
""")

    # 2. SubjectActivity.java (04-subject.png)
    _w(f"{src}/SubjectActivity.java", r"""package com.thaker.app;

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
        } else if ("math12".equals(subjectKey)) {
            tvTitle.setText("الرياضيات 3D");
            tvMeta.setText("7 وحدات · 250 صفحة · 13 مجسماً تفاعلياً");
            tvGradePill.setText("الثالث الثانوي");
            ivIcon.setImageResource(R.drawable.ic_subj_math);
            quizKey = "math_12";

            addPartCard("الكتاب التفاعلي الشامل ومعمل الرياضيات 3D", "الأعداد المركبة، ذات الحدين، القطوع، الهندسة الفضائية، الاحتمالات، المشتقات والتكامل",
                ThakerStore.getBookPct(this, "math_12", 20), "250 صفحة تفاعلية", "22 حلاً خطوة بخطوة + 13 مجسماً",
                "📐 افتح كتاب الرياضيات التفاعلي", "html", "math-12th-book.html",
                "🧊 افتح معمل الرياضيات 3D (13 مجسماً)", "math-12th-lab.html");
        } else if ("arabic_lit".equals(subjectKey)) {
            tvTitle.setText("الأدب والنصوص");
            tvMeta.setText("قسمان · 36 موضوعاً · 212 صفحة");
            tvGradePill.setText("الثالث الثانوي");
            ivIcon.setImageResource(R.drawable.ic_subj_literature);
            quizKey = "arabic_lit";

            addPartCard("الكتاب التفاعلي للأدب والنصوص والنقد", "الأدب في العصرين المملوكي والعثماني، النهضة، المدارس الأدبية، والنقد الأدبي",
                ThakerStore.getBookPct(this, "arabic_lit", 20), "212 صفحة تفاعلية", "36 تحليلاً جمالياً + بطاقات نصوص",
                "افتح كتاب الأدب والنصوص التفاعلي", "html", "arabic-literature-12th-book.html",
                "تصفح قسم النقد الأدبي", "arabic-literature-12th-book.html");
        } else if ("quran".equals(subjectKey)) {
            tvTitle.setText("القرآن الكريم وعلومه");
            tvMeta.setText("3 أقسام · 34 درساً · 188 صفحة");
            tvGradePill.setText("الثالث الثانوي");
            ivIcon.setImageResource(R.drawable.ic_subj_quran);
            quizKey = "quran";

            addPartCard("كتاب القرآن الكريم التفاعلي + المصحف الصوتي", "تفسير سورة النور (الحصري المعلم)، علوم القرآن، و18 حصة تلاوة بالرسم العثماني",
                ThakerStore.getBookPct(this, "quran", 15), "188 صفحة تفاعلية", "120 تلاوة أوفلاين + 16 تقويماً",
                "🕌 افتح كتاب القرآن الكريم التفاعلي", "html", "quran-12th-book.html",
                "🎧 افتح المصحف الصوتي والقصص", "quran-12th-book.html");
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
            tvMeta.setText("9 وحدات · 187 صفحة · 10 تجارب 3D في المعمل");
            tvGradePill.setText("الثالث الثانوي");
            ivIcon.setImageResource(R.drawable.ic_subj_chem);
            quizKey = "chem_12";

            addPartCard("الكتاب التفاعلي الشامل ومعمل الكيمياء", "العناصر الانتقالية، الكيمياء الحرارية والكهربية، النووية والعضوية والبيئة",
                ThakerStore.getBookPct(this, "chem_12", 25), "187 صفحة تفاعلية", "ربط مباشر بالمعمل 3D",
                "⚗️ افتح كتاب الكيمياء التفاعلي", "html", "chemistry-12th-book.html",
                "🔬 افتح مختبر الكيمياء 3D (10 تجارب)", "chem-lab-book.html");
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
""")

    # 3. ProgressActivity.java (11-progress.png)
    _w(f"{src}/ProgressActivity.java", r"""package com.thaker.app;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Gravity;
import android.view.View;
import android.widget.FrameLayout;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

public class ProgressActivity extends Activity {

    private float dp;
    private FrameLayout weeklyRingHost;
    private LinearLayout masteryContainer, badgesContainer;
    private TextView tvStudentSub, tvGoalMain, tvGoalHint, tvWrongCount;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_progress);
        dp = getResources().getDisplayMetrics().density;

        weeklyRingHost = findViewById(R.id.ring_weekly_host);
        masteryContainer = findViewById(R.id.mastery_grid_container);
        badgesContainer = findViewById(R.id.badges_row_container);
        tvStudentSub = findViewById(R.id.tv_prog_student_sub);
        tvGoalMain = findViewById(R.id.tv_weekly_goal_main);
        tvGoalHint = findViewById(R.id.tv_weekly_goal_hint);
        tvWrongCount = findViewById(R.id.tv_prog_wrong_count);

        findViewById(R.id.btn_prog_back).setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) { finish(); }
        });

        findViewById(R.id.card_prog_review_wrong).setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                if (ThakerStore.getWrongIds(ProgressActivity.this).isEmpty()) {
                    Toast.makeText(ProgressActivity.this, "لا توجد أسئلة خاطئة حالياً! ابدأ اختباراً للتدرب.", Toast.LENGTH_SHORT).show();
                    return;
                }
                Intent i = new Intent(ProgressActivity.this, QuizActivity.class);
                i.putExtra("quiz_subject", "all_9th");
                i.putExtra("review_wrong", true);
                startActivity(i);
            }
        });

        NavBarHelper.setup(this, "library", null);
    }

    @Override
    protected void onResume() {
        super.onResume();
        renderProgress();
    }

    private void renderProgress() {
        tvStudentSub.setText(ThakerStore.getStudentName(this) + " · " + ThakerStore.getGradeLabel(this));

        int streak = ThakerStore.getStreakDays(this);
        int goal = ThakerStore.getWeeklyGoal(this);
        tvGoalMain.setText("ذاكرت " + streak + " أيام من " + goal);
        tvGoalHint.setText(streak >= goal ? "أنجزت هدفك الأسبوعي بنجاح! 🏆" : "باقي " + (goal - streak) + " أيام لإتمام الهدف");

        weeklyRingHost.removeAllViews();
        RingProgressView ring = new RingProgressView(this);
        int sz = (int) (74 * dp);
        ring.setLayoutParams(new FrameLayout.LayoutParams(sz, sz));
        ring.configure(streak, goal, streak + "/" + goal, 0xFF059669, ThakerStore.isDarkMode(this) ? 0xFFECFAF2 : 0xFF0F291E);
        weeklyRingHost.addView(ring);

        int wrongCnt = ThakerStore.getWrongIds(this).size();
        tvWrongCount.setText(wrongCnt + " أسئلة تحتاج مراجعة");

        masteryContainer.removeAllViews();
        String[][] units = ThakerStore.getStage(this) == 1 ? new String[][]{
            {"phys_u1", "كمية التحرك", "physics"},
            {"phys_u2", "التيار المتردد", "physics"},
            {"bio_u1", "الجهاز العصبي", "biology"},
            {"bio_u2", "الهرمونات والتكاثر", "biology"},
            {"chem_u1", "العناصر الانتقالية", "chemistry"},
            {"chem_u2", "الكيمياء العضوية", "chemistry"}
        } : new String[][]{
            {"u9", "9: التفاعلات والهالوجينات", "science"},
            {"u10", "10: خواص المادة", "science"},
            {"u11", "11: الضغط والموائع", "science"},
            {"u13", "13: الطاقة الشمسية", "science"},
            {"m_u5", "5: الدائرة والمماس", "math"},
            {"m_u6", "6: حساب المثلثات", "math"}
        };
        int[] defaults = {3, 2, 1, 0, 2, 0};

        for (int rowIdx = 0; rowIdx < units.length; rowIdx += 2) {
            LinearLayout row = new LinearLayout(this);
            row.setOrientation(LinearLayout.HORIZONTAL);
            row.setPadding(0, 0, 0, (int) (8 * dp));
            row.addView(makeMasteryTile(units[rowIdx][0], units[rowIdx][1], units[rowIdx][2], defaults[rowIdx]));
            if (rowIdx + 1 < units.length) {
                View sp = new View(this);
                sp.setLayoutParams(new LinearLayout.LayoutParams((int) (8 * dp), 1));
                row.addView(sp);
                row.addView(makeMasteryTile(units[rowIdx + 1][0], units[rowIdx + 1][1], units[rowIdx + 1][2], defaults[rowIdx + 1]));
            }
            masteryContainer.addView(row);
        }

        badgesContainer.removeAllViews();
        boolean lab = ThakerStore.hasBadge(this, "lab");
        boolean hunt = ThakerStore.hasBadge(this, "mistake_hunter");
        boolean per = streak >= 3;
        badgesContainer.addView(makeBadgeCard("🧪", "مختبري", lab ? "مفتوحة" : "جرّب معمل 3D", lab));
        View s1 = new View(this); s1.setLayoutParams(new LinearLayout.LayoutParams((int) (8 * dp), 1));
        badgesContainer.addView(s1);
        badgesContainer.addView(makeBadgeCard("🎯", "صائد الأخطاء", hunt ? "مفتوحة" : "صحّح خطأً", hunt));
        View s2 = new View(this); s2.setLayoutParams(new LinearLayout.LayoutParams((int) (8 * dp), 1));
        badgesContainer.addView(s2);
        badgesContainer.addView(makeBadgeCard("🔥", "المثابر", per ? "مفتوحة" : "سلسلة 3 أيام", per));
    }

    private LinearLayout makeMasteryTile(String unitId, String title, final String subjKey, int defLvl) {
        int lvl = ThakerStore.getUnitMastery(this, unitId, defLvl);
        String label;
        int bg, fg;
        if (lvl >= 3) { label = "متقن"; bg = R.drawable.pill_mint; fg = 0xFF065F46; }
        else if (lvl == 2) { label = "متوسط"; bg = R.drawable.pill_gold; fg = 0xFF92400E; }
        else if (lvl == 1) { label = "ضعيف"; bg = R.drawable.pill_rose; fg = 0xFF991B1B; }
        else { label = "لم يبدأ"; bg = R.drawable.pill_gray; fg = 0xFF475569; }

        LinearLayout tile = new LinearLayout(this);
        tile.setOrientation(LinearLayout.VERTICAL);
        tile.setBackgroundResource(R.drawable.card_white_rounded);
        tile.setElevation(2 * dp);
        int p = (int) (12 * dp);
        tile.setPadding(p, p, p, p);
        tile.setLayoutParams(new LinearLayout.LayoutParams(0, -2, 1f));

        TextView tvBadge = new TextView(this);
        tvBadge.setText(label);
        tvBadge.setBackgroundResource(bg);
        tvBadge.setTextColor(fg);
        tvBadge.setTextSize(10);
        tvBadge.getPaint().setFakeBoldText(true);
        tvBadge.setPadding((int) (8 * dp), (int) (2 * dp), (int) (8 * dp), (int) (2 * dp));
        tvBadge.setLayoutParams(new LinearLayout.LayoutParams(-2, -2));
        tile.addView(tvBadge);

        TextView tvTitle = new TextView(this);
        tvTitle.setText("الوحدة " + title);
        tvTitle.setTextColor(ThakerStore.isDarkMode(this) ? 0xFFECFAF2 : 0xFF0F291E);
        tvTitle.setTextSize(13);
        tvTitle.getPaint().setFakeBoldText(true);
        tvTitle.setPadding(0, (int) (6 * dp), 0, 0);
        tile.addView(tvTitle);

        tile.setOnClickListener(new View.OnClickListener() {
            @Override public void onClick(View v) {
                Intent i = new Intent(ProgressActivity.this, SummaryActivity.class);
                i.putExtra("summary_subject", subjKey);
                startActivity(i);
            }
        });
        return tile;
    }

    private LinearLayout makeBadgeCard(String icon, String title, String status, boolean unlocked) {
        LinearLayout c = new LinearLayout(this);
        c.setOrientation(LinearLayout.VERTICAL);
        c.setGravity(Gravity.CENTER);
        c.setBackgroundResource(unlocked ? R.drawable.card_mint_tint : R.drawable.card_white_rounded);
        c.setElevation(2 * dp);
        int p = (int) (10 * dp);
        c.setPadding(p, p, p, p);
        c.setLayoutParams(new LinearLayout.LayoutParams(0, -2, 1f));
        c.setAlpha(unlocked ? 1f : 0.65f);

        TextView ico = new TextView(this); ico.setText(icon); ico.setTextSize(22); c.addView(ico);
        TextView ttl = new TextView(this); ttl.setText(title); ttl.setTextSize(12);
        ttl.getPaint().setFakeBoldText(true);
        ttl.setTextColor(ThakerStore.isDarkMode(this) ? 0xFFECFAF2 : 0xFF0F291E);
        ttl.setPadding(0, (int) (4 * dp), 0, 0);
        c.addView(ttl);
        TextView st = new TextView(this); st.setText(status); st.setTextSize(10);
        st.setTextColor(unlocked ? 0xFF059669 : 0xFF64748B);
        c.addView(st);
        return c;
    }
}
""")

    # 4. SummaryActivity.java (09-summary.png)
    _w(f"{src}/SummaryActivity.java", r"""package com.thaker.app;

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
""")

    # 5. QuizActivity.java (10-quiz.png)
    _w(f"{src}/QuizActivity.java", r"""package com.thaker.app;

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
""")
