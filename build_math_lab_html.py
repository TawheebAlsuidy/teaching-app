from pathlib import Path
import json
import shutil

from v3_lab_shell import build_v3_lab_css, build_v3_lab_body_html, build_v3_lab_controller_js

BASE_DIR = Path("/media/tawheeb/New Volume3/ذاكر/teaching-app")

UNIT_TITLES = {
    "u1": "الوحدة 1: الأعداد المركبة",
    "u2": "الوحدة 2: مبرهنة دي موافر والتوسعة ذات الحدين",
    "u3": "الوحدة 3: القطوع المخروطية",
    "u4": "الوحدة 4: الهندسة في فضاء ثلاثي الأبعاد",
    "u5": "الوحدة 5: الاحتمالات",
    "u6": "الوحدة 6: المشتقات",
    "u7": "الوحدة 7: التكامل",
}

TOOLS = {
    "math_complex": ["مستوى إحداثيات", "متجه العدد المركب", "مقياس الطول والزاوية"],
    "math_cone_sections": ["مخروط دائري", "مستوى قاطع متغير الميل", "مقياس الانحراف e"],
    "math_ellipse": ["محوران كبير وصغير", "بؤرتان ثابتتان", "خيط رابط للبعدين"],
    "math_hyperbola": ["فرعان متقابلان", "خطان مقاربان", "بؤرتان ثابتتان"],
    "math_parabola": ["بؤرة", "دليل مستقيم", "نقاط متساوية البعد"],
    "math_3d_pythagoras": ["مكعب", "قطر وجه", "قطر فراغي"],
    "math_line_plane": ["مستوى", "مستقيم", "متجه طبيعي"],
    "math_dihedral": ["مستويان", "خط التقاطع", "متجهان طبيعيان"],
    "math_probability_space": ["فضاء عينة", "حدث A", "حدث B"],
    "math_derivative": ["منحنى دالة", "نقطة متحركة", "مماس"],
    "math_integral": ["منحنى دالة", "حدود تكامل", "مساحة متراكمة"],
    "math_area_between": ["منحنى علوي", "منحنى سفلي", "فارق المساحة"],
    "math_revolution": ["منحنى", "محور دوران", "أقراص متراكمة"],
}

