#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shared Dark-Navy V3 Guided Lab UI Shell for Grade 12 Interactive Laboratories
(physics-12th-lab.html & biology-12th-lab.html)
Matches the exact 5-step guided lab architecture and visual design from
Grade 9 Science Part 2 (upgrade_experiments_v3.py / /mnt/sdcard/تطبيق ذاكر/تصميم التجارب):
1. فحص الأدوات والعينات (Inspection of samples/tools with interactive discovery chips)
2. ضبط المتغيرات والتوقع التفاعلي (Run action & select predictions)
3. الملاحظة الحية والتحقق المعملي (Live bench results & observation chips)
4. التفسير العلمي والقانون الرياضي / البنية المجهرية (Scientific law & structural explanation)
5. الإتقان وسؤال التحقق (Celebration badge, interactive quiz, retry & return)
"""


def build_v3_lab_css(accent_hex="#38BDF8", accent_rgb="56, 189, 248"):
    return f"""
:root {{
  --bg: #060E17;
  --stage-radial: radial-gradient(circle at 50% 22%, #13283E 0%, #091522 60%, #060E17 100%);
  --sheet-bg: #0F1D2E;
  --card: rgba(255, 255, 255, 0.05);
  --primary: #10B981;
  --primary-deep: #059669;
  --sky: #0EA5E9;
  --accent: {accent_hex};
  --accent-rgb: {accent_rgb};
  --warning: #FBBF24;
  --danger: #EF4444;
  --text: #F8FAFC;
  --muted: #94A3B8;
  --border: rgba(255, 255, 255, 0.10);
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }}
html, body {{
  width: 100%; height: 100dvh; max-height: 100dvh; overflow: hidden;
  background: var(--stage-radial); color: var(--text);
  font-family: 'Tajawal', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}}

/* Shell Container (Responsive 5-step guided layout) */
.act-shell {{
  width: 100%; max-width: 620px; margin: 0 auto; height: 100dvh; max-height: 100dvh;
  display: flex; flex-direction: column; justify-content: space-between; overflow: hidden;
  background: var(--stage-radial); position: relative;
}}
@media (min-width: 960px) {{
  .act-shell {{
    max-width: 1180px; flex-direction: row; align-items: stretch; padding: 14px; gap: 16px;
  }}
}}

/* V3 Top Header & Segmented Progress Row */
.act-head-wrap {{
  flex: 0 0 auto; width: 100%; background: rgba(6, 14, 23, 0.55); backdrop-filter: blur(10px); z-index: 25;
}}
@media (min-width: 960px) {{
  .act-head-wrap {{
    position: absolute; top: 14px; left: 14px; right: 14px; width: auto;
    border-radius: 20px; border: 1px solid var(--border);
  }}
}}
.act-top-bar {{
  display: flex; align-items: center; justify-content: space-between; gap: 10px;
  padding: 12px 14px 6px;
}}
.act-sq-btn {{
  width: 42px; height: 42px; border-radius: 13px; flex-shrink: 0;
  background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.12);
  color: #FFFFFF; font-size: 17px; font-weight: 800; cursor: pointer;
  display: flex; align-items: center; justify-content: center; font-family: inherit;
  transition: transform 0.15s ease, background 0.15s ease;
}}
.act-sq-btn:hover {{ background: rgba(255, 255, 255, 0.14); }}
.act-sq-btn:active {{ transform: scale(0.94); }}
.act-header-meta {{ text-align: center; flex: 1; min-width: 0; }}
.act-title {{
  font-size: 16.5px; font-weight: 800; color: #FFFFFF; line-height: 1.3;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}}
.act-sub-row {{
  display: flex; align-items: center; justify-content: center; gap: 6px; margin-top: 2px;
  flex-wrap: wrap;
}}
.act-sub {{ font-size: 11.5px; color: var(--muted); font-weight: 600; }}
.act-exp-pill {{
  background: rgba(var(--accent-rgb), 0.16); border: 1px solid rgba(var(--accent-rgb), 0.4);
  color: var(--accent); border-radius: 999px; padding: 2px 10px; font-size: 11px; font-weight: 800;
  cursor: pointer; font-family: inherit; transition: background 0.2s;
}}
.act-exp-pill:hover {{ background: rgba(var(--accent-rgb), 0.28); }}
#expSelect {{ display: none; }}

/* Segmented 5 progress bars */
.act-seg-row {{
  display: flex; align-items: center; gap: 8px; padding: 6px 14px 8px; width: 100%;
}}
.act-seg-bars {{ flex: 1; display: flex; gap: 6px; }}
.act-seg {{
  flex: 1; height: 5px; border-radius: 999px; background: rgba(255, 255, 255, 0.15);
  cursor: pointer; transition: all 0.25s ease;
}}
.act-seg.done {{ background: #10B981; }}
.act-seg.active {{ background: #0EA5E9; box-shadow: 0 0 10px rgba(14, 165, 233, 0.65); }}
.act-seg-count {{
  font-size: 12px; font-weight: 800; color: #CBD5E1; min-width: 28px; text-align: left;
  font-variant-numeric: tabular-nums; flex-shrink: 0;
}}

/* Open Lab Bench Stage */
#stageArea {{
  position: relative; flex: 1 1 auto; min-height: 200px; width: 100%;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  overflow: hidden; background: transparent;
}}
@media (min-width: 960px) {{
  #stageArea {{
    flex: 1.25; height: 100%; min-height: 0; margin-top: 80px;
    border-radius: 26px; border: 1px solid var(--border);
    background: radial-gradient(circle at 50% 36%, #13283E 0%, #091522 70%, #060E17 100%);
  }}
}}
#canvas3d, #canvas2d {{
  position: absolute; inset: 0; width: 100%; height: 100%; display: block;
}}
#canvas3d {{ z-index: 2; }}
#canvas2d {{ z-index: 3; pointer-events: none; }}

.act-bench-horizon {{
  position: absolute; left: 0; right: 0; bottom: 0; height: 32px; z-index: 4; pointer-events: none;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.035) 0%, rgba(6, 14, 23, 0.55) 100%);
  border-top: 1px solid rgba(255, 255, 255, 0.09);
}}

