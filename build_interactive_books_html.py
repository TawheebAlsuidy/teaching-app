#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compiler for Standalone Physics & Biology Interactive Textbooks (v2.0 Full Interactive Engine)
Generates:
1. physics-12th-book.html
2. biology-12th-book.html
"""
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ACTIVITY_MODAL_HTML = """
<!-- Grade 12 Guided Interactive Simulator Modal (Dark-Navy Design Matching تصاميم التجارب) -->
<style id="g12-lab-modal-responsive">
#g12ActivityModal { height: 100dvh; max-height: 100dvh; overflow: hidden; }
#g12ActivityModal .g12-lab-head { flex: 0 0 auto; }
#g12ActivityModal .g12-lab-stage { flex: 1 1 auto; min-height: 0; min-width: 0; }
#g12ActivityModal .g12-lab-sheet {
  flex: 0 0 auto; min-height: 0; max-height: min(52dvh, 460px);
  overflow-y: auto; -webkit-overflow-scrolling: touch;
}
#g12ActivityModal #actVisualStage { width: 100%; max-width: 100%; min-width: 0; overflow-wrap: anywhere; }
#g12ActivityModal #actControlsContainer > div { min-width: 0; }
#g12ActivityModal #g12MainCtaBtn {
  position: sticky; bottom: 0; z-index: 2; flex-shrink: 0;
  box-shadow: 0 -6px 18px 6px #0F1D2E, 0 8px 20px rgba(5,150,105,0.35);
}
#g12MoreBackdrop > div { max-height: min(75dvh, 560px); padding-bottom: calc(24px + env(safe-area-inset-bottom, 0px)); }
@media (max-width: 480px) {
  #g12ActivityModal .g12-lab-head { padding: 10px 10px 6px; }
  #g12ActivityModal .g12-lab-head button { width: 38px; height: 38px; }
  #g12ActivityModal .g12-lab-stage { padding: 8px 10px 6px; }
  #g12ActivityModal .g12-lab-sheet {
    max-height: 58dvh;
    padding: 12px 12px calc(16px + env(safe-area-inset-bottom, 0px));
  }
  #g12ActivityModal #g12BottomStepTitle { font-size: 17px; }
  #g12ActivityModal #actModalDesc { font-size: 12.5px; }
}
@media (max-height: 640px) {
  #g12ActivityModal .g12-lab-sheet { max-height: 64dvh; }
}
</style>
<div id="g12ActivityModal" style="display:none; position:fixed; inset:0; height:100dvh; max-height:100dvh; background:radial-gradient(circle at 50% 22%, #13283E 0%, #091522 60%, #060E17 100%); z-index:960; color:#F8FAFC; overflow:hidden; align-items:center; justify-content:center;">
  <div class="g12-lab-shell" style="width:100%; max-width:580px; height:100%; min-height:0; margin:0 auto; display:flex; flex-direction:column;">
    <div class="g12-lab-head" style="flex:0 0 auto;">
      <div style="display:flex; justify-content:space-between; align-items:center; padding:12px 12px 6px; gap:10px;">
        <button class="act-circle-btn" style="width:42px; height:42px; border-radius:13px; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.1); color:#fff; font-size:18px; cursor:pointer;" onclick="closeActivityModal()">✕</button>
        <div style="text-align:center; flex:1; min-width:0;">
          <div id="actModalTitle" style="font-size:17px; font-weight:800; color:#FFFFFF; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">المختبر التفاعلي</div>
          <div id="g12ActSubTitle" style="font-size:12px; color:#94A3B8; margin-top:2px;">محاكاة علمية · التفاعل المباشر</div>
        </div>
        <button class="act-circle-btn" style="width:42px; height:42px; border-radius:13px; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.1); color:#fff; font-size:18px; cursor:pointer;" onclick="toggleG12MoreMenu(true)">···</button>
      </div>
      <div style="display:flex; align-items:center; gap:6px; padding:6px 12px 4px;">
        <div style="flex:1; display:flex; gap:6px;">
          <div id="g12Seg1" onclick="setG12Step(1)" style="flex:1; height:4.5px; border-radius:99px; background:#0EA5E9; cursor:pointer;"></div>
          <div id="g12Seg2" onclick="setG12Step(2)" style="flex:1; height:4.5px; border-radius:99px; background:rgba(255,255,255,0.14); cursor:pointer;"></div>
          <div id="g12Seg3" onclick="setG12Step(3)" style="flex:1; height:4.5px; border-radius:99px; background:rgba(255,255,255,0.14); cursor:pointer;"></div>
        </div>
        <span id="g12StepCounter" style="font-size:12px; font-weight:700; color:#94A3B8;">1/3</span>
      </div>
    </div>

    <div class="g12-lab-stage" style="position:relative; flex:1 1 auto; min-height:0; min-width:0; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:10px 12px 6px; overflow:hidden;">
      <div id="actVisualStage" style="width:100%; color:#f8fafc; text-align:center;"></div>
      <div id="g12DoneCheckBadge" style="display:none; width:64px; height:64px; border-radius:50%; background:linear-gradient(135deg,#10B981,#059669); box-shadow:0 0 0 10px rgba(16,185,129,0.16); align-items:center; justify-content:center; font-size:30px; color:#fff; font-weight:900; margin-top:12px;">✓</div>
      <div style="position:absolute; left:0; right:0; bottom:0; height:26px; background:linear-gradient(180deg, rgba(255,255,255,0.03), rgba(6,14,23,0.4)); border-top:1px solid rgba(255,255,255,0.08); pointer-events:none;"></div>
    </div>

    <div class="g12-lab-sheet" style="background:#0F1D2E; border-top:1px solid rgba(255,255,255,0.08); border-radius:28px 28px 0 0; padding:14px 14px calc(16px + env(safe-area-inset-bottom, 0px)); display:flex; flex-direction:column; flex:0 0 auto; min-height:0; gap:10px; max-height:min(52dvh, 460px); overflow-y:auto; -webkit-overflow-scrolling:touch; box-shadow:0 -10px 30px rgba(0,0,0,0.35);">
      <h4 id="g12BottomStepTitle" style="margin:0; font-size:19px; font-weight:800; color:#FFFFFF;">اضبط المتغيرات ولاحظ النتيجة</h4>
      <p id="actModalDesc" style="margin:0; font-size:13px; color:#94A3B8; line-height:1.6;"></p>
      <div id="actControlsContainer" style="display:flex; flex-direction:column; gap:8px;"></div>
      <div id="actReadoutBox" style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.12); border-radius:16px; padding:12px 14px; font-size:13px; line-height:1.7; color:#E2E8F0; display:none;"></div>
      <div id="g12DualBtns" style="display:none; gap:8px; flex-wrap:wrap;">
        <button onclick="setG12Step(1)" style="flex:1; min-width:110px; background:rgba(255,255,255,0.07); border:1px solid rgba(255,255,255,0.12); color:#F1F5F9; border-radius:999px; padding:10px; font-weight:700; cursor:pointer; font-family:inherit;">🔁 تعديل القيم</button>
        <button onclick="openDedicatedLabForPage()" style="flex:1.2; min-width:140px; background:rgba(14,165,233,0.18); border:1px solid rgba(56,189,248,0.45); color:#7DD3FC; border-radius:999px; padding:10px; font-weight:800; cursor:pointer; font-family:inherit;">🔬 المعمل الكامل (خطوات)</button>
        <button onclick="closeActivityModal()" style="flex:1; min-width:110px; background:rgba(255,255,255,0.07); border:1px solid rgba(255,255,255,0.12); color:#F1F5F9; border-radius:999px; padding:10px; font-weight:700; cursor:pointer; font-family:inherit;">📖 إلى صفحة الكتاب</button>
      </div>
      <button id="g12MainCtaBtn" onclick="advanceG12Step()" style="width:100%; height:50px; border-radius:999px; border:none; background:linear-gradient(135deg,#10B981,#059669); color:#fff; font-size:15.5px; font-weight:800; cursor:pointer; box-shadow:0 8px 20px rgba(5,150,105,0.35); font-family:inherit;">شغّل المحاكاة &nbsp;‹</button>
    </div>
  </div>
</div>

<div id="g12MoreBackdrop" style="display:none; position:fixed; inset:0; background:rgba(3,8,15,0.68); z-index:980; align-items:flex-end; justify-content:center;" onclick="if(event.target===this)toggleG12MoreMenu(false)">
  <div style="width:100%; max-width:580px; max-height:75vh; overflow-y:auto; background:#0F1D2E; border-top:1px solid rgba(255,255,255,0.1); border-radius:28px 28px 0 0; padding:10px 18px 24px; color:#F8FAFC;">
    <div style="width:42px; height:4px; border-radius:99px; background:rgba(255,255,255,0.22); margin:0 auto 10px;"></div>
    <div style="font-size:12.5px; font-weight:700; color:#94A3B8; padding:6px 4px;">أنشطة المحاكاة التفاعلية</div>
    <div id="g12MoreActivitiesList"></div>
    <div style="height:1px; background:rgba(255,255,255,0.1); margin:8px 0;"></div>
    <button onclick="toggleG12MoreMenu(false); openDedicatedLabForPage();" style="width:100%; background:rgba(16,185,129,0.14); border:1px solid rgba(16,185,129,0.35); border-radius:12px; color:#34D399; padding:11px 12px; font-size:14px; font-weight:800; text-align:right; cursor:pointer; font-family:inherit; margin-bottom:6px;">🔬 فتح معمل الأنشطة والخطوات الكامل 3D ‹</button>
    <button onclick="toggleG12MoreMenu(false); setG12Step(1);" style="width:100%; background:transparent; border:none; color:#F8FAFC; padding:12px 4px; font-size:14.5px; font-weight:700; text-align:right; cursor:pointer; font-family:inherit;">↺ إعادة الضبط للخطوة الأولى</button>
    <button onclick="toggleG12MoreMenu(false); closeActivityModal();" style="width:100%; background:transparent; border:none; color:#F8FAFC; padding:12px 4px; font-size:14.5px; font-weight:700; text-align:right; cursor:pointer; font-family:inherit;">📖 العودة لصفحة الكتاب</button>
  </div>
</div>
"""

INTERACTIVE_ENGINE_JS = """
// ========================================================
// GRADE 12 FULL INTERACTIVE ENGINE (ACTIVITIES, 3D & QUIZZES)
// ========================================================
function getCurrentPageContext() {
  const p = PAGES[state.curPageIdx] || PAGES[0] || {};
  const uid = p.unit_id || 'u1';
  const bp = p.book_page || 10;
  const matchedLesson = LESSONS.find(l => l.unitId === uid && l.pages && bp >= l.pages[0] && bp <= l.pages[l.pages.length - 1])
    || LESSONS.find(l => l.unitId === uid)
    || LESSONS[0];
  const lid = matchedLesson ? matchedLesson.id : '';
  const spots = INTERACTIONS[p.page_id] || [];
  const expSpot = spots.find(s => s.type === 'explainable_text');
  const actSpot = spots.find(s => s.type === 'activity');
  const diagSpot = spots.find(s => s.type === 'interactive_3d');
  const quizSpot = spots.find(s => s.type === 'assessment');
  return {
    page: p,
    unitId: uid,
    expRef: (expSpot && expSpot.explanation_ref) || ('exp-' + lid) || Object.keys(EXPLANATIONS)[0],
    actRef: (actSpot && actSpot.activity_ref) || Object.keys(ACTIVITIES).find(k => k.endsWith(uid)) || Object.keys(ACTIVITIES)[0],
    diagRef: (diagSpot && diagSpot.diagram_ref) || Object.keys(DIAGRAMS)[0],
    quizRef: (quizSpot && quizSpot.assessment_ref) || Object.keys(ASSESSMENTS).find(k => k.endsWith(uid)) || Object.keys(ASSESSMENTS)[0]
  };
}

function openCurrentPageExplanation() {
  const ctx = getCurrentPageContext();
  if (ctx.expRef && EXPLANATIONS[ctx.expRef]) openTextExplanation(ctx.expRef);
  else showToast('لا يوجد شرح مضاف لهذه الصفحة التمهيدية، انتقل لوحدة دراسية');
}

function openCurrentPageActivity() {
  const ctx = getCurrentPageContext();
  if (ctx.actRef && ACTIVITIES[ctx.actRef]) openActivityModal(ctx.actRef);
  else showToast('اختر صفحة من الوحدات الدراسية لتشغيل النشاط التفاعلي');
}

function openCurrentPage3d() {
  const ctx = getCurrentPageContext();
  if (ctx.diagRef && DIAGRAMS[ctx.diagRef]) openLab3d(ctx.diagRef);
  else showToast('اختر صفحة من الوحدات الدراسية لعرض المجسم ثلاثي الأبعاد');
}

function openCurrentPageQuiz() {
  const ctx = getCurrentPageContext();
  if (ctx.quizRef && ASSESSMENTS[ctx.quizRef]) openAssessmentModal(ctx.quizRef);
  else showToast('اختر صفحة من الوحدات الدراسية لبدء اختبار اختبر نفسك');
}

// Override handleHotspotClick to support activities natively
handleHotspotClick = function(item) {
  playClickSound();
  if (item.type === 'explainable_text' || item.type === 'title') {
    openTextExplanation(item.explanation_ref);
  } else if (item.type === 'interactive_3d') {
    openLab3d(item.diagram_ref);
  } else if (item.type === 'activity') {
    openActivityModal(item.activity_ref);
  } else if (item.type === 'assessment') {
    openAssessmentModal(item.assessment_ref);
  }
};

function getUnitDefaultExpForPage(p) {
  const spots = INTERACTIONS[p?.page_id] || [];
  const actSpot = spots.find(s => s.type === 'activity' && s.activity_ref);
  if (actSpot) {
    if (actSpot.lab_exp) return actSpot.lab_exp;
    const actObj = ACTIVITIES[actSpot.activity_ref];
    if (actObj && actObj.lab_exp) return actObj.lab_exp;
    if (BOOK_SUBJECT_KEY !== 'chemistry') return actSpot.activity_ref;
  }
  const diagSpot = spots.find(s => s.type === 'interactive_3d' && (s.lab_exp || (s.diagram_ref && DIAGRAMS[s.diagram_ref]?.lab_exp)));
  if (diagSpot) return diagSpot.lab_exp || DIAGRAMS[diagSpot.diagram_ref].lab_exp;
  if (BOOK_SUBJECT_KEY === 'chemistry') {
    const uObj = (UNITS || []).find(u => u.id === p?.unit_id);
    if (uObj && uObj.lab_id) return uObj.lab_id;
    return '';
  }
  const uid = p?.unit_id || 'u1';
  const unitDiag = Object.values(DIAGRAMS).find(d => d.lab_exp && (d.id.includes(uid) || d.lab_exp.includes(uid)));
  if (unitDiag) return unitDiag.lab_exp;
  const labAct = Object.values(ACTIVITIES).find(a => a.lab_url && a.id.includes(uid));
  return labAct ? labAct.id : '';
}