QUIZZES = {
    "math_complex": {
        "q": "إذا كانت z = r(cosθ + i sinθ) فما الجزء الحقيقي a؟",
        "options": ["a = r cosθ", "a = r sinθ", "a = r²", "a = θ/r"],
        "answer": 0,
        "explain": "الإسقاط على المحور الحقيقي يعطي a = r cosθ.",
    },
    "math_cone_sections": {
        "q": "ما الذي يحدد نوع القطع الناتج من قطع المخروط بمستوى؟",
        "options": ["ميل مستوى القطع", "لون المخروط", "عدد وجوه المخروط", "طول قاعدة المخروط فقط"],
        "answer": 0,
        "explain": "ميل مستوى القطع يحدد الدائرة أو القطع الناقص أو المكافئ أو الزائد.",
    },
    "math_ellipse": {
        "q": "لقطع ناقص نصفا محوره a و b حيث a > b، فما قيمة c؟",
        "options": ["c = √(a² − b²)", "c = a + b", "c = a² + b²", "c = b/a"],
        "answer": 0,
        "explain": "بؤرتا القطع الناقص تقعان عند (±c، 0) حيث c² = a² − b².",
    },
    "math_hyperbola": {
        "q": "خطا مقاربة القطع x²/a² − y²/b² = 1 هما:",
        "options": ["y = ±(b/a)x", "y = ±(a/b)x", "y = ±ab", "y = 0"],
        "answer": 0,
        "explain": "خطا المقاربة للقطع الزائد القياسي هما y = ±(b/a)x.",
    },
    "math_parabola": {
        "q": "بؤرة القطع المكافئ y² = 4px هي:",
        "options": ["(p، 0)", "(0، p)", "(−p، 0)", "(2p، 0)"],
        "answer": 0,
        "explain": "بالصيغة القياسية y² = 4px تكون البؤرة (p، 0) والدليل x = −p.",
    },
    "math_3d_pythagoras": {
        "q": "القطر الفراغي لمكعب ضلعه a يساوي:",
        "options": ["a√3", "a√2", "3a", "a/√3"],
        "answer": 0,
        "explain": "بتطبيق فيثاغورس مرتين: قطر الوجه a√2 ثم القطر الفراغي √(2a²+a²)=a√3.",
    },
    "math_line_plane": {
        "q": "إذا كانت زاوية مستقيم مع متجه طبيعي لمستوى α، فإن زاويته مع المستوى:",
        "options": ["90° − α", "α", "180° − α", "α/2"],
        "answer": 0,
        "explain": "الزاوية مع المستوى مكمّلة للزاوية مع المتجه الطبيعي.",
    },
    "math_dihedral": {
        "q": "تُقاس الزاوية بين مستويين باستخدام:",
        "options": ["المتجهين الطبيعيين للمستويين", "محيط المستويين", "مساحة المستويين", "طول خط التقاطع فقط"],
        "answer": 0,
        "explain": "cosφ = |n₁·n₂|/(|n₁||n₂|) حيث n₁ و n₂ متجهان طبيعيان.",
    },
    "math_probability_space": {
        "q": "قاعدة اتحاد حدثين هي:",
        "options": ["P(A)+P(B)−P(A∩B)", "P(A)+P(B)", "P(A)×P(B)", "P(A)−P(B)"],
        "answer": 0,
        "explain": "يُطرح التقاطع حتى لا يُحسب مرتين.",
    },
    "math_derivative": {
        "q": "إذا كان f(x)=x²/8 فإن f′(x):",
        "options": ["x/4", "x/8", "2x", "x²/4"],
        "answer": 0,
        "explain": "مشتقة x²/8 هي (2x)/8 = x/4.",
    },
    "math_integral": {
        "q": "المساحة تحت f(x)=x/4 من 0 إلى b تساوي:",
        "options": ["b²/8", "b/4", "b²/4", "4b"],
        "answer": 0,
        "explain": "∫₀ᵇ x/4 dx = [x²/8]₀ᵇ = b²/8.",
    },
    "math_area_between": {
        "q": "المساحة بين f(x)=2 و g(x)=x/4 تُحسب بـ:",
        "options": ["∫|f(x)−g(x)|dx", "∫f(x)dx + ∫g(x)dx", "f(x)−g(x) عند نقطة واحدة", "محيط المنحنيين"],
        "answer": 0,
        "explain": "المساحة بين منحنيين هي تكامل القيمة المطلقة للفرق.",
    },
    "math_revolution": {
        "q": "حجم مجسم الدوران بطريقة الأقراص يعطي:",
        "options": ["V = π∫[f(x)]²dx", "V = ∫f(x)dx", "V = 2π∫f(x)dx", "V = π[f(x)]² فقط"],
        "answer": 0,
        "explain": "كل قرص حجمه π[f(x)]²dx ومجموع الأقراص يعطي الحجم.",
    },
}


def extract_three_js():
    text = (BASE_DIR / "thaker-interactive-book.html").read_text(encoding="utf-8")
    start = text.find("!function(t,e){")
    end = text.find("window.THAKER_CURRICULUM_P2")
    chunk = text[start:end]
    close = chunk.rfind("</script>")
    if close != -1:
        chunk = chunk[:close]
    return chunk.strip()


