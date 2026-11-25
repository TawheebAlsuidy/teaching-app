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
<!-- Grade 12 Interactive Activity Simulator Modal -->
<div id="g12ActivityModal" style="display:none; position:fixed; inset:0; background:#0B151C; z-index:960; padding:16px; overflow-y:auto; color:#f8fafc;">
  <div style="max-width:680px; margin:14px auto; display:flex; flex-direction:column; gap:12px;">
    <div style="display:flex; justify-content:space-between; align-items:center;">
      <button class="act-circle-btn" onclick="closeActivityModal()">✕</button>
      <div style="text-align:center; flex:1;">
        <div style="font-size:11.5px; font-weight:800; color:#38bdf8;">🧪 المختبر والنشاط التفاعلي</div>
        <h3 id="actModalTitle" style="margin:2px 0 0; font-size:16.5px; color:#FFFFFF;">عنوان النشاط</h3>
      </div>
      <div style="width:40px;"></div>
    </div>
    <p id="actModalDesc" style="font-size:13px; color:#94a3b8; line-height:1.6; text-align:center;"></p>
    <div id="actVisualStage" style="background:radial-gradient(circle at 50% 45%, #163044 0%, #0B151C 100%); border:1px solid rgba(56,189,248,0.25); border-radius:20px; padding:16px; color:#f8fafc; min-height:160px;"></div>
    <div id="actControlsContainer" style="display:flex; flex-direction:column; gap:10px;"></div>
    <div id="actReadoutBox" style="background:rgba(0,168,89,0.14); border:1px solid var(--primary); border-radius:16px; padding:12px 14px; font-size:13.5px; line-height:1.7; color:#f8fafc;"></div>
    <button class="btn-nav" onclick="closeActivityModal()" style="background:var(--primary); color:#fff; border-color:var(--primary); border-radius:999px; padding:12px; width:100%;">إغلاق والعودة للكتاب</button>
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

// --------------------------------------------------------
// INTERACTIVE ACTIVITY SIMULATOR MODAL
// --------------------------------------------------------
let curActivity = null;
let curActValues = {};

function openActivityModal(actRef) {
  const data = ACTIVITIES[actRef] || Object.values(ACTIVITIES)[0];
  if (!data) { showToast('النشاط غير متاح حالياً'); return; }
  curActivity = data;
  curActValues = {};
  document.getElementById('actModalTitle').textContent = data.title;
  document.getElementById('actModalDesc').textContent = data.description;

  const ctrlBox = document.getElementById('actControlsContainer');
  ctrlBox.innerHTML = (data.controls || []).map(c => {
    curActValues[c.id] = c.default;
    return `
      <div style="background:rgba(148,163,184,0.08); border:1px solid var(--border-light); border-radius:10px; padding:10px 12px;">
        <div style="display:flex; justify-content:space-between; font-size:13px; font-weight:700; margin-bottom:6px;">
          <span>${c.label}</span>
          <span id="actVal_${c.id}" style="color:var(--primary); font-family:monospace; font-size:14px;">${c.default}</span>
        </div>
        <input type="range" min="${c.min}" max="${c.max}" step="${c.step}" value="${c.default}"
          style="width:100%; accent-color:var(--primary); cursor:pointer;"
          oninput="onActivityControlChange('${c.id}', parseFloat(this.value))">
      </div>
    `;
  }).join('');

  document.getElementById('g12ActivityModal').style.display = 'block';
  updateActivitySimulation();
}

