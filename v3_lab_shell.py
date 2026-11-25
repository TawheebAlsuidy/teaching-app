#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shared Dark-Navy V3 Guided Lab UI Shell for Grade 12 Interactive Laboratories
(physics-12th-lab.html & biology-12th-lab.html)
Matches upgrade_experiments_v3.py design tokens & UX:
- Radial Deep-Navy Stage (#13283E -> #091522 -> #060E17)
- Rounded #0F1D2E Bottom/Side Control Sheet (28px top radius on mobile)
- Squircle header controls (.act-sq-btn), segmented progress bars (#10B981 / #0EA5E9)
- Pill tabs & interactive tools, #10B981 -> #059669 sticky Emerald pill CTA, #actMoreBackdrop drawer
"""


def build_v3_lab_css(accent_hex="#38BDF8", accent_rgb="56, 189, 248"):
    return f"""
:root {{
  --bg: #060E17;
  --stage-radial: radial-gradient(circle at 50% 24%, #13283E 0%, #091522 60%, #060E17 100%);
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
.act-shell {{
  width: 100%; height: 100dvh; display: flex; flex-direction: column; overflow: hidden;
  background: var(--stage-radial);
}}

/* V3 Top Header & Segmented Progress Row */
.act-head-wrap {{ flex: 0 0 auto; width: 100%; background: rgba(6, 14, 23, 0.45); backdrop-filter: blur(8px); z-index: 20; }}
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
  font-size: 16px; font-weight: 800; color: #FFFFFF; line-height: 1.3;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}}
.act-sub-row {{
  display: flex; align-items: center; justify-content: center; gap: 6px; margin-top: 2px;
  flex-wrap: wrap;
}}
.act-sub {{ font-size: 11.5px; color: var(--muted); font-weight: 600; }}
.act-exp-pill {{
  background: rgba(var(--accent-rgb), 0.15); border: 1px solid rgba(var(--accent-rgb), 0.35);
  color: var(--accent); border-radius: 999px; padding: 2px 10px; font-size: 11px; font-weight: 800;
  cursor: pointer; font-family: inherit;
}}
#expSelect {{ display: none; }}

.act-seg-row {{
  display: flex; align-items: center; gap: 10px; padding: 6px 14px 8px; max-width: 1200px; margin: 0 auto; width: 100%;
}}
.act-seg-bars {{ flex: 1; display: flex; gap: 6px; }}
.act-seg {{
  flex: 1; height: 4.5px; border-radius: 999px; background: rgba(255, 255, 255, 0.14);
  cursor: pointer; transition: all 0.25s ease;
}}
.act-seg.done {{ background: #10B981; }}
.act-seg.active {{ background: #0EA5E9; box-shadow: 0 0 8px rgba(14, 165, 233, 0.55); }}
.act-seg-count {{ font-size: 12px; font-weight: 800; color: #CBD5E1; flex-shrink: 0; }}

/* Main Content Shell: Mobile Column Bottom-Sheet | Desktop Split Glass */
#mainWrap {{
  flex: 1 1 auto; min-height: 0; width: 100%; display: flex; flex-direction: column; overflow: hidden;
}}
@media (min-width: 920px) {{
  #mainWrap {{ flex-direction: row; padding: 0 14px 14px; gap: 14px; max-width: 1400px; margin: 0 auto; }}
}}

/* Stage Bench */
#stageArea {{
  position: relative; flex: 0 0 clamp(200px, 34dvh, 310px); min-height: 185px; width: 100%;
  overflow: hidden; background: transparent;
}}
@media (min-width: 920px) {{
  #stageArea {{
    flex: 1.18; height: auto; min-height: 0; border-radius: 26px;
    border: 1px solid var(--border); background: radial-gradient(circle at 50% 40%, #13283E 0%, #091522 70%, #060E17 100%);
  }}
}}
#canvas3d, #canvas2d {{
  position: absolute; inset: 0; width: 100%; height: 100%; display: block;
}}
#canvas3d {{ z-index: 2; }}
#canvas2d {{ z-index: 3; pointer-events: none; }}

.act-bench-horizon {{
  position: absolute; left: 0; right: 0; bottom: 0; height: 28px; z-index: 4; pointer-events: none;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.03), rgba(6, 14, 23, 0.55));
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}}
#stageHud {{
  position: absolute; top: 8px; right: 10px; left: 10px; z-index: 6; pointer-events: none;
  display: flex; justify-content: space-between; align-items: flex-start; gap: 8px; flex-wrap: wrap;
}}
.act-float-tag {{
  pointer-events: auto; background: rgba(15, 29, 46, 0.85); backdrop-filter: blur(8px);
  border: 1px solid rgba(var(--accent-rgb), 0.35); color: #E2E8F0; font-size: 11px; font-weight: 700;
  padding: 5px 11px; border-radius: 12px; max-width: 100%;
}}
#liveFormulaHud {{
  position: absolute; bottom: 10px; right: 10px; left: 10px; z-index: 6; pointer-events: none;
  display: flex; justify-content: space-between; align-items: center; gap: 6px; flex-wrap: wrap;
}}
.formula-badge {{
  background: rgba(15, 29, 46, 0.88); backdrop-filter: blur(8px);
  border: 1px solid rgba(var(--accent-rgb), 0.4); border-radius: 10px;
  padding: 5px 11px; font-size: 11.5px; font-weight: 800; color: var(--accent);
  direction: rtl; max-width: 100%; overflow-wrap: anywhere;
}}
.act-complete-badge {{
  display: none; position: absolute; top: 14px; left: 16px; z-index: 8;
  width: 52px; height: 52px; border-radius: 50%;
  background: linear-gradient(135deg, #10B981, #059669);
  box-shadow: 0 0 0 8px rgba(16, 185, 129, 0.16), 0 10px 24px rgba(5, 150, 105, 0.45);
  align-items: center; justify-content: center; font-size: 26px; color: #FFFFFF; font-weight: 900;
}}
.act-complete-badge.show {{ display: flex; }}

/* Rounded Dark-Navy Control Sheet (#0F1D2E) */
#sidePanel {{
  flex: 1 1 auto; min-height: 0; background: var(--sheet-bg);
  border-top: 1px solid var(--border); border-radius: 28px 28px 0 0;
  box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.38);
  display: flex; flex-direction: column; overflow: hidden; z-index: 10;
}}
@media (min-width: 920px) {{
  #sidePanel {{
    flex: 0.92; border-radius: 26px; border: 1px solid var(--border);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.32);
  }}
}}
.sheet-handle {{
  width: 42px; height: 4px; border-radius: 99px; background: rgba(255, 255, 255, 0.18);
  margin: 8px auto 4px; flex-shrink: 0;
}}
@media (min-width: 920px) {{ .sheet-handle {{ display: none; }} }}