def build_experiments():
    lab = json.loads((BASE_DIR / "data/curriculum/grade12/math/geometry_lab.json").read_text(encoding="utf-8"))
    experiments = []
    for scene in lab["scenes"]:
        steps = []
        for item in scene.get("steps", []):
            detail = item.get("detail", "")
            formula = item.get("formula", "")
            steps.append({
                "title": item.get("title", "خطوة"),
                "desc": detail or formula or scene.get("prompt", ""),
                "params": {c["id"]: c.get("default", c.get("min", 0)) for c in scene.get("controls", [])},
                "obs": formula or detail,
            })
        while len(steps) < 3:
            steps.append({
                "title": f"خطوة {len(steps) + 1}: راقب العلاقة",
                "desc": scene.get("prompt", "غيّر المتغير ولاحظ الأثر."),
                "params": {c["id"]: c.get("default", c.get("min", 0)) for c in scene.get("controls", [])},
                "obs": scene.get("formula", ""),
            })
        sim_key = scene["sim_key"]
        experiments.append({
            "id": scene["id"],
            "unit": scene.get("unit_id", "u1"),
            "unitTitle": UNIT_TITLES.get(scene.get("unit_id", "u1"), "وحدة دراسية"),
            "bookPage": scene.get("page", 7),
            "title": scene["title"],
            "simType": sim_key,
            "formula": scene.get("formula", ""),
            "tools": TOOLS.get(sim_key, ["أدوات المحاكاة", "المتغيرات", "القاعدة الحاكمة"]),
            "controls": scene.get("controls", []),
            "steps": steps,
            "conclusion": f"{scene.get('formula', '')} — {scene.get('prompt', '')}",
            "quiz": QUIZZES.get(sim_key, QUIZZES["math_complex"]),
        })
    return experiments