function openDedicatedLabForPage(explicitExpId) {
  const p = PAGES[state.curPageIdx] || PAGES[0] || {};
  const expId = explicitExpId || getUnitDefaultExpForPage(p);
  const bp = p.book_page || '';
  if (BOOK_LAB_HTML === 'chem-lab-book.html') {
    let hashParts = ['from=book'];
    if (expId) hashParts.push('exp=' + encodeURIComponent(expId));
    if (bp) hashParts.push('page=' + encodeURIComponent(bp));
    window.location.href = `${BOOK_LAB_HTML}#${hashParts.join('&')}`;
    return;
  }
  let url = `${BOOK_LAB_HTML}?from=book`;
  if (expId) url += `&exp=${encodeURIComponent(expId)}`;
  if (bp) url += `&page=${encodeURIComponent(bp)}`;
  window.location.href = url;
}

function openActiveDiagInDedicatedLab() {
  const expId = curLabDiag?.lab_exp || getUnitDefaultExpForPage(PAGES[state.curPageIdx]);
  closeLab3d();
  openDedicatedLabForPage(expId);
}

openRelatedActivityFromSheet = function() {
  closeTextSheet();
  const ctx = getCurrentPageContext();
  if (ctx.actRef && ACTIVITIES[ctx.actRef]) {
    openActivityModal(ctx.actRef);
  } else {
    openDedicatedLabForPage();
  }
};

// --------------------------------------------------------
// INTERACTIVE ACTIVITY SIMULATOR MODAL & LAB ROUTER
// --------------------------------------------------------
let curActivity = null;
let curActValues = {};
let curG12Step = 1;

function openActivityModal(actRef) {
  const p = PAGES[state.curPageIdx] || PAGES[0] || {};
  const candidate = ACTIVITIES[actRef];
  if (candidate && candidate.lab_url && candidate.has_lab !== false) {
    const bp = p.book_page || candidate.book_page || '';
    if (candidate.lab_url.includes('#')) {
      const cleaned = candidate.lab_url.replace(/&?page=\\d+/g, '').replace(/[?&]$/, '');
      window.location.href = bp ? `${cleaned}&page=${encodeURIComponent(bp)}` : cleaned;
    } else {
      const sep = candidate.lab_url.includes('?') ? '&' : '?';
      window.location.href = bp ? `${candidate.lab_url}${sep}page=${encodeURIComponent(bp)}` : candidate.lab_url;
    }
    return;
  }

  const simKeys = Object.keys(ACTIVITIES).filter(k => ACTIVITIES[k] && ACTIVITIES[k].sim_type && ACTIVITIES[k].has_lab !== true);
  const unitMatchAct = Object.values(ACTIVITIES).find(a => a && a.unit_id === (p.unit_id || 'u1') && a.sim_type && a.controls && a.controls.length);
  const subjFallback = BOOK_SUBJECT_KEY === 'chemistry'
    ? unitMatchAct
    : ACTIVITIES[`act-${BOOK_SUBJECT_KEY === 'physics' ? 'phys' : 'bio'}-${p.unit_id || 'u1'}`];
  const fallback = (candidate && candidate.sim_type) ? candidate : (subjFallback || ACTIVITIES[simKeys[0]] || Object.values(ACTIVITIES)[0]);
  if (!fallback) {
    openDedicatedLabForPage(actRef);
    return;
  }
  if (!fallback.controls || fallback.controls.length === 0) {
    openDedicatedLabForPage(fallback.id || actRef);
    return;
  }
  curActivity = fallback;
  curActValues = {};
  document.getElementById('actModalTitle').textContent = fallback.title;
  const idx = Math.max(1, simKeys.indexOf(fallback.id) + 1);
  const sub = document.getElementById('g12ActSubTitle');
  if (sub) sub.textContent = `${(fallback.unit_id || p.unit_id || 'u1').toUpperCase()} · مختبر حسابي ${idx} من ${Math.max(1, simKeys.length)}`;
  document.getElementById('actModalDesc').textContent = fallback.description || '';

  const ctrlBox = document.getElementById('actControlsContainer');
  ctrlBox.innerHTML = (fallback.controls || []).map(c => {
    curActValues[c.id] = c.default;
    return `
      <div style="background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.12); border-radius:14px; padding:10px 12px;">
        <div style="display:flex; justify-content:space-between; font-size:12.5px; font-weight:700; margin-bottom:6px; color:#E2E8F0;">
          <span>${c.label}</span>
          <span id="actVal_${c.id}" style="color:#10B981; font-family:monospace; font-size:13.5px;">${c.default}</span>
        </div>
        <input type="range" min="${c.min}" max="${c.max}" step="${c.step}" value="${c.default}"
          style="width:100%; accent-color:#10B981; cursor:pointer;"
          oninput="onActivityControlChange('${c.id}', parseFloat(this.value))">
      </div>
    `;
  }).join('');

  const listEl = document.getElementById('g12MoreActivitiesList');
  if (listEl) {
    listEl.innerHTML = Object.keys(ACTIVITIES).map(k => {
      const a = ACTIVITIES[k];
      const active = (a === fallback);
      const badge = a.lab_url ? '🔬 معمل' : '🎛️ فوري';
      return `<button onclick="toggleG12MoreMenu(false); openActivityModal('${k}');" style="width:100%; background:transparent; border:none; border-bottom:1px solid rgba(255,255,255,0.06); color:#F8FAFC; padding:11px 4px; font-size:13px; font-weight:700; text-align:right; display:flex; justify-content:space-between; align-items:center; gap:8px; cursor:pointer; font-family:inherit;">
        <span style="overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${a.title}</span>
        <span style="color:${active ? '#10B981' : '#38BDF8'}; font-size:11px; flex-shrink:0;">${active ? '✓ نشط' : badge}</span>
      </button>`;
    }).join('');
  }

  document.getElementById('g12ActivityModal').style.display = 'flex';
  setG12Step(1);
  updateActivitySimulation();
}

function setG12Step(stepNum) {
  curG12Step = Math.max(1, Math.min(3, stepNum));
  const counter = document.getElementById('g12StepCounter');
  if (counter) counter.textContent = `${curG12Step}/3`;
  for (let i = 1; i <= 3; i++) {
    const seg = document.getElementById('g12Seg' + i);
    if (seg) seg.style.background = i < curG12Step ? '#10B981' : (i === curG12Step ? '#0EA5E9' : 'rgba(255,255,255,0.14)');
  }
  const h = document.getElementById('g12BottomStepTitle');
  const desc = document.getElementById('actModalDesc');
  const ctrls = document.getElementById('actControlsContainer');
  const readout = document.getElementById('actReadoutBox');
  const dual = document.getElementById('g12DualBtns');
  const badge = document.getElementById('g12DoneCheckBadge');
  const cta = document.getElementById('g12MainCtaBtn');

  if (curG12Step === 1) {
    if (h) h.textContent = '1. اضبط المتغيرات قبل التشغيل';
    if (desc) desc.style.display = 'block';
    if (ctrls) ctrls.style.display = 'flex';
    if (readout) readout.style.display = 'none';
    if (dual) dual.style.display = 'none';
    if (badge) badge.style.display = 'none';
    if (cta) cta.innerHTML = 'تشغيل المحاكاة ومشاهدة النتائج &nbsp;‹';
  } else if (curG12Step === 2) {
    if (h) h.textContent = '2. النتائج الحية والتفاعل المباشر';
    if (desc) desc.style.display = 'none';
    if (ctrls) ctrls.style.display = 'flex';
    if (readout) readout.style.display = 'block';
    if (dual) dual.style.display = 'none';
    if (badge) badge.style.display = 'none';
    if (cta) cta.innerHTML = 'الاستنتاج والربط بالمنهج &nbsp;‹';
  } else {
    if (h) h.textContent = 'أحسنت! أتممت المحاكاة بنجاح';
    if (desc) desc.style.display = 'none';
    if (ctrls) ctrls.style.display = 'none';
    if (readout) readout.style.display = 'block';
    if (dual) dual.style.display = 'flex';
    if (badge) badge.style.display = 'flex';
    if (cta) cta.innerHTML = 'اختبر نفسك في الدرس &nbsp;‹';
  }
}

function advanceG12Step() {
  if (curG12Step < 3) {
    setG12Step(curG12Step + 1);
  } else {
    closeActivityModal();
    openCurrentPageQuiz();
  }
}

function toggleG12MoreMenu(show) {
  const m = document.getElementById('g12MoreBackdrop');
  if (m) m.style.display = show ? 'flex' : 'none';
}

function closeActivityModal() {
  document.getElementById('g12ActivityModal').style.display = 'none';
  toggleG12MoreMenu(false);
}

function onActivityControlChange(id, val) {
  curActValues[id] = val;
  const lbl = document.getElementById('actVal_' + id);
  if (lbl) lbl.textContent = val;
  updateActivitySimulation();
}

