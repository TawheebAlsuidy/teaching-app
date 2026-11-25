#!/usr/bin/env python3
"""
Upgrades #activityModal in thaker-interactive-book.html to match the exact
5-step guided experiment architecture and dark-navy visual design in
/mnt/sdcard/تطبيق ذاكر/تصميم التجارب (screens 1..6).
"""
import os
import re

WORK_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(WORK_DIR, "thaker-interactive-book.html")
ANDROID_HTML_PATH = os.path.join(WORK_DIR, "thaker-android-src", "assets", "thaker-interactive-book.html")

NEW_ACTIVITY_CSS = r"""/* Layer 3D: Guided 5-Step Dark Lab Modal (/mnt/sdcard/تطبيق ذاكر/تصميم التجارب) */
#activityModal {
  display: none; position: fixed; inset: 0;
  background: radial-gradient(circle at 50% 22%, #13283E 0%, #091522 60%, #060E17 100%);
  z-index: 150; flex-direction: column; color: #F8FAFC; overflow: hidden;
}
#activityModal.open { display: flex; }
.act-shell {
  width: 100%; max-width: 580px; margin: 0 auto; height: 100%;
  display: flex; flex-direction: column; justify-content: space-between; overflow-y: auto;
}
.act-top-bar {
  display: flex; align-items: center; justify-content: space-between;
  padding: 14px 16px 6px; gap: 10px; flex-shrink: 0;
}
.act-sq-btn {
  width: 42px; height: 42px; border-radius: 13px;
  background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.09);
  color: #F8FAFC; font-size: 18px; cursor: pointer;
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
  transition: transform 0.15s, background 0.15s;
}
.act-sq-btn:active { transform: scale(0.94); background: rgba(255,255,255,0.14); }
.act-header-meta { flex: 1; text-align: center; min-width: 0; }
.act-title {
  font-size: 17px; font-weight: 800; color: #FFFFFF;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.act-sub { font-size: 12px; color: #94A3B8; margin-top: 2px; font-weight: 600; }
.act-seg-row {
  display: flex; align-items: center; gap: 6px; padding: 6px 16px 4px; flex-shrink: 0;
}
.act-seg-bars { flex: 1; display: flex; gap: 6px; }
.act-seg {
  flex: 1; height: 4.5px; border-radius: 99px; cursor: pointer;
  background: rgba(255, 255, 255, 0.14); transition: background 0.25s;
}
.act-seg.done { background: #10B981; }
.act-seg.active { background: #0EA5E9; }
.act-seg-count {
  font-size: 12px; font-weight: 700; color: #94A3B8; min-width: 28px; text-align: left;
  font-variant-numeric: tabular-nums;
}

/* Open Lab Bench Stage (no box clutter) */
.act-bench-stage {
  position: relative; flex: 1; min-height: 225px; width: 100%;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  padding: 8px 14px 18px; overflow: hidden;
}
.act-bench-horizon {
  position: absolute; left: 0; right: 0; bottom: 0; height: 34px;
  background: linear-gradient(180deg, rgba(255,255,255,0.035) 0%, rgba(6,14,23,0.45) 100%);
  border-top: 1px solid rgba(255,255,255,0.09); pointer-events: none;
}
.act-float-tag {
  background: rgba(12, 24, 38, 0.84); border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 999px; padding: 4px 11px; font-size: 11px; font-weight: 700; color: #E2E8F0;
  white-space: nowrap; box-shadow: 0 4px 12px rgba(0,0,0,0.28);
}
.act-prop-stack {
  position: absolute; right: 14px; top: 14px; z-index: 6;
  display: flex; flex-direction: column; gap: 7px; align-items: flex-start;
}
.act-prop-chip {
  background: rgba(15, 29, 46, 0.85); border: 1px solid rgba(255,255,255,0.16);
  color: #CBD5E1; border-radius: 999px; padding: 5px 12px;
  font-size: 11.5px; font-weight: 700; cursor: pointer; transition: all 0.2s;
  display: inline-flex; align-items: center; gap: 6px;
}
.act-prop-chip.checked {
  background: rgba(16, 185, 129, 0.14); border-color: #10B981; color: #ECFDF5;
}
.act-complete-badge {
  width: 72px; height: 72px; border-radius: 50%;
  background: linear-gradient(135deg, #10B981, #059669);
  box-shadow: 0 0 0 12px rgba(16, 185, 129, 0.16), 0 12px 26px rgba(5, 150, 105, 0.45);
  display: flex; align-items: center; justify-content: center;
  font-size: 34px; color: #FFFFFF; font-weight: 900; margin-bottom: 10px;
}

/* Rounded Dark Bottom Control Sheet */
.act-bottom-sheet {
  background: #0F1D2E; border-top: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 28px 28px 0 0; padding: 20px 18px 20px;
  display: flex; flex-direction: column; gap: 11px; flex-shrink: 0;
  box-shadow: 0 -10px 32px rgba(0, 0, 0, 0.38);
}
.act-step-h { font-size: 20px; font-weight: 800; color: #FFFFFF; margin: 0; line-height: 1.3; }
.act-step-p { font-size: 13.5px; color: #94A3B8; line-height: 1.65; margin: 0; }
.act-step-p b { color: #F8FAFC; }
.act-pills-wrap { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 2px; }
.act-choice-pill {
  background: rgba(255, 255, 255, 0.05); border: 1.5px solid rgba(255, 255, 255, 0.14);
  color: #E2E8F0; border-radius: 999px; padding: 8px 14px;
  font-size: 12.5px; font-weight: 700; cursor: pointer; transition: all 0.2s;
  font-family: inherit;
}
.act-choice-pill.selected {
  background: rgba(16, 185, 129, 0.16); border-color: #10B981; color: #FFFFFF;
}
.act-safety-line {
  font-size: 12px; font-weight: 700; color: #FBBF24;
  display: flex; align-items: center; gap: 6px; padding-top: 2px;
}
.act-eq-box {
  background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.11);
  border-radius: 16px; padding: 13px 14px; text-align: center;
  font-size: 15px; font-weight: 800; color: #FFFFFF; direction: ltr;
}
.act-dual-row { display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; }
.act-ghost-pill {
  flex: 1; min-width: 130px; background: rgba(255, 255, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.12); color: #F1F5F9;
  border-radius: 999px; padding: 10px 14px; font-size: 13px; font-weight: 700;
  cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 6px;
  font-family: inherit;
}
.act-primary-cta {
  width: 100%; height: 52px; border-radius: 999px; border: none;
  background: linear-gradient(135deg, #10B981 0%, #059669 100%);
  color: #FFFFFF; font-size: 15.5px; font-weight: 800; cursor: pointer;
  display: flex; align-items: center; justify-content: center; gap: 8px;
  box-shadow: 0 8px 22px rgba(5, 150, 105, 0.35); margin-top: 4px; font-family: inherit;
}
.act-primary-cta:active { transform: scale(0.98); }

/* Atomic / Molecular Step 4 Stage */
.act-micro-badge {
  background: rgba(14, 165, 233, 0.12); border: 1px solid rgba(56, 189, 248, 0.4);
  color: #BAE6FD; border-radius: 999px; padding: 6px 14px;
  font-size: 12px; font-weight: 700; margin-bottom: 12px;
}
.act-micro-cols {
  width: 100%; max-width: 440px; direction: ltr;
  display: flex; align-items: center; justify-content: space-between; gap: 8px;
}
.act-micro-side { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 10px; }
.act-micro-lbl { font-size: 12px; font-weight: 700; color: #94A3B8; }

/* More Menu Bottom Sheet (6-menu-more.png) */
.act-more-backdrop {
  display: none; position: fixed; inset: 0; background: rgba(3, 8, 15, 0.68);
  z-index: 180; align-items: flex-end; justify-content: center;
}
.act-more-backdrop.open { display: flex; }
.act-more-sheet {
  width: 100%; max-width: 580px; max-height: 78vh; overflow-y: auto;
  background: #0F1D2E; border-top: 1px solid rgba(255,255,255,0.1);
  border-radius: 28px 28px 0 0; padding: 10px 18px 24px;
  display: flex; flex-direction: column; gap: 4px; color: #F8FAFC;
}
.act-more-handle {
  width: 42px; height: 4px; border-radius: 99px; background: rgba(255,255,255,0.22);
  margin: 0 auto 10px;
}
.act-more-sec-title {
  font-size: 12.5px; font-weight: 700; color: #94A3B8; padding: 8px 4px 4px;
}
.act-more-item {
  width: 100%; background: transparent; border: none; border-bottom: 1px solid rgba(255,255,255,0.06);
  color: #F8FAFC; padding: 12px 4px; font-size: 15px; font-weight: 700; cursor: pointer;
  display: flex; align-items: center; justify-content: space-between; gap: 10px; text-align: right;
  font-family: inherit;
}
.act-more-item:last-child { border-bottom: none; }
.act-more-divider { height: 1px; background: rgba(255,255,255,0.1); margin: 6px 0; }

/* Shared lab animations kept cleanly */
.burner-flame {
  width: 26px; height: 48px;
  background: radial-gradient(ellipse at bottom, #7dd3fc 0%, #f59e0b 58%, transparent 82%);
  border-radius: 50% 50% 25% 25%; animation: flameFlicker 0.16s infinite alternate;
}
@keyframes flameFlicker { 0% { transform: scale(1); } 100% { transform: scale(1.07, 0.94); } }
.magnesium-glow {
  position: absolute; width: 64px; height: 64px; border-radius: 50%;
  background: radial-gradient(circle, #ffffff 32%, #e0f2fe 65%, transparent 85%);
  box-shadow: 0 0 60px 28px #ffffff, 0 0 110px 55px rgba(186,230,253,0.65);
}
"""