.panel-tabs {{
  display: flex; gap: 6px; padding: 6px 14px 8px; flex-shrink: 0;
}}
.tab-btn {{
  flex: 1; padding: 8px 6px; border-radius: 999px; border: 1px solid rgba(255, 255, 255, 0.12);
  background: rgba(255, 255, 255, 0.05); color: #CBD5E1;
  font-size: 12.5px; font-weight: 800; cursor: pointer; font-family: inherit;
  transition: all 0.2s ease; white-space: nowrap;
}}
.tab-btn.active {{
  background: rgba(14, 165, 233, 0.18); border-color: #0EA5E9; color: #FFFFFF;
  box-shadow: 0 0 0 1px rgba(14, 165, 233, 0.35);
}}

.panel-scroll {{
  flex: 1 1 auto; min-height: 0; overflow-y: auto; -webkit-overflow-scrolling: touch;
  padding: 6px 14px calc(14px + env(safe-area-inset-bottom, 0px));
  display: flex; flex-direction: column; gap: 10px;
}}

.box-card {{
  background: rgba(255, 255, 255, 0.04); border: 1px solid var(--border); border-radius: 16px; padding: 12px;
}}
.box-title {{
  font-size: 12.5px; font-weight: 800; color: var(--accent); margin-bottom: 6px;
  display: flex; align-items: center; gap: 6px;
}}
.tools-list {{ display: flex; flex-wrap: wrap; gap: 6px; }}
.tool-chip {{
  background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(var(--accent-rgb), 0.35);
  color: #E2E8F0; padding: 5px 10px; border-radius: 999px; font-size: 11.5px; font-weight: 700;
}}