function closeActivityModal() {
  document.getElementById('g12ActivityModal').style.display = 'none';
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
      <div style="display:flex; justify-content:space-around; align-items:center; height:120px; text-align:center;">
        <div style="padding:10px; border-radius:10px; background:rgba(56,189,248,0.15); border:1px solid #38bdf8;">
          <div style="font-size:11px; color:#94a3b8;">المفاعلة الحثية XL</div>
          <div style="font-size:18px; font-weight:800; color:#38bdf8;">${XL.toFixed(1)} Ω</div>
        </div>
        <div style="font-size:22px;">${isRes ? '⚡ رنين!' : (XL > Xc ? '🔺 حثية' : '🔻 سعوية')}</div>
        <div style="padding:10px; border-radius:10px; background:rgba(245,158,11,0.15); border:1px solid #f59e0b;">
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
      <div style="display:flex; justify-content:space-around; align-items:center; height:115px; text-align:center;">
        <div><div style="font-size:12px; color:#94a3b8;">تيار القاعدة (IB)</div><div style="font-size:17px; color:#f59e0b; font-weight:bold;">${ib} µA</div></div>
        <div style="font-size:24px;">➔ [ β = ${beta} ] ➔</div>
        <div><div style="font-size:12px; color:#94a3b8;">تيار المجمع (IC)</div><div style="font-size:20px; color:#10b981; font-weight:800;">${ic.toFixed(2)} mA</div></div>
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
  }
}

// --------------------------------------------------------
// REAL SUBJECT-SPECIFIC 3D THREE.JS SCENES
// --------------------------------------------------------
let curLabDiag = null;
let labDynamicMeshes = [];

