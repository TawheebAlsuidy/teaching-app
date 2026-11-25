package com.thaker.app;

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
            row1.addView(makeSubjectTile("الكيمياء 3D", "الثالث الثانوي", R.drawable.ic_subj_chem, R.drawable.card_mint_tint, "chemistry", true));
            row1.addView(makeSpace(10));
            row1.addView(makeSubjectTile("الفيزياء 3D", "منهج تفاعلي", R.drawable.ic_subj_physics, R.drawable.card_cream_tint, "physics", true));
            homeSubjectsContainer.addView(row1);

            LinearLayout row2 = makeRow();
            row2.setPadding(0, (int) (10 * dp), 0, 0);
            row2.addView(makeSubjectTile("الأحياء 3D", "منهج تفاعلي", R.drawable.ic_subj_bio, R.drawable.card_mint_tint, "biology", true));
            row2.addView(makeSpace(10));
            row2.addView(makeSubjectTile("التاسع (العلوم)", "استعراض الإعدادية", R.drawable.ic_subj_science, R.drawable.card_white_rounded, "science", true));
            homeSubjectsContainer.addView(row2);
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
        r2.addView(makeSubjectTile("الكيمياء 3D", "مختبر العناصر والتفاعلات", R.drawable.ic_subj_chem, R.drawable.card_mint_tint, "chemistry", true));
        r2.addView(makeSpace(10));
        r2.addView(makeSubjectTile("الفيزياء 3D", "214 صفحة تفاعلية", R.drawable.ic_subj_physics, R.drawable.card_cream_tint, "physics", true));
        allSubjectsContainer.addView(r2);

        LinearLayout r3 = makeRow();
        r3.setPadding(0, (int) (10 * dp), 0, 0);
        r3.addView(makeSubjectTile("الأحياء 3D", "218 صفحة تفاعلية", R.drawable.ic_subj_bio, R.drawable.card_mint_tint, "biology", true));
        allSubjectsContainer.addView(r3);
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
        addHtmlBookItem("⚡ الفيزياء 12 التفاعلي (214 صفحة)", "كمية التحرك، التيار المتردد، الذرة والفيزياء النووية", "physics-12th-book.html");
        addHtmlBookItem("🧬 الأحياء 12 التفاعلي (218 صفحة)", "الجهاز العصبي، الهرمونات، الوراثة وتضاعف DNA", "biology-12th-book.html");
        addHtmlBookItem("⚗️ مختبر الكيمياء 3D - الثالث الثانوي", "معمل كيمياء ثلاثي الأبعاد بالكامل", "chem-lab-book.html");
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
