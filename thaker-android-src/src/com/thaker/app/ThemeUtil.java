package com.thaker.app;

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