function updateActivitySimulation() {
  if (!curActivity) return;
  const stage = document.getElementById('actVisualStage');
  const readout = document.getElementById('actReadoutBox');
  const st = curActivity.sim_type;
  const v = curActValues;

  if (st === 'phys_projectile_lab') {
    const v0 = v.v0 || 50, ang = v.angle || 45, g = 9.8;
    const rad = ang * Math.PI / 180;
    const T = (2 * v0 * Math.sin(rad)) / g;
    const H = (v0 * v0 * Math.pow(Math.sin(rad), 2)) / (2 * g);
    const R = (v0 * v0 * Math.sin(2 * rad)) / g;
    const maxR = (100 * 100) / g;
    const maxH = (100 * 100) / (2 * g);
    const px = Math.min(280, (R / maxR) * 260 + 20);
    const py = Math.max(15, 115 - (H / maxH) * 95);
    stage.innerHTML = `
      <svg viewBox="0 0 300 130" style="width:100%; height:140px;">
        <line x1="15" y1="115" x2="290" y2="115" stroke="#475569" stroke-width="2"/>
        <path d="M 20 115 Q ${(20+px)/2} ${py - 45} ${px} 115" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="5,3"/>
        <circle cx="20" cy="115" r="5" fill="#f59e0b"/>
        <circle cx="${(20+px)/2}" cy="${(115+py)/2 - 15}" r="4" fill="#10b981"/>
        <circle cx="${px}" cy="115" r="5" fill="#ef4444"/>
        <text x="20" y="128" fill="#cbd5e1" font-size="9">الإطلاق</text>
        <text x="${(20+px)/2 - 12}" y="${Math.max(14, (115+py)/2 - 22)}" fill="#4ade80" font-size="9">الذروة H</text>
        <text x="${px - 15}" y="128" fill="#fca5a5" font-size="9">المدى R</text>
      </svg>`;
    readout.innerHTML = `<b>📊 النتائج اللحظية:</b><br>• أقصى ارتفاع (H) = <b>${H.toFixed(2)} m</b><br>• المدى الأفقي (R) = <b>${R.toFixed(2)} m</b> ${ang === 45 ? '<span style="color:#10b981;">(أقصى مدى ممكن عند 45°!)</span>' : ''}<br>• زمن التحليق الكلي (T) = <b>${T.toFixed(2)} s</b>`;
  } else if (st === 'phys_rlc_lab') {
    const f = v.freq || 50, L = (v.L || 100) * 1e-3, C = (v.C || 100) * 1e-6, R = v.R || 20;
    const XL = 2 * Math.PI * f * L;
    const Xc = 1 / (2 * Math.PI * f * C);
    const Z = Math.sqrt(R * R + Math.pow(XL - Xc, 2));
    const f0 = 1 / (2 * Math.PI * Math.sqrt(L * C));
    const isRes = Math.abs(XL - Xc) < 3;
    stage.innerHTML = `
      <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:8px; min-height:110px; text-align:center;">
        <div style="min-width:0; max-width:46%; padding:8px; border-radius:10px; background:rgba(56,189,248,0.15); border:1px solid #38bdf8;">
          <div style="font-size:11px; color:#94a3b8;">المفاعلة الحثية XL</div>
          <div style="font-size:18px; font-weight:800; color:#38bdf8;">${XL.toFixed(1)} Ω</div>
        </div>
        <div style="font-size:22px;">${isRes ? '⚡ رنين!' : (XL > Xc ? '🔺 حثية' : '🔻 سعوية')}</div>
        <div style="min-width:0; max-width:46%; padding:8px; border-radius:10px; background:rgba(245,158,11,0.15); border:1px solid #f59e0b;">
          <div style="font-size:11px; color:#94a3b8;">المفاعلة السعوية Xc</div>
          <div style="font-size:18px; font-weight:800; color:#f59e0b;">${Xc.toFixed(1)} Ω</div>
        </div>
      </div>`;
    readout.innerHTML = `<b>📊 حسابات الدائرة:</b><br>• المعاوقة الكلية (Z) = <b>${Z.toFixed(2)} Ω</b><br>• تردد الرنين النظري (f₀) = <b>${f0.toFixed(1)} Hz</b><br>• حالة الدائرة: <b>${isRes ? 'رنين كهربائي مثالي (XL ≈ Xc، التيار أعظمي)' : (XL > Xc ? 'خواص حثية (الجهد يتقدم على التيار)' : 'خواص سعوية (التيار يتقدم على الجهد)')}</b>`;
  } else if (st === 'phys_transistor_lab') {
    const ib = v.ib || 50, beta = v.beta || 100;
    const ic = (ib * beta) / 1000;
    const ie = (ib / 1000) + ic;
    const alpha = beta / (beta + 1);
    stage.innerHTML = `
      <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center; gap:8px; min-height:110px; text-align:center;">
        <div style="min-width:0;"><div style="font-size:12px; color:#94a3b8;">تيار القاعدة (IB)</div><div style="font-size:17px; color:#f59e0b; font-weight:bold;">${ib} µA</div></div>
        <div style="font-size:24px;">➔ [ β = ${beta} ] ➔</div>
        <div style="min-width:0;"><div style="font-size:12px; color:#94a3b8;">تيار المجمع (IC)</div><div style="font-size:20px; color:#10b981; font-weight:800;">${ic.toFixed(2)} mA</div></div>
      </div>`;
    readout.innerHTML = `<b>📊 معادلات الترانزستور:</b><br>• تيار المجمع IC = β·IB = <b>${ic.toFixed(2)} mA</b><br>• تيار الباعث IE = IB + IC = <b>${ie.toFixed(3)} mA</b><br>• معامل التوزيع α = IC/IE = <b>${alpha.toFixed(4)}</b>`;
  } else if (st === 'phys_radar_lab') {
    const dt = v.dt || 200, fc = v.freq_cro || 3;
    const d_km = (3e8 * (dt * 1e-6)) / 2000;
    let pts = '';
    for (let x = 0; x <= 280; x += 4) {
      const y = 60 + Math.sin((x / 280) * Math.PI * 2 * fc) * 35;
      pts += `${x},${y.toFixed(1)} `;
    }
    stage.innerHTML = `
      <svg viewBox="0 0 280 120" style="width:100%; height:120px; background:#022c22; border-radius:8px;">
        <line x1="0" y1="60" x2="280" y2="60" stroke="#065f46" stroke-width="1"/>
        <polyline fill="none" stroke="#34d399" stroke-width="2.5" points="${pts}"/>
      </svg>`;
    readout.innerHTML = `<b>📡 قياس الرادار والأوسيلوسكوب:</b><br>• مسافة الهدف الجوي: d = (c·Δt)/2 = <b>${d_km.toFixed(2)} km</b><br>• سرعة الموجات الكهرومغناطيسية c = <b>3×10⁸ m/s</b>`;
  } else if (st === 'phys_bohr_lab') {
    const n2 = Math.max(v.n2 || 3, (v.n1 || 2) + 1);
    const n1 = Math.min(v.n1 || 2, n2 - 1);
    const e2 = -13.6 / (n2 * n2), e1 = -13.6 / (n1 * n1);
    const dE = e2 - e1;
    const lambda_nm = 1240 / dE;
    const series = n1 === 1 ? 'متسلسلة ليمان (فوق بنفسجية UV)' : n1 === 2 ? 'متسلسلة بالمر (ضوء مرئي 🌈)' : n1 === 3 ? 'متسلسلة باشن (تحت حمراء IR)' : 'متسلسلة براكت/فوند (تحت حمراء)';
    stage.innerHTML = `
      <div style="text-align:center; padding:12px;">
        <div style="font-size:15px; font-weight:bold; color:#38bdf8;">انتقال الإلكترون: n = ${n2} ⬇ إلى n = ${n1}</div>
        <div style="margin:12px auto; width:80%; height:14px; border-radius:8px; background:${n1===2?'linear-gradient(90deg,#ef4444,#eab308,#22c55e,#3b82f6,#8b5cf6)':'#475569'};"></div>
        <div style="font-size:13px; color:#cbd5e1;">طاقة الفوتون المنبعث: <b style="color:#fbbf24;">${dE.toFixed(2)} eV</b></div>
      </div>`;
    readout.innerHTML = `<b>⚛️ الحسابات الطيفية:</b><br>• طاقة المدار الأعلى E(${n2}) = <b>${e2.toFixed(2)} eV</b><br>• طاقة المدار الأدنى E(${n1}) = <b>${e1.toFixed(2)} eV</b><br>• الطول الموجي للفوتون λ ≈ <b>${lambda_nm.toFixed(1)} nm</b><br>• المتسلسلة الطيفية: <b>${series}</b>`;
  } else if (st === 'phys_photoelectric_lab') {
    const nu = v.freq_nu || 8, phi = v.phi || 2.3;
    const h_ev = 4.1357e-15;
    const E_photon = h_ev * (nu * 1e14);
    const kmax = E_photon - phi;
    const ejected = kmax >= 0;
    stage.innerHTML = `
      <div style="text-align:center; padding:14px;">
        <div style="font-size:28px;">${ejected ? '☀️ ➔ ⚡ تحررت الإلكترونات!' : '☀️ ➔ 🚫 لا يتحرر أي إلكترون'}</div>
        <div style="margin-top:8px; font-size:13px; color:${ejected ? '#4ade80' : '#fca5a5'};">
          طاقة الفوتون (${E_photon.toFixed(2)} eV) ${ejected ? '≥' : '<'} دالة الشغل (${phi.toFixed(2)} eV)
        </div>
      </div>`;
    readout.innerHTML = `<b>💡 معادلة أينشتاين الكهروضوئية:</b><br>• طاقة الفوتون الساقط (hν) = <b>${E_photon.toFixed(2)} eV</b><br>• دالة الشغل للفلز (φ) = <b>${phi.toFixed(2)} eV</b><br>• الطاقة الحركية العظمى للإلكترونات: <b>${ejected ? kmax.toFixed(2) + ' eV' : 'صفر (التردد أقل من تردد العتبة)'}</b>`;
  } else if (st === 'phys_halflife_lab') {
    const th = v.t_half || 8, te = v.t_elapsed ?? 24;
    const n_periods = te / th;
    const rem_pct = 100 * Math.pow(0.5, n_periods);
    stage.innerHTML = `
      <div style="padding:12px;">
        <div style="font-size:13px; margin-bottom:8px;">النسبة المتبقية من الأنوية المشعة: <b>${rem_pct.toFixed(1)}%</b></div>
        <div style="width:100%; height:22px; background:#334155; border-radius:11px; overflow:hidden;">
          <div style="width:${rem_pct}%; height:100%; background:linear-gradient(90deg,#10b981,#34d399); transition:width 0.3s;"></div>
        </div>
      </div>`;
    readout.innerHTML = `<b>☢️ قانون التحلل الإشعاعي:</b><br>• عدد فترات عمر النصف المنقضية (n = t / T₁/₂) = <b>${n_periods.toFixed(2)} فترة</b><br>• النسبة المتبقية دون تحلل = <b>${rem_pct.toFixed(2)}%</b><br>• النسبة التي تحللت إلى عنصر وليد = <b>${(100 - rem_pct).toFixed(2)}%</b>`;
  } else if (st === 'phys_solar_lab') {
    const A = v.area || 4, I = v.irradiance || 850, eff = v.eff || 18;
    const Pout = A * I * (eff / 100);
    stage.innerHTML = `
      <div style="text-align:center; padding:14px;">
        <div style="font-size:28px;">☀️ ➔ 🟦🟦🟦 ➔ ⚡ ${Pout.toFixed(0)} Watt</div>
        <div style="font-size:13px; color:#cbd5e1; margin-top:6px;">طاقة شمسية ساقطة: ${(A*I).toFixed(0)} W | قدرة كهربائية صافية: ${Pout.toFixed(0)} W</div>
      </div>`;
    readout.innerHTML = `<b>☀️ حسابات المنظومة الشمسية:</b><br>• القدرة الكهربائية الناتجة = <b>${Pout.toFixed(1)} واط</b> (تكفي لتشغيل ${(Pout/15).toFixed(0)} مصباح LED)<br>• في 5 ساعات ذروة شمسية باليمن تُنتج يومياً: <b>${((Pout*5)/1000).toFixed(2)} kWh</b>`;
  } else if (st === 'phys_stars_lab') {
    const T = v.temp || 5800;
    const lam = (2.898e-3 / T) * 1e9;
    let color = '#fbbf24', cls = 'G (نجم أصفر مثل الشمس)';
    if (T >= 20000) { color = '#60a5fa'; cls = 'O / B (عملاق أزرق شديد الحرارة)'; }
    else if (T >= 8500) { color = '#e0f2fe'; cls = 'A (نجم أبيض مزرق)'; }
    else if (T >= 6000) { color = '#fef08a'; cls = 'F (نجم أبيض مصفر)'; }
    else if (T >= 4500) { color = '#fb923c'; cls = 'K (نجم برتقالي)'; }
    else if (T < 4500) { color = '#ef4444'; cls = 'M (قزم أو عملاق أحمر بارد)'; }
    stage.innerHTML = `<div style="text-align:center; padding:14px;"><div style="width:64px; height:64px; border-radius:50%; background:${color}; margin:0 auto 8px; box-shadow:0 0 30px ${color};"></div><div style="font-size:14px; font-weight:bold;">التصنيف الطيفي: ${cls}</div></div>`;
    readout.innerHTML = `<b>🔭 قانون فين للإزاحة:</b><br>• الطول الموجي للأشعة الأعظمية (λ_max) = <b>${lam.toFixed(0)} nm</b><br>• كلما ارتفعت حرارة النجم انزاح لونه نحو الأزرق والأشعة فوق البنفسجية.`;
  } else if (st === 'bio_nerve_eye_lab') {
    const stim = v.stimulus || 25, my = v.myelin_on || 4;
    const pot = -70 + stim;
    const fired = pot >= -55;
    const speed = my * 25;
    stage.innerHTML = `
      <div style="text-align:center; padding:12px;">
        <div style="font-size:16px; font-weight:bold; color:${fired ? '#4ade80' : '#fca5a5'};">
          ${fired ? '⚡ تم تجاوز عتبة الإثارة (-55 mV) ← انطلق السيال العصبي (+40 mV)!' : '⏸️ منبه ضعيف لم يصل لعتبة الإثارة (-55 mV)'}
        </div>
        <div style="font-size:13px; color:#cbd5e1; margin-top:8px;">الجهد الناتج مبدئياً: ${pot} mV | سرعة التوصيل بالقفز: ${fired ? speed + ' m/s' : '0 m/s'}</div>
      </div>`;
    readout.innerHTML = `<b>🧠 قانون الكل أو لا شيء:</b><br>• جهد الراحة = <b>-70 mV</b> | جهد العتبة = <b>-55 mV</b><br>• إذا وصل المنبه للعتبة تفتح قنوات الصوديوم ويندفع للداخل ليصل الجهد إلى <b>+40 mV</b> ثم يعود بالبوتاسيوم.`;
  } else if (st === 'bio_auxin_lab') {
    const ang = v.light_angle ?? 30, glu = v.glucose || 100;
    const darkSide = ang > 0 ? 'اليسار (البعيد عن الضوء)' : ang < 0 ? 'اليمين (البعيد عن الضوء)' : 'متساوية في الجانبين';
    const gluMsg = glu > 125 ? 'ارتفاع السكر ← تفرز خلايا بيتا هرمون الإنسولين 💉 لخفضه وتخزينه بالكبد.' : glu < 75 ? 'انخفاض السكر ← تفرز خلايا ألفا هرمون الجلوكاجون 🔋 لرفعه.' : 'مستوى السكر متوازن (75-120 mg/dL) ✅.';
    stage.innerHTML = `
      <div style="display:flex; justify-content:space-around; align-items:center; padding:12px;">
        <div style="font-size:28px; transform:rotate(${ang * 0.4}deg); transition:transform 0.3s;">🌱</div>
        <div style="font-size:13px; max-width:200px;">اتجاه الضوء: <b>${ang}°</b><br>تتجمع الأوكسينات في: <b>${darkSide}</b></div>
      </div>`;
    readout.innerHTML = `<b>🌿 التنظيم الهرموني:</b><br>• الانتحاء الضوئي: ينحني الساق نحو الضوء لأن الأوكسينات (IAA) تستطيل خلايا الجانب المظلم.<br>• اتزان سكر الدم (${glu} mg/dL): <b>${gluMsg}</b>`;
  } else if (st === 'bio_cycle_lab') {
    const d = v.cycle_day || 14;
    let phase = 'الطور الحويصلي (نمو الحويصلة وإفراز الإستروجين)';
    if (d <= 5) phase = 'طور الطمث (انسلاخ بطانة الرحم)';
    else if (d === 14) phase = '🌟 يوم الإباضة (ذروة هرمون LH وتحرر البويضة لقناة فالوب)';
    else if (d > 14) phase = 'طور الجسم الأصفر (إفراز البروجستيرون لتهيئة الرحم)';
    stage.innerHTML = `<div style="text-align:center; padding:14px;"><div style="font-size:22px; font-weight:800; color:#f472b6;">اليوم ${d} من 28</div><div style="font-size:14px; margin-top:8px;">${phase}</div></div>`;
    readout.innerHTML = `<b>🔄 ملخص الهرمونات في اليوم ${d}:</b><br>• ينشط FSH الحويصلة، ويرفع الإستروجين سماكة البطانة، وتفجر ذروة LH البويضة في اليوم 14، ثم يثبت البروجستيرون البطانة.`;
  } else if (st === 'bio_punnett_lab') {
    const ct = v.cross_type || 1;
    let html = '', txt = '';
    if (ct === 1) {
      html = `<table style="width:100%; text-align:center; border-collapse:collapse;"><tr><th></th><th>T</th><th>t</th></tr><tr><th>T</th><td style="border:1px solid #475569; padding:6px;">TT (طويل)</td><td style="border:1px solid #475569; padding:6px;">Tt (طويل)</td></tr><tr><th>t</th><td style="border:1px solid #475569; padding:6px;">Tt (طويل)</td><td style="border:1px solid #475569; padding:6px; color:#f59e0b;">tt (قصير)</td></tr></table>`;
      txt = '<b>التهجين الأحادي (Tt × Tt):</b><br>• النسبة المظهرية: <b>75% طويل الساق : 25% قصير الساق (3 : 1)</b><br>• النسبة الجينية: <b>1 TT : 2 Tt : 1 tt</b>';
    } else if (ct === 2) {
      html = `<table style="width:100%; text-align:center; border-collapse:collapse;"><tr><th></th><th>T</th><th>t</th></tr><tr><th>t</th><td style="border:1px solid #475569; padding:6px;">Tt (طويل)</td><td style="border:1px solid #475569; padding:6px; color:#f59e0b;">tt (قصير)</td></tr><tr><th>t</th><td style="border:1px solid #475569; padding:6px;">Tt (طويل)</td><td style="border:1px solid #475569; padding:6px; color:#f59e0b;">tt (قصير)</td></tr></table>`;
      txt = '<b>التلقيح الاختباري (Tt × tt):</b><br>• النسبة المظهرية والجينية: <b>50% طويل هجين : 50% قصير متنحي (1 : 1)</b>';
    } else {
      html = `<table style="width:100%; text-align:center; border-collapse:collapse;"><tr><th></th><th>Iᴬ</th><th>Iᴮ</th></tr><tr><th>i</th><td style="border:1px solid #475569; padding:6px; color:#38bdf8;">Iᴬi (فصيلة A)</td><td style="border:1px solid #475569; padding:6px; color:#4ade80;">Iᴮi (فصيلة B)</td></tr><tr><th>i</th><td style="border:1px solid #475569; padding:6px; color:#38bdf8;">Iᴬi (فصيلة A)</td><td style="border:1px solid #475569; padding:6px; color:#4ade80;">Iᴮi (فصيلة B)</td></tr></table>`;
      txt = '<b>توارث فصائل الدم (IᴬIᴮ × ii):</b><br>• الأبناء: <b>50% فصيلة A : 50% فصيلة B</b> (يستحيل ظهور AB أو O).';
    }
    stage.innerHTML = html;
    readout.innerHTML = txt;
  } else if (st === 'bio_dna_protein_lab') {
    const idx = v.codon_idx || 1;
    const map = {
      1: {dna: "3'-TAC-5'", comp: "5'-ATG-3'", mrna: "5'-AUG-3'", trna: 'UAC', aa: 'الميثيونين (كودون البدء 🌟)'},
      2: {dna: "3'-CCG-5'", comp: "5'-GGC-3'", mrna: "5'-GGC-3'", trna: 'CCG', aa: 'الجلايسين (Glycine)'},
      3: {dna: "3'-GGA-5'", comp: "5'-CCT-3'", mrna: "5'-CCU-3'", trna: 'GGA', aa: 'البرولين (Proline)'},
      4: {dna: "3'-ATT-5'", comp: "5'-TAA-3'", mrna: "5'-UAA-3'", trna: '—', aa: 'توقف بناء البروتين (كودون إيقاف 🛑)'}
    };
    const r = map[idx] || map[1];
    stage.innerHTML = `
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; text-align:center; font-family:monospace; font-size:14px;">
        <div style="padding:8px; background:rgba(56,189,248,0.15); border-radius:8px;">DNA القالب:<br><b>${r.dna}</b></div>
        <div style="padding:8px; background:rgba(16,185,129,0.15); border-radius:8px;">DNA المكمل:<br><b>${r.comp}</b></div>
        <div style="padding:8px; background:rgba(245,158,11,0.15); border-radius:8px;">نسخ mRNA:<br><b>${r.mrna}</b></div>
        <div style="padding:8px; background:rgba(168,85,247,0.15); border-radius:8px;">مضاد tRNA:<br><b>${r.trna}</b></div>
      </div>`;
    readout.innerHTML = `<b>🧬 نتيجة الترجمة على الرايبوسوم:</b><br>• الحمض الأميني الناتج: <b>${r.aa}</b><br>• لاحظ استبدال الثايمين (T) في DNA باليوراسيل (U) في RNA.`;
  } else if (st === 'bio_evolution_lab') {
    const p = v.pressure || 50, g = v.gens || 5;
    const freq = Math.min(99, 10 + (p * g * 0.18));
    stage.innerHTML = `<div style="padding:14px; text-align:center;"><div style="font-size:15px;">تواتر الأليل المتكيف بعد ${g} أجيال: <b style="color:#4ade80; font-size:20px;">${freq.toFixed(1)}%</b></div></div>`;
    readout.innerHTML = `<b>🦎 الانتخاب الطبيعي:</b><br>• كلما زاد ضغط الانتخاب البيئي وتعددت الأجيال، زاد تواتر الصفات التكيفية النافعة في الجماعة.`;
  } else if (st === 'bio_ecology_lab') {
    const E0 = v.prod_energy || 10000;
    stage.innerHTML = `
      <div style="display:flex; flex-direction:column; align-items:center; gap:5px; font-size:12px;">
        <div style="width:25%; background:#ef4444; text-align:center; padding:4px; border-radius:4px;">مستهلك ثالث: ${(E0*0.001).toFixed(0)} kcal</div>
        <div style="width:45%; background:#f97316; text-align:center; padding:4px; border-radius:4px;">مستهلك ثانٍ: ${(E0*0.01).toFixed(0)} kcal</div>
        <div style="width:70%; background:#eab308; color:#000; text-align:center; padding:4px; border-radius:4px;">مستهلك أول: ${(E0*0.1).toFixed(0)} kcal</div>
        <div style="width:95%; background:#10b981; text-align:center; padding:4px; border-radius:4px;">المنتجات (النباتات): ${E0} kcal</div>
      </div>`;
    readout.innerHTML = `<b>🌿 قاعدة 10% في النظام البيئي:</b><br>• ينتقل 10% فقط من الطاقة لكل مستوى غذائي تالٍ، ويُفقد 90% كطاقة حرارية وعمليات حيوية.`;
  } else if (st === 'bio_geology_lab') {
    const pct = v.c14_pct || 25, era = v.era_idx || 2;
    const halfLives = Math.log2(100 / pct);
    const age = halfLives * 5730;
    const eras = {1: 'حقبة الحياة القديمة (الأسماك والبرمائيات وثلاثيات الفصوص)', 2: 'حقبة الحياة المتوسطة (الديناصورات والزواحف العملاقة)', 3: 'حقبة الحياة الحديثة (الثدييات والإنسان)'};
    stage.innerHTML = `<div style="text-align:center; padding:12px;"><div style="font-size:18px; font-weight:bold; color:#fbbf24;">العمر التقديري بالكربون-14: ~${age.toFixed(0)} سنة</div><div style="font-size:13px; margin-top:8px;">${eras[era]}</div></div>`;
    readout.innerHTML = `<b>🪨 التأريخ الإشعاعي:</b><br>• عمر النصف للكربون-14 = <b>5,730 سنة</b> (يُستخدم للأحافير الحديثة)، أما الصخور القديمة بملايين السنين فتؤرخ باليورانيوم-238.`;
  } else if (st === 'chem_radiation_safety_sim') {
    const d = v.dist || 2, sh = v.shield || 3;
    const relInt = (100 / (d * d)).toFixed(1);
    const shInfo = {1: 'ورق مقوى (يوقف أشعة ألفا α فقط وتمر بيتا وجاما)', 2: 'لوح ألومنيوم (يوقف ألفا وبيتا β بينما تنفذ جاما)', 3: 'درع رصاص سميك Pb (يمتص ألفا وبيتا ويضعف أشعة جاما γ)'}[sh];
    stage.innerHTML = `<div style="padding:12px; text-align:center;"><div style="font-size:20px; font-weight:800; color:#38bdf8;">شدة الإشعاع النسبية عند ${d} م: ${relInt}%</div><div style="font-size:13px; margin-top:8px; color:#cbd5e1;">🛡️ الحماية: ${shInfo}</div></div>`;
    readout.innerHTML = `<b>☢️ قانون التربيع العكسي:</b><br>• مضاعفة المسافة تقلل التعرض الإشعاعي إلى الربع.<br>• مع تغطية أسطح العمل بالرصاص وارتداء البدل الواقية تتحقق الوقاية الآمنة (نشاط 4-1 ص 88).`;
  } else if (st === 'chem_seliwanoff_sim') {
    const rg = v.reagent || 2, hm = v.heat_min || 2;
    if (rg === 1) {
      stage.innerHTML = `<div style="display:flex; justify-content:space-around; padding:10px;"><div style="padding:10px; border-radius:10px; background:rgba(239,68,68,0.2);">الجلوكوز + فهلنج<br>🔴 راسب أحمر طوبي Cu₂O</div><div style="padding:10px; border-radius:10px; background:rgba(239,68,68,0.2);">الفركتوز + فهلنج<br>🔴 راسب أحمر طوبي Cu₂O</div></div>`;
      readout.innerHTML = `<b>⚠️ ملاحظة هامة:</b> كلاً من الجلوكوز والفركتوز يختزلان فهلنج القلوي، لذا نحتاج إلى <b>كاشف سليفانوف (الخيار 2)</b> للتمييز الحاسم بينهما!`;
    } else {
      const fCol = hm >= 2 ? '#dc2626' : '#f87171';
      stage.innerHTML = `<div style="display:flex; justify-content:space-around; padding:10px;"><div style="padding:10px; border-radius:10px; background:rgba(148,163,184,0.15);">الجلوكوز (ألدوهكسوز)<br>⚪ لون باهت بطيء جداً</div><div style="padding:10px; border-radius:10px; background:${fCol}; color:#fff;">الفركتوز (كيتوهكسوز)<br>🩸 لون أحمر كرزي سريع (${hm} د)</div></div>`;
      readout.innerHTML = `<b>🧪 اختبار سليفانوف (نشاط 6-2 ص 110):</b> يتفاعل الفركتوز الكيتوني سريعاً مع الريزورسينول + HCl المركز معطياً لوناً أحمر كرزياً، بينما يتأخر الجلوكوز الألدهيدي.`;
    }
  } else if (st === 'chem_albumin_sim') {
    const m = v.method || 1, smp = v.sample || 2;
    const pos = smp === 2;
    const resTxt = m === 1
      ? (pos ? '☁️ تكون عكارة وراسب أبيض متخثر لا يذوب بإضافة حمض الخليك ← يوجد زلال بالبول!' : '💧 يبقى المحلول رائقاً تماماً ← عينة سليمة خالية من الزلال ✅')
      : (pos ? '💍 تتكون حلقة بيضاء عند السطح الفاصل مع HNO₃ المركز ← يوجد زلال!' : '💧 عدم تكون حلقة بيضاء ← عينة خالية من الزلال ✅');
    stage.innerHTML = `<div style="padding:14px; text-align:center;"><div style="font-size:28px;">${pos ? '🧪☁️' : '🧪💧'}</div><div style="font-size:14px; font-weight:700; margin-top:8px;">${resTxt}</div></div>`;
    readout.innerHTML = `<b>🔬 الكشف عن الزلال (نشاط 6-5 ص 115):</b><br>• يتخثر البروتين (الزلال) بالحرارة ولا يذوب في حمض الخليك المخفف، بينما يترسب الفوسفات يذوب بالحمض.`;
  } else if (st === 'chem_petro_list_sim') {
    const c = v.cat || 1;
    const dataMap = {
      1: ['اللدائن والبلاستيك', 'أواني منزلية، مواسير، عوازل أسلاك، حقائب وتغليف (البولي إيثيلين و PVC).'],
      2: ['الألياف الصناعية والكساء', 'البولي أميد (نايلون 6,6)، البوليستر (الداكرون)، والجلود الصناعية.'],
      3: ['الأدوية والعطور والمذيبات', 'الأسبرين، المضادات الحيوية، الأصباغ، المنظفات الأنيونية والمذيبات العضوية.']
    };
    const [t, d] = dataMap[c];
    stage.innerHTML = `<div style="padding:12px;"><div style="font-size:17px; font-weight:800; color:#fbbf24;">🛢️ ${t}</div><div style="font-size:13px; margin-top:8px; color:#e2e8f0;">${d}</div></div>`;
    readout.innerHTML = `<b>📋 نشاط (7-1) ص 124:</b> تمتاز مشتقات البترول بتنوع استخداماتها الصناعية في كل بيت وسوق تجاري.`;
  } else if (st === 'chem_oil_origin_sim') {
    const th = v.theory || 1;
    stage.innerHTML = `<div style="padding:12px;"><div style="font-size:16px; font-weight:800; color:${th===1?'#4ade80':'#f59e0b'};">${th===1?'🐚 نظرية الأصل الحي (الراجحة علمياً)':'⛏️ نظرية الكربيد غير العضوية'}</div><div style="font-size:13px; margin-top:8px;">${th===1?'تحلل بقايا الكائنات البحرية والنباتية الدقيقة تحت طبقات الرسوب والضغط والحرارة عبر ملايين السنين.':'تفاعل كربيدات الفلزات مثل CaC₂ مع الماء منتجة أسيتيلين يتبلمر بالحرارة والضغط.'}</div></div>`;
    readout.innerHTML = `<b>🔍 الأدلة العلمية (نشاط 7-2 ص 128):</b> وجود مركبات النيتروجين والفوسفور والنشاط الضوئي والحفريات البحرية بالصخور الرسوبية يرجّح <b>نظرية الأصل الحي</b>.`;
  } else if (st === 'chem_yemen_oil_sim') {
    const b = v.basin || 1;
    const bMap = {1: 'حوض مأرب – الجوف (صافر): أول حقل تجاري منتج للنفط والغاز باليمن وتصفيته محلياً.', 2: 'حوض المسيلة – شبوة: من أكبر أحواض التصدير النفطية في حضرموت وشبوة.', 3: 'مصفاة عدن: مصفاة ساحلية تاريخية للتكرير بالتقطير التجزيئي وفصل المشتقات.'};
    stage.innerHTML = `<div style="padding:12px; font-size:14px; font-weight:700; color:#38bdf8;">🗺️ ${bMap[b]}</div>`;
    readout.innerHTML = `<b>📘 نشاط (7-3) ص 131:</b> بعد استخراج النفط الخام بالضغط الطبيعي والمضخات يُكرَّر بالتقطير التجزيئي — ويمكنك تجربة برج التقطير 3D بالضغط على شكل (7-3)!`;
  } else if (st === 'chem_petro_value_sim') {
    const md = v.mode || 2;
    stage.innerHTML = `<div style="padding:12px; text-align:center;"><div style="font-size:24px;">${md===1?'🔥 احتراق مباشر (طاقة فقط)':'🏭 صناعات بتروكيماوية (+10 أضعاف قيمة)'}</div></div>`;
    readout.innerHTML = md === 1
      ? '<b>⛽ الحرق كوقود:</b> يوفر طاقة حرارية وميكانيكية سريعة لكنه يستهلك الخام دون منتجات باقية.'
      : '<b>🧪 البتروكيماويات (نشاط 7-4 ص 136):</b> تحويل نسبة صغيرة من النفط لللدائن والأدوية والأسمدة يضاعف القيمة الاقتصادية عشرات المرات.';
  } else if (st === 'chem_nylon_sim') {
    const stch = v.stretch || 4, mbal = v.monomer || 100;
    const strPct = Math.round((stch / 4) * (mbal / 100) * 100);
    stage.innerHTML = `<div style="padding:12px; text-align:center;"><div style="font-size:18px; font-weight:800; color:#a78bfa;">🧵 سحب خيط نايلون 6,6: ${stch}× الطول الأصلي</div><div style="margin:10px auto; width:85%; height:14px; background:#334155; border-radius:9px; overflow:hidden;"><div style="width:${strPct}%; height:100%; background:linear-gradient(90deg,#8b5cf6,#10b981);"></div></div><div style="font-size:13px;">متانة الشد: <b>${strPct}%</b></div></div>`;
    readout.innerHTML = `<b>🔬 نشاط (8-1) ص 154:</b> يتكاثف حمض الأديبيك (6 كربون) مع هكساميثيلين ثنائي الأمين (6 كربون) مكوّناً خيط بولي أميد متوازٍ السلاسل تتضاعف متانته بالشد 4 أضعاف.`;
  } else if (st === 'chem_pesticide_safety_sim') {
    const pr = v.practice || 2;
    stage.innerHTML = `<div style="padding:12px; font-size:14px; font-weight:700; color:${pr===1?'#fca5a5':'#4ade80'};">${pr===1?'⚠️ خطر الرش العشوائي والمركبات المكلورة (DDT): تسمم التربة والمياه الجوفية وتراكم حيوي بالثمار!':'✅ المكافحة الآمنة: استخدام مبيدات قابلة للتحلل والالتزام بفترات الأمان والكمامات الواقية.'}</div>`;
    readout.innerHTML = `<b>🌱 نشاط (9-1) ص 180:</b> سوء استخدام المبيدات الزراعية في اليمن يهدد صحة المزارع والمستهلك وتوازن النحل والتربة.`;
  } else if (st === 'chem_local_env_sim') {
    const et = v.env_type || 1;
    const eMap = {
      1: ['تلوث الهواء وعوادم المركبات', 'تركيب المحولات الحفزية بالشكمات، نزع الكبريت بـ CaO، وفلاتر المداخن والتشجير.'],
      2: ['تلوث المياه والبيارات والمصانع', 'معالجة ثلاثية (ترسيب + هضم حيوي + كربون نشط) ومنع صرف المصانع لمجاري المياه.'],
      3: ['تلوث التربة الزراعية والمخلفات الصلبة', 'ترشيد الأسمدة والمبيدات، تقليب التربة، وإعادة تدوير الزجاج والورق والبلاستيك.']
    };
    const [hTitle, hSol] = eMap[et];
    stage.innerHTML = `<div style="padding:12px;"><div style="font-size:16px; font-weight:800; color:#34d399;">🌍 ${hTitle}</div><div style="font-size:13px; margin-top:8px; color:#e2e8f0;">${hSol}</div></div>`;
    readout.innerHTML = `<b>♻️ نشاط (9-2) ص 182:</b> الحلول الكيميائية والوقائية تعمل معاً لحماية الهواء والماء والتربة في البيئة المحلية.`;
  }
}