MATH_LAB_JS = r"""
const EXPERIMENTS = __EXPS_JSON__;

let curExp = EXPERIMENTS[0];
let curStepIdx = 0;
let params = {};
let simTime = 0;
let scene3d, camera3d, renderer3d = null, modelGroup = null, webglReady = false;
let rotY = 0.2, rotX = 0.12;
let dynObjs = {};

function init3D() {
  const c3 = document.getElementById('canvas3d');
  const stage = document.getElementById('stageArea');
  const w = Math.max(300, stage.clientWidth);
  const h = Math.max(240, stage.clientHeight);
  try {
    scene3d = new THREE.Scene();
    camera3d = new THREE.PerspectiveCamera(45, w / h, 0.1, 100);
    camera3d.position.set(0, 1.2, 4.4);
    camera3d.lookAt(0, 0, 0);
    renderer3d = new THREE.WebGLRenderer({ canvas: c3, antialias: true, alpha: true });
    renderer3d.setSize(w, h);
    renderer3d.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    const amb = new THREE.AmbientLight(0xffffff, 0.85);
    const dir = new THREE.DirectionalLight(0xffffff, 0.9);
    dir.position.set(4, 6, 5);
    const pt = new THREE.PointLight(0x10b981, 1.2, 12);
    pt.position.set(-2, 2, 3);
    scene3d.add(amb, dir, pt);
    modelGroup = new THREE.Group();
    scene3d.add(modelGroup);
    webglReady = true;
  } catch (e) {
    webglReady = false;
    c3.style.display = 'none';
  }

  let drag = false, px = 0, py = 0;
  stage.onmousedown = e => { drag = true; px = e.clientX; py = e.clientY; };
  window.onmouseup = () => { drag = false; };
  window.onmousemove = e => {
    if (!drag) return;
    rotY += (e.clientX - px) * 0.01;
    rotX = Math.max(-0.8, Math.min(0.8, rotX + (e.clientY - py) * 0.01));
    px = e.clientX; py = e.clientY;
  };
  stage.ontouchstart = e => { if (e.touches.length === 1) { drag = true; px = e.touches[0].clientX; py = e.touches[0].clientY; } };
  stage.ontouchend = () => { drag = false; };
  stage.ontouchmove = e => {
    if (!drag || e.touches.length !== 1) return;
    rotY += (e.touches[0].clientX - px) * 0.012;
    rotX = Math.max(-0.8, Math.min(0.8, rotX + (e.touches[0].clientY - py) * 0.012));
    px = e.touches[0].clientX; py = e.touches[0].clientY;
  };

  const handleResize = () => {
    const sw = Math.max(260, stage.clientWidth);
    const sh = Math.max(180, stage.clientHeight);
    if (renderer3d && camera3d) {
      camera3d.aspect = sw / sh;
      camera3d.updateProjectionMatrix();
      renderer3d.setSize(sw, sh);
    }
    const c2 = document.getElementById('canvas2d');
    c2.width = sw;
    c2.height = sh;
  };
  window.addEventListener('resize', handleResize);
  if (window.ResizeObserver) new ResizeObserver(handleResize).observe(stage);
  handleResize();
}

function addMesh(geo, color, x=0, y=0, z=0, rx=0, ry=0, rz=0, opacity=1) {
  const mat = new THREE.MeshPhongMaterial({ color, transparent: opacity < 1, opacity, shininess: 70 });
  const m = new THREE.Mesh(geo, mat);
  m.position.set(x, y, z);
  m.rotation.set(rx, ry, rz);
  modelGroup.add(m);
  return m;
}

function addLine(points, color) {
  const geo = new THREE.BufferGeometry().setFromPoints(points.map(p => new THREE.Vector3(p[0], p[1], p[2])));
  const line = new THREE.Line(geo, new THREE.LineBasicMaterial({ color: color || 0x10b981 }));
  modelGroup.add(line);
  return line;
}

function build3dForExperiment() {
  if (!webglReady || !modelGroup) return;
  while (modelGroup.children.length) modelGroup.remove(modelGroup.children[0]);
  dynObjs = {};
  const st = curExp.simType;
  addMesh(new THREE.BoxGeometry(3.8, 0.08, 1.8), 0x1e293b, 0, -0.95, 0);

  if (st === 'math_complex') {
    addLine([[-1.4,0,0],[1.4,0,0]], 0x64748b);
    addLine([[0,-1.05,0],[0,1.05,0]], 0x64748b);
    dynObjs.point = addMesh(new THREE.SphereGeometry(0.13, 20, 20), 0x10b981, 0.9, 0.9, 0);
  } else if (st === 'math_cone_sections') {
    addMesh(new THREE.ConeGeometry(0.95, 1.9, 32, 1, true), 0x38bdf8, 0, 0.05, 0, 0, 0, 0, 0.5);
    dynObjs.plane = addMesh(new THREE.BoxGeometry(1.9, 0.035, 1.15), 0xf59e0b, 0, 0.1, 0, 0, 0, 0, 0.85);
  } else if (st === 'math_ellipse' || st === 'math_hyperbola' || st === 'math_parabola') {
    const curve = new THREE.Group();
    const a = params.a ?? 3, b = params.b ?? 2, p = params.p ?? 2;
    for (let i = 0; i < 44; i++) {
      const t = i / 43;
      let X = 0, Y = 0;
      if (st === 'math_ellipse') { const ang = t * Math.PI * 2; X = Math.cos(ang) * Math.min(1.25, a/5); Y = Math.sin(ang) * Math.min(0.85, b/5); }
      else if (st === 'math_hyperbola') { const x = -1.25 + t*2.5; X = x; Y = Math.sign(x) * Math.sqrt(Math.max(0, x*x/a - 1)) * 0.42; }
      else { const y = -1 + t*2; X = y*y/(4*p) * 1.15; Y = y; }
      const dot = new THREE.Mesh(new THREE.SphereGeometry(0.045, 10, 10), new THREE.MeshPhongMaterial({ color: 0x10b981 }));
      dot.position.set(X, Y, 0);
      curve.add(dot);
    }
    modelGroup.add(curve);
    addLine([[-1.35,0,0],[1.35,0,0]], 0x64748b);
    addLine([[0,-1.05,0],[0,1.05,0]], 0x64748b);
    dynObjs.curve = curve;
  } else if (st === 'math_3d_pythagoras') {
    const cube = new THREE.Group();
    cube.add(new THREE.Mesh(new THREE.BoxGeometry(1.4, 1.4, 1.4), new THREE.MeshPhongMaterial({ color: 0x10b981, transparent: true, opacity: 0.12 })));
    cube.add(new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.BoxGeometry(1.4, 1.4, 1.4)), new THREE.LineBasicMaterial({ color: 0x10b981 })));
    cube.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(-0.7,-0.7,-0.7), new THREE.Vector3(0.7,0.7,0.7)]), new THREE.LineBasicMaterial({ color: 0xf59e0b })));
    modelGroup.add(cube);
    dynObjs.cube = cube;
  } else if (st === 'math_line_plane') {
    addMesh(new THREE.BoxGeometry(2.5, 0.035, 1.55), 0x0ea5e9, 0, -0.35, 0, 0, 0, 0, 0.55);
    dynObjs.line = addMesh(new THREE.CylinderGeometry(0.035, 0.035, 1.9, 12), 0xf59e0b, 0, 0.35, 0, 0, 0, Math.PI/3);
    dynObjs.normal = addMesh(new THREE.CylinderGeometry(0.025, 0.025, 1.1, 12), 0x10b981, 0, 0.15, 0);
  } else if (st === 'math_dihedral') {
    addMesh(new THREE.BoxGeometry(2.0, 0.035, 1.2), 0x38bdf8, 0, -0.15, 0, 0, 0, 0, 0.5);
    dynObjs.plane2 = addMesh(new THREE.BoxGeometry(2.0, 0.035, 1.2), 0x10b981, 0, -0.15, 0, 0, 0, 0, 0.5);
  } else if (st === 'math_probability_space') {
    dynObjs.a = addMesh(new THREE.SphereGeometry(0.52, 24, 24), 0x10b981, -0.34, 0, 0, 0, 0, 0, 0.35);
    dynObjs.b = addMesh(new THREE.SphereGeometry(0.52, 24, 24), 0x38bdf8, 0.34, 0, 0, 0, 0, 0, 0.35);
  } else if (st === 'math_derivative' || st === 'math_integral' || st === 'math_area_between') {
    const curve = new THREE.Group();
    for (let i = 0; i <= 18; i++) {
      const x = i * 0.13 - 1.2, y = x*x*0.42 - 0.7;
      const dot = new THREE.Mesh(new THREE.SphereGeometry(0.045, 10, 10), new THREE.MeshPhongMaterial({ color: 0x10b981 }));
      dot.position.set(x, y, 0);
      curve.add(dot);
    }
    modelGroup.add(curve);
    dynObjs.marker = addMesh(new THREE.SphereGeometry(0.1, 16, 16), 0xf59e0b, 0, -0.55, 0);
  } else if (st === 'math_revolution') {
    const discs = new THREE.Group();
    for (let i = 0; i < 12; i++) {
      const r = 0.12 + i * 0.095;
      const disc = new THREE.Mesh(new THREE.CylinderGeometry(r, r, 0.025, 24), new THREE.MeshPhongMaterial({ color: 0x10b981, transparent: true, opacity: 0.65 }));
      disc.rotation.z = Math.PI / 2;
      disc.position.x = -1.25 + i * 0.22;
      discs.add(disc);
    }
    modelGroup.add(discs);
    dynObjs.discs = discs;
  }
}

function fmt(v) {
  if (!Number.isFinite(v)) return '—';
  if (Math.abs(v) >= 1000 || (Math.abs(v) > 0 && Math.abs(v) < 0.001)) return v.toExponential(3);
  return String(Number(v.toFixed(3)));
}

function computeSimulationResults() {
  const st = curExp.simType;
  if (st === 'math_complex') {
    const r = params.r ?? 5, th = (params.theta ?? 45) * Math.PI / 180;
    const a = r * Math.cos(th), b = r * Math.sin(th);
    return { short: `z = ${fmt(a)} + ${fmt(b)}i`, detail: `r = ${r}، θ = ${params.theta ?? 45}°` };
  }
  if (st === 'math_cone_sections') {
    const t = params.tilt ?? 35;
    const type = t === 0 ? 'دائرة' : (t < 45 ? 'قطع ناقص' : (t === 45 ? 'قطع مكافئ' : 'قطع زائد'));
    return { short: `القطع: ${type}`, detail: `ميل المستوى = ${t}°` };
  }
  if (st === 'math_ellipse') {
    const a = params.a ?? 5, b = params.b ?? 3, c = Math.sqrt(Math.max(0, a*a - b*b));
    return { short: `c = ${fmt(c)}`, detail: `البؤرتان: (±${fmt(c)}, 0)` };
  }
  if (st === 'math_hyperbola') {
    const a = params.a ?? 2, b = params.b ?? 3;
    return { short: `y = ±${fmt(b/a)}x`, detail: `|PF₁−PF₂| = ${2*a}` };
  }
  if (st === 'math_parabola') {
    const p = params.p ?? 2;
    return { short: `F = (${p}, 0)`, detail: `الدليل: x = −${p}` };
  }
  if (st === 'math_3d_pythagoras') {
    const a = params.a ?? 4;
    return { short: `d = ${fmt(a * Math.sqrt(3))}`, detail: `a√3 عند a = ${a}` };
  }
  if (st === 'math_line_plane') {
    const alpha = params.alpha ?? 40;
    return { short: `θ = ${90 - alpha}°`, detail: `θ = 90° − α` };
  }
  if (st === 'math_dihedral') {
    const phi = params.phi ?? 60;
    return { short: `φ = ${phi}°`, detail: `cosφ = |n₁·n₂|/(|n₁||n₂|)` };
  }
  if (st === 'math_probability_space') {
    const pa = params.pa ?? 55, pb = params.pb ?? 40;
    const inter = Math.max(0, Math.min(params.inter ?? 20, pa, pb));
    return { short: `P(A∪B) = ${fmt(pa + pb - inter)}%`, detail: `P(A)+P(B)−P(A∩B)` };
  }
  if (st === 'math_derivative') {
    const x = params.x ?? 4;
    return { short: `f′(${x}) = ${fmt(x/4)}`, detail: `f(x)=x²/8 ⇒ f′(x)=x/4` };
  }
  if (st === 'math_integral') {
    const b = params.b ?? 6;
    return { short: `A = ${fmt(b*b/8)}`, detail: `∫₀ᵇ x/4 dx = b²/8` };
  }
  if (st === 'math_area_between') {
    const b = params.b ?? 5;
    const area = b <= 8 ? (2*b - b*b/8) : (b*b/8 - 2*b + 16);
    return { short: `A = ${fmt(area)}`, detail: `∫₀ᵇ |2 − x/4| dx` };
  }
  if (st === 'math_revolution') {
    const n = params.n ?? 10, dx = 2 / n;
    let v = 0;
    for (let i = 0; i < n; i++) { const x = i * dx; v += Math.PI * x*x * dx; }
    return { short: `V ≈ ${fmt(v)}`, detail: `${n} أقراص، dV = π[f(x)]²dx` };
  }
  return { short: curExp.formula || '', detail: '' };
}

function draw2DOverlay() {
  const c2 = document.getElementById('canvas2d');
  const ctx = c2.getContext('2d');
  const w = c2.width, h = c2.height;
  ctx.clearRect(0, 0, w, h);
  if (!webglReady) { ctx.fillStyle = '#091522'; ctx.fillRect(0, 0, w, h); }
  const cx = w / 2, cy = h / 2;
  const px = x => cx + x * (w / 14);
  const py = y => cy - y * (h / 12);
  const label = (s, x, y, color, size) => {
    ctx.fillStyle = color || '#E2E8F0';
    ctx.font = `bold ${size || 13}px Tajawal, sans-serif`;
    ctx.textAlign = 'center';
    ctx.fillText(s, x, y);
  };
  ctx.save();
  ctx.strokeStyle = '#475569';
  ctx.lineWidth = 1;
  ctx.beginPath(); ctx.moveTo(10, cy); ctx.lineTo(w-10, cy); ctx.moveTo(cx, 10); ctx.lineTo(cx, h-10); ctx.stroke();
  label(curExp.formula, cx, 24, '#6EE7B7', 14);
  const st = curExp.simType;

  if (st === 'math_complex') {
    const r = params.r ?? 5, th = (params.theta ?? 45) * Math.PI / 180;
    const x = r * Math.cos(th), y = r * Math.sin(th);
    ctx.strokeStyle = '#10B981'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(px(x), py(y)); ctx.stroke();
    ctx.fillStyle = '#34d399'; ctx.beginPath(); ctx.arc(px(x), py(y), 6, 0, Math.PI*2); ctx.fill();
  } else if (st === 'math_cone_sections') {
    ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(px(-4), py(-3)); ctx.lineTo(px(0), py(4)); ctx.lineTo(px(4), py(-3)); ctx.stroke();
    ctx.strokeStyle = '#f59e0b';
    ctx.beginPath(); ctx.moveTo(px(-3.5), py(1)); ctx.lineTo(px(3.5), py(1 + Math.tan((params.tilt ?? 35) * Math.PI/180))); ctx.stroke();
  } else if (st === 'math_ellipse' || st === 'math_hyperbola' || st === 'math_parabola') {
    const a = params.a ?? 4, b = params.b ?? 3, p = params.p ?? 2;
    ctx.strokeStyle = '#10B981'; ctx.lineWidth = 2; ctx.beginPath();
    if (st === 'math_ellipse') {
      for (let t = 0; t <= Math.PI*2 + 0.01; t += 0.05) { const X = a*Math.cos(t), Y = b*Math.sin(t); if (t === 0) ctx.moveTo(px(X), py(Y)); else ctx.lineTo(px(X), py(Y)); }
    } else if (st === 'math_hyperbola') {
      for (let x = -6; x <= 6; x += 0.1) if (Math.abs(x) >= a) { const y = (b/a)*Math.sqrt(x*x-a*a); ctx.lineTo(px(x), py(y)); }
      ctx.stroke(); ctx.beginPath();
      for (let x = -6; x <= 6; x += 0.1) if (Math.abs(x) >= a) { const y = -(b/a)*Math.sqrt(x*x-a*a); ctx.lineTo(px(x), py(y)); }
    } else {
      for (let y = -5; y <= 5; y += 0.1) { const x = y*y/(4*p); if (y === -5) ctx.moveTo(px(x), py(y)); else ctx.lineTo(px(x), py(y)); }
    }
    ctx.stroke();
  } else if (st === 'math_probability_space') {
    ctx.strokeStyle = '#10B981'; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.arc(cx - 34, cy, 58, 0, Math.PI*2); ctx.stroke();
    ctx.strokeStyle = '#38bdf8'; ctx.beginPath(); ctx.arc(cx + 34, cy, 58, 0, Math.PI*2); ctx.stroke();
  } else if (st === 'math_derivative' || st === 'math_integral' || st === 'math_area_between') {
    ctx.strokeStyle = '#10B981'; ctx.lineWidth = 2; ctx.beginPath();
    for (let x = 0; x <= 9; x += 0.1) { const y = x*x/8; if (x === 0) ctx.moveTo(px(x), py(y)); else ctx.lineTo(px(x), py(y)); }
    ctx.stroke();
    const bx = params.x ?? params.b ?? 5;
    ctx.fillStyle = 'rgba(16,185,129,0.22)';
    ctx.fillRect(px(0), py(bx*bx/8), px(bx)-px(0), Math.max(0, py(0)-py(bx*bx/8)));
  } else if (st === 'math_revolution') {
    for (let i = 0; i < Math.min(20, params.n ?? 10); i++) {
      const y = py(i * 0.32 - 2.2), r = (i * 0.32 + 0.3) * (w/40);
      ctx.strokeStyle = '#10B981'; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.ellipse(cx, y, r, 8, 0, 0, Math.PI*2); ctx.stroke();
    }
  } else if (st === 'math_3d_pythagoras' || st === 'math_line_plane' || st === 'math_dihedral') {
    label(computeSimulationResults().short, cx, cy, '#6EE7B7', 18);
  }
  label(computeSimulationResults().short, cx, h - 22, '#D1FAE5', 13);
  ctx.restore();
}

function animateLoop() {
  requestAnimationFrame(animateLoop);
  simTime += 0.016;
  const st = curExp.simType;
  if (webglReady && modelGroup) {
    modelGroup.rotation.y = rotY;
    modelGroup.rotation.x = rotX;
    if (st === 'math_complex' && dynObjs.point) {
      const r = params.r ?? 5, th = (params.theta ?? 45) * Math.PI / 180;
      dynObjs.point.position.set(Math.cos(th) * r/7, Math.sin(th) * r/7, Math.sin(th) * r/20);
    }
    if (st === 'math_cone_sections' && dynObjs.plane) dynObjs.plane.rotation.x = -(params.tilt ?? 35) * Math.PI / 180;
    if (st === 'math_3d_pythagoras' && dynObjs.cube) dynObjs.cube.scale.setScalar(Math.max(0.35, Math.min(1.7, (params.a ?? 4) / 4)));
    if (st === 'math_line_plane' && dynObjs.line && dynObjs.normal) {
      dynObjs.line.rotation.z = (90 - (params.alpha ?? 40)) * Math.PI / 180;
      dynObjs.normal.rotation.z = -(params.alpha ?? 40) * Math.PI / 180;
    }
    if (st === 'math_dihedral' && dynObjs.plane2) dynObjs.plane2.rotation.y = (params.phi ?? 60) * Math.PI / 180;
    if (st === 'math_probability_space' && dynObjs.a && dynObjs.b) {
      dynObjs.a.scale.setScalar(Math.max(0.55, (params.pa ?? 55) / 70));
      dynObjs.b.scale.setScalar(Math.max(0.55, (params.pb ?? 40) / 70));
    }
    if ((st === 'math_derivative' || st === 'math_integral' || st === 'math_area_between') && dynObjs.marker) {
      const x = Math.max(-1.2, Math.min(1.2, ((params.x ?? params.b ?? 4) - 5) / 4));
      dynObjs.marker.position.set(x, x*x*0.42 - 0.7, 0);
    }
    if (st === 'math_revolution' && dynObjs.discs) {
      dynObjs.discs.children.forEach((d, i) => { d.visible = i < Math.max(2, Math.min(12, params.n ?? 10)); });
    }
    renderer3d.render(scene3d, camera3d);
  }
  draw2DOverlay();
}
"""