.step-card {{
  background: rgba(255, 255, 255, 0.04); border: 1.5px solid rgba(255, 255, 255, 0.10);
  border-radius: 16px; padding: 12px; cursor: pointer; transition: all 0.2s ease;
}}
.step-card:hover {{ border-color: rgba(14, 165, 233, 0.5); }}
.step-card.active {{
  background: rgba(14, 165, 233, 0.12); border-color: #0EA5E9;
  box-shadow: 0 4px 16px rgba(14, 165, 233, 0.16);
}}
.step-card.done {{ border-right: 4px solid #10B981; }}
.step-head {{ font-size: 13.5px; font-weight: 800; color: #FFFFFF; margin-bottom: 4px; }}
.step-desc {{ font-size: 12.5px; color: #CBD5E1; line-height: 1.6; }}
.obs-box {{
  margin-top: 8px; padding: 8px 10px; border-radius: 10px;
  background: rgba(16, 185, 129, 0.14); border: 1px solid rgba(16, 185, 129, 0.42);
  color: #A7F3D0; font-size: 12.5px; line-height: 1.55;
}}

.act-eq-box {{
  background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 14px; padding: 10px 12px; text-align: center;
  font-size: 14px; font-weight: 800; color: #FFFFFF; direction: rtl; overflow-wrap: anywhere;
}}

.act-dual-row {{ display: flex; gap: 8px; flex-wrap: wrap; }}
.act-ghost-pill {{
  flex: 1; min-width: 110px; background: rgba(255, 255, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.14); color: #F1F5F9;
  border-radius: 999px; padding: 10px 12px; font-size: 13px; font-weight: 700;
  cursor: pointer; font-family: inherit;
}}
.act-primary-cta {{
  position: sticky; bottom: 0; z-index: 5; flex-shrink: 0;
  width: 100%; height: 48px; border-radius: 999px; border: none;
  background: linear-gradient(135deg, #10B981, #059669); color: #FFFFFF;
  font-size: 15px; font-weight: 800; cursor: pointer; font-family: inherit;
  box-shadow: 0 -6px 18px 6px #0F1D2E, 0 8px 22px rgba(5, 150, 105, 0.38);
  display: flex; align-items: center; justify-content: center; gap: 8px;
}}

.ctrl-row {{
  margin-bottom: 10px; background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.10); border-radius: 14px; padding: 10px 12px;
}}
.ctrl-label {{
  display: flex; justify-content: space-between; font-size: 12.5px; font-weight: 700;
  margin-bottom: 6px; color: #E2E8F0; gap: 8px;
}}
input[type=range].lab-slider {{ width: 100%; accent-color: #10B981; cursor: pointer; }}

.quiz-opt {{
  width: 100%; text-align: right; background: rgba(255, 255, 255, 0.06); color: #F8FAFC;
  border: 1px solid rgba(255, 255, 255, 0.14); border-radius: 999px; padding: 11px 16px;
  font-size: 13px; font-weight: 700; cursor: pointer; font-family: inherit; margin-bottom: 8px;
  transition: all 0.2s ease;
}}
.quiz-opt.correct {{ background: #059669; border-color: #10B981; color: #FFFFFF; }}
.quiz-opt.wrong {{ background: #B91C1C; border-color: #EF4444; color: #FFFFFF; }}

/* More Menu Bottom Sheet (#actMoreBackdrop) */
.act-more-backdrop {{
  display: none; position: fixed; inset: 0; background: rgba(3, 8, 15, 0.68);
  z-index: 300; align-items: flex-end; justify-content: center;
}}
.act-more-backdrop.open {{ display: flex; }}
.act-more-sheet {{
  width: 100%; max-width: 560px; max-height: min(80dvh, 580px); overflow-y: auto;
  background: #0F1D2E; border-top: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 28px 28px 0 0; padding: 10px 18px calc(24px + env(safe-area-inset-bottom, 0px));
  box-shadow: 0 -16px 40px rgba(0, 0, 0, 0.55);
}}
.act-more-handle {{ width: 42px; height: 4px; border-radius: 99px; background: rgba(255, 255, 255, 0.22); margin: 0 auto 10px; }}
.act-more-sec-title {{ font-size: 12px; font-weight: 800; color: #94A3B8; padding: 6px 4px; }}
.act-more-item {{
  width: 100%; background: transparent; border: none; border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  color: #F8FAFC; padding: 11px 4px; font-size: 13.5px; font-weight: 700; cursor: pointer;
  display: flex; align-items: center; justify-content: space-between; gap: 10px;
  text-align: right; font-family: inherit;
}}
.act-more-item:last-child {{ border-bottom: none; }}
.act-more-divider {{ height: 1px; background: rgba(255, 255, 255, 0.1); margin: 8px 0; }}
"""


def build_v3_lab_body_html(header_title, book_back_label="إلى الكتاب"):
    return f"""
<div class="act-shell">
  <div class="act-head-wrap">
    <div class="act-top-bar">
      <button class="act-sq-btn" onclick="goBack()" title="{book_back_label}">◀</button>
      <div class="act-header-meta">
        <div class="act-title" id="hudTitle">{header_title}</div>
        <div class="act-sub-row">
          <span class="act-sub" id="actSubUnit">مختبر تفاعلي 3D</span>
          <button type="button" class="act-exp-pill" onclick="toggleLabMoreMenu(true)">تبديل التجربة ▾</button>
        </div>
      </div>
      <button class="act-sq-btn" onclick="toggleLabMoreMenu(true)" title="قائمة التجارب والخيارات">···</button>
    </div>
    <div class="act-seg-row">
      <div class="act-seg-bars" id="actSegBars"></div>
      <span class="act-seg-count" id="actStepBadge">1/3</span>
    </div>
    <select id="expSelect" onchange="selectExperiment(this.value)"></select>
  </div>

  <div id="mainWrap">
    <div id="stageArea">
      <canvas id="canvas3d"></canvas>
      <canvas id="canvas2d"></canvas>
      <div id="stageHud">
        <div class="act-float-tag" id="hudSubtitle">🔄 اسحب للدوران 360° • نفّذ الخطوات أو عدّل المتغيرات</div>
      </div>
      <div class="act-complete-badge" id="actCompleteBadge">✓</div>
      <div id="liveFormulaHud">
        <div class="formula-badge" id="hudFormula"></div>
        <div class="formula-badge" id="hudReadout" style="background:rgba(16,185,129,0.22); border-color:#10B981; color:#A7F3D0;"></div>
      </div>
      <div class="act-bench-horizon"></div>
    </div>

    <aside id="sidePanel">
      <div class="sheet-handle"></div>
      <div class="panel-tabs">
        <button class="tab-btn active" id="tabSteps" onclick="switchTab('steps')">📋 الخطوات</button>
        <button class="tab-btn" id="tabControls" onclick="switchTab('controls')">🎛️ المتغيرات</button>
        <button class="tab-btn" id="tabQuiz" onclick="switchTab('quiz')">📝 اختبر فهمك</button>
      </div>

      <div class="panel-scroll" id="paneSteps" style="overflow:hidden; padding:0;">
        <div style="flex:1 1 auto; min-height:0; overflow-y:auto; -webkit-overflow-scrolling:touch; padding:6px 14px 10px; display:flex; flex-direction:column; gap:10px;">
          <div class="box-card">
            <div class="box-title">🧰 الأدوات والمواد <span id="stepBookPage" style="color:#94A3B8;"></span></div>
            <div class="tools-list" id="toolsContainer"></div>
          </div>
          <div id="stepsContainer" style="display:flex; flex-direction:column; gap:8px;"></div>
          <div class="act-eq-box" id="stepFormulaBox"></div>
          <div class="box-card" style="border-color:rgba(251,191,36,0.38); background:rgba(251,191,36,0.08);">
            <div class="box-title" style="color:#FBBF24;">💡 الاستنتاج العلمي</div>
            <div id="conclusionText" style="font-size:12.5px; line-height:1.65; color:#FEF3C7;"></div>
          </div>
          <div class="act-dual-row">
            <button class="act-ghost-pill" onclick="resetExperiment()">↺ إعادة التجربة</button>
            <button class="act-ghost-pill" onclick="goBack()">📖 {book_back_label}</button>
          </div>
        </div>
        <div style="flex:0 0 auto; padding:8px 14px calc(12px + env(safe-area-inset-bottom, 0px)); background:#0F1D2E; border-top:1px solid rgba(255,255,255,0.07);">
          <button class="act-primary-cta" id="btnNextStepCta" onclick="nextStepInteractive()" style="position:static; box-shadow:0 8px 22px rgba(5,150,105,0.35);">▶ نفّذ الخطوة التالية &nbsp;‹</button>
        </div>
      </div>

      <div class="panel-scroll" id="paneControls" style="display:none;">
        <div class="box-card">
          <div class="box-title">🎛️ ضبط المتغيرات المباشرة</div>
          <div id="slidersContainer"></div>
        </div>
        <div class="box-card" style="border-color:rgba(16,185,129,0.38);">
          <div class="box-title" style="color:#34D399;">📊 القراءات العلمية اللحظية</div>
          <div id="detailedReadout" style="font-size:13px; line-height:1.8; color:#E2E8F0;"></div>
        </div>
      </div>

      <div class="panel-scroll" id="paneQuiz" style="display:none;">
        <div class="box-card">
          <div class="box-title">📝 سؤال التحقق من فهم النشاط</div>
          <div id="quizPrompt" style="font-size:14.5px; font-weight:800; margin:6px 0 12px; line-height:1.6; color:#FFFFFF;"></div>
          <div id="quizOptions"></div>
          <div id="quizFeedback" style="display:none; margin-top:8px; padding:10px; border-radius:12px; font-size:13px; line-height:1.6;"></div>
        </div>
      </div>
    </aside>
  </div>
</div>

<div id="actMoreBackdrop" class="act-more-backdrop" onclick="if(event.target===this)toggleLabMoreMenu(false)">
  <div class="act-more-sheet">
    <div class="act-more-handle"></div>
    <div class="act-more-sec-title">جميع أنشطة وتجارب المنهج (18 نشاطاً)</div>
    <div id="actMoreList"></div>
    <div class="act-more-divider"></div>
    <div class="act-more-sec-title">خيارات</div>
    <button class="act-more-item" onclick="toggleLabMoreMenu(false); resetExperiment();">
      <span>↺ إعادة ضبط التجربة</span><span style="color:#94A3B8;">›</span>
    </button>
    <button class="act-more-item" onclick="toggleLabMoreMenu(false); switchTab('controls');">
      <span>🎛️ تعديل المتغيرات الحية</span><span style="color:#38BDF8;">›</span>
    </button>
    <button class="act-more-item" onclick="toggleLabMoreMenu(false); goBack();">
      <span>📖 العودة لصفحة الكتاب</span><span style="color:#10B981;">›</span>
    </button>
  </div>
</div>
"""


def build_v3_lab_controller_js(exp_array_name, return_book_html):
    return f"""
function toggleLabMoreMenu(show) {{
  const el = document.getElementById('actMoreBackdrop');
  if (el) el.classList.toggle('open', !!show);
}}

function renderMoreDrawerExps() {{
  const listEl = document.getElementById('actMoreList');
  if (!listEl) return;
  listEl.innerHTML = {exp_array_name}.map((e, i) => {{
    const active = curExp && e.id === curExp.id;
    return `<button class="act-more-item" onclick="toggleLabMoreMenu(false); selectExperiment('${{e.id}}');">
      <span style="overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${{i + 1}}. ${{e.title}} <span style="color:#94A3B8;font-size:11px;">(ص ${{e.bookPage}})</span></span>
      <span style="color:#10B981; font-weight:900; flex-shrink:0;">${{active ? '✓' : ''}}</span>
    </button>`;
  }}).join('');
}}

function updateSegProgressUI() {{
  const total = Math.max(1, (curExp?.steps || []).length);
  const barsEl = document.getElementById('actSegBars');
  if (barsEl) {{
    barsEl.innerHTML = (curExp?.steps || []).map((_, idx) => {{
      const cls = idx < curStepIdx ? 'done' : (idx === curStepIdx ? 'active' : '');
      return `<div class="act-seg ${{cls}}" onclick="activateStep(${{idx}})"></div>`;
    }}).join('');
  }}
  const badge = document.getElementById('actStepBadge');
  if (badge) badge.textContent = `${{curStepIdx + 1}}/${{total}}`;
  const chk = document.getElementById('actCompleteBadge');
  if (chk) chk.classList.toggle('show', curStepIdx >= total - 1);
  const cta = document.getElementById('btnNextStepCta');
  if (cta) {{
    cta.innerHTML = curStepIdx < total - 1
      ? '▶ نفّذ الخطوة التالية &nbsp;‹'
      : '📝 اختبر فهمك في هذه التجربة &nbsp;‹';
  }}
}}

function selectExperiment(id) {{
  curExp = {exp_array_name}.find(e => e.id === id) || {exp_array_name}[0];
  const sel = document.getElementById('expSelect');
  if (sel) sel.value = curExp.id;
  curStepIdx = 0;
  params = {{}};
  (curExp.controls || []).forEach(c => params[c.id] = c.default);

  const expNum = {exp_array_name}.indexOf(curExp) + 1;
  document.getElementById('hudTitle').textContent = curExp.title;
  const subUnit = document.getElementById('actSubUnit');
  if (subUnit) subUnit.textContent = `${{curExp.unitTitle}} · نشاط ${{expNum}} من ${{{exp_array_name}.length}} · ص ${{curExp.bookPage}}`;
  document.getElementById('hudFormula').textContent = '⚖️ ' + curExp.formula;
  const stepF = document.getElementById('stepFormulaBox');
  if (stepF) stepF.textContent = curExp.formula;
  document.getElementById('stepBookPage').textContent = '(ص ' + curExp.bookPage + ')';
  document.getElementById('toolsContainer').innerHTML = (curExp.tools || []).map(t => `<span class="tool-chip">${{t}}</span>`).join('');
  document.getElementById('conclusionText').textContent = curExp.conclusion;

  renderSliders();
  renderSteps();
  renderQuiz();
  renderMoreDrawerExps();
  build3dForExperiment();
  updateReadout();
  updateSegProgressUI();
}}

function renderSliders() {{
  document.getElementById('slidersContainer').innerHTML = (curExp.controls || []).map(c => `
    <div class="ctrl-row">
      <div class="ctrl-label">
        <span>${{c.label}}</span>
        <span id="lbl_${{c.id}}" style="color:var(--accent); font-family:monospace;">${{params[c.id]}}</span>
      </div>
      <input type="range" class="lab-slider" id="rng_${{c.id}}" min="${{c.min}}" max="${{c.max}}" step="${{c.step}}" value="${{params[c.id]}}"
        oninput="onParamChange('${{c.id}}', parseFloat(this.value))">
    </div>
  `).join('');
}}

function onParamChange(id, val) {{
  params[id] = val;
  const lbl = document.getElementById('lbl_' + id);
  if (lbl) lbl.textContent = val;
  updateReadout();
}}

function updateReadout() {{
  const res = computeSimulationResults();
  document.getElementById('hudReadout').textContent = res.short;
  document.getElementById('detailedReadout').innerHTML = res.detail;
}}

function renderSteps() {{
  const container = document.getElementById('stepsContainer');
  container.innerHTML = curExp.steps.map((s, idx) => `
    <div class="step-card ${{idx === curStepIdx ? 'active' : (idx < curStepIdx ? 'done' : '')}}" onclick="activateStep(${{idx}})">
      <div class="step-head">${{idx < curStepIdx ? '✅ ' : (idx === curStepIdx ? '▶️ ' : '⭕ ')}} ${{s.title}}</div>
      <div class="step-desc">${{s.desc}}</div>
      ${{idx <= curStepIdx ? `<div class="obs-box"><b>🔍 الملاحظة:</b> ${{s.obs}}</div>` : ''}}
    </div>
  `).join('');
}}

function activateStep(idx) {{
  curStepIdx = Math.max(0, Math.min(curExp.steps.length - 1, idx));
  const step = curExp.steps[curStepIdx];
  if (step && step.params) {{
    Object.entries(step.params).forEach(([k, v]) => {{
      params[k] = v;
      const rng = document.getElementById('rng_' + k);
      const lbl = document.getElementById('lbl_' + k);
      if (rng) rng.value = v;
      if (lbl) lbl.textContent = v;
    }});
  }}
  renderSteps();
  updateReadout();
  updateSegProgressUI();
}}

function nextStepInteractive() {{
  if (curStepIdx < curExp.steps.length - 1) {{
    activateStep(curStepIdx + 1);
  }} else {{
    switchTab('quiz');
  }}
}}

function resetExperiment() {{
  switchTab('steps');
  activateStep(0);
}}

function renderQuiz() {{
  const q = curExp.quiz;
  document.getElementById('quizPrompt').textContent = q.q;
  document.getElementById('quizFeedback').style.display = 'none';
  document.getElementById('quizOptions').innerHTML = q.options.map((opt, i) => `
    <button class="quiz-opt" onclick="checkQuiz(${{i}})">${{['أ','ب','ج','د'][i]}}. ${{opt}}</button>
  `).join('');
}}

function checkQuiz(idx) {{
  const q = curExp.quiz;
  const btns = document.querySelectorAll('#quizOptions .quiz-opt');
  const fb = document.getElementById('quizFeedback');
  btns.forEach(b => b.classList.remove('correct', 'wrong'));
  if (idx === q.answer) {{
    btns[idx].classList.add('correct');
    fb.style.display = 'block';
    fb.style.background = 'rgba(16,185,129,0.2)';
    fb.style.color = '#A7F3D0';
    fb.innerHTML = '🎉 <b>إجابة صحيحة!</b><br>' + q.explain;
  }} else {{
    btns[idx].classList.add('wrong');
    btns[q.answer].classList.add('correct');
    fb.style.display = 'block';
    fb.style.background = 'rgba(239,68,68,0.2)';
    fb.style.color = '#FECACA';
    fb.innerHTML = '❌ <b>غير صحيح.</b> ' + q.explain;
  }}
}}

function switchTab(t) {{
  document.getElementById('paneSteps').style.display = t === 'steps' ? 'flex' : 'none';
  document.getElementById('paneControls').style.display = t === 'controls' ? 'flex' : 'none';
  document.getElementById('paneQuiz').style.display = t === 'quiz' ? 'flex' : 'none';
  document.getElementById('tabSteps').classList.toggle('active', t === 'steps');
  document.getElementById('tabControls').classList.toggle('active', t === 'controls');
  document.getElementById('tabQuiz').classList.toggle('active', t === 'quiz');
}}

const labUrlParams = (window.location.search + '&' + window.location.hash);
const labPageMatch = labUrlParams.match(/page=(\\d+)/);
const labReturnPage = labPageMatch ? labPageMatch[1] : '';

function goBack() {{
  if (labUrlParams.includes('from=book')) {{
    window.location.href = labReturnPage ? `{return_book_html}?restore=1&page=${{labReturnPage}}` : `{return_book_html}?restore=1`;
  }} else if (document.referrer && document.referrer.includes('{return_book_html.replace(".html", "")}')) {{
    window.history.back();
  }} else if (window.ThakerBridge && window.ThakerBridge.returnToHome) {{
    window.ThakerBridge.returnToHome();
  }} else {{
    window.location.href = `{return_book_html}?restore=1`;
  }}
}}

window.addEventListener('DOMContentLoaded', () => {{
  const sel = document.getElementById('expSelect');
  if (sel) sel.innerHTML = {exp_array_name}.map(e => `<option value="${{e.id}}">${{e.unitTitle.split(':')[0]}}: ${{e.title}}</option>`).join('');
  init3D();
  const m = labUrlParams.match(/exp=([a-zA-Z0-9_-]+)/);
  selectExperiment(m ? m[1] : {exp_array_name}[0].id);
  animateLoop();
}});
"""