function buildSubject3dScene(diagRef) {
  if (!labScene || !labApparatusGroup) return;
  while (labApparatusGroup.children.length > 0) {
    labApparatusGroup.remove(labApparatusGroup.children[0]);
  }
  labDynamicMeshes = [];
  bubbles = [];

  const data = DIAGRAMS[diagRef] || Object.values(DIAGRAMS)[0];
  curLabDiag = data;
  const sk = data ? data.sim_key : 'phys_bohr';

  // Update Modal Title & Slider UI cleanly
  const titleEl = document.querySelector('#lab3dModal h3');
  if (titleEl && data) titleEl.textContent = '🧊 ' + data.title;
  const sliderEl = document.querySelector('#lab3dModal input[type="range"]');
  const sliderValEl = document.getElementById('sliderAcidVal');
  const rateTextEl = document.getElementById('labLiveRateText');
  const labelSpan = sliderEl ? sliderEl.previousElementSibling : null;
  if (sliderEl && data) {
    sliderEl.min = data.slider_min ?? 0;
    sliderEl.max = data.slider_max ?? 100;
    sliderEl.value = data.slider_val ?? 50;
    if (sliderValEl) sliderValEl.textContent = (data.slider_val ?? 50) + (data.slider_unit || '');
    if (labelSpan && labelSpan.firstChild) labelSpan.firstChild.textContent = (data.slider_label || 'تحكم بالمحاكاة: ') + ' ';
  }
  if (rateTextEl) rateTextEl.textContent = 'اسحب المجسم بلمسك للدوران 360° واضغط على الأجزاء للتفصيل';

  const addMesh = (geo, color, x=0, y=0, z=0, rx=0, ry=0, rz=0, opacity=1) => {
    const mat = new THREE.MeshPhongMaterial({ color, transparent: opacity < 1, opacity, shininess: 80 });
    const m = new THREE.Mesh(geo, mat);
    m.position.set(x, y, z);
    m.rotation.set(rx, ry, rz);
    labApparatusGroup.add(m);
    return m;
  };

  if (sk === 'phys_projectiles') {
    addMesh(new THREE.BoxGeometry(3.2, 0.1, 1.4), 0x334155, 0, -0.7, 0);
    const cannon = addMesh(new THREE.CylinderGeometry(0.14, 0.18, 0.9, 16), 0x94a3b8, -1.1, -0.4, 0, 0, 0, -Math.PI/4);
    labDynamicMeshes.push({ type: 'cannon', mesh: cannon });
    for (let i = 0; i <= 14; i++) {
      const t = i / 14;
      const px = -1.0 + t * 2.2;
      const py = -0.35 + Math.sin(t * Math.PI) * 1.1;
      addMesh(new THREE.SphereGeometry(0.06, 12, 12), i === 7 ? 0x10b981 : 0x38bdf8, px, py, 0);
    }
  } else if (sk === 'phys_dynamo') {
    addMesh(new THREE.BoxGeometry(0.5, 1.2, 1.0), 0xef4444, -1.2, 0, 0);
    addMesh(new THREE.BoxGeometry(0.5, 1.2, 1.0), 0x3b82f6, 1.2, 0, 0);
    const coil = new THREE.Group();
    const c1 = new THREE.Mesh(new THREE.TorusGeometry(0.55, 0.06, 12, 24), new THREE.MeshPhongMaterial({color: 0xf59e0b}));
    coil.add(c1);
    labApparatusGroup.add(coil);
    labDynamicMeshes.push({ type: 'spin', mesh: coil });
    addMesh(new THREE.TorusGeometry(0.22, 0.04, 10, 20), 0xcbd5e1, 0, -0.85, 0, Math.PI/2, 0, 0);
  } else if (sk === 'phys_rlc') {
    addMesh(new THREE.BoxGeometry(0.6, 0.25, 0.25), 0xf59e0b, -1.0, 0.3, 0);
    for (let i = -2; i <= 2; i++) addMesh(new THREE.TorusGeometry(0.18, 0.05, 10, 20), 0x38bdf8, i * 0.1, 0.3, 0, 0, Math.PI/2, 0);
    addMesh(new THREE.BoxGeometry(0.08, 0.7, 0.6), 0x10b981, 0.9, 0.3, 0);
    addMesh(new THREE.BoxGeometry(0.08, 0.7, 0.6), 0x10b981, 1.15, 0.3, 0);
    addMesh(new THREE.BoxGeometry(2.6, 0.06, 0.06), 0x94a3b8, 0, -0.45, 0);
  } else if (sk === 'phys_bohr') {
    addMesh(new THREE.SphereGeometry(0.24, 24, 24), 0xef4444, 0, 0, 0);
    [0.65, 1.05, 1.45].forEach((r, idx) => {
      addMesh(new THREE.TorusGeometry(r, 0.015, 10, 48), 0x38bdf8, 0, 0, 0, Math.PI/2, 0, 0, 0.6);
      const elec = addMesh(new THREE.SphereGeometry(0.08, 16, 16), 0x4ade80, r, 0, 0);
      labDynamicMeshes.push({ type: 'orbit', mesh: elec, radius: r, speed: 0.03 / (idx + 1), angle: idx * 2 });
    });
  } else if (sk === 'phys_diode' || sk === 'phys_cro' || sk === 'phys_photoelectric' || sk === 'phys_nuclear' || sk === 'phys_solar') {
    addMesh(new THREE.BoxGeometry(1.0, 0.9, 0.8), 0x3b82f6, -0.55, 0, 0, 0, 0, 0, 0.85);
    addMesh(new THREE.BoxGeometry(0.2, 0.9, 0.8), 0xfbbf24, 0, 0, 0, 0, 0, 0, 0.7);
    addMesh(new THREE.BoxGeometry(1.0, 0.9, 0.8), 0x10b981, 0.55, 0, 0, 0, 0, 0, 0.85);
    const orb = addMesh(new THREE.SphereGeometry(0.12, 16, 16), 0x38bdf8, 0, 0.75, 0);
    labDynamicMeshes.push({ type: 'spin', mesh: orb });
  } else if (sk === 'bio_neuron') {
    addMesh(new THREE.SphereGeometry(0.42, 24, 24), 0xa855f7, -1.0, 0, 0);
    addMesh(new THREE.SphereGeometry(0.18, 16, 16), 0xec4899, -1.0, 0, 0.28);
    addMesh(new THREE.CylinderGeometry(0.07, 0.07, 2.2, 16), 0x38bdf8, 0.2, 0, 0, 0, 0, Math.PI/2);
    [-0.3, 0.25, 0.8].forEach(px => addMesh(new THREE.CylinderGeometry(0.14, 0.14, 0.38, 16), 0xfbbf24, px, 0, 0, 0, 0, Math.PI/2));
    const pulse = addMesh(new THREE.SphereGeometry(0.13, 16, 16), 0x4ade80, -0.6, 0, 0);
    labDynamicMeshes.push({ type: 'pulse', mesh: pulse });
  } else if (sk === 'bio_eye') {
    addMesh(new THREE.SphereGeometry(0.9, 28, 28), 0xf8fafc, 0, 0, 0, 0, 0, 0, 0.45);
    addMesh(new THREE.SphereGeometry(0.45, 24, 24), 0x0284c7, 0, 0, 0.65);
    addMesh(new THREE.SphereGeometry(0.22, 20, 20), 0x0f172a, 0, 0, 0.88);
    addMesh(new THREE.CylinderGeometry(0.14, 0.14, 0.9, 16), 0xf59e0b, 0, 0, -1.1, Math.PI/2, 0, 0);
  } else if (sk === 'bio_ear') {
    addMesh(new THREE.TorusGeometry(0.55, 0.12, 14, 28, Math.PI * 1.5), 0xfdba74, -1.1, 0, 0);
    addMesh(new THREE.CylinderGeometry(0.15, 0.15, 0.9, 16), 0xfb923c, -0.45, 0, 0, 0, 0, Math.PI/2);
    addMesh(new THREE.TorusKnotGeometry(0.42, 0.1, 64, 12, 2, 3), 0x38bdf8, 0.75, 0, 0);
  } else if (sk === 'bio_dna') {
    const dnaGroup = new THREE.Group();
    for (let i = -5; i <= 5; i++) {
      const y = i * 0.22;
      const a = i * 0.55;
      const x1 = Math.cos(a) * 0.55, z1 = Math.sin(a) * 0.55;
      const x2 = -x1, z2 = -z1;
      const m1 = new THREE.Mesh(new THREE.SphereGeometry(0.1, 12, 12), new THREE.MeshPhongMaterial({color: 0x38bdf8}));
      m1.position.set(x1, y, z1);
      const m2 = new THREE.Mesh(new THREE.SphereGeometry(0.1, 12, 12), new THREE.MeshPhongMaterial({color: 0x10b981}));
      m2.position.set(x2, y, z2);
      const bar = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 1.1, 8), new THREE.MeshPhongMaterial({color: i%2===0?0xf59e0b:0xec4899}));
      bar.position.set(0, y, 0);
      bar.rotation.z = Math.PI/2;
      bar.rotation.y = -a;
      dnaGroup.add(m1, m2, bar);
    }
    labApparatusGroup.add(dnaGroup);
    labDynamicMeshes.push({ type: 'spin', mesh: dnaGroup });
  } else {
    // Endocrine / Flower / Chromosome / Earth 3D
    const grp = new THREE.Group();
    const core = new THREE.Mesh(new THREE.SphereGeometry(0.6, 24, 24), new THREE.MeshPhongMaterial({color: 0x10b981}));
    const ring = new THREE.Mesh(new THREE.TorusGeometry(0.95, 0.08, 12, 32), new THREE.MeshPhongMaterial({color: 0x38bdf8}));
    ring.rotation.x = Math.PI / 3;
    grp.add(core, ring);
    labApparatusGroup.add(grp);
    labDynamicMeshes.push({ type: 'spin', mesh: grp });
  }
}