/* Floating tags & HUD badges on Stage */
#stageHud {{
  position: absolute; top: 10px; right: 12px; left: 12px; z-index: 6; pointer-events: none;
  display: flex; justify-content: space-between; align-items: flex-start; gap: 8px; flex-wrap: wrap;
}}
.act-float-tag {{
  pointer-events: auto; background: rgba(12, 24, 38, 0.86); backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 999px;
  padding: 4px 12px; font-size: 11px; font-weight: 700; color: #E2E8F0;
  box-shadow: 0 4px 12px rgba(0,0,0,0.3); max-width: 100%;
}}
#liveFormulaHud {{
  position: absolute; bottom: 10px; right: 12px; left: 12px; z-index: 6; pointer-events: none;
  display: flex; justify-content: space-between; align-items: center; gap: 6px; flex-wrap: wrap;
}}
.formula-badge {{
  background: rgba(15, 29, 46, 0.88); backdrop-filter: blur(8px);
  border: 1px solid rgba(var(--accent-rgb), 0.4); border-radius: 12px;
  padding: 4px 11px; font-size: 11.5px; font-weight: 800; color: var(--accent);
  direction: rtl; max-width: 100%; overflow-wrap: anywhere;
}}

/* Interactive Property Discovery Chips on Stage (Step 1) */
.act-prop-stack {{
  position: absolute; right: 12px; top: 12px; z-index: 7;
  display: flex; flex-direction: column; gap: 6px; align-items: flex-start; max-width: 65%;
}}
.act-prop-chip {{
  background: rgba(15, 29, 46, 0.88); backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.16); color: #CBD5E1;
  border-radius: 999px; padding: 5px 12px; font-size: 11.5px; font-weight: 700;
  cursor: pointer; transition: all 0.2s ease; display: inline-flex; align-items: center; gap: 6px;
  font-family: inherit;
}}
.act-prop-chip:hover {{ border-color: rgba(var(--accent-rgb), 0.6); }}
.act-prop-chip.checked {{
  background: rgba(16, 185, 129, 0.18); border-color: #10B981; color: #ECFDF5;
  box-shadow: 0 0 10px rgba(16, 185, 129, 0.25);
}}

/* Celebration Badge (Step 5) */
.act-complete-badge {{
  display: none; position: absolute; top: 18px; left: 50%; transform: translateX(-50%); z-index: 8;
  width: 68px; height: 68px; border-radius: 50%;
  background: linear-gradient(135deg, #10B981, #059669);
  box-shadow: 0 0 0 12px rgba(16, 185, 129, 0.18), 0 12px 28px rgba(5, 150, 105, 0.48);
  align-items: center; justify-content: center; font-size: 32px; color: #FFFFFF; font-weight: 900;
  animation: pulseComplete 1.8s infinite alternate;
}}
.act-complete-badge.show {{ display: flex; }}
@keyframes pulseComplete {{
  0% {{ transform: translateX(-50%) scale(0.96); }}
  100% {{ transform: translateX(-50%) scale(1.04); }}
}}

/* Rounded Dark-Navy Bottom Control Sheet (#0F1D2E) */
.act-bottom-sheet {{
  flex: 0 0 auto; width: 100%; background: var(--sheet-bg);
  border-top: 1px solid var(--border); border-radius: 28px 28px 0 0;
  padding: 16px 18px calc(16px + env(safe-area-inset-bottom, 0px));
  box-shadow: 0 -10px 32px rgba(0, 0, 0, 0.42);
  display: flex; flex-direction: column; gap: 11px; z-index: 10;
  max-height: 54dvh; min-height: 0; overflow-y: auto; -webkit-overflow-scrolling: touch;
}}
@media (min-width: 960px) {{
  .act-bottom-sheet {{
    flex: 0.95; height: 100%; max-height: none; margin-top: 80px;
    border-radius: 26px; border: 1px solid var(--border);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.35); padding: 22px 20px;
  }}
}}

