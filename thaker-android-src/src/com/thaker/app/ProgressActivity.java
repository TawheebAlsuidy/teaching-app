package com.thaker.app;

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
