package com.thaker.app;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Switch;
import android.widget.CompoundButton;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends Activity {

    private static final String PREFS_NAME = "thaker_app_prefs";
    private static final String KEY_AUTO_LAUNCH = "auto_launch_lab";

    private SharedPreferences prefs;
    private LinearLayout containerHighSchool;
    private LinearLayout containerMiddleSchool;
    private Button tabHighSchool;
    private Button tabMiddleSchool;
    private TextView tvGradeLabel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);

        prefs = getSharedPreferences(PREFS_NAME, MODE_PRIVATE);
        boolean autoLaunch = prefs.getBoolean(KEY_AUTO_LAUNCH, false);

        if (autoLaunch && !getIntent().getBooleanExtra("no_auto_launch", false)) {
            Intent intent = new Intent(this, LabActivity.class);
            startActivity(intent);
        }

        setContentView(R.layout.activity_main);

        containerHighSchool = findViewById(R.id.container_high_school);
        containerMiddleSchool = findViewById(R.id.container_middle_school);
        tabHighSchool = findViewById(R.id.tab_high_school);
        tabMiddleSchool = findViewById(R.id.tab_middle_school);
        tvGradeLabel = findViewById(R.id.tv_grade_label);

        // Stage Switcher Tabs
        tabHighSchool.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                switchToHighSchool();
            }
        });

        tabMiddleSchool.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                switchToMiddleSchool();
            }
        });

        // Chem Lab 3D Launch
        findViewById(R.id.btn_open_chem_lab).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, LabActivity.class));
            }
        });

        // Next-Gen Intelligent Interactive Textbook Engine (Science P2)
        View btnInteractiveEngine = findViewById(R.id.btn_open_sci9_interactive_engine);
        if (btnInteractiveEngine != null) {
            btnInteractiveEngine.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    Intent labIntent = new Intent(MainActivity.this, LabActivity.class);
                    labIntent.putExtra("html_asset", "thaker-interactive-book.html");
                    startActivity(labIntent);
                }
            });
        }

        // 9th Grade 3D Science Book & Laboratory
        findViewById(R.id.btn_open_sci9_3d_book).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent labIntent = new Intent(MainActivity.this, LabActivity.class);
                labIntent.putExtra("html_asset", "science-9th-book.html");
                startActivity(labIntent);
            }
        });

        // 9th Grade 3D Math Book & Laboratory
        findViewById(R.id.btn_open_math9_3d_book).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent labIntent = new Intent(MainActivity.this, LabActivity.class);
                labIntent.putExtra("html_asset", "math-9th-book.html");
                startActivity(labIntent);
            }
        });

        // 9th Grade Interactive Science Lab (opens complete 3D Science Book & Lab)
        findViewById(R.id.btn_open_sci9_lab).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent labIntent = new Intent(MainActivity.this, LabActivity.class);
                labIntent.putExtra("html_asset", "science-9th-book.html");
                startActivity(labIntent);
            }
        });

        // Auto launch checkbox
        Switch cb = findViewById(R.id.cb_auto_launch);
        cb.setChecked(autoLaunch);
        cb.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                prefs.edit().putBoolean(KEY_AUTO_LAUNCH, isChecked).apply();
            }
        });

        // About Button
        findViewById(R.id.btn_about).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showAboutDialog();
            }
        });

        setupMiddleSchoolButtons();

        findViewById(R.id.btn_notifications).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showSimpleDialog("الإشعارات", "لا توجد إشعارات جديدة.");
            }
        });
        findViewById(R.id.btn_profile).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showSimpleDialog("الملف الشخصي", "تطبيق ذاكر يعمل بالكامل دون اتصال بالإنترنت.");
            }
        });
        findViewById(R.id.btn_theme).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                ThemeUtil.toggle(MainActivity.this);
            }
        });
        findViewById(R.id.nav_home).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setNav(0);
            }
        });
        findViewById(R.id.nav_subjects).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setNav(1);
                switchToMiddleSchool();
            }
        });
        findViewById(R.id.nav_library).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setNav(2);
                showLibraryDialog();
            }
        });
        findViewById(R.id.nav_favorites).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setNav(3);
                showSimpleDialog("المفضلة", getString(R.string.favorites_empty));
            }
        });
        findViewById(R.id.nav_settings).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setNav(4);
                showThemeDialog();
            }
        });

        setNav(0);
        int stage = prefs.getInt(KEY_STAGE, 0);
        if (stage == 1) {
            switchToMiddleSchool();
        }
    }

    private static final String KEY_STAGE = "stage";

    private void setNav(int active) {
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
    }

    private void showSimpleDialog(String title, String message) {
        new AlertDialog.Builder(this).setTitle(title).setMessage(message).setPositiveButton("حسناً", null).show();
    }

    private void showThemeDialog() {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle(R.string.theme_toggle);
        builder.setItems(new CharSequence[]{getString(R.string.theme_light), getString(R.string.theme_dark)}, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                ThemeUtil.setDark(MainActivity.this, which == 1);
            }
        });
        builder.show();
    }

    private void showLibraryDialog() {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle(R.string.library_title);
        builder.setItems(new CharSequence[]{
                getString(R.string.chem_card_title),
                getString(R.string.book_science_3d),
                getString(R.string.book_math_3d),
                getString(R.string.science_lab)
        }, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                String asset = null;
                if (which == 1 || which == 3) {
                    asset = "science-9th-book.html";
                } else if (which == 2) {
                    asset = "math-9th-book.html";
                }
                Intent intent = new Intent(MainActivity.this, LabActivity.class);
                if (asset != null) {
                    intent.putExtra("html_asset", asset);
                }
                startActivity(intent);
            }
        });
        builder.show();
    }

    private void switchToHighSchool() {
        tabHighSchool.setBackgroundResource(R.drawable.tab_active);
        tabHighSchool.setTextColor(0xFFFFFFFF);
        tabMiddleSchool.setBackgroundResource(R.drawable.tab_inactive);
        tabMiddleSchool.setTextColor(ThemeUtil.color(this, R.attr.thakerTextSecondary));
        tvGradeLabel.setText(R.string.grade_12_title);
        containerHighSchool.setVisibility(View.VISIBLE);
        containerMiddleSchool.setVisibility(View.GONE);
        prefs.edit().putInt(KEY_STAGE, 0).apply();
    }

    private void switchToMiddleSchool() {
        tabMiddleSchool.setBackgroundResource(R.drawable.tab_active);
        tabMiddleSchool.setTextColor(0xFFFFFFFF);
        tabHighSchool.setBackgroundResource(R.drawable.tab_inactive);
        tabHighSchool.setTextColor(ThemeUtil.color(this, R.attr.thakerTextSecondary));
        tvGradeLabel.setText(R.string.grade_9_title);
        containerHighSchool.setVisibility(View.GONE);
        containerMiddleSchool.setVisibility(View.VISIBLE);
        prefs.edit().putInt(KEY_STAGE, 1).apply();
    }

    private void setupMiddleSchoolButtons() {
        // Science Part 1
        findViewById(R.id.btn_read_sci_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openBook("sci_p1", 0);
            }
        });
        findViewById(R.id.btn_index_sci_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showUnitIndexDialog("sci_p1");
            }
        });
        findViewById(R.id.btn_summary_sci_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openSummary("sci_p1");
            }
        });
        findViewById(R.id.btn_quiz_sci_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openQuiz("sci_p1");
            }
        });

        // Science Part 2
        findViewById(R.id.btn_read_sci_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openBook("sci_p2", 0);
            }
        });
        findViewById(R.id.btn_index_sci_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showUnitIndexDialog("sci_p2");
            }
        });
        findViewById(R.id.btn_summary_sci_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openSummary("sci_p2");
            }
        });
        findViewById(R.id.btn_quiz_sci_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openQuiz("sci_p2");
            }
        });

        // Math Part 1
        findViewById(R.id.btn_read_math_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openBook("math_p1", 0);
            }
        });
        findViewById(R.id.btn_index_math_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showUnitIndexDialog("math_p1");
            }
        });
        findViewById(R.id.btn_summary_math_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openSummary("math_p1");
            }
        });
        findViewById(R.id.btn_quiz_math_p1).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openQuiz("math_p1");
            }
        });

        // Math Part 2
        findViewById(R.id.btn_read_math_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openBook("math_p2", 0);
            }
        });
        findViewById(R.id.btn_index_math_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showUnitIndexDialog("math_p2");
            }
        });
        findViewById(R.id.btn_summary_math_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openSummary("math_p2");
            }
        });
        findViewById(R.id.btn_quiz_math_p2).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openQuiz("math_p2");
            }
        });

        // Comprehensive Exam (all 9th subjects)
        findViewById(R.id.btn_exam_9th_all).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openQuiz("all_9th");
            }
        });
    }

    private void openBook(String bookKey, int startPage) {
        Intent intent = new Intent(this, BookViewerActivity.class);
        intent.putExtra("book_key", bookKey);
        intent.putExtra("start_page", startPage);
        startActivity(intent);
    }

    private void openSummary(String tabKey) {
        Intent intent = new Intent(this, SummaryActivity.class);
        intent.putExtra("active_tab", tabKey);
        startActivity(intent);
    }

    private void openQuiz(String subjectKey) {
        Intent intent = new Intent(this, QuizActivity.class);
        intent.putExtra("quiz_subject", subjectKey);
        startActivity(intent);
    }

    private void showUnitIndexDialog(final String bookKey) {
        final String[] units;
        final int[] pages;
        String title;

        if ("sci_p1".equals(bookKey)) {
            title = "فهرس وحدات العلوم (الجزء الأول)";
            units = new String[]{
                "الوحدة 1: المحاليل وطرق التعبير عنها (ص 1)",
                "الوحدة 2: التفاعلات الكيميائية في حياتنا (ص 21)",
                "الوحدة 3: الصوت وانتقاله وتطبيقاته (ص 47)",
                "الوحدة 4: الضوء والرؤية والمرايا والعدسات (ص 67)",
                "الوحدة 5: الإخراج في الكائنات الحية (ص 99)",
                "الوحدة 6: التكاثر في الكائنات الحية (ص 125)",
                "الوحدة 7: أمراض الجهازين البولي والتناسلي (ص 151)"
            };
            pages = new int[]{1, 21, 47, 67, 99, 125, 151};
        } else if ("sci_p2".equals(bookKey)) {
            title = "فهرس وحدات العلوم (الجزء الثاني)";
            units = new String[]{
                "الوحدة 8: الكهرباء الساكنة والتيار وقانون أوم (ص 1)",
                "الوحدة 9: المغناطيسية والكهرومغناطيسية (ص 25)",
                "الوحدة 10: الطاقة ومصادرها وتحولاتها (ص 55)",
                "الوحدة 11: البيئة والتوازن البيئي والتلوث (ص 81)",
                "الوحدة 12: علوم الأرض والمعادن والطبقات (ص 105)",
                "الوحدة 13: الفضاء والكون والنظام الشمسي (ص 131)"
            };
            pages = new int[]{1, 25, 55, 81, 105, 131};
        } else if ("math_p1".equals(bookKey)) {
            title = "فهرس وحدات الرياضيات (الجزء الأول)";
            units = new String[]{
                "الوحدة 1: المجموعات والعلاقات والتكافؤ (ص 7)",
                "الوحدة 2: التطبيقات وأنواعها (ص 32)",
                "الوحدة 3: مجموعة الأعداد الحقيقية R (ص 40)",
                "الوحدة 4: تحليل المقادير الجبرية (ص 61)",
                "الوحدة 5: الكسور الجبرية والعمليات عليها (ص 94)",
                "تمارين عامة ومسائل وزارية شاملة (ص 160)"
            };
            pages = new int[]{7, 32, 40, 61, 94, 160};
        } else {
            title = "فهرس وحدات الرياضيات (الجزء الثاني)";
            units = new String[]{
                "الوحدة 5: الهندسة المستوية (الدائرة ونظرياتها) (ص 5)",
                "الوحدة 6: حساب المثلثات والزوايا الحادة (ص 45)",
                "الوحدة 7: التحويلات الهندسية والتكبير (ص 80)",
                "الوحدة 8: الإحصاء والاحتمالات (ص 111)"
            };
            pages = new int[]{5, 45, 80, 111};
        }

        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle(title);
        builder.setItems(units, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                openBook(bookKey, pages[which] - 1);
            }
        });
        builder.setNegativeButton("إلغاء", null);
        builder.show();
    }

    private void showAboutDialog() {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("عن ذاكر");
        builder.setMessage("كتاب ومعمل للصف التاسع والثالث الثانوي.\n\nتقرأ المنهج، وتجرّب التفاعلات بثلاثة أبعاد، وتتدرب على الأسئلة الوزارية. كل شيء يعمل دون إنترنت.\n\nتعلّم بوضوح.");
        builder.setPositiveButton("حسناً", null);
        builder.show();
    }
}