.act-step-h {{
  font-size: 19px; font-weight: 800; color: #FFFFFF; margin: 0; line-height: 1.35;
}}
.act-step-p {{
  font-size: 13.5px; color: var(--muted); line-height: 1.65; margin: 0;
}}
.act-step-p b {{ color: #F8FAFC; }}

/* Pills & Interactive Choice buttons */
.act-pills-wrap {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 2px; }}
.act-choice-pill {{
  background: rgba(255, 255, 255, 0.05); border: 1.5px solid rgba(255, 255, 255, 0.14);
  color: #E2E8F0; border-radius: 999px; padding: 8px 14px;
  font-size: 12.5px; font-weight: 700; cursor: pointer; transition: all 0.2s ease;
  font-family: inherit;
}}
.act-choice-pill:hover {{ border-color: rgba(var(--accent-rgb), 0.5); }}
.act-choice-pill.selected {{
  background: rgba(16, 185, 129, 0.18); border-color: #10B981; color: #FFFFFF;
  box-shadow: 0 0 10px rgba(16, 185, 129, 0.25);
}}

/* Equation / Law Box */
.act-eq-box {{
  background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 14px; padding: 11px 14px; text-align: center;
  font-size: 14px; font-weight: 800; color: #FFFFFF; direction: rtl; overflow-wrap: anywhere;
}}

/* Controls / Sliders inside Step 2 */
.ctrl-row {{
  background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.10);
  border-radius: 14px; padding: 9px 12px; margin-bottom: 6px;
}}
.ctrl-label {{
  display: flex; justify-content: space-between; font-size: 12px; font-weight: 700;
  margin-bottom: 5px; color: #E2E8F0; gap: 8px;
}}
input[type=range].lab-slider {{
  width: 100%; accent-color: #10B981; cursor: pointer; height: 6px; border-radius: 99px;
}}

/* Dual Action Buttons */
.act-dual-row {{ display: flex; gap: 8px; flex-wrap: wrap; margin-top: 2px; }}
.act-ghost-pill {{
  flex: 1; min-width: 120px; background: rgba(255, 255, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.14); color: #F1F5F9;
  border-radius: 999px; padding: 10px 14px; font-size: 13px; font-weight: 700;
  cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 6px;
  font-family: inherit; transition: background 0.2s;
}}
.act-ghost-pill:hover {{ background: rgba(255, 255, 255, 0.12); }}