// --------------------------------------------------------
// REAL SUBJECT-SPECIFIC 3D THREE.JS SCENES
// --------------------------------------------------------
let curLabDiag = null;
let labDynamicMeshes = [];
let labFallbackCanvas = null;

function renderSubjectLabDiagTabs(activeRef) {
  const tabsEl = document.getElementById('labDiagTabs');
  if (!tabsEl) return;
  const list = Object.values(DIAGRAMS || {});
  tabsEl.innerHTML = list.map(d => {
    const isAct = d.id === activeRef;
    return `<button class="diag-tab-btn ${isAct ? 'active' : ''}" data-diag="${d.id}" onclick="loadDiagramModel('${d.id}')">${d.title}</button>`;
  }).join('');
  const activeBtn = tabsEl.querySelector('.diag-tab-btn.active');
  if (activeBtn && activeBtn.scrollIntoView) {
    try { activeBtn.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' }); } catch (e) {}
  }
}

function drawLab2DFallback(data, sliderVal) {
  const container = document.getElementById('labCanvasContainer');
  if (!container) return;
  if (!labFallbackCanvas) {
    labFallbackCanvas = document.createElement('canvas');
    labFallbackCanvas.id = 'labFallbackCanvas2D';
    labFallbackCanvas.style.cssText = 'position:absolute; inset:0; width:100%; height:100%; pointer-events:none; z-index:4;';
    container.appendChild(labFallbackCanvas);
  }
  const w = Math.max(280, container.clientWidth);
  const h = Math.max(220, container.clientHeight);
  labFallbackCanvas.width = w;
  labFallbackCanvas.height = h;
  const ctx = labFallbackCanvas.getContext('2d');
  if (!ctx) return;
  ctx.clearRect(0, 0, w, h);

  // Only draw 2D canvas schematic when WebGL renderer is unavailable
  if (labRenderer) return;

  // Pure 2D fallback visualization when WebGL is unavailable
  ctx.fillStyle = '#091522';
  ctx.fillRect(0, 0, w, h);
  ctx.strokeStyle = '#38bdf8';
  ctx.lineWidth = 2;
  ctx.beginPath();
  for (let x = 20; x < w - 20; x += 6) {
    const t = (x - 20) / Math.max(1, w - 40);
    const y = h * 0.52 + Math.sin(t * Math.PI * (2 + (sliderVal || 50) * 0.05)) * (h * 0.18);
    if (x === 20) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  }
  ctx.stroke();
  ctx.fillStyle = '#e2e8f0';
  ctx.font = 'bold 15px Tajawal, sans-serif';
  ctx.textAlign = 'center';
  ctx.fillText(data ? data.title : 'محاكاة علمية تفاعلية', w / 2, h * 0.24);
  if (data && data.formula) {
    ctx.fillStyle = '#34d399';
    ctx.font = 'bold 13px Tajawal, sans-serif';
    ctx.fillText(data.formula, w / 2, h * 0.82);
  }
}

function buildSubject3dScene(diagRef) {
  const ref = (diagRef && DIAGRAMS[diagRef]) ? diagRef : (DEFAULT_DIAG_REF && DIAGRAMS[DEFAULT_DIAG_REF] ? DEFAULT_DIAG_REF : Object.keys(DIAGRAMS)[0]);
  const data = DIAGRAMS[ref] || Object.values(DIAGRAMS)[0];
  curLabDiag = data;
  const sk = data ? (data.sim_key || '') : '';
  const did = data ? (data.id || '') : '';

  renderSubjectLabDiagTabs(ref);

  const titleEl = document.getElementById('labModalTitle') || document.querySelector('#lab3dModal .lab-title');
  if (titleEl && data) titleEl.textContent = '🔬 ' + data.title;
  const sliderEl = document.getElementById('sliderAcidRate') || document.querySelector('#lab3dModal input[type="range"]');
  const sliderValEl = document.getElementById('sliderAcidVal');
  const rateTextEl = document.getElementById('labLiveRateText');
  const labelSpan = document.getElementById('labControlLabel') || (sliderEl ? sliderEl.previousElementSibling : null);
  const eqBadgeEl = document.getElementById('labEquationBadge');
  if (sliderEl && data) {
    sliderEl.min = data.slider_min ?? 0;
    sliderEl.max = data.slider_max ?? 100;
    sliderEl.step = (data.slider_max - data.slider_min) <= 10 ? 0.5 : 1;
    sliderEl.value = data.slider_val ?? 50;
    if (sliderValEl) sliderValEl.textContent = (data.slider_val ?? 50) + (data.slider_unit || '');
    if (labelSpan) labelSpan.textContent = (data.slider_label || 'تحكم بالمحاكاة:').replace(/:?\\s*$/, ':');
  }
  if (eqBadgeEl && data) {
    eqBadgeEl.innerHTML = `⚖️ المبدأ: <b>${data.formula || data.title}</b>`;
  }
  if (rateTextEl) rateTextEl.textContent = 'اسحب للدوران 360° واضغط على أجزاء النموذج';

  if (!labScene) {
    try { initLabThree(); } catch (e) { labRenderer = null; }
  }
  if (labScene && !labApparatusGroup) {
    labApparatusGroup = new THREE.Group();
    labScene.add(labApparatusGroup);
  }
  if (labCamera) {
    labCamera.position.set(0, 0.85, 3.8);
    labCamera.lookAt(0, 0, 0);
  }
  if (!labScene || !labApparatusGroup) {
    drawLab2DFallback(data, sliderEl ? parseFloat(sliderEl.value) : 50);
    return;
  }
  if (!labApparatusGroup.parent) labScene.add(labApparatusGroup);
  while (labApparatusGroup.children.length > 0) {
    labApparatusGroup.remove(labApparatusGroup.children[0]);
  }
  labDynamicMeshes = [];
  bubbles = [];
  flameMesh = null;

  const addMesh = (geo, color, x=0, y=0, z=0, rx=0, ry=0, rz=0, opacity=1) => {
    const mat = new THREE.MeshPhongMaterial({ color, transparent: opacity < 1, opacity, shininess: 85 });
    const m = new THREE.Mesh(geo, mat);
    m.position.set(x, y, z);
    m.rotation.set(rx, ry, rz);
    labApparatusGroup.add(m);
    return m;
  };

  // Bench base
  addMesh(new THREE.BoxGeometry(3.5, 0.08, 1.6), 0x1e293b, 0, -0.92, 0);

  if (sk === 'phys_collision1d' || sk === 'phys_collision2d') {
    addMesh(new THREE.BoxGeometry(3.1, 0.06, 0.55), 0x334155, 0, -0.78, 0);
    const b1 = addMesh(new THREE.SphereGeometry(0.26, 24, 24), 0xef4444, -1.0, -0.5, 0);
    const b2 = addMesh(new THREE.SphereGeometry(0.26, 24, 24), 0x38bdf8, 0.2, -0.5, 0);
    labDynamicMeshes.push({ type: sk, b1, b2 });
  } else if (sk === 'phys_rocket') {
    const rkt = new THREE.Group();
    rkt.add(new THREE.Mesh(new THREE.CylinderGeometry(0.22, 0.26, 1.15, 24), new THREE.MeshPhongMaterial({ color: 0xe2e8f0 })));
    const cone = new THREE.Mesh(new THREE.ConeGeometry(0.22, 0.45, 24), new THREE.MeshPhongMaterial({ color: 0xef4444 }));
    cone.position.y = 0.8; rkt.add(cone);
    const flm = new THREE.Mesh(new THREE.ConeGeometry(0.18, 0.55, 16), new THREE.MeshBasicMaterial({ color: 0xf59e0b }));
    flm.position.y = -0.82; flm.rotation.x = Math.PI; rkt.add(flm);
    labApparatusGroup.add(rkt);
    flameMesh = flm;
    labDynamicMeshes.push({ type: 'bob', mesh: rkt, amp: 0.08 });
  } else if (sk === 'phys_satellite') {
    addMesh(new THREE.SphereGeometry(0.68, 28, 28), 0x0284c7, 0, 0, 0);
    addMesh(new THREE.TorusGeometry(1.38, 0.018, 12, 64), 0x38bdf8, 0, 0, 0, Math.PI/2, 0, 0, 0.65);
    const sat = addMesh(new THREE.BoxGeometry(0.22, 0.16, 0.22), 0xfbbf24, 1.38, 0, 0);
    labDynamicMeshes.push({ type: 'orbit', mesh: sat, radius: 1.38, speed: 0.025, angle: 0 });
  } else if (sk === 'phys_angular') {
    const wheel = new THREE.Group();
    wheel.add(new THREE.Mesh(new THREE.TorusGeometry(0.8, 0.08, 16, 48), new THREE.MeshPhongMaterial({ color: 0x94a3b8 })));
    wheel.add(new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 1.55, 12), new THREE.MeshPhongMaterial({ color: 0x38bdf8 })));
    wheel.rotation.x = Math.PI / 6;
    labApparatusGroup.add(wheel);
    labDynamicMeshes.push({ type: 'spin_z', mesh: wheel });
  } else if (sk === 'phys_projectiles') {
    const cannon = addMesh(new THREE.CylinderGeometry(0.14, 0.18, 0.85, 16), 0x94a3b8, -1.2, -0.5, 0, 0, 0, -Math.PI/4);
    labDynamicMeshes.push({ type: 'cannon', mesh: cannon });
    for (let i = 0; i <= 14; i++) {
      const t = i / 14;
      addMesh(new THREE.SphereGeometry(0.055, 12, 12), i === 7 ? 0x10b981 : 0x38bdf8, -1.05 + t * 2.2, -0.45 + Math.sin(t * Math.PI) * 1.15, 0);
    }
  } else if (sk === 'phys_dynamo') {
    addMesh(new THREE.BoxGeometry(0.5, 1.2, 0.9), 0xef4444, -1.2, 0, 0);
    addMesh(new THREE.BoxGeometry(0.5, 1.2, 0.9), 0x3b82f6, 1.2, 0, 0);
    const coil = new THREE.Group();
    coil.add(new THREE.Mesh(new THREE.BoxGeometry(0.95, 0.65, 0.08), new THREE.MeshPhongMaterial({ color: 0xf59e0b })));
    labApparatusGroup.add(coil);
    labDynamicMeshes.push({ type: 'spin', mesh: coil });
    addMesh(new THREE.TorusGeometry(0.22, 0.04, 10, 20), 0xcbd5e1, 0, -0.82, 0, Math.PI/2, 0, 0);
  } else if (sk === 'phys_capacitor') {
    const p1 = addMesh(new THREE.BoxGeometry(0.12, 1.0, 0.85), 0x38bdf8, -0.45, 0, 0);
    const p2 = addMesh(new THREE.BoxGeometry(0.12, 1.0, 0.85), 0x10b981, 0.45, 0, 0);
    addMesh(new THREE.BoxGeometry(0.18, 0.92, 0.78), 0xfbbf24, 0, 0, 0, 0, 0, 0, 0.45);
    labDynamicMeshes.push({ type: 'cap_plates', p1, p2 });
  } else if (sk === 'phys_rlc') {
    addMesh(new THREE.BoxGeometry(0.55, 0.24, 0.24), 0xf59e0b, -1.05, 0.25, 0);
    for (let i = -2; i <= 2; i++) addMesh(new THREE.TorusGeometry(0.18, 0.05, 10, 20), 0x38bdf8, i * 0.1, 0.25, 0, 0, Math.PI/2, 0);
    addMesh(new THREE.BoxGeometry(0.08, 0.7, 0.6), 0x10b981, 0.88, 0.25, 0);
    addMesh(new THREE.BoxGeometry(0.08, 0.7, 0.6), 0x10b981, 1.12, 0.25, 0);
    addMesh(new THREE.BoxGeometry(2.6, 0.06, 0.06), 0x94a3b8, 0, -0.45, 0);
  } else if (sk === 'phys_diode') {
    addMesh(new THREE.BoxGeometry(0.95, 0.85, 0.75), 0x3b82f6, -0.58, 0, 0, 0, 0, 0, 0.85);
    addMesh(new THREE.BoxGeometry(0.22, 0.85, 0.75), 0xfbbf24, 0, 0, 0, 0, 0, 0, 0.65);
    addMesh(new THREE.BoxGeometry(0.95, 0.85, 0.75), 0x10b981, 0.58, 0, 0, 0, 0, 0, 0.85);
    const orb = addMesh(new THREE.SphereGeometry(0.12, 16, 16), 0x38bdf8, -0.8, 0, 0.5);
    labDynamicMeshes.push({ type: 'pulse', mesh: orb });
  } else if (sk === 'phys_cro') {
    addMesh(new THREE.CylinderGeometry(0.55, 0.22, 1.7, 24), 0x38bdf8, 0, 0, 0, 0, 0, Math.PI/2, 0.35);
    addMesh(new THREE.BoxGeometry(0.08, 0.9, 0.9), 0x064e3b, 0.88, 0, 0);
    const beam = addMesh(new THREE.SphereGeometry(0.09, 14, 14), 0x4ade80, -0.7, 0, 0);
    labDynamicMeshes.push({ type: 'pulse', mesh: beam });
  } else if (sk === 'phys_bohr') {
    addMesh(new THREE.SphereGeometry(0.24, 24, 24), 0xef4444, 0, 0, 0);
    [0.58, 0.95, 1.32].forEach((r, idx) => {
      addMesh(new THREE.TorusGeometry(r, 0.015, 10, 48), 0x38bdf8, 0, 0, 0, Math.PI/2, 0, 0, 0.6);
      const elec = addMesh(new THREE.SphereGeometry(0.08, 16, 16), 0x4ade80, r, 0, 0);
      labDynamicMeshes.push({ type: 'orbit', mesh: elec, radius: r, speed: 0.032 / (idx + 1), angle: idx * 2.1 });
    });
  } else if (sk === 'phys_photoelectric') {
    addMesh(new THREE.BoxGeometry(0.16, 1.0, 0.85), 0x94a3b8, -0.9, 0.2, 0);
    addMesh(new THREE.CylinderGeometry(0.06, 0.06, 0.9, 12), 0xfbbf24, 0.9, 0, 0);
    const photon = addMesh(new THREE.SphereGeometry(0.09, 14, 14), 0xa855f7, 0.2, 0.85, 0);
    const pe = addMesh(new THREE.SphereGeometry(0.08, 14, 14), 0x4ade80, -0.7, 0.2, 0);
    labDynamicMeshes.push({ type: 'pulse', mesh: pe }, { type: 'bob', mesh: photon, amp: 0.22 });
  } else if (sk === 'phys_nuclear') {
    addMesh(new THREE.BoxGeometry(0.55, 0.55, 0.55), 0x64748b, 0, -0.55, 0);
    addMesh(new THREE.BoxGeometry(0.32, 0.55, 0.45), 0xef4444, -0.9, 0.25, 0);
    addMesh(new THREE.BoxGeometry(0.32, 0.55, 0.45), 0x3b82f6, 0.9, 0.25, 0);
    const a = addMesh(new THREE.SphereGeometry(0.1, 14, 14), 0xf97316, -0.25, 0.45, 0);
    const b = addMesh(new THREE.SphereGeometry(0.07, 12, 12), 0x38bdf8, 0.45, 0.55, 0);
    const g = addMesh(new THREE.SphereGeometry(0.07, 12, 12), 0xfde047, 0, 0.72, 0);
    labDynamicMeshes.push({ type: 'bob', mesh: a, amp: 0.14 }, { type: 'bob', mesh: b, amp: 0.2 }, { type: 'bob', mesh: g, amp: 0.24 });
  } else if (sk === 'phys_solar') {
    addMesh(new THREE.ConeGeometry(0.6, 1.0, 3), 0x38bdf8, -0.2, 0.25, 0, 0, 0, 0, 0.65);
    addMesh(new THREE.BoxGeometry(1.45, 0.09, 0.95), 0x1d4ed8, 0.2, -0.55, 0, 0.28, 0, 0);
  } else if (sk === 'phys_cosmos') {
    const star = addMesh(new THREE.SphereGeometry(0.62, 28, 28), 0xfbbf24, 0, 0, 0);
    addMesh(new THREE.TorusGeometry(1.22, 0.08, 12, 48), 0x818cf8, 0, 0, 0, Math.PI/2.4, 0, 0, 0.55);
    labDynamicMeshes.push({ type: 'spin', mesh: star });
  } else if (did === 'diag-bio-hydra' || did === 'diag-bio-neuron' || sk === 'bio_neuron') {
    addMesh(new THREE.SphereGeometry(0.42, 24, 24), 0xa855f7, -1.0, 0, 0);
    addMesh(new THREE.SphereGeometry(0.18, 16, 16), 0xec4899, -1.0, 0, 0.28);
    addMesh(new THREE.CylinderGeometry(0.07, 0.07, 2.2, 16), 0x38bdf8, 0.2, 0, 0, 0, 0, Math.PI/2);
    [-0.3, 0.25, 0.8].forEach(px => addMesh(new THREE.CylinderGeometry(0.14, 0.14, 0.38, 16), 0xfbbf24, px, 0, 0, 0, 0, Math.PI/2));
    const pulse = addMesh(new THREE.SphereGeometry(0.13, 16, 16), 0x4ade80, -0.6, 0, 0);
    labDynamicMeshes.push({ type: 'pulse', mesh: pulse });
  } else if (did === 'diag-bio-eye-ear') {
    addMesh(new THREE.SphereGeometry(0.88, 28, 28), 0xf8fafc, 0, 0, 0, 0, 0, 0, 0.45);
    addMesh(new THREE.SphereGeometry(0.45, 24, 24), 0x0284c7, 0, 0, 0.62);
    addMesh(new THREE.SphereGeometry(0.22, 20, 20), 0x0f172a, 0, 0, 0.86);
    addMesh(new THREE.CylinderGeometry(0.14, 0.14, 0.85, 16), 0xf59e0b, 0, 0, -1.05, Math.PI/2, 0, 0);
  } else if (did === 'diag-bio-flower') {
    addMesh(new THREE.CylinderGeometry(0.12, 0.16, 0.7, 16), 0x22c55e, 0, -0.45, 0);
    addMesh(new THREE.SphereGeometry(0.32, 20, 20), 0x10b981, 0, 0, 0);
    for (let i = 0; i < 6; i++) {
      const a = (i / 6) * Math.PI * 2;
      addMesh(new THREE.SphereGeometry(0.24, 16, 12), 0xec4899, Math.cos(a)*0.55, 0.1, Math.sin(a)*0.55);
    }
  } else if (did === 'diag-bio-fossils' || did === 'diag-bio-radiometric' || did === 'diag-bio-yemen-geo') {
    addMesh(new THREE.BoxGeometry(2.4, 0.35, 1.1), 0x78350f, 0, -0.65, 0);
    addMesh(new THREE.BoxGeometry(2.4, 0.35, 1.1), 0x92400e, 0, -0.28, 0);
    addMesh(new THREE.BoxGeometry(2.4, 0.32, 1.1), 0xb45309, 0, 0.08, 0);
    const fossil = addMesh(new THREE.TorusKnotGeometry(0.25, 0.07, 48, 8), 0xfde047, 0, 0.45, 0);
    labDynamicMeshes.push({ type: 'spin', mesh: fossil });
  } else if (sk === 'bio_dna' || did.includes('dna') || did.includes('mendel') || did.includes('biotech')) {
    const dnaGroup = new THREE.Group();
    for (let i = -5; i <= 5; i++) {
      const y = i * 0.21;
      const a = i * 0.55;
      const x1 = Math.cos(a) * 0.55, z1 = Math.sin(a) * 0.55;
      const m1 = new THREE.Mesh(new THREE.SphereGeometry(0.1, 12, 12), new THREE.MeshPhongMaterial({ color: 0x38bdf8 }));
      m1.position.set(x1, y, z1);
      const m2 = new THREE.Mesh(new THREE.SphereGeometry(0.1, 12, 12), new THREE.MeshPhongMaterial({ color: 0x10b981 }));
      m2.position.set(-x1, y, -z1);
      const bar = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 1.1, 8), new THREE.MeshPhongMaterial({ color: i % 2 === 0 ? 0xf59e0b : 0xec4899 }));
      bar.position.set(0, y, 0); bar.rotation.z = Math.PI / 2; bar.rotation.y = -a;
      dnaGroup.add(m1, m2, bar);
    }
    labApparatusGroup.add(dnaGroup);
    labDynamicMeshes.push({ type: 'spin', mesh: dnaGroup });
  } else if (sk === 'chem_blast_furnace') {
    addMesh(new THREE.CylinderGeometry(0.45, 0.72, 1.85, 24), 0x475569, 0, 0.1, 0);
    addMesh(new THREE.CylinderGeometry(0.55, 0.55, 0.35, 24), 0xf97316, 0, -0.65, 0);
    const molten = addMesh(new THREE.CylinderGeometry(0.48, 0.48, 0.18, 24), 0xfef08a, 0, -0.82, 0);
    labDynamicMeshes.push({ type: 'bob', mesh: molten, amp: 0.04 });
  } else if (sk === 'chem_iron_ions' || sk === 'chem_calorimetry' || sk === 'chem_biochem') {
    const col1 = sk === 'chem_iron_ions' ? 0x4ade80 : (sk === 'chem_biochem' ? 0x1e3a8a : 0x38bdf8);
    const col2 = sk === 'chem_iron_ions' ? 0x991b1b : (sk === 'chem_biochem' ? 0xc2410c : 0xf97316);
    addMesh(new THREE.CylinderGeometry(0.26, 0.26, 1.35, 20), col1, -0.58, -0.1, 0, 0, 0, 0, 0.85);
    addMesh(new THREE.CylinderGeometry(0.26, 0.26, 1.35, 20), col2, 0.58, -0.1, 0, 0, 0, 0, 0.85);
    const stir = addMesh(new THREE.CylinderGeometry(0.04, 0.04, 1.4, 12), 0xe2e8f0, 0, 0.35, 0);
    labDynamicMeshes.push({ type: 'bob', mesh: stir, amp: 0.08 });
  } else if (sk === 'chem_daniell_cell' || sk === 'chem_lead_battery' || sk === 'chem_electrolysis' || sk === 'chem_electroplating') {
    addMesh(new THREE.BoxGeometry(0.75, 0.85, 0.7), 0x0284c7, -0.68, -0.35, 0, 0, 0, 0, 0.55);
    addMesh(new THREE.BoxGeometry(0.75, 0.85, 0.7), 0x38bdf8, 0.68, -0.35, 0, 0, 0, 0, 0.55);
    addMesh(new THREE.BoxGeometry(0.14, 0.95, 0.14), 0x94a3b8, -0.68, 0, 0);
    addMesh(new THREE.BoxGeometry(0.14, 0.95, 0.14), sk === 'chem_electroplating' ? 0xf8fafc : 0xd97706, 0.68, 0, 0);
    addMesh(new THREE.CylinderGeometry(0.06, 0.06, 1.38, 12), 0xfde047, 0, 0.55, 0, 0, 0, Math.PI/2);
    const ePulse = addMesh(new THREE.SphereGeometry(0.09, 12, 12), 0x4ade80, -0.6, 0.55, 0);
    labDynamicMeshes.push({ type: 'pulse', mesh: ePulse });
  } else if (sk === 'chem_distillation_tower') {
    addMesh(new THREE.CylinderGeometry(0.42, 0.42, 2.0, 24), 0x94a3b8, 0, 0.1, 0, 0, 0, 0, 0.42);
    [0x1e293b, 0x92400e, 0xd97706, 0xfacc15, 0x38bdf8].forEach((c, idx) => {
      addMesh(new THREE.CylinderGeometry(0.4, 0.4, 0.06, 20), c, 0, -0.65 + idx * 0.36, 0);
    });
    const vap = addMesh(new THREE.SphereGeometry(0.1, 14, 14), 0xfef08a, 0, -0.6, 0);
    labDynamicMeshes.push({ type: 'bob', mesh: vap, amp: 0.45 });
  } else {
    const grp = new THREE.Group();
    grp.add(new THREE.Mesh(new THREE.SphereGeometry(0.58, 24, 24), new THREE.MeshPhongMaterial({ color: 0x10b981 })));
    const ring = new THREE.Mesh(new THREE.TorusGeometry(0.95, 0.08, 12, 32), new THREE.MeshPhongMaterial({ color: 0x38bdf8 }));
    ring.rotation.x = Math.PI / 3; grp.add(ring);
    labApparatusGroup.add(grp);
    labDynamicMeshes.push({ type: 'spin', mesh: grp });
  }
  drawLab2DFallback(data, sliderEl ? parseFloat(sliderEl.value) : 50);
}