openLab3d = function(diagRef) {
  const modal = document.getElementById('lab3dModal');
  modal.classList.add('open');
  if (!labRenderer) initLabThree();

  const container = document.getElementById('labCanvasContainer');
  labRenderer.setSize(container.clientWidth, container.clientHeight);
  labCamera.aspect = container.clientWidth / container.clientHeight;
  labCamera.updateProjectionMatrix();

  buildSubject3dScene(diagRef);

  const data = DIAGRAMS[diagRef] || Object.values(DIAGRAMS)[0];
  const badgesContainer = document.getElementById('labPartsBadges');
  if (data && data.components) {
    badgesContainer.innerHTML = data.components.map(c => `
      <span class="part-badge" onclick="highlightLabPart('${c.id}', '${c.name}', '${c.role}')">${c.name}</span>
    `).join('') + `<div id="labPartInfoBox" style="width:100%; margin-top:8px; padding:10px; border-radius:10px; background:rgba(56,189,248,0.12); border:1px solid rgba(56,189,248,0.35); color:#e2e8f0; font-size:12.5px; display:none;"></div>`;
  }

  animateLab();
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
  labDynamicMeshes.forEach(item => {
    if (item.type === 'cannon') item.mesh.rotation.z = -(val * Math.PI / 180);
  });
};