def main():
    experiments = build_experiments()
    three_js = extract_three_js()
    exps_json = json.dumps(experiments, ensure_ascii=False)
    lab_js = MATH_LAB_JS.replace("__EXPS_JSON__", exps_json)
    v3_css = build_v3_lab_css("#10B981", "16, 185, 129")
    v3_body = build_v3_lab_body_html("معمل الرياضيات التفاعلي 3D", "إلى كتاب الرياضيات")
    v3_body = v3_body.replace("18 نشاطاً", f"{len(experiments)} نشاطاً")
    v3_ctrl_js = build_v3_lab_controller_js("EXPERIMENTS", "math-12th-book.html")

    html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=2.0, user-scalable=yes">
<title>معمل الرياضيات التفاعلي 3D — الصف الثالث الثانوي (ذاكر)</title>
<style>
{v3_css}
</style>
</head>
<body>
{v3_body}

<script>
{three_js}
</script>

<script>
{lab_js}

{v3_ctrl_js}
</script>
</body>
</html>"""

    out_root = BASE_DIR / "math-12th-lab.html"
    out_mirror = BASE_DIR / "thaker-android-src/assets/math-12th-lab.html"
    out_root.write_text(html, encoding="utf-8")
    shutil.copy2(out_root, out_mirror)
    print(f"[✓] math-12th-lab.html generated & mirrored ({len(html)//1024} KB) with {len(experiments)} interactive scenes!")


if __name__ == "__main__":
    main()
