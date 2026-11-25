package com.thaker.app;

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