animateLab = function() {
  labAnimId = requestAnimationFrame(animateLab);
  const sliderEl = document.querySelector('#lab3dModal input[type="range"]');
  const speedMul = sliderEl ? (parseFloat(sliderEl.value) || 4) * 0.004 : 0.015;

  labDynamicMeshes.forEach(item => {
    if (item.type === 'spin') {
      item.mesh.rotation.y += speedMul;
    } else if (item.type === 'orbit') {
      item.angle += item.speed;
      item.mesh.position.x = Math.cos(item.angle) * item.radius;
      item.mesh.position.z = Math.sin(item.angle) * item.radius;
    } else if (item.type === 'pulse') {
      item.mesh.position.x += 0.025;
      if (item.mesh.position.x > 1.25) item.mesh.position.x = -0.65;
    }
  });

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
"""

def build_book(subject_key, title_main, title_sub, primary_color, accent_color, bundle_js_var, bundle_file, out_filename, eq_label):
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

    # Customize titles and colors
    html_new = html_new.replace("<title>ذاكر — كتاب العلوم التفاعلي الذكي (الصف التاسع - الجزء الثاني)</title>", f"<title>{title_main}</title>")
    html_new = html_new.replace('<span class="title-main" id="currentSectionTitle">كتاب العلوم التفاعلي الذكي</span>', f'<span class="title-main" id="currentSectionTitle">{title_main}</span>')
    html_new = html_new.replace('<span class="title-main">كتاب العلوم التفاعلي الذكي</span>', f'<span class="title-main">{title_main}</span>')
    html_new = html_new.replace('<span class="title-sub" id="currentSectionTitle">الصف التاسع الأساسي · الجزء الثاني</span>', f'<span class="title-sub" id="currentSectionTitle">{title_sub}</span>')
    html_new = html_new.replace('id="indexBookSub">كتاب العلوم · الجزء الثاني', f'id="indexBookSub">{title_main} · {title_sub}')
    html_new = html_new.replace("فهرس وحدات الجزء الثاني", f"فهرس وحدات {title_sub}")
    html_new = html_new.replace("المعادلات الكيميائية المرتبطة:", eq_label)

    if primary_color != "#00a859":
        html_new = html_new.replace("--primary: #00a859;", f"--primary: {primary_color};")
        html_new = html_new.replace("--primary-dark: #008f4c;", f"--primary-dark: {primary_color};")
        html_new = html_new.replace("border-color: #00a859;", f"border-color: {primary_color};")

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
        accent_color="#38bdf8",
        bundle_js_var="window.THAKER_CURRICULUM_G12_PHYSICS",
        bundle_file="data/curriculum/grade12/physics/data_bundle.js",
        out_filename="physics-12th-book.html",
        eq_label="القوانين والمعادلات المرتبطة:"
    )

    build_book(
        subject_key="biology",
        title_main="كتاب ومعمل الأحياء التفاعلي الذكي",
        title_sub="الصف الثالث الثانوي · القسم العلمي",
        primary_color="#00a859",
        accent_color="#10b981",
        bundle_js_var="window.THAKER_CURRICULUM_G12_BIOLOGY",
        bundle_file="data/curriculum/grade12/biology/data_bundle.js",
        out_filename="biology-12th-book.html",
        eq_label="التفاعلات والنسب الحيوية المرتبطة:"
    )

if __name__ == "__main__":
    main()
