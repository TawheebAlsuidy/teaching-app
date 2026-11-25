#!/usr/bin/env python3
"""
V2 Android XML Resources, Drawables, Layouts & Manifest for Thaker (ذاكر)
Faithful to mockups 01-splash through 11-progress in /mnt/sdcard/تطبيق ذاكر
Zero AndroidX dependency (100% pure android.widget / Material API 24+).
"""
import os


def _w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.lstrip("\n"))


def write_v2_resources(base_dir):
    res = f"{base_dir}/res"

    # 1. strings.xml
    _w(f"{res}/values/strings.xml", """
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">ذاكر</string>
    <string name="app_subtitle">افهم · جرّب · أتقن</string>
    <string name="nav_subjects">موادي</string>
    <string name="nav_library">المكتبة</string>
    <string name="nav_home">الرئيسية</string>
    <string name="nav_bookmarks">المفضلة</string>
    <string name="nav_settings">الإعدادات</string>
</resources>
""")

    # 2. attrs.xml (preserved attribute contract for ThemeUtil + BookViewerActivity)
    _w(f"{res}/values/attrs.xml", """
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <attr name="thakerBg" format="color" />
    <attr name="thakerSurface" format="color" />
    <attr name="thakerSurfaceAlt" format="color" />
    <attr name="thakerPrimary" format="color" />
    <attr name="thakerPrimaryLight" format="color" />
    <attr name="thakerTextPrimary" format="color" />
    <attr name="thakerTextSecondary" format="color" />
    <attr name="thakerStroke" format="color" />
    <attr name="thakerHeaderBg" format="color" />
</resources>
""")

    # 3. colors.xml
    _w(f"{res}/values/colors.xml", """
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="emerald_deep">#064E3B</color>
    <color name="emerald_mid">#047857</color>
    <color name="emerald_action">#059669</color>
    <color name="mint_canvas">#F2F7F4</color>
    <color name="mint_pill_bg">#D1FAE5</color>
    <color name="mint_pill_text">#065F46</color>
    <color name="gold_pill_bg">#FEF3C7</color>
    <color name="gold_pill_text">#92400E</color>
    <color name="amber_accent">#F59E0B</color>
    <color name="card_white">#FFFFFF</color>
    <color name="card_cream">#FFFBEB</color>
    <color name="stroke_soft">#DCE8E0</color>
    <color name="text_dark">#0F291E</color>
    <color name="text_muted">#5A7267</color>

    <color name="dark_canvas">#0A1410</color>
    <color name="dark_card">#11221B</color>
    <color name="dark_card_alt">#162C23</color>
    <color name="dark_stroke">#244537</color>
    <color name="dark_text">#ECFAF2</color>
    <color name="dark_text_muted">#9BC4B0</color>
</resources>
""")

    # 4. styles.xml
    _w(f"{res}/values/styles.xml", """
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="AppTheme" parent="android:Theme.Material.Light.NoActionBar">
        <item name="android:windowBackground">@color/mint_canvas</item>
        <item name="android:statusBarColor">@color/emerald_deep</item>
        <item name="android:navigationBarColor">@color/card_white</item>
        <item name="android:windowLightStatusBar">false</item>
        <item name="thakerBg">@color/mint_canvas</item>
        <item name="thakerSurface">@color/card_white</item>
        <item name="thakerSurfaceAlt">@color/mint_pill_bg</item>
        <item name="thakerPrimary">@color/emerald_action</item>
        <item name="thakerPrimaryLight">@color/emerald_mid</item>
        <item name="thakerTextPrimary">@color/text_dark</item>
        <item name="thakerTextSecondary">@color/text_muted</item>
        <item name="thakerStroke">@color/stroke_soft</item>
        <item name="thakerHeaderBg">@color/emerald_deep</item>
    </style>

    <style name="AppTheme.Splash" parent="AppTheme">
        <item name="android:windowBackground">@color/emerald_deep</item>
        <item name="android:statusBarColor">@color/emerald_deep</item>
        <item name="android:navigationBarColor">@color/emerald_mid</item>
    </style>

    <style name="AppTheme.Dark" parent="android:Theme.Material.NoActionBar">
        <item name="android:windowBackground">@color/dark_canvas</item>
        <item name="android:statusBarColor">@color/emerald_deep</item>
        <item name="android:navigationBarColor">@color/dark_card</item>
        <item name="thakerBg">@color/dark_canvas</item>
        <item name="thakerSurface">@color/dark_card</item>
        <item name="thakerSurfaceAlt">@color/dark_card_alt</item>
        <item name="thakerPrimary">#10B981</item>
        <item name="thakerPrimaryLight">#34D399</item>
        <item name="thakerTextPrimary">@color/dark_text</item>
        <item name="thakerTextSecondary">@color/dark_text_muted</item>
        <item name="thakerStroke">@color/dark_stroke</item>
        <item name="thakerHeaderBg">@color/emerald_deep</item>
    </style>
</resources>
""")

    # 5. Drawables
    drawables = {
        "splash_emerald_bg.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="#064E3B" android:centerColor="#047857" android:endColor="#065F46" android:angle="270"/>
</shape>""",
        "bg_emerald_header_curved.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <gradient android:startColor="#064E3B" android:endColor="#047857" android:angle="270"/>
    <corners android:bottomLeftRadius="28dp" android:bottomRightRadius="28dp"/>
</shape>""",
        "pill_white_translucent.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#28FFFFFF"/>
    <corners android:radius="14dp"/>
</shape>""",
        "pill_logo_mini.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#FFFFFF"/>
    <corners android:radius="10dp"/>
</shape>""",
        "card_white_rounded.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurface"/>
    <corners android:radius="20dp"/>
    <stroke android:width="1dp" android:color="?attr/thakerStroke"/>
</shape>""",
        "card_mint_tint.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurface"/>
    <corners android:radius="20dp"/>
    <stroke android:width="1.5dp" android:color="#A7F3D0"/>
</shape>""",
        "card_cream_tint.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#FFFBEB"/>
    <corners android:radius="20dp"/>
    <stroke android:width="1.5dp" android:color="#FDE68A"/>
</shape>""",
        "onboarding_card_selected.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurface"/>
    <corners android:radius="18dp"/>
    <stroke android:width="2dp" android:color="#059669"/>
</shape>""",
        "onboarding_card_normal.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurface"/>
    <corners android:radius="18dp"/>
    <stroke android:width="1dp" android:color="?attr/thakerStroke"/>
</shape>""",
        "pill_emerald_btn.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#059669"/>
    <corners android:radius="16dp"/>
</shape>""",
        "pill_emerald_outline.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="@android:color/transparent"/>
    <corners android:radius="14dp"/>
    <stroke android:width="1.5dp" android:color="#059669"/>
</shape>""",
        "pill_mint.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#D1FAE5"/>
    <corners android:radius="999dp"/>
</shape>""",
        "pill_gold.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#FEF3C7"/>
    <corners android:radius="999dp"/>
</shape>""",
        "pill_rose.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#FEE2E2"/>
    <corners android:radius="999dp"/>
</shape>""",
        "pill_gray.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#E2E8F0"/>
    <corners android:radius="999dp"/>
</shape>""",
        "pill_blue_soft.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#EFF6FF"/>
    <corners android:radius="14dp"/>
    <stroke android:width="1dp" android:color="#BFDBFE"/>
</shape>""",
        "bottom_dock_pill.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurface"/>
    <corners android:radius="28dp"/>
    <stroke android:width="1dp" android:color="?attr/thakerStroke"/>
</shape>""",
        "nav_center_circle.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android" android:shape="oval">
    <gradient android:startColor="#10B981" android:endColor="#047857" android:angle="270"/>
    <stroke android:width="3dp" android:color="#FFFFFF"/>
</shape>""",
        "progress_horizontal_emerald.xml": """
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:id="@android:id/background">
        <shape>
            <corners android:radius="99dp"/>
            <solid android:color="#DCE8E0"/>
        </shape>
    </item>
    <item android:id="@android:id/progress">
        <clip>
            <shape>
                <corners android:radius="99dp"/>
                <solid android:color="#059669"/>
            </shape>
        </clip>
    </item>
</layer-list>""",
        "quiz_opt_default.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="?attr/thakerSurface"/>
    <corners android:radius="16dp"/>
    <stroke android:width="1.5dp" android:color="?attr/thakerStroke"/>
</shape>""",
        "quiz_opt_right.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#ECFDF5"/>
    <corners android:radius="16dp"/>
    <stroke android:width="2dp" android:color="#059669"/>
</shape>""",
        "quiz_opt_wrong.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#FEF2F2"/>
    <corners android:radius="16dp"/>
    <stroke android:width="2dp" android:color="#EF4444"/>
</shape>""",
        "viewer_bar_pill.xml": """
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <solid android:color="#EB064E3B"/>
    <corners android:radius="18dp"/>
</shape>""",
    }
    for name, body in drawables.items():
        _w(f"{res}/drawable/{name}", body)

    # 6. Reusable Floating Bottom Dock (matching 03-home (1).png & 04-subject.png)
    _w(f"{res}/layout/layout_bottom_dock.xml", """
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="88dp"
    android:layout_gravity="bottom"
    android:clipChildren="false"
    android:clipToPadding="false"
    android:layoutDirection="rtl"
    android:paddingLeft="14dp"
    android:paddingRight="14dp"
    android:paddingBottom="10dp">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="64dp"
        android:layout_gravity="bottom"
        android:background="@drawable/bottom_dock_pill"
        android:elevation="10dp"
        android:gravity="center"
        android:orientation="horizontal"
        android:paddingLeft="6dp"
        android:paddingRight="6dp">

        <LinearLayout
            android:id="@+id/nav_tab_subjects"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:gravity="center"
            android:orientation="vertical">
            <TextView
                android:id="@+id/nav_ico_subjects"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="📚"
                android:textSize="17sp"/>
            <TextView
                android:id="@+id/nav_lbl_subjects"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="@string/nav_subjects"
                android:textColor="?attr/thakerTextSecondary"
                android:textSize="11sp"
                android:textStyle="bold"/>
        </LinearLayout>

        <LinearLayout
            android:id="@+id/nav_tab_library"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:gravity="center"
            android:orientation="vertical">
            <TextView
                android:id="@+id/nav_ico_library"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="📖"
                android:textSize="17sp"/>
            <TextView
                android:id="@+id/nav_lbl_library"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="@string/nav_library"
                android:textColor="?attr/thakerTextSecondary"
                android:textSize="11sp"
                android:textStyle="bold"/>
        </LinearLayout>

        <View
            android:layout_width="68dp"
            android:layout_height="1dp"/>

        <LinearLayout
            android:id="@+id/nav_tab_bookmarks"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:gravity="center"
            android:orientation="vertical">
            <TextView
                android:id="@+id/nav_ico_bookmarks"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="⭐"
                android:textSize="17sp"/>
            <TextView
                android:id="@+id/nav_lbl_bookmarks"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="@string/nav_bookmarks"
                android:textColor="?attr/thakerTextSecondary"
                android:textSize="11sp"
                android:textStyle="bold"/>
        </LinearLayout>

        <LinearLayout
            android:id="@+id/nav_tab_settings"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1"
            android:gravity="center"
            android:orientation="vertical">
            <TextView
                android:id="@+id/nav_ico_settings"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="⚙️"
                android:textSize="17sp"/>
            <TextView
                android:id="@+id/nav_lbl_settings"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="@string/nav_settings"
                android:textColor="?attr/thakerTextSecondary"
                android:textSize="11sp"
                android:textStyle="bold"/>
        </LinearLayout>
    </LinearLayout>

    <!-- Raised center emerald circle -->
    <LinearLayout
        android:id="@+id/nav_tab_home"
        android:layout_width="62dp"
        android:layout_height="62dp"
        android:layout_gravity="center_horizontal|top"
        android:layout_marginTop="4dp"
        android:background="@drawable/nav_center_circle"
        android:elevation="14dp"
        android:gravity="center"
        android:orientation="vertical">
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="🏠"
            android:textColor="#FFFFFF"
            android:textSize="19sp"/>
        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/nav_home"
            android:textColor="#FFFFFF"
            android:textSize="10sp"
            android:textStyle="bold"/>
    </LinearLayout>
</FrameLayout>
""")

    # 7. activity_splash.xml (01-splash.png)
    _w(f"{res}/layout/activity_splash.xml", """
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/splash_root"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@drawable/splash_emerald_bg"
    android:layoutDirection="rtl">

    <ImageView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:scaleType="centerCrop"
        android:src="@drawable/splash_rays"/>

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:gravity="center"
        android:orientation="vertical"
        android:padding="28dp">

        <ImageView
            android:layout_width="116dp"
            android:layout_height="116dp"
            android:src="@drawable/logo_splash_card"
            android:elevation="10dp"/>

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginTop="20dp"
            android:text="ذاكر"
            android:textColor="#FFFFFF"
            android:textSize="38sp"
            android:textStyle="bold"/>

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginTop="6dp"
            android:text="افهم · جرّب · أتقن"
            android:textColor="#FBBF24"
            android:textSize="17sp"
            android:textStyle="bold"/>

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginTop="14dp"
            android:gravity="center"
            android:text="منهجك اليمني.. تفاعلي ثلاثي الأبعاد"
            android:textColor="#E2F4EC"
            android:textSize="14sp"/>

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginTop="4dp"
            android:text="يعمل بالكامل بلا إنترنت"
            android:textColor="#A7F3D0"
            android:textSize="12sp"/>
    </LinearLayout>

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_gravity="bottom"
        android:gravity="center"
        android:orientation="vertical"
        android:paddingBottom="30dp">

        <LinearLayout
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:gravity="center"
            android:orientation="horizontal">
            <View android:layout_width="6dp" android:layout_height="6dp" android:background="#80FFFFFF" android:layout_margin="3dp"/>
            <View android:layout_width="6dp" android:layout_height="6dp" android:background="#80FFFFFF" android:layout_margin="3dp"/>
            <View android:layout_width="24dp" android:layout_height="6dp" android:background="#FBBF24" android:layout_margin="3dp"/>
        </LinearLayout>

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginTop="10dp"
            android:text="الإصدار 2.0"
            android:textColor="#A7F3D0"
            android:textSize="12sp"/>
    </LinearLayout>
</FrameLayout>
""")

    # 8. activity_onboarding.xml (02-onboarding.png)
    _w(f"{res}/layout/activity_onboarding.xml", """
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="?attr/thakerBg"
    android:layoutDirection="rtl"
    android:orientation="vertical"
    android:padding="18dp">

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center_vertical"
        android:orientation="horizontal">

        <TextView
            android:id="@+id/tv_onb_step_badge"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:background="@drawable/pill_mint"
            android:paddingLeft="14dp"
            android:paddingTop="6dp"
            android:paddingRight="14dp"
            android:paddingBottom="6dp"
            android:text="الخطوة 1 من 3"
            android:textColor="#065F46"
            android:textSize="12sp"
            android:textStyle="bold"/>

        <View android:layout_width="0dp" android:layout_height="1dp" android:layout_weight="1"/>

        <TextView
            android:id="@+id/btn_onb_skip"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:padding="8dp"
            android:text="تخطّي"
            android:textColor="?attr/thakerTextSecondary"
            android:textSize="14sp"
            android:textStyle="bold"/>
    </LinearLayout>

    <ProgressBar
        android:id="@+id/prog_onboarding"
        style="?android:attr/progressBarStyleHorizontal"
        android:layout_width="match_parent"
        android:layout_height="8dp"
        android:layout_marginTop="12dp"
        android:max="3"
        android:progress="1"
        android:progressDrawable="@drawable/progress_horizontal_emerald"/>

    <ScrollView
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"
        android:fillViewport="true"
        android:paddingTop="18dp">

        <FrameLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content">

            <!-- STEP 1: Stage, Grade, Exam Countdown -->
            <LinearLayout
                android:id="@+id/onb_step_1"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:orientation="vertical">

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="أهلاً بك في ذاكر 👋"
                    android:textColor="#059669"
                    android:textSize="14sp"
                    android:textStyle="bold"/>

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="4dp"
                    android:text="في أي مرحلة أنت؟"
                    android:textColor="?attr/thakerTextPrimary"
                    android:textSize="24sp"
                    android:textStyle="bold"/>

                <!-- Prep card -->
                <LinearLayout
                    android:id="@+id/card_stage_prep"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="16dp"
                    android:background="@drawable/onboarding_card_selected"
                    android:elevation="2dp"
                    android:gravity="center_vertical"
                    android:orientation="horizontal"
                    android:padding="14dp">

                    <ImageView
                        android:layout_width="54dp"
                        android:layout_height="54dp"
                        android:src="@drawable/ic_stage_prep"/>

                    <LinearLayout
                        android:layout_width="0dp"
                        android:layout_height="wrap_content"
                        android:layout_weight="1"
                        android:orientation="vertical"
                        android:paddingStart="12dp"
                        android:paddingEnd="12dp">
                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:text="المرحلة الإعدادية"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="17sp"
                            android:textStyle="bold"/>
                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="2dp"
                            android:text="الصفوف 7 – 9 · منهج الشهادة الأساسية"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="12sp"/>
                    </LinearLayout>

                    <TextView
                        android:id="@+id/chk_stage_prep"
                        android:layout_width="28dp"
                        android:layout_height="28dp"
                        android:background="@drawable/pill_mint"
                        android:gravity="center"
                        android:text="✓"
                        android:textColor="#059669"
                        android:textSize="15sp"
                        android:textStyle="bold"/>
                </LinearLayout>

                <!-- Secondary card -->
                <LinearLayout
                    android:id="@+id/card_stage_sec"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="12dp"
                    android:background="@drawable/onboarding_card_normal"
                    android:elevation="2dp"
                    android:gravity="center_vertical"
                    android:orientation="horizontal"
                    android:padding="14dp">

                    <ImageView
                        android:layout_width="54dp"
                        android:layout_height="54dp"
                        android:src="@drawable/ic_stage_sec"/>

                    <LinearLayout
                        android:layout_width="0dp"
                        android:layout_height="wrap_content"
                        android:layout_weight="1"
                        android:orientation="vertical"
                        android:paddingStart="12dp"
                        android:paddingEnd="12dp">
                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:text="المرحلة الثانوية"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="17sp"
                            android:textStyle="bold"/>
                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="2dp"
                            android:text="الصفوف 10 – 12 · القسم العلمي"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="12sp"/>
                    </LinearLayout>

                    <TextView
                        android:id="@+id/chk_stage_sec"
                        android:layout_width="28dp"
                        android:layout_height="28dp"
                        android:background="@drawable/pill_gray"
                        android:gravity="center"
                        android:text=""
                        android:textColor="#059669"
                        android:textSize="15sp"
                        android:textStyle="bold"/>
                </LinearLayout>

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="18dp"
                    android:text="الصف الدراسي"
                    android:textColor="?attr/thakerTextPrimary"
                    android:textSize="15sp"
                    android:textStyle="bold"/>

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="10dp"
                    android:orientation="horizontal">
                    <Button
                        android:id="@+id/btn_grade_opt1"
                        android:layout_width="0dp"
                        android:layout_height="44dp"
                        android:layout_weight="1"
                        android:layout_marginEnd="8dp"
                        android:background="@drawable/onboarding_card_normal"
                        android:text="السابع"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textSize="13sp"
                        android:textStyle="bold"/>
                    <Button
                        android:id="@+id/btn_grade_opt2"
                        android:layout_width="0dp"
                        android:layout_height="44dp"
                        android:layout_weight="1"
                        android:layout_marginEnd="8dp"
                        android:background="@drawable/onboarding_card_normal"
                        android:text="الثامن"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textSize="13sp"
                        android:textStyle="bold"/>
                    <Button
                        android:id="@+id/btn_grade_opt3"
                        android:layout_width="0dp"
                        android:layout_height="44dp"
                        android:layout_weight="1"
                        android:background="@drawable/pill_emerald_btn"
                        android:text="التاسع"
                        android:textColor="#FFFFFF"
                        android:textSize="13sp"
                        android:textStyle="bold"/>
                </LinearLayout>

                <!-- Exam countdown card -->
                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="18dp"
                    android:background="@drawable/card_white_rounded"
                    android:gravity="center_vertical"
                    android:orientation="horizontal"
                    android:padding="14dp">

                    <LinearLayout
                        android:layout_width="0dp"
                        android:layout_height="wrap_content"
                        android:layout_weight="1"
                        android:orientation="vertical">
                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:text="📅 موعد امتحانك"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="15sp"
                            android:textStyle="bold"/>
                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:text="اضغط لتعديل الأيام المتبقية"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="12sp"/>
                    </LinearLayout>

                    <TextView
                        android:id="@+id/btn_exam_days_pill"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:background="@drawable/pill_gold"
                        android:paddingLeft="14dp"
                        android:paddingTop="8dp"
                        android:paddingRight="14dp"
                        android:paddingBottom="8dp"
                        android:text="199 يوماً"
                        android:textColor="#92400E"
                        android:textSize="13sp"
                        android:textStyle="bold"/>
                </LinearLayout>
            </LinearLayout>

            <!-- STEP 2: Student Name & Weekly Target -->
            <LinearLayout
                android:id="@+id/onb_step_2"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:orientation="vertical"
                android:visibility="gone">

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="خصص تجربتك ✨"
                    android:textColor="#059669"
                    android:textSize="14sp"
                    android:textStyle="bold"/>

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="4dp"
                    android:text="ما اسمك يا بطل؟"
                    android:textColor="?attr/thakerTextPrimary"
                    android:textSize="24sp"
                    android:textStyle="bold"/>

                <EditText
                    android:id="@+id/et_onb_name"
                    android:layout_width="match_parent"
                    android:layout_height="52dp"
                    android:layout_marginTop="16dp"
                    android:background="@drawable/card_white_rounded"
                    android:hint="اكتب اسمك هنا (مثلاً: أسماء)"
                    android:inputType="textPersonName"
                    android:paddingLeft="16dp"
                    android:paddingRight="16dp"
                    android:text="أسماء"
                    android:textColor="?attr/thakerTextPrimary"
                    android:textSize="16sp"/>

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="22dp"
                    android:text="هدفك الأسبوعي للمذاكرة"
                    android:textColor="?attr/thakerTextPrimary"
                    android:textSize="16sp"
                    android:textStyle="bold"/>

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="12dp"
                    android:orientation="horizontal">
                    <Button
                        android:id="@+id/btn_goal_3"
                        android:layout_width="0dp"
                        android:layout_height="48dp"
                        android:layout_weight="1"
                        android:layout_marginEnd="8dp"
                        android:background="@drawable/onboarding_card_normal"
                        android:text="3 أيام"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textStyle="bold"/>
                    <Button
                        android:id="@+id/btn_goal_5"
                        android:layout_width="0dp"
                        android:layout_height="48dp"
                        android:layout_weight="1"
                        android:layout_marginEnd="8dp"
                        android:background="@drawable/pill_emerald_btn"
                        android:text="5 أيام"
                        android:textColor="#FFFFFF"
                        android:textStyle="bold"/>
                    <Button
                        android:id="@+id/btn_goal_7"
                        android:layout_width="0dp"
                        android:layout_height="48dp"
                        android:layout_weight="1"
                        android:background="@drawable/onboarding_card_normal"
                        android:text="يومياً (7)"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textStyle="bold"/>
                </LinearLayout>
            </LinearLayout>

            <!-- STEP 3: Ready Summary -->
            <LinearLayout
                android:id="@+id/onb_step_3"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:orientation="vertical"
                android:visibility="gone">

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="كل شيء جاهز! 🚀"
                    android:textColor="#059669"
                    android:textSize="15sp"
                    android:textStyle="bold"/>

                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="4dp"
                    android:text="أهلاً بك في عالم ذاكر التفاعلي"
                    android:textColor="?attr/thakerTextPrimary"
                    android:textSize="22sp"
                    android:textStyle="bold"/>

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="16dp"
                    android:background="@drawable/card_white_rounded"
                    android:orientation="vertical"
                    android:padding="16dp">
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="📖 الكتب الرسمية والصفحات التفاعلية"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textSize="16sp"
                        android:textStyle="bold"/>
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:layout_marginTop="4dp"
                        android:text="شروح مبسطة على كل صفحة، مع فهرس ذكي ومفضلة بلا إنترنت."
                        android:textColor="?attr/thakerTextSecondary"
                        android:textSize="13sp"/>
                </LinearLayout>

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="12dp"
                    android:background="@drawable/card_white_rounded"
                    android:orientation="vertical"
                    android:padding="16dp">
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="🧪 مختبر وتجارب 3D + اختبارات وزارية"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textSize="16sp"
                        android:textStyle="bold"/>
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:layout_marginTop="4dp"
                        android:text="جرّب الأجهزة الكيميائية والفيزيائية بيدك، واختبر نفسك مع تصحيح فوري."
                        android:textColor="?attr/thakerTextSecondary"
                        android:textSize="13sp"/>
                </LinearLayout>
            </LinearLayout>
        </FrameLayout>
    </ScrollView>

    <Button
        android:id="@+id/btn_onb_next"
        android:layout_width="match_parent"
        android:layout_height="54dp"
        android:background="@drawable/pill_emerald_btn"
        android:elevation="4dp"
        android:text="التالي  ←"
        android:textColor="#FFFFFF"
        android:textSize="16sp"
        android:textStyle="bold"/>
</LinearLayout>
""")

    # 9. activity_main.xml (03-home (1).png + موادي + المكتبة + المفضلة + الإعدادات)
    _w(f"{res}/layout/activity_main.xml", """
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="?attr/thakerBg"
    android:layoutDirection="rtl">

    <!-- PAGE 1: HOME (exact match to 03-home (1).png) -->
    <ScrollView
        android:id="@+id/page_home"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:fillViewport="true"
        android:scrollbars="none">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:paddingBottom="102dp">

            <!-- Deep Emerald Curved Header -->
            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:background="@drawable/bg_emerald_header_curved"
                android:orientation="vertical"
                android:paddingLeft="18dp"
                android:paddingTop="16dp"
                android:paddingRight="18dp"
                android:paddingBottom="60dp">

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:gravity="center_vertical"
                    android:orientation="horizontal">

                    <ImageView
                        android:id="@+id/btn_home_avatar"
                        android:layout_width="42dp"
                        android:layout_height="42dp"
                        android:background="@drawable/pill_white_translucent"
                        android:padding="4dp"
                        android:src="@drawable/avatar_student"/>

                    <LinearLayout
                        android:layout_width="0dp"
                        android:layout_height="wrap_content"
                        android:layout_weight="1"
                        android:gravity="center"
                        android:orientation="horizontal">
                        <ImageView
                            android:layout_width="28dp"
                            android:layout_height="28dp"
                            android:src="@drawable/logo_splash_card"/>
                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:layout_marginStart="6dp"
                            android:text="ذاكر"
                            android:textColor="#FFFFFF"
                            android:textSize="18sp"
                            android:textStyle="bold"/>
                    </LinearLayout>

                    <TextView
                        android:id="@+id/btn_home_progress_bell"
                        android:layout_width="42dp"
                        android:layout_height="42dp"
                        android:background="@drawable/pill_white_translucent"
                        android:gravity="center"
                        android:text="🔔"
                        android:textSize="18sp"/>
                </LinearLayout>

                <TextView
                    android:id="@+id/tv_home_greeting"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="16dp"
                    android:text="مساء الخير يا أسماء"
                    android:textColor="#FFFFFF"
                    android:textSize="22sp"
                    android:textStyle="bold"/>

                <TextView
                    android:id="@+id/tv_home_countdown"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="4dp"
                    android:text="📅 باقي 199 يوماً على امتحان الشهادة الأساسية"
                    android:textColor="#A7F3D0"
                    android:textSize="13sp"/>
            </LinearLayout>

            <!-- Overlapping Resume Card ("تابع من حيث توقفت") -->
            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginLeft="16dp"
                android:layout_marginTop="-42dp"
                android:layout_marginRight="16dp"
                android:background="@drawable/card_white_rounded"
                android:elevation="6dp"
                android:orientation="vertical"
                android:padding="16dp">

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:orientation="horizontal">

                    <ImageView
                        android:layout_width="68dp"
                        android:layout_height="84dp"
                        android:src="@drawable/mini_book_preview"/>

                    <LinearLayout
                        android:layout_width="0dp"
                        android:layout_height="wrap_content"
                        android:layout_weight="1"
                        android:orientation="vertical"
                        android:paddingStart="14dp">

                        <TextView
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:background="@drawable/pill_mint"
                            android:paddingLeft="10dp"
                            android:paddingTop="3dp"
                            android:paddingRight="10dp"
                            android:paddingBottom="3dp"
                            android:text="تابع من حيث توقفت"
                            android:textColor="#065F46"
                            android:textSize="11sp"
                            android:textStyle="bold"/>

                        <TextView
                            android:id="@+id/tv_resume_title"
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="6dp"
                            android:text="العلوم - الجزء الثاني"
                            android:textColor="?attr/thakerTextPrimary"
                            android:textSize="16sp"
                            android:textStyle="bold"/>

                        <TextView
                            android:id="@+id/tv_resume_subtitle"
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="2dp"
                            android:text="الوحدة 9 · صفحة 8"
                            android:textColor="?attr/thakerTextSecondary"
                            android:textSize="12sp"/>

                        <ProgressBar
                            android:id="@+id/prog_resume_bar"
                            style="?android:attr/progressBarStyleHorizontal"
                            android:layout_width="match_parent"
                            android:layout_height="7dp"
                            android:layout_marginTop="8dp"
                            android:max="100"
                            android:progress="38"
                            android:progressDrawable="@drawable/progress_horizontal_emerald"/>

                        <TextView
                            android:id="@+id/tv_resume_pct"
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="3dp"
                            android:text="38% من الجزء"
                            android:textColor="#059669"
                            android:textSize="11sp"
                            android:textStyle="bold"/>
                    </LinearLayout>
                </LinearLayout>

                <Button
                    android:id="@+id/btn_resume_reading"
                    android:layout_width="match_parent"
                    android:layout_height="46dp"
                    android:layout_marginTop="12dp"
                    android:background="@drawable/pill_emerald_btn"
                    android:text="تابع القراءة  ←"
                    android:textColor="#FFFFFF"
                    android:textSize="14sp"
                    android:textStyle="bold"/>
            </LinearLayout>

            <!-- Daily Mission Section ("مهمة اليوم" + Streak Pill) -->
            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginLeft="16dp"
                android:layout_marginTop="20dp"
                android:layout_marginRight="16dp"
                android:gravity="center_vertical"
                android:orientation="horizontal">

                <TextView
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_weight="1"
                    android:text="مهمة اليوم"
                    android:textColor="?attr/thakerTextPrimary"
                    android:textSize="17sp"
                    android:textStyle="bold"/>

                <TextView
                    android:id="@+id/btn_home_streak_pill"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:background="@drawable/pill_gold"
                    android:paddingLeft="12dp"
                    android:paddingTop="5dp"
                    android:paddingRight="12dp"
                    android:paddingBottom="5dp"
                    android:text="🔥 4 من 5 أيام"
                    android:textColor="#92400E"
                    android:textSize="12sp"
                    android:textStyle="bold"/>
            </LinearLayout>

            <!-- Daily Task 1 -->
            <LinearLayout
                android:id="@+id/card_task_1"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginLeft="16dp"
                android:layout_marginTop="10dp"
                android:layout_marginRight="16dp"
                android:background="@drawable/card_white_rounded"
                android:elevation="2dp"
                android:gravity="center_vertical"
                android:orientation="horizontal"
                android:padding="13dp">
                <TextView
                    android:layout_width="36dp"
                    android:layout_height="36dp"
                    android:background="@drawable/pill_mint"
                    android:gravity="center"
                    android:text="📖"
                    android:textSize="17sp"/>
                <LinearLayout
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_weight="1"
                    android:orientation="vertical"
                    android:paddingStart="12dp">
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="اقرأ درس اليوم (10 صفحات)"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textSize="14sp"
                        android:textStyle="bold"/>
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="تصفح الكتاب التفاعلي وشاهد الشروحات"
                        android:textColor="?attr/thakerTextSecondary"
                        android:textSize="11sp"/>
                </LinearLayout>
                <TextView
                    android:id="@+id/chk_task_1"
                    android:layout_width="26dp"
                    android:layout_height="26dp"
                    android:background="@drawable/pill_mint"
                    android:gravity="center"
                    android:text="✓"
                    android:textColor="#059669"
                    android:textSize="14sp"
                    android:textStyle="bold"/>
            </LinearLayout>

            <!-- Daily Task 2 -->
            <LinearLayout
                android:id="@+id/card_task_2"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginLeft="16dp"
                android:layout_marginTop="8dp"
                android:layout_marginRight="16dp"
                android:background="@drawable/card_white_rounded"
                android:elevation="2dp"
                android:gravity="center_vertical"
                android:orientation="horizontal"
                android:padding="13dp">
                <TextView
                    android:layout_width="36dp"
                    android:layout_height="36dp"
                    android:background="@drawable/pill_gold"
                    android:gravity="center"
                    android:text="🎯"
                    android:textSize="17sp"/>
                <LinearLayout
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_weight="1"
                    android:orientation="vertical"
                    android:paddingStart="12dp">
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="أجب عن اختبار قصير (5 أسئلة)"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textSize="14sp"
                        android:textStyle="bold"/>
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="عزّز إتقانك واكسب شارة المثابر"
                        android:textColor="?attr/thakerTextSecondary"
                        android:textSize="11sp"/>
                </LinearLayout>
                <TextView
                    android:id="@+id/chk_task_2"
                    android:layout_width="26dp"
                    android:layout_height="26dp"
                    android:background="@drawable/pill_gray"
                    android:gravity="center"
                    android:text=""
                    android:textColor="#059669"
                    android:textSize="14sp"
                    android:textStyle="bold"/>
            </LinearLayout>

            <!-- My Subjects Header ("موادي" + "عرض الكل") -->
            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginLeft="16dp"
                android:layout_marginTop="20dp"
                android:layout_marginRight="16dp"
                android:gravity="center_vertical"
                android:orientation="horizontal">
                <TextView
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_weight="1"
                    android:text="موادي"
                    android:textColor="?attr/thakerTextPrimary"
                    android:textSize="17sp"
                    android:textStyle="bold"/>
                <TextView
                    android:id="@+id/btn_view_all_subjects"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="عرض الكل ←"
                    android:textColor="#059669"
                    android:textSize="13sp"
                    android:textStyle="bold"/>
            </LinearLayout>

            <!-- Dynamic 2-col Subjects Container (populated cleanly by MainActivity based on Stage) -->
            <LinearLayout
                android:id="@+id/home_subjects_container"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginLeft="16dp"
                android:layout_marginTop="10dp"
                android:layout_marginRight="16dp"
                android:orientation="vertical"/>

        </LinearLayout>
    </ScrollView>

    <!-- PAGE 2: SUBJECTS ALL ("موادي") -->
    <ScrollView
        android:id="@+id/page_subjects"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:visibility="gone"
        android:padding="16dp">
        <LinearLayout
            android:id="@+id/all_subjects_container"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:paddingBottom="102dp"/>
    </ScrollView>

    <!-- PAGE 3: LIBRARY & PROGRESS ("المكتبة") -->
    <ScrollView
        android:id="@+id/page_library"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:visibility="gone"
        android:padding="16dp">
        <LinearLayout
            android:id="@+id/library_container"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:paddingBottom="102dp"/>
    </ScrollView>

    <!-- PAGE 4: BOOKMARKS ("المفضلة") -->
    <ScrollView
        android:id="@+id/page_bookmarks"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:visibility="gone"
        android:padding="16dp">
        <LinearLayout
            android:id="@+id/bookmarks_container"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:paddingBottom="102dp"/>
    </ScrollView>

    <!-- PAGE 5: SETTINGS ("الإعدادات") -->
    <ScrollView
        android:id="@+id/page_settings"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:visibility="gone"
        android:padding="16dp">
        <LinearLayout
            android:id="@+id/settings_container"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:paddingBottom="102dp"/>
    </ScrollView>

    <include android:id="@+id/bottom_dock" layout="@layout/layout_bottom_dock"/>
</FrameLayout>
""")

    # 10. activity_subject.xml (04-subject.png)
    _w(f"{res}/layout/activity_subject.xml", """
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="?attr/thakerBg"
    android:layoutDirection="rtl">

    <ScrollView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:fillViewport="true"
        android:scrollbars="none">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:paddingBottom="102dp">

            <!-- Deep Emerald Curved Header -->
            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:background="@drawable/bg_emerald_header_curved"
                android:orientation="vertical"
                android:paddingLeft="18dp"
                android:paddingTop="14dp"
                android:paddingRight="18dp"
                android:paddingBottom="26dp">

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:gravity="center_vertical"
                    android:orientation="horizontal">
                    <TextView
                        android:id="@+id/btn_subj_back"
                        android:layout_width="40dp"
                        android:layout_height="40dp"
                        android:background="@drawable/pill_white_translucent"
                        android:gravity="center"
                        android:text="→"
                        android:textColor="#FFFFFF"
                        android:textSize="20sp"
                        android:textStyle="bold"/>
                    <View android:layout_width="0dp" android:layout_height="1dp" android:layout_weight="1"/>
                    <TextView
                        android:id="@+id/tv_subj_grade_pill"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:background="@drawable/pill_gold"
                        android:paddingLeft="12dp"
                        android:paddingTop="5dp"
                        android:paddingRight="12dp"
                        android:paddingBottom="5dp"
                        android:text="الصف التاسع"
                        android:textColor="#92400E"
                        android:textSize="12sp"
                        android:textStyle="bold"/>
                </LinearLayout>

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="16dp"
                    android:gravity="center_vertical"
                    android:orientation="horizontal">
                    <LinearLayout
                        android:layout_width="0dp"
                        android:layout_height="wrap_content"
                        android:layout_weight="1"
                        android:orientation="vertical">
                        <TextView
                            android:id="@+id/tv_subj_title"
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:text="العلوم"
                            android:textColor="#FFFFFF"
                            android:textSize="28sp"
                            android:textStyle="bold"/>
                        <TextView
                            android:id="@+id/tv_subj_meta"
                            android:layout_width="wrap_content"
                            android:layout_height="wrap_content"
                            android:layout_marginTop="4dp"
                            android:text="جزءان · 15 وحدة · كتب رسمية وتفاعلية"
                            android:textColor="#A7F3D0"
                            android:textSize="13sp"/>
                    </LinearLayout>
                    <ImageView
                        android:id="@+id/iv_subj_icon"
                        android:layout_width="64dp"
                        android:layout_height="64dp"
                        android:background="@drawable/pill_logo_mini"
                        android:padding="8dp"
                        android:src="@drawable/ic_subj_science"/>
                </LinearLayout>
            </LinearLayout>

            <!-- Part Cards Container (Part 1 & Part 2, each with RingProgressView) -->
            <LinearLayout
                android:id="@+id/subj_parts_container"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginLeft="16dp"
                android:layout_marginTop="16dp"
                android:layout_marginRight="16dp"
                android:orientation="vertical"/>

            <!-- Bottom 3 Quick Action Cards ("امتحان شامل / أخطائي / الملخصات") -->
            <LinearLayout
                android:id="@+id/card_subj_exam"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginLeft="16dp"
                android:layout_marginTop="10dp"
                android:layout_marginRight="16dp"
                android:background="@drawable/card_white_rounded"
                android:elevation="2dp"
                android:gravity="center_vertical"
                android:orientation="horizontal"
                android:padding="14dp">
                <TextView android:layout_width="38dp" android:layout_height="38dp" android:background="@drawable/pill_gold" android:gravity="center" android:text="🏆" android:textSize="18sp"/>
                <LinearLayout android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:orientation="vertical" android:paddingStart="12dp">
                    <TextView android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="امتحان شامل في المادة" android:textColor="?attr/thakerTextPrimary" android:textSize="15sp" android:textStyle="bold"/>
                    <TextView android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="أسئلة وزارية مع حل وشرح فوري" android:textColor="?attr/thakerTextSecondary" android:textSize="12sp"/>
                </LinearLayout>
                <TextView android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="←" android:textColor="#059669" android:textSize="18sp" android:textStyle="bold"/>
            </LinearLayout>

            <LinearLayout
                android:id="@+id/card_subj_mistakes"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginLeft="16dp"
                android:layout_marginTop="10dp"
                android:layout_marginRight="16dp"
                android:background="@drawable/card_white_rounded"
                android:elevation="2dp"
                android:gravity="center_vertical"
                android:orientation="horizontal"
                android:padding="14dp">
                <TextView android:layout_width="38dp" android:layout_height="38dp" android:background="@drawable/pill_rose" android:gravity="center" android:text="🔁" android:textSize="18sp"/>
                <LinearLayout android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:orientation="vertical" android:paddingStart="12dp">
                    <TextView android:id="@+id/tv_subj_mistakes_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="أخطائي · 0" android:textColor="?attr/thakerTextPrimary" android:textSize="15sp" android:textStyle="bold"/>
                    <TextView android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="راجع الأسئلة التي أخطأت فيها سابقاً" android:textColor="?attr/thakerTextSecondary" android:textSize="12sp"/>
                </LinearLayout>
                <TextView android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="←" android:textColor="#059669" android:textSize="18sp" android:textStyle="bold"/>
            </LinearLayout>

            <LinearLayout
                android:id="@+id/card_subj_summary"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginLeft="16dp"
                android:layout_marginTop="10dp"
                android:layout_marginRight="16dp"
                android:background="@drawable/card_white_rounded"
                android:elevation="2dp"
                android:gravity="center_vertical"
                android:orientation="horizontal"
                android:padding="14dp">
                <TextView android:layout_width="38dp" android:layout_height="38dp" android:background="@drawable/pill_mint" android:gravity="center" android:text="⭐" android:textSize="18sp"/>
                <LinearLayout android:layout_width="0dp" android:layout_height="wrap_content" android:layout_weight="1" android:orientation="vertical" android:paddingStart="12dp">
                    <TextView android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="الملخصات والقوانين المهمة" android:textColor="?attr/thakerTextPrimary" android:textSize="15sp" android:textStyle="bold"/>
                    <TextView android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="تعريفات وقواعد وأخطاء شائعة في كل وحدة" android:textColor="?attr/thakerTextSecondary" android:textSize="12sp"/>
                </LinearLayout>
                <TextView android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="←" android:textColor="#059669" android:textSize="18sp" android:textStyle="bold"/>
            </LinearLayout>

        </LinearLayout>
    </ScrollView>

    <include android:id="@+id/bottom_dock" layout="@layout/layout_bottom_dock"/>
</FrameLayout>
""")

    # 11. activity_progress.xml (11-progress.png)
    _w(f"{res}/layout/activity_progress.xml", """
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="?attr/thakerBg"
    android:layoutDirection="rtl">

    <ScrollView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:fillViewport="true">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:padding="16dp"
            android:paddingBottom="102dp">

            <!-- Header -->
            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:gravity="center_vertical"
                android:orientation="horizontal">
                <TextView
                    android:id="@+id/btn_prog_back"
                    android:layout_width="40dp"
                    android:layout_height="40dp"
                    android:background="@drawable/card_white_rounded"
                    android:gravity="center"
                    android:text="→"
                    android:textColor="?attr/thakerTextPrimary"
                    android:textSize="20sp"
                    android:textStyle="bold"/>
                <LinearLayout
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_weight="1"
                    android:orientation="vertical"
                    android:paddingStart="12dp">
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="تقدمي"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textSize="24sp"
                        android:textStyle="bold"/>
                    <TextView
                        android:id="@+id/tv_prog_student_sub"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="أسماء · الصف التاسع"
                        android:textColor="?attr/thakerTextSecondary"
                        android:textSize="13sp"/>
                </LinearLayout>
            </LinearLayout>

            <!-- Weekly Goal Card -->
            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="16dp"
                android:background="@drawable/card_white_rounded"
                android:elevation="3dp"
                android:gravity="center_vertical"
                android:orientation="horizontal"
                android:padding="16dp">
                <LinearLayout
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_weight="1"
                    android:orientation="vertical">
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:background="@drawable/pill_mint"
                        android:paddingLeft="10dp"
                        android:paddingTop="3dp"
                        android:paddingRight="10dp"
                        android:paddingBottom="3dp"
                        android:text="هدفك الأسبوعي"
                        android:textColor="#065F46"
                        android:textSize="11sp"
                        android:textStyle="bold"/>
                    <TextView
                        android:id="@+id/tv_weekly_goal_main"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:layout_marginTop="6dp"
                        android:text="ذاكرت 4 أيام من 5"
                        android:textColor="?attr/thakerTextPrimary"
                        android:textSize="18sp"
                        android:textStyle="bold"/>
                    <TextView
                        android:id="@+id/tv_weekly_goal_hint"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:layout_marginTop="2dp"
                        android:text="استمر! اقتربت من إكمال سلسلتك الأسبوعية"
                        android:textColor="?attr/thakerTextSecondary"
                        android:textSize="12sp"/>
                </LinearLayout>
                <FrameLayout
                    android:id="@+id/ring_weekly_host"
                    android:layout_width="76dp"
                    android:layout_height="76dp"/>
            </LinearLayout>

            <!-- Mastery Grid Title -->
            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_marginTop="20dp"
                android:text="خريطة الإتقان"
                android:textColor="?attr/thakerTextPrimary"
                android:textSize="17sp"
                android:textStyle="bold"/>

            <LinearLayout
                android:id="@+id/mastery_grid_container"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="10dp"
                android:orientation="vertical"/>

            <!-- Wrong Questions Review Reminder -->
            <LinearLayout
                android:id="@+id/card_prog_review_wrong"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="16dp"
                android:background="@drawable/card_cream_tint"
                android:elevation="2dp"
                android:gravity="center_vertical"
                android:orientation="horizontal"
                android:padding="14dp">
                <TextView
                    android:layout_width="38dp"
                    android:layout_height="38dp"
                    android:background="@drawable/pill_gold"
                    android:gravity="center"
                    android:text="🔁"
                    android:textSize="18sp"/>
                <LinearLayout
                    android:layout_width="0dp"
                    android:layout_height="wrap_content"
                    android:layout_weight="1"
                    android:orientation="vertical"
                    android:paddingStart="12dp">
                    <TextView
                        android:id="@+id/tv_prog_wrong_count"
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="0 أسئلة تحتاج مراجعة"
                        android:textColor="#92400E"
                        android:textSize="15sp"
                        android:textStyle="bold"/>
                    <TextView
                        android:layout_width="wrap_content"
                        android:layout_height="wrap_content"
                        android:text="اضغط لبدء جلسة مراجعة للأخطاء"
                        android:textColor="#B45309"
                        android:textSize="12sp"/>
                </LinearLayout>
                <TextView
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="راجع ←"
                    android:textColor="#92400E"
                    android:textSize="13sp"
                    android:textStyle="bold"/>
            </LinearLayout>

            <!-- Badges Row ("شاراتي") -->
            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_marginTop="20dp"
                android:text="شاراتي"
                android:textColor="?attr/thakerTextPrimary"
                android:textSize="17sp"
                android:textStyle="bold"/>

            <LinearLayout
                android:id="@+id/badges_row_container"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="10dp"
                android:orientation="horizontal"/>
        </LinearLayout>
    </ScrollView>

    <include android:id="@+id/bottom_dock" layout="@layout/layout_bottom_dock"/>
</FrameLayout>
""")

    # 12. activity_summary.xml (09-summary.png)
    _w(f"{res}/layout/activity_summary.xml", """
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="?attr/thakerBg"
    android:layoutDirection="rtl"
    android:orientation="vertical">

    <!-- Header -->
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center_vertical"
        android:orientation="horizontal"
        android:paddingLeft="16dp"
        android:paddingTop="14dp"
        android:paddingRight="16dp"
        android:paddingBottom="10dp">

        <TextView
            android:id="@+id/btn_summary_back"
            android:layout_width="40dp"
            android:layout_height="40dp"
            android:background="@drawable/card_white_rounded"
            android:gravity="center"
            android:text="→"
            android:textColor="?attr/thakerTextPrimary"
            android:textSize="20sp"
            android:textStyle="bold"/>

        <LinearLayout
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:orientation="vertical"
            android:paddingStart="12dp">
            <TextView
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="الملخص"
                android:textColor="?attr/thakerTextPrimary"
                android:textSize="22sp"
                android:textStyle="bold"/>
            <TextView
                android:id="@+id/tv_summary_title"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="العلوم · ملخص الوحدات"
                android:textColor="?attr/thakerTextSecondary"
                android:textSize="13sp"/>
        </LinearLayout>

        <TextView
            android:id="@+id/btn_summary_bookmark"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:background="@drawable/pill_gold"
            android:paddingLeft="14dp"
            android:paddingTop="7dp"
            android:paddingRight="14dp"
            android:paddingBottom="7dp"
            android:text="⭐ احفظ"
            android:textColor="#92400E"
            android:textSize="13sp"
            android:textStyle="bold"/>
    </LinearLayout>

    <!-- Unit Filter Pills -->
    <HorizontalScrollView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:scrollbars="none"
        android:paddingLeft="16dp"
        android:paddingRight="16dp"
        android:paddingBottom="6dp">
        <LinearLayout
            android:id="@+id/summary_unit_pills"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:orientation="horizontal"/>
    </HorizontalScrollView>

    <!-- Colored-Stripe Cards Container -->
    <ScrollView
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"
        android:paddingLeft="16dp"
        android:paddingRight="16dp">
        <LinearLayout
            android:id="@+id/summary_cards_container"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical"
            android:paddingTop="8dp"
            android:paddingBottom="16dp"/>
    </ScrollView>

    <!-- Bottom CTA -->
    <FrameLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:padding="14dp"
        android:background="?attr/thakerSurface">
        <Button
            android:id="@+id/btn_summary_quiz"
            android:layout_width="match_parent"
            android:layout_height="52dp"
            android:background="@drawable/pill_emerald_btn"
            android:text="اختبر نفسك في هذا الدرس  ←"
            android:textColor="#FFFFFF"
            android:textSize="15sp"
            android:textStyle="bold"/>
    </FrameLayout>
</LinearLayout>
""")

    # 13. activity_quiz.xml (10-quiz.png)
    _w(f"{res}/layout/activity_quiz.xml", """
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="?attr/thakerBg"
    android:layoutDirection="rtl"
    android:orientation="vertical">

    <!-- Top Quiz Bar -->
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:gravity="center_vertical"
        android:orientation="horizontal"
        android:paddingLeft="16dp"
        android:paddingTop="14dp"
        android:paddingRight="16dp"
        android:paddingBottom="10dp">

        <TextView
            android:id="@+id/tv_quiz_progress"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:background="@drawable/pill_mint"
            android:paddingLeft="12dp"
            android:paddingTop="6dp"
            android:paddingRight="12dp"
            android:paddingBottom="6dp"
            android:text="1 / 5"
            android:textColor="#065F46"
            android:textSize="13sp"
            android:textStyle="bold"/>

        <LinearLayout
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:gravity="center"
            android:orientation="vertical">
            <TextView
                android:id="@+id/tv_quiz_subject"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="اختبر نفسك · تدريب"
                android:textColor="?attr/thakerTextPrimary"
                android:textSize="15sp"
                android:textStyle="bold"/>
            <TextView
                android:id="@+id/tv_quiz_score_top"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="النقاط: 0"
                android:textColor="#059669"
                android:textSize="12sp"
                android:textStyle="bold"/>
        </LinearLayout>

        <TextView
            android:id="@+id/btn_quiz_back"
            android:layout_width="38dp"
            android:layout_height="38dp"
            android:background="@drawable/card_white_rounded"
            android:gravity="center"
            android:text="✕"
            android:textColor="?attr/thakerTextPrimary"
            android:textSize="17sp"
            android:textStyle="bold"/>
    </LinearLayout>

    <ProgressBar
        android:id="@+id/prog_quiz_bar"
        style="?android:attr/progressBarStyleHorizontal"
        android:layout_width="match_parent"
        android:layout_height="7dp"
        android:layout_marginLeft="16dp"
        android:layout_marginRight="16dp"
        android:max="100"
        android:progress="20"
        android:progressDrawable="@drawable/progress_horizontal_emerald"/>

    <ScrollView
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"
        android:padding="16dp">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="vertical">

            <!-- Question Card -->
            <LinearLayout
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:background="@drawable/card_white_rounded"
                android:elevation="3dp"
                android:orientation="vertical"
                android:padding="18dp">

                <TextView
                    android:id="@+id/tv_quiz_unit_badge"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:background="@drawable/pill_gold"
                    android:paddingLeft="10dp"
                    android:paddingTop="4dp"
                    android:paddingRight="10dp"
                    android:paddingBottom="4dp"
                    android:text="سهل · الوحدة 9"
                    android:textColor="#92400E"
                    android:textSize="11sp"
                    android:textStyle="bold"/>

                <TextView
                    android:id="@+id/tv_question_text"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="12dp"
                    android:lineSpacingExtra="4dp"
                    android:textColor="?attr/thakerTextPrimary"
                    android:textSize="18sp"
                    android:textStyle="bold"/>
            </LinearLayout>

            <!-- 4 Option Buttons -->
            <Button
                android:id="@+id/btn_opt_0"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="14dp"
                android:background="@drawable/quiz_opt_default"
                android:gravity="center_vertical|right"
                android:minHeight="54dp"
                android:padding="14dp"
                android:textColor="?attr/thakerTextPrimary"
                android:textSize="15sp"/>

            <Button
                android:id="@+id/btn_opt_1"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="10dp"
                android:background="@drawable/quiz_opt_default"
                android:gravity="center_vertical|right"
                android:minHeight="54dp"
                android:padding="14dp"
                android:textColor="?attr/thakerTextPrimary"
                android:textSize="15sp"/>

            <Button
                android:id="@+id/btn_opt_2"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="10dp"
                android:background="@drawable/quiz_opt_default"
                android:gravity="center_vertical|right"
                android:minHeight="54dp"
                android:padding="14dp"
                android:textColor="?attr/thakerTextPrimary"
                android:textSize="15sp"/>

            <Button
                android:id="@+id/btn_opt_3"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="10dp"
                android:background="@drawable/quiz_opt_default"
                android:gravity="center_vertical|right"
                android:minHeight="54dp"
                android:padding="14dp"
                android:textColor="?attr/thakerTextPrimary"
                android:textSize="15sp"/>

            <!-- Explanation + Review Page / Try Activity Card -->
            <LinearLayout
                android:id="@+id/card_explanation"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:layout_marginTop="16dp"
                android:background="@drawable/pill_blue_soft"
                android:orientation="vertical"
                android:padding="16dp"
                android:visibility="gone">

                <TextView
                    android:id="@+id/tv_explain_header"
                    android:layout_width="wrap_content"
                    android:layout_height="wrap_content"
                    android:text="لماذا؟ · الحل"
                    android:textColor="#065F46"
                    android:textSize="15sp"
                    android:textStyle="bold"/>

                <TextView
                    android:id="@+id/tv_explain_body"
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="6dp"
                    android:lineSpacingExtra="4dp"
                    android:textColor="#1E293B"
                    android:textSize="14sp"/>

                <LinearLayout
                    android:layout_width="match_parent"
                    android:layout_height="wrap_content"
                    android:layout_marginTop="12dp"
                    android:orientation="horizontal">
                    <Button
                        android:id="@+id/btn_quiz_review_page"
                        android:layout_width="0dp"
                        android:layout_height="40dp"
                        android:layout_weight="1"
                        android:layout_marginEnd="8dp"
                        android:background="@drawable/pill_emerald_outline"
                        android:text="📖 راجع الصفحة"
                        android:textColor="#059669"
                        android:textSize="12sp"
                        android:textStyle="bold"/>
                    <Button
                        android:id="@+id/btn_quiz_try_lab"
                        android:layout_width="0dp"
                        android:layout_height="40dp"
                        android:layout_weight="1"
                        android:background="@drawable/pill_gold"
                        android:text="🧪 جرّب النشاط"
                        android:textColor="#92400E"
                        android:textSize="12sp"
                        android:textStyle="bold"/>
                </LinearLayout>
            </LinearLayout>
        </LinearLayout>
    </ScrollView>

    <FrameLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:padding="14dp"
        android:background="?attr/thakerSurface">
        <Button
            android:id="@+id/btn_quiz_next"
            android:layout_width="match_parent"
            android:layout_height="52dp"
            android:background="@drawable/pill_emerald_btn"
            android:text="السؤال التالي  ←"
            android:textColor="#FFFFFF"
            android:textSize="15sp"
            android:textStyle="bold"
            android:visibility="gone"/>
    </FrameLayout>
</LinearLayout>
""")

    # 14. activity_book_viewer.xml (V2 styled PDF Viewer preserving all 13 BookViewerActivity IDs!)
    _w(f"{res}/layout/activity_book_viewer.xml", """
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#E6EFEA"
    android:layoutDirection="rtl">

    <ImageView
        android:id="@+id/pdf_image_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:scaleType="matrix"/>

    <ProgressBar
        android:id="@+id/pdf_progress"
        android:layout_width="48dp"
        android:layout_height="48dp"
        android:layout_gravity="center"
        android:visibility="gone"/>

    <!-- Top Emerald Floating Bar -->
    <LinearLayout
        android:id="@+id/top_toolbar"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_gravity="top"
        android:layout_margin="10dp"
        android:background="@drawable/viewer_bar_pill"
        android:elevation="8dp"
        android:gravity="center_vertical"
        android:orientation="horizontal"
        android:padding="8dp">

        <Button
            android:id="@+id/btn_back_viewer"
            android:layout_width="40dp"
            android:layout_height="40dp"
            android:background="@drawable/pill_white_translucent"
            android:text="→"
            android:textColor="#FFFFFF"
            android:textSize="18sp"
            android:textStyle="bold"/>

        <LinearLayout
            android:layout_width="0dp"
            android:layout_height="wrap_content"
            android:layout_weight="1"
            android:orientation="vertical"
            android:paddingStart="10dp"
            android:paddingEnd="8dp">
            <TextView
                android:id="@+id/tv_viewer_book_title"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:singleLine="true"
                android:text="الكتاب المدرسي"
                android:textColor="#FFFFFF"
                android:textSize="14sp"
                android:textStyle="bold"/>
            <TextView
                android:id="@+id/tv_viewer_unit_name"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:singleLine="true"
                android:text="الوحدة"
                android:textColor="#A7F3D0"
                android:textSize="11sp"/>
        </LinearLayout>

        <Button
            android:id="@+id/btn_open_unit_index"
            android:layout_width="wrap_content"
            android:layout_height="36dp"
            android:layout_marginEnd="6dp"
            android:background="@drawable/pill_gold"
            android:paddingLeft="12dp"
            android:paddingRight="12dp"
            android:text="الفهرس"
            android:textColor="#92400E"
            android:textSize="12sp"
            android:textStyle="bold"/>

        <Button
            android:id="@+id/btn_reset_zoom"
            android:layout_width="36dp"
            android:layout_height="36dp"
            android:background="@drawable/pill_white_translucent"
            android:text="⌖"
            android:textColor="#FFFFFF"
            android:textSize="16sp"/>
    </LinearLayout>

    <!-- Bottom Page Scrubber Pill -->
    <LinearLayout
        android:id="@+id/bottom_toolbar"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_gravity="bottom"
        android:layout_margin="12dp"
        android:background="@drawable/bottom_dock_pill"
        android:elevation="10dp"
        android:orientation="vertical"
        android:padding="10dp">

        <SeekBar
            android:id="@+id/page_seekbar"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"/>

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_marginTop="4dp"
            android:gravity="center_vertical"
            android:orientation="horizontal">
            <Button
                android:id="@+id/btn_prev_page"
                android:layout_width="wrap_content"
                android:layout_height="38dp"
                android:background="@drawable/pill_mint"
                android:paddingLeft="14dp"
                android:paddingRight="14dp"
                android:text="السابق"
                android:textColor="#065F46"
                android:textSize="12sp"
                android:textStyle="bold"/>
            <TextView
                android:id="@+id/tv_page_indicator"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:gravity="center"
                android:text="صفحة 1 من 1"
                android:textColor="?attr/thakerTextPrimary"
                android:textSize="13sp"
                android:textStyle="bold"/>
            <Button
                android:id="@+id/btn_next_page"
                android:layout_width="wrap_content"
                android:layout_height="38dp"
                android:background="@drawable/pill_emerald_btn"
                android:paddingLeft="14dp"
                android:paddingRight="14dp"
                android:text="التالي"
                android:textColor="#FFFFFF"
                android:textSize="12sp"
                android:textStyle="bold"/>
        </LinearLayout>
    </LinearLayout>
</FrameLayout>
""")

    # 15. activity_lab.xml (Full-screen WebView container)
    _w(f"{res}/layout/activity_lab.xml", """
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#F2F7F4">
    <WebView
        android:id="@+id/webview"
        android:layout_width="match_parent"
        android:layout_height="match_parent"/>
</FrameLayout>
""")

    # 16. AndroidManifest.xml (SplashActivity is LAUNCHER!)
    _w(f"{base_dir}/AndroidManifest.xml", """
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.thaker.app"
    android:versionCode="20"
    android:versionName="2.0">

    <uses-sdk android:minSdkVersion="24" android:targetSdkVersion="34" />

    <queries>
        <intent>
            <action android:name="android.intent.action.TTS_SERVICE" />
        </intent>
    </queries>

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:label="@string/app_name"
        android:supportsRtl="true"
        android:theme="@style/AppTheme"
        android:hardwareAccelerated="true">

        <activity
            android:name=".SplashActivity"
            android:exported="true"
            android:theme="@style/AppTheme.Splash"
            android:screenOrientation="portrait">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <activity android:name=".OnboardingActivity" android:exported="false" android:screenOrientation="portrait"/>
        <activity android:name=".MainActivity" android:exported="false" android:launchMode="singleTop" android:screenOrientation="portrait"/>
        <activity android:name=".SubjectActivity" android:exported="false" android:screenOrientation="portrait"/>
        <activity android:name=".ProgressActivity" android:exported="false" android:screenOrientation="portrait"/>
        <activity android:name=".BookViewerActivity" android:exported="false" android:configChanges="orientation|screenSize"/>
        <activity android:name=".QuizActivity" android:exported="false" android:screenOrientation="portrait"/>
        <activity android:name=".SummaryActivity" android:exported="false" android:screenOrientation="portrait"/>
        <activity android:name=".LabActivity" android:exported="false" android:configChanges="orientation|screenSize|keyboardHidden"/>

    </application>
</manifest>
""")