function resizeLab3d() {
  const container = document.getElementById('labCanvasContainer');
  if (!container) return;
  const w = Math.max(1, container.clientWidth);
  const h = Math.max(1, container.clientHeight);
  if (labRenderer && labCamera && labScene) {
    labRenderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    labRenderer.setSize(w, h);
    labCamera.aspect = w / h;
    labCamera.updateProjectionMatrix();
    labRenderer.render(labScene, labCamera);
  }
  const sliderEl = document.getElementById('sliderAcidRate');
  drawLab2DFallback(curLabDiag, sliderEl ? parseFloat(sliderEl.value) : 50);
}
window.addEventListener('resize', resizeLab3d);
window.addEventListener('orientationchange', function() { setTimeout(resizeLab3d, 120); });

function renderDiagramPartsBadges(data) {
  const badgesContainer = document.getElementById('labPartsBadges');
  if (!badgesContainer) return;
  const dedBtn = document.getElementById('btnLab3dOpenDedicated');
  if (dedBtn) {
    const showDed = (BOOK_SUBJECT_KEY !== 'chemistry') || Boolean(data && (data.lab_exp || data.lab_url));
    dedBtn.style.display = showDed ? 'block' : 'none';
  }
  if (data && data.components && data.components.length) {
    badgesContainer.innerHTML = data.components.map((c, i) => `
      <span class="part-badge" onclick="highlightLabPart('${c.id}', '${c.name}', '${c.role}')">${c.name}</span>
    `).join('') + `<div id="labPartInfoBox" style="width:100%; margin-top:8px; padding:10px; border-radius:10px; background:rgba(56,189,248,0.12); border:1px solid rgba(56,189,248,0.35); color:#e2e8f0; font-size:12.5px; display:none;"></div>`;
  } else {
    badgesContainer.innerHTML = '';
  }
}