NEW_ACTIVITY_HTML = r"""<!-- Layer 3D: Guided 5-Step Lab Modal (/mnt/sdcard/تطبيق ذاكر/تصميم التجارب) -->
<div id="activityModal">
  <div class="act-shell">
    <div>
      <div class="act-top-bar">
        <button class="act-sq-btn" onclick="closeActivityModal()" title="إغلاق">✕</button>
        <div class="act-header-meta">
          <div class="act-title" id="actModalMainTitle">احتراق الماغنسيوم</div>
          <div class="act-sub" id="actModalSubTitle">أكسدة الفلزات · نشاط 1 من 3</div>
        </div>
        <button class="act-sq-btn" onclick="toggleActMoreMenu(true)" title="المزيد">···</button>
      </div>
      <div class="act-seg-row">
        <div class="act-seg-bars" id="actSegBars">
          <div class="act-seg active" onclick="jumpActivityStep(1)"></div>
          <div class="act-seg" onclick="jumpActivityStep(2)"></div>
          <div class="act-seg" onclick="jumpActivityStep(3)"></div>
          <div class="act-seg" onclick="jumpActivityStep(4)"></div>
          <div class="act-seg" onclick="jumpActivityStep(5)"></div>
        </div>
        <span class="act-seg-count" id="actStepCounterBadge">1/5</span>
      </div>
    </div>

    <div class="act-bench-stage" id="actStageBox">
      <div id="dynamicStageVisual" style="width:100%; height:100%; position:relative; display:flex; flex-direction:column; align-items:center; justify-content:center;"></div>
      <div class="act-bench-horizon"></div>
    </div>

    <div class="act-bottom-sheet" id="actBottomSheet"></div>
  </div>
</div>

<!-- More Menu Bottom Sheet (6-menu-more.png) -->
<div id="actMoreBackdrop" class="act-more-backdrop" onclick="if(event.target===this)toggleActMoreMenu(false)">
  <div class="act-more-sheet">
    <div class="act-more-handle"></div>
    <div class="act-more-sec-title">الأنشطة</div>
    <div id="actMoreActivitiesList"></div>
    <button class="act-more-item" id="btnToggleAllActsMenu" onclick="toggleShowAllActivitiesInMenu()" style="color:#38BDF8; font-size:13px;">
      <span>📚 عرض جميع أنشطة الكتاب (15)</span>
      <span>⌄</span>
    </button>
    <div class="act-more-divider"></div>
    <div class="act-more-sec-title">خيارات</div>
    <button class="act-more-item" onclick="toggleActMoreMenu(false); resetActivitySimulation();">
      <span>↺ إعادة النشاط</span><span style="color:#94A3B8;">›</span>
    </button>
    <button class="act-more-item" onclick="toggleActMoreMenu(false); showCurrentActivityHint();">
      <span>💡 تلميح</span><span style="color:#FBBF24;">›</span>
    </button>
    <button class="act-more-item" onclick="toggleActMoreMenu(false); showBeforeAfterCompareModal();">
      <span>⚖️ مقارنة قبل وبعد</span><span style="color:#34D399;">›</span>
    </button>
    <button class="act-more-item" onclick="jumpToActivityBookPage();">
      <span>📖 الانتقال إلى صفحة الكتاب</span><span style="color:#94A3B8;">›</span>
    </button>
  </div>
</div>
"""

