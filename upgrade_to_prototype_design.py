#!/usr/bin/env python3
"""
Full transformation script to apply prototype design from prototipe.for.image.png to build_apk.py
"""
import sys
import re

BUILD_APK_PATH = "/mnt/sdcard/projects/teaching-app/build_apk.py"

with open(BUILD_APK_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update colors.xml
colors_xml_new = """    # 2. Colors and theme tokens
    with open(f"{res_dir}/values/colors.xml", "w", encoding="utf-8") as f:
        f.write(\"\"\"<?xml version="1.0" encoding="utf-8"?>
<resources>
    <!-- Light Mode (Exact match to prototipe.for.image.png) -->
    <color name="light_background">#F5FAF7</color>
    <color name="light_surface">#FFFFFF</color>
    <color name="light_surface_elevated">#FFFFFF</color>
    <color name="light_surface_soft">#EDF8F2</color>
    <color name="light_text_primary">#0F172A</color>
    <color name="light_text_secondary">#64748B</color>
    <color name="light_border">#E2F0E7</color>
    <color name="light_primary">#00A859</color>
    <color name="light_primary_dark">#008C4A</color>
    <color name="light_primary_light">#E8F8F0</color>
    <color name="light_disabled">#CBD5E1</color>
    <color name="light_success">#059669</color>
    <color name="light_warning">#F59E0B</color>
    <color name="light_error">#EF4444</color>
    <color name="light_physics">#0284C7</color>
    <color name="light_biology">#9333EA</color>

    <!-- Dark Mode -->
    <color name="dark_background">#0B151C</color>
    <color name="dark_surface">#12242E</color>
    <color name="dark_surface_elevated">#182F3B</color>
    <color name="dark_surface_soft">#1A3D36</color>
    <color name="dark_text_primary">#F8FAFC</color>
    <color name="dark_text_secondary">#94A3B8</color>
    <color name="dark_border">#244852</color>
    <color name="dark_primary">#00D678</color>
    <color name="dark_primary_dark">#00A859</color>
    <color name="dark_primary_light">#1A453B</color>
    <color name="dark_disabled">#334D55</color>
    <color name="dark_success">#10B981</color>
    <color name="dark_warning">#FBBF24</color>
    <color name="dark_error">#F87171</color>
    <color name="dark_physics">#38BDF8</color>
    <color name="dark_biology">#C084FC</color>
</resources>\"\"\")"""

pattern_colors = re.compile(r'    # 2\. Colors and theme tokens.*?with open\(f"\{res_dir\}/values/colors\.xml".*?\"\"\"\)', re.DOTALL)
text = pattern_colors.sub(colors_xml_new, text)

# 2. Add all new prototype drawables to the drawables dict
# We can find the start of drawables = { and add our drawables
prototype_drawables = """        "bg_top_wave.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="#2000B050" android:endColor="#00F5FAF7" android:angle="270" />
</shape>\"\"\",
        "header_squircle_btn.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurface" />
    <corners android:radius="14dp" />
    <stroke android:width="1dp" android:color="?attr/thakerBorder" />
</shape>\"\"\",
        "hero_card_banner.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurface" />
    <corners android:radius="26dp" />
    <stroke android:width="1.2dp" android:color="?attr/thakerBorder" />
</shape>\"\"\",
        "chip_chem_pill.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerPrimaryLight" />
    <corners android:radius="999dp" />
</shape>\"\"\",
        "chip_feature_pill.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#EDFBF4" />
    <corners android:radius="999dp" />
</shape>\"\"\",
        "stage_tab_bar_bg.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#EEF8F3" />
    <corners android:radius="999dp" />
    <stroke android:width="1dp" android:color="?attr/thakerBorder" />
</shape>\"\"\",
        "featured_book_card.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurface" />
    <corners android:radius="24dp" />
    <stroke android:width="1.2dp" android:color="?attr/thakerBorder" />
</shape>\"\"\",
        "switch_container_bg.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#EDF8F3" />
    <corners android:radius="14dp" />
</shape>\"\"\",
        "squircle_physics.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#E0F2FE" />
    <corners android:radius="16dp" />
</shape>\"\"\",
        "squircle_biology.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#F3E8FF" />
    <corners android:radius="16dp" />
</shape>\"\"\",
        "squircle_science.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#CCFBF1" />
    <corners android:radius="16dp" />
</shape>\"\"\",
        "squircle_math.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#EDE9FE" />
    <corners android:radius="16dp" />
</shape>\"\"\",
        "bottom_nav_dock.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurface" />
    <corners android:radius="28dp" />
    <stroke android:width="1dp" android:color="?attr/thakerBorder" />
</shape>\"\"\",
        "nav_fab_home.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">
    <gradient android:startColor="#00C853" android:endColor="#008C4A" android:angle="45" />
</shape>\"\"\",
        "nav_fab_glow.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">
    <solid android:color="#2600B050" />
</shape>\"\"\",
        "notification_badge_green.xml": \"\"\"<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">
    <solid android:color="#00A859" />
</shape>\"\"\",
        "ic_atom.xml": \"\"\"<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="28dp" android:height="28dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="#0284C7" android:pathData="M12,12m-2,0a2,2 0,1 1,4 0a2,2 0,1 1,-4 0"/>
    <path android:strokeColor="#0284C7" android:strokeWidth="1.4" android:pathData="M12,4.5C6.75,4.5 2.5,7.86 2.5,12C2.5,16.14 6.75,19.5 12,19.5C17.25,19.5 21.5,16.14 21.5,12C21.5,7.86 17.25,4.5 12,4.5Z" />
    <path android:strokeColor="#0284C7" android:strokeWidth="1.4" android:pathData="M5.5,7.7C2.88,12.24 3.73,17.48 7.39,19.6C11.06,21.72 16.18,19.92 18.8,15.38C21.42,10.84 20.57,5.6 16.91,3.48C13.24,1.36 8.12,3.16 5.5,7.7Z" />
    <path android:strokeColor="#0284C7" android:strokeWidth="1.4" android:pathData="M18.8,7.7C16.18,3.16 11.06,1.36 7.39,3.48C3.73,5.6 2.88,10.84 5.5,15.38C8.12,19.92 13.24,21.72 16.91,19.6C20.57,17.48 21.42,12.24 18.8,7.7Z" />
</vector>\"\"\",
        "ic_dna.xml": \"\"\"<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="28dp" android:height="28dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="#9333EA" android:pathData="M7.7,2.5c0.4,-0.4 1,-0.4 1.4,0l0.7,0.7c2.3,2.3 3.6,5.3 3.6,8.5s-1.3,6.2 -3.6,8.5l-0.7,0.7c-0.4,0.4 -1,0.4 -1.4,0c-0.4,-0.4 -0.4,-1 0,-1.4l0.7,-0.7C10.1,17 11.2,14.4 11.2,11.7S10.1,6.4 8.4,4.6L7.7,3.9C7.3,3.5 7.3,2.9 7.7,2.5z"/>
    <path android:fillColor="#9333EA" android:pathData="M16.3,2.5c-0.4,-0.4 -1,-0.4 -1.4,0l-0.7,0.7c-2.3,2.3 -3.6,5.3 -3.6,8.5s1.3,6.2 3.6,8.5l0.7,0.7c0.4,0.4 1,0.4 1.4,0c0.4,-0.4 0.4,-1 0,-1.4l-0.7,-0.7C13.9,17 12.8,14.4 12.8,11.7s1.1,-5.3 2.8,-7.1l0.7,-0.7C16.7,2.9 16.7,2.5 16.3,2.5z"/>
    <path android:strokeColor="#9333EA" android:strokeWidth="1.5" android:pathData="M8.5,5.5h7M6.5,9.5h11M6.5,14.5h11M8.5,18.5h7"/>
</vector>\"\"\",
        "ic_chevron_left.xml": \"\"\"<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:strokeColor="#94A3B8" android:strokeWidth="2.2" android:strokeLineCap="round" android:strokeLineJoin="round" android:pathData="M15,18l-6,-6l6,-6" />
</vector>\"\"\",
        "ic_layers.xml": \"\"\"<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="22dp" android:height="22dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:strokeColor="#FFFFFF" android:strokeWidth="2" android:strokeLineCap="round" android:strokeLineJoin="round" android:pathData="M12,2L2,7l10,5l10,-5zM2,12l10,5l10,-5M2,17l10,5l10,-5" />
</vector>\"\"\",
        "ic_ribbon.xml": \"\"\"<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="36dp" android:viewportWidth="24" android:viewportHeight="36">
    <path android:fillColor="#00A859" android:pathData="M0,0h24v36l-12,-8l-12,8z" />
</vector>\"\"\",
        "ic_download_box.xml": \"\"\"<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:strokeColor="?attr/thakerTextSecondary" android:strokeWidth="1.8" android:strokeLineCap="round" android:strokeLineJoin="round" android:pathData="M4,17v2a2,2 0,0 0,2 2h12a2,2 0,0 0,2 -2v-2M7,11l5,5l5,-5M12,4v12" />
</vector>\"\"\",
        "ic_bookmark.xml": \"\"\"<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:strokeColor="?attr/thakerTextSecondary" android:strokeWidth="1.8" android:strokeLineCap="round" android:strokeLineJoin="round" android:pathData="M19,21l-7,-5l-7,5V5a2,2 0,0 1,2 -2h10a2,2 0,0 1,2 2z" />
</vector>\"\"\",
        "ic_settings_gear.xml": \"\"\"<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:strokeColor="?attr/thakerTextSecondary" android:strokeWidth="1.8" android:strokeLineCap="round" android:strokeLineJoin="round" android:pathData="M12,15a3,3 0,1 0,0 -6a3,3 0,0 0,0 6zM19.4,15a1.65,1.65 0,0 0,0.33 1.82l0.06,0.06a2,2 0,0 1,-2.83 2.83l-0.06,-0.06a1.65,1.65 0,0 0,-1.82,-0.33 1.65,1.65 0,0 0,-1 1.51V21a2,2 0,0 1,-4 0v-0.09A1.65,1.65 0,0 0,9 19.4a1.65,1.65 0,0 0,-1.82,0.33l-0.06,0.06a2,2 0,0 1,-2.83,-2.83l0.06,-0.06a1.65,1.65 0,0 0,0.33,-1.82 1.65,1.65 0,0 0,-1.51,-1H3a2,2 0,0 1,0,-4h0.09A1.65,1.65 0,0 0,4.6 9a1.65,1.65 0,0 0,-0.33,-1.82l-0.06,-0.06a2,2 0,0 1,2.83,-2.83l0.06,0.06a1.65,1.65 0,0 0,1.82,0.33H9a1.65,1.65 0,0 0,1,-1.51V3a2,2 0,0 1,4 0v0.09a1.65,1.65 0,0 0,1,1.51 1.65,1.65 0,0 0,1.82,-0.33l0.06,-0.06a2,2 0,0 1,2.83,2.83l-0.06,0.06a1.65,1.65 0,0 0,-0.33,1.82V9a1.65,1.65 0,0 0,1.51,1H21a2,2 0,0 1,0,4h-0.09a1.65,1.65 0,0 0,-1.51,1z" />
</vector>\"\"\",
        "ic_graduation_cap.xml": \"\"\"<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:strokeColor="?attr/thakerTextSecondary" android:strokeWidth="1.8" android:strokeLineCap="round" android:strokeLineJoin="round" android:pathData="M22,10v6M2,10l10,-5l10,5l-10,5zM6,12v5c0,2.2 2.7,4 6,4s6,-1.8 6,-4v-5" />
</vector>\"\"\",
        "ic_home_white.xml": \"\"\"<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="26dp" android:height="26dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:fillColor="#FFFFFF" android:pathData="M10,20v-6h4v6h5v-8h3L12,3 2,12h3v8z" />
</vector>\"\"\",
        "ic_book_green.xml": \"\"\"<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="24dp" android:height="24dp" android:viewportWidth="24" android:viewportHeight="24">
    <path android:strokeColor="#00A859" android:strokeWidth="2" android:strokeLineCap="round" android:strokeLineJoin="round" android:pathData="M2,3h6a4,4 0,0 1,4 4v14a3,3 0,0 0,-3 -3H2zM22,3h-6a4,4 0,0 0,-4 4v14a3,3 0,0 1,3 -3h7z" />
</vector>\"\"\",
        "ic_app_logo_mortarboard.xml": \"\"\"<vector xmlns:android="http://schemas.android.com/apk/res/android" android:width="36dp" android:height="36dp" android:viewportWidth="36" android:viewportHeight="36">
    <path android:fillColor="#00A859" android:pathData="M18,3L2,11l16,8l16,-8z" />
    <path android:fillColor="#008C4A" android:pathData="M8,14.5v6c0,3 4.5,5.5 10,5.5s10,-2.5 10,-5.5v-6l-10,4.5z" />
    <path android:strokeColor="#F59E0B" android:strokeWidth="2" android:strokeLineCap="round" android:pathData="M32,13v10l2,2" />
    <path android:strokeColor="#1E293B" android:strokeWidth="2.2" android:strokeLineCap="round" android:pathData="M5,31c4.5,-2.5 8.5,-2.5 13,0c4.5,-2.5 8.5,-2.5 13,0M18,22v9" />
</vector>\"\"\",
"""

text = text.replace('    drawables = {\n', '    drawables = {\n' + prototype_drawables)

# 3. Complete activity_main.xml matching prototipe.for.image.png
activity_main_xml_new = '''    # 5. Layouts
    # A. activity_main.xml
    with open(f"{res_dir}/layout/activity_main.xml", "w", encoding="utf-8") as f:
        f.write("""<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:layoutDirection="rtl"
    android:background="?attr/thakerBackground">

    <!-- Top soft gradient wave -->
    <View
        android:layout_width="match_parent"
        android:layout_height="220dp"
        android:background="@drawable/bg_top_wave" />

    <!-- Main Container -->
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical">

        <!-- Header Bar -->
        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal"
            android:gravity="center_vertical"
            android:paddingStart="20dp"
            android:paddingEnd="20dp"
            android:paddingTop="20dp"
            android:paddingBottom="10dp">

            <!-- Profile Button -->
            <ImageButton
                android:id="@+id/btn_profile"
                android:layout_width="46dp"
                android:layout_height="46dp"
                android:background="@drawable/header_squircle_btn"
                android:src="@drawable/ic_person"
                android:tint="?attr/thakerPrimary"
                android:contentDescription="الملف الشخصي"
                android:scaleType="centerInside" />

            <!-- Center Logo & Title -->
            <LinearLayout
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:orientation="vertical"
                android:gravity="center_horizontal">

                <LinearLayout
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:orientation="horizontal"
                    android:gravity="center_vertical">

                    <ImageView
                        android:layout_width="32dp"
                        android:layout_height="32dp"
                        android:src="@drawable/ic_app_logo_mortarboard"
                        android:contentDescription="" />

                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:layout_marginStart="8dp"
                        android:text="@string/app_name"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textSize="24sp"
                        android:textStyle="bold" />
                </LinearLayout>

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="2dp"
                    android:text="@string/app_tagline_new"
                    android:textColor="?attr/thakerTextSecondary"
                    android:textSize="11sp" />

                <!-- Hidden grade label for controller binding -->
                <TextView
                    android:id="@+id/tv_grade_label"
                    android:layout_width="0dp"
                    android:layout_height="0dp"
                    android:visibility="gone" />
            </LinearLayout>

            <!-- Notifications Button with green dot -->
            <FrameLayout
                android:layout_width="46dp"
                android:layout_height="46dp">

                <ImageButton
                    android:id="@+id/btn_notifications"
                    android:layout_width="match_parent"
                    android:layout_height="match_parent"
                    android:background="@drawable/header_squircle_btn"
                    android:src="@drawable/ic_bell"
                    android:tint="?attr/thakerTextPrimary"
                    android:contentDescription="الإشعارات"
                    android:scaleType="centerInside" />

                <View
                    android:layout_width="10dp"
                    android:layout_height="10dp"
                    android:layout_gravity="top|end"
                    android:layout_marginTop="8dp"
                    android:layout_marginEnd="8dp"
                    android:background="@drawable/notification_badge_green" />
            </FrameLayout>

            <ImageButton
                android:id="@+id/btn_theme"
                android:layout_width="0dp"
                android:layout_height="0dp"
                android:visibility="gone" />
        </LinearLayout>

        <!-- Scrollable Body -->
        <ScrollView
            android:layout_width="match_parent"
            android:layout_height="0dp"
            android:layout_weight="1"
            android:fillViewport="true"
            android:clipToPadding="false"
            android:paddingStart="18dp"
            android:paddingEnd="18dp"
            android:paddingTop="6dp"
            android:paddingBottom="100dp">

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:orientation="vertical">

                <!-- 1. Top Featured Hero Card (كتاب ومعمل الكيمياء) -->
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="horizontal"
                    android:background="@drawable/hero_card_banner"
                    android:paddingStart="16dp"
                    android:paddingEnd="16dp"
                    android:paddingTop="18dp"
                    android:paddingBottom="18dp"
                    android:gravity="center_vertical"
                    android:elevation="3dp">

                    <ImageView
                        android:layout_width="114dp"
                        android:layout_height="114dp"
                        android:src="@drawable/illustration_hero_lab"
                        android:scaleType="fitCenter"
                        android:contentDescription="" />

                    <View
                        android:layout_width="12dp"
                        android:layout_height="match_parent" />

                    <LinearLayout
                        android:layout_width="0dp"
                        android:layout_height="wrap_content"
                        android:layout_weight="1"
                        android:orientation="vertical">

                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:background="@drawable/chip_chem_pill"
                            android:text="⚗️ الكيمياء"
                            android:textColor="?attr/thakerPrimary"
                            android:textSize="11sp"
                            android:textStyle="bold"
                            android:paddingStart="12dp"
                            android:paddingEnd="12dp"
                            android:paddingTop="4dp"
                            android:paddingBottom="4dp" />

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="8dp"
                            android:text="@string/chem_card_title"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="19sp"
                            android:textStyle="bold" />

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="2dp"
                            android:text="@string/chem_card_subtitle"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="12sp" />

                        <LinearLayout
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="10dp"
                            android:orientation="horizontal">

                            <TextView
                                android:layout_width="wrap_content"
                                android:layout_height="wrap_content"
                                android:background="@drawable/chip_feature_pill"
                                android:text="✓ شرح تفاعلي"
                                android:textColor="#059669"
                                android:textSize="9sp"
                                android:textStyle="bold"
                                android:paddingStart="7dp"
                                android:paddingEnd="7dp"
                                android:paddingTop="3dp"
                                android:paddingBottom="3dp" />

                            <View
                                android:layout_width="4dp"
                                android:layout_height="match_parent" />

                            <TextView
                                android:layout_width="wrap_content"
                                android:layout_height="wrap_content"
                                android:background="@drawable/chip_feature_pill"
                                android:text="✓ تجارب افتراضية"
                                android:textColor="#059669"
                                android:textSize="9sp"
                                android:textStyle="bold"
                                android:paddingStart="7dp"
                                android:paddingEnd="7dp"
                                android:paddingTop="3dp"
                                android:paddingBottom="3dp" />

                            <View
                                android:layout_width="4dp"
                                android:layout_height="match_parent" />

                            <TextView
                                android:layout_width="wrap_content"
                                android:layout_height="wrap_content"
                                android:background="@drawable/chip_feature_pill"
                                android:text="✓ بدون اتصال"
                                android:textColor="#059669"
                                android:textSize="9sp"
                                android:textStyle="bold"
                                android:paddingStart="7dp"
                                android:paddingEnd="7dp"
                                android:paddingTop="3dp"
                                android:paddingBottom="3dp" />
                        </LinearLayout>
                    </LinearLayout>
                </LinearLayout>

                <!-- 2. Segmented Stage Switcher (الثانوية / الإعدادية) -->
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="52dp"
                    android:layout_marginTop="18dp"
                    android:orientation="horizontal"
                    android:background="@drawable/stage_tab_bar_bg"
                    android:padding="4dp">

                    <Button
                        android:id="@+id/tab_high_school"
                        android:layout_width="0dp"
                        android:layout_height="match_parent"
                        android:layout_weight="1"
                        android:minHeight="0dp"
                        android:minWidth="0dp"
                        android:background="@drawable/tab_active"
                        android:text="@string/stage_high_school"
                        android:textColor="#FFFFFF"
                        android:textSize="14sp"
                        android:textStyle="bold"
                        android:drawableStart="@drawable/ic_layers"
                        android:drawablePadding="8dp"
                        android:paddingStart="16dp"
                        android:paddingEnd="16dp" />

                    <Button
                        android:id="@+id/tab_middle_school"
                        android:layout_width="0dp"
                        android:layout_height="match_parent"
                        android:layout_weight="1"
                        android:minHeight="0dp"
                        android:minWidth="0dp"
                        android:background="@drawable/tab_inactive"
                        android:text="@string/stage_middle_school"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textSize="14sp"
                        android:textStyle="bold"
                        android:drawableStart="@drawable/ic_graduation"
                        android:drawablePadding="8dp"
                        android:paddingStart="16dp"
                        android:paddingEnd="16dp" />
                </LinearLayout>

                <!-- 3. Section Header: الكتب الدراسية -->
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="22dp"
                    android:layout_marginBottom="12dp"
                    android:orientation="horizontal"
                    android:gravity="center_vertical">

                    <ImageView
                        android:layout_width="24dp"
                        android:layout_height="24dp"
                        android:src="@drawable/ic_book_green"
                        android:contentDescription="" />

                    <LinearLayout
                        android:layout_width="0dp"
                        android:layout_height="wrap_content"
                        android:layout_weight="1"
                        android:orientation="vertical"
                        android:paddingStart="10dp">

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:text="@string/section_books_title"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="18sp"
                            android:textStyle="bold" />

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="1dp"
                            android:text="@string/section_books_sub"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="12sp" />
                    </LinearLayout>
                </LinearLayout>

                <!-- High School Container -->
                <LinearLayout
                    android:id="@+id/container_high_school"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="vertical"
                    android:visibility="visible">

                    <!-- Featured Book & Lab Card -->
                    <FrameLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:background="@drawable/featured_book_card"
                        android:elevation="3dp">

                        <LinearLayout
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:orientation="vertical"
                            android:padding="16dp">

                            <LinearLayout
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:orientation="horizontal"
                                android:gravity="center_vertical">

                                <ImageView
                                    android:layout_width="128dp"
                                    android:layout_height="110dp"
                                    android:src="@drawable/illustration_featured_lab"
                                    android:scaleType="fitCenter"
                                    android:contentDescription="" />

                                <View
                                    android:layout_width="12dp"
                                    android:layout_height="match_parent" />

                                <LinearLayout
                                    android:layout_width="0dp"
                                    android:layout_height="wrap_content"
                                    android:layout_weight="1"
                                    android:orientation="vertical">

                                    <TextView
                                        android:layout_width="match_parent"
                                        android:layout_height="wrap_content"
                                        android:text="@string/chem_card_title"
                                        android:textColor="?attr/thakerTextPrimary"
                                        android:textSize="18sp"
                                        android:textStyle="bold" />

                                    <TextView
                                        android:layout_width="match_parent"
                                        android:layout_height="wrap_content"
                                        android:layout_marginTop="2dp"
                                        android:text="@string/chem_card_subtitle"
                                        android:textColor="?attr/thakerTextSecondary"
                                        android:textSize="11sp" />

                                    <Button
                                        android:id="@+id/btn_open_chem_lab"
                                        android:layout_width="match_parent"
                                        android:layout_height="46dp"
                                        android:layout_marginTop="12dp"
                                        android:minHeight="0dp"
                                        android:minWidth="0dp"
                                        android:background="@drawable/btn_primary_emerald"
                                        android:text="فتح المعمل  ▶"
                                        android:textColor="#FFFFFF"
                                        android:textSize="14sp"
                                        android:textStyle="bold"
                                        android:paddingStart="16dp"
                                        android:paddingEnd="16dp" />
                                </LinearLayout>
                            </LinearLayout>

                            <LinearLayout
                                android:layout_width="match_parent"
                                android:layout_height="44dp"
                                android:layout_marginTop="12dp"
                                android:orientation="horizontal"
                                android:background="@drawable/switch_container_bg"
                                android:gravity="center_vertical"
                                android:paddingStart="14dp"
                                android:paddingEnd="10dp">

                                <TextView
                                    android:layout_width="0dp"
                                    android:layout_height="wrap_content"
                                    android:layout_weight="1"
                                    android:text="@string/auto_launch_pref"
                                    android:textColor="?attr/thakerTextPrimary"
                                    android:textSize="12sp"
                                    android:textStyle="bold" />

                                <Switch
                                    android:id="@+id/cb_auto_launch"
                                    android:layout_width="wrap_content"
                                    android:layout_height="wrap_content"
                                    android:thumbTint="?attr/thakerPrimary"
                                    android:trackTint="#A7F3D0" />
                            </LinearLayout>
                        </LinearLayout>

                        <ImageView
                            android:layout_width="22dp"
                            android:layout_height="32dp"
                            android:layout_gravity="top|start"
                            android:layout_marginStart="24dp"
                            android:src="@drawable/ic_ribbon"
                            android:contentDescription="" />
                    </FrameLayout>

                    <!-- Physics Card -->
                    <LinearLayout
                        android:id="@+id/card_physics"
                        android:layout_width="match_parent"
                        android:layout_height="72dp"
                        android:layout_marginTop="14dp"
                        android:orientation="horizontal"
                        android:background="@drawable/surface_card"
                        android:gravity="center_vertical"
                        android:paddingStart="16dp"
                        android:paddingEnd="16dp"
                        android:elevation="2dp">

                        <ImageView
                            android:layout_width="18dp"
                            android:layout_height="18dp"
                            android:src="@drawable/ic_chevron_left"
                            android:contentDescription="" />

                        <LinearLayout
                            android:layout_width="0dp"
                            android:layout_height="wrap_content"
                            android:layout_weight="1"
                            android:orientation="vertical"
                            android:paddingStart="14dp">

                            <TextView
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:text="@string/subject_physics"
                                android:textColor="?attr/thakerTextPrimary"
                                android:textSize="16sp"
                                android:textStyle="bold" />

                            <TextView
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:layout_marginTop="2dp"
                                android:text="بصريات"
                                android:textColor="?attr/thakerTextSecondary"
                                android:textSize="12sp" />
                        </LinearLayout>

                        <FrameLayout
                            android:layout_width="48dp"
                            android:layout_height="48dp"
                            android:background="@drawable/squircle_physics">

                            <ImageView
                                android:layout_width="28dp"
                                android:layout_height="28dp"
                                android:layout_gravity="center"
                                android:src="@drawable/ic_atom"
                                android:contentDescription="" />
                        </FrameLayout>
                    </LinearLayout>

                    <!-- Biology Card -->
                    <LinearLayout
                        android:id="@+id/card_biology"
                        android:layout_width="match_parent"
                        android:layout_height="72dp"
                        android:layout_marginTop="12dp"
                        android:orientation="horizontal"
                        android:background="@drawable/surface_card"
                        android:gravity="center_vertical"
                        android:paddingStart="16dp"
                        android:paddingEnd="16dp"
                        android:elevation="2dp">

                        <ImageView
                            android:layout_width="18dp"
                            android:layout_height="18dp"
                            android:src="@drawable/ic_chevron_left"
                            android:contentDescription="" />

                        <LinearLayout
                            android:layout_width="0dp"
                            android:layout_height="wrap_content"
                            android:layout_weight="1"
                            android:orientation="vertical"
                            android:paddingStart="14dp">

                            <TextView
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:text="@string/subject_biology"
                                android:textColor="?attr/thakerTextPrimary"
                                android:textSize="16sp"
                                android:textStyle="bold" />

                            <TextView
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:layout_marginTop="2dp"
                                android:text="مجسمات"
                                android:textColor="?attr/thakerTextSecondary"
                                android:textSize="12sp" />
                        </LinearLayout>

                        <FrameLayout
                            android:layout_width="48dp"
                            android:layout_height="48dp"
                            android:background="@drawable/squircle_biology">

                            <ImageView
                                android:layout_width="28dp"
                                android:layout_height="28dp"
                                android:layout_gravity="center"
                                android:src="@drawable/ic_dna"
                                android:contentDescription="" />
                        </FrameLayout>
                    </LinearLayout>
                </LinearLayout>

                <!-- Middle School Container -->
                <LinearLayout
                    android:id="@+id/container_middle_school"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="vertical"
                    android:visibility="gone">

                    <!-- 9th Grade Hero Banner -->
                    <LinearLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:orientation="horizontal"
                        android:background="@drawable/hero_card_banner"
                        android:padding="16dp"
                        android:gravity="center_vertical"
                        android:elevation="3dp">

                        <ImageView
                            android:layout_width="96dp"
                            android:layout_height="96dp"
                            android:src="@drawable/illustration_science"
                            android:contentDescription="" />

                        <View
                            android:layout_width="12dp"
                            android:layout_height="match_parent" />

                        <LinearLayout
                            android:layout_width="0dp"
                            android:layout_height="wrap_content"
                            android:layout_weight="1"
                            android:orientation="vertical">

                            <TextView
                                android:layout_width="wrap_content"
                                android:layout_height="wrap_content"
                                android:background="@drawable/chip_chem_pill"
                                android:text="🔬 العلوم والرياضيات · تاسع"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="10sp"
                                android:textStyle="bold"
                                android:paddingStart="10dp"
                                android:paddingEnd="10dp"
                                android:paddingTop="3dp"
                                android:paddingBottom="3dp" />

                            <TextView
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:layout_marginTop="6dp"
                                android:text="منهج الصف التاسع التفاعلي"
                                android:textColor="?attr/thakerTextPrimary"
                                android:textSize="17sp"
                                android:textStyle="bold" />

                            <TextView
                                android:layout_width="match_parent"
                                android:layout_height="wrap_content"
                                android:layout_marginTop="2dp"
                                android:text="كتب 3D ومعامل وتجارب واختبارات وزارية"
                                android:textColor="?attr/thakerTextSecondary"
                                android:textSize="11sp" />
                        </LinearLayout>
                    </LinearLayout>

                    <Button
                        android:id="@+id/btn_open_sci9_3d_book"
                        android:layout_width="match_parent"
                        android:layout_height="50dp"
                        android:layout_marginTop="12dp"
                        android:background="@drawable/btn_primary_emerald"
                        android:text="كتاب ومعمل العلوم 3D  ▶"
                        android:textColor="#FFFFFF"
                        android:textSize="13sp"
                        android:textStyle="bold" />

                    <Button
                        android:id="@+id/btn_open_math9_3d_book"
                        android:layout_width="match_parent"
                        android:layout_height="50dp"
                        android:layout_marginTop="8dp"
                        android:background="@drawable/btn_primary_emerald"
                        android:text="كتاب ومعمل الرياضيات 3D  ▶"
                        android:textColor="#FFFFFF"
                        android:textSize="13sp"
                        android:textStyle="bold" />

                    <Button
                        android:id="@+id/btn_open_sci9_lab"
                        android:layout_width="match_parent"
                        android:layout_height="48dp"
                        android:layout_marginTop="8dp"
                        android:background="@drawable/surface_card"
                        android:text="معمل العلوم التفاعلي (13 درس)  ⚗️"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textSize="13sp"
                        android:textStyle="bold" />

                    <Button
                        android:id="@+id/btn_exam_9th_all"
                        android:layout_width="match_parent"
                        android:layout_height="48dp"
                        android:layout_marginTop="8dp"
                        android:background="@drawable/surface_card"
                        android:text="الاختبار الوزاري الشامل  📝"
                        android:textColor="?attr/thakerPrimary"
                        android:textSize="13sp"
                        android:textStyle="bold" />

                    <!-- Middle School Subjects -->
                    <!-- Sci P1 -->
                    <LinearLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:layout_marginTop="14dp"
                        android:background="@drawable/surface_card"
                        android:padding="12dp"
                        android:orientation="vertical">

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:text="@string/sci_p1_title"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="15sp"
                            android:textStyle="bold" />
                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="2dp"
                            android:text="@string/sci_p1_sub"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="11sp" />

                        <LinearLayout
                            android:layout_width="match_parent"
                            android:layout_height="38dp"
                            android:layout_marginTop="10dp"
                            android:orientation="horizontal">

                            <Button
                                android:id="@+id/btn_read_sci_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الكتاب"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_index_sci_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الفهرس"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_summary_sci_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الملخص"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_quiz_sci_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="اختبار"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                        </LinearLayout>
                    </LinearLayout>

                    <!-- Sci P2 -->
                    <LinearLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:layout_marginTop="10dp"
                        android:background="@drawable/surface_card"
                        android:padding="12dp"
                        android:orientation="vertical">

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:text="@string/sci_p2_title"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="15sp"
                            android:textStyle="bold" />
                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="2dp"
                            android:text="@string/sci_p2_sub"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="11sp" />

                        <LinearLayout
                            android:layout_width="match_parent"
                            android:layout_height="38dp"
                            android:layout_marginTop="10dp"
                            android:orientation="horizontal">

                            <Button
                                android:id="@+id/btn_read_sci_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الكتاب"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_index_sci_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الفهرس"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_summary_sci_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الملخص"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_quiz_sci_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="اختبار"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                        </LinearLayout>
                    </LinearLayout>

                    <!-- Math P1 -->
                    <LinearLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:layout_marginTop="10dp"
                        android:background="@drawable/surface_card"
                        android:padding="12dp"
                        android:orientation="vertical">

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:text="@string/math_p1_title"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="15sp"
                            android:textStyle="bold" />
                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="2dp"
                            android:text="@string/math_p1_sub"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="11sp" />

                        <LinearLayout
                            android:layout_width="match_parent"
                            android:layout_height="38dp"
                            android:layout_marginTop="10dp"
                            android:orientation="horizontal">

                            <Button
                                android:id="@+id/btn_read_math_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الكتاب"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_index_math_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الفهرس"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_summary_math_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الملخص"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_quiz_math_p1"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="اختبار"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                        </LinearLayout>
                    </LinearLayout>

                    <!-- Math P2 -->
                    <LinearLayout
                        android:layout_width="match_parent"
                        android:layout_height="wrap_content"
                        android:layout_marginTop="10dp"
                        android:background="@drawable/surface_card"
                        android:padding="12dp"
                        android:orientation="vertical">

                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:text="@string/math_p2_title"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="15sp"
                            android:textStyle="bold" />
                        <TextView
                            android:layout_width="match_parent"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="2dp"
                            android:text="@string/math_p2_sub"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="11sp" />

                        <LinearLayout
                            android:layout_width="match_parent"
                            android:layout_height="38dp"
                            android:layout_marginTop="10dp"
                            android:orientation="horizontal">

                            <Button
                                android:id="@+id/btn_read_math_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الكتاب"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_index_math_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الفهرس"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_summary_math_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="الملخص"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                            <View android:layout_width="6dp" android:layout_height="match_parent" />
                            <Button
                                android:id="@+id/btn_quiz_math_p2"
                                android:layout_width="0dp"
                                android:layout_height="match_parent"
                                android:layout_weight="1"
                                android:background="@drawable/chip_feature_pill"
                                android:text="اختبار"
                                android:textColor="?attr/thakerPrimary"
                                android:textSize="11sp" />
                        </LinearLayout>
                    </LinearLayout>
                </LinearLayout>

                <!-- About App Button -->
                <Button
                    android:id="@+id/btn_about"
                    android:layout_width="wrap_content"
                    android:layout_height="34dp"
                    android:layout_gravity="center_horizontal"
                    android:layout_marginTop="20dp"
                    android:minHeight="0dp"
                    android:minWidth="0dp"
                    android:background="@drawable/chip_neutral"
                    android:text="@string/about_app"
                    android:textColor="?attr/thakerTextSecondary"
                    android:textSize="10sp"
                    android:paddingStart="14dp"
                    android:paddingEnd="14dp" />
            </LinearLayout>
        </ScrollView>
    </LinearLayout>

    <!-- Bottom Navigation Dock Bar (Matches Prototype Exactly) -->
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="72dp"
        android:layout_gravity="bottom"
        android:layout_marginStart="14dp"
        android:layout_marginEnd="14dp"
        android:layout_marginBottom="12dp"
        android:orientation="horizontal"
        android:background="@drawable/bottom_nav_dock"
        android:elevation="12dp"
        android:gravity="center_vertical"
        android:paddingStart="6dp"
        android:paddingEnd="6dp">

        <!-- 1. موادي -->
        <Button
            android:id="@+id/nav_subjects"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:minHeight="0dp"
            android:minWidth="0dp"
            android:background="@android:color/transparent"
            android:text="@string/nav_subjects"
            android:textColor="?attr/thakerTextSecondary"
            android:textSize="11sp"
            android:textStyle="bold"
            android:drawableTop="@drawable/ic_graduation_cap"
            android:drawablePadding="2dp"
            android:paddingTop="10dp"
            android:paddingBottom="4dp" />

        <!-- 2. المكتبة -->
        <Button
            android:id="@+id/nav_library"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:minHeight="0dp"
            android:minWidth="0dp"
            android:background="@android:color/transparent"
            android:text="@string/nav_library"
            android:textColor="?attr/thakerTextSecondary"
            android:textSize="11sp"
            android:textStyle="bold"
            android:drawableTop="@drawable/ic_download_box"
            android:drawablePadding="2dp"
            android:paddingTop="10dp"
            android:paddingBottom="4dp" />

        <!-- 3. الرئيسية (Elevated FAB Center) -->
        <FrameLayout
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1.2">

            <View
                android:layout_width="56dp"
                android:layout_height="56dp"
                android:layout_gravity="center_horizontal|top"
                android:layout_marginTop="2dp"
                android:background="@drawable/nav_fab_glow" />

            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="match_parent"
                android:orientation="vertical"
                android:gravity="center_horizontal">

                <Button
                    android:id="@+id/nav_home"
                    android:layout_width="48dp"
                    android:layout_height="48dp"
                    android:background="@drawable/nav_fab_home"
                    android:drawableTop="@drawable/ic_home_white"
                    android:gravity="center"
                    android:paddingTop="12dp"
                    android:elevation="4dp" />

                <TextView
                    android:id="@+id/tv_nav_home"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="1dp"
                    android:text="@string/nav_home"
                    android:textColor="?attr/thakerPrimary"
                    android:textSize="11sp"
                    android:textStyle="bold" />
            </LinearLayout>
        </FrameLayout>

        <!-- 4. المفضلة -->
        <Button
            android:id="@+id/nav_favorites"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:minHeight="0dp"
            android:minWidth="0dp"
            android:background="@android:color/transparent"
            android:text="@string/nav_favorites"
            android:textColor="?attr/thakerTextSecondary"
            android:textSize="11sp"
            android:textStyle="bold"
            android:drawableTop="@drawable/ic_bookmark"
            android:drawablePadding="2dp"
            android:paddingTop="10dp"
            android:paddingBottom="4dp" />

        <!-- 5. الإعدادات -->
        <Button
            android:id="@+id/nav_settings"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:minHeight="0dp"
            android:minWidth="0dp"
            android:background="@android:color/transparent"
            android:text="@string/nav_settings"
            android:textColor="?attr/thakerTextSecondary"
            android:textSize="11sp"
            android:textStyle="bold"
            android:drawableTop="@drawable/ic_settings_gear"
            android:drawablePadding="2dp"
            android:paddingTop="10dp"
            android:paddingBottom="4dp" />
    </LinearLayout>
</FrameLayout>""")'''

pattern_main_xml = re.compile(r'    # 5\. Layouts\s+# A\. activity_main\.xml.*?with open\(f"\{res_dir\}/layout/activity_main\.xml".*?\"\"\"\)', re.DOTALL)
text = pattern_main_xml.sub(activity_main_xml_new, text)

# 4. Update setNav in MainActivity.java to work smoothly with new bottom nav dock
new_set_nav = '''    private void setNav(int active) {
        TextView tvHome = findViewById(R.id.tv_nav_home);
        if (tvHome != null) {
            tvHome.setTextColor(active == 0 ? ThemeUtil.color(this, R.attr.thakerPrimary) : ThemeUtil.color(this, R.attr.thakerTextSecondary));
        }
        int[] otherIds = new int[]{R.id.nav_subjects, R.id.nav_library, R.id.nav_favorites, R.id.nav_settings};
        int[] otherIndices = new int[]{1, 2, 3, 4};
        for (int i = 0; i < otherIds.length; i++) {
            Button b = findViewById(otherIds[i]);
            if (b != null) {
                boolean isCurrent = (active == otherIndices[i]);
                b.setTextColor(isCurrent ? ThemeUtil.color(this, R.attr.thakerPrimary) : ThemeUtil.color(this, R.attr.thakerTextSecondary));
            }
        }
    }'''

pattern_set_nav = re.compile(r'    private void setNav\(int active\) \{.*?^\s*\}', re.MULTILINE | re.DOTALL)
text = pattern_set_nav.sub(new_set_nav, text)

with open(BUILD_APK_PATH, "w", encoding="utf-8") as f:
    f.write(text)

print("✓ Upgraded build_apk.py with exact prototype design elements!")
