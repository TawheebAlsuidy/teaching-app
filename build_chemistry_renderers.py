#!/usr/bin/env python3
"""Bespoke labeled 2D Canvas diagram renderers for all 74 unique Chemistry figures (Units 1-9).

All coordinates scale proportionally within the visible safe canvas bounds [76 .. h - 44]
so mobile (360x800) and tablet/desktop viewports render crisp non-overlapping Arabic schematics.
"""


def get_chemistry_2d_js() -> str:
    return r"""
// Ensure clean toggle pill between 3D model and bespoke labeled 2D schematic
window.__chemViewMode = window.__chemViewMode || '3d';
function ensureChemModeToggle(data) {
  const container = document.getElementById('labCanvasContainer');
  if (!container) return;
  let bar = document.getElementById('chemModeToggleBar');
  const isChem = !!(data && (data.sim_key || '').indexOf('chem_') === 0);
  const zoomHud = container.querySelector('.lab-hud-zoom');
  const touchHint = container.querySelector('.lab-touch-hint');
  if (!isChem) {
    if (bar) bar.style.display = 'none';
    if (zoomHud) zoomHud.style.display = 'flex';
    if (touchHint) touchHint.style.display = '';
    return;
  }
  const is2 = (window.__chemViewMode === '2d') || !labRenderer;
  if (zoomHud) zoomHud.style.display = is2 ? 'none' : 'flex';
  if (touchHint) {
    touchHint.style.display = is2 ? 'none' : '';
    if (!is2) { touchHint.style.top = '48px'; touchHint.style.right = '10px'; }
  }
  if (!labRenderer) {
    if (bar) bar.style.display = 'none';
    return;
  }
  if (!bar) {
    bar = document.createElement('div');
    bar.id = 'chemModeToggleBar';
    bar.style.cssText = 'position:absolute; top:6px; left:8px; z-index:25; display:flex; gap:4px; background:rgba(7,19,30,0.92); border:1px solid rgba(56,189,248,0.5); border-radius:999px; padding:3px; pointer-events:auto; backdrop-filter:blur(4px); box-shadow:0 2px 10px rgba(0,0,0,0.35);';
    bar.innerHTML = `<button type="button" id="btnChemMode3D" style="border:none;border-radius:999px;padding:4px 10px;font-size:11px;font-weight:700;cursor:pointer;font-family:Tajawal,sans-serif;">🧊 3D</button><button type="button" id="btnChemMode2D" style="border:none;border-radius:999px;padding:4px 10px;font-size:11px;font-weight:700;cursor:pointer;font-family:Tajawal,sans-serif;">📐 المخطط المشروح</button>`;
    container.appendChild(bar);
    bar.querySelector('#btnChemMode3D').onclick = () => {
      window.__chemViewMode = '3d';
      ensureChemModeToggle(curLabDiag);
      const sl = document.getElementById('sliderAcidRate');
      drawLab2DFallback(curLabDiag, sl ? parseFloat(sl.value) : 50);
    };
    bar.querySelector('#btnChemMode2D').onclick = () => {
      window.__chemViewMode = '2d';
      ensureChemModeToggle(curLabDiag);
      const sl = document.getElementById('sliderAcidRate');
      drawLab2DFallback(curLabDiag, sl ? parseFloat(sl.value) : 50);
    };
  }
  bar.style.display = 'flex';
  const b3 = bar.querySelector('#btnChemMode3D');
  const b2 = bar.querySelector('#btnChemMode2D');
  b3.style.background = is2 ? 'transparent' : '#0ea5e9';
  b3.style.color = is2 ? '#cbd5e1' : '#ffffff';
  b2.style.background = is2 ? '#10b981' : 'transparent';
  b2.style.color = is2 ? '#ffffff' : '#cbd5e1';
}

function drawChem2DSchematic(data, sliderVal, ctx, w, h) {
  const sk = (data && data.sim_key) || '';
  const sv = Number.isFinite(sliderVal) ? sliderVal : (data && data.slider_val != null ? data.slider_val : 50);

  // Dark scientific blueprint grid background
  const g = ctx.createLinearGradient(0, 0, 0, h);
  g.addColorStop(0, '#071422');
  g.addColorStop(1, '#0b1d2e');
  ctx.fillStyle = g;
  ctx.fillRect(0, 0, w, h);
  ctx.strokeStyle = 'rgba(56,189,248,0.11)';
  ctx.lineWidth = 1;
  for (let gx = 24; gx < w; gx += 28) { ctx.beginPath(); ctx.moveTo(gx, 0); ctx.lineTo(gx, h); ctx.stroke(); }
  for (let gy = 24; gy < h; gy += 28) { ctx.beginPath(); ctx.moveTo(0, gy); ctx.lineTo(w, gy); ctx.stroke(); }

  // Safe vertical coordinate mapper [0..1] inside [76 .. h - 46] (below mode toggle + header, above formula pill)
  const py = t => 78 + t * Math.max(96, h - 124);
  const px = t => t * w;
  const usableH = Math.max(96, h - 124);

  const txt = (s, x, y, col = '#f1f5f9', sz = 12, align = 'center', rtl = true, maxW = null) => {
    ctx.save();
    ctx.fillStyle = col;
    ctx.font = `bold ${sz}px Tajawal, Cairo, sans-serif`;
    ctx.textAlign = align;
    ctx.textBaseline = 'middle';
    if ('direction' in ctx) ctx.direction = rtl ? 'rtl' : 'ltr';
    ctx.fillText(String(s), x, y, maxW || (w - 22));
    ctx.restore();
  };
  const rrect = (x, y, rw, rh, rad, fill, stroke) => {
    ctx.save();
    ctx.beginPath();
    const r = Math.min(rad, Math.abs(rw) / 2, Math.abs(rh) / 2);
    ctx.moveTo(x + r, y); ctx.lineTo(x + rw - r, y); ctx.quadraticCurveTo(x + rw, y, x + rw, y + r);
    ctx.lineTo(x + rw, y + rh - r); ctx.quadraticCurveTo(x + rw, y + rh, x + rw - r, y + rh);
    ctx.lineTo(x + r, y + rh); ctx.quadraticCurveTo(x, y + rh, x, y + rh - r);
    ctx.lineTo(x, y + r); ctx.quadraticCurveTo(x, y, x + r, y);
    if (fill) { ctx.fillStyle = fill; ctx.fill(); }
    if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = 1.6; ctx.stroke(); }
    ctx.restore();
  };
  const arr = (x1, y1, x2, y2, col = '#38bdf8', lw = 2) => {
    ctx.save();
    ctx.strokeStyle = col; ctx.fillStyle = col; ctx.lineWidth = lw;
    ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
    const a = Math.atan2(y2 - y1, x2 - x1);
    ctx.beginPath();
    ctx.moveTo(x2, y2);
    ctx.lineTo(x2 - 8 * Math.cos(a - 0.42), y2 - 8 * Math.sin(a - 0.42));
    ctx.lineTo(x2 - 8 * Math.cos(a + 0.42), y2 - 8 * Math.sin(a + 0.42));
    ctx.closePath(); ctx.fill();
    ctx.restore();
  };
  const beaker = (cx, by, bw, bh, liqCol, colLabel) => {
    const x0 = cx - bw / 2, y0 = by - bh;
    ctx.save();
    ctx.fillStyle = liqCol;
    ctx.fillRect(x0 + 3, y0 + bh * 0.35, bw - 6, bh * 0.63);
    ctx.strokeStyle = '#94a3b8'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x0, by); ctx.lineTo(x0 + bw, by); ctx.lineTo(x0 + bw, y0); ctx.stroke();
    ctx.restore();
    if (colLabel) txt(colLabel, cx, by + 13, '#cbd5e1', 10, 'center', true, bw + 44);
  };
  const poly = (cx, cy, r, sides, col = '#38bdf8', arom = false, rot = 0) => {
    ctx.save();
    ctx.strokeStyle = col; ctx.lineWidth = 2;
    ctx.beginPath();
    for (let i = 0; i <= sides; i++) {
      const a = rot + (i * Math.PI * 2) / sides;
      const vx = cx + Math.cos(a) * r, vy = cy + Math.sin(a) * r;
      if (i === 0) ctx.moveTo(vx, vy); else ctx.lineTo(vx, vy);
    }
    ctx.stroke();
    if (arom) { ctx.beginPath(); ctx.arc(cx, cy, r * 0.56, 0, Math.PI * 2); ctx.stroke(); }
    ctx.restore();
  };

  // Header placed cleanly below top-left toggle pill bar (top 38px reserved)
  rrect(10, 42, w - 20, 26, 7, 'rgba(15,23,42,0.88)', 'rgba(56,189,248,0.42)');
  txt(data ? data.title : '', px(0.5), 55, '#7dd3fc', 11, 'center', true, w - 34);

  // ---------------- UNIT 1 ----------------
  if (sk === 'chem_u1_d_f_blocks') {
    rrect(px(0.08), py(0.08), px(0.11), usableH * 0.56, 5, sv === 1 ? 'rgba(239,68,68,0.42)' : 'rgba(239,68,68,0.2)', '#f87171');
    txt('s', px(0.135), py(0.36), '#fecaca', 13, 'center', false);
    rrect(px(0.21), py(0.22), px(0.45), usableH * 0.42, 5, 'rgba(245,158,11,0.34)', '#fbbf24');
    txt('الفئة d (الانتقالية الرئيسية · 10 أعمدة)', px(0.435), py(0.38), '#fde68a', 11, 'center', true, px(0.42));
    txt('3d / 4d / 5d / 6d', px(0.435), py(0.52), '#fcd34d', 10, 'center', false);
    rrect(px(0.68), py(0.08), px(0.24), usableH * 0.56, 5, 'rgba(56,189,248,0.22)', '#38bdf8');
    txt('p', px(0.80), py(0.36), '#bae6fd', 13, 'center', false);
    rrect(px(0.21), py(0.72), px(0.45), usableH * 0.22, 5, 'rgba(16,185,129,0.28)', '#34d399');
    txt('الفئة f (4f اللانثانيدات · 5f الأكتينيدات)', px(0.435), py(0.83), '#a7f3d0', 10.5, 'center', true, px(0.43));
  } else if (sk === 'chem_u1_orbitals') {
    const z = Math.round(sv);
    const dCount = z === 24 ? 5 : (z === 29 ? 10 : Math.max(1, Math.min(10, z - 20)));
    const sCount = (z === 24 || z === 29) ? 1 : 2;
    txt(`Z = ${z}  |  4s^${sCount} 3d^${dCount} ${(z === 24 || z === 29) ? '⭐ (حالة استقرار شاذة)' : ''}`, px(0.5), py(0.12), '#fbbf24', 12);
    const bw = Math.min(44, (w - 64) / 5), gap = 6, x0 = (w - (5 * bw + 4 * gap)) / 2;
    for (let i = 0; i < 5; i++) {
      const bx = x0 + i * (bw + gap);
      rrect(bx, py(0.26), bw, usableH * 0.22, 6, '#1e293b', '#38bdf8');
      if (dCount > i) txt('↑', bx + bw * 0.34, py(0.37), '#4ade80', 14, 'center', false);
      if (dCount > i + 5) txt('↓', bx + bw * 0.68, py(0.37), '#f472b6', 14, 'center', false);
    }
    txt('أفلاك المستوى الفرعي 3d الخمسة', px(0.5), py(0.56), '#94a3b8', 11);
    rrect(px(0.5) - 24, py(0.65), 48, usableH * 0.20, 6, '#1e293b', '#fbbf24');
    txt(sCount === 2 ? '↑ ↓' : '↑', px(0.5), py(0.75), '#fde047', 14, 'center', false);
    txt('فلك 4s', px(0.5), py(0.92), '#cbd5e1', 11);
  } else if (sk === 'chem_blast_furnace') {
    rrect(px(0.14), py(0.01), px(0.72), 22, 6, 'rgba(30,41,59,0.9)', '#94a3b8');
    txt('شحنة القمة: Fe₂O₃ + كوك + جير', px(0.5), py(0.01) + 11, '#f8fafc', 10, 'center', true, px(0.68));
    arr(px(0.5), py(0.01) + 23, px(0.5), py(0.13), '#cbd5e1', 1.8);
    ctx.beginPath();
    ctx.moveTo(px(0.36), py(0.14)); ctx.lineTo(px(0.64), py(0.14));
    ctx.lineTo(px(0.74), py(0.66)); ctx.lineTo(px(0.70), py(0.84));
    ctx.lineTo(px(0.30), py(0.84)); ctx.lineTo(px(0.26), py(0.66));
    ctx.closePath();
    const fg = ctx.createLinearGradient(0, py(0.14), 0, py(0.84));
    fg.addColorStop(0, '#475569'); fg.addColorStop(0.45, '#ea580c'); fg.addColorStop(0.85, '#dc2626'); fg.addColorStop(1, '#fbbf24');
    ctx.fillStyle = fg; ctx.fill(); ctx.strokeStyle = '#cbd5e1'; ctx.lineWidth = 2; ctx.stroke();
    rrect(px(0.31), py(0.25), px(0.38), 22, 5, 'rgba(15,23,42,0.72)', 'rgba(253,230,138,0.45)');
    txt('500°C: 3Fe₂O₃+CO → 2Fe₃O₄', px(0.5), py(0.25) + 11, '#fde68a', 9.5, 'center', false, px(0.35));
    rrect(px(0.29), py(0.49), px(0.42), 22, 5, 'rgba(15,23,42,0.72)', 'rgba(254,240,138,0.45)');
    txt('900°C: FeO+CO → Fe+CO₂', px(0.5), py(0.49) + 11, '#fef08a', 9.5, 'center', false, px(0.39));
    arr(px(0.08), py(0.74), px(0.28), py(0.74), '#f87171', 2);
    txt('هواء ساخن', px(0.15), py(0.67), '#fca5a5', 9.5, 'center', true, px(0.20));
    arr(px(0.72), py(0.74), px(0.92), py(0.74), '#60a5fa', 2);
    txt('خبث CaSiO₃', px(0.85), py(0.67), '#93c5fd', 9.5, 'center', true, px(0.20));
    txt(`حديد منصهر بالقاعدة • ${sv} °م`, px(0.5), py(0.93), '#fde047', 11);
  } else if (sk === 'chem_iron_ions') {
    const bh = usableH * 0.48, bw = Math.min(64, w * 0.19);
    beaker(px(0.20), py(0.78), bw, bh, 'rgba(74,222,128,0.45)', 'Fe²⁺ + NaOH');
    txt('أبيض مخضر', px(0.20), py(0.48), '#bbf7d0', 9.5, 'center', true, bw + 12);
    beaker(px(0.50), py(0.78), bw, bh, 'rgba(180,83,9,0.75)', 'Fe³⁺ + NaOH');
    txt('بني محمر', px(0.50), py(0.48), '#fed7aa', 9.5, 'center', true, bw + 12);
    beaker(px(0.80), py(0.78), bw, bh, sv >= 2 ? 'rgba(185,28,28,0.85)' : 'rgba(248,113,113,0.5)', 'Fe³⁺ + KSCN');
    txt('أحمر دموي', px(0.80), py(0.48), '#fecaca', 9.5, 'center', true, bw + 12);
    rrect(16, py(0.06), w - 32, 26, 6, 'rgba(148,163,184,0.16)', '#64748b');
    txt('الخمول: طبقة رقيقة متماسكة غير مسامية من Fe₃O₄ تحمي الحديد', px(0.5), py(0.06) + 13, '#e2e8f0', 10, 'center', true, w - 44);

  // ---------------- UNIT 2 ----------------
  } else if (sk === 'chem_energy_forms') {
    const cx = px(0.5), cy = py(0.52);
    [['كيميائية', -0.28, -0.24, '#f59e0b'], ['حرارية', 0.28, -0.24, '#ef4444'], ['كهربائية', 0.28, 0.24, '#38bdf8'], ['ضوئية', -0.28, 0.24, '#facc15'], ['ميكانيكية', 0, -0.38, '#10b981']].forEach(([lbl, dx, dy, col]) => {
      const tx = cx + px(dx), ty = cy + usableH * dy;
      arr(cx, cy, tx, ty, col, 1.8);
      rrect(tx - 40, ty - 13, 80, 26, 8, 'rgba(15,23,42,0.92)', col);
      txt(lbl, tx, ty, col, 10.5);
    });
    rrect(cx - 46, cy - 15, 92, 30, 10, '#0f172a', '#e2e8f0');
    txt('تحول الطاقة ⇌', cx, cy, '#ffffff', 11);
  } else if (sk === 'chem_k_water_exo') {
    beaker(px(0.5), py(0.86), px(0.42), usableH * 0.46, 'rgba(56,189,248,0.32)', 'ماء H₂O + فينولفثالين');
    ctx.beginPath(); ctx.arc(px(0.5), py(0.54), 9, 0, Math.PI * 2); ctx.fillStyle = '#cbd5e1'; ctx.fill();
    for (let i = 0; i < 6; i++) {
      ctx.beginPath(); ctx.arc(px(0.5) - 18 + i * 7, py(0.44) - (i % 3) * 14, 5 + (sv / 25), 0, Math.PI * 2);
      ctx.fillStyle = i % 2 ? '#a855f7' : '#f97316'; ctx.fill();
    }
    txt('قطعة K + لهب أرجواني (H₂ مشتعل)', px(0.5), py(0.14), '#fdba74', 11.5);
    txt('تفاعل طارد للحرارة ΔH < 0 🔥', px(0.5), py(0.28), '#fca5a5', 11);
  } else if (sk === 'chem_nh4no3_endo') {
    rrect(px(0.10), py(0.28), px(0.24), 34, 10, 'rgba(203,213,225,0.2)', '#94a3b8');
    txt('NH₄NO₃', px(0.22), py(0.28) + 17, '#fff', 11, 'center', false);
    ctx.beginPath(); ctx.moveTo(px(0.34), py(0.32)); ctx.quadraticCurveTo(px(0.55), py(0.18), px(0.72), py(0.44));
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 3; ctx.stroke();
    beaker(px(0.74), py(0.86), px(0.28), usableH * 0.42, 'rgba(56,189,248,0.25)', 'جمع الغاز فوق الماء');
    txt('↑ غاز N₂O', px(0.74), py(0.32), '#7dd3fc', 10.5);
    txt('🔥 تسخين مستمر (ماص ΔH > 0)', px(0.25), py(0.74), '#fbbf24', 10.5, 'center', true, px(0.42));
  } else if (sk === 'chem_system_surroundings') {
    rrect(px(0.08), py(0.08), px(0.84), usableH * 0.84, 14, 'rgba(30,41,59,0.45)', '#64748b');
    txt('الوسط المحيط (Surroundings)', px(0.5), py(0.17), '#94a3b8', 11);
    beaker(px(0.5), py(0.82), px(0.36), usableH * 0.42, sv >= 0 ? 'rgba(56,189,248,0.3)' : 'rgba(249,115,22,0.38)', 'حدود النظام');
    txt('النظام الكيميائي', px(0.5), py(0.66), '#fff', 10.5);
    if (sv >= 0) { arr(px(0.14), py(0.58), px(0.31), py(0.58), '#38bdf8'); arr(px(0.86), py(0.58), px(0.69), py(0.58), '#38bdf8'); txt('امتصاص حرارة (+q)', px(0.5), py(0.30), '#7dd3fc', 11); }
    else { arr(px(0.31), py(0.58), px(0.14), py(0.58), '#f97316'); arr(px(0.69), py(0.58), px(0.86), py(0.58), '#f97316'); txt('انطلاق حرارة (−q)', px(0.5), py(0.30), '#fdba74', 11); }
  } else if (sk === 'chem_endo_exo_curves') {
    const exo = sv <= 0;
    ctx.strokeStyle = '#94a3b8'; ctx.lineWidth = 1.6;
    ctx.beginPath(); ctx.moveTo(px(0.14), py(0.08)); ctx.lineTo(px(0.14), py(0.88)); ctx.lineTo(px(0.92), py(0.88)); ctx.stroke();
    txt('H', px(0.08), py(0.14), '#cbd5e1', 11, 'center', false);
    const yR = exo ? py(0.24) : py(0.70), yP = exo ? py(0.72) : py(0.24);
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(px(0.18), yR); ctx.lineTo(px(0.38), yR);
    ctx.quadraticCurveTo(px(0.52), Math.min(yR, yP) - 24, px(0.66), yP); ctx.lineTo(px(0.88), yP); ctx.stroke();
    arr(px(0.52), yR, px(0.52), yP, exo ? '#ef4444' : '#10b981', 2.4);
    txt('متفاعلات', px(0.28), yR - 14, '#7dd3fc', 10.5);
    txt('نواتج', px(0.77), yP - 14, '#6ee7b7', 10.5);
    txt(exo ? 'طارد للحرارة (ΔH < 0)' : 'ماص للحرارة (ΔH > 0)', px(0.55), py(0.94), exo ? '#fca5a5' : '#a7f3d0', 11);
  } else if (sk === 'chem_water_heating_curve') {
    const pts = [[px(0.14), py(0.82)], [px(0.28), py(0.60)], [px(0.48), py(0.60)], [px(0.64), py(0.30)], [px(0.82), py(0.30)], [px(0.91), py(0.12)]];
    ctx.strokeStyle = '#64748b'; ctx.beginPath(); ctx.moveTo(px(0.14), py(0.08)); ctx.lineTo(px(0.14), py(0.86)); ctx.lineTo(px(0.92), py(0.86)); ctx.stroke();
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 3; ctx.beginPath();
    pts.forEach(([x, y], i) => i ? ctx.lineTo(x, y) : ctx.moveTo(x, y)); ctx.stroke();
    txt('0°C انصهار (+6 kJ)', px(0.38), py(0.50), '#fde047', 10);
    txt('100°C تبخر (+40.7 kJ)', px(0.73), py(0.20), '#fca5a5', 10);
    ctx.beginPath(); ctx.arc(px(0.14 + (sv / 100) * 0.76), py(0.45), 6, 0, Math.PI * 2); ctx.fillStyle = '#10b981'; ctx.fill();
    txt('كمية الحرارة المضافة ←', px(0.53), py(0.94), '#94a3b8', 10);
  } else if (sk === 'chem_bomb_calorimeter') {
    rrect(px(0.20), py(0.12), px(0.60), usableH * 0.74, 12, 'rgba(56,189,248,0.22)', '#94a3b8');
    rrect(px(0.34), py(0.30), px(0.32), usableH * 0.42, 10, '#334155', '#fbbf24');
    txt('وعاء الاحتراق + O₂', px(0.5), py(0.51), '#fde047', 10.5, 'center', true, px(0.28));
    ctx.strokeStyle = '#ef4444'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(px(0.72), py(0.06)); ctx.lineTo(px(0.72), py(0.78)); ctx.stroke();
    txt('ترمومتر ΔT', px(0.86), py(0.24), '#fca5a5', 10);
    txt('ماء معزول', px(0.27), py(0.22), '#7dd3fc', 10);

  // ---------------- UNIT 3 ----------------
  } else if (sk === 'chem_zn_cuso4_redox') {
    beaker(px(0.5), py(0.84), px(0.44), usableH * 0.56, 'rgba(37,99,235,0.45)', 'محلول CuSO₄ الأزرق');
    rrect(px(0.46), py(0.12), px(0.08), usableH * 0.58, 4, '#94a3b8', '#e2e8f0');
    rrect(px(0.45), py(0.52), px(0.10), usableH * 0.24, 3, '#b45309', '#f59e0b');
    txt('Zn', px(0.5), py(0.20), '#fff', 10.5, 'center', false);
    txt('Zn → Zn²⁺ + 2e⁻', px(0.21), py(0.44), '#7dd3fc', 10, 'center', false, px(0.34));
    txt('Cu²⁺ + 2e⁻ → Cu↓', px(0.79), py(0.58), '#fdba74', 10, 'center', false, px(0.34));
  } else if (sk === 'chem_porous_cell') {
    beaker(px(0.5), py(0.86), px(0.54), usableH * 0.52, 'rgba(56,189,248,0.2)', '');
    ctx.setLineDash([4, 4]); ctx.strokeStyle = '#fbbf24'; ctx.beginPath(); ctx.moveTo(px(0.5), py(0.34)); ctx.lineTo(px(0.5), py(0.86)); ctx.stroke(); ctx.setLineDash([]);
    rrect(px(0.30), py(0.26), 14, usableH * 0.44, 2, '#94a3b8', '#fff'); rrect(px(0.66), py(0.26), 14, usableH * 0.44, 2, '#d97706', '#fff');
    ctx.strokeStyle = '#fde047'; ctx.beginPath(); ctx.moveTo(px(0.32), py(0.26)); ctx.lineTo(px(0.32), py(0.10)); ctx.lineTo(px(0.68), py(0.10)); ctx.lineTo(px(0.68), py(0.26)); ctx.stroke();
    txt('حاجز مسامي', px(0.5), py(0.94), '#fde047', 10.5);
    txt('Zn (−)', px(0.20), py(0.48), '#e2e8f0', 10.5); txt('Cu (+)', px(0.82), py(0.48), '#fdba74', 10.5);
  } else if (sk === 'chem_daniell_cell') {
    beaker(px(0.24), py(0.86), px(0.26), usableH * 0.44, 'rgba(148,163,184,0.25)', 'ZnSO₄');
    beaker(px(0.76), py(0.86), px(0.26), usableH * 0.44, 'rgba(37,99,235,0.45)', 'CuSO₄');
    rrect(px(0.20), py(0.26), 14, usableH * 0.44, 2, '#cbd5e1', '#fff'); rrect(px(0.76), py(0.26), 14, usableH * 0.44, 2, '#b45309', '#fff');
    ctx.strokeStyle = '#facc15'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(px(0.22), py(0.26)); ctx.lineTo(px(0.22), py(0.08)); ctx.lineTo(px(0.78), py(0.08)); ctx.lineTo(px(0.78), py(0.26)); ctx.stroke();
    rrect(px(0.5) - 28, py(0.02), 56, 22, 6, '#0f172a', '#10b981'); txt('1.10 V', px(0.5), py(0.02) + 11, '#4ade80', 10.5, 'center', false);
    ctx.strokeStyle = '#e2e8f0'; ctx.lineWidth = 6; ctx.beginPath();
    ctx.moveTo(px(0.30), py(0.66)); ctx.lineTo(px(0.30), py(0.30)); ctx.lineTo(px(0.70), py(0.30)); ctx.lineTo(px(0.70), py(0.66)); ctx.stroke();
    txt('قنطرة ملحية U', px(0.5), py(0.38), '#fde047', 10.5);
  } else if (sk === 'chem_she_cell') {
    beaker(px(0.25), py(0.86), px(0.28), usableH * 0.42, 'rgba(148,163,184,0.28)', 'Zn | ZnSO₄');
    beaker(px(0.75), py(0.86), px(0.28), usableH * 0.42, 'rgba(220,38,38,0.22)', 'H₂(1 atm) | H⁺');
    rrect(px(0.72), py(0.30), 12, usableH * 0.38, 2, '#475569', '#e2e8f0');
    arr(px(0.92), py(0.38), px(0.78), py(0.38), '#38bdf8', 2); txt('H₂', px(0.92), py(0.29), '#7dd3fc', 10, 'center', false);
    rrect(px(0.5) - 28, py(0.05), 56, 22, 6, '#0f172a', '#f59e0b'); txt('+0.76 V', px(0.5), py(0.05) + 11, '#fde047', 10.5, 'center', false);
    txt('قطب البلاتين E°=0', px(0.75), py(0.20), '#fca5a5', 10, 'center', true, px(0.4));
  } else if (sk === 'chem_cells_trio') {
    [[0.20, 36, usableH * 0.46, 'Zn-C جافة 1.5V', '#64748b'], [0.50, 36, usableH * 0.46, 'قاعدية KOH 1.5V', '#f59e0b'], [0.80, 46, usableH * 0.22, 'زئبق 1.35V', '#94a3b8']].forEach(([rx, bw, bh, lbl, col]) => {
      const cy = py(0.46);
      rrect(px(rx) - bw / 2, cy - bh / 2, bw, bh, 6, col, '#e2e8f0');
      txt(lbl, px(rx), py(0.80), '#e2e8f0', 10, 'center', true, px(0.28));
    });
  } else if (sk === 'chem_dry_cell_leclanche') {
    rrect(px(0.36), py(0.14), px(0.28), usableH * 0.72, 8, '#475569', '#cbd5e1');
    rrect(px(0.48), py(0.06), px(0.04), usableH * 0.74, 2, '#0f172a', '#f8fafc');
    txt('جرافيت (+)', px(0.81), py(0.28), '#fca5a5', 10.5);
    txt('وعاء Zn (−)', px(0.19), py(0.48), '#93c5fd', 10.5);
    txt('NH₄Cl + MnO₂', px(0.81), py(0.64), '#fde68a', 10);
  } else if (sk === 'chem_alkaline_cell') {
    rrect(px(0.35), py(0.14), px(0.30), usableH * 0.72, 10, '#78350f', '#fbbf24');
    rrect(px(0.47), py(0.10), px(0.06), usableH * 0.74, 2, '#e2e8f0', '#fff');
    txt('Zn مسامي (−)', px(0.18), py(0.44), '#7dd3fc', 10.5);
    txt('إلكتروليت KOH', px(0.82), py(0.42), '#6ee7b7', 10.5);
    txt('MnO₂ (+)', px(0.82), py(0.66), '#fcd34d', 10.5);
  } else if (sk === 'chem_mercury_button_cell') {
    rrect(px(0.26), py(0.26), px(0.48), usableH * 0.48, 22, '#64748b', '#e2e8f0');
    rrect(px(0.30), py(0.32), px(0.40), usableH * 0.16, 6, '#38bdf8', '#fff');
    rrect(px(0.30), py(0.52), px(0.40), usableH * 0.16, 6, '#dc2626', '#fff');
    txt('Zn (−)', px(0.5), py(0.40), '#fff', 10.5);
    txt('HgO (+)', px(0.5), py(0.60), '#fff', 10.5);
    txt('خلية زر للساعات (1.35 V)', px(0.5), py(0.84), '#cbd5e1', 10.5);
  } else if (sk === 'chem_lead_battery') {
    rrect(px(0.14), py(0.14), px(0.72), usableH * 0.68, 8, '#1e293b', '#38bdf8');
    for (let i = 0; i < 6; i++) {
      const ax = px(0.17) + i * px(0.112);
      rrect(ax, py(0.22), 11, usableH * 0.52, 2, '#94a3b8', '#fff');
      rrect(ax + 13, py(0.22), 11, usableH * 0.52, 2, '#991b1b', '#fca5a5');
    }
    txt(`6 خلايا × 2V = 12V  |  كثافة H₂SO₄ = ${(sv / 100).toFixed(2)}`, px(0.5), py(0.92), '#fde047', 10.5);
  } else if (sk === 'chem_h2o2_fuel_cell') {
    rrect(px(0.25), py(0.18), px(0.50), usableH * 0.62, 8, 'rgba(16,185,129,0.2)', '#34d399');
    rrect(px(0.34), py(0.22), 12, usableH * 0.54, 2, '#475569', '#e2e8f0');
    rrect(px(0.64), py(0.22), 12, usableH * 0.54, 2, '#475569', '#e2e8f0');
    arr(px(0.08), py(0.48), px(0.25), py(0.48), '#38bdf8', 2); txt('H₂', px(0.12), py(0.36), '#7dd3fc', 11, 'center', false);
    arr(px(0.92), py(0.48), px(0.75), py(0.48), '#ef4444', 2); txt('O₂', px(0.88), py(0.36), '#fca5a5', 11, 'center', false);
    txt('كهرباء + ماء نقي H₂O للفضاء', px(0.5), py(0.90), '#6ee7b7', 10.5);
  } else if (sk === 'chem_cucl2_electrolysis') {
    beaker(px(0.5), py(0.88), px(0.44), usableH * 0.54, 'rgba(37,99,235,0.4)', 'محلول CuCl₂');
    rrect(px(0.39), py(0.24), 12, usableH * 0.52, 2, '#1e293b', '#94a3b8');
    rrect(px(0.59), py(0.24), 12, usableH * 0.52, 2, '#1e293b', '#b45309');
    txt('أنود (+): Cl₂↑', px(0.18), py(0.42), '#a3e635', 10.5);
    txt('كاثود (−): Cu↓', px(0.82), py(0.42), '#fdba74', 10.5);
    rrect(px(0.5) - 32, py(0.04), 64, 22, 6, '#0f172a', '#fbbf24'); txt('بطارية DC', px(0.5), py(0.04) + 11, '#fde047', 10);
  } else if (sk === 'chem_electroplating') {
    beaker(px(0.5), py(0.88), px(0.46), usableH * 0.54, 'rgba(203,213,225,0.22)', 'محلول AgNO₃');
    rrect(px(0.36), py(0.24), 14, usableH * 0.52, 2, '#f8fafc', '#cbd5e1');
    rrect(px(0.62), py(0.28), 12, usableH * 0.46, 4, '#e2e8f0', '#38bdf8');
    arr(px(0.40), py(0.54), px(0.61), py(0.54), '#7dd3fc', 2);
    txt('فضة Ag (+)', px(0.18), py(0.44), '#f8fafc', 10.5);
    txt('ملعقة Ag↓ (−)', px(0.83), py(0.44), '#7dd3fc', 10.5);
    txt('Ag⁺', px(0.5), py(0.45), '#fde047', 10.5, 'center', false);

  // ---------------- UNIT 4 ----------------
  } else if (sk === 'chem_mass_spectrometer') {
    rrect(px(0.08), py(0.40), px(0.18), 36, 6, '#334155', '#fbbf24'); txt('أيونات', px(0.17), py(0.40) + 18, '#fde047', 10.5);
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2.5;
    ctx.beginPath(); ctx.moveTo(px(0.26), py(0.50)); ctx.quadraticCurveTo(px(0.48), py(0.44), px(0.84), py(0.18)); ctx.stroke();
    ctx.strokeStyle = '#f472b6';
    ctx.beginPath(); ctx.moveTo(px(0.26), py(0.50)); ctx.quadraticCurveTo(px(0.52), py(0.56), px(0.84), py(0.78)); ctx.stroke();
    txt('⁴He (أخف ← انحراف أكبر)', px(0.64), py(0.12), '#7dd3fc', 10);
    txt('¹²C (أثقل ← انحراف أقل)', px(0.64), py(0.88), '#f9a8d4', 10);
  } else if (sk === 'chem_binding_energy_curve') {
    const pts = [[px(0.14), py(0.80)], [px(0.23), py(0.46)], [px(0.36), py(0.32)], [px(0.48), py(0.20)], [px(0.68), py(0.28)], [px(0.88), py(0.36)]];
    ctx.strokeStyle = '#64748b'; ctx.beginPath(); ctx.moveTo(px(0.14), py(0.10)); ctx.lineTo(px(0.14), py(0.86)); ctx.lineTo(px(0.92), py(0.86)); ctx.stroke();
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 3; ctx.beginPath();
    pts.forEach(([x, y], i) => i ? ctx.lineTo(x, y) : ctx.moveTo(x, y)); ctx.stroke();
    ctx.beginPath(); ctx.arc(px(0.48), py(0.20), 6, 0, Math.PI * 2); ctx.fillStyle = '#fbbf24'; ctx.fill();
    txt('الذروة ⁵⁶Fe (8.8 MeV)', px(0.52), py(0.10), '#fde047', 10.5);
    txt('الاندماج ↗', px(0.26), py(0.60), '#7dd3fc', 10);
    txt('↖ الانشطار (U)', px(0.76), py(0.48), '#fca5a5', 10);
  } else if (sk === 'chem_stability_belt') {
    ctx.strokeStyle = '#64748b'; ctx.beginPath(); ctx.moveTo(px(0.14), py(0.10)); ctx.lineTo(px(0.14), py(0.86)); ctx.lineTo(px(0.90), py(0.86)); ctx.stroke();
    ctx.setLineDash([4, 4]); ctx.strokeStyle = '#94a3b8'; ctx.beginPath(); ctx.moveTo(px(0.14), py(0.86)); ctx.lineTo(px(0.86), py(0.16)); ctx.stroke(); ctx.setLineDash([]);
    ctx.strokeStyle = '#10b981'; ctx.lineWidth = 8; ctx.beginPath(); ctx.moveTo(px(0.16), py(0.84)); ctx.quadraticCurveTo(px(0.45), py(0.60), px(0.82), py(0.12)); ctx.stroke();
    txt('حزام الاستقرار (N/Z ≈ 1..1.5)', px(0.56), py(0.20), '#6ee7b7', 10);
    txt('β⁻ فوق الحزام', px(0.32), py(0.34), '#7dd3fc', 10);
    txt('β⁺ تحت الحزام', px(0.70), py(0.74), '#fca5a5', 10);
  } else if (sk === 'chem_alpha_beta_gamma_shield') {
    const bx = [px(0.35), px(0.56), px(0.78)];
    rrect(bx[0], py(0.12), 6, usableH * 0.68, 1, '#f8fafc', '#94a3b8'); txt('ورقة', bx[0] + 3, py(0.88), '#e2e8f0', 10);
    rrect(bx[1], py(0.12), 14, usableH * 0.68, 2, '#94a3b8', '#e2e8f0'); txt('ألومنيوم', bx[1] + 7, py(0.88), '#7dd3fc', 10);
    rrect(bx[2], py(0.12), 26, usableH * 0.68, 3, '#475569', '#fbbf24'); txt('رصاص', bx[2] + 13, py(0.88), '#fde047', 10);
    arr(px(0.12), py(0.26), bx[0], py(0.26), '#ef4444', 3); txt('α', px(0.07), py(0.26), '#fca5a5', 12, 'center', false);
    arr(px(0.12), py(0.46), bx[1], py(0.46), '#38bdf8', 2.5); txt('β', px(0.07), py(0.46), '#7dd3fc', 12, 'center', false);
    arr(px(0.12), py(0.66), px(0.94), py(0.66), '#a855f7', 2); txt('γ', px(0.07), py(0.66), '#d8b4fe', 12, 'center', false);
  } else if (sk === 'chem_u235_chain_fission') {
    arr(px(0.07), py(0.50), px(0.24), py(0.50), '#facc15', 2); txt('¹₀n', px(0.12), py(0.40), '#fde047', 10.5, 'center', false);
    ctx.beginPath(); ctx.arc(px(0.30), py(0.50), 18, 0, Math.PI * 2); ctx.fillStyle = '#38bdf8'; ctx.fill(); txt('U-235', px(0.30), py(0.50), '#fff', 10, 'center', false);
    arr(px(0.36), py(0.46), px(0.58), py(0.24), '#10b981', 2); arr(px(0.36), py(0.54), px(0.58), py(0.76), '#f97316', 2);
    rrect(px(0.58), py(0.16), 46, 28, 6, '#059669', '#fff'); txt('Ba', px(0.58) + 23, py(0.16) + 14, '#fff', 10.5, 'center', false);
    rrect(px(0.58), py(0.70), 46, 28, 6, '#d97706', '#fff'); txt('Kr', px(0.58) + 23, py(0.70) + 14, '#fff', 10.5, 'center', false);
    for (let k = 0; k < Math.min(3, Math.round(sv)); k++) arr(px(0.38), py(0.50), px(0.92), py(0.22 + k * 0.28), '#facc15', 1.6);
    txt('+ 3 نيوترونات متسلسلة', px(0.74), py(0.50), '#fde047', 10);
  } else if (sk === 'chem_nuclear_reactor_5parts') {
    rrect(px(0.06), py(0.28), px(0.24), usableH * 0.44, 8, '#334155', '#f59e0b'); txt('قلب U-235', px(0.18), py(0.35), '#fde047', 10);
    const rodDep = usableH * (0.12 + (sv / 100) * 0.22);
    for (let i = 0; i < 3; i++) rrect(px(0.12 + i * 0.055), py(0.24), 5, rodDep, 2, '#94a3b8', '#ef4444');
    arr(px(0.30), py(0.44), px(0.42), py(0.44), '#ef4444', 2.2);
    rrect(px(0.42), py(0.32), px(0.22), usableH * 0.26, 6, '#1e3a8a', '#38bdf8'); txt('مبادل حراري', px(0.53), py(0.45), '#fff', 10);
    arr(px(0.64), py(0.44), px(0.72), py(0.44), '#e2e8f0', 2);
    rrect(px(0.72), py(0.32), px(0.22), usableH * 0.26, 6, '#065f46', '#10b981'); txt('توربين ⚡', px(0.83), py(0.45), '#a7f3d0', 10);
    txt('قضبان التحكم بالكادميوم', px(0.24), py(0.84), '#fca5a5', 10);
  } else if (sk === 'chem_radioisotope_bone_scan') {
    ctx.beginPath(); ctx.arc(px(0.46), py(0.22), 16, 0, Math.PI * 2); ctx.fillStyle = '#475569'; ctx.fill();
    rrect(px(0.39), py(0.34), px(0.14), usableH * 0.44, 8, '#334155', '#94a3b8');
    ctx.beginPath(); ctx.arc(px(0.46), py(0.52), 7, 0, Math.PI * 2); ctx.fillStyle = '#10b981'; ctx.fill();
    arr(px(0.48), py(0.52), px(0.70), py(0.32), '#34d399', 2);
    rrect(px(0.68), py(0.18), px(0.24), 42, 6, '#0f172a', '#34d399'); txt('كاميرا جاما', px(0.80), py(0.18) + 21, '#6ee7b7', 10);
    txt('مقتفي Tc-99 للتصوير التشخيصي', px(0.5), py(0.90), '#a7f3d0', 10.5);
  } else if (sk === 'chem_gamma_radiotherapy') {
    rrect(px(0.22), py(0.54), px(0.56), 24, 6, '#334155', '#94a3b8'); txt('مريض العلاج الإشعاعي', px(0.5), py(0.54) + 12, '#e2e8f0', 10);
    const rad = (sv * Math.PI) / 180;
    const gx = px(0.5) + Math.cos(rad) * px(0.22), gy = py(0.54) - Math.abs(Math.sin(rad)) * usableH * 0.34 - 16;
    rrect(gx - 22, gy - 12, 44, 24, 6, '#7c3aed', '#e2e8f0'); txt('⁶⁰Co', gx, gy, '#fff', 10, 'center', false);
    arr(gx, gy + 12, px(0.5), py(0.54), '#a855f7', 2.5);
    txt('تركيز أشعة جاما على الورم الخبيث', px(0.5), py(0.84), '#d8b4fe', 10.5);
  } else if (sk === 'chem_fusion_hbomb') {
    ctx.beginPath(); ctx.arc(px(0.24), py(0.46), 18, 0, Math.PI * 2); ctx.fillStyle = '#38bdf8'; ctx.fill(); txt('²H', px(0.24), py(0.46), '#fff', 11, 'center', false);
    ctx.beginPath(); ctx.arc(px(0.42), py(0.46), 20, 0, Math.PI * 2); ctx.fillStyle = '#10b981'; ctx.fill(); txt('³H', px(0.42), py(0.46), '#fff', 11, 'center', false);
    arr(px(0.51), py(0.46), px(0.68), py(0.46), '#fbbf24', 2.5);
    ctx.beginPath(); ctx.arc(px(0.78), py(0.46), 24, 0, Math.PI * 2); ctx.fillStyle = '#f59e0b'; ctx.fill(); txt('⁴He + طاقة', px(0.78), py(0.72), '#fde047', 11);

  // ---------------- UNIT 5 ----------------
  } else if (sk === 'chem_u5_nitrogen_rings') {
    poly(px(0.22), py(0.48), 26, 6, '#38bdf8', true); txt('N', px(0.22) + 22, py(0.48), '#fbbf24', 11, 'center', false);
    poly(px(0.50), py(0.48), 24, 5, '#10b981', true); txt('N', px(0.50), py(0.48) + 22, '#fbbf24', 11, 'center', false);
    poly(px(0.76), py(0.48), 26, 6, '#f472b6', false); txt('NH₂', px(0.76) + 34, py(0.48), '#f9a8d4', 10.5, 'center', false);
    txt('مركبات نيتروجينية حلقية وأروماتية حيوية', px(0.5), py(0.84), '#7dd3fc', 11);
  } else if (sk === 'chem_amines_123') {
    const r = Math.round(sv);
    [['NH₃', 'أمونيا'], ['R–NH₂', 'أمين أولي'], ['R₂NH', 'أمين ثانوي'], ['R₃N', 'أمين ثالثي']].forEach(([f, nm], i) => {
      const cx = px(0.14 + i * 0.24), cw = px(0.21);
      rrect(cx - cw / 2, py(0.28), cw, usableH * 0.36, 8, i === r ? 'rgba(16,185,129,0.32)' : 'rgba(15,23,42,0.82)', i === r ? '#34d399' : '#475569');
      txt(f, cx, py(0.40), '#fde047', 11, 'center', false, cw - 6);
      txt(nm, cx, py(0.54), '#cbd5e1', 9.5, 'center', true, cw - 6);
    });
    txt('استبدال ذرات H في NH₃ بمجموعات ألكيل R', px(0.5), py(0.82), '#6ee7b7', 11);
  } else if (sk === 'chem_piperidine_pyridine_aniline') {
    const cyH = py(0.42);
    poly(px(0.19), cyH, 24, 6, '#38bdf8', false, Math.PI / 6);
    rrect(px(0.19) - 13, cyH + 17, 26, 15, 5, '#0c4a6e', '#38bdf8');
    txt('NH', px(0.19), cyH + 24.5, '#e0f2fe', 8.5, 'center', false);
    txt('بيبيريدين (مشبع)', px(0.19), py(0.72), '#7dd3fc', 10, 'center', true, px(0.28));

    poly(px(0.49), cyH, 24, 6, '#10b981', true, Math.PI / 6);
    rrect(px(0.49) - 10, cyH + 17, 20, 15, 5, '#064e3b', '#10b981');
    txt('N', px(0.49), cyH + 24.5, '#d1fae5', 8.5, 'center', false);
    txt('بيريدين (أروماتي)', px(0.49), py(0.72), '#6ee7b7', 10, 'center', true, px(0.28));

    poly(px(0.76), cyH, 24, 6, '#f59e0b', true);
    ctx.strokeStyle = '#fde047'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(px(0.76) + 24, cyH); ctx.lineTo(px(0.76) + 33, cyH); ctx.stroke();
    txt('NH₂', px(0.76) + 46, cyH, '#fde047', 9.5, 'center', false);
    txt('أنيلين (أروماتي)', px(0.76), py(0.72), '#fde047', 10, 'center', true, px(0.26));
  } else if (sk === 'chem_amides_urea_benzamide') {
    [['أسيتاميد', 'CH₃CONH₂'], ['نيكوتيناميد', 'C₅H₄N-CONH₂'], ['بنزاميد', 'C₆H₅CONH₂'], ['يوريا', 'NH₂CONH₂']].forEach(([nm, fm], i) => {
      const cx = px(0.14 + i * 0.24), cw = px(0.21);
      rrect(cx - cw / 2, py(0.26), cw, usableH * 0.38, 8, i + 1 === Math.round(sv) ? 'rgba(56,189,248,0.28)' : 'rgba(15,23,42,0.8)', '#38bdf8');
      txt(nm, cx, py(0.38), '#fde047', 10, 'center', true, cw - 4);
      txt(fm, cx, py(0.53), '#e2e8f0', 8.5, 'center', false, cw - 4);
    });
    txt('المجموعة الوظيفية للأميد –CO–NH₂ متعادلة', px(0.5), py(0.82), '#7dd3fc', 11);
  } else if (sk === 'chem_nitriles_reactions') {
    rrect(px(0.06), py(0.38), px(0.22), 36, 8, '#1e293b', '#f59e0b'); txt('R–C≡N', px(0.17), py(0.38) + 18, '#fde047', 11, 'center', false);
    arr(px(0.28), py(0.42), px(0.50), py(0.26), '#38bdf8', 2); txt('+ 2H₂O / H⁺', px(0.39), py(0.22), '#7dd3fc', 9.5, 'center', false);
    rrect(px(0.50), py(0.18), px(0.42), 32, 8, '#1e3a8a', '#38bdf8'); txt('R–COOH (حمض كربوكسيلي)', px(0.71), py(0.18) + 16, '#fff', 10);
    arr(px(0.28), py(0.52), px(0.50), py(0.68), '#10b981', 2); txt('+ 2H₂ / Ni', px(0.39), py(0.72), '#6ee7b7', 9.5, 'center', false);
    rrect(px(0.50), py(0.62), px(0.42), 32, 8, '#065f46', '#10b981'); txt('R–CH₂–NH₂ (أمين أولي)', px(0.71), py(0.62) + 16, '#fff', 10);
  } else if (sk === 'chem_amino_acids_types') {
    [['متعادلة (جلايسين/ألانين)', '–NH₂ = –COOH', '#10b981'], ['حمضية (أسبارتيك)', '–COOH إضافية', '#ef4444'], ['قاعدية (أرجينين)', '–NH₂ إضافية', '#38bdf8']].forEach(([t1, t2, c], i) => {
      rrect(px(0.08), py(0.12 + i * 0.28), px(0.84), usableH * 0.22, 8, 'rgba(15,23,42,0.85)', c);
      txt(t1, px(0.64), py(0.23 + i * 0.28), c, 10.5, 'center', true, px(0.44));
      txt(t2, px(0.26), py(0.23 + i * 0.28), '#e2e8f0', 10, 'center', true, px(0.32));
    });
  } else if (sk === 'chem_zwitterion_amphoteric') {
    const ph = sv;
    const state = ph < 5 ? 'وسط حمضي (+): ⁺H₃N–CH(R)–COOH ← للكاثود' : (ph > 9 ? 'وسط قاعدي (−): H₂N–CH(R)–COO⁻ ← للأنود' : 'أيون ثنائي القطب (Zwitterion): ⁺H₃N–CH(R)–COO⁻');
    rrect(px(0.07), py(0.20), px(0.86), usableH * 0.42, 10, 'rgba(56,189,248,0.18)', '#38bdf8');
    txt(`pH = ${ph}`, px(0.5), py(0.31), '#fde047', 12, 'center', false);
    txt(state, px(0.5), py(0.49), '#f8fafc', 10.5, 'center', true, px(0.80));
    txt('الخاصية الأمفوتيرية: تتفاعل مع الأحماض والقواعد', px(0.5), py(0.78), '#6ee7b7', 11);

  // ---------------- UNIT 6 ----------------
  } else if (sk === 'chem_biochem_sciences_map') {
    const links = ['الطب', 'علم الوراثة', 'الصيدلة', 'الزراعة', 'التغذية'];
    links.forEach((l, i) => {
      const a = (i * Math.PI * 2) / links.length - Math.PI / 2;
      const nx = px(0.5) + Math.cos(a) * px(0.30), ny = py(0.50) + Math.sin(a) * usableH * 0.34;
      arr(px(0.5), py(0.50), nx, ny, '#38bdf8', 1.6);
      rrect(nx - 36, ny - 13, 72, 26, 8, '#0f172a', '#10b981'); txt(l, nx, ny, '#a7f3d0', 10);
    });
    rrect(px(0.5) - 48, py(0.50) - 15, 96, 30, 10, '#1e3a8a', '#facc15'); txt('الكيمياء الحيوية', px(0.5), py(0.50), '#fff', 10.5);
  } else if (sk === 'chem_monosaccharide_fruits') {
    ctx.beginPath(); ctx.arc(px(0.32), py(0.46), 28, 0, Math.PI * 2); ctx.fillStyle = '#ef4444'; ctx.fill();
    txt('فركتوز (سكر الفواكه)', px(0.32), py(0.76), '#fca5a5', 10.5);
    for (let i = 0; i < 6; i++) { ctx.beginPath(); ctx.arc(px(0.62) + (i % 3) * 14, py(0.42) + Math.floor(i / 3) * 14, 7, 0, Math.PI * 2); ctx.fillStyle = '#a855f7'; ctx.fill(); }
    txt('جلوكوز (سكر العنب C₆H₁₂O₆)', px(0.68), py(0.76), '#d8b4fe', 10.5);
  } else if (sk === 'chem_glucose_fructose_rings') {
    txt('CHO–(CHOH)₄–CH₂OH ⇌', px(0.28), py(0.26), '#7dd3fc', 10.5, 'center', false, px(0.46));
    poly(px(0.74), py(0.26), 24, 6, '#38bdf8', false); txt('جلوكوز (سداسي)', px(0.74), py(0.44), '#7dd3fc', 9.5);
    txt('CH₂OH–CO–(CHOH)₃–CH₂OH ⇌', px(0.28), py(0.66), '#fde047', 10, 'center', false, px(0.46));
    poly(px(0.74), py(0.68), 22, 5, '#f59e0b', false, -Math.PI / 2); txt('فركتوز (خماسي)', px(0.74), py(0.86), '#fde047', 9.5);
  } else if (sk === 'chem_lactose_structure') {
    poly(px(0.30), py(0.46), 26, 6, '#38bdf8', false); txt('جالاكتوز', px(0.30), py(0.74), '#7dd3fc', 10.5);
    ctx.strokeStyle = '#facc15'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(px(0.30) + 26, py(0.46)); ctx.lineTo(px(0.70) - 26, py(0.46)); ctx.stroke();
    txt('–O–', px(0.5), py(0.38), '#fde047', 11, 'center', false);
    poly(px(0.70), py(0.46), 26, 6, '#10b981', false); txt('جلوكوز', px(0.70), py(0.74), '#6ee7b7', 10.5);
  } else if (sk === 'chem_sucrose_condensation') {
    poly(px(0.18), py(0.46), 22, 6, '#38bdf8', false); txt('جلوكوز', px(0.18), py(0.72), '#7dd3fc', 10);
    txt('+', px(0.30), py(0.46), '#fff', 13, 'center', false);
    poly(px(0.42), py(0.46), 20, 5, '#f59e0b', false, -Math.PI / 2); txt('فركتوز', px(0.42), py(0.72), '#fde047', 10);
    arr(px(0.50), py(0.46), px(0.60), py(0.46), '#ef4444', 2); txt('–H₂O', px(0.55), py(0.36), '#fca5a5', 10, 'center', false);
    poly(px(0.72), py(0.46), 20, 6, '#34d399', false); poly(px(0.86), py(0.46), 18, 5, '#34d399', false, -Math.PI / 2);
    txt('سكروز C₁₂H₂₂O₁₁', px(0.79), py(0.72), '#6ee7b7', 10.5);
  } else if (sk === 'chem_six_amino_acids') {
    ['جلايسين (H)', 'ألانين (CH₃)', 'فالين', 'ليوسين', 'جلوتاميك (حمضي)', 'فينيل ألانين'].forEach((nm, i) => {
      const col = i < 2 ? '#38bdf8' : '#10b981';
      const rx = px(0.06 + (i % 3) * 0.30), ry = py(0.14 + Math.floor(i / 3) * 0.42), cw = px(0.27);
      rrect(rx, ry, cw, usableH * 0.32, 7, '#0f172a', col);
      txt(nm, rx + cw / 2, ry + usableH * 0.16, col, 9.5, 'center', true, cw - 6);
    });
  } else if (sk === 'chem_peptide_bond_dipeptide') {
    rrect(px(0.06), py(0.36), px(0.25), 36, 6, '#1e293b', '#38bdf8'); txt('جلايسين', px(0.185), py(0.36) + 18, '#7dd3fc', 10);
    txt('+', px(0.33), py(0.36) + 18, '#fff', 12, 'center', false);
    rrect(px(0.35), py(0.36), px(0.23), 36, 6, '#1e293b', '#10b981'); txt('ألانين', px(0.465), py(0.36) + 18, '#6ee7b7', 10);
    arr(px(0.59), py(0.36) + 18, px(0.67), py(0.36) + 18, '#ef4444', 2); txt('–H₂O', px(0.63), py(0.26), '#fca5a5', 9.5, 'center', false);
    rrect(px(0.68), py(0.36), px(0.27), 36, 6, '#064e3b', '#facc15'); txt('رابطة ببتيدية', px(0.815), py(0.36) + 18, '#fde047', 10);
  } else if (sk === 'chem_saturated_unsaturated_fats') {
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 4;
    ctx.beginPath(); for (let i = 0; i < 8; i++) { const x = px(0.14 + i * 0.10), y = py(0.30) + (i % 2 ? -8 : 8); i ? ctx.lineTo(x, y) : ctx.moveTo(x, y); } ctx.stroke();
    txt('حمض البالمتيك المشبع (مستقيم — صلب)', px(0.5), py(0.16), '#7dd3fc', 10.5);
    ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 4;
    ctx.beginPath(); ctx.moveTo(px(0.14), py(0.68)); ctx.lineTo(px(0.36), py(0.64)); ctx.lineTo(px(0.54), py(0.76)); ctx.lineTo(px(0.82), py(0.84)); ctx.stroke();
    txt('حمض اللينولينيك غير المشبع (3 روابط C=C — سائل)', px(0.5), py(0.54), '#fde047', 10);
  } else if (sk === 'chem_enzyme_lock_key') {
    const gap = Math.max(0, px(0.22) * (1 - sv / 100));
    rrect(px(0.14), py(0.22), px(0.30), usableH * 0.44, 14, '#1e3a8a', '#38bdf8');
    ctx.fillStyle = '#071422'; ctx.fillRect(px(0.37), py(0.36), px(0.08), usableH * 0.18);
    txt('إنزيم E', px(0.27), py(0.45), '#fff', 11);
    rrect(px(0.44) + gap, py(0.36), px(0.22), usableH * 0.18, 8, '#10b981', '#a7f3d0');
    txt('ركيزة S', px(0.55) + gap, py(0.45), '#fff', 10.5);
    txt('تطابق القفل والمفتاح → خفض طاقة التنشيط', px(0.5), py(0.84), '#fde047', 10.5);

  // ---------------- UNIT 7 ----------------
  } else if (sk === 'chem_petro_products_grid') {
    ['لدائن وبلاستيك', 'أدوية وصبغات', 'ألياف صناعية', 'وقود وغازات'].forEach((pr, i) => {
      const rx = px(0.08 + (i % 2) * 0.44), ry = py(0.14 + Math.floor(i / 2) * 0.42), cw = px(0.40);
      rrect(rx, ry, cw, usableH * 0.34, 8, '#0f172a', '#fbbf24');
      txt(pr, rx + cw / 2, ry + usableH * 0.17, '#fde047', 11);
    });
  } else if (sk === 'chem_seismic_oil_trap') {
    rrect(px(0.08), py(0.10), px(0.22), 24, 5, '#475569', '#facc15'); txt('تفجير سيزمي', px(0.19), py(0.10) + 12, '#fff', 9.5);
    ctx.strokeStyle = '#38bdf8'; ctx.beginPath(); ctx.moveTo(px(0.19), py(0.22)); ctx.lineTo(px(0.5), py(0.52)); ctx.lineTo(px(0.84), py(0.22)); ctx.stroke();
    ctx.beginPath(); ctx.arc(px(0.5), py(0.86), 66, Math.PI, 0); ctx.fillStyle = '#dc2626'; ctx.fill();
    ctx.beginPath(); ctx.arc(px(0.5), py(0.86), 44, Math.PI, 0); ctx.fillStyle = '#0f172a'; ctx.fill();
    txt('غاز طبيعي (قمة)', px(0.5), py(0.46), '#fca5a5', 10);
    txt('نفط خام', px(0.5), py(0.64), '#fde047', 10.5);
    txt('ماء مالح (أسفل)', px(0.5), py(0.80), '#7dd3fc', 10);
  } else if (sk === 'chem_distillation_tower') {
    const lvls = [['غازات (<40°C)', '#93c5fd'], ['جازولين (40-175°)', '#fbbf24'], ['كيروسين (175-275°)', '#f97316'], ['ديزل وسولار', '#ea580c'], ['إسفلت وقار (>400°)', '#334155']];
    rrect(px(0.32), py(0.06), px(0.30), usableH * 0.84, 12, '#0f172a', '#cbd5e1');
    lvls.forEach(([nm, col], i) => {
      const yy = py(0.10 + i * 0.16);
      rrect(px(0.34), yy, px(0.26), usableH * 0.12, 4, col, '#fff');
      txt(nm, px(0.80), yy + usableH * 0.06, '#f1f5f9', 9.5, 'center', true, px(0.34));
    });
    txt('فرن 450°C', px(0.16), py(0.76), '#ef4444', 10);
  } else if (sk === 'chem_oil_fractions_uses') {
    [['غاز مسال LPG', 'تدفئة وطبخ'], ['جازولين', 'سيارات'], ['كيروسين', 'طائرات'], ['زيت ديزل', 'شاحنات وقطارات'], ['إسفلت', 'رصف الطرق']].forEach(([k, u], i) => {
      const yy = py(0.06 + i * 0.18);
      rrect(px(0.08), yy, px(0.84), usableH * 0.14, 5, 'rgba(15,23,42,0.85)', '#38bdf8');
      txt(k, px(0.70), yy + usableH * 0.07, '#7dd3fc', 10);
      txt(u, px(0.28), yy + usableH * 0.07, '#a7f3d0', 10);
    });
  } else if (sk === 'chem_gasoline_cars') {
    rrect(px(0.10), py(0.32), px(0.80), 24, 10, '#1e293b', '#64748b');
    const fw = Math.max(18, (sv / 100) * (px(0.80) - 4));
    rrect(px(0.10) + 2, py(0.32) + 2, fw, 20, 8, sv >= 90 ? '#10b981' : '#f59e0b', null);
    txt(`رقم الأوكتان: ${sv} (${sv >= 90 ? 'وقود ممتاز مقاوم للفرقعة' : 'قابل للفرقعة'})`, px(0.5), py(0.58), '#fde047', 11);
    txt('هبتان عادي = 0  |  أيزوأوكتان = 100', px(0.5), py(0.76), '#cbd5e1', 10.5);
  } else if (sk === 'chem_oil_consumption_87_13') {
    const dw = Math.min(116, px(0.32)), dh = usableH * 0.72, x0 = px(0.5) - dw / 2, y0 = py(0.14);
    const topH = dh * (sv / 100);
    rrect(x0, y0, dw, topH, 4, '#10b981', '#e2e8f0');
    rrect(x0, y0 + topH, dw, dh - topH, 4, '#475569', '#e2e8f0');
    txt(`${sv}% بتروكيماويات`, px(0.18), y0 + topH / 2, '#6ee7b7', 10, 'center', true, px(0.28));
    txt(`${100 - sv}% يستهلك كوقود`, px(0.82), y0 + topH + (dh - topH) / 2, '#fde047', 10, 'center', true, px(0.28));

  // ---------------- UNIT 8 ----------------
  } else if (sk === 'chem_fertilizer_taxonomy') {
    rrect(px(0.30), py(0.08), px(0.40), 26, 6, '#1e3a8a', '#38bdf8'); txt('الأسمدة الكيميائية', px(0.5), py(0.08) + 13, '#fff', 11);
    arr(px(0.5), py(0.08) + 26, px(0.27), py(0.36), '#94a3b8'); arr(px(0.5), py(0.08) + 26, px(0.73), py(0.36), '#94a3b8');
    rrect(px(0.08), py(0.36), px(0.38), usableH * 0.24, 6, '#0f172a', '#fbbf24'); txt('غير مباشرة (جير/دولوميت)', px(0.27), py(0.48), '#fde047', 10, 'center', true, px(0.34));
    rrect(px(0.54), py(0.36), px(0.38), usableH * 0.24, 6, '#0f172a', '#10b981'); txt('مباشرة (أساسية NPK)', px(0.73), py(0.48), '#6ee7b7', 10, 'center', true, px(0.34));
    txt('أحادية (N / P / K)  |  عديدة العناصر (مركبة / مخلوطة)', px(0.5), py(0.78), '#7dd3fc', 10.5);
  } else if (sk === 'chem_urea_carbamate') {
    rrect(px(0.06), py(0.36), px(0.22), 36, 6, '#1e293b', '#38bdf8'); txt('2NH₃+CO₂', px(0.17), py(0.36) + 18, '#7dd3fc', 10, 'center', false);
    arr(px(0.28), py(0.36) + 18, px(0.36), py(0.36) + 18, '#fbbf24');
    rrect(px(0.36), py(0.34), px(0.28), 44, 6, '#1e293b', '#fbbf24'); txt('كربامات NH₄⁺', px(0.50), py(0.34) + 22, '#fde047', 9.5);
    arr(px(0.64), py(0.36) + 18, px(0.72), py(0.36) + 18, '#10b981');
    rrect(px(0.72), py(0.36), px(0.22), 36, 6, '#065f46', '#34d399'); txt('CO(NH₂)₂+H₂O', px(0.83), py(0.36) + 18, '#fff', 9.5, 'center', false);
  } else if (sk === 'chem_npk_bag_6_12_12') {
    rrect(px(0.30), py(0.12), px(0.40), usableH * 0.66, 12, '#14532d', '#4ade80');
    txt('سماد للخضروات', px(0.5), py(0.26), '#bbf7d0', 11.5);
    rrect(px(0.36), py(0.38), px(0.28), 30, 6, '#0f172a', '#fde047'); txt('6 - 12 - 12', px(0.5), py(0.38) + 15, '#fde047', 12, 'center', false);
    txt('6% N  |  12% P₂O₅  |  12% K₂O', px(0.5), py(0.86), '#e2e8f0', 10.5);
  } else if (sk === 'chem_ddt_synthesis') {
    poly(px(0.24), py(0.44), 22, 6, '#38bdf8', true); txt('Cl', px(0.12), py(0.44), '#4ade80', 11, 'center', false);
    arr(px(0.33), py(0.44), px(0.45), py(0.44), '#fbbf24');
    poly(px(0.58), py(0.44), 20, 6, '#ef4444', true); poly(px(0.78), py(0.44), 20, 6, '#ef4444', true);
    txt('CH–CCl₃', px(0.68), py(0.66), '#fde047', 11, 'center', false);
    txt('DDT ثنائي كلورو ثنائي فينيل ثلاثي كلورو إيثان', px(0.5), py(0.86), '#fca5a5', 10);
  } else if (sk === 'chem_bhc_lindane') {
    poly(px(0.24), py(0.46), 24, 6, '#38bdf8', true); txt('+ 3Cl₂ (ضوء) ➔', px(0.46), py(0.46), '#fde047', 10.5);
    poly(px(0.70), py(0.46), 26, 6, '#10b981', false, (sv * Math.PI) / 180);
    txt('6 Cl + 6 H (أيزومر جاما لندان)', px(0.68), py(0.78), '#6ee7b7', 10.5);
  } else if (sk === 'chem_trichlorophon_parathion') {
    rrect(px(0.06), py(0.16), px(0.42), usableH * 0.62, 8, '#0f172a', '#38bdf8');
    txt('تراي كلوروفون + بارا أوكسون', px(0.27), py(0.34), '#7dd3fc', 10, 'center', true, px(0.38));
    txt('رابطة P=O سريعة التحلل', px(0.27), py(0.56), '#e2e8f0', 9.5, 'center', true, px(0.38));
    rrect(px(0.52), py(0.16), px(0.42), usableH * 0.62, 8, '#0f172a', '#f59e0b');
    txt('باراثيون (Parathion)', px(0.73), py(0.34), '#fde047', 10, 'center', true, px(0.38));
    txt('رابطة P=S فعالة وسامة', px(0.73), py(0.56), '#fca5a5', 9.5, 'center', true, px(0.38));
  } else if (sk === 'chem_nylon66_interfacial') {
    beaker(px(0.34), py(0.86), px(0.28), usableH * 0.50, 'rgba(56,189,248,0.28)', 'طبقتا المونومرين');
    ctx.strokeStyle = '#f8fafc'; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(px(0.34), py(0.56)); ctx.lineTo(px(0.34), py(0.16)); ctx.lineTo(px(0.74), py(0.16)); ctx.stroke();
    txt(`سحب خيط النايلون 6,6 × ${sv}`, px(0.68), py(0.38), '#fde047', 10.5, 'center', true, px(0.36));
    txt('(رابطة بولي أميد متينة)', px(0.68), py(0.56), '#6ee7b7', 10);
  } else if (sk === 'chem_nylon_fabrics_ester') {
    rrect(px(0.08), py(0.24), px(0.26), usableH * 0.48, 8, '#7c3aed', '#e2e8f0'); txt('بكرات النايلون', px(0.21), py(0.48), '#fff', 10);
    arr(px(0.35), py(0.48), px(0.45), py(0.48), '#10b981');
    rrect(px(0.46), py(0.24), px(0.46), usableH * 0.48, 8, '#065f46', '#34d399');
    txt('تفاعل الأسترة ← البولي إستر', px(0.69), py(0.48), '#a7f3d0', 10, 'center', true, px(0.42));
  } else if (sk === 'chem_dacron_suit') {
    rrect(px(0.30), py(0.14), px(0.40), usableH * 0.68, 10, '#1e3a8a', '#93c5fd');
    txt('نسيج بدلة الداكرون', px(0.5), py(0.40), '#fff', 11.5);
    txt('مقاوم للتجعد والعثّ', px(0.5), py(0.58), '#bae6fd', 10);
  } else if (sk === 'chem_dacron_heart_patch') {
    const hcx = px(0.5), hcy = py(0.44), hs = Math.min(48, usableH * 0.25);
    ctx.save();
    ctx.beginPath();
    ctx.moveTo(hcx, hcy + hs * 0.95);
    ctx.bezierCurveTo(hcx - hs * 1.45, hcy + hs * 0.15, hcx - hs * 1.25, hcy - hs * 0.95, hcx, hcy - hs * 0.35);
    ctx.bezierCurveTo(hcx + hs * 1.25, hcy - hs * 0.95, hcx + hs * 1.45, hcy + hs * 0.15, hcx, hcy + hs * 0.95);
    ctx.fillStyle = 'rgba(220,38,38,0.52)'; ctx.fill();
    ctx.strokeStyle = '#f87171'; ctx.lineWidth = 2; ctx.stroke();
    ctx.restore();
    rrect(hcx - 28, hcy - 14, 56, 30, 5, 'rgba(250,204,21,0.34)', '#fde047');
    ctx.strokeStyle = '#fef08a'; ctx.lineWidth = 1.5;
    for (let sx = hcx - 22; sx <= hcx + 22; sx += 11) {
      ctx.beginPath(); ctx.moveTo(sx, hcy - 18); ctx.lineTo(sx, hcy - 10);
      ctx.moveTo(sx, hcy + 12); ctx.lineTo(sx, hcy + 20); ctx.stroke();
    }
    txt('رقعة داكرون', hcx, hcy + 1, '#fff', 9.5);
    txt('جراحة القلب والشرايين — لا تسبب تجلط الدم', px(0.5), py(0.86), '#fca5a5', 10.5);
  } else if (sk === 'chem_soap_colors') {
    ['#f472b6', '#34d399', '#fbbf24', '#38bdf8'].forEach((c, i) => {
      const cw = px(0.18), cx = px(0.10 + i * 0.21);
      rrect(cx, py(0.30), cw, usableH * 0.34, 12, c, '#fff');
    });
    txt('أملاح الصوديوم للأحماض الدهنية + ألوان وعطور', px(0.5), py(0.80), '#e2e8f0', 10.5);
  } else if (sk === 'chem_soap_micelle') {
    const cy = py(0.46), rDrop = Math.min(28, usableH * 0.14), rHead = rDrop * 2.1;
    ctx.beginPath(); ctx.arc(px(0.5), cy, rDrop, 0, Math.PI * 2); ctx.fillStyle = '#d97706'; ctx.fill();
    txt('دهن', px(0.5), cy, '#fff', 10.5);
    for (let i = 0; i < 12; i++) {
      const a = (i * Math.PI * 2) / 12;
      ctx.strokeStyle = '#94a3b8'; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(px(0.5) + Math.cos(a) * rDrop, cy + Math.sin(a) * rDrop);
      ctx.lineTo(px(0.5) + Math.cos(a) * rHead, cy + Math.sin(a) * rHead); ctx.stroke();
      ctx.beginPath(); ctx.arc(px(0.5) + Math.cos(a) * (rHead + 4), cy + Math.sin(a) * (rHead + 4), 5, 0, Math.PI * 2);
      ctx.fillStyle = '#38bdf8'; ctx.fill();
    }
    txt('رأس محب للماء (–COO⁻ Na⁺)  |  ذيل كاره للماء', px(0.5), py(0.90), '#7dd3fc', 10);
  } else if (sk === 'chem_anionic_detergents') {
    const p1 = Math.round(sv) === 1;
    rrect(px(0.07), py(0.14), px(0.86), usableH * 0.30, 8, p1 ? 'rgba(56,189,248,0.26)' : 'rgba(15,23,42,0.8)', '#38bdf8');
    txt('1) حمض ألكيل بنزين سلفونيك + NaOH → منظف سلفوناتي', px(0.5), py(0.29), '#7dd3fc', 10, 'center', true, px(0.80));
    rrect(px(0.07), py(0.54), px(0.86), usableH * 0.30, 8, !p1 ? 'rgba(16,185,129,0.26)' : 'rgba(15,23,42,0.8)', '#10b981');
    txt('2) كحول طويل + H₂SO₄ + NaOH → كبريتات ألكيل الصوديوم (أقوى)', px(0.5), py(0.69), '#6ee7b7', 9.5, 'center', true, px(0.80));
  } else if (sk === 'chem_paint_oil_crosslink') {
    rrect(px(0.10), py(0.22), px(0.80), 20, 4, '#38bdf8', null); txt('–CH₂–CH–CH=CH–CH₂–', px(0.5), py(0.22) + 10, '#0f172a', 10, 'center', false);
    ctx.strokeStyle = '#ef4444'; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(px(0.5), py(0.22) + 20); ctx.lineTo(px(0.5), py(0.62)); ctx.stroke();
    rrect(px(0.5) - 16, py(0.45) - 9, 32, 18, 4, '#dc2626', '#fff'); txt('–O–', px(0.5), py(0.45), '#fff', 10, 'center', false);
    rrect(px(0.10), py(0.62), px(0.80), 20, 4, '#38bdf8', null); txt('–CH₂–CH–CH=CH–CH₂–', px(0.5), py(0.62) + 10, '#0f172a', 10, 'center', false);
    txt('أكسدة الزيت وجفاف الطلاء بجسر الأكسجين', px(0.5), py(0.86), '#fde047', 10.5);

  // ---------------- UNIT 9 + PERIODIC TABLE ----------------
  } else if (sk === 'chem_carbon_cycle') {
    rrect(px(0.10), py(0.18), px(0.32), 36, 8, '#14532d', '#4ade80'); txt('تمثيل ضوئي 🌿', px(0.26), py(0.18) + 18, '#bbf7d0', 10);
    rrect(px(0.58), py(0.18), px(0.32), 36, 8, '#1e3a8a', '#38bdf8'); txt('تنفس الكائنات 🐘', px(0.74), py(0.18) + 18, '#bae6fd', 10);
    arr(px(0.42), py(0.22), px(0.58), py(0.22), '#fde047');
    arr(px(0.58), py(0.32), px(0.42), py(0.32), '#fca5a5');
    rrect(px(0.32), py(0.64), px(0.36), 34, 8, '#78350f', '#fbbf24'); txt('تحلل بكتيري + CO₂', px(0.5), py(0.64) + 17, '#fde68a', 10);
  } else if (sk === 'chem_greenhouse_effect') {
    rrect(px(0.08), py(0.74), px(0.84), 26, 6, '#14532d', '#22c55e'); txt('سطح الأرض', px(0.5), py(0.74) + 13, '#dcfce7', 10.5);
    ctx.setLineDash([6, 4]); ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = Math.max(2, sv / 90);
    ctx.beginPath(); ctx.moveTo(px(0.08), py(0.22)); ctx.lineTo(px(0.92), py(0.22)); ctx.stroke(); ctx.setLineDash([]);
    txt(`طبقة CO₂ المحبسة (${sv} ppm)`, px(0.5), py(0.12), '#7dd3fc', 10.5);
    arr(px(0.20), py(0.06), px(0.32), py(0.72), '#facc15', 2);
    arr(px(0.44), py(0.72), px(0.58), py(0.24), '#ef4444', 2); arr(px(0.58), py(0.24), px(0.72), py(0.72), '#ef4444', 2);
    txt('انحباس الأشعة تحت الحمراء ↑↓', px(0.74), py(0.48), '#fca5a5', 10, 'center', true, px(0.34));
  } else if (sk === 'chem_pollution_sources') {
    rrect(px(0.14), py(0.46), px(0.20), usableH * 0.36, 4, '#334155', '#94a3b8'); txt('مصنع', px(0.24), py(0.64), '#e2e8f0', 10);
    rrect(px(0.50), py(0.64), px(0.34), 30, 6, '#1e293b', '#f59e0b'); txt('سيارات (سولار/بنزين)', px(0.67), py(0.64) + 15, '#fde047', 9.5);
    ctx.beginPath(); ctx.arc(px(0.42), py(0.26), 24, 0, Math.PI * 2); ctx.arc(px(0.58), py(0.24), 28, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(148,163,184,${Math.min(0.85, sv / 110)})`; ctx.fill();
    txt('SO₂ + NOx + CO + هيدروكربونات', px(0.50), py(0.25), '#f8fafc', 10);
  } else if (sk === 'chem_acid_rain_marble') {
    rrect(px(0.35), py(0.34), px(0.30), usableH * 0.44, 8, '#cbd5e1', '#94a3b8'); txt('تمثال CaCO₃', px(0.5), py(0.56), '#0f172a', 11);
    for (let i = 0; i < 6; i++) arr(px(0.30 + i * 0.08), py(0.08), px(0.30 + i * 0.08), py(0.30), '#ef4444', 1.6);
    txt(`مطر حمضي H₂SO₄ (pH = ${sv}) → تآكل CaSO₄`, px(0.5), py(0.88), '#fca5a5', 10.5);
  } else if (sk === 'chem_photochemical_smog') {
    txt('☀️ أشعة UV + NO + هيدروكربونات (HC) ➔', px(0.5), py(0.24), '#fde047', 11);
    arr(px(0.5), py(0.32), px(0.5), py(0.50), '#f97316', 2);
    rrect(px(0.10), py(0.52), px(0.80), usableH * 0.28, 8, 'rgba(217,119,6,0.3)', '#f59e0b');
    txt('الأوزون الأرضي O₃ + ألدهيدات + PAN (ضباب دخاني)', px(0.5), py(0.66), '#fed7aa', 10);
  } else if (sk === 'chem_periodic_table_interactive') {
    const grp = Math.round(sv);
    rrect(px(0.07), py(0.16), px(0.14), usableH * 0.46, 4, grp === 1 ? '#dc2626' : 'rgba(220,38,38,0.35)', '#fca5a5'); txt('s', px(0.14), py(0.39), '#fff', 12);
    rrect(px(0.23), py(0.30), px(0.44), usableH * 0.32, 4, grp === 3 ? '#d97706' : 'rgba(217,119,6,0.35)', '#fde047'); txt('d (انتقالية)', px(0.45), py(0.46), '#fff', 10.5);
    rrect(px(0.69), py(0.16), px(0.24), usableH * 0.46, 4, grp === 2 ? '#0284c7' : 'rgba(2,132,199,0.35)', '#7dd3fc'); txt('p', px(0.81), py(0.39), '#fff', 12);
    rrect(px(0.23), py(0.68), px(0.44), usableH * 0.16, 4, grp === 4 ? '#059669' : 'rgba(5,150,105,0.35)', '#6ee7b7'); txt('f (لانثانيدات وأكتينيدات)', px(0.45), py(0.76), '#fff', 9.5);
  }

  // Full-width bottom formula banner (unobstructed since .lab-hud-zoom hides in 2D mode)
  rrect(12, h - 34, w - 24, 24, 6, 'rgba(16,185,129,0.16)', 'rgba(16,185,129,0.50)');
  txt(data ? data.formula : '', px(0.5), h - 22, '#6ee7b7', 10.5, 'center', false, w - 34);
}
"""