loadDiagramModel = function(diagRef) {
  buildSubject3dScene(diagRef);
  renderDiagramPartsBadges(curLabDiag);
  if (labRenderer && labScene && labCamera) labRenderer.render(labScene, labCamera);
};

openLab3d = function(diagRef) {
  const modal = document.getElementById('lab3dModal');
  modal.classList.add('open');
  if (!labRenderer) {
    try { initLabThree(); } catch (e) { labRenderer = null; }
  }
  loadDiagramModel(diagRef || DEFAULT_DIAG_REF);
  resizeLab3d();
  requestAnimationFrame(resizeLab3d);
  if (!labAnimId) animateLab();
};

highlightLabPart = function(id, name, role) {
  const box = document.getElementById('labPartInfoBox');
  if (box) {
    box.style.display = 'block';
    box.innerHTML = `<b style="color:#38bdf8;">📌 ${name}:</b> ${role}`;
  }
};

onAcidSliderChange = function(val) {
  const u = (curLabDiag && curLabDiag.slider_unit) || '';
  const el = document.getElementById('sliderAcidVal');
  if (el) el.textContent = val + u;
  const f = parseFloat(val) || 0;
  labDynamicMeshes.forEach(item => {
    if (item.type === 'cannon') item.mesh.rotation.z = -(f * Math.PI / 180);
    if (item.type === 'cap_plates') {
      const gap = Math.max(0.18, 0.9 - (f / 1000));
      item.p1.position.x = -gap; item.p2.position.x = gap;
    }
  });
  drawLab2DFallback(curLabDiag, f);
};

animateLab = function() {
  const modal = document.getElementById('lab3dModal');
  if (!modal || !modal.classList.contains('open')) { labAnimId = 0; return; }
  labAnimId = requestAnimationFrame(animateLab);
  const sliderEl = document.getElementById('sliderAcidRate');
  const sVal = sliderEl ? (parseFloat(sliderEl.value) || 4) : 4;
  const speedMul = Math.max(0.006, sVal * 0.0005);
  const t = performance.now() * 0.002;

  labDynamicMeshes.forEach(item => {
    if (item.type === 'spin') item.mesh.rotation.y += speedMul;
    else if (item.type === 'spin_z') item.mesh.rotation.z += speedMul;
    else if (item.type === 'orbit') {
      item.angle += item.speed;
      item.mesh.position.x = Math.cos(item.angle) * item.radius;
      item.mesh.position.z = Math.sin(item.angle) * item.radius;
    } else if (item.type === 'pulse') {
      item.mesh.position.x += 0.025;
      if (item.mesh.position.x > 1.2) item.mesh.position.x = -0.8;
    } else if (item.type === 'bob') {
      item.mesh.position.y = Math.sin(t * 2) * (item.amp || 0.12);
    } else if (item.type === 'phys_collision1d') {
      const u = (t * 0.5) % 2;
      if (u < 1) {
        item.b1.position.x = -1.1 + u * 1.1; item.b2.position.x = 0.0;
      } else {
        const v = u - 1;
        if (sVal < 0.4) { item.b1.position.x = v * 0.65; item.b2.position.x = v * 0.65 + 0.35; }
        else { item.b1.position.x = 0.0; item.b2.position.x = v * 1.1; }
      }
    } else if (item.type === 'phys_collision2d') {
      const u = (t * 0.5) % 2;
      if (u < 1) {
        item.b1.position.set(-1.1 + u * 1.1, -0.5, 0);
        item.b2.position.set(0.0, -0.5, 0);
      } else {
        const v = u - 1;
        item.b1.position.set(v * 0.9, -0.5 + v * 0.65, 0);
        item.b2.position.set(v * 0.9, -0.5 - v * 0.35, 0);
      }
    }
  });

  if (flameMesh) {
    flameMesh.scale.y = 0.9 + Math.random() * 0.25;
  }
  if (labRenderer && labScene && labCamera) {
    labRenderer.render(labScene, labCamera);
  }
};

// --------------------------------------------------------
// UPGRADED MULTI-QUESTION ASSESSMENT ENGINE ('اختبر نفسك')
// --------------------------------------------------------
let curQuizArray = [];
let curQuizIdx = 0;
let curQuizAnswered = {};

openAssessmentModal = function(refId) {
  const raw = ASSESSMENTS[refId] || Object.values(ASSESSMENTS)[0];
  if (Array.isArray(raw)) {
    curQuizArray = raw;
  } else if (raw) {
    curQuizArray = [raw];
  } else {
    showToast('لا توجد أسئلة متاحة حالياً');
    return;
  }
  curQuizIdx = 0;
  curQuizAnswered = {};
  assessmentScore = 0;
  document.getElementById('assessmentModal').classList.add('open');
  renderAssessmentContent();
};

