package com.thaker.app;

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