NEW_ACTIVITY_JS = r"""// --------------------------------------------------------
// LAYER 3D: GUIDED 5-STEP INTERACTIVE LAB ENGINE (DESIGN V3)
// --------------------------------------------------------
const actState = {
  currentActId: 'act-magnesium-combustion',
  curStep: 1,
  totalSteps: 5,
  metal: 'mg',
  discoveredProps: [true, true, false],
  selectedPrediction: 1,
  selectedObs: [true, true, false],
  showAllMenuActs: false
};

const ACT_META = {
  'act-magnesium-combustion': {
    shortTitle: 'احتراق الماغنسيوم',
    unitGroup: 'u9_ox',
    unitSub: 'أكسدة الفلزات',
    icon: '⚗️',
    props: ['فلز صلب', 'رمادي فضي لامع', 'موصل للكهرباء'],
    step1H: 'افحص شريط الماغنسيوم',
    step1P: 'المس الشريط لتتعرف على خواصه الفيزيائية قبل التفاعل.',
    step1Btn: 'افحص الشريط',
    step2H: 'قرّب الشريط من اللهب',
    step2P: 'أمسكه بالملقط فوق اللهب. <b>ماذا تتوقع أن يحدث؟</b>',
    predictions: ['يذوب بهدوء', 'يشتعل بضوء ساطع', 'لا يحدث شيء'],
    step2Btn: 'قرّب الشريط من اللهب',
    step3H: 'الاحتراق يحدث الآن!',
    obs: ['ضوء أبيض ساطع', 'مسحوق أبيض', 'حرارة عالية'],
    step3Btn: 'فسّر ما حدث',
    step4H: 'الماغنسيوم + الأكسجين',
    step4P: 'اتحد الماغنسيوم بالأكسجين فتكوّن أكسيد الماغنسيوم، وتُسمى هذه العملية <b>أكسدة</b>.',
    step4Btn: 'تحقق من فهمك',
    step5P: 'تعلمت كيف يتأكسد الفلز عند اتحاده بالأكسجين.',
    micro: {
      badge: '🔬 مستوى الذرات (تكبير)',
      before: [{t:'atom',s:'Mg',c:'#94A3B8',tc:'#0F172A'}, {t:'atom',s:'Mg',c:'#94A3B8',tc:'#0F172A'}, {t:'plus'}, {t:'di',s:'O',c:'#38BDF8',tc:'#082F49'}],
      after:  [{t:'pair',a:'Mg',b:'O',ca:'#94A3B8',cb:'#38BDF8'}, {t:'pair',a:'Mg',b:'O',ca:'#94A3B8',cb:'#38BDF8'}]
    }
  },
  'act-sulfur-combustion': {
    shortTitle: 'احتراق الكبريت',
    unitGroup: 'u9_ox',
    unitSub: 'أكسدة اللافلزات',
    icon: '🔥',
    props: ['لا فلز أصفر هش', 'غير موصل للكهرباء', 'صلب لا يذوب بالماء'],
    step1H: 'افحص مسحوق الكبريت',
    step1P: 'تعرّف على خواص عنصر الكبريت اللافلزي قبل التسخين.',
    step1Btn: 'افحص الكبريت',
    step2H: 'سخّن الكبريت فوق اللهب',
    step2P: 'نضع الكبريت في ملعقة الاحتراق. <b>ماذا تتوقع عند اشتعاله؟</b>',
    predictions: ['يحمر دوار الشمس الأزرق', 'يزرق الورقة الحمراء', 'يتبخر دون تفاعل'],
    step2Btn: 'سخّن في اللهب',
    step3H: 'لهب أزرق وتصاعد الغاز!',
    obs: ['لهب أزرق خافت', 'غاز SO₂ خانق', 'احمرار دوار الشمس'],
    step3Btn: 'فسّر ما حدث',
    step4H: 'الكبريت + الأكسجين',
    step4P: 'اتحد الكبريت بالأكسجين مكوناً ثاني أكسيد الكبريت وهو أكسيد <b>حامضي</b>.',
    step4Btn: 'تحقق من فهمك',
    step5P: 'أكاسيد اللافلزات أكاسيد حامضية تحمّر ورقة دوار الشمس.',
    micro: {
      badge: '🔬 مستوى الذرات (تكبير)',
      before: [{t:'atom',s:'S',c:'#FACC15',tc:'#422006'}, {t:'plus'}, {t:'di',s:'O',c:'#38BDF8',tc:'#082F49'}],
      after:  [{t:'tri',a:'O',b:'S',c:'O',ca:'#38BDF8',cb:'#FACC15',cc:'#38BDF8'}]
    }
  },
  'act-rusting-conditions': {
    shortTitle: 'صدأ الحديد',
    unitGroup: 'u9_ox',
    unitSub: 'أكسدة الفلزات',
    icon: '🔩',
    props: ['حديد لامع صلب', 'موصل جيد', 'يتأثر بالرطوبة والهواء'],
    step1H: 'افحص المسامير قبل التجربة',
    step1P: 'المس المسامير النظيفة لتتأكد من خلوها من الصدأ قبل وضعها في الأنابيب.',
    step1Btn: 'افحص المسامير',
    step2H: 'جهّز الأنابيب الأربعة',
    step2P: 'ماء+هواء، ماء مغلي+زيت، هواء جاف، وماء مالح. <b>أين يظهر الصدأ؟</b>',
    predictions: ['بالماء والهواء معاً', 'بالهواء الجاف فقط', 'في الماء المغلي المعزول'],
    step2Btn: 'ابدأ المراقبة لأيام',
    step3H: 'ظهور الصدأ البني الهش!',
    obs: ['صدأ بالماء والهواء', 'صدأ أشد بالماء المالح', 'عدم صدأ 2 و 3'],
    step3Btn: 'فسّر ما حدث',
    step4H: 'الحديد + الأكسجين + الماء',
    step4P: 'يتطلب صدأ الحديد وجود <b>الماء والأكسجين معاً</b>، والأملاح تسرّع التآكل.',
    step4Btn: 'تحقق من فهمك',
    step5P: 'تعلمت شروط صدأ الحديد وطرق حمايته بالعزل والطلاء.',
    micro: {
      badge: '🔬 التفسير المجهري للصدأ',
      before: [{t:'atom',s:'Fe',c:'#94A3B8',tc:'#0F172A'}, {t:'plus'}, {t:'di',s:'O',c:'#38BDF8',tc:'#082F49'}, {t:'plus'}, {t:'atom',s:'H₂O',c:'#60A5FA',tc:'#082F49'}],
      after:  [{t:'pair',a:'Fe₂O₃',b:'H₂O',ca:'#C2410C',cb:'#60A5FA'}]
    }
  },
  'act-carbon-allotropy': {
    shortTitle: 'تآصل الكربون',
    unitGroup: 'u9_c',
    unitSub: 'الكربون وتآصله',
    icon: '💎',
    props: ['الماس: شفاف صلب', 'الجرافيت: رمادي ناعم', 'كلاهما ذرات كربون C'],
    step1H: 'افحص الماس والجرافيت',
    step1P: 'لاحظ الاختلاف الكبير في الشكل والصلابة رغم أنهما من عنصر واحد.',
    step1Btn: 'افحص العينتين',
    step2H: 'اختبر التوصيل الكهربائي',
    step2P: 'نوصل الجرافيت ثم الماس بدائرة مصباح. <b>أيهما يضيء المصباح؟</b>',
    predictions: ['الجرافيت يضيء المصباح', 'الماس يضيء المصباح', 'كلاهما عازل'],
    step2Btn: 'شغّل الدائرة',
    step3H: 'نتيجة اختبار الدائرة والصلابة',
    obs: ['إضاءة المصباح بالجرافيت', 'عزل كهربائي في الماس', 'الماس يخدش الزجاج'],
    step3Btn: 'فسّر السبب البلوري',
    step4H: 'الشبكة البلورية sp³ vs sp²',
    step4P: 'تُسمى هذه الظاهرة <b>التآصل</b> لاختلاف ترتيب ارتباط ذرات الكربون هندسياً.',
    step4Btn: 'تحقق من فهمك',
    step5P: 'فهمت لماذا يتفوق الماس في الصلابة والجرافيت في التوصيل الكهربائي.',
    micro: {
      badge: '🔬 مقارنة الشبكة الذرية',
      before: [{t:'atom',s:'sp³ 💎',c:'#38BDF8',tc:'#082F49'}],
      after:  [{t:'atom',s:'sp² ⬡',c:'#64748B',tc:'#F8FAFC'}]
    }
  },
  'act-co2-prep-procedure': {
    shortTitle: 'تحضير غاز CO₂',
    unitGroup: 'u9_c',
    unitSub: 'مركبات الكربون',
    icon: '🔬',
    props: ['رخام CaCO₃ صلب', 'حمض HCl مخفف', 'زجاجة وف ومخبار جمع'],
    step1H: 'افحص أدوات التحضير',
    step1P: 'تأكد من إحكام أنبوبة القمع الطويل فوق قطع الرخام البيضاء.',
    step1Btn: 'افحص الجهاز',
    step2H: 'اسكب حمض الهيدروكلوريك',
    step2P: 'نصب الحمض عبر القمع فوق كربونات الكالسيوم. <b>ماذا تتوقع؟</b>',
    predictions: ['فوران وتصاعد CO₂', 'لا يحدث تفاعل', 'تجمد الحمض'],
    step2Btn: 'اسكب الحمض الآن',
    step3H: 'فوران وتصاعد الغاز!',
    obs: ['فوران شديد وفقاعات', 'تجمع الغاز بالأسفل', 'إزاحة الهواء لأعلى'],
    step3Btn: 'فسّر التفاعل',
    step4H: 'كربونات الكالسيوم + حمض HCl',
    step4P: 'يتفكك الرخام وينطلق غاز <b>ثاني أكسيد الكربون</b> الأثقل من الهواء.',
    step4Btn: 'تحقق من فهمك',
    step5P: 'أتممت تحضير وجمع غاز CO₂ بإزاحة الهواء لأعلى.',
    micro: {
      badge: '🔬 مستوى الجزيئات',
      before: [{t:'atom',s:'CaCO₃',c:'#E2E8F0',tc:'#0F172A'}, {t:'plus'}, {t:'atom',s:'2HCl',c:'#34D399',tc:'#064E3B'}],
      after:  [{t:'atom',s:'CaCl₂',c:'#94A3B8',tc:'#0F172A'}, {t:'plus'}, {t:'tri',a:'O',b:'C',c:'O',ca:'#EF4444',cb:'#64748B',cc:'#EF4444'}]
    }
  },
  'act-co2-properties': {
    shortTitle: 'خواص غاز CO₂',
    unitGroup: 'u9_c',
    unitSub: 'مركبات الكربون',
    icon: '🕯️',
    props: ['غاز أثقل من الهواء', 'شمعة مشتعلة', 'ماء جير رائق Ca(OH)₂'],
    step1H: 'افحص المخبار والشمعة',
    step1P: 'لدينا مخبار مملوء بغاز CO₂ وأنبوبة ماء جير رائق وشمعة.',
    step1Btn: 'افحص الأدوات',
    step2H: 'اسكب الغاز على الشمعة وماء الجير',
    step2P: 'أمل المخبار فوق الشمعة ثم مرّر الغاز بماء الجير. <b>ماذا تتوقع؟</b>',
    predictions: ['تشتعل الشمعة أكثر', 'تنطفئ الشمعة ويتعكر الجير', 'لا يتأثر شيء'],
    step2Btn: 'نفّذ الاختبارين',
    step3H: 'انطفاء الشمعة وتعكر الجير!',
    obs: ['انطفاء فوري للشمعة', 'عكارة بيضاء بالجير', 'CO₂ أثقل من الهواء'],
    step3Btn: 'فسّر ما حدث',
    step4H: 'كربونات الكالسيوم المترسبة',
    step4P: 'تفاعل CO₂ مع هيدروكسيد الكالسيوم مكوّناً <b>راسباً أبيض</b> هو CaCO₃.',
    step4Btn: 'تحقق من فهمك',
    step5P: 'أثبتّ أن CO₂ لا يساعد على الاشتعال ويُكشف عنه بماء الجير.',
    micro: {
      badge: '🔬 تفاعل الكشف الكيميائي',
      before: [{t:'tri',a:'O',b:'C',c:'O',ca:'#EF4444',cb:'#64748B',cc:'#EF4444'}, {t:'plus'}, {t:'atom',s:'Ca(OH)₂',c:'#38BDF8',tc:'#082F49'}],
      after:  [{t:'atom',s:'CaCO₃↓',c:'#F8FAFC',tc:'#0F172A'}, {t:'plus'}, {t:'atom',s:'H₂O',c:'#60A5FA',tc:'#082F49'}]
    }
  },
  'act-petroleum-refining': {
    shortTitle: 'تكرير النفط الخام',
    unitGroup: 'u9_hydro',
    unitSub: 'الهيدروكربونات',
    icon: '🛢️',
    props: ['خليط سائل أسود', 'سلاسل كربونية مختلفة', 'تباين درجات الغليان'],
    step1H: 'افحص عينة النفط الخام',
    step1P: 'النفط الخام مزيج من مئات الهيدروكربونات تختلف في أطوال سلاسلها.',
    step1Btn: 'افحص العينة',
    step2H: 'تسخين النفط إلى برج التقطير',
    step2P: 'نضخ الأبخرة في برج التقطير المتدرج الحرارة. <b>كيف تنفصل؟</b>',
    predictions: ['حسب درجة الغليان والارتفاع', 'تتكثف جميعها بالقاع', 'تحترق داخل البرج'],
    step2Btn: 'شغّل برج التقطير',
    step3H: 'انفصال المشتقات في البرج!',
    obs: ['بنزين وغازات بالأعلى', 'كيروسين وديزل بالوسط', 'أسفلت ثقيل بالقاع'],
    step3Btn: 'فسّر آلية الفصل',
    step4H: 'التقطير التجزيئي',
    step4P: 'تتصاعد الجزيئات الأخف والأقل غلياناً للقمة بينما تتكثف الأثقل أسفلاً (<b>التقطير التجزيئي</b>).',
    step4Btn: 'تحقق من فهمك',
    step5P: 'فهمت كيف نحصل على الغاز والبنزين والديزل من النفط الخام.',
    micro: {
      badge: '🔬 حجم السلاسل الهيدروكربونية',
      before: [{t:'atom',s:'خليط C₁..C₄₀',c:'#334155',tc:'#F8FAFC'}],
      after:  [{t:'atom',s:'C₅–C₈ ⛽',c:'#38BDF8',tc:'#082F49'}, {t:'atom',s:'C₁₄+ 🛣️',c:'#F59E0B',tc:'#451A03'}]
    }
  },
  'act-chlorine-prep': {
    shortTitle: 'تحضير غاز الكلور',
    unitGroup: 'u10_hal',
    unitSub: 'الهالوجينات',
    icon: '🧫',
    props: ['MnO₂ أسود صلب', 'حمض HCl مركز', 'قنينة ماء وH₂SO₄ للتنقية'],
    step1H: 'افحص جهاز تحضير الكلور',
    step1P: 'تأكد من توصيل الدورق بزجاجة الماء ثم حمض الكبريتيك لجمع كلور نقي وجاف.',
    step1Btn: 'افحص الجهاز',
    step2H: 'سخّن الخليط بحذر',
    step2P: 'نبدأ تسخين MnO₂ مع HCl المركز. <b>ماذا تتوقع داخل المخبار؟</b>',
    predictions: ['غاز أصفر مخضر يقصر الألوان', 'غاز عديم اللون لا يؤثر', 'يتكون مسحوق أبيض'],
    step2Btn: 'ابدأ التسخين',
    step3H: 'تصاعد الكلور وزوال اللون!',
    obs: ['غاز أصفر مخضر Cl₂', 'تنقية بالماء وتجفيف بالحامض', 'ابيضاض الزهرة الرطبة'],
    step3Btn: 'فسّر آلية القصر',
    step4H: 'أكسدة HCl + قصر الألوان',
    step4P: 'تأكسد حمض الهيدروكلوريك ليطلق <b>غاز الكلور</b> الذي يكون حمض الهيبوكلوروز المبيّض.',
    step4Btn: 'تحقق من فهمك',
    step5P: 'أتممت تحضير الكلور النقي وفهمت آلية تبييض الألوان الرطبة.',
    micro: {
      badge: '🔬 مستوى الجزيئات',
      before: [{t:'atom',s:'MnO₂',c:'#64748B',tc:'#F8FAFC'}, {t:'plus'}, {t:'atom',s:'4HCl',c:'#34D399',tc:'#064E3B'}],
      after:  [{t:'atom',s:'MnCl₂',c:'#94A3B8',tc:'#0F172A'}, {t:'plus'}, {t:'di',s:'Cl',c:'#A3E635',tc:'#1A2E05'}]
    }
  },
  'act-elasticity-solids': {
    shortTitle: 'المرونة واللدونة',
    unitGroup: 'u11_prop',
    unitSub: 'خواص الأجسام',
    icon: '🌀',
    props: ['نابض فولاذي مرن', 'قطعة صلصال طرية', 'حالة سكون أصلية'],
    step1H: 'افحص النابض والصلصال',
    step1P: 'المس العيّنتين وقارن قوام كل منهما قبل التأثير عليهما بقوة.',
    step1Btn: 'افحص العينات',
    step2H: 'طبّق قوة شد وضغط',
    step2P: 'نشد النابض ونضغط الصلصال ثم نرفع اليد. <b>ماذا تتوقع؟</b>',
    predictions: ['يعود النابض ويبقى الصلصال', 'يعود كلاهما تماماً', 'ينكسر النابض'],
    step2Btn: 'طبّق القوة الآن',
    step3H: 'سلوك مختلف بعد زوال القوة!',
    obs: ['استطالة وعودة النابض', 'بقاء تشوّه الصلصال', 'وجود حد للمرونة'],
    step3Btn: 'فسّر الظاهرة',
    step4H: 'المرونة vs اللدونة (قانون هوك)',
    step4P: 'الأجسام <b>المرنة</b> تستعيد شكلها عند زوال القوة، أما <b>اللدنة</b> فتحتفظ بتشوهها.',
    step4Btn: 'تحقق من فهمك',
    step5P: 'ميّزت عملياً بين المرونة واللدونة وتعرفت على قانون هوك.',
    micro: {
      badge: '🔬 ترابط الجزيئات الداخلية',
      before: [{t:'atom',s:'شد + إرجاع',c:'#38BDF8',tc:'#082F49'}],
      after:  [{t:'atom',s:'انزلاق دائم',c:'#F59E0B',tc:'#451A03'}]
    }
  },
  'act-surface-tension': {
    shortTitle: 'التوتر السطحي للماء',
    unitGroup: 'u11_prop',
    unitSub: 'خواص الأجسام',
    icon: '💧',
    props: ['حوض ماء نقي ساكن', 'إبرة فولاذية جافة', 'سائل صابون'],
    step1H: 'افحص حوض الماء والإبرة',
    step1P: 'ضع الإبرة الفولاذية برفق وبشكل أفقي على سطح الماء الساكن.',
    step1Btn: 'ضع الإبرة برفق',
    step2H: 'أضف قطرة سائل الصابون',
    step2P: 'تطفو الإبرة الآن رغم كثافة الحديد! <b>ماذا يحدث عند إضافة الصابون؟</b>',
    predictions: ['ينكسر الغشاء وتغوص الإبرة', 'ترتفع الإبرة للأعلى', 'تلتصق بجدار الحوض'],
    step2Btn: 'أضف قطرة الصابون',
    step3H: 'تمزق الغشاء وغوص الإبرة!',
    obs: ['تكوّن غشاء مشدود بالماء', 'تشتت التوتر بالصابون', 'غوص الإبرة للقاع'],
    step3Btn: 'فسّر ما حدث',
    step4H: 'قوى التماسك السطحي والصابون',
    step4P: 'جزيئات السطح تنجذب للداخل كغشاء مشدود (<b>التوتر السطحي</b>) والصابون يضعفها.',
    step4Btn: 'تحقق من فهمك',
    step5P: 'فهمت سر مشي الحشرات فوق الماء ولماذا يزيل الصابون الدهون.',
    micro: {
      badge: '🔬 جزيئات السطح والصابون',
      before: [{t:'pair',a:'H₂O',b:'H₂O',ca:'#38BDF8',cb:'#38BDF8'}],
      after:  [{t:'atom',s:'كسر الروابط 🫧',c:'#F472B6',tc:'#500724'}]
    }
  },
  'act-viscosity-liquids': {
    shortTitle: 'لزوجة السوائل',
    unitGroup: 'u11_prop',
    unitSub: 'خواص الأجسام',
    icon: '🍯',
    props: ['مخبار ماء سريع', 'مخبار زيت متوسط', 'مخبار عسل كثيف'],
    step1H: 'افحص الأنابيب والكرات',
    step1P: 'ثلاث سوائل مختلفة الكثافة ومقاومة الجريان مع 3 كرات معدنية متماثلة.',
    step1Btn: 'جهّز الكرات',
    step2H: 'أسقط الكرات الثلاث معاً',
    step2P: 'سنسقط الكرات في نفس اللحظة. <b>أي كرة تصل القاع أولاً؟</b>',
    predictions: ['كرة الماء ثم الزيت ثم العسل', 'كرة العسل أولاً', 'تصل كلها في نفس الوقت'],
    step2Btn: 'أسقط الكرات الآن',
    step3H: 'تفاوت سرعة الهبوط!',
    obs: ['هبوط سريع في الماء', 'بطء شديد في العسل البارد', 'تسارع الهبوط بالتسخين'],
    step3Btn: 'فسّر أثر الحرارة',
    step4H: 'الاحتكاك الداخلي والحرارة',
    step4P: '<b>اللزوجة</b> هي مقاومة السائل للجريان وتقل كلما ارتفعت درجة الحرارة.',
    step4Btn: 'تحقق من فهمك',
    step5P: 'تعرفت على قياس اللزوجة وأهمية اختيار زيوت المحركات المناسبة.',
    micro: {
      badge: '🔬 احتكاك طبقات السائل',
      before: [{t:'atom',s:'عسل بارد 🐢',c:'#D97706',tc:'#FFFBEB'}],
      after:  [{t:'atom',s:'عسل دافئ ⚡',c:'#FBBF24',tc:'#451A03'}]
    }
  },
  'act-liquid-pressure-depth': {
    shortTitle: 'ضغط السوائل والعمق',
    unitGroup: 'u12_p',
    unitSub: 'الضغط والموائع',
    icon: '🌊',
    props: ['زجاجة طويلة بـ 3 ثقوب', 'ماء يملأ الإناء', 'اختلاف الارتفاع h'],
    step1H: 'افحص الثقوب الثلاثة',
    step1P: 'ثقب علوي قليل العمق، ثقب أوسط، وثقب سفلي قريب من القاعدة.',
    step1Btn: 'افحص الزجاجة',
    step2H: 'انزع الشريط اللاصق عن الثقوب',
    step2P: 'ملأنا الزجاجة بالماء. <b>أي ثقب سيندفع منه الماء لمسافة أبعد؟</b>',
    predictions: ['الثقب السفلي (الأعمق)', 'الثقب العلوي', 'جميعها بنفس المدى'],
    step2Btn: 'افتح الثقوب الآن',
    step3H: 'تدرج مدى الاندفاع مع العمق!',
    obs: ['اندفاع ضعيف في الأعلى', 'اندفاع متوسط في الوسط', 'أقوى مدى في الأسفل'],
    step3Btn: 'فسّر العلاقة الرياضية',
    step4H: 'قانون ضغط السائل P = ρ·g·h',
    step4P: 'يزداد ضغط السائل طردياً مع <b>العمق (h)</b> وكثافة السائل (ρ) لا مع شكل الإناء.',
    step4Btn: 'تحقق من فهمك',
    step5P: 'أدركت سر بناء قواعد السدود الخرسانية بشكل أكثر سمكاً في الأسفل.',
    micro: {
      badge: '🔬 وزن عمود السائل',
      before: [{t:'atom',s:'عمق قليل h₁',c:'#7DD3FC',tc:'#082F49'}],
      after:  [{t:'atom',s:'عمق كبير h₃ ➔ P كبير',c:'#0284C7',tc:'#FFFFFF'}]
    }
  },
  'act-atmospheric-cup': {
    shortTitle: 'تجربة الضغط الجوي',
    unitGroup: 'u12_p',
    unitSub: 'الضغط والموائع',
    icon: '🥛',
    props: ['كأس مملوء تماماً بالماء', 'بطاقة كرتون مستوية', 'هواء جوي خارجي'],
    step1H: 'افحص الكأس والورقة',
    step1P: 'املأ الكأس حتى حافته دون فقاعات هواء وغطِّه ببطاقة مستوية.',
    step1Btn: 'املأ الكأس وغطّه',
    step2H: 'اقلب الكأس رأساً على عقب',
    step2P: 'سنرفع يدنا بحذر بعد قلب الكأس. <b>ماذا تتوقع أن يحدث؟</b>',
    predictions: ['تثبت الورقة ولا ينسكب الماء', 'ينسكب الماء كله', 'تتمزق الورقة فوراً'],
    step2Btn: 'ارفع يدك عن الورقة',
    step3H: 'بقاء الماء معلقاً دون انسكاب!',
    obs: ['تماسك الورقة بالفوهة', 'منع دخول الهواء للداخل', 'توازن القوى رأسياً'],
    step3Btn: 'فسّر القوة الخفية',
    step4H: 'ضغط الهواء الجوي الصاعد',
    step4P: 'يؤثر <b>الضغط الجوي</b> من الأسفل للأعلى بقوة تفوق وزن عمود الماء داخل الكأس.',
    step4Btn: 'تحقق من فهمك',
    step5P: 'أثبتّ وجود الضغط الجوي الجبار الذي يحيط بنا من كل اتجاه.',
    micro: {
      badge: '🔬 تصادم جزيئات الهواء',
      before: [{t:'atom',s:'وزن الماء ⬇️',c:'#38BDF8',tc:'#082F49'}],
      after:  [{t:'atom',s:'P_atm ⬆️ أقوى',c:'#10B981',tc:'#052E16'}]
    }
  },
  'act-solar-concentration': {
    shortTitle: 'تركيز الطاقة الشمسية',
    unitGroup: 'u13_sol',
    unitSub: 'الطاقة الشمسية',
    icon: '☀️',
    props: ['أشعة شمسية متوازية', 'عدسة محدبة لامة', 'ورقة جافة ووعاء أسود'],
    step1H: 'افحص العدسة المحدبة',
    step1P: 'العدسة المحدبة سميكة بالوسط وتكسر الأشعة لتتجمع في نقطة البؤرة.',
    step1Btn: 'وجّه العدسة للشمس',
    step2H: 'اضبط البؤرة على الورقة',
    step2P: 'نحرّك العدسة حتى تصغر البقعة الضوئية جداً. <b>ماذا تتوقع؟</b>',
    predictions: ['ترتفع الحرارة وتشتعل الورقة', 'تتشتت الأشعة وتبرد', 'يتغير لون العدسة'],
    step2Btn: 'ركّز الأشعة الآن',
    step3H: 'تركز حراري شديد واشتعال!',
    obs: ['بقعة ضوئية حارقة', 'دخان واشتعال الورقة', 'الوعاء الأسود يمتص أكثر'],
    step3Btn: 'فسّر التحول الطاقي',
    step4H: 'التجميع البؤري واللون الأسود',
    step4P: 'يتحول الإشعاع الشمسي المركز في البؤرة إلى <b>طاقة حرارية</b> عالية والأسود يمتصها بكفاءة.',
    step4Btn: 'تحقق من فهمك',
    step5P: 'فهمت مبدأ عمل السخانات الشمسية والمجمعات الحرارية المنزلية.',
    micro: {
      badge: '🔬 تقارب الفوتونات الضوئية',
      before: [{t:'atom',s:'أشعة متوازية ☀️',c:'#FACC15',tc:'#422006'}],
      after:  [{t:'atom',s:'بؤرة حرارية 🔥',c:'#EF4444',tc:'#FFFFFF'}]
    }
  },
  'act-mendel-punnett': {
    shortTitle: 'تجارب مندل والوراثة',
    unitGroup: 'u16_gen',
    unitSub: 'الوراثة والكائنات',
    icon: '🧬',
    props: ['نبات أرجواني نقي AA', 'نبات أبيض متنحٍ aa', 'جدول التزاوج بانيت'],
    step1H: 'افحص صفات الأبوين النقيين',
    step1P: 'أب يحمل جينين سائدين (AA) وأم تحمل جينين متنحيين (aa).',
    step1Btn: 'استخلص الأمشاج',
    step2H: 'تزاوج الجيل الأول ثم الثاني',
    step2P: 'يتزاوج أفراد الجيل الأول الهجين (Aa × Aa). <b>ما نسبة ظهور الأبيض؟</b>',
    predictions: ['25% أبيض : 75% أرجواني', '50% أرجواني : 50% أبيض', 'يختفي الأبيض للأبد'],
    step2Btn: 'أجرِ التزاوج (بانيت)',
    step3H: 'ظهور مربع بانيت للجيلين!',
    obs: ['الجيل F₁ كله أرجواني Aa', 'ظهور الأبيض aa في F₂', 'النسبة المظهرية 3 : 1'],
    step3Btn: 'فسّر القوانين الوراثية',
    step4H: 'قانون انعزال الصفات لمندل',
    step4P: 'الصفة <b>السائدة (A)</b> تحجب المتنحية في الجيل الأول وتنفصل الأمشاج مستقلة في الثاني.',
    step4Btn: 'تحقق من فهمك',
    step5P: 'أتقنت التنبؤ بالطرز الجينية والمظهرية عبر مربع بانيت.',
    micro: {
      badge: '🔬 انفصال الأليلات الوراثية',
      before: [{t:'atom',s:'AA',c:'#A855F7',tc:'#FAF5FF'}, {t:'plus'}, {t:'atom',s:'aa',c:'#E2E8F0',tc:'#0F172A'}],
      after:  [{t:'pair',a:'A',b:'a',ca:'#A855F7',cb:'#E2E8F0'}, {t:'atom',s:'(3 : 1)',c:'#10B981',tc:'#052E16'}]
    }
  }
};

function openActivityModal(actId) {
  if (actId) actState.currentActId = actId;
  const modal = document.getElementById('activityModal');
  if (!modal) return;
  modal.classList.add('open');
  switchActivity(actState.currentActId);
  playDingSound();
}

function closeActivityModal() {
  const modal = document.getElementById('activityModal');
  if (modal) modal.classList.remove('open');
  toggleActMoreMenu(false);
  playClickSound();
}

function switchActivity(actId) {
  actState.currentActId = (actId && ACT_META[actId]) ? actId : 'act-magnesium-combustion';
  actState.curStep = 1;
  actState.metal = 'mg';
  actState.discoveredProps = [true, true, false];
  actState.selectedPrediction = 1;
  actState.selectedObs = [true, true, false];
  updateActivityUI();
}

function getUnitSiblings(actId) {
  const grp = ACT_META[actId]?.unitGroup || 'u9_ox';
  const keys = Object.keys(ACT_META);
  if (actState.showAllMenuActs) return keys;
  const same = keys.filter(k => ACT_META[k].unitGroup === grp);
  return same.length ? same : keys.slice(0, 3);
}

function updateActivityUI() {
  const acts = window.THAKER_CURRICULUM_P2?.activities || {};
  const data = acts[actState.currentActId];
  const meta = ACT_META[actState.currentActId];
  if (!data || !meta) return;

  const siblings = getUnitSiblings(actState.currentActId);
  const unitAll = Object.keys(ACT_META).filter(k => ACT_META[k].unitGroup === meta.unitGroup);
  const idxInUnit = Math.max(1, unitAll.indexOf(actState.currentActId) + 1);

  document.getElementById('actModalMainTitle').textContent = meta.shortTitle;
  document.getElementById('actModalSubTitle').textContent = `${meta.unitSub} · نشاط ${idxInUnit} من ${unitAll.length}`;

  const step = actState.curStep;
  const total = actState.totalSteps;
  document.getElementById('actStepCounterBadge').textContent = `${step}/${total}`;

  // Segmented 5 bars (#10B981 done, #0EA5E9 active, muted upcoming)
  const bars = document.querySelectorAll('#actSegBars .act-seg');
  bars.forEach((bar, i) => {
    const num = i + 1;
    bar.classList.remove('done', 'active');
    if (num < step) bar.classList.add('done');
    else if (num === step) bar.classList.add('active');
  });

  renderActivityStageV3(actState.currentActId, step, meta, data);
  renderActivityBottomSheetV3(actState.currentActId, step, meta, data);
  renderMoreMenuListV3(siblings);
}

function renderActivityStageV3(actId, step, meta, data) {
  const el = document.getElementById('dynamicStageVisual');
  if (!el) return;

  if (step === 4) {
    el.innerHTML = buildMicroAtomicStage(meta.micro);
    return;
  }

  // Render underlying experiment bench illustration cleanly
  if (actId === 'act-magnesium-combustion') renderMagnesiumStageV3(el, step);
  else if (actId === 'act-sulfur-combustion') renderSulfurStage(el, step);
  else if (actId === 'act-rusting-conditions') renderRustingStage(el, step);
  else if (actId === 'act-carbon-allotropy') renderCarbonStage(el, step);
  else if (actId === 'act-co2-prep-procedure') renderCo2PrepStage(el, step);
  else if (actId === 'act-co2-properties') renderCo2PropsStage(el, step);
  else if (actId === 'act-petroleum-refining') renderPetroleumStage(el, step);
  else if (actId === 'act-chlorine-prep') renderChlorinePrepStage(el, step);
  else if (actId === 'act-elasticity-solids') renderElasticityStage(el, step);
  else if (actId === 'act-surface-tension') renderSurfaceTensionStage(el, step);
  else if (actId === 'act-viscosity-liquids') renderViscosityStage(el, step);
  else if (actId === 'act-liquid-pressure-depth') renderLiquidPressureStage(el, step);
  else if (actId === 'act-atmospheric-cup') renderAtmosphericCupStage(el, step);
  else if (actId === 'act-solar-concentration') renderSolarConcentrationStage(el, step);
  else if (actId === 'act-mendel-punnett') renderMendelPunnettStage(el, step);

  // Step 1: Attach clean interactive property discovery chips on the side
  if (step === 1 && meta.props) {
    const stack = document.createElement('div');
    stack.className = 'act-prop-stack';
    stack.innerHTML = meta.props.map((p, i) => {
      const chk = actState.discoveredProps[i];
      return `<button type="button" class="act-prop-chip ${chk ? 'checked' : ''}" onclick="togglePropDiscover(${i})">${chk ? '✓' : '○'} ${p}</button>`;
    }).join('');
    el.appendChild(stack);
  }

  // Step 5: Attach clean green completion checkmark centered above bench result
  if (step === 5) {
    const badge = document.createElement('div');
    badge.className = 'act-complete-badge';
    badge.style.position = 'absolute';
    badge.style.top = '18px';
    badge.style.left = '50%';
    badge.style.transform = 'translateX(-50%)';
    badge.style.zIndex = '8';
    badge.textContent = '✓';
    el.appendChild(badge);
  }
}

function renderMagnesiumStageV3(el, step) {
  const ribbonColors = {
    mg: { strip: 'linear-gradient(90deg, #94A3B8, #F1F5F9, #64748B)', tag: 'شريط ماغنسيوم (Mg)', ash: 'أكسيد الماغنسيوم MgO', glow: '#ffffff', halo: '#bae6fd' },
    na: { strip: 'linear-gradient(90deg, #CBD5E1, #E2E8F0)', tag: 'صوديوم نقي (Na)', ash: 'أكسيد الصوديوم Na₂O', glow: '#fef08a', halo: '#f59e0b' },
    ca: { strip: 'linear-gradient(90deg, #94A3B8, #CBD5E1)', tag: 'كالسيوم صلب (Ca)', ash: 'أكسيد الكالسيوم CaO', glow: '#fed7aa', halo: '#ef4444' },
    fe: { strip: 'linear-gradient(90deg, #475569, #94A3B8)', tag: 'ليف حديد (Fe)', ash: 'أكسيد الحديد Fe₃O₄', glow: '#fde68a', halo: '#f97316' }
  }[actState.metal || 'mg'];

  if (step === 1) {
    el.innerHTML = `
      <div style="width:100%; height:100%; position:relative; cursor:pointer;" onclick="discoverAllPropsV3()">
        <div style="position:absolute; bottom:12px; left:24%; display:flex; flex-direction:column; align-items:center;">
          <div class="burner-flame"></div>
          <div style="width:28px; height:64px; background:linear-gradient(90deg,#64748B,#E2E8F0,#475569); border-radius:6px 6px 2px 2px;"></div>
          <div style="width:68px; height:12px; background:rgba(148,163,184,0.22); border-radius:50%; margin-top:2px;"></div>
        </div>
        <div style="position:absolute; bottom:10px; right:16%; display:flex; flex-direction:column; align-items:center;">
          <div style="width:128px; height:24px; border-radius:50%; border:2px solid rgba(255,255,255,0.28); background:rgba(255,255,255,0.06); display:flex; align-items:center; justify-content:center;">
            <div style="width:76px; height:8px; border-radius:4px; background:${ribbonColors.strip}; transform:rotate(-6deg); box-shadow:0 0 8px rgba(255,255,255,0.35);"></div>
          </div>
          <span class="act-float-tag" style="position:relative; top:-64px; left:64px;">${ribbonColors.tag}</span>
        </div>
      </div>
    `;
  } else if (step === 2) {
    el.innerHTML = `
      <div style="width:100%; height:100%; position:relative;">
        <div style="position:absolute; bottom:12px; left:24%; display:flex; flex-direction:column; align-items:center;">
          <div class="burner-flame"></div>
          <div style="width:28px; height:64px; background:linear-gradient(90deg,#64748B,#E2E8F0,#475569); border-radius:6px 6px 2px 2px;"></div>
        </div>
        <svg viewBox="0 0 120 80" style="position:absolute; bottom:84px; left:14%; width:95px; height:64px; pointer-events:none;">
          <path d="M 15 10 Q 32 46 68 62" fill="none" stroke="#38BDF8" stroke-width="3" stroke-dasharray="6,6"/>
        </svg>
        <div style="position:absolute; bottom:106px; left:22%; display:flex; align-items:center;">
          <div style="width:72px; height:9px; background:${ribbonColors.strip}; border-radius:4px; box-shadow:0 0 10px rgba(255,255,255,0.45);"></div>
          <div style="width:155px; height:7px; background:linear-gradient(90deg,#CBD5E1,#64748B); transform:rotate(-26deg); transform-origin:left center; border-radius:4px;"></div>
        </div>
        <span class="act-float-tag" style="position:absolute; right:16%; top:20%;">ملقط</span>
        <span class="act-float-tag" style="position:absolute; left:10%; bottom:26%;">موقد بنسن</span>
        <div style="position:absolute; bottom:10px; right:16%; width:124px; height:22px; border-radius:50%; border:2px solid rgba(255,255,255,0.25); background:rgba(255,255,255,0.05);"></div>
      </div>
    `;
  } else if (step === 3) {
    el.innerHTML = `
      <div style="width:100%; height:100%; position:relative; background:radial-gradient(circle at 38% 48%, ${ribbonColors.halo} 0%, rgba(255,255,255,0.18) 28%, transparent 62%);">
        <div style="position:absolute; bottom:12px; left:26%; width:28px; height:66px; background:linear-gradient(90deg,#64748B,#E2E8F0,#475569); border-radius:6px 6px 2px 2px;"></div>
        <div class="magnesium-glow" style="left:33%; top:34%; background:radial-gradient(circle, ${ribbonColors.glow} 40%, ${ribbonColors.halo} 75%, transparent 90%);"></div>
        <div style="position:absolute; bottom:10px; right:16%; width:124px; height:22px; border-radius:50%; border:2px solid rgba(255,255,255,0.28); background:rgba(255,255,255,0.06);"></div>
      </div>
    `;
  } else {
    el.innerHTML = `
      <div style="width:100%; height:100%; position:relative;">
        <div style="position:absolute; bottom:12px; left:24%; width:28px; height:64px; background:linear-gradient(90deg,#64748B,#E2E8F0,#475569); border-radius:6px 6px 2px 2px;"></div>
        <div style="position:absolute; bottom:12px; right:14%; display:flex; flex-direction:column; align-items:center;">
          <span class="act-float-tag" style="margin-bottom:8px;">${ribbonColors.ash}</span>
          <div style="width:134px; height:26px; border-radius:50%; border:2px solid rgba(255,255,255,0.3); background:rgba(255,255,255,0.07); position:relative; display:flex; align-items:center; justify-content:center;">
            <div style="width:74px; height:22px; background:radial-gradient(ellipse at bottom, #FFFFFF 55%, #CBD5E1 100%); border-radius:50% 50% 8px 8px; margin-top:-10px; box-shadow:0 0 14px rgba(255,255,255,0.35);"></div>
          </div>
        </div>
      </div>
    `;
  }
}

function buildMicroAtomicStage(micro) {
  const renderTok = (tok) => {
    if (tok.t === 'plus') return `<span style="font-size:20px; font-weight:800; color:#94A3B8;">+</span>`;
    if (tok.t === 'atom') {
      const sz = tok.s.length > 3 ? 52 : 44;
      const fs = tok.s.length > 3 ? 11 : 14;
      return `<div style="width:${sz}px; height:${sz}px; border-radius:50%; background:${tok.c}; color:${tok.tc}; font-size:${fs}px; font-weight:800; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 14px rgba(0,0,0,0.3);">${tok.s}</div>`;
    }
    if (tok.t === 'di') {
      return `<div style="display:flex; align-items:center;">
        <div style="width:36px; height:36px; border-radius:50%; background:${tok.c}; color:${tok.tc}; font-weight:800; font-size:13px; display:flex; align-items:center; justify-content:center;">${tok.s}</div>
        <div style="width:36px; height:36px; border-radius:50%; background:${tok.c}; color:${tok.tc}; font-weight:800; font-size:13px; display:flex; align-items:center; justify-content:center; margin-left:-6px; border:2px solid #091522;">${tok.s}</div>
      </div>`;
    }
    if (tok.t === 'tri') {
      return `<div style="display:flex; align-items:center;">
        <div style="width:30px; height:30px; border-radius:50%; background:${tok.ca}; color:#0F172A; font-weight:800; font-size:11px; display:flex; align-items:center; justify-content:center;">${tok.a}</div>
        <div style="width:36px; height:36px; border-radius:50%; background:${tok.cb}; color:#0F172A; font-weight:800; font-size:12px; display:flex; align-items:center; justify-content:center; margin:0 -6px; border:2px solid #091522;">${tok.b}</div>
        <div style="width:30px; height:30px; border-radius:50%; background:${tok.cc}; color:#0F172A; font-weight:800; font-size:11px; display:flex; align-items:center; justify-content:center;">${tok.c}</div>
      </div>`;
    }
    if (tok.t === 'pair') {
      return `<div style="display:flex; align-items:center;">
        <div style="width:42px; height:42px; border-radius:50%; background:${tok.ca}; color:#0F172A; font-weight:800; font-size:12px; display:flex; align-items:center; justify-content:center;">${tok.a}</div>
        <div style="width:32px; height:32px; border-radius:50%; background:${tok.cb}; color:#082F49; font-weight:800; font-size:11px; display:flex; align-items:center; justify-content:center; margin-left:-10px; border:2px solid #091522;">${tok.b}</div>
      </div>`;
    }
    return '';
  };

  return `
    <div style="width:100%; height:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:8px 12px;">
      <div class="act-micro-badge">${micro.badge}</div>
      <div class="act-micro-cols">
        <div class="act-micro-side">
          <div class="act-micro-lbl">قبل التفاعل</div>
          <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:8px;">
            ${micro.before.map(renderTok).join('')}
          </div>
        </div>
        <div style="font-size:30px; color:#10B981; font-weight:900; padding-top:16px;">➔</div>
        <div class="act-micro-side">
          <div class="act-micro-lbl">بعد التفاعل</div>
          <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; gap:8px;">
            ${micro.after.map(renderTok).join('')}
          </div>
        </div>
      </div>
    </div>
  `;
}

function renderActivityBottomSheetV3(actId, step, meta, data) {
  const sheet = document.getElementById('actBottomSheet');
  if (!sheet) return;
  const stepData = (data.steps && data.steps[step - 1]) || {};
  let html = '';

  if (step === 1) {
    html = `
      <h3 class="act-step-h">${meta.step1H}</h3>
      <p class="act-step-p">${meta.step1P}</p>
      <button class="act-primary-cta" onclick="executeStep1Inspect()">${meta.step1Btn} &nbsp;‹</button>
    `;
  } else if (step === 2) {
    const pills = meta.predictions.map((txt, idx) =>
      `<button class="act-choice-pill ${actState.selectedPrediction === idx ? 'selected' : ''}" onclick="selectActPred(${idx})">${txt}</button>`
    ).join('');
    html = `
      <h3 class="act-step-h">${meta.step2H}</h3>
      <p class="act-step-p">${meta.step2P}</p>
      <div class="act-pills-wrap">${pills}</div>
      <button class="act-primary-cta" onclick="executeCurrentActAction()">${meta.step2Btn} &nbsp;‹</button>
    `;
  } else if (step === 3) {
    const obsPills = meta.obs.map((txt, idx) => {
      const on = actState.selectedObs[idx];
      return `<button class="act-choice-pill ${on ? 'selected' : ''}" onclick="toggleActObs(${idx})">${txt}${on ? ' ✓' : ''}</button>`;
    }).join('');
    const warn = stepData.safety ? `<div class="act-safety-line">⚠️ ${stepData.safety.replace(/^⚠️\s*(تحذير\s*وزاري:|تحذير:)?\s*/,'')}</div>` : '';
    html = `
      <h3 class="act-step-h">${meta.step3H}</h3>
      <p class="act-step-p">ماذا لاحظت؟ المس ما رأيته:</p>
      <div class="act-pills-wrap">${obsPills}</div>
      ${warn}
      <button class="act-primary-cta" onclick="jumpActivityStep(4)">${meta.step3Btn} &nbsp;‹</button>
    `;
  } else if (step === 4) {
    html = `
      <h3 class="act-step-h">${meta.step4H}</h3>
      <p class="act-step-p">${meta.step4P}</p>
      <div class="act-eq-box">${data.equation_symbolic || ''}</div>
      <button class="act-primary-cta" onclick="jumpActivityStep(5)">${meta.step4Btn} &nbsp;‹</button>
    `;
  } else {
    const retryBtn = actId === 'act-magnesium-combustion'
      ? `<button class="act-ghost-pill" onclick="cycleOtherMetalV3()">🔁 جرّب فلزاً آخر</button>`
      : `<button class="act-ghost-pill" onclick="resetActivitySimulation()">🔁 إعادة التجربة</button>`;
    html = `
      <h3 class="act-step-h">أحسنت! أتممت النشاط</h3>
      <p class="act-step-p">${meta.step5P}</p>
      <div class="act-dual-row">
        ${retryBtn}
        <button class="act-ghost-pill" onclick="closeActivityModal()">📖 إلى صفحة الكتاب</button>
      </div>
      <button class="act-primary-cta" onclick="launchActivityQuiz()">اختبر نفسك &nbsp;‹</button>
    `;
  }
  sheet.innerHTML = html;
}

function togglePropDiscover(idx) {
  actState.discoveredProps[idx] = !actState.discoveredProps[idx];
  playClickSound();
  updateActivityUI();
}
function discoverAllPropsV3() {
  actState.discoveredProps = [true, true, true];
  playDingSound();
  updateActivityUI();
}
function executeStep1Inspect() {
  actState.discoveredProps = [true, true, true];
  playDingSound();
  jumpActivityStep(2);
}
function selectActPred(idx) {
  actState.selectedPrediction = idx;
  playClickSound();
  updateActivityUI();
}
function toggleActObs(idx) {
  actState.selectedObs[idx] = !actState.selectedObs[idx];
  playClickSound();
  updateActivityUI();
}
function executeCurrentActAction() {
  playDingSound();
  jumpActivityStep(Math.min(actState.totalSteps, actState.curStep + 1));
}
function jumpActivityStep(stepNum) {
  actState.curStep = Math.max(1, Math.min(actState.totalSteps, stepNum));
  playClickSound();
  updateActivityUI();
}
function nextActivityStep() { if (actState.curStep < actState.totalSteps) jumpActivityStep(actState.curStep + 1); }
function prevActivityStep() { if (actState.curStep > 1) jumpActivityStep(actState.curStep - 1); }
function resetActivitySimulation() {
  switchActivity(actState.currentActId);
  playSnapSound();
}
function cycleOtherMetalV3() {
  const order = ['mg', 'na', 'ca', 'fe'];
  const nxt = order[(order.indexOf(actState.metal || 'mg') + 1) % order.length];
  actState.metal = nxt;
  const msgs = {
    mg: 'الماغنسيوم Mg: اشتعال بضوء أبيض ساطع (MgO)',
    na: 'الصوديوم Na: اشتعال سريع بلهب أصفر ذهبي (Na₂O)',
    ca: 'الكالسيوم Ca: لهب أحمر قرميدي (CaO)',
    fe: 'الحديد Fe: توهج وشرارات متطايرة (Fe₃O₄)'
  };
  showToast(msgs[nxt]);
  playDingSound();
  updateActivityUI();
}
function launchActivityQuiz() {
  closeActivityModal();
  const p = PAGES[state.curPageIdx];
  const ints = INTERACTIONS[p?.page_id] || [];
  const qInt = ints.find(i => i.assessment_ref);
  if (qInt && ASSESSMENTS[qInt.assessment_ref]) openAssessmentModal(qInt.assessment_ref);
  else switchBookTab('quiz');
}
function toggleActMoreMenu(show) {
  const el = document.getElementById('actMoreBackdrop');
  if (el) el.classList.toggle('open', !!show);
}
function renderMoreMenuListV3(keys) {
  const listEl = document.getElementById('actMoreActivitiesList');
  const toggleBtn = document.getElementById('btnToggleAllActsMenu');
  if (!listEl) return;
  listEl.innerHTML = keys.map(k => {
    const m = ACT_META[k];
    const active = k === actState.currentActId;
    return `<button class="act-more-item" onclick="toggleActMoreMenu(false); switchActivity('${k}');">
      <span>${m.icon} &nbsp; ${m.shortTitle}</span>
      <span style="color:#10B981; font-weight:900;">${active ? '✓' : ''}</span>
    </button>`;
  }).join('');
  if (toggleBtn) {
    toggleBtn.querySelector('span').textContent = actState.showAllMenuActs
      ? '🔼 عرض أنشطة هذه الوحدة فقط'
      : '📚 عرض جميع أنشطة الكتاب (15)';
  }
}
function toggleShowAllActivitiesInMenu() {
  actState.showAllMenuActs = !actState.showAllMenuActs;
  renderMoreMenuListV3(getUnitSiblings(actState.currentActId));
}
function showCurrentActivityHint() {
  const acts = window.THAKER_CURRICULUM_P2?.activities || {};
  const data = acts[actState.currentActId];
  const st = data?.steps?.[actState.curStep - 1];
  showToast('💡 ' + (st?.voice || st?.desc || 'اتبع الخطوات بالتسلسل لتكتشف النتيجة.'));
}
function showBeforeAfterCompareModal() {
  const acts = window.THAKER_CURRICULUM_P2?.activities || {};
  const data = acts[actState.currentActId];
  if (!data?.comparison) {
    showToast(data?.equation_verbal || 'النشاط مكتمل بالمعادلة الموزونة.');
    return;
  }
  const c = data.comparison;
  showToast(`⚖️ قبل: ${c.before.color} · ${c.before.state}  |  بعد: ${c.after.color} · ${c.after.state}`);
}
function jumpToActivityBookPage() {
  const acts = window.THAKER_CURRICULUM_P2?.activities || {};
  const data = acts[actState.currentActId];
  toggleActMoreMenu(false);
  closeActivityModal();
  if (data?.book_pages?.length) {
    const idx = PAGES.findIndex(p => p.book_page === data.book_pages[0]);
    if (idx !== -1) loadPage(idx);
  }
}
"""