renderAssessmentContent = function() {
  const qObj = curQuizArray[curQuizIdx];
  if (!qObj) return;

  const promptEl = document.getElementById('assessmentQuestionPrompt');
  const optsContainer = document.getElementById('assessmentOptionsContainer');
  const fbBox = document.getElementById('assessmentFeedbackBox');
  const btnNext = document.getElementById('btnNextExercise');
  const scoreEl = document.getElementById('assessmentScoreText');

  fbBox.style.display = 'none';
  if (qObj.q && qObj.options) {
    promptEl.innerHTML = `<div style="font-size:12px; color:var(--primary); font-weight:800; margin-bottom:6px;">سؤال ${curQuizIdx + 1} من ${curQuizArray.length} ${qObj.page ? `(ص ${qObj.page})` : ''}</div>${qObj.q}`;
    optsContainer.innerHTML = qObj.options.map((opt, i) => `
      <button class="quiz-opt" onclick="selectAssessmentOption(${i})">
        <span>${['أ', 'ب', 'ج', 'د'][i] || (i+1)}. ${opt.text}</span>
        <span>⚪</span>
      </button>
    `).join('');
    scoreEl.textContent = `النتيجة: ${assessmentScore} / ${curQuizArray.length}`;
    if (btnNext) {
      btnNext.style.display = (curQuizIdx < curQuizArray.length - 1) ? 'inline-block' : 'none';
    }
  }
};

selectAssessmentOption = function(idx) {
  const qObj = curQuizArray[curQuizIdx];
  if (!qObj) return;
  const correctIdx = (typeof qObj.answer === 'number') ? qObj.answer : qObj.correct_index;
  const isCorrect = (idx === correctIdx);
  const selectedOpt = qObj.options[idx];
  const buttons = document.querySelectorAll('.quiz-opt');
  const fb = document.getElementById('assessmentFeedbackBox');

  if (!curQuizAnswered[curQuizIdx]) {
    curQuizAnswered[curQuizIdx] = true;
    if (isCorrect) assessmentScore++;
    document.getElementById('assessmentScoreText').textContent = `النتيجة: ${assessmentScore} / ${curQuizArray.length}`;
  }

  buttons.forEach(b => b.classList.remove('correct', 'wrong'));
  if (isCorrect) {
    buttons[idx].classList.add('correct');
    playDingSound();
    fb.style.display = 'block';
    fb.style.background = 'rgba(5, 150, 105, 0.2)';
    fb.style.border = '1px solid #10b981';
    fb.style.color = '#4ade80';
    fb.innerHTML = `<b>🎉 إجابة صحيحة وممتازة!</b><br>${qObj.explain || qObj.explanation || ''}`;
  } else {
    buttons[idx].classList.add('wrong');
    if (buttons[correctIdx]) buttons[correctIdx].classList.add('correct');
    playSnapSound();
    fb.style.display = 'block';
    fb.style.background = 'rgba(220, 38, 38, 0.2)';
    fb.style.border = '1px solid #ef4444';
    fb.style.color = '#fca5a5';
    let fbHtml = `<b>❌ إجابة غير صحيحة</b><br>`;
    if (selectedOpt && selectedOpt.why_wrong) {
      fbHtml += `<div class="why-wrong-box"><b>💡 لماذا هذا الخيار غير صحيح؟</b><br>${selectedOpt.why_wrong}</div>`;
    }
    fbHtml += `<div style="margin-top:6px; color:#cbd5e1;"><b>الشرح العلمي:</b> ${qObj.explain || qObj.explanation || ''}</div>`;
    fb.innerHTML = fbHtml;
  }

  const btnNext = document.getElementById('btnNextExercise');
  if (btnNext && curQuizIdx < curQuizArray.length - 1) {
    btnNext.style.display = 'inline-block';
  }
};

nextAssessmentExercise = function() {
  if (curQuizIdx < curQuizArray.length - 1) {
    curQuizIdx++;
    renderAssessmentContent();
  }
};

// --------------------------------------------------------
// V2 READER CONSISTENCY OVERRIDES (240 DPI, SCOPED STORAGE, TABS)
// --------------------------------------------------------
getVisitedPagesSet = function() {
  try {
    return new Set(JSON.parse(localStorage.getItem('thaker_visited_' + BOOK_SUBJECT_KEY) || '[]'));
  } catch (e) { return new Set(); }
};
markPageVisited = function(bookPage) {
  try {
    const s = getVisitedPagesSet();
    s.add(bookPage);
    localStorage.setItem('thaker_visited_' + BOOK_SUBJECT_KEY, JSON.stringify([...s]));
  } catch (e) {}
};
toggleBookmarkPage = function() {
  const p = PAGES[state.curPageIdx];
  if (!p) return;
  try {
    const key = 'thaker_bookmarks_' + BOOK_SUBJECT_KEY;
    const bms = JSON.parse(localStorage.getItem(key) || '[]');
    const existsIdx = bms.findIndex(b => b.page_id === p.page_id);
    if (existsIdx >= 0) {
      bms.splice(existsIdx, 1);
      showToast('تمت الإزالة من المفضلة');
    } else {
      bms.push({ page_id: p.page_id, book_page: p.book_page, title: p.title });
      showToast('تم حفظ الصفحة في المفضلة ⭐');
    }
    localStorage.setItem(key, JSON.stringify(bms));
    updateBookmarkButtonUI(p.page_id);
  } catch (e) {}
};
updateBookmarkButtonUI = function(pageId) {
  try {
    const bms = JSON.parse(localStorage.getItem('thaker_bookmarks_' + BOOK_SUBJECT_KEY) || '[]');
    const marked = bms.some(b => b.page_id === pageId);
    const btn = document.getElementById('btnBookmarkPage');
    if (btn) btn.classList.toggle('bookmarked', marked);
  } catch (e) {}
};
saveStudentProgress = function() {
  try {
    const key = 'thaker_student_' + BOOK_SUBJECT_KEY;
    const cur = JSON.parse(localStorage.getItem(key) || '{}');
    cur.lastPage = PAGES[state.curPageIdx]?.book_page || PAGES[0]?.book_page || 4;
    cur.updatedAt = new Date().toISOString();
    localStorage.setItem(key, JSON.stringify(cur));
  } catch (e) {}
};

// High-DPI 240 DPI Loader (image_full priority + exact aspect fit)
loadPage = function(pageIdx, direction = 0) {
  if (pageIdx < 0 || pageIdx >= PAGES.length) return;
  state.curPageIdx = pageIdx;
  const p = PAGES[pageIdx];
  resetPageZoom();

  const container = document.getElementById('pageContainer');
  if (container && direction !== 0) {
    container.style.transition = 'transform 0.15s ease-out, opacity 0.15s ease-out';
    container.style.opacity = '0.45';
    container.style.transform = direction > 0 ? 'translateX(-22px)' : 'translateX(22px)';
    setTimeout(() => {
      container.style.transition = 'transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.25s ease';
      container.style.opacity = '1';
      container.style.transform = 'none';
    }, 25);
  }

  const imgEl = document.getElementById('pageImg');
  imgEl._retriedOpt = false;
  imgEl._retriedPath = false;
  imgEl.onerror = function() {
    if (!this._retriedOpt && p.image && this.src !== p.image) {
      this._retriedOpt = true;
      this.src = p.image;
    } else if (this.src.indexOf('assets/curriculum') !== -1 && !this._retriedPath) {
      this._retriedPath = true;
      this.src = this.src.replace('assets/curriculum', 'curriculum');
    }
  };
  imgEl.onload = function() {
    if (this.naturalWidth && this.naturalHeight) {
      const vp = document.getElementById('bookViewport');
      const pc = document.getElementById('pageContainer');
      if (vp && pc) {
        const aspect = this.naturalWidth / this.naturalHeight;
        const availW = Math.max(100, vp.clientWidth - 16);
        const availH = Math.max(100, vp.clientHeight - 16);
        let tw, th;
        if (availW / availH > aspect) { th = availH; tw = Math.round(th * aspect); }
        else { tw = availW; th = Math.round(tw / aspect); }
        pc.style.width = tw + 'px';
        pc.style.height = th + 'px';
      }
    }
  };
  imgEl.src = p.image_full || p.image;
  updatePageContainerDimensions();

  const totalBook = PAGES[PAGES.length - 1]?.book_page || PAGES.length;
  const ind = document.getElementById('pageIndicatorText');
  if (ind) ind.textContent = `صفحة ${p.book_page} من ${totalBook}`;
  const secTitle = document.getElementById('currentSectionTitle');
  if (secTitle) secTitle.textContent = p.title || BOOK_TITLE_MAIN;

  const slider = document.getElementById('pageRangeSlider');
  if (slider) {
    slider.max = Math.max(0, PAGES.length - 1);
    slider.value = pageIdx;
  }
  const minLbl = document.getElementById('sliderMinLabel');
  const maxLbl = document.getElementById('sliderMaxLabel');
  if (minLbl) minLbl.textContent = PAGES[0]?.book_page || 1;
  if (maxLbl) maxLbl.textContent = totalBook;

  const hsCount = (INTERACTIONS[p.page_id] || []).length;
  const hsText = document.getElementById('hotspotCountText');
  if (hsText) hsText.textContent = `✨ النقاط التفاعلية · ${hsCount}`;

  renderInteractionsOverlay(p.page_id);
  updateBookmarkButtonUI(p.page_id);
  markPageVisited(p.book_page);
  saveStudentProgress();

  if (window.ThakerBridge && window.ThakerBridge.updateProgress) {
    try {
      const pct = Math.max(1, Math.round(((pageIdx + 1) / PAGES.length) * 100));
      window.ThakerBridge.updateProgress(document.title, p.book_page, pct, p.unit_id || 'u1', p.title || '');
    } catch (e) {}
  }
};

renderIndexView = function() {
  const container = document.getElementById('indexUnitsContainer');
  if (!container) return;
  const query = (document.getElementById('indexSearchInput')?.value || '').trim();
  const visited = getVisitedPagesSet();

  container.innerHTML = (UNITS || []).map((u, idx) => {
    const allULessons = (LESSONS || []).filter(l => l.unitId === u.id || l.unit_id === u.id);
    const filtered = allULessons.filter(l => !query || (l.title || '').includes(query) || (u.title || '').includes(query));
    if (query && filtered.length === 0) return '';
    let doneCount = 0;
    allULessons.forEach(l => {
      const lp = l.pages || [];
      if (lp.some(pg => visited.has(pg))) doneCount++;
    });
    const pct = allULessons.length ? Math.round((doneCount / allULessons.length) * 100) : 0;
    return `
      <div class="index-unit-card">
        <div class="index-unit-head" onclick="jumpFromIndex(${u.page_start})">
          <div class="unit-ring-badge">${u.order || idx + 1}</div>
          <div style="flex:1;">
            <div style="font-size:15px; font-weight:800; color:var(--text-main);">${u.title || ('الوحدة ' + (idx + 1))}</div>
            <div style="font-size:11.5px; color:var(--text-muted);">${pct}% مكتمل · ${allULessons.length} دروس · ص ${u.page_start}–${u.page_end}</div>
          </div>
          <span class="page-chip-soft">افتح الوحدة</span>
        </div>
        ${filtered.map(l => {
          const lp = l.pages || [];
          const pT = lp.length ? lp[0] : (l.p_start || u.page_start || 1);
          const done = lp.some(pg => visited.has(pg)) || visited.has(pT);
          return `
            <div class="index-lesson-row" onclick="jumpFromIndex(${pT})">
              <div class="lesson-check-dot ${done ? 'done' : ''}">${done ? '✓' : ''}</div>
              <div style="flex:1; font-size:13.5px; font-weight:700; color:var(--text-main);">${l.title}</div>
              <span class="page-chip-soft">ص ${pT}</span>
            </div>
          `;
        }).join('')}
      </div>
    `;
  }).join('');
};

renderSummaryView = function() {
  const container = document.getElementById('summaryCardsContainer');
  if (!container) return;
  const p = PAGES[state.curPageIdx] || PAGES[0] || {};
  const bp = p.book_page || 10;
  const unit = UNITS.find(u => u.id === p.unit_id)
    || UNITS.find(u => bp >= u.page_start && bp <= u.page_end)
    || UNITS[0]
    || {};
  const uId = unit.id || 'u1';
  const ints = INTERACTIONS[p.page_id] || [];
  const expRef = ints.find(i => i.explanation_ref)?.explanation_ref;
  const expObj = (expRef && EXPLANATIONS[expRef])
    || Object.values(EXPLANATIONS).find(e => e.id && e.id.includes(uId))
    || Object.values(EXPLANATIONS)[0];

  const subEl = document.getElementById('summaryUnitSub');
  if (subEl) subEl.textContent = `${unit.title || p.title || ''} · ملخص مفاهيم وقوانين الدرس`;

  let cards = [];
  const vocabIds = (expObj?.vocabulary_ids && expObj.vocabulary_ids.length)
    ? expObj.vocabulary_ids
    : Object.keys(GLOSSARY).filter(k => (GLOSSARY[k]?.unit_id === uId) || k.includes(uId)).slice(0, 4);
  const vList = (vocabIds.length ? vocabIds : Object.keys(GLOSSARY).slice(0, 3)).map(vid => GLOSSARY[vid]).filter(Boolean);
  if (vList.length) {
    cards.push(`
      <div class="summary-stripe-card purple">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span style="font-size:15px; font-weight:800; color:#7C3AED;">💡 تعريفات ومصطلحات</span>
          <span class="page-chip-soft">ص ${bp}</span>
        </div>
        ${vList.map(v => `<div style="font-size:13.5px; line-height:1.6;"><b style="color:var(--text-main);">${v.term}:</b> <span style="color:var(--text-muted);">${v.definition}</span></div>`).join('')}
      </div>
    `);
  }

  const eqs = expObj?.chemical_equations || [];
  const laws = unit.key_laws || [];
  if (eqs.length > 0 || laws.length > 0 || expObj) {
    const eqBlock = eqs.length
      ? eqs.map(e => `<div class="formula-highlight-box">${e.label}: <span style="direction:ltr;display:inline-block;">${e.eq}</span></div>`).join('')
      : (laws.length
          ? laws.map(l => `<div class="formula-highlight-box">${l}</div>`).join('')
          : `<div class="formula-highlight-box">${expObj?.levels?.basic || expObj?.original_text || ''}</div>`);
    cards.push(`
      <div class="summary-stripe-card blue">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span style="font-size:15px; font-weight:800; color:#0284C7;">📐 القوانين والمفاهيم الأساسية</span>
          <span class="page-chip-soft">${unit.title?.split(':')[0] || uId.toUpperCase()}</span>
        </div>
        ${eqBlock}
      </div>
    `);
  }

  const apps = unit.real_world_apps || [];
  const interTxt = expObj?.levels?.intermediate || unit.short_desc || '';
  if (interTxt || apps.length) {
    cards.push(`
      <div class="summary-stripe-card amber">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span style="font-size:15px; font-weight:800; color:#D97706;">🧪 الشرح التطبيقي والحياتي</span>
          <span class="page-chip-soft">ص ${unit.page_start || bp}–${unit.page_end || bp}</span>
        </div>
        ${interTxt ? `<div style="font-size:13.5px; line-height:1.7; color:var(--text-main);">${interTxt}</div>` : ''}
        ${apps.map(a => `<div style="font-size:12.5px; line-height:1.6; color:var(--text-muted);">• ${a}</div>`).join('')}
      </div>
    `);
  }

  const advTxt = expObj?.levels?.advanced || unit.short_desc || 'راجع القوانين والأشكال التوضيحية ونفّذ النشاط العملي لترسيخ الفهم.';
  cards.push(`
    <div class="summary-stripe-card red">
      <div style="font-size:15px; font-weight:800; color:#DC2626;">⚠️ تعمق وتطبيق عملي</div>
      <div style="font-size:13.5px; line-height:1.6; color:var(--text-main);">${advTxt}</div>
      <button onclick="openDedicatedLabForPage()" style="margin-top:4px; background:var(--primary); color:#fff; border:none; border-radius:999px; padding:10px 14px; font-size:13px; font-weight:800; cursor:pointer; font-family:inherit;">🔬 جرّب أنشطة الوحدة في المعمل 3D ‹</button>
    </div>
  `);
  container.innerHTML = cards.join('');
};

