package com.thaker.app;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;
import android.util.TypedValue;

public final class ThemeUtil {
    private static final String PREFS = "thaker_theme_prefs";
    private static final String KEY_DARK = "dark_mode";

    public static void apply(Activity activity) {
        SharedPreferences prefs = activity.getSharedPreferences(PREFS, Context.MODE_PRIVATE);
        boolean dark = prefs.getBoolean(KEY_DARK, false);
        activity.setTheme(dark ? R.style.AppTheme_Dark : R.style.AppTheme_Light);
    }

    public static boolean isDark(Context context) {
        return context.getSharedPreferences(PREFS, Context.MODE_PRIVATE).getBoolean(KEY_DARK, false);
    }

    public static void setDark(Activity activity, boolean dark) {
        activity.getSharedPreferences(PREFS, Context.MODE_PRIVATE).edit().putBoolean(KEY_DARK, dark).apply();
        activity.recreate();
    }

    public static void toggle(Activity activity) {
        setDark(activity, !isDark(activity));
    }

    public static int color(Context context, int attr) {
        TypedValue value = new TypedValue();
        if (context.getTheme().resolveAttribute(attr, value, true)) {
            return value.data;
        }
        return 0;
    }
}
