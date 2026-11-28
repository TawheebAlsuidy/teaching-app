#!/usr/bin/env python3
"""Bespoke Three.js 3D scene builders for all 74 unique Chemistry figures (Units 1-9).

Every single sim_key constructs its own distinct 3D apparatus, molecule, graph, or process model.
"""


def get_chemistry_3d_js() -> str:
    return r"""
function buildChem3dScene(sk, addMesh, THREE, grp, dyn) {
  if (!sk || sk.indexOf('chem_') !== 0) return false;
  const g = new THREE.Group();
  grp.add(g);
  const M = (geo, col, x = 0, y = 0, z = 0, rx = 0, ry = 0, rz = 0, op = 1) => {
    const mat = new THREE.MeshPhongMaterial({ color: col, transparent: op < 1, opacity: op, shininess: 60 });
    const m = new THREE.Mesh(geo, mat);
    m.position.set(x, y, z); m.rotation.set(rx, ry, rz);
    g.add(m); return m;
  };
  const B = (w, h, d, col, x, y, z, rx = 0, ry = 0, rz = 0, op = 1) => M(new THREE.BoxGeometry(w, h, d), col, x, y, z, rx, ry, rz, op);
  const C = (rt, rb, h, col, x, y, z, rx = 0, ry = 0, rz = 0, op = 1) => M(new THREE.CylinderGeometry(rt, rb, h, 24), col, x, y, z, rx, ry, rz, op);
  const S = (r, col, x, y, z, op = 1) => M(new THREE.SphereGeometry(r, 20, 20), col, x, y, z, 0, 0, 0, op);
  const T = (R, r, col, x, y, z, rx = 0, ry = 0, rz = 0) => M(new THREE.TorusGeometry(R, r, 12, 32), col, x, y, z, rx, ry, rz);
  const hex3 = (cx, cy, cz, rad, col, arom = false, tilt = 0) => {
    for (let i = 0; i < 6; i++) {
      const a1 = (i * Math.PI) / 3, a2 = ((i + 1) * Math.PI) / 3;
      const x1 = cx + Math.cos(a1) * rad, z1 = cz + Math.sin(a1) * rad;
      const x2 = cx + Math.cos(a2) * rad, z2 = cz + Math.sin(a2) * rad;
      const mx = (x1 + x2) / 2, mz = (z1 + z2) / 2;
      B(rad * 1.02, 0.08, 0.08, col, mx, cy, mz, tilt, -Math.atan2(z2 - z1, x2 - x1), 0);
      S(0.11, 0x334155, x1, cy, z1);
    }
    if (arom) T(rad * 0.55, 0.04, 0xfbbf24, cx, cy, cz, Math.PI / 2 + tilt, 0, 0);
  };
  const beaker3 = (cx, cy, colLiq) => {
    C(0.55, 0.55, 0.85, 0x94a3b8, cx, cy, 0, 0, 0, 0, 0.32);
    C(0.50, 0.50, 0.55, colLiq, cx, cy - 0.14, 0, 0, 0, 0, 0.78);
  };
  const spinSlow = (spd = 0.008) => dyn.push({ type: 'chem_spin', mesh: g, spd });

  // ================= UNIT 1 =================
  if (sk === 'chem_u1_d_f_blocks') {
    T(0.95, 0.05, 0xf59e0b, 0, 0.15, 0, Math.PI / 3, 0, 0);
    T(0.65, 0.05, 0x38bdf8, 0, 0.15, 0, -Math.PI / 4, 0, 0);
    B(1.4, 0.22, 0.25, 0xf59e0b, 0, -0.45, 0);
    B(1.1, 0.18, 0.25, 0x10b981, 0, -0.78, 0.25);
    spinSlow(0.008);
  } else if (sk === 'chem_u1_orbitals') {
    for (let i = 0; i < 5; i++) {
      B(0.34, 0.34, 0.14, 0x1e293b, -0.9 + i * 0.45, 0.35, 0);
      C(0.04, 0.04, 0.24, 0x4ade80, -0.9 + i * 0.45, 0.35, 0.12);
    }
    B(0.36, 0.36, 0.14, 0xf59e0b, 0, -0.35, 0);
    C(0.04, 0.04, 0.24, 0xfef08a, 0, -0.35, 0.12);
    spinSlow(0.006);
  } else if (sk === 'chem_blast_furnace') {
    C(0.35, 0.72, 1.55, 0x64748b, 0, 0.15, 0);
    C(0.72, 0.62, 0.55, 0xdc2626, 0, -0.82, 0);
    C(0.60, 0.60, 0.22, 0xfbbf24, 0, -1.12, 0);
    C(0.09, 0.09, 0.85, 0xf97316, -0.82, -0.78, 0, 0, 0, Math.PI / 2);
    C(0.09, 0.09, 0.85, 0x94a3b8, 0.82, -0.92, 0, 0, 0, Math.PI / 2);
    spinSlow(0.005);
  } else if (sk === 'chem_iron_ions') {
    C(0.18, 0.18, 1.25, 0x4ade80, -0.75, 0, 0, 0, 0, 0, 0.82);
    C(0.18, 0.18, 1.25, 0xb45309, 0, 0, 0, 0, 0, 0, 0.85);
    C(0.18, 0.18, 1.25, 0x991b1b, 0.75, 0, 0, 0, 0, 0, 0.92);
    B(1.9, 0.10, 0.35, 0x475569, 0, -0.68, 0);
    dyn.push({ type: 'bob', mesh: g, amp: 0.06 });

  // ================= UNIT 2 =================
  } else if (sk === 'chem_energy_forms') {
    S(0.34, 0xfacc15, 0, 0, 0);
    [0xef4444, 0x38bdf8, 0x10b981, 0xa855f7, 0xf97316].forEach((c, i) => {
      const a = (i * Math.PI * 2) / 5;
      S(0.20, c, Math.cos(a) * 1.15, Math.sin(a) * 0.7, Math.sin(a * 2) * 0.4);
      C(0.03, 0.03, 1.1, c, Math.cos(a) * 0.58, Math.sin(a) * 0.35, 0, 0, 0, a - Math.PI / 2);
    });
    spinSlow(0.01);
  } else if (sk === 'chem_k_water_exo') {
    beaker3(0, -0.25, 0x38bdf8);
    S(0.16, 0xe2e8f0, 0, 0.06, 0);
    M(new THREE.ConeGeometry(0.18, 0.55, 16), 0xa855f7, 0, 0.42, 0);
    M(new THREE.ConeGeometry(0.12, 0.38, 16), 0xf97316, 0.12, 0.36, 0.08);
    dyn.push({ type: 'bob', mesh: g, amp: 0.08 });
  } else if (sk === 'chem_nh4no3_endo') {
    C(0.22, 0.22, 1.1, 0xcbd5e1, -0.85, 0.15, 0, 0, 0, Math.PI / 2.6, 0.75);
    M(new THREE.ConeGeometry(0.16, 0.38, 16), 0x38bdf8, -1.05, -0.35, 0);
    beaker3(0.85, -0.2, 0x0ea5e9);
    C(0.14, 0.14, 0.8, 0x7dd3fc, 0.85, 0.25, 0, 0, 0, 0, 0.45);
    spinSlow(0.006);
  } else if (sk === 'chem_system_surroundings') {
    B(2.2, 1.4, 1.4, 0x334155, 0, 0, 0, 0, 0, 0, 0.24);
    beaker3(0, -0.15, 0xf97316);
    spinSlow(0.007);
  } else if (sk === 'chem_endo_exo_curves') {
    B(2.3, 0.06, 0.5, 0x64748b, 0, -0.75, 0);
    B(0.75, 0.08, 0.45, 0x38bdf8, -0.75, 0.45, 0);
    B(0.75, 0.08, 0.45, 0x10b981, 0.75, -0.38, 0);
    C(0.05, 0.05, 0.9, 0xef4444, 0, 0.05, 0);
    M(new THREE.ConeGeometry(0.12, 0.24, 12), 0xef4444, 0, -0.45, 0, Math.PI, 0, 0);
    spinSlow(0.006);
  } else if (sk === 'chem_water_heating_curve') {
    B(0.6, 0.22, 0.5, 0x93c5fd, -0.9, -0.55, 0);
    B(0.6, 0.22, 0.5, 0x38bdf8, -0.25, -0.15, 0);
    B(0.65, 0.22, 0.5, 0xf59e0b, 0.45, 0.35, 0);
    B(0.5, 0.22, 0.5, 0xef4444, 1.05, 0.72, 0);
    spinSlow(0.006);
  } else if (sk === 'chem_bomb_calorimeter') {
    C(0.85, 0.85, 1.35, 0x1e3a8a, 0, 0, 0, 0, 0, 0, 0.35);
    C(0.45, 0.45, 0.85, 0x94a3b8, 0, -0.05, 0);
    C(0.04, 0.04, 1.45, 0xef4444, 0.55, 0.2, 0);
    C(0.03, 0.03, 1.4, 0xfbbf24, -0.55, 0.15, 0);
    spinSlow(0.008);

  // ================= UNIT 3 =================
  } else if (sk === 'chem_zn_cuso4_redox') {
    beaker3(0, -0.25, 0x2563eb);
    B(0.24, 1.15, 0.08, 0x94a3b8, 0, 0.1, 0);
    B(0.28, 0.52, 0.11, 0xb45309, 0, -0.22, 0);
    S(0.08, 0xf59e0b, -0.35, 0.1, 0.2); S(0.08, 0x7dd3fc, 0.35, -0.15, -0.2);
    spinSlow(0.008);
  } else if (sk === 'chem_porous_cell') {
    B(1.9, 1.05, 0.9, 0x0284c7, 0, -0.1, 0, 0, 0, 0, 0.32);
    B(0.06, 1.0, 0.86, 0xfde047, 0, -0.1, 0, 0, 0, 0, 0.78);
    B(0.14, 1.1, 0.35, 0x94a3b8, -0.55, 0.05, 0);
    B(0.14, 1.1, 0.35, 0xd97706, 0.55, 0.05, 0);
    T(0.18, 0.05, 0xfacc15, 0, 0.85, 0);
    spinSlow(0.007);
  } else if (sk === 'chem_daniell_cell') {
    beaker3(-0.85, -0.25, 0x94a3b8); beaker3(0.85, -0.25, 0x2563eb);
    B(0.14, 1.0, 0.2, 0xcbd5e1, -1.0, 0.05, 0); B(0.14, 1.0, 0.2, 0xd97706, 1.0, 0.05, 0);
    C(0.08, 0.08, 1.05, 0xf8fafc, 0, 0.42, 0, 0, 0, Math.PI / 2);
    C(0.08, 0.08, 0.55, 0xf8fafc, -0.52, 0.16, 0); C(0.08, 0.08, 0.55, 0xf8fafc, 0.52, 0.16, 0);
    B(0.45, 0.26, 0.15, 0x10b981, 0, 0.82, 0);
    spinSlow(0.007);
  } else if (sk === 'chem_she_cell') {
    beaker3(-0.75, -0.25, 0x94a3b8); beaker3(0.75, -0.25, 0xef4444);
    C(0.24, 0.28, 0.8, 0xe2e8f0, 0.75, 0.1, 0, 0, 0, 0, 0.38);
    B(0.12, 0.72, 0.06, 0x334155, 0.75, -0.1, 0);
    B(0.14, 0.9, 0.14, 0x64748b, -0.75, 0.05, 0);
    C(0.05, 0.05, 0.7, 0x38bdf8, 1.2, 0.2, 0, 0, 0, Math.PI / 2);
    spinSlow(0.007);
  } else if (sk === 'chem_cells_trio') {
    C(0.24, 0.24, 1.05, 0x64748b, -0.85, 0, 0);
    C(0.26, 0.26, 1.05, 0xf59e0b, 0, 0, 0);
    C(0.32, 0.32, 0.28, 0x94a3b8, 0.85, -0.35, 0);
    spinSlow(0.008);
  } else if (sk === 'chem_dry_cell_leclanche') {
    C(0.45, 0.45, 1.35, 0x64748b, 0, 0, 0, 0, 0, 0, 0.55);
    C(0.34, 0.34, 1.15, 0x0f172a, 0, -0.04, 0);
    C(0.09, 0.09, 1.5, 0x334155, 0, 0.08, 0);
    C(0.14, 0.14, 0.14, 0xfbbf24, 0, 0.84, 0);
    spinSlow(0.008);
  } else if (sk === 'chem_alkaline_cell') {
    C(0.46, 0.46, 1.32, 0xd97706, 0, 0, 0, 0, 0, 0, 0.72);
    C(0.22, 0.22, 1.12, 0x38bdf8, 0, -0.05, 0);
    C(0.08, 0.08, 1.48, 0xe2e8f0, 0, -0.05, 0);
    spinSlow(0.008);
  } else if (sk === 'chem_mercury_button_cell') {
    C(0.65, 0.65, 0.34, 0x94a3b8, 0, 0, 0);
    C(0.56, 0.56, 0.12, 0x38bdf8, 0, 0.15, 0);
    C(0.56, 0.56, 0.12, 0xdc2626, 0, -0.14, 0);
    spinSlow(0.01);
  } else if (sk === 'chem_lead_battery') {
    B(1.9, 1.15, 1.0, 0x0f172a, 0, 0, 0, 0, 0, 0, 0.42);
    for (let i = 0; i < 6; i++) {
      const px = -0.75 + i * 0.30;
      B(0.07, 0.92, 0.75, 0x94a3b8, px - 0.05, 0, 0);
      B(0.07, 0.92, 0.75, 0x991b1b, px + 0.05, 0, 0);
    }
    B(1.95, 0.14, 1.05, 0x1e293b, 0, 0.62, 0);
    spinSlow(0.007);
  } else if (sk === 'chem_h2o2_fuel_cell') {
    B(1.4, 1.1, 0.8, 0x059669, 0, 0, 0, 0, 0, 0, 0.35);
    B(0.12, 1.0, 0.72, 0x475569, -0.35, 0, 0);
    B(0.12, 1.0, 0.72, 0x475569, 0.35, 0, 0);
    C(0.08, 0.08, 0.6, 0x38bdf8, -0.95, 0.1, 0, 0, 0, Math.PI / 2);
    C(0.08, 0.08, 0.6, 0xef4444, 0.95, 0.1, 0, 0, 0, Math.PI / 2);
    spinSlow(0.007);
  } else if (sk === 'chem_cucl2_electrolysis') {
    beaker3(0, -0.22, 0x1d4ed8);
    C(0.09, 0.09, 1.15, 0x1e293b, -0.3, 0.1, 0);
    C(0.09, 0.09, 1.15, 0x1e293b, 0.3, 0.1, 0);
    S(0.08, 0xa3e635, -0.3, 0.62, 0); S(0.11, 0xd97706, 0.3, -0.3, 0);
    spinSlow(0.008);
  } else if (sk === 'chem_electroplating') {
    beaker3(0, -0.22, 0x64748b);
    B(0.14, 1.0, 0.45, 0xf8fafc, -0.36, 0.08, 0);
    C(0.06, 0.18, 0.95, 0xe2e8f0, 0.34, 0.08, 0);
    S(0.07, 0xbae6fd, 0, 0.15, 0); S(0.07, 0xbae6fd, 0.12, -0.1, 0);
    dyn.push({ type: 'bob', mesh: g, amp: 0.06 });

  // ================= UNIT 4 =================
  } else if (sk === 'chem_mass_spectrometer') {
    B(0.55, 0.36, 0.4, 0xfbbf24, -1.05, 0, 0);
    T(1.1, 0.06, 0x38bdf8, 0.1, 0.3, 0, 0, 0, 0.25);
    T(1.45, 0.06, 0xf472b6, 0.1, -0.35, 0, 0, 0, -0.18);
    B(0.16, 1.2, 0.7, 0x475569, 1.05, 0, 0);
    spinSlow(0.006);
  } else if (sk === 'chem_binding_energy_curve') {
    const pts = [[-1.1, -0.7], [-0.8, 0.2], [-0.3, 0.78], [0.25, 0.62], [1.1, 0.35]];
    pts.forEach(([x, y], i) => {
      S(0.11, i === 2 ? 0xfbbf24 : 0x10b981, x, y, 0);
      if (i > 0) {
        const [px, py] = pts[i - 1];
        B(Math.hypot(x - px, y - py), 0.08, 0.08, 0x34d399, (x + px) / 2, (y + py) / 2, 0, 0, 0, Math.atan2(y - py, x - px));
      }
    });
    spinSlow(0.006);
  } else if (sk === 'chem_stability_belt') {
    B(2.2, 0.05, 0.4, 0x64748b, 0, -0.75, 0); B(0.05, 1.5, 0.4, 0x64748b, -1.1, 0, 0);
    for (let i = 0; i < 12; i++) S(0.09, i % 3 ? 0x10b981 : 0xf59e0b, -0.95 + i * 0.17, -0.62 + Math.pow(i / 11, 1.25) * 1.25, 0);
    spinSlow(0.007);
  } else if (sk === 'chem_alpha_beta_gamma_shield') {
    B(0.04, 1.2, 0.9, 0xf8fafc, -0.45, 0, 0);
    B(0.12, 1.2, 0.9, 0x94a3b8, 0.25, 0, 0);
    B(0.32, 1.2, 0.9, 0x475569, 0.95, 0, 0);
    C(0.04, 0.04, 0.8, 0xef4444, -0.85, 0.36, 0, 0, 0, Math.PI / 2);
    C(0.04, 0.04, 1.45, 0x38bdf8, -0.5, 0, 0, 0, 0, Math.PI / 2);
    C(0.04, 0.04, 2.35, 0xa855f7, 0.1, -0.36, 0, 0, 0, Math.PI / 2);
    spinSlow(0.006);
  } else if (sk === 'chem_u235_chain_fission') {
    S(0.32, 0x38bdf8, -0.65, 0, 0);
    S(0.22, 0x10b981, 0.35, 0.5, 0.2); S(0.22, 0xf97316, 0.35, -0.5, -0.2);
    [-0.6, 0, 0.6].forEach(yy => S(0.09, 0xfacc15, 0.95, yy, 0));
    spinSlow(0.01);
  } else if (sk === 'chem_nuclear_reactor_5parts') {
    C(0.58, 0.58, 1.2, 0x475569, -0.6, 0, 0, 0, 0, 0, 0.6);
    C(0.05, 0.05, 0.95, 0xef4444, -0.72, 0.35, 0); C(0.05, 0.05, 0.95, 0xef4444, -0.48, 0.35, 0);
    B(0.55, 0.72, 0.55, 0x1e3a8a, 0.35, 0, 0);
    C(0.24, 0.24, 0.6, 0x10b981, 1.08, 0, 0, 0, 0, Math.PI / 2);
    spinSlow(0.006);
  } else if (sk === 'chem_radioisotope_bone_scan') {
    B(0.45, 1.15, 0.24, 0x94a3b8, -0.2, 0, 0); S(0.22, 0x94a3b8, -0.2, 0.76, 0);
    S(0.12, 0x10b981, -0.2, 0.2, 0.14);
    B(0.42, 0.55, 0.3, 0x0f172a, 0.8, 0.25, 0);
    spinSlow(0.007);
  } else if (sk === 'chem_gamma_radiotherapy') {
    B(1.6, 0.22, 0.55, 0x475569, 0, -0.5, 0);
    T(0.95, 0.08, 0x38bdf8, 0, 0.1, 0);
    M(new THREE.ConeGeometry(0.14, 0.75, 16), 0xa855f7, 0, 0.25, 0, Math.PI, 0, 0);
    dyn.push({ type: 'chem_spin', mesh: g, spd: 0.009 });
  } else if (sk === 'chem_fusion_hbomb') {
    S(0.26, 0x38bdf8, -0.65, 0.2, 0); S(0.28, 0x10b981, -0.65, -0.25, 0);
    S(0.42, 0xf59e0b, 0.55, 0, 0);
    T(0.65, 0.05, 0xfef08a, 0.55, 0, 0, Math.PI / 3, 0, 0);
    spinSlow(0.014);

  // ================= UNIT 5 =================
  } else if (sk === 'chem_u5_nitrogen_rings') {
    hex3(-0.7, 0.1, 0, 0.45, 0x38bdf8, true);
    hex3(0.7, -0.1, 0, 0.45, 0x10b981, true);
    S(0.16, 0xfbbf24, -0.25, 0.1, 0); S(0.16, 0xfbbf24, 0.25, -0.1, 0);
    spinSlow(0.01);
  } else if (sk === 'chem_amines_123') {
    S(0.28, 0x3b82f6, 0, 0.2, 0);
    [0, 1, 2].forEach(i => {
      const a = (i * Math.PI * 2) / 3;
      S(0.18, i === 2 ? 0xf8fafc : 0x475569, Math.cos(a) * 0.75, -0.25, Math.sin(a) * 0.75);
      C(0.04, 0.04, 0.85, 0x94a3b8, Math.cos(a) * 0.37, -0.02, Math.sin(a) * 0.37);
    });
    spinSlow(0.01);
  } else if (sk === 'chem_piperidine_pyridine_aniline') {
    hex3(-0.95, 0.25, 0, 0.34, 0x38bdf8, false);
    hex3(0, 0.25, 0, 0.34, 0x10b981, true);
    hex3(0.95, -0.25, 0, 0.34, 0xf59e0b, true);
    S(0.14, 0x3b82f6, 0.95, -0.25, 0.48);
    spinSlow(0.01);
  } else if (sk === 'chem_amides_urea_benzamide') {
    S(0.24, 0x475569, 0, 0, 0); S(0.22, 0xef4444, 0, 0.65, 0);
    S(0.22, 0x3b82f6, -0.65, -0.25, 0); S(0.22, 0x3b82f6, 0.65, -0.25, 0);
    C(0.06, 0.06, 0.65, 0xfacc15, 0, 0.32, 0);
    spinSlow(0.01);
  } else if (sk === 'chem_nitriles_reactions') {
    S(0.24, 0x475569, -0.55, 0, 0); S(0.24, 0x3b82f6, 0.55, 0, 0);
    [-0.12, 0, 0.12].forEach(yy => C(0.035, 0.035, 0.95, 0xfbbf24, 0, yy, 0, 0, 0, Math.PI / 2));
    spinSlow(0.01);
  } else if (sk === 'chem_amino_acids_types') {
    hex3(-0.85, 0, 0, 0.35, 0x38bdf8, true);
    B(0.8, 0.12, 0.12, 0x10b981, 0.1, 0, 0);
    S(0.22, 0x3b82f6, -0.25, 0.45, 0); S(0.22, 0xef4444, 0.65, 0.45, 0);
    spinSlow(0.01);
  } else if (sk === 'chem_zwitterion_amphoteric') {
    S(0.24, 0x475569, 0, 0, 0);
    S(0.28, 0x38bdf8, -0.75, 0, 0);
    S(0.28, 0xef4444, 0.75, 0, 0);
    C(0.05, 0.05, 1.4, 0xf8fafc, 0, 0, 0, 0, 0, Math.PI / 2);
    spinSlow(0.01);

  // ================= UNIT 6 =================
  } else if (sk === 'chem_biochem_sciences_map') {
    S(0.32, 0xfacc15, 0, 0, 0);
    for (let i = 0; i < 5; i++) {
      const a = (i * Math.PI * 2) / 5;
      S(0.18, 0x10b981, Math.cos(a) * 0.95, Math.sin(a) * 0.45, Math.sin(a) * 0.45);
    }
    spinSlow(0.01);
  } else if (sk === 'chem_monosaccharide_fruits') {
    S(0.35, 0xef4444, -0.55, 0, 0);
    for (let i = 0; i < 5; i++) S(0.15, 0xa855f7, 0.45 + (i % 2) * 0.26, 0.3 - i * 0.16, 0);
    spinSlow(0.01);
  } else if (sk === 'chem_glucose_fructose_rings') {
    hex3(-0.65, 0.15, 0, 0.45, 0x38bdf8, false);
    for (let i = 0; i < 5; i++) {
      const a = (i * Math.PI * 2) / 5;
      S(0.11, 0xf59e0b, 0.68 + Math.cos(a) * 0.42, -0.15, Math.sin(a) * 0.42);
    }
    spinSlow(0.01);
  } else if (sk === 'chem_lactose_structure') {
    hex3(-0.65, 0, 0, 0.42, 0x38bdf8, false);
    hex3(0.65, 0, 0, 0.42, 0x10b981, false);
    S(0.16, 0xef4444, 0, 0.12, 0);
    spinSlow(0.009);
  } else if (sk === 'chem_sucrose_condensation') {
    hex3(-0.62, 0.1, 0, 0.4, 0x38bdf8, false);
    for (let i = 0; i < 5; i++) S(0.12, 0xf59e0b, 0.65 + Math.cos(i * 1.25) * 0.35, -0.1, Math.sin(i * 1.25) * 0.35);
    S(0.15, 0xef4444, 0, 0, 0);
    spinSlow(0.009);
  } else if (sk === 'chem_six_amino_acids') {
    [0x38bdf8, 0x10b981, 0xf59e0b, 0xa855f7, 0xef4444, 0xec4899].forEach((c, i) => {
      B(0.45, 0.35, 0.25, c, -0.75 + (i % 3) * 0.75, i < 3 ? 0.35 : -0.35, 0);
    });
    spinSlow(0.008);
  } else if (sk === 'chem_peptide_bond_dipeptide') {
    [-0.9, -0.3, 0.3, 0.9].forEach((xx, i) => {
      S(0.22, i % 2 ? 0x38bdf8 : 0x10b981, xx, i % 2 ? 0.18 : -0.18, 0);
      if (i < 3) B(0.62, 0.08, 0.08, 0xfbbf24, xx + 0.3, 0, 0);
    });
    spinSlow(0.01);
  } else if (sk === 'chem_saturated_unsaturated_fats') {
    for (let i = 0; i < 6; i++) S(0.12, 0x38bdf8, -0.8 + i * 0.32, 0.38, 0);
    for (let i = 0; i < 6; i++) S(0.12, 0xf59e0b, -0.8 + i * 0.32, i < 3 ? -0.25 : -0.25 - (i - 2) * 0.18, 0);
    spinSlow(0.008);
  } else if (sk === 'chem_enzyme_lock_key') {
    M(new THREE.TorusGeometry(0.62, 0.22, 16, 28, Math.PI * 1.55), 0x1e3a8a, -0.25, 0, 0, 0, 0, Math.PI * 0.22);
    S(0.32, 0x10b981, 0.45, 0, 0);
    dyn.push({ type: 'bob', mesh: g, amp: 0.09 });

  // ================= UNIT 7 =================
  } else if (sk === 'chem_petro_products_grid') {
    C(0.45, 0.45, 0.85, 0x0f172a, -0.55, 0, 0);
    [0xfbbf24, 0xef4444, 0x38bdf8, 0x10b981].forEach((c, i) => B(0.32, 0.32, 0.32, c, 0.4 + (i % 2) * 0.45, i < 2 ? 0.28 : -0.28, 0));
    spinSlow(0.009);
  } else if (sk === 'chem_seismic_oil_trap') {
    C(0.95, 1.15, 0.35, 0x78350f, 0, 0.4, 0);
    C(1.15, 1.25, 0.25, 0xdc2626, 0, 0.1, 0);
    C(1.25, 1.32, 0.25, 0x0f172a, 0, -0.15, 0);
    C(1.32, 1.38, 0.25, 0x0284c7, 0, -0.4, 0);
    spinSlow(0.007);
  } else if (sk === 'chem_distillation_tower') {
    C(0.38, 0.56, 1.85, 0x475569, 0, 0, 0, 0, 0, 0, 0.55);
    [0xfef08a, 0xfacc15, 0xf97316, 0xd97706, 0x334155].forEach((col, i) => {
      C(0.46, 0.46, 0.08, col, 0, 0.72 - i * 0.36, 0);
    });
    spinSlow(0.009);
  } else if (sk === 'chem_oil_fractions_uses') {
    [0.35, 0.65, 0.95, 1.25].forEach((hh, i) => {
      B(0.28, hh, 0.28, [0x38bdf8, 0xfbbf24, 0x10b981, 0xf97316][i], -0.6 + i * 0.42, -0.6 + hh / 2, 0);
    });
    spinSlow(0.008);
  } else if (sk === 'chem_gasoline_cars') {
    B(1.5, 0.38, 0.68, 0xdc2626, 0, -0.1, 0);
    B(0.75, 0.32, 0.6, 0x93c5fd, 0.08, 0.25, 0);
    C(0.18, 0.18, 0.8, 0x0f172a, -0.48, -0.32, 0, Math.PI / 2, 0, 0);
    C(0.18, 0.18, 0.8, 0x0f172a, 0.48, -0.32, 0, Math.PI / 2, 0, 0);
    spinSlow(0.008);
  } else if (sk === 'chem_oil_consumption_87_13') {
    C(0.55, 0.55, 0.28, 0x10b981, 0, 0.58, 0);
    C(0.55, 0.55, 1.05, 0x334155, 0, -0.12, 0);
    T(0.57, 0.04, 0x94a3b8, 0, 0.35, 0, Math.PI / 2, 0, 0);
    T(0.57, 0.04, 0x94a3b8, 0, -0.35, 0, Math.PI / 2, 0, 0);
    spinSlow(0.008);

  // ================= UNIT 8 =================
  } else if (sk === 'chem_fertilizer_taxonomy') {
    B(0.95, 0.28, 0.3, 0xef4444, 0, 0.72, 0);
    B(0.65, 0.28, 0.3, 0xf59e0b, -0.65, 0.1, 0);
    B(0.65, 0.28, 0.3, 0x10b981, 0.65, 0.1, 0);
    [0, 1, 2].forEach(i => B(0.38, 0.28, 0.3, 0x38bdf8, -0.55 + i * 0.55, -0.55, 0));
    spinSlow(0.007);
  } else if (sk === 'chem_urea_carbamate') {
    S(0.24, 0x475569, 0, 0, 0); S(0.22, 0xef4444, 0, 0.62, 0);
    S(0.22, 0x3b82f6, -0.6, -0.22, 0); S(0.22, 0x3b82f6, 0.6, -0.22, 0);
    B(1.1, 0.06, 0.06, 0x4ade80, 0, -0.58, 0);
    spinSlow(0.01);
  } else if (sk === 'chem_npk_bag_6_12_12') {
    B(1.05, 1.35, 0.42, 0x16a34a, 0, 0, 0);
    B(0.75, 0.32, 0.45, 0xfde047, 0, 0.15, 0);
    spinSlow(0.008);
  } else if (sk === 'chem_ddt_synthesis') {
    hex3(-0.68, 0, 0, 0.4, 0x38bdf8, true); hex3(0.68, 0, 0, 0.4, 0x38bdf8, true);
    S(0.18, 0x475569, 0, 0.15, 0); S(0.18, 0x4ade80, -1.18, 0, 0); S(0.18, 0x4ade80, 1.18, 0, 0);
    S(0.20, 0x22c55e, 0, -0.55, 0.25);
    spinSlow(0.01);
  } else if (sk === 'chem_bhc_lindane') {
    hex3(0, 0, 0, 0.55, 0x10b981, false, 0.35);
    for (let i = 0; i < 6; i++) {
      const a = (i * Math.PI) / 3;
      S(0.14, 0x4ade80, Math.cos(a) * 0.85, i % 2 ? 0.38 : -0.38, Math.sin(a) * 0.85);
    }
    spinSlow(0.012);
  } else if (sk === 'chem_trichlorophon_parathion') {
    S(0.28, 0xf97316, -0.55, 0, 0); S(0.20, 0xef4444, -0.55, 0.58, 0);
    S(0.28, 0xf97316, 0.55, 0, 0); S(0.20, 0xfacc15, 0.55, 0.58, 0);
    spinSlow(0.01);
  } else if (sk === 'chem_nylon66_interfacial') {
    beaker3(0, -0.35, 0x38bdf8);
    C(0.06, 0.06, 1.25, 0xf8fafc, 0, 0.25, 0);
    C(0.08, 0.08, 1.1, 0x94a3b8, 0.45, 0.82, 0, 0, 0, Math.PI / 2);
    dyn.push({ type: 'bob', mesh: g, amp: 0.08 });
  } else if (sk === 'chem_nylon_fabrics_ester') {
    [-0.75, 0, 0.75].forEach((xx, i) => C(0.24, 0.24, 0.95, [0x8b5cf6, 0xec4899, 0x38bdf8][i], xx, 0, 0));
    spinSlow(0.009);
  } else if (sk === 'chem_dacron_suit') {
    B(0.95, 1.1, 0.28, 0x1e3a8a, 0, 0, 0);
    B(0.32, 0.85, 0.24, 0x1e3a8a, -0.65, 0.08, 0, 0, 0, 0.25);
    B(0.32, 0.85, 0.24, 0x1e3a8a, 0.65, 0.08, 0, 0, 0, -0.25);
    spinSlow(0.008);
  } else if (sk === 'chem_dacron_heart_patch') {
    S(0.62, 0xdc2626, 0, 0, 0);
    B(0.45, 0.45, 0.14, 0xfde047, 0, 0.08, 0.55);
    dyn.push({ type: 'bob', mesh: g, amp: 0.08 });
  } else if (sk === 'chem_soap_colors') {
    [-0.75, 0, 0.75].forEach((xx, i) => B(0.55, 0.28, 0.82, [0xf472b6, 0x34d399, 0xfbbf24][i], xx, (i - 1) * 0.12, 0));
    spinSlow(0.008);
  } else if (sk === 'chem_soap_micelle') {
    S(0.35, 0xd97706, 0, 0, 0);
    for (let i = 0; i < 10; i++) {
      const a = (i * Math.PI * 2) / 10;
      S(0.11, 0x38bdf8, Math.cos(a) * 0.95, Math.sin(a) * 0.95, 0);
      B(0.52, 0.05, 0.05, 0x94a3b8, Math.cos(a) * 0.62, Math.sin(a) * 0.62, 0, 0, 0, a);
    }
    spinSlow(0.01);
  } else if (sk === 'chem_anionic_detergents') {
    hex3(-0.35, 0, 0, 0.42, 0x38bdf8, true);
    S(0.24, 0xfacc15, 0.55, 0, 0); S(0.16, 0xef4444, 0.95, 0.25, 0); S(0.16, 0xef4444, 0.95, -0.25, 0);
    spinSlow(0.01);
  } else if (sk === 'chem_paint_oil_crosslink') {
    B(1.8, 0.14, 0.2, 0x38bdf8, 0, 0.42, 0); B(1.8, 0.14, 0.2, 0x38bdf8, 0, -0.42, 0);
    C(0.06, 0.06, 0.84, 0xef4444, 0, 0, 0); S(0.18, 0xef4444, 0, 0, 0);
    spinSlow(0.008);

  // ================= UNIT 9 + PERIODIC TABLE =================
  } else if (sk === 'chem_carbon_cycle') {
    T(0.85, 0.07, 0x38bdf8, 0, 0, 0);
    S(0.24, 0x22c55e, -0.85, 0, 0); S(0.24, 0xf59e0b, 0.85, 0, 0); S(0.24, 0xa855f7, 0, -0.85, 0);
    spinSlow(0.01);
  } else if (sk === 'chem_greenhouse_effect') {
    S(0.55, 0x16a34a, 0, -0.2, 0);
    S(0.88, 0x38bdf8, 0, -0.2, 0, 0.24);
    C(0.04, 0.04, 0.85, 0xfef08a, -0.75, 0.55, 0, 0, 0, -0.6);
    spinSlow(0.008);
  } else if (sk === 'chem_pollution_sources') {
    B(0.85, 0.72, 0.65, 0x334155, -0.45, -0.3, 0);
    C(0.11, 0.14, 0.95, 0x64748b, -0.65, 0.35, 0);
    S(0.32, 0x94a3b8, -0.35, 0.82, 0, 0.72); S(0.40, 0x64748b, 0.25, 0.88, 0, 0.62);
    spinSlow(0.006);
  } else if (sk === 'chem_acid_rain_marble') {
    C(0.26, 0.35, 1.15, 0xe2e8f0, 0, -0.2, 0); S(0.22, 0xe2e8f0, 0, 0.52, 0);
    [-0.4, 0, 0.4].forEach(xx => C(0.025, 0.025, 0.45, 0xef4444, xx, 0.85, 0));
    dyn.push({ type: 'bob', mesh: g, amp: 0.05 });
  } else if (sk === 'chem_photochemical_smog') {
    S(0.32, 0xfef08a, -0.75, 0.7, 0);
    B(1.9, 0.48, 0.9, 0xf97316, 0, 0.15, 0, 0, 0, 0, 0.38);
    B(0.8, 0.35, 0.45, 0x334155, 0, -0.45, 0);
    spinSlow(0.007);
  } else if (sk === 'chem_periodic_table_interactive') {
    for (let c = 0; c < 18; c++) {
      const col = c < 2 ? 0xef4444 : (c < 12 ? 0xf59e0b : 0x38bdf8);
      const rows = (c === 0 || c === 17) ? 7 : (c >= 2 && c < 12 ? 4 : 6);
      for (let r = 0; r < rows; r++) B(0.11, 0.11, 0.12, col, -1.1 + c * 0.13, 0.65 - r * 0.14, 0);
    }
    for (let c = 0; c < 14; c++) B(0.11, 0.10, 0.12, 0x10b981, -0.85 + c * 0.13, -0.58, 0.15);
    g.scale.set(0.72, 0.72, 0.72);
    spinSlow(0.005);
  }
  return true;
}
"""