let quizFilterByUnit = true;
renderQuizView = function() {
  const container = document.getElementById('quizTabContainer');
  if (!container) return;
  const p = PAGES[state.curPageIdx] || PAGES[0] || {};
  const uId = p.unit_id || UNITS[0]?.id || 'u1';
  const rawEntries = Object.entries(ASSESSMENTS || {});
  const qList = [];
  rawEntries.forEach(([k, val]) => {
    if (quizFilterByUnit && !k.includes(uId)) return;
    if (Array.isArray(val)) val.forEach(sub => qList.push(sub));
    else if (val) qList.push(val);
  });
  if (qList.length === 0) {
    rawEntries.forEach(([, val]) => {
      if (Array.isArray(val)) val.forEach(sub => qList.push(sub));
      else if (val) qList.push(val);
    });
  }
  window._flatQuizList = qList;
  if (qList.length === 0) {
    container.innerHTML = '<div class="quiz-question-card">لا توجد تمارين متاحة حالياً.</div>';
    return;
  }
  if (quizTabIdx >= qList.length) quizTabIdx = 0;
  const q = qList[quizTabIdx];
  document.getElementById('quizTabCounter').textContent = `${quizTabIdx + 1} / ${qList.length}`;
  document.getElementById('quizTabProgressBar').style.width = `${Math.round(((quizTabIdx + 1) / qList.length) * 100)}%`;

  const filterBar = `
    <div style="display:flex; gap:6px; margin-bottom:2px;">
      <button onclick="quizFilterByUnit=true; quizTabIdx=0; renderQuizView();" class="scrubber-nav-btn" style="flex:1; padding:6px; ${quizFilterByUnit ? 'background:var(--primary); color:#fff;' : ''}">أسئلة الوحدة (${uId.toUpperCase()})</button>
      <button onclick="quizFilterByUnit=false; quizTabIdx=0; renderQuizView();" class="scrubber-nav-btn" style="flex:1; padding:6px; ${!quizFilterByUnit ? 'background:var(--primary); color:#fff;' : ''}">كل أسئلة الكتاب</button>
    </div>
  `;
  const opts = q.options || [];
  const jumpPg = q.page || p.book_page;
  container.innerHTML = `
    ${filterBar}
    <div class="quiz-question-card">
      <span class="amber-tag-pill">تمرين كتاب الوزارة ${q.page ? `· ص ${q.page}` : ''}</span>
      <div style="font-size:16px; font-weight:800; line-height:1.6;">${q.prompt || q.q || q.question}</div>
    </div>
    ${opts.map((o, i) => `
      <button class="quiz-opt" id="qtOpt${i}" onclick="answerTabQuiz(${i})">
        <span>${['أ','ب','ج','د'][i] || (i+1)}. ${o.text || o}</span>
        <span>⚪</span>
      </button>
    `).join('')}
    <div id="quizTabFeedback" class="why-wrong-box" style="display:none;"></div>
    <div style="display:flex; gap:8px;">
      <button onclick="jumpFromIndex(${jumpPg})" class="btn-nav" style="flex:1; border-radius:999px;">📖 راجع الصفحة ${q.page ? `(ص ${q.page})` : ''}</button>
      <button onclick="quizTabIdx = (quizTabIdx + 1) % ${qList.length}; renderQuizView();" style="flex:1.3; background:var(--primary); color:#fff; border:none; border-radius:999px; padding:13px; font-size:14.5px; font-weight:800; cursor:pointer; font-family:inherit;">السؤال التالي ‹</button>
    </div>
  `;
};

initApp = function() {
  state.isDark = false;
  window.addEventListener('resize', updatePageContainerDimensions);
  window.addEventListener('orientationchange', function() { setTimeout(updatePageContainerDimensions, 100); });
  updatePageContainerDimensions();
  initTouchGestures();

  let startIdx = Math.min(5, Math.max(0, PAGES.length - 1));
  let startTab = 'reader';
  try {
    const raw = (window.location.search || '') + '&' + (window.location.hash || '');
    const pm = raw.match(/page=(\\d+)/);
    if (pm) {
      const targetBp = parseInt(pm[1], 10);
      const foundIdx = PAGES.findIndex(pg => pg.book_page === targetBp);
      if (foundIdx !== -1) startIdx = foundIdx;
    } else if (raw.includes('restore=1')) {
      const saved = JSON.parse(localStorage.getItem('thaker_student_' + BOOK_SUBJECT_KEY) || '{}');
      if (saved.lastPage) {
        const savedIdx = PAGES.findIndex(pg => pg.book_page === saved.lastPage);
        if (savedIdx !== -1) startIdx = savedIdx;
      }
    }
    const tm = raw.match(/tab=(reader|index|summary|quiz)/);
    if (tm) startTab = tm[1];
  } catch (e) {}

  loadPage(startIdx);
  if (startTab !== 'reader') switchBookTab(startTab);
};
if (document.readyState !== 'loading') {
  initApp();
}
"""

def build_book(subject_key, title_main, title_sub, primary_color, primary_dark, primary_light, accent_color, bundle_js_var, bundle_file, out_filename, eq_label, lab_html_file, lab_btn_label, default_diag):
    print(f"[*] Building interactive HTML for {subject_key} -> {out_filename}...")

    with open(f"{BASE_DIR}/thaker-interactive-book.html", "r", encoding="utf-8") as f:
        html = f.read()

    with open(f"{BASE_DIR}/{bundle_file}", "r", encoding="utf-8") as f:
        bundle_content = f.read()

    start_tag = "window.THAKER_CURRICULUM_P2 = {"
    end_tag = "const LESSONS = window.THAKER_CURRICULUM_P2?.lessons || [];"

    idx_start = html.find(start_tag)
    idx_end = html.find(end_tag)

    if idx_start == -1 or idx_end == -1:
        raise ValueError("Could not find curriculum boundary tags in template")

    new_data_header = f"""
{bundle_content}

const CURR_DATA = {bundle_js_var};
const BOOK_SUBJECT_KEY = {json.dumps(subject_key)};
const BOOK_TITLE_MAIN = {json.dumps(title_main, ensure_ascii=False)};
const BOOK_LAB_HTML = {json.dumps(lab_html_file)};
const DEFAULT_DIAG_REF = {json.dumps(default_diag)};
const PAGES = CURR_DATA?.pages || [];
const INTERACTIONS = CURR_DATA?.interactions || {{}};
const EXPLANATIONS = CURR_DATA?.explanations || {{}};
const DIAGRAMS = CURR_DATA?.diagrams || {{}};
const ACTIVITIES = CURR_DATA?.activities || {{}};
const ASSESSMENTS = CURR_DATA?.assessments || {{}};
const GLOSSARY = CURR_DATA?.glossary || {{}};
const LESSONS = CURR_DATA?.lessons || [];
const UNITS = CURR_DATA?.units || [];
"""

    html_new = html[:idx_start] + new_data_header + html[idx_end + len(end_tag):]

    # Customize titles, metadata, floating lab pill, and #lab3dModal Grade-9 removal
    html_new = html_new.replace("<title>ذاكر — كتاب العلوم التفاعلي الذكي (الصف التاسع - الجزء الثاني)</title>", f"<title>{title_main} — {title_sub}</title>")
    html_new = html_new.replace('<span class="title-main" id="currentSectionTitle">كتاب العلوم التفاعلي الذكي</span>', f'<span class="title-main" id="currentSectionTitle">{title_main}</span>')
    html_new = html_new.replace('<span class="title-main">كتاب العلوم التفاعلي الذكي</span>', f'<span class="title-main">{title_main}</span>')
    html_new = html_new.replace('id="indexBookSub">كتاب العلوم · الجزء الثاني', f'id="indexBookSub">{title_main} · {title_sub}')
    html_new = html_new.replace("فهرس وحدات الجزء الثاني", f"فهرس وحدات {title_sub}")
    html_new = html_new.replace("المعادلات الكيميائية المرتبطة:", eq_label)

    # Replace single hotspot pill with dual reader pills (Hotspots + Dedicated Lab)
    old_pill = """    <button class="hotspot-summary-pill" id="hotspotSummaryPill" onclick="cyclePageHotspot()">
      <span id="hotspotCountText">✨ النقاط التفاعلية · 0</span>
    </button>"""
    new_pill = f"""    <div style="display:flex; align-items:center; justify-content:center; gap:8px; flex-wrap:wrap; pointer-events:auto;">
      <button class="hotspot-summary-pill" id="hotspotSummaryPill" onclick="cyclePageHotspot()">
        <span id="hotspotCountText">✨ النقاط التفاعلية · 0</span>
      </button>
      <button class="hotspot-summary-pill" id="btnOpenDedicatedLab" onclick="openDedicatedLabForPage()" style="background:linear-gradient(135deg,{primary_color},{primary_dark});">
        <span>{lab_btn_label}</span>
      </button>
    </div>"""
    html_new = html_new.replace(old_pill, new_pill)

    # Purge hardcoded Science 9th CO2/Cl2/Allotropes tabs & labels inside #lab3dModal
    import re
    html_new = re.sub(
        r'<div class="diag-tabs-bar" id="labDiagTabs">.*?</div>',
        '<div class="diag-tabs-bar" id="labDiagTabs"></div>',
        html_new,
        count=1,
        flags=re.S,
    )
    html_new = html_new.replace('id="labControlLabel">معدل سكب حمض HCl:', 'id="labControlLabel">متغير المحاكاة:')
    html_new = html_new.replace('<span id="labEquationBadge">⚖️ المعادلة: <b>CaCO₃ + 2HCl ➔ CaCl₂ + H₂O + CO₂ ↑</b></span>', '<span id="labEquationBadge">⚖️ المبدأ العلمي: <b>—</b></span>')
    html_new = html_new.replace('id="labLiveRateText" style="color:#4ade80; font-weight:bold;">تصاعد الغاز: نشط', 'id="labLiveRateText" style="color:#4ade80; font-weight:bold;">تفاعل حي 360°')

    # Inject a direct link inside #lab3dModal to open the full step-by-step dedicated lab
    lab_full_btn = """      <span id="labLiveRateText" style="color:#4ade80; font-weight:bold;">تفاعل حي 360°</span>
    </div>
    <button id="btnLab3dOpenDedicated" onclick="openActiveDiagInDedicatedLab()" style="width:100%; background:linear-gradient(135deg,#10B981,#059669); color:#fff; border:none; border-radius:999px; padding:9px 14px; font-size:12.5px; font-weight:800; cursor:pointer; font-family:inherit;">🔬 افتح النشاط بالخطوات الكاملة في المعمل 3D ‹</button>"""
    html_new = html_new.replace('      <span id="labLiveRateText" style="color:#4ade80; font-weight:bold;">تفاعل حي 360°</span>\n    </div>', lab_full_btn, 1)

    if primary_color != "#00a859":
        html_new = html_new.replace("--primary: #00a859;", f"--primary: {primary_color};")
        html_new = html_new.replace("--primary-dark: #008f4c;", f"--primary-dark: {primary_dark};")
        html_new = html_new.replace("--primary-light: #E8F8F0;", f"--primary-light: {primary_light};")
        html_new = html_new.replace("--border-primary: rgba(0, 168, 89, 0.25);", f"--border-primary: {primary_color}40;")
        html_new = html_new.replace("border-color: #00a859;", f"border-color: {primary_color};")

    # Ensure DOMContentLoaded invokes the overridden initApp (not captured origInitApp ref)
    html_new = html_new.replace(
        "document.addEventListener('DOMContentLoaded', initApp);",
        "document.addEventListener('DOMContentLoaded', function() { initApp(); });",
    )

    # Inject Activity Modal + Full Interactive JS Engine before </body>
    injection = f"""
{ACTIVITY_MODAL_HTML}
<script>
{INTERACTIVE_ENGINE_JS}
</script>
</body>
"""
    html_new = html_new.replace("</body>", injection)

    # Save to workspace root and mirror to android assets
    with open(f"{BASE_DIR}/{out_filename}", "w", encoding="utf-8") as f:
        f.write(html_new)

    with open(f"{BASE_DIR}/thaker-android-src/assets/{out_filename}", "w", encoding="utf-8") as f:
        f.write(html_new)

    print(f"[✓] {out_filename} generated and mirrored successfully ({len(html_new)//1024} KB)!")

def main():
    build_book(
        subject_key="physics",
        title_main="كتاب ومعمل الفيزياء التفاعلي الذكي",
        title_sub="الصف الثالث الثانوي · القسم العلمي",
        primary_color="#0284c7",
        primary_dark="#0369a1",
        primary_light="#E0F2FE",
        accent_color="#38bdf8",
        bundle_js_var="window.THAKER_CURRICULUM_G12_PHYSICS",
        bundle_file="data/curriculum/grade12/physics/data_bundle.js",
        out_filename="physics-12th-book.html",
        eq_label="القوانين والمعادلات المرتبطة:",
        lab_html_file="physics-12th-lab.html",
        lab_btn_label="⚡ معمل الفيزياء 3D",
        default_diag="diag-u1-collision1d"
    )

    build_book(
        subject_key="biology",
        title_main="كتاب ومعمل الأحياء التفاعلي الذكي",
        title_sub="الصف الثالث الثانوي · القسم العلمي",
        primary_color="#00a859",
        primary_dark="#008f4c",
        primary_light="#E8F8F0",
        accent_color="#10b981",
        bundle_js_var="window.THAKER_CURRICULUM_G12_BIOLOGY",
        bundle_file="data/curriculum/grade12/biology/data_bundle.js",
        out_filename="biology-12th-book.html",
        eq_label="التفاعلات والنسب الحيوية المرتبطة:",
        lab_html_file="biology-12th-lab.html",
        lab_btn_label="🧬 معمل الأحياء 3D",
        default_diag="diag-bio-hydra"
    )

    build_book(
        subject_key="chemistry",
        title_main="كتاب ومعمل الكيمياء التفاعلي الذكي",
        title_sub="الصف الثالث الثانوي · القسم العلمي",
        primary_color="#0f766e",
        primary_dark="#115e59",
        primary_light="#CCFBF1",
        accent_color="#14b8a6",
        bundle_js_var="window.THAKER_CURRICULUM_G12_CHEMISTRY",
        bundle_file="data/curriculum/grade12/chemistry/data_bundle.js",
        out_filename="chemistry-12th-book.html",
        eq_label="المعادلات الكيميائية المرتبطة:",
        lab_html_file="chem-lab-book.html",
        lab_btn_label="⚗️ معمل الكيمياء 3D",
        default_diag="diag-chem-galvanic"
    )

if __name__ == "__main__":
    main()
