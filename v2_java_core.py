#!/usr/bin/env python3
"""
V2 Core Java Classes for Thaker (ذاكر):
- ThakerStore.java (offline SharedPreferences state: profile, resume, tasks, streak, mistakes, bookmarks, mastery)
- ThemeUtil.java (Mint Light default + Dark Mode toggle)
- RingProgressView.java (anti-aliased Canvas arc progress ring for 04-subject & 11-progress)
- NavBarHelper.java (shared 5-tab floating pill dock handler across Activities)
- SplashActivity.java (01-splash.png)
- OnboardingActivity.java (02-onboarding.png)
- LabActivity.java (WebView host with #page=X&tab=Y deep linking + updateProgress bridge)
"""
import os


def _w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.lstrip("\n"))


def write_v2_core_java(base_dir):
    src = f"{base_dir}/src/com/thaker/app"

    # 1. ThakerStore.java
    _w(f"{src}/ThakerStore.java", """package com.thaker.app;

import android.content.Context;
import android.content.SharedPreferences;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;

public class ThakerStore {
    private static final String PREF = "thaker_v2_prefs";

    private static SharedPreferences prefs(Context ctx) {
        return ctx.getSharedPreferences(PREF, Context.MODE_PRIVATE);
    }

    public static boolean isOnboarded(Context ctx) {
        return prefs(ctx).getBoolean("onboarded", false);
    }

    public static void setOnboarded(Context ctx, boolean done) {
        prefs(ctx).edit().putBoolean("onboarded", done).apply();
    }

    public static String getStudentName(Context ctx) {
        String n = prefs(ctx).getString("student_name", "أسماء");
        return (n == null || n.trim().isEmpty()) ? "أسماء" : n.trim();
    }

    public static void setStudentName(Context ctx, String name) {
        prefs(ctx).edit().putString("student_name", (name == null || name.trim().isEmpty()) ? "أسماء" : name.trim()).apply();
    }

    public static int getStage(Context ctx) {
        return prefs(ctx).getInt("stage", 0); // 0 = prep (7-9), 1 = high (10-12)
    }

    public static void setStage(Context ctx, int stage) {
        prefs(ctx).edit().putInt("stage", stage).apply();
    }

    public static int getGrade(Context ctx) {
        return prefs(ctx).getInt("grade", 9);
    }

    public static void setGrade(Context ctx, int grade) {
        prefs(ctx).edit().putInt("grade", grade).apply();
    }

    public static String getGradeLabel(Context ctx) {
        int g = getGrade(ctx);
        switch (g) {
            case 7: return "الصف السابع";
            case 8: return "الصف الثامن";
            case 9: return "الصف التاسع";
            case 10: return "الأول الثانوي";
            case 11: return "الثاني الثانوي";
            case 12: return "الثالث الثانوي";
            default: return "الصف التاسع";
        }
    }

    public static int getExamDaysLeft(Context ctx) {
        return prefs(ctx).getInt("exam_days", 199);
    }

    public static void setExamDaysLeft(Context ctx, int days) {
        prefs(ctx).edit().putInt("exam_days", Math.max(1, days)).apply();
    }

    public static int getWeeklyGoal(Context ctx) {
        return prefs(ctx).getInt("weekly_goal", 5);
    }

    public static void setWeeklyGoal(Context ctx, int days) {
        prefs(ctx).edit().putInt("weekly_goal", Math.max(1, days)).apply();
    }

    public static int getStreakDays(Context ctx) {
        return prefs(ctx).getInt("streak_days", 4);
    }

    public static void bumpStudyStreak(Context ctx) {
        int g = getWeeklyGoal(ctx);
        int cur = getStreakDays(ctx);
        if (cur < g) {
            prefs(ctx).edit().putInt("streak_days", cur + 1).apply();
        }
    }

    public static boolean isDarkMode(Context ctx) {
        return prefs(ctx).getBoolean("dark_mode", false);
    }

    public static void setDarkMode(Context ctx, boolean dark) {
        prefs(ctx).edit().putBoolean("dark_mode", dark).apply();
    }

    // Resume last read tracking
    public static String getLastTitle(Context ctx) {
        String def = getStage(ctx) == 1 ? "الفيزياء - الثالث الثانوي" : "العلوم - الجزء الثاني";
        return prefs(ctx).getString("last_title", def);
    }

    public static String getLastSubtitle(Context ctx) {
        String def = getStage(ctx) == 1 ? "الوحدة 1 · صفحة 9" : "الوحدة 9 · صفحة 8";
        return prefs(ctx).getString("last_subtitle", def);
    }

    public static String getLastAsset(Context ctx) {
        String def = getStage(ctx) == 1 ? "physics-12th-book.html" : "thaker-interactive-book.html";
        return prefs(ctx).getString("last_asset", def);
    }

    public static String getLastType(Context ctx) {
        return prefs(ctx).getString("last_type", "html"); // "html" or "pdf"
    }

    public static int getLastPage(Context ctx) {
        return prefs(ctx).getInt("last_page", getStage(ctx) == 1 ? 9 : 8);
    }

    public static int getLastPct(Context ctx) {
        return prefs(ctx).getInt("last_pct", 38);
    }

    public static void saveReadingProgress(Context ctx, String bookKey, String title, String subtitle, String type, String assetOrPdfKey, int page, int pct) {
        SharedPreferences.Editor ed = prefs(ctx).edit();
        ed.putString("last_title", title);
        ed.putString("last_subtitle", subtitle);
        ed.putString("last_type", type);
        ed.putString("last_asset", assetOrPdfKey);
        ed.putInt("last_page", Math.max(1, page));
        int clamped = Math.max(1, Math.min(100, pct));
        ed.putInt("last_pct", clamped);
        if (bookKey != null && !bookKey.isEmpty()) {
            ed.putInt("book_pct_" + bookKey, clamped);
        }
        ed.putBoolean("task_read_done", true);
        ed.apply();
    }

    public static int getBookPct(Context ctx, String bookKey, int defaultPct) {
        return prefs(ctx).getInt("book_pct_" + bookKey, defaultPct);
    }

    public static boolean isTaskDone(Context ctx, int idx) {
        return prefs(ctx).getBoolean(idx == 1 ? "task_read_done" : "task_quiz_done", idx == 1);
    }

    public static void setTaskDone(Context ctx, int idx, boolean done) {
        prefs(ctx).edit().putBoolean(idx == 1 ? "task_read_done" : "task_quiz_done", done).apply();
    }

    // Wrong question IDs bank (strings separated by comma)
    public static List<String> getWrongIds(Context ctx) {
        String raw = prefs(ctx).getString("wrong_ids", "");
        List<String> out = new ArrayList<String>();
        if (raw == null || raw.trim().isEmpty()) return out;
        for (String p : raw.split(",")) {
            String t = p.trim();
            if (!t.isEmpty() && !out.contains(t)) out.add(t);
        }
        return out;
    }

    public static void addWrongId(Context ctx, String qid) {
        if (qid == null || qid.trim().isEmpty()) return;
        Set<String> set = new LinkedHashSet<String>(getWrongIds(ctx));
        set.add(qid.trim());
        saveWrongSet(ctx, set);
    }

    public static void removeWrongId(Context ctx, String qid) {
        if (qid == null) return;
        Set<String> set = new LinkedHashSet<String>(getWrongIds(ctx));
        if (set.remove(qid.trim())) {
            prefs(ctx).edit().putBoolean("badge_mistake_hunter", true).apply();
            saveWrongSet(ctx, set);
        }
    }

    private static void saveWrongSet(Context ctx, Set<String> set) {
        StringBuilder sb = new StringBuilder();
        for (String s : set) {
            if (sb.length() > 0) sb.append(",");
            sb.append(s);
        }
        prefs(ctx).edit().putString("wrong_ids", sb.toString()).apply();
    }

    // Unit Mastery (0=not started, 1=weak, 2=medium, 3=mastered)
    public static int getUnitMastery(Context ctx, String unitKey, int defaultVal) {
        return prefs(ctx).getInt("mastery_" + unitKey, defaultVal);
    }

    public static void setUnitMastery(Context ctx, String unitKey, int level) {
        prefs(ctx).edit().putInt("mastery_" + unitKey, Math.max(0, Math.min(3, level))).apply();
    }

    // Bookmarks ("label|type|target|page")
    public static List<String> getBookmarks(Context ctx) {
        String raw = prefs(ctx).getString("bookmarks_v2", "");
        List<String> list = new ArrayList<String>();
        if (raw != null && !raw.trim().isEmpty()) {
            list.addAll(Arrays.asList(raw.split(";;")));
        }
        return list;
    }

    public static boolean toggleBookmark(Context ctx, String entry) {
        List<String> cur = getBookmarks(ctx);
        boolean added;
        if (cur.contains(entry)) {
            cur.remove(entry);
            added = false;
        } else {
            cur.add(0, entry);
            added = true;
        }
        StringBuilder sb = new StringBuilder();
        for (String item : cur) {
            if (item == null || item.trim().isEmpty()) continue;
            if (sb.length() > 0) sb.append(";;");
            sb.append(item);
        }
        prefs(ctx).edit().putString("bookmarks_v2", sb.toString()).apply();
        return added;
    }

    public static void unlockLabBadge(Context ctx) {
        prefs(ctx).edit().putBoolean("badge_lab", true).apply();
    }

    public static boolean hasBadge(Context ctx, String key) {
        return prefs(ctx).getBoolean("badge_" + key, false);
    }

    public static void resetAll(Context ctx) {
        prefs(ctx).edit().clear().apply();
    }
}
""")

    # 2. ThemeUtil.java
    _w(f"{src}/ThemeUtil.java", """package com.thaker.app;

import android.app.Activity;

public class ThemeUtil {
    public static void apply(Activity activity) {
        if (ThakerStore.isDarkMode(activity)) {
            activity.setTheme(R.style.AppTheme_Dark);
        } else {
            activity.setTheme(R.style.AppTheme);
        }
    }

    public static void toggleDarkMode(Activity activity, boolean dark) {
        ThakerStore.setDarkMode(activity, dark);
        activity.recreate();
    }
}
""")

    # 3. RingProgressView.java (anti-aliased Canvas arc ring matching 04-subject & 11-progress)
    _w(f"{src}/RingProgressView.java", """package com.thaker.app;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.RectF;
import android.view.View;

public class RingProgressView extends View {
    private int progress = 0;
    private int max = 100;
    private String centerText = "0%";
    private int ringColor = 0xFF059669;
    private int trackColor = 0xFFDCE8E0;
    private int textColor = 0xFF0F291E;

    private final Paint trackPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final Paint arcPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final Paint textPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final RectF arcBounds = new RectF();

    public RingProgressView(Context context) {
        super(context);
        float dp = context.getResources().getDisplayMetrics().density;
        trackPaint.setStyle(Paint.Style.STROKE);
        trackPaint.setStrokeWidth(6.5f * dp);
        trackPaint.setStrokeCap(Paint.Cap.ROUND);

        arcPaint.setStyle(Paint.Style.STROKE);
        arcPaint.setStrokeWidth(6.5f * dp);
        arcPaint.setStrokeCap(Paint.Cap.ROUND);

        textPaint.setTextAlign(Paint.Align.CENTER);
        textPaint.setTextSize(14f * dp);
        textPaint.setFakeBoldText(true);
    }

    public void configure(int progress, int max, String label, int ringColor, int textColor) {
        this.progress = Math.max(0, progress);
        this.max = Math.max(1, max);
        this.centerText = label != null ? label : (progress + "%");
        this.ringColor = ringColor;
        this.textColor = textColor;
        invalidate();
    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        float w = getWidth();
        float h = getHeight();
        float stroke = arcPaint.getStrokeWidth();
        float pad = stroke / 2f + 2f;
        arcBounds.set(pad, pad, w - pad, h - pad);

        trackPaint.setColor(trackColor);
        arcPaint.setColor(ringColor);
        textPaint.setColor(textColor);

        canvas.drawOval(arcBounds, trackPaint);
        float sweep = 360f * Math.min(progress, max) / (float) max;
        canvas.drawArc(arcBounds, -90f, sweep, false, arcPaint);

        Paint.FontMetrics fm = textPaint.getFontMetrics();
        float ty = h / 2f - (fm.ascent + fm.descent) / 2f;
        canvas.drawText(centerText, w / 2f, ty, textPaint);
    }
}
""")

    # 4. NavBarHelper.java (shared bottom 5-tab floating pill dock handler)
    _w(f"{src}/NavBarHelper.java", """package com.thaker.app;

import android.app.Activity;
import android.content.Intent;
import android.view.View;
import android.widget.TextView;

public class NavBarHelper {

    public interface TabListener {
        void onTabSelected(String tabKey);
    }

    public static void setup(final Activity activity, String activeTab, final TabListener inActivityListener) {
        View dock = activity.findViewById(R.id.bottom_dock);
        if (dock == null) return;

        int activeCol = 0xFF059669;
        int mutedCol = ThakerStore.isDarkMode(activity) ? 0xFF9BC4B0 : 0xFF5A7267;

        TextView lblSubj = dock.findViewById(R.id.nav_lbl_subjects);
        TextView lblLib = dock.findViewById(R.id.nav_lbl_library);
        TextView lblBook = dock.findViewById(R.id.nav_lbl_bookmarks);
        TextView lblSet = dock.findViewById(R.id.nav_lbl_settings);

        if (lblSubj != null) lblSubj.setTextColor("subjects".equals(activeTab) ? activeCol : mutedCol);
        if (lblLib != null) lblLib.setTextColor("library".equals(activeTab) ? activeCol : mutedCol);
        if (lblBook != null) lblBook.setTextColor("bookmarks".equals(activeTab) ? activeCol : mutedCol);
        if (lblSet != null) lblSet.setTextColor("settings".equals(activeTab) ? activeCol : mutedCol);

        bindTab(activity, dock, R.id.nav_tab_home, "home", inActivityListener);
        bindTab(activity, dock, R.id.nav_tab_subjects, "subjects", inActivityListener);
        bindTab(activity, dock, R.id.nav_tab_library, "library", inActivityListener);
        bindTab(activity, dock, R.id.nav_tab_bookmarks, "bookmarks", inActivityListener);
        bindTab(activity, dock, R.id.nav_tab_settings, "settings", inActivityListener);
    }

    private static void bindTab(final Activity activity, View dock, int viewId, final String tabKey, final TabListener listener) {
        View v = dock.findViewById(viewId);
        if (v == null) return;
        v.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (listener != null) {
                    listener.onTabSelected(tabKey);
                } else {
                    Intent i = new Intent(activity, MainActivity.class);
                    i.putExtra("open_tab", tabKey);
                    i.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
                    activity.startActivity(i);
                    activity.finish();
                }
            }
        });
    }
}
""")

    # 5. SplashActivity.java (01-splash.png)
    _w(f"{src}/SplashActivity.java", """package com.thaker.app;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.view.View;

public class SplashActivity extends Activity {
    private boolean navigated = false;
    private final Handler handler = new Handler(Looper.getMainLooper());
    private final Runnable autoAdvance = new Runnable() {
        @Override
        public void run() {
            goNext();
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);

        View root = findViewById(R.id.splash_root);
        if (root != null) {
            root.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    goNext();
                }
            });
        }
        handler.postDelayed(autoAdvance, 1400);
    }

    private void goNext() {
        if (navigated) return;
        navigated = true;
        handler.removeCallbacks(autoAdvance);
        Class<?> target = ThakerStore.isOnboarded(this) ? MainActivity.class : OnboardingActivity.class;
        startActivity(new Intent(this, target));
        overridePendingTransition(android.R.anim.fade_in, android.R.anim.fade_out);
        finish();
    }

    @Override
    protected void onDestroy() {
        handler.removeCallbacks(autoAdvance);
        super.onDestroy();
    }
}
""")

    # 6. OnboardingActivity.java (02-onboarding.png)
    _w(f"{src}/OnboardingActivity.java", """package com.thaker.app;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;

public class OnboardingActivity extends Activity {

    private int step = 1;
    private int selectedStage = 0; // 0 prep, 1 high
    private int selectedGrade = 9;
    private int examDays = 199;
    private int weeklyGoal = 5;

    private TextView tvStepBadge, btnExamPill, chkPrep, chkSec;
    private ProgressBar progBar;
    private View step1View, step2View, step3View;
    private View cardPrep, cardSec;
    private Button btnG1, btnG2, btnG3, btnNext;
    private Button btnGoal3, btnGoal5, btnGoal7;
    private EditText etName;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_onboarding);

        selectedStage = ThakerStore.getStage(this);
        selectedGrade = ThakerStore.getGrade(this);
        examDays = ThakerStore.getExamDaysLeft(this);
        weeklyGoal = ThakerStore.getWeeklyGoal(this);

        tvStepBadge = findViewById(R.id.tv_onb_step_badge);
        progBar = findViewById(R.id.prog_onboarding);
        step1View = findViewById(R.id.onb_step_1);
        step2View = findViewById(R.id.onb_step_2);
        step3View = findViewById(R.id.onb_step_3);

        cardPrep = findViewById(R.id.card_stage_prep);
        cardSec = findViewById(R.id.card_stage_sec);
        chkPrep = findViewById(R.id.chk_stage_prep);
        chkSec = findViewById(R.id.chk_stage_sec);

        btnG1 = findViewById(R.id.btn_grade_opt1);
        btnG2 = findViewById(R.id.btn_grade_opt2);
        btnG3 = findViewById(R.id.btn_grade_opt3);
        btnExamPill = findViewById(R.id.btn_exam_days_pill);

        etName = findViewById(R.id.et_onb_name);
        etName.setText(ThakerStore.getStudentName(this));
        btnGoal3 = findViewById(R.id.btn_goal_3);
        btnGoal5 = findViewById(R.id.btn_goal_5);
        btnGoal7 = findViewById(R.id.btn_goal_7);
        btnNext = findViewById(R.id.btn_onb_next);

        findViewById(R.id.btn_onb_skip).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finishOnboarding();
            }
        });

        cardPrep.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                selectedStage = 0;
                selectedGrade = 9;
                renderStep1Ui();
            }
        });

        cardSec.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                selectedStage = 1;
                selectedGrade = 12;
                renderStep1Ui();
            }
        });

        btnG1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                selectedGrade = selectedStage == 0 ? 7 : 10;
                renderStep1Ui();
            }
        });
        btnG2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                selectedGrade = selectedStage == 0 ? 8 : 11;
                renderStep1Ui();
            }
        });
        btnG3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                selectedGrade = selectedStage == 0 ? 9 : 12;
                renderStep1Ui();
            }
        });

        btnExamPill.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                final String[] opts = {"90 يوماً (3 أشهر)", "150 يوماً (5 أشهر)", "199 يوماً (بداية العام)", "30 يوماً (مراجعة نهائية)"};
                final int[] vals = {90, 150, 199, 30};
                new AlertDialog.Builder(OnboardingActivity.this)
                    .setTitle("الوقت المتبقي على الامتحان")
                    .setItems(opts, new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                            examDays = vals[which];
                            btnExamPill.setText(examDays + " يوماً");
                        }
                    }).show();
            }
        });

        btnGoal3.setOnClickListener(new View.OnClickListener() { @Override public void onClick(View v) { weeklyGoal = 3; renderGoalButtons(); }});
        btnGoal5.setOnClickListener(new View.OnClickListener() { @Override public void onClick(View v) { weeklyGoal = 5; renderGoalButtons(); }});
        btnGoal7.setOnClickListener(new View.OnClickListener() { @Override public void onClick(View v) { weeklyGoal = 7; renderGoalButtons(); }});

        btnNext.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (step < 3) {
                    step++;
                    renderWizardStep();
                } else {
                    finishOnboarding();
                }
            }
        });

        renderStep1Ui();
        renderGoalButtons();
        renderWizardStep();
    }

    private void renderStep1Ui() {
        boolean isPrep = (selectedStage == 0);
        cardPrep.setBackgroundResource(isPrep ? R.drawable.onboarding_card_selected : R.drawable.onboarding_card_normal);
        cardSec.setBackgroundResource(!isPrep ? R.drawable.onboarding_card_selected : R.drawable.onboarding_card_normal);
        chkPrep.setBackgroundResource(isPrep ? R.drawable.pill_mint : R.drawable.pill_gray);
        chkPrep.setText(isPrep ? "✓" : "");
        chkSec.setBackgroundResource(!isPrep ? R.drawable.pill_mint : R.drawable.pill_gray);
        chkSec.setText(!isPrep ? "✓" : "");

        if (isPrep) {
            btnG1.setText("السابع");
            btnG2.setText("الثامن");
            btnG3.setText("التاسع");
            styleGradeChip(btnG1, selectedGrade == 7);
            styleGradeChip(btnG2, selectedGrade == 8);
            styleGradeChip(btnG3, selectedGrade == 9);
        } else {
            btnG1.setText("الأول الثانوي");
            btnG2.setText("الثاني الثانوي");
            btnG3.setText("الثالث الثانوي");
            styleGradeChip(btnG1, selectedGrade == 10);
            styleGradeChip(btnG2, selectedGrade == 11);
            styleGradeChip(btnG3, selectedGrade == 12);
        }
        btnExamPill.setText(examDays + " يوماً");
    }

    private void styleGradeChip(Button btn, boolean active) {
        btn.setBackgroundResource(active ? R.drawable.pill_emerald_btn : R.drawable.onboarding_card_normal);
        btn.setTextColor(active ? 0xFFFFFFFF : (ThakerStore.isDarkMode(this) ? 0xFFECFAF2 : 0xFF0F291E));
    }

    private void renderGoalButtons() {
        styleGradeChip(btnGoal3, weeklyGoal == 3);
        styleGradeChip(btnGoal5, weeklyGoal == 5);
        styleGradeChip(btnGoal7, weeklyGoal == 7);
    }

    private void renderWizardStep() {
        tvStepBadge.setText("الخطوة " + step + " من 3");
        progBar.setProgress(step);
        step1View.setVisibility(step == 1 ? View.VISIBLE : View.GONE);
        step2View.setVisibility(step == 2 ? View.VISIBLE : View.GONE);
        step3View.setVisibility(step == 3 ? View.VISIBLE : View.GONE);
        btnNext.setText(step < 3 ? "التالي  ←" : "ابدأ التعلم الآن  ←");
    }

    private void finishOnboarding() {
        ThakerStore.setStage(this, selectedStage);
        ThakerStore.setGrade(this, selectedGrade);
        ThakerStore.setExamDaysLeft(this, examDays);
        ThakerStore.setWeeklyGoal(this, weeklyGoal);
        if (etName != null) {
            ThakerStore.setStudentName(this, etName.getText().toString());
        }
        ThakerStore.setOnboarded(this, true);
        startActivity(new Intent(this, MainActivity.class));
        finish();
    }
}
""")

    # 7. LabActivity.java (with #page=X&tab=Y + updateProgress JS bridge)
    _w(f"{src}/LabActivity.java", """package com.thaker.app;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.os.Bundle;
import android.speech.tts.TextToSpeech;
import android.view.View;
import android.webkit.JavascriptInterface;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import java.util.Locale;

public class LabActivity extends Activity {

    private WebView webView;
    private String htmlAsset = "thaker-interactive-book.html";
    private TextToSpeech tts;
    private volatile boolean ttsReady = false;

    @SuppressLint({"SetJavaScriptEnabled", "JavascriptInterface"})
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lab);

        tts = new TextToSpeech(this, new TextToSpeech.OnInitListener() {
            @Override
            public void onInit(int status) {
                ttsReady = (status == TextToSpeech.SUCCESS);
            }
        });

        String requested = getIntent().getStringExtra("html_asset");
        if (requested != null && !requested.trim().isEmpty()) {
            htmlAsset = requested.trim();
        }
        int startPage = getIntent().getIntExtra("start_page", 0);
        String startTab = getIntent().getStringExtra("start_tab");

        ThakerStore.unlockLabBadge(this);

        webView = findViewById(R.id.webview);
        WebSettings ws = webView.getSettings();
        ws.setJavaScriptEnabled(true);
        ws.setDomStorageEnabled(true);
        ws.setAllowFileAccess(true);
        ws.setAllowFileAccessFromFileURLs(true);
        ws.setAllowUniversalAccessFromFileURLs(true);
        ws.setBuiltInZoomControls(true);
        ws.setDisplayZoomControls(false);
        ws.setUseWideViewPort(true);
        ws.setLoadWithOverviewMode(true);
        webView.setLayerType(View.LAYER_TYPE_HARDWARE, null);

        webView.addJavascriptInterface(new Object() {
            @JavascriptInterface
            public void returnToHome() {
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        finish();
                    }
                });
            }

            @JavascriptInterface
            public void updateProgress(String bookTitle, int pageNum, int pct, String unitId, String sectionTitle) {
                String cleanTitle = (bookTitle != null && !bookTitle.trim().isEmpty()) ? bookTitle.trim() : getBookTitleForAsset(htmlAsset);
                String sub = (sectionTitle != null && !sectionTitle.trim().isEmpty())
                        ? (sectionTitle.trim() + " · صفحة " + pageNum)
                        : ("صفحة " + pageNum);
                ThakerStore.saveReadingProgress(LabActivity.this, assetToKey(htmlAsset), cleanTitle, sub, "html", htmlAsset, pageNum, pct);
                if (unitId != null && !unitId.trim().isEmpty()) {
                    int lvl = pct >= 70 ? 3 : (pct >= 25 ? 2 : 1);
                    ThakerStore.setUnitMastery(LabActivity.this, unitId.trim(), Math.max(lvl, ThakerStore.getUnitMastery(LabActivity.this, unitId.trim(), 0)));
                }
            }

            @JavascriptInterface
            public boolean isTtsAvailable() {
                return ttsReady && tts != null;
            }

            @JavascriptInterface
            public boolean speak(final String text, final String lang) {
                if (!ttsReady || tts == null || text == null || text.trim().isEmpty()) {
                    return false;
                }
                final String tag = (lang == null || lang.trim().isEmpty()) ? "en-GB" : lang.trim();
                final Locale loc = Locale.forLanguageTag(tag.replace('_', '-'));
                int res = tts.setLanguage(loc);
                if (res == TextToSpeech.LANG_MISSING_DATA || res == TextToSpeech.LANG_NOT_SUPPORTED) {
                    if (tag.toLowerCase(Locale.US).startsWith("en")) {
                        res = tts.setLanguage(Locale.US);
                    }
                }
                if (res == TextToSpeech.LANG_MISSING_DATA || res == TextToSpeech.LANG_NOT_SUPPORTED) {
                    return false;
                }
                tts.speak(text.trim(), TextToSpeech.QUEUE_FLUSH, null, "thaker_tts");
                return true;
            }
        }, "ThakerBridge");

        webView.setWebViewClient(new WebViewClient());
        webView.setWebChromeClient(new WebChromeClient());

        StringBuilder url = new StringBuilder("file:///android_asset/").append(htmlAsset);
        if (startPage > 0 || (startTab != null && !startTab.isEmpty())) {
            url.append("#");
            boolean needAmp = false;
            if (startPage > 0) {
                url.append("page=").append(startPage);
                needAmp = true;
            }
            if (startTab != null && !startTab.isEmpty()) {
                if (needAmp) url.append("&");
                url.append("tab=").append(startTab);
            }
        }
        webView.loadUrl(url.toString());
    }

    private String assetToKey(String asset) {
        if (asset.contains("thaker-interactive")) return "sci_p2";
        if (asset.contains("science-9th")) return "sci_p1_lab";
        if (asset.contains("math-9th")) return "math_lab";
        if (asset.contains("math-12th")) return "math_12";
        if (asset.contains("arabic-literature-12th")) return "arabic_lit";
        if (asset.contains("quran-12th")) return "quran";
        if (asset.contains("physics-12th")) return "phys_12";
        if (asset.contains("biology-12th")) return "bio_12";
        if (asset.contains("chemistry-12th") || asset.contains("chem-lab")) return "chem_12";
        return "chem_12";
    }

    private String getBookTitleForAsset(String asset) {
        if (asset.contains("thaker-interactive")) return "العلوم - الجزء الثاني";
        if (asset.contains("science-9th")) return "العلوم 3D - الصف التاسع";
        if (asset.contains("math-9th")) return "الرياضيات 3D - الصف التاسع";
        if (asset.contains("math-12th")) return "الرياضيات - الثالث الثانوي";
        if (asset.contains("arabic-literature-12th")) return "الأدب والنصوص - الثالث الثانوي";
        if (asset.contains("quran-12th")) return "القرآن الكريم وعلومه - الثالث الثانوي";
        if (asset.contains("physics-12th")) return "الفيزياء - الثالث الثانوي";
        if (asset.contains("biology-12th")) return "الأحياء - الثالث الثانوي";
        if (asset.contains("chem-lab")) return "مختبر الكيمياء 3D - الثالث الثانوي";
        return "الكيمياء - الثالث الثانوي";
    }

    @Override
    public void onBackPressed() {
        if (webView != null && webView.canGoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (tts != null) tts.stop();
        if (webView != null) webView.onPause();
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (webView != null) webView.onResume();
    }

    @Override
    protected void onDestroy() {
        if (tts != null) {
            tts.stop();
            tts.shutdown();
        }
        if (webView != null) webView.destroy();
        super.onDestroy();
    }
}
""")