/* Primary Emerald Action CTA */
.act-primary-cta {{
  position: sticky; bottom: 0; z-index: 5; flex-shrink: 0;
  width: 100%; height: 50px; border-radius: 999px; border: none;
  background: linear-gradient(135deg, #10B981 0%, #059669 100%);
  color: #FFFFFF; font-size: 15.5px; font-weight: 800; cursor: pointer; font-family: inherit;
  display: flex; align-items: center; justify-content: center; gap: 8px;
  box-shadow: 0 -6px 18px 6px #0F1D2E, 0 8px 22px rgba(5, 150, 105, 0.38);
  transition: transform 0.15s ease, filter 0.2s ease; margin-top: 4px;
}}
.act-primary-cta:hover {{ filter: brightness(1.06); }}
.act-primary-cta:active {{ transform: scale(0.98); }}

/* Micro / Atomic / Law Badges (Step 4) */
.act-micro-badge {{
  background: rgba(14, 165, 233, 0.14); border: 1px solid rgba(56, 189, 248, 0.45);
  color: #BAE6FD; border-radius: 999px; padding: 6px 14px;
  font-size: 12px; font-weight: 700; text-align: center; margin-bottom: 4px;
}}
.act-micro-cols {{
  width: 100%; display: flex; align-items: center; justify-content: space-around; gap: 10px;
  padding: 6px 0;
}}
.act-micro-item {{
  background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 14px; padding: 8px 12px; text-align: center; flex: 1;
}}
.act-micro-item-title {{ font-size: 11px; color: var(--muted); margin-bottom: 4px; }}
.act-micro-item-val {{ font-size: 13.5px; font-weight: 800; color: #FFFFFF; }}

/* Quiz in Step 5 */
.quiz-opt {{
  width: 100%; text-align: right; background: rgba(255, 255, 255, 0.06); color: #F8FAFC;
  border: 1px solid rgba(255, 255, 255, 0.14); border-radius: 999px; padding: 10px 16px;
  font-size: 13px; font-weight: 700; cursor: pointer; font-family: inherit; margin-bottom: 6px;
  transition: all 0.2s ease;
}}
.quiz-opt:hover {{ background: rgba(255, 255, 255, 0.12); }}
.quiz-opt.correct {{ background: #059669; border-color: #10B981; color: #FFFFFF; }}
.quiz-opt.wrong {{ background: #B91C1C; border-color: #EF4444; color: #FFFFFF; }}

/* More Menu Drawer Bottom Sheet (#actMoreBackdrop) */
.act-more-backdrop {{
  display: none; position: fixed; inset: 0; background: rgba(3, 8, 15, 0.72);
  z-index: 300; align-items: flex-end; justify-content: center; backdrop-filter: blur(4px);
}}
.act-more-backdrop.open {{ display: flex; }}
.act-more-sheet {{
  width: 100%; max-width: 580px; max-height: min(82dvh, 600px); overflow-y: auto;
  background: #0F1D2E; border-top: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 28px 28px 0 0; padding: 10px 18px calc(24px + env(safe-area-inset-bottom, 0px));
  box-shadow: 0 -16px 40px rgba(0, 0, 0, 0.55); color: #F8FAFC;
}}
.act-more-handle {{ width: 42px; height: 4px; border-radius: 99px; background: rgba(255, 255, 255, 0.22); margin: 0 auto 10px; }}
.act-more-sec-title {{ font-size: 12px; font-weight: 800; color: #94A3B8; padding: 6px 4px; }}
.act-more-item {{
  width: 100%; background: transparent; border: none; border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  color: #F8FAFC; padding: 11px 4px; font-size: 13.5px; font-weight: 700; cursor: pointer;
  display: flex; align-items: center; justify-content: space-between; gap: 10px;
  text-align: right; font-family: inherit; transition: color 0.15s;
}}
.act-more-item:hover {{ color: var(--accent); }}
.act-more-item:last-child {{ border-bottom: none; }}
.act-more-divider {{ height: 1px; background: rgba(255, 255, 255, 0.1); margin: 8px 0; }}

/* Mobile safeguards */
@media (max-width: 480px) {{
  .act-top-bar {{ padding: 10px 12px 4px; }}
  .act-sq-btn {{ width: 38px; height: 38px; }}
  .act-title {{ font-size: 15px; }}
  .act-seg-row {{ padding: 4px 12px 6px; }}
  .act-bottom-sheet {{ max-height: 58dvh; padding: 14px 14px calc(14px + env(safe-area-inset-bottom, 0px)); }}
  .act-step-h {{ font-size: 17px; }}
  .act-step-p {{ font-size: 12.5px; line-height: 1.55; }}
  .act-primary-cta {{ height: 46px; font-size: 14.5px; }}
  .act-prop-chip {{ font-size: 10.5px; padding: 4px 9px; }}
  .act-complete-badge {{ width: 58px; height: 58px; font-size: 28px; }}
}}
@media (max-height: 640px) {{
  .act-bottom-sheet {{ max-height: 62dvh; }}
  #stageArea {{ min-height: 140px; }}
}}
"""


def build_v3_lab_body_html(header_title, book_back_label="إلى الكتاب"):
    return f"""
<div class="act-shell">
  <!-- Top Navigation Bar & 5 Segmented Step Bars -->
  <div class="act-head-wrap">
    <div class="act-top-bar">
      <button class="act-sq-btn" onclick="goBack()" title="{book_back_label}">◀</button>
      <div class="act-header-meta">
        <div class="act-title" id="hudTitle">{header_title}</div>
        <div class="act-sub-row">
          <span class="act-sub" id="actSubUnit">معمل تفاعلي خطوة بخطوة</span>
          <button type="button" class="act-exp-pill" onclick="toggleLabMoreMenu(true)">تبديل التجربة ▾</button>
        </div>
      </div>
      <button class="act-sq-btn" onclick="toggleLabMoreMenu(true)" title="قائمة التجارب والخيارات">···</button>
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
    <select id="expSelect" onchange="selectExperiment(this.value)"></select>
  </div>

  <!-- Open Interactive 3D / 2D Bench Stage -->
  <div id="stageArea">
    <canvas id="canvas3d"></canvas>
    <canvas id="canvas2d"></canvas>
    <div id="stageHud">
      <div class="act-float-tag" id="hudSubtitle">🔄 اسحب للدوران 360° • خطوة بخطوة بالمعمل</div>
    </div>
    <!-- Step 1 Discoverable Property Chips Stack -->
    <div class="act-prop-stack" id="actPropStack"></div>
    <!-- Step 5 Big Glowing Celebration Badge -->
    <div class="act-complete-badge" id="actCompleteBadge">✓</div>
    <div id="liveFormulaHud">
      <div class="formula-badge" id="hudFormula"></div>
      <div class="formula-badge" id="hudReadout" style="background:rgba(16,185,129,0.22); border-color:#10B981; color:#A7F3D0;"></div>
    </div>
    <div class="act-bench-horizon"></div>
  </div>

  <!-- Rounded Dark-Navy 5-Step Control Sheet -->
  <div class="act-bottom-sheet" id="actBottomSheet">
    <!-- Populated dynamically by renderActivityBottomSheetV3() for Steps 1..5 -->
  </div>
</div>

<!-- Drawer Bottom Sheet with All Experiments -->
<div id="actMoreBackdrop" class="act-more-backdrop" onclick="if(event.target===this)toggleLabMoreMenu(false)">
  <div class="act-more-sheet">
    <div class="act-more-handle"></div>
    <div class="act-more-sec-title">تجارب ومجسمات المنهج التفاعلية (18 نشاطاً)</div>
    <div id="actMoreList"></div>
    <div class="act-more-divider"></div>
    <div class="act-more-sec-title">خيارات</div>
    <button class="act-more-item" onclick="toggleLabMoreMenu(false); resetActivitySimulation();">
      <span>↺ إعادة بدء التجربة من الخطوة 1</span><span style="color:#94A3B8;">›</span>
    </button>
    <button class="act-more-item" onclick="toggleLabMoreMenu(false); jumpActivityStep(2);">
      <span>🎛️ ضبط وتعديل المتغيرات الحية</span><span style="color:#38BDF8;">›</span>
    </button>
    <button class="act-more-item" onclick="toggleLabMoreMenu(false); goBack();">
      <span>📖 العودة لصفحة الكتاب المدرسي</span><span style="color:#10B981;">›</span>
    </button>
  </div>
</div>
"""


RAW_V3_CONTROLLER_JS = r"""
// --------------------------------------------------------
// WEB AUDIO API SYNTHESIZER (100% OFFLINE HAPTIC AUDIO)
// --------------------------------------------------------
function playTone(freq, type, duration) {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = type || 'sine';
    osc.frequency.setValueAtTime(freq, ctx.currentTime);
    gain.gain.setValueAtTime(0.14, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + duration);
  } catch(e) {}
}
function playClickSound() { playTone(850, 'sine', 0.05); }
function playDingSound() { playTone(1046.5, 'sine', 0.35); }
function playSnapSound() { playTone(220, 'square', 0.08); }

// --------------------------------------------------------
// 5-STEP GUIDED LAB STATE
// --------------------------------------------------------
const actState = {
  curStep: 1,
  totalSteps: 5,
  discoveredProps: [false, false, false],
  selectedPrediction: 0,
  selectedObs: [true, true, true],
  actionExecuted: false
};

function toggleLabMoreMenu(show) {
  const el = document.getElementById('actMoreBackdrop');
  if (el) el.classList.toggle('open', !!show);
}

function renderMoreDrawerExps() {
  const listEl = document.getElementById('actMoreList');
  if (!listEl) return;
  listEl.innerHTML = __EXP_ARRAY_NAME__.map((e, i) => {
    const active = curExp && e.id === curExp.id;
    return `<button class="act-more-item" onclick="toggleLabMoreMenu(false); selectExperiment('${e.id}');">
      <span style="overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${i + 1}. ${e.title} <span style="color:#94A3B8;font-size:11px;">(ص ${e.bookPage})</span></span>
      <span style="color:#10B981; font-weight:900; flex-shrink:0;">${active ? '✓ نشط' : ''}</span>
    </button>`;
  }).join('');
}

function getExperiment5StepMeta(exp) {
  const cleanTitle = (exp.title || '').split('(')[0].replace(/^(النشاط|نشاط|تجربة|مختبر)\s*\d*\s*:?\s*/, '').trim();
  const tools = (exp.tools && exp.tools.length) ? exp.tools : ['عينة الاختبار', 'أداة القياس المخبرية', 'شروط التفاعل المعيارية'];
  
  // Handcrafted predictions or smart derivations
  let defaultPreds = [
    'يحدث تفاعل مباشر وتتحقق النتيجة المتوافقة مع القانون',
    'تظل المنظومة في حالة سكون دون أي تغير ملحوظ',
    'تنعكس حركة الجسيمات أو تتلاشى الطاقة كلياً'
  ];
  if (exp.predictions && exp.predictions.length) {
    defaultPreds = exp.predictions;
  } else if (exp.steps && exp.steps[1] && exp.steps[1].obs) {
    defaultPreds = [
      exp.steps[1].obs.split('؛')[0].replace(/^[^\s]+\s*/, ''),
      'لا يحدث أي تبادل أو انحراف وتبقى القراءات ثابتة',
      'فقدان تام للطاقة وتوقف النظام فوراً'
    ];
  }

  // Checkable observations
  let defaultObs = (exp.steps || []).map(s => s.obs).filter(Boolean);
  if (!defaultObs.length) defaultObs = ['حدوث الاستجابة المتوقعة بدقة', 'توافق القياسات مع معادلة الظاهرة', 'تحقق التوازن واستقرار القراءات'];

  return {
    step1H: exp.step1H || `1. افحص أدوات وعينات ${cleanTitle}`,
    step1P: exp.step1P || `المس العينات والأدوات لتتعرف على خواصها ومواصفاتها المعملية قبل بدء التجربة.`,
    step1Btn: exp.step1Btn || 'افحص الأدوات والعينات',
    props: exp.props || tools,
    step2H: exp.step2H || `2. اضبط المتغيرات وتوقع النتيجة`,
    step2P: exp.step2P || `${(exp.steps && exp.steps[0] ? exp.steps[0].desc : 'جهّز المنظومة واضبط القيم المطلوبة')}. <b>ماذا تتوقع أن يحدث عند التشغيل؟</b>`,
    step2Btn: exp.step2Btn || 'شغّل التجربة الآن',
    predictions: defaultPreds,
    step3H: exp.step3H || `3. حدوث التجربة والملاحظة الحية!`,
    step3P: exp.step3P || 'ماذا لاحظت في المعمل؟ المس المشاهدات التي رأيتها:',
    obs: exp.obs || defaultObs,
    step3Btn: exp.step3Btn || 'فسّر السبب العلمي والقانون',
    step4H: exp.step4H || `4. التفسير العلمي والقانون الحاكم`,
    step4P: exp.step4P || (exp.conclusion || (exp.steps && exp.steps[2] ? exp.steps[2].desc : '')),
    step4Btn: exp.step4Btn || 'تحقق من فهمك',
    step5P: exp.step5P || `أتقنت فهم ظاهرة ${cleanTitle} وتطبيق القانون العلمي الحاكم لها بنجاح.`
  };
}

function updateSegProgressUI() {
  const step = actState.curStep;
  const total = actState.totalSteps;
  const badge = document.getElementById('actStepCounterBadge');
  if (badge) badge.textContent = `${step}/${total}`;

  const bars = document.querySelectorAll('#actSegBars .act-seg');
  bars.forEach((bar, i) => {
    const num = i + 1;
    bar.classList.remove('done', 'active');
    if (num < step) bar.classList.add('done');
    else if (num === step) bar.classList.add('active');
  });

  const chk = document.getElementById('actCompleteBadge');
  if (chk) chk.classList.toggle('show', step === 5);
}

function jumpActivityStep(stepNum) {
  actState.curStep = Math.max(1, Math.min(actState.totalSteps, stepNum));
  playClickSound();
  updateActivityUI();
}

function executeStep1Inspect() {
  actState.discoveredProps = actState.discoveredProps.map(() => true);
  playDingSound();
  jumpActivityStep(2);
}

function executeStep2Action() {
  actState.actionExecuted = true;
  playDingSound();
  // Apply any step 1 or step 2 parameters to simulation
  if (curExp.steps && curExp.steps[1] && curExp.steps[1].params) {
    Object.entries(curExp.steps[1].params).forEach(([k, v]) => {
      params[k] = v;
      const rng = document.getElementById('rng_' + k);
      const lbl = document.getElementById('lbl_' + k);
      if (rng) rng.value = v;
      if (lbl) lbl.textContent = v;
    });
  }
  updateReadout();
  jumpActivityStep(3);
}

function togglePropDiscover(idx) {
  actState.discoveredProps[idx] = !actState.discoveredProps[idx];
  playClickSound();
  updateActivityUI();
}

function selectActPrediction(idx) {
  actState.selectedPrediction = idx;
  playClickSound();
  updateActivityUI();
}

function toggleActObs(idx) {
  actState.selectedObs[idx] = !actState.selectedObs[idx];
  playClickSound();
  updateActivityUI();
}

function onParamChange(id, val) {
  params[id] = val;
  const lbl = document.getElementById('lbl_' + id);
  if (lbl) lbl.textContent = val;
  updateReadout();
}

function updateReadout() {
  const res = computeSimulationResults();
  const hud = document.getElementById('hudReadout');
  if (hud) hud.textContent = res.short;
  const s3hud = document.getElementById('step3ReadoutHud');
  if (s3hud) s3hud.innerHTML = '📊 ' + res.short + (res.detail ? `<div style="font-size:12px;color:#CBD5E1;margin-top:4px;">${res.detail}</div>` : '');
}

function renderActivityStageOverlays() {
  const step = actState.curStep;
  const meta = getExperiment5StepMeta(curExp);
  const stack = document.getElementById('actPropStack');
  if (stack) {
    if (step === 1 && meta.props && meta.props.length) {
      stack.style.display = 'flex';
      stack.innerHTML = meta.props.map((p, i) => {
        const chk = actState.discoveredProps[i];
        return `<button type="button" class="act-prop-chip ${chk ? 'checked' : ''}" onclick="togglePropDiscover(${i})">
          ${chk ? '✓' : '○'} ${p}
        </button>`;
      }).join('');
    } else {
      stack.style.display = 'none';
    }
  }
}

function renderActivityBottomSheetV3() {
  const sheet = document.getElementById('actBottomSheet');
  if (!sheet || !curExp) return;

  const step = actState.curStep;
  const meta = getExperiment5StepMeta(curExp);
  let html = '';

  if (step === 1) {
    const propPills = (meta.props || []).map((p, i) => {
      const chk = actState.discoveredProps[i];
      return `<button type="button" class="act-prop-chip ${chk ? 'checked' : ''}" onclick="togglePropDiscover(${i})">
        ${chk ? '✓' : '○'} ${p}
      </button>`;
    }).join('');

    html = `
      <h3 class="act-step-h">${meta.step1H}</h3>
      <p class="act-step-p">${meta.step1P}</p>
      <div class="act-pills-wrap">${propPills}</div>
      <button class="act-primary-cta" onclick="executeStep1Inspect()">${meta.step1Btn} &nbsp;‹</button>
    `;
  } else if (step === 2) {
    const preds = (meta.predictions || []).map((txt, idx) =>
      `<button class="act-choice-pill ${actState.selectedPrediction === idx ? 'selected' : ''}" onclick="selectActPrediction(${idx})">${txt}</button>`
    ).join('');

    const slidersHtml = (curExp.controls || []).map(c => `
      <div class="ctrl-row">
        <div class="ctrl-label">
          <span>${c.label}</span>
          <span id="lbl_${c.id}" style="color:var(--accent); font-family:monospace;">${params[c.id]}</span>
        </div>
        <input type="range" class="lab-slider" id="rng_${c.id}" min="${c.min}" max="${c.max}" step="${c.step}" value="${params[c.id]}"
          oninput="onParamChange('${c.id}', parseFloat(this.value))">
      </div>
    `).join('');

    html = `
      <h3 class="act-step-h">${meta.step2H}</h3>
      <p class="act-step-p">${meta.step2P}</p>
      <div class="act-pills-wrap">${preds}</div>
      ${slidersHtml ? `<div style="margin-top:4px;">${slidersHtml}</div>` : ''}
      <button class="act-primary-cta" onclick="executeStep2Action()">${meta.step2Btn} &nbsp;‹</button>
    `;
  } else if (step === 3) {
    const obsPills = (meta.obs || []).map((txt, idx) => {
      const on = actState.selectedObs[idx];
      return `<button class="act-choice-pill ${on ? 'selected' : ''}" onclick="toggleActObs(${idx})">${txt}${on ? ' ✓' : ''}</button>`;
    }).join('');

    html = `
      <h3 class="act-step-h">${meta.step3H}</h3>
      <p class="act-step-p">${meta.step3P}</p>
      <div class="act-pills-wrap">${obsPills}</div>
      <div class="act-eq-box" id="step3ReadoutHud"></div>
      <button class="act-primary-cta" onclick="jumpActivityStep(4)">${meta.step3Btn} &nbsp;‹</button>
    `;
  } else if (step === 4) {
    html = `
      <h3 class="act-step-h">${meta.step4H}</h3>
      <p class="act-step-p">${meta.step4P}</p>
      <div class="act-eq-box">⚖️ ${curExp.formula}</div>
      <div class="act-micro-badge">🔬 النموذج العلمي والقانون الفيزيائي / الحيوي</div>
      <button class="act-primary-cta" onclick="jumpActivityStep(5)">${meta.step4Btn} &nbsp;‹</button>
    `;
  } else {
    const q = curExp.quiz;
    const optsHtml = q.options.map((opt, i) => `
      <button class="quiz-opt" id="quizOpt_${i}" onclick="checkQuiz(${i})">${['أ','ب','ج','د'][i]}. ${opt}</button>
    `).join('');

    html = `
      <h3 class="act-step-h">أحسنت! أتممت النشاط بنجاح 🎉</h3>
      <p class="act-step-p">${meta.step5P}</p>
      <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:16px; padding:12px; margin:4px 0;">
        <div style="font-size:13.5px; font-weight:800; color:#FFFFFF; margin-bottom:8px; line-height:1.5;">📝 ${q.q}</div>
        <div id="quizOptions">${optsHtml}</div>
        <div id="quizFeedback" style="display:none; padding:10px 12px; border-radius:12px; font-size:12.5px; line-height:1.6; margin-top:8px;"></div>
      </div>
      <div class="act-dual-row">
        <button class="act-ghost-pill" onclick="resetActivitySimulation()">🔁 إعادة التجربة</button>
        <button class="act-ghost-pill" onclick="goBack()">📖 العودة لصفحة الكتاب</button>
      </div>
    `;
  }

  sheet.innerHTML = html;
  if (step === 3) updateReadout();
}

function updateActivityUI() {
  updateSegProgressUI();
  renderActivityStageOverlays();
  renderActivityBottomSheetV3();
}

function selectExperiment(id) {
  curExp = __EXP_ARRAY_NAME__.find(e => e.id === id) || __EXP_ARRAY_NAME__[0];
  const sel = document.getElementById('expSelect');
  if (sel) sel.value = curExp.id;

  actState.curStep = 1;
  const meta = getExperiment5StepMeta(curExp);
  actState.discoveredProps = (meta.props || []).map(() => false);
  actState.selectedPrediction = 0;
  actState.selectedObs = (meta.obs || []).map(() => true);
  actState.actionExecuted = false;

  params = {};
  (curExp.controls || []).forEach(c => params[c.id] = c.default);

  const expNum = __EXP_ARRAY_NAME__.indexOf(curExp) + 1;
  document.getElementById('hudTitle').textContent = curExp.title;
  const subUnit = document.getElementById('actSubUnit');
  if (subUnit) subUnit.textContent = `${curExp.unitTitle} · نشاط ${expNum} من ${__EXP_ARRAY_NAME__.length} · ص ${curExp.bookPage}`;
  document.getElementById('hudFormula').textContent = '⚖️ ' + curExp.formula;

  renderMoreDrawerExps();
  build3dForExperiment();
  updateReadout();
  updateActivityUI();
}

function resetActivitySimulation() {
  params = {};
  (curExp.controls || []).forEach(c => params[c.id] = c.default);
  actState.curStep = 1;
  const meta = getExperiment5StepMeta(curExp);
  actState.discoveredProps = (meta.props || []).map(() => false);
  actState.selectedPrediction = 0;
  actState.actionExecuted = false;
  build3dForExperiment();
  updateReadout();
  updateActivityUI();
  playSnapSound();
}

function checkQuiz(idx) {
  const q = curExp.quiz;
  const btns = document.querySelectorAll('#quizOptions .quiz-opt');
  const fb = document.getElementById('quizFeedback');
  btns.forEach(b => b.classList.remove('correct', 'wrong'));
  if (idx === q.answer) {
    playDingSound();
    btns[idx].classList.add('correct');
    fb.style.display = 'block';
    fb.style.background = 'rgba(16,185,129,0.22)';
    fb.style.border = '1px solid #10B981';
    fb.style.color = '#A7F3D0';
    fb.innerHTML = '🎉 <b>إجابة ممتازة وصحيحة!</b><br>' + q.explain;
  } else {
    playSnapSound();
    btns[idx].classList.add('wrong');
    btns[q.answer].classList.add('correct');
    fb.style.display = 'block';
    fb.style.background = 'rgba(239,68,68,0.22)';
    fb.style.border = '1px solid #EF4444';
    fb.style.color = '#FECACA';
    fb.innerHTML = '❌ <b>غير صحيح.</b> ' + q.explain;
  }
}

const labUrlParams = (window.location.search + '&' + window.location.hash);
const labPageMatch = labUrlParams.match(/page=(\d+)/);
const labReturnPage = labPageMatch ? labPageMatch[1] : '';

function goBack() {
  if (labUrlParams.includes('from=book')) {
    window.location.href = labReturnPage ? `__RETURN_BOOK_HTML__?restore=1&page=${labReturnPage}` : `__RETURN_BOOK_HTML__?restore=1`;
  } else if (document.referrer && document.referrer.includes('__RETURN_BOOK_HTML_CLEAN__')) {
    window.history.back();
  } else if (window.ThakerBridge && window.ThakerBridge.returnToHome) {
    window.ThakerBridge.returnToHome();
  } else {
    window.location.href = `__RETURN_BOOK_HTML__?restore=1`;
  }
}

window.addEventListener('DOMContentLoaded', () => {
  const sel = document.getElementById('expSelect');
  if (sel) sel.innerHTML = __EXP_ARRAY_NAME__.map(e => `<option value="${e.id}">${e.unitTitle.split(':')[0]}: ${e.title}</option>`).join('');
  init3D();
  const m = labUrlParams.match(/exp=([a-zA-Z0-9_-]+)/);
  selectExperiment(m ? m[1] : __EXP_ARRAY_NAME__[0].id);
  animateLoop();
});
"""


def build_v3_lab_controller_js(exp_array_name, return_book_html):
    clean_book = return_book_html.replace(".html", "")
    return (
        RAW_V3_CONTROLLER_JS
        .replace("__EXP_ARRAY_NAME__", exp_array_name)
        .replace("__RETURN_BOOK_HTML__", return_book_html)
        .replace("__RETURN_BOOK_HTML_CLEAN__", clean_book)
    )
