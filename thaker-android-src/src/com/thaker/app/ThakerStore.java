package com.thaker.app;

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