def main():
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        src = f.read()

    # 1. Replace Activity Modal CSS block cleanly
    css_pattern = re.compile(
        r"/\* Layer 3D: Dark Immersive Activity Modal.*?/\* Assessment Modal \(10-quiz\.png\) \*/",
        re.S,
    )
    if not css_pattern.search(src):
        raise RuntimeError("Could not find CSS activityModal block in thaker-interactive-book.html")
    src = css_pattern.sub(lambda _: NEW_ACTIVITY_CSS + "\n/* Assessment Modal (10-quiz.png) */", src, count=1)

    # 2. Replace Activity Modal HTML block cleanly
    html_pattern = re.compile(
        r"<!-- Layer 3D: Immersive Step-by-Step Activity Modal.*?<!-- Layer 3C: Assessment Modal",
        re.S,
    )
    if not html_pattern.search(src):
        raise RuntimeError("Could not find HTML activityModal block in thaker-interactive-book.html")
    src = html_pattern.sub(lambda _: NEW_ACTIVITY_HTML + "\n<!-- Layer 3C: Assessment Modal", src, count=1)

    # 3. Replace old actState + open/switch/update/execute/renderMagnesium block while KEEPING custom stage renderers!
    js_top_pat = re.compile(
        r"// LAYER 3D: INTERACTIVE ACTIVITY ENGINE \(ALL 7 UNIT 9 ACTIVITIES\).*?function renderChlorinePrepStage",
        re.S,
    )
    if not js_top_pat.search(src):
        raise RuntimeError("Could not find JS actState..renderChlorinePrepStage block")
    src = js_top_pat.sub(lambda _: NEW_ACTIVITY_JS + "\nfunction renderChlorinePrepStage", src, count=1)

    # 4. Also remove old renderMagnesiumStage + duplicate executeCurrentActAction..testOtherMetal after renderPetroleumStage
    js_tail_pat = re.compile(
        r"// 1\. Magnesium Combustion Visual Stage.*?function renderSulfurStage",
        re.S,
    )
    if js_tail_pat.search(src):
        src = js_tail_pat.sub(lambda _: "// 2. Sulfur Combustion Visual Stage\nfunction renderSulfurStage", src, count=1)

    js_exec_pat = re.compile(
        r"function executeCurrentActAction\(\).*?// LAYER 3A: SMART TEXT BOTTOM SHEET",
        re.S,
    )
    if not js_exec_pat.search(src):
        raise RuntimeError("Could not find old executeCurrentActAction block")
    src = js_exec_pat.sub(lambda _: "\n// LAYER 3A: SMART TEXT BOTTOM SHEET", src, count=1)

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(src)
    print("✓ Updated thaker-interactive-book.html with Guided 5-Step Lab Design")

    if os.path.exists(os.path.dirname(ANDROID_HTML_PATH)):
        with open(ANDROID_HTML_PATH, "w", encoding="utf-8") as f:
            f.write(src)
        print("✓ Mirrored to thaker-android-src/assets/thaker-interactive-book.html")


if __name__ == "__main__":
    main()
