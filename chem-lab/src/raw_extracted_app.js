const $=s=>document.querySelector(s),clamp=(v,a,b)=>Math.min(b,Math.max(a,v));

const $$ = s => Array.from(document.querySelectorAll(s));

// ==========================================
// 1. UTILITIES & AUDIO SYNTHESIZER
// ==========================================
const F = 'Tajawal,Tahoma,"Segoe UI",Arial,sans-serif';
const N = n => n.toLocaleString('ar-EG');
const cl = (v, a, b) => Math.min(b, Math.max(a, v));
const lerp = (a, b, t) => a + (b - a) * t;
const CM = (a, b, t) => new THREE.Color(a).lerp(new THREE.Color(b), cl(t, 0, 1));

// Web Audio API Standalone Synthesizer (Zero external files!)
class SoundEngine {
  constructor() {
    this.ctx = null;
    this.enabled = true;
  }
  init() {
    if (!this.ctx && (window.AudioContext || window.webkitAudioContext)) {
      this.ctx = new (window.AudioContext || window.webkitAudioContext)();
    }
  }
  playPour(duration = 0.8) {
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    try {
      const bufferSize = this.ctx.sampleRate * duration;
      const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
      const data = buffer.getChannelData(0);
      for (let i = 0; i < bufferSize; i++) {
        data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (bufferSize * 0.7));
      }
      const noise = this.ctx.createBufferSource();
      noise.buffer = buffer;
      const filter = this.ctx.createBiquadFilter();
      filter.type = 'bandpass';
      filter.frequency.setValueAtTime(1400, this.ctx.currentTime);
      filter.frequency.exponentialRampToValueAtTime(700, this.ctx.currentTime + duration);
      filter.Q.value = 5.0;
      const gain = this.ctx.createGain();
      gain.gain.setValueAtTime(0.22, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + duration);
      noise.connect(filter);
      filter.connect(gain);
      gain.connect(this.ctx.destination);
      noise.start();
    } catch (e) {}
  }
  playClink() {
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(1900 + Math.random() * 400, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(800, this.ctx.currentTime + 0.18);
      gain.gain.setValueAtTime(0.18, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.18);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.18);
    } catch (e) {}
  }
  playBubble() {
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      const f = 400 + Math.random() * 500;
      osc.frequency.setValueAtTime(f, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(f * 1.8, this.ctx.currentTime + 0.08);
      gain.gain.setValueAtTime(0.12, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.08);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.08);
    } catch (e) {}
  }
  playIgnite() {
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(220, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(90, this.ctx.currentTime + 0.35);
      gain.gain.setValueAtTime(0.2, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.35);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.35);
    } catch (e) {}
  }
  playPop() {
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(350, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(80, this.ctx.currentTime + 0.12);
      gain.gain.setValueAtTime(0.4, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.12);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.12);
    } catch (e) {}
  }
  playSuccess() {
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    try {
      [523.25, 659.25, 783.99, 1046.5].forEach((freq, idx) => {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.value = freq;
        const start = this.ctx.currentTime + idx * 0.07;
        gain.gain.setValueAtTime(0.12, start);
        gain.gain.exponentialRampToValueAtTime(0.001, start + 0.35);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(start);
        osc.stop(start + 0.35);
      });
    } catch (e) {}
  }
}
const audio = new SoundEngine();
function toggleAudio() {
  audio.enabled = !audio.enabled;
  $('#mutb').textContent = audio.enabled ? '🔊' : '🔇';
  showToast(audio.enabled ? 'المؤثرات الصوتية مفعّلة' : 'تم كتم المؤثرات الصوتية');
}

// Toast helper
function showToast(text, duration = 2400) {
  const t = $('#dragToast');
  if (!t) return;
  t.textContent = text;
  t.classList.add('visible');
  clearTimeout(t._tm);
  t._tm = setTimeout(() => t.classList.remove('visible'), duration);
}

// ==========================================
// 2. THREE.JS SCENE SETUP & LIGHTING
// ==========================================
const canvas = $('#c');
const R = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });
R.setPixelRatio(Math.min(devicePixelRatio, 2));
R.outputEncoding = THREE.sRGBEncoding;
R.shadowMap.enabled = true;
R.shadowMap.type = THREE.PCFSoftShadowMap;

const S = new THREE.Scene();
const isDark = matchMedia('(prefers-color-scheme: dark)').matches;
S.background = new THREE.Color(isDark ? 0x14100c : 0xe9dcc8);

const cam = new THREE.PerspectiveCamera(40, innerWidth / innerHeight, 0.1, 100);

// Lights
const ambLight = new THREE.AmbientLight(0xffffff, 0.85);
S.add(ambLight);

const dirLight = new THREE.DirectionalLight(0xfff7ed, 0.75);
dirLight.position.set(5, 11, 7);
dirLight.castShadow = true;
dirLight.shadow.mapSize.set(2048, 2048);
dirLight.shadow.camera.left = -10;
dirLight.shadow.camera.right = 10;
dirLight.shadow.camera.top = 10;
dirLight.shadow.camera.bottom = -10;
dirLight.shadow.camera.near = 0.5;
dirLight.shadow.camera.far = 30;
dirLight.shadow.bias = -0.0004;
S.add(dirLight);

// Dynamic Reaction Point Light (lights up when flame, redox, or reactions fire)
const reactionLight = new THREE.PointLight(0xff9922, 0, 7);
reactionLight.position.set(-1.6, 2.0, 0);
S.add(reactionLight);

// Materials & Mesh Helpers
const M = opt => new THREE.MeshLambertMaterial(opt);
const MP = opt => {
  const o = Object.assign({ shininess: 35 }, opt || {});
  delete o.roughness;
  delete o.metalness;
  return new THREE.MeshPhongMaterial(o);
};
const GLS = new THREE.MeshPhongMaterial({
  color: 0xe0f2fe,
  transparent: true,
  opacity: 0.28,
  shininess: 95,
  specular: 0xffffff,
  side: THREE.DoubleSide,
  depthWrite: false
});

// Table (rich wood tabletop with bevel and shadows)
const tableCanvas = document.createElement('canvas');
tableCanvas.width = tableCanvas.height = 512;
const tx = tableCanvas.getContext('2d');
tx.fillStyle = '#8b5a2b';
tx.fillRect(0, 0, 512, 512);
for (let i = 0; i < 110; i++) {
  tx.strokeStyle = `rgba(${50 + Math.random() * 50 | 0}, 28, 12, ${0.08 + Math.random() * 0.16})`;
  tx.lineWidth = 1 + Math.random() * 4;
  tx.beginPath();
  const y = Math.random() * 512;
  tx.moveTo(0, y);
  tx.bezierCurveTo(170, y + (Math.random() * 30 - 15), 340, y + (Math.random() * 30 - 15), 512, y);
  tx.stroke();
}
const tableTex = new THREE.CanvasTexture(tableCanvas);
tableTex.wrapS = tableTex.wrapT = THREE.RepeatWrapping;
tableTex.repeat.set(6, 4);
tableTex.encoding = THREE.sRGBEncoding;

const tableGeo = new THREE.BoxGeometry(36, 0.2, 24);
const tableMesh = new THREE.Mesh(tableGeo, M({ map: tableTex }));
tableMesh.position.y = -0.1;
tableMesh.receiveShadow = true;
S.add(tableMesh);

// 3D Open Chemistry Textbook
const aniso = R.capabilities.getMaxAnisotropy();
const bookGroup = new THREE.Group();
bookGroup.position.set(0, 0, 0); // Open textbook centered at origin
S.add(bookGroup);

// Leather Cover and pages block
const coverMat = MP({ color: 0x5a1818, roughness: 0.6 });
const cover = new THREE.Mesh(new THREE.BoxGeometry(2 * PW + 0.34, 0.14, PH + 0.26), coverMat);
cover.position.set(0, 0, 0);
cover.receiveShadow = true;
bookGroup.add(cover);

const pagesBlock = new THREE.Mesh(
  new THREE.BoxGeometry(2 * PW + 0.18, 0.14, PH + 0.14),
  MP({ color: 0xfaf4e8 })
);
pagesBlock.position.set(0, 0.1, 0);
pagesBlock.castShadow = true;
pagesBlock.receiveShadow = true;
bookGroup.add(pagesBlock);

// Page Curvature Geometry Builder
function buildCurvedPage(side, texture) {
  const geo = new THREE.PlaneGeometry(PW, PH, 32, 1);
  geo.translate(PW / 2 * side, 0, 0);
  const pos = geo.attributes.position;
  for (let i = 0; i < pos.count; i++) {
    const x = pos.getX(i);
    pos.setZ(i, 0.11 * Math.sin(Math.min(Math.abs(x) / PW, 1) * 2.2));
  }
  geo.computeVertexNormals();
  const mat = MP({ map: texture, side: THREE.DoubleSide });
  const mesh = new THREE.Mesh(geo, mat);
  mesh.rotation.x = -Math.PI / 2;
  mesh.receiveShadow = true;
  const pivot = new THREE.Group();
  pivot.position.y = 0.18;
  pivot.add(mesh);
  bookGroup.add(pivot);
  mesh.userData.pivot = pivot;
  return mesh;
}

// Scanned Textbook Textures
const textbookTex = new THREE.Texture();
textbookTex.encoding = THREE.sRGBEncoding;
textbookTex.anisotropy = aniso;
const PR = buildCurvedPage(1, textbookTex);
const pivR = PR.userData.pivot;

// Left Page Canvas (Illustrated Lesson Guide & Holographic Base)
const leftPageCanvas = document.createElement('canvas');
leftPageCanvas.width = 1024;
leftPageCanvas.height = 1360;
const lctx = leftPageCanvas.getContext('2d');
const leftPageTex = new THREE.CanvasTexture(leftPageCanvas);
leftPageTex.encoding = THREE.sRGBEncoding;
leftPageTex.anisotropy = aniso;
const L = buildCurvedPage(-1, leftPageTex);
const pivL = L.userData.pivot;

function updateLeftPageText(exp) {
  const w = 1024, h = 1360;

  // 1. Deep technical laboratory mat base
  const bgGrad = lctx.createLinearGradient(0, 0, w, h);
  bgGrad.addColorStop(0, '#081724');
  bgGrad.addColorStop(0.5, '#0b1f2e');
  bgGrad.addColorStop(1, '#06131e');
  lctx.fillStyle = bgGrad;
  lctx.fillRect(0, 0, w, h);

  // 2. Distinct Checkered Pattern (مربعات متناوبة واضحة وجميلة)
  const tileSize = 64;
  for (let x = 32; x < w - 32; x += tileSize) {
    for (let y = 32; y < h - 32; y += tileSize) {
      const isEven = (Math.floor((x - 32) / tileSize) + Math.floor((y - 32) / tileSize)) % 2 === 0;
      lctx.fillStyle = isEven ? 'rgba(14, 116, 144, 0.12)' : 'rgba(2, 132, 199, 0.04)';
      lctx.fillRect(x, y, tileSize, tileSize);
    }
  }

  // 3. Precision Technical Grid Lines (مربعات القياس الهندسي الدقيق)
  lctx.strokeStyle = 'rgba(34, 211, 238, 0.10)';
  lctx.lineWidth = 1;
  for (let x = 32; x < w - 32; x += 16) {
    lctx.beginPath(); lctx.moveTo(x, 32); lctx.lineTo(x, h - 32); lctx.stroke();
  }
  for (let y = 32; y < h - 32; y += 16) {
    lctx.beginPath(); lctx.moveTo(32, y); lctx.lineTo(w - 32, y); lctx.stroke();
  }

  lctx.strokeStyle = 'rgba(34, 211, 238, 0.32)';
  lctx.lineWidth = 1.8;
  for (let x = 32; x <= w - 32; x += 64) {
    lctx.beginPath(); lctx.moveTo(x, 32); lctx.lineTo(x, h - 32); lctx.stroke();
  }
  for (let y = 32; y <= h - 32; y += 64) {
    lctx.beginPath(); lctx.moveTo(32, y); lctx.lineTo(w - 32, y); lctx.stroke();
  }

  // Intersection crosshairs (+)
  lctx.fillStyle = 'rgba(56, 189, 248, 0.65)';
  for (let x = 96; x < w - 64; x += 128) {
    for (let y = 96; y < h - 64; y += 128) {
      lctx.fillRect(x - 4, y - 0.75, 9, 1.5);
      lctx.fillRect(x - 0.75, y - 4, 1.5, 9);
    }
  }

  // 4. Circular Reaction Target Zones
  lctx.strokeStyle = 'rgba(34, 211, 238, 0.38)';
  lctx.lineWidth = 2;
  lctx.setLineDash([8, 6]);
  lctx.beginPath();
  lctx.arc(w / 2, h / 2 + 60, 220, 0, Math.PI * 2);
  lctx.stroke();
  lctx.beginPath();
  lctx.arc(w / 2, h / 2 + 60, 140, 0, Math.PI * 2);
  lctx.stroke();
  lctx.beginPath();
  lctx.arc(w / 2, h / 2 + 60, 60, 0, Math.PI * 2);
  lctx.stroke();
  lctx.setLineDash([]);

  // Zone Labels
  lctx.fillStyle = 'rgba(34, 211, 238, 0.5)';
  lctx.font = 'bold 18px Tajawal, sans-serif';
  lctx.textAlign = 'center';
  lctx.fillText('⚗️ مَنطِقَةُ التَّفَاعُلِ الكِيمْيَائِيِّ الرَّئِيسِيَّة', w / 2, h / 2 + 60);

  lctx.fillStyle = 'rgba(56, 189, 248, 0.4)';
  lctx.font = 'bold 15px Tajawal, sans-serif';
  lctx.textAlign = 'right';
  lctx.fillText('◀ مِنَصَّةُ الكَوَاشِفِ وَالقَطَّارَاتِ', w - 50, h / 2 + 60);
  lctx.textAlign = 'left';
  lctx.fillText('مِنَصَّةُ الأَجْهِزَةِ وَالقِيَاسِ ▶', 50, h / 2 + 60);

  // 5. Border Rulers with Millimeter Ticks & Metric Scale
  lctx.strokeStyle = '#0284c7';
  lctx.lineWidth = 3;
  lctx.strokeRect(32, 32, w - 64, h - 64);

  lctx.strokeStyle = 'rgba(34, 211, 238, 0.7)';
  lctx.lineWidth = 1.5;
  for (let x = 32; x <= w - 32; x += 8) {
    const isMajor = (x - 32) % 64 === 0;
    const isMid = (x - 32) % 32 === 0;
    const tickLen = isMajor ? 14 : (isMid ? 9 : 5);
    lctx.beginPath(); lctx.moveTo(x, 32); lctx.lineTo(x, 32 + tickLen); lctx.stroke();
    lctx.beginPath(); lctx.moveTo(x, h - 32); lctx.lineTo(x, h - 32 - tickLen); lctx.stroke();
    if (isMajor && x < w - 60) {
      lctx.fillStyle = 'rgba(34, 211, 238, 0.6)';
      lctx.font = '10px monospace';
      lctx.textAlign = 'center';
      lctx.fillText(`${(x - 32) / 8}`, x, 56);
    }
  }
  for (let y = 32; y <= h - 32; y += 8) {
    const isMajor = (y - 32) % 64 === 0;
    const isMid = (y - 32) % 32 === 0;
    const tickLen = isMajor ? 14 : (isMid ? 9 : 5);
    lctx.beginPath(); lctx.moveTo(32, y); lctx.lineTo(32 + tickLen, y); lctx.stroke();
    lctx.beginPath(); lctx.moveTo(w - 32, y); lctx.lineTo(w - 32 - tickLen, y); lctx.stroke();
    if (isMajor && y < h - 50) {
      lctx.fillStyle = 'rgba(34, 211, 238, 0.6)';
      lctx.font = '10px monospace';
      lctx.textAlign = 'left';
      lctx.fillText(`${(y - 32) / 8}`, 48, y + 4);
    }
  }

  // 6. Corner Technical Brackets
  const drawCornerBracket = (cx, cy, dirX, dirY) => {
    lctx.strokeStyle = '#38bdf8';
    lctx.lineWidth = 3;
    lctx.beginPath();
    lctx.moveTo(cx + dirX * 36, cy);
    lctx.lineTo(cx, cy);
    lctx.lineTo(cx, cy + dirY * 36);
    lctx.stroke();
    lctx.fillStyle = '#f59e0b';
    lctx.beginPath();
    lctx.arc(cx + dirX * 12, cy + dirY * 12, 3, 0, Math.PI * 2);
    lctx.fill();
  };
  drawCornerBracket(42, 42, 1, 1);
  drawCornerBracket(w - 42, 42, -1, 1);
  drawCornerBracket(42, h - 42, 1, -1);
  drawCornerBracket(w - 42, h - 42, -1, -1);

  // 7. Footer Quality & Certification Badge
  lctx.fillStyle = 'rgba(148, 163, 184, 0.6)';
  lctx.font = '12px Tajawal, sans-serif';
  lctx.textAlign = 'center';
  lctx.fillText('🔬 مَنَصَّةُ المَعْمَلِ التَّفَاعُلِيِّ – مُطَابِقَةٌ لِمَعَايِيرِ كِتَابِ الكِيمْيَاءِ المَدْرَسِيِّ (الثَّالِثُ الثَّانَوِيُّ)', w / 2, h - 50);

  leftPageTex.needsUpdate = true;

  if (lab3DTitlePlaque && exp) {
    lab3DTitlePlaque.updateTitle(exp.n);
  }
}
// ==========================================
// 3. CAMERA CONTROLLER & MODES
// ==========================================
const camPreset = {
  // 1. Panoramic book view: both pages visible side-by-side
  book: { pos: new THREE.Vector3(0, 4.6, 7.6), target: new THREE.Vector3(0, 0.35, 0) },
  // 2. Focused on second page (left page 3D lab)
  lab:  { pos: new THREE.Vector3(-PW / 2, 3.2, 4.7), target: new THREE.Vector3(-PW / 2, 0.40, 0) },
  // 3. Focused on first page (right page textbook scan)
  page: { pos: new THREE.Vector3(PW / 2, 3.0, 3.8), target: new THREE.Vector3(PW / 2, 0.25, 0) }
};
let curViewMode = 'book';
const _initDist = camPreset.book.pos.distanceTo(camPreset.book.target);
const camState = {
  pos: camPreset.book.pos.clone(),
  target: camPreset.book.target.clone(),
  orbitTheta: Math.atan2(camPreset.book.pos.x - camPreset.book.target.x, camPreset.book.pos.z - camPreset.book.target.z),
  orbitPhi: Math.acos(cl((camPreset.book.pos.y - camPreset.book.target.y) / _initDist, -1, 1)),
  orbitRadius: _initDist
};
let isOrbiting = false;
let autoOrbit = false;

function view(mode) {
  curViewMode = mode;
  $$('#btnViewBook, #btnViewLab, #btnViewPage').forEach(b => b.classList.remove('active'));
  if (mode === 'book') $('#btnViewBook')?.classList.add('active');
  if (mode === 'lab') $('#btnViewLab')?.classList.add('active');
  if (mode === 'page') $('#btnViewPage')?.classList.add('active');

  const p = camPreset[mode];
  if (p) {
    camState.target.copy(p.target);
    camState.pos.copy(p.pos);
    camState.orbitRadius = p.pos.distanceTo(p.target);
    const dy = cl((p.pos.y - p.target.y) / camState.orbitRadius, -1, 1);
    camState.orbitPhi = Math.acos(dy);
    camState.orbitTheta = Math.atan2(p.pos.x - p.target.x, p.pos.z - p.target.z);
  }
}

// EFFORTLESS POINTER & MULTI-TOUCH CONTROLLER
// 1-Tap or Drag for tools; Smooth background Orbit & Pinch Zoom
// ==========================================
const activePointers = new Map();
let pointerDownTarget = null;
let pointerDownPos = { x: 0, y: 0 };
let pointerMovedDist = 0;
let prevPinchDist = null;
let isPanning = false;

const raycaster = new THREE.Raycaster();
const dragPlane = new THREE.Plane(new THREE.Vector3(0, 1, 0), 0);
const dragPlaneIntersect = new THREE.Vector3();

// Universal Drag and Drop Manager
const draggables = [];
let activeDrag = null;
let hoveredTarget = null;

class DraggableManager {
  static register(item) {
    draggables.push(item);
  }
  static clear() {
    draggables.length = 0;
    activeDrag = null;
    hoveredTarget = null;
  }
}

function updateCamPosFromTarget() {
  const phi = camState.orbitPhi;
  const theta = camState.orbitTheta;
  const r = camState.orbitRadius;
  camState.pos.set(
    camState.target.x + r * Math.sin(phi) * Math.sin(theta),
    camState.target.y + r * Math.cos(phi),
    camState.target.z + r * Math.sin(phi) * Math.cos(theta)
  );
}

function panCamera(dx, dy) {
  const factor = camState.orbitRadius * 0.0016;
  const sinTh = Math.sin(camState.orbitTheta);
  const cosTh = Math.cos(camState.orbitTheta);

  camState.target.x -= (cosTh * dx - sinTh * dy) * factor;
  camState.target.z -= (-sinTh * dx - cosTh * dy) * factor;

  camState.target.x = cl(camState.target.x, -5.0, 5.0);
  camState.target.z = cl(camState.target.z, -3.5, 3.5);
  updateCamPosFromTarget();
}

canvas.addEventListener('pointerdown', e => {
  audio.init();
  canvas.setPointerCapture(e.pointerId);
  activePointers.set(e.pointerId, { x: e.clientX, y: e.clientY, pointerType: e.pointerType });
  pointerDownPos = { x: e.clientX, y: e.clientY };
  pointerMovedDist = 0;

  if (activePointers.size === 1) {
    // Check if clicked/tapped a 3D tool
    const mouse = new THREE.Vector2(
      (e.clientX / innerWidth) * 2 - 1,
      -(e.clientY / innerHeight) * 2 + 1
    );
    raycaster.setFromCamera(mouse, cam);

    const hitDraggable = raycaster.intersectObjects(
      draggables.map(d => d.hitMesh || d.root),
      true
    );

    if (hitDraggable.length > 0) {
      const hitObj = hitDraggable[0].object;
      const item = draggables.find(d => d.hitMesh === hitObj || d.root === hitObj || (d.root.getObjectById && d.root.getObjectById(hitObj.id)));
      if (item && !item.locked) {
        pointerDownTarget = item;
        activeDrag = item;
        const worldPos = new THREE.Vector3();
        item.root.getWorldPosition(worldPos);
        dragPlane.setFromNormalAndCoplanarPoint(new THREE.Vector3(0, 1, 0), worldPos);
        item.onStartDrag?.();
        isOrbiting = false;
        return;
      }
    }

    // Otherwise touching background
    pointerDownTarget = null;
    if (e.button === 2 || e.button === 1) {
      isPanning = true;
    } else {
      isOrbiting = true;
    }
  } else if (activePointers.size === 2) {
    // Two fingers: Pinch-to-zoom and Pan
    if (activeDrag) {
      activeDrag.onDropEmpty?.();
      activeDrag = null;
    }
    isOrbiting = false;
    isPanning = true;
    const pts = [...activePointers.values()];
    prevPinchDist = Math.hypot(pts[0].x - pts[1].x, pts[0].y - pts[1].y);
  }
});

canvas.addEventListener('pointermove', e => {
  if (!activePointers.has(e.pointerId)) return;
  const prevP = activePointers.get(e.pointerId);
  activePointers.set(e.pointerId, { x: e.clientX, y: e.clientY, pointerType: e.pointerType });
  pointerMovedDist += Math.hypot(e.clientX - prevP.x, e.clientY - prevP.y);

  if (activePointers.size === 1) {
    if (activeDrag) {
      // Dragging tool
      const mouse = new THREE.Vector2(
        (e.clientX / innerWidth) * 2 - 1,
        -(e.clientY / innerHeight) * 2 + 1
      );
      raycaster.setFromCamera(mouse, cam);
      if (raycaster.ray.intersectPlane(dragPlane, dragPlaneIntersect)) {
        if (activeDrag.root.parent) {
          const localPos = activeDrag.root.parent.worldToLocal(dragPlaneIntersect.clone());
          activeDrag.root.position.x = cl(localPos.x, -4.5, 2.5);
          activeDrag.root.position.z = cl(localPos.z, -3.0, 3.0);
          activeDrag.onDrag?.(activeDrag.root.position.x, activeDrag.root.position.z);
        }

        let foundTarget = null;
        if (activeDrag.targets) {
          for (const tgt of activeDrag.targets) {
            let tgtLocalX = 0, tgtLocalZ = 0;
            if (tgt.mesh) {
              tgtLocalX = tgt.mesh.position.x;
              tgtLocalZ = tgt.mesh.position.z;
            } else if (tgt.pos) {
              tgtLocalX = tgt.pos.x !== undefined ? tgt.pos.x : tgt.pos[0];
              tgtLocalZ = tgt.pos.z !== undefined ? tgt.pos.z : tgt.pos[2];
            }
            const dist = Math.hypot(activeDrag.root.position.x - tgtLocalX, activeDrag.root.position.z - tgtLocalZ);
            if (dist < (tgt.radius || 1.8)) {
              foundTarget = tgt;
              break;
            }
          }
        }

        if (foundTarget !== hoveredTarget) {
          if (hoveredTarget) hoveredTarget.onHoverExit?.();
          hoveredTarget = foundTarget;
          if (hoveredTarget) {
            hoveredTarget.onHoverEnter?.();
            audio.playBubble();
          }
        }
      }
    } else if (isOrbiting) {
      // Natural 1-finger orbit
      const dx = e.clientX - prevP.x;
      const dy = e.clientY - prevP.y;
      camState.orbitTheta -= dx * 0.0055;
      camState.orbitPhi = cl(camState.orbitPhi + dy * 0.0055, 0.15, 1.45);
      updateCamPosFromTarget();
    } else if (isPanning) {
      const dx = e.clientX - prevP.x;
      const dy = e.clientY - prevP.y;
      panCamera(dx, dy);
    }
  } else if (activePointers.size === 2) {
    // Pinch to Zoom
    const pts = [...activePointers.values()];
    const curDist = Math.hypot(pts[0].x - pts[1].x, pts[0].y - pts[1].y);
    if (prevPinchDist && curDist > 10) {
      const ratio = curDist / prevPinchDist;
      camState.orbitRadius = cl(camState.orbitRadius / ratio, 3.0, 18.0);
      updateCamPosFromTarget();
    }
    prevPinchDist = curDist;
  }
});

canvas.addEventListener('pointerup', e => {
  activePointers.delete(e.pointerId);

  if (activePointers.size === 0) {
    if (activeDrag) {
      if (pointerMovedDist < 8 && pointerDownTarget === activeDrag) {
        // TAP DETECTION! If user simply tapped the tool without dragging:
        // Automatically perform the action on its primary target!
        audio.playClink();
        if (activeDrag.targets && activeDrag.targets.length > 0) {
          activeDrag.targets[0].onDrop?.(activeDrag);
        } else if (activeDrag.onTap) {
          activeDrag.onTap();
        }
      } else if (hoveredTarget) {
        // Dragged and dropped onto target!
        audio.playClink();
        hoveredTarget.onDrop?.(activeDrag);
        hoveredTarget.onHoverExit?.();
        hoveredTarget = null;
      } else {
        activeDrag.onDropEmpty?.();
      }
      activeDrag.onEndDrag?.();
      activeDrag = null;
    }
    pointerDownTarget = null;
    isOrbiting = false;
    isPanning = false;
    prevPinchDist = null;
  }
});
canvas.addEventListener('pointercancel', e => {
  activePointers.delete(e.pointerId);
});
// Context menu disable on canvas (for smooth right click pan on desktop)
canvas.addEventListener('contextmenu', e => e.preventDefault());

canvas.addEventListener('wheel', e => {
  e.preventDefault();
  camState.orbitRadius = cl(camState.orbitRadius * (1 + e.deltaY * 0.001), 3.2, 22);
  updateCamPosFromTarget();
}, { passive: false });

function resizeCanvas() {
  R.setSize(innerWidth, innerHeight, false);
  cam.aspect = innerWidth / innerHeight;
  cam.updateProjectionMatrix();
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

// ==========================================
// 4. PROCEDURAL 3D LAB GLASSWARE & APPARATUS BUILDERS
// ==========================================
const labMasterGroup = new THREE.Group();
const LAB_SCALE = 0.46;
const LAB_OFFSET_X = -PW / 2 + (1.60 * LAB_SCALE); // Center average apparatus (-1.60) exactly on Page 2 (-PW/2 = -1.415)
labMasterGroup.position.set(LAB_OFFSET_X, 0.28, 0); // Sits cleanly on the left page surface (y=0.28)
labMasterGroup.scale.set(LAB_SCALE, LAB_SCALE, LAB_SCALE);
S.add(labMasterGroup);

function makeCyl(rTop, rBot, h, col, x, y, z, matOpt) {
  const mesh = new THREE.Mesh(
    new THREE.CylinderGeometry(rTop, rBot, h, 28),
    MP(Object.assign({ color: col }, matOpt || {}))
  );
  mesh.position.set(x, y, z);
  mesh.castShadow = true;
  mesh.receiveShadow = true;
  return mesh;
}

function makeBox(w, h, d, col, x, y, z, matOpt) {
  const mesh = new THREE.Mesh(
    new THREE.BoxGeometry(w, h, d),
    MP(Object.assign({ color: col }, matOpt || {}))
  );
  mesh.position.set(x, y, z);
  mesh.castShadow = true;
  mesh.receiveShadow = true;
  return mesh;
}

// ==========================================
// 3D FLOATING ILLUMINATED WORKBENCH TITLE PLAQUE
// ==========================================
let lab3DTitlePlaque = null;

function create3DTitlePlaque() {
  const plaqueGroup = new THREE.Group();
  plaqueGroup.position.set(-PW / 2, 0.44, -1.62);
  plaqueGroup.rotation.x = -0.32; // Tilted towards user camera

  // Chrome mounting studs
  const stud1 = makeCyl(0.024, 0.024, 0.16, 0xd4d4d8, -0.88, -0.06, 0);
  const stud2 = makeCyl(0.024, 0.024, 0.16, 0xd4d4d8, 0.88, -0.06, 0);
  plaqueGroup.add(stud1);
  plaqueGroup.add(stud2);

  // Metallic Golden/Cyan Bezel
  const bezel = makeBox(2.08, 0.42, 0.035, 0x0284c7, 0, 0, -0.012, { shininess: 90 });
  plaqueGroup.add(bezel);

  // Obsidian Acrylic Slab
  const slab = makeBox(2.02, 0.38, 0.04, 0x071520, 0, 0, 0, { shininess: 100 });
  plaqueGroup.add(slab);

  // Canvas Texture for 3D Typography
  const c = document.createElement('canvas');
  c.width = 1024;
  c.height = 200;
  const ctx = c.getContext('2d');
  const tex = new THREE.CanvasTexture(c);
  tex.encoding = THREE.sRGBEncoding;

  const faceMat = MP({ map: tex, transparent: true, shininess: 80 });
  const faceMesh = new THREE.Mesh(new THREE.PlaneGeometry(1.98, 0.35), faceMat);
  faceMesh.position.set(0, 0, 0.024);
  plaqueGroup.add(faceMesh);

  plaqueGroup.updateTitle = function(expTitle) {
    ctx.clearRect(0, 0, 1024, 200);

    const g = ctx.createLinearGradient(0, 0, 1024, 0);
    g.addColorStop(0, 'rgba(8, 23, 36, 0.96)');
    g.addColorStop(0.5, 'rgba(14, 116, 144, 0.96)');
    g.addColorStop(1, 'rgba(8, 23, 36, 0.96)');
    ctx.fillStyle = g;
    ctx.beginPath();
    ctx.roundRect ? ctx.roundRect(10, 10, 1004, 180, 24) : ctx.rect(10, 10, 1004, 180);
    ctx.fill();

    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 4;
    ctx.stroke();

    ctx.strokeStyle = 'rgba(245, 158, 11, 0.8)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.roundRect ? ctx.roundRect(16, 16, 992, 168, 20) : ctx.rect(16, 16, 992, 168);
    ctx.stroke();

    ctx.fillStyle = '#f59e0b';
    ctx.fillRect(26, 95, 10, 10);
    ctx.fillRect(988, 95, 10, 10);

    ctx.font = 'bold 44px Tajawal, Tahoma, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    ctx.fillStyle = '#021827';
    ctx.fillText('⚗️ مَنَصَّةُ المَعْمَلِ الكِيمْيَائِيِّ التَّفَاعُلِيِّ', 514, 64);

    ctx.fillStyle = '#ffffff';
    ctx.fillText('⚗️ مَنَصَّةُ المَعْمَلِ الكِيمْيَائِيِّ التَّفَاعُلِيِّ', 512, 62);

    ctx.font = 'bold 26px Tajawal, Tahoma, sans-serif';
    ctx.fillStyle = '#fde047';
    ctx.fillText(expTitle ? `🧪 ${expTitle}` : 'كيمياء الصف الثالث الثانوي', 512, 132);

    tex.needsUpdate = true;
  };

  plaqueGroup.updateTitle('كيمياء الثالث الثانوي');
  bookGroup.add(plaqueGroup);
  return plaqueGroup;
}

// Initialize the 3D Title Plaque
lab3DTitlePlaque = create3DTitlePlaque();


function makeSphere(r, col, x, y, z, matOpt) {
  const mesh = new THREE.Mesh(
    new THREE.SphereGeometry(r, 16, 14),
    MP(Object.assign({ color: col }, matOpt || {}))
  );
  mesh.position.set(x, y, z);
  return mesh;
}

// 3D Text/Sprite Label
function make3DLabel(text, x, y, z, color = '#0e7490', scale = 1.0) {
  const c = document.createElement('canvas');
  c.width = 512;
  c.height = 128;
  const ctx = c.getContext('2d');
  const tex = new THREE.CanvasTexture(c);
  tex.encoding = THREE.sRGBEncoding;

  const sprite = new THREE.Sprite(new THREE.SpriteMaterial({ map: tex, transparent: true }));
  sprite.scale.set(2.4 * scale, 0.6 * scale, 1);
  sprite.position.set(x, y, z);

  sprite.setText = function(str) {
    ctx.clearRect(0, 0, 512, 128);
    if (!str) {
      tex.needsUpdate = true;
      return;
    }
    // Background pill
    ctx.fillStyle = 'rgba(255, 255, 255, 0.94)';
    ctx.strokeStyle = color;
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.roundRect ? ctx.roundRect(12, 16, 488, 96, 48) : ctx.rect(12, 16, 488, 96);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = color;
    ctx.font = 'bold 44px Tajawal, Tahoma, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(str, 256, 64);
    tex.needsUpdate = true;
  };

  sprite.setText(text);
  return sprite;
}

// Realistic Laboratory Beaker
function createBeaker({ radius = 0.8, height = 1.8, liquidColor = 0x38bdf8, liquidLevel = 0.6, pos = [0, 0, 0] }) {
  const grp = new THREE.Group();
  grp.position.set(...pos);

  // Outer glass cylinder
  const glass = new THREE.Mesh(
    new THREE.CylinderGeometry(radius, radius * 0.96, height, 32, 1, true),
    GLS
  );
  glass.position.y = height / 2;
  glass.castShadow = true;
  grp.add(glass);

  // Bottom glass plate
  const base = new THREE.Mesh(
    new THREE.CylinderGeometry(radius * 0.96, radius * 0.96, 0.06, 32),
    GLS
  );
  base.position.y = 0.03;
  grp.add(base);

  // Flared top rim lip
  const rim = new THREE.Mesh(
    new THREE.TorusGeometry(radius, 0.035, 12, 32),
    GLS
  );
  rim.rotation.x = Math.PI / 2;
  rim.position.y = height;
  grp.add(rim);

  // Liquid mesh
  const lqMat = MP({
    color: liquidColor,
    transparent: true,
    opacity: 0.76,
    shininess: 80
  });
  const liquid = new THREE.Mesh(
    new THREE.CylinderGeometry(radius * 0.94, radius * 0.92, 1, 32),
    lqMat
  );
  liquid.position.y = 0.5;
  grp.add(liquid);

  // Precipitate sediment mesh
  const pptMat = MP({
    color: 0x166534,
    transparent: true,
    opacity: 0.0
  });
  const ppt = new THREE.Mesh(
    new THREE.CylinderGeometry(radius * 0.93, radius * 0.91, 0.35, 32),
    pptMat
  );
  ppt.position.y = 0.2;
  grp.add(ppt);

  function setLevel(lvl) {
    const l = cl(lvl, 0.001, 0.96);
    liquid.scale.y = l * height;
    liquid.position.y = (l * height) / 2 + 0.03;
  }
  setLevel(liquidLevel);

  function setColor(col, dur = 0.0) {
    liquid.material.color.set(col);
  }

  function setPrecipitate(col, opacity = 1.0) {
    ppt.material.color.set(col);
    ppt.material.opacity = opacity;
  }

  return {
    root: grp,
    liquid,
    ppt,
    setLevel,
    setColor,
    setPrecipitate,
    radius,
    height
  };
}

// Realistic Laboratory Test Tube
function createTestTube({ radius = 0.38, height = 2.4, liquidColor = 0xa3e635, liquidLevel = 0.55, pos = [0, 0, 0] }) {
  const grp = new THREE.Group();
  grp.position.set(...pos);

  // Glass tube body
  const glass = new THREE.Mesh(
    new THREE.CylinderGeometry(radius, radius, height, 28, 1, true),
    GLS
  );
  glass.position.y = height / 2 + radius;
  grp.add(glass);

  // Hemisphere bottom
  const bottom = new THREE.Mesh(
    new THREE.SphereGeometry(radius, 28, 14, 0, Math.PI * 2, Math.PI / 2, Math.PI / 2),
    GLS
  );
  bottom.position.y = radius;
  bottom.rotation.x = Math.PI;
  grp.add(bottom);

  // Rim lip
  const rim = new THREE.Mesh(new THREE.TorusGeometry(radius, 0.03, 10, 28), GLS);
  rim.rotation.x = Math.PI / 2;
  rim.position.y = height + radius;
  grp.add(rim);

  // Liquid mesh
  const lqMat = MP({
    color: liquidColor,
    transparent: true,
    opacity: 0.78,
    shininess: 70
  });
  const liquid = new THREE.Mesh(
    new THREE.CylinderGeometry(radius * 0.92, radius * 0.92, 1, 28),
    lqMat
  );
  grp.add(liquid);

  // Precipitate mesh
  const pptMat = MP({ color: 0x475569, transparent: true, opacity: 0 });
  const ppt = new THREE.Mesh(new THREE.CylinderGeometry(radius * 0.91, radius * 0.91, 0.4, 28), pptMat);
  ppt.position.y = radius + 0.2;
  grp.add(ppt);

  function setLevel(lvl) {
    const l = cl(lvl, 0.001, 0.95);
    liquid.scale.y = l * height;
    liquid.position.y = radius + (l * height) / 2;
  }
  setLevel(liquidLevel);

  return {
    root: grp,
    liquid,
    ppt,
    setLevel,
    setColor: col => liquid.material.color.set(col),
    setPrecipitate: (col, op = 1.0) => {
      ppt.material.color.set(col);
      ppt.material.opacity = op;
    },
    radius,
    height
  };
}

// Wooden Test Tube Rack
function createTestTubeRack(tubeCount = 4, spacing = 0.9) {
  const grp = new THREE.Group();
  const width = tubeCount * spacing + 0.6;
  const woodMat = MP({ color: 0x9a6a3a, roughness: 0.7 });

  // Base
  const base = new THREE.Mesh(new THREE.BoxGeometry(width, 0.16, 1.2), woodMat);
  base.position.y = 0.08;
  base.castShadow = true;
  base.receiveShadow = true;
  grp.add(base);

  // Top plate with holes
  const top = new THREE.Mesh(new THREE.BoxGeometry(width, 0.14, 1.2), woodMat);
  top.position.y = 1.6;
  top.castShadow = true;
  grp.add(top);

  // Side pillars
  [-width / 2 + 0.15, width / 2 - 0.15].forEach(x => {
    const pillar = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 1.5, 16), woodMat);
    pillar.position.set(x, 0.85, 0);
    pillar.castShadow = true;
    grp.add(pillar);
  });

  return grp;
}

// Reagent Dropper Bottle (Draggable tool)
function createDropperBottle({ id, name, formula, liquidColor, bottleColor = 0xa16207, pos = [0, 0, 0], onDropOnTarget }) {
  const grp = new THREE.Group();
  grp.position.set(...pos);

  // Amber glass bottle body
  const bottle = new THREE.Mesh(
    new THREE.CylinderGeometry(0.36, 0.36, 1.1, 24),
    MP({ color: bottleColor, transparent: true, opacity: 0.82, shininess: 80 })
  );
  bottle.position.y = 0.55;
  bottle.castShadow = true;
  grp.add(bottle);

  // Bottle neck
  const neck = new THREE.Mesh(new THREE.CylinderGeometry(0.18, 0.22, 0.35, 20), MP({ color: bottleColor }));
  neck.position.y = 1.25;
  grp.add(neck);

  // Label
  const labelCanvas = document.createElement('canvas');
  labelCanvas.width = 256;
  labelCanvas.height = 128;
  const lx = labelCanvas.getContext('2d');
  lx.fillStyle = '#ffffff';
  lx.fillRect(0, 0, 256, 128);
  lx.fillStyle = '#0f172a';
  lx.font = 'bold 36px Tajawal, sans-serif';
  lx.textAlign = 'center';
  lx.fillText(formula, 128, 55);
  lx.font = '22px Tajawal, sans-serif';
  lx.fillStyle = '#0e7490';
  lx.fillText(name, 128, 95);
  const labelTex = new THREE.CanvasTexture(labelCanvas);
  labelTex.encoding = THREE.sRGBEncoding;

  const labelMesh = new THREE.Mesh(
    new THREE.CylinderGeometry(0.37, 0.37, 0.65, 24, 1, true, -Math.PI / 2, Math.PI),
    MP({ map: labelTex })
  );
  labelMesh.position.y = 0.55;
  grp.add(labelMesh);

  // Dropper Pipette with rubber bulb
  const pipetteGrp = new THREE.Group();
  pipetteGrp.position.set(0, 1.4, 0);
  const bulb = new THREE.Mesh(new THREE.SphereGeometry(0.18, 16, 12), MP({ color: 0xdc2626 }));
  bulb.position.y = 0.45;
  bulb.scale.set(1, 1.3, 1);
  pipetteGrp.add(bulb);

  const glassStem = new THREE.Mesh(new THREE.CylinderGeometry(0.045, 0.03, 1.1, 16), GLS);
  glassStem.position.y = -0.15;
  pipetteGrp.add(glassStem);

  // Liquid inside pipette tip
  const tipLiquid = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.025, 0.35, 16), MP({ color: liquidColor }));
  tipLiquid.position.y = -0.5;
  pipetteGrp.add(tipLiquid);

  grp.add(pipetteGrp);

  // Falling drop particle mesh (animated when dispensing)
  const dropMesh = new THREE.Mesh(
    new THREE.SphereGeometry(0.08, 12, 10),
    MP({ color: liquidColor, transparent: true, opacity: 0.9 })
  );
  dropMesh.visible = false;
  grp.add(dropMesh);

  const homePos = grp.position.clone();
  const homeRot = grp.rotation.clone();

  // Pouring Animation
  function dispenseDrops(targetPos, onComplete) {
    audio.playPour(0.7);
    let t = 0;
    const startPos = grp.position.clone();
    const pourPos = new THREE.Vector3(targetPos.x, targetPos.y + 1.6, targetPos.z);

    const animInterval = setInterval(() => {
      t += 0.05;
      if (t <= 1) {
        // Move towards target and tilt
        grp.position.lerpVectors(startPos, pourPos, t);
        grp.rotation.z = -0.6 * t;
      } else if (t <= 2) {
        // Drop falls
        dropMesh.visible = true;
        const dt = t - 1;
        dropMesh.position.set(0.4, 0.8 - dt * 1.6, 0);
        if (Math.random() < 0.3) audio.playBubble();
      } else if (t <= 3) {
        // Reset and return
        dropMesh.visible = false;
        const rt = t - 2;
        grp.position.lerpVectors(pourPos, homePos, rt);
        grp.rotation.z = -0.6 * (1 - rt);
      } else {
        clearInterval(animInterval);
        dropMesh.visible = false;
        grp.position.copy(homePos);
        grp.rotation.copy(homeRot);
        onComplete?.();
      }
    }, 25);
  }

  const draggableItem = {
    id,
    name: `${name} (${formula})`,
    formula,
    root: grp,
    hitMesh: bottle,
    homePos,
    homeRot,
    targets: [],
    dispenseDrops,
    onDropEmpty: () => {
      grp.position.copy(homePos);
      grp.rotation.copy(homeRot);
    }
  };

  DraggableManager.register(draggableItem);
  return draggableItem;
}

// Laboratory Thermometer with dynamic liquid column and 3D numeric badge
function createThermometer({ id = 'thermometer', pos = [0, 0, 0] }) {
  const grp = new THREE.Group();
  grp.position.set(...pos);

  // Clear glass stem
  const stem = new THREE.Mesh(new THREE.CylinderGeometry(0.06, 0.06, 3.2, 20), GLS);
  stem.position.y = 1.6;
  stem.castShadow = true;
  grp.add(stem);

  // Red alcohol bulb at bottom
  const bulb = new THREE.Mesh(new THREE.SphereGeometry(0.13, 20, 16), MP({ color: 0xdc2626 }));
  bulb.position.y = 0.12;
  grp.add(bulb);

  // Dynamic red mercury/alcohol capillary
  const capillary = new THREE.Mesh(
    new THREE.CylinderGeometry(0.035, 0.035, 1, 16),
    MP({ color: 0xdc2626 })
  );
  capillary.position.y = 0.8;
  grp.add(capillary);

  // Floating digital badge
  const tempBadge = make3DLabel('25.0 °C', 0, 3.5, 0, '#0e7490', 0.8);
  grp.add(tempBadge);

  let currentTemp = 25.0;
  function setTemp(targetT) {
    currentTemp = targetT;
    const norm = cl((currentTemp - 0) / 100, 0.08, 0.95);
    capillary.scale.y = norm * 2.8;
    capillary.position.y = 0.12 + (norm * 2.8) / 2;
    const col = currentTemp < 20 ? '#0284c7' : currentTemp > 40 ? '#dc2626' : '#0e7490';
    tempBadge.setText(`${currentTemp.toFixed(1)} °C`);
    $('#hudSensors').innerHTML = `<span class="sensor-badge">🌡️ درجة الحرارة: <b>${currentTemp.toFixed(1)} °C</b></span>`;
  }
  setTemp(25.0);

  const homePos = grp.position.clone();
  const draggableItem = {
    id,
    name: 'ميزان الحرارة',
    root: grp,
    hitMesh: stem,
    homePos,
    setTemp,
    getTemp: () => currentTemp,
    onDropEmpty: () => grp.position.copy(homePos)
  };

  DraggableManager.register(draggableItem);
  return draggableItem;
}

// Bunsen Burner with adjustable 3D flame and tripod
function createBunsenBurner({ id = 'burner', pos = [0, 0, 0], withTripod = true }) {
  const grp = new THREE.Group();
  grp.position.set(...pos);

  // Heavy cast iron base
  const base = new THREE.Mesh(new THREE.CylinderGeometry(0.65, 0.75, 0.14, 28), MP({ color: 0x334155, roughness: 0.8 }));
  base.position.y = 0.07;
  base.castShadow = true;
  grp.add(base);

  // Brass vertical barrel
  const barrel = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 1.2, 20), MP({ color: 0xd97706, metalness: 0.8, roughness: 0.3 }));
  barrel.position.y = 0.74;
  barrel.castShadow = true;
  grp.add(barrel);

  // Air collar ring
  const collar = new THREE.Mesh(new THREE.CylinderGeometry(0.15, 0.15, 0.22, 20), MP({ color: 0x78350f }));
  collar.position.y = 0.32;
  grp.add(collar);

  // Multi-layered 3D animated flame
  const flameGrp = new THREE.Group();
  flameGrp.position.set(0, 1.34, 0);

  // Inner cone (light cyan hot core)
  const innerFlame = new THREE.Mesh(
    new THREE.ConeGeometry(0.14, 0.6, 16),
    MP({ color: 0x67e8f9, emissive: 0x06b6d4, transparent: true, opacity: 0.85 })
  );
  innerFlame.position.y = 0.3;
  flameGrp.add(innerFlame);

  // Outer cone (blue / orange roaring flame)
  const outerFlame = new THREE.Mesh(
    new THREE.ConeGeometry(0.25, 1.1, 18),
    MP({ color: 0x38bdf8, emissive: 0x0284c7, transparent: true, opacity: 0.75 })
  );
  outerFlame.position.y = 0.55;
  flameGrp.add(outerFlame);

  flameGrp.visible = false;
  grp.add(flameGrp);

  // Tripod Stand and Wire Gauze
  let tripod = null;
  if (withTripod) {
    tripod = new THREE.Group();
    // 3 Metallic Legs
    for (let i = 0; i < 3; i++) {
      const angle = (i * Math.PI * 2) / 3;
      const leg = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 2.6, 12), MP({ color: 0x475569 }));
      leg.position.set(Math.cos(angle) * 0.95, 1.3, Math.sin(angle) * 0.95);
      leg.rotation.z = Math.cos(angle) * 0.15;
      leg.rotation.x = Math.sin(angle) * 0.15;
      leg.castShadow = true;
      tripod.add(leg);
    }
    // Top Ring
    const topRing = new THREE.Mesh(new THREE.TorusGeometry(1.05, 0.06, 12, 32), MP({ color: 0x475569 }));
    topRing.rotation.x = Math.PI / 2;
    topRing.position.y = 2.58;
    tripod.add(topRing);

    // Ceramic wire gauze mat
    const gauze = new THREE.Mesh(new THREE.BoxGeometry(2.1, 0.05, 2.1), MP({ color: 0xe2e8f0, roughness: 0.9 }));
    gauze.position.y = 2.62;
    gauze.receiveShadow = true;
    tripod.add(gauze);

    grp.add(tripod);
  }

  let isLit = false;
  function setLit(on) {
    isLit = on;
    flameGrp.visible = on;
    reactionLight.intensity = on ? 1.5 : 0;
    if (on) audio.playIgnite();
  }

  function updateFlame(t) {
    if (isLit) {
      const wobble = 1 + Math.sin(t * 18) * 0.08;
      outerFlame.scale.set(wobble, 1 + Math.sin(t * 22) * 0.12, wobble);
      reactionLight.intensity = 1.3 + Math.sin(t * 15) * 0.3;
    }
  }

  const homePos = grp.position.clone();
  const draggableItem = {
    id,
    name: 'موقد بنسن',
    root: grp,
    hitMesh: barrel,
    homePos,
    setLit,
    isLit: () => isLit,
    updateFlame,
    onDropEmpty: () => grp.position.copy(homePos)
  };

  DraggableManager.register(draggableItem);
  return draggableItem;
}

// Glass Stirring Rod
function createStirringRod({ id = 'stirRod', pos = [0, 0, 0] }) {
  const grp = new THREE.Group();
  grp.position.set(...pos);

  const rod = new THREE.Mesh(new THREE.CylinderGeometry(0.045, 0.045, 2.8, 16), GLS);
  rod.position.y = 1.4;
  rod.rotation.z = 0.15;
  rod.castShadow = true;
  grp.add(rod);

  const homePos = grp.position.clone();
  const draggableItem = {
    id,
    name: 'ساق تحريك زجاجية',
    root: grp,
    hitMesh: rod,
    homePos,
    onDropEmpty: () => grp.position.copy(homePos)
  };
  DraggableManager.register(draggableItem);
  return draggableItem;
}

// Spatula with solid powder/crystals
function createSpatula({ id, name, chemicalName, powderColor = 0xffffff, pos = [0, 0, 0] }) {
  const grp = new THREE.Group();
  grp.position.set(...pos);

  // Metallic spatula blade
  const blade = new THREE.Mesh(new THREE.BoxGeometry(0.24, 0.03, 1.4), MP({ color: 0x94a3b8, metalness: 0.8, roughness: 0.2 }));
  blade.position.set(0, 0.1, 0.7);
  grp.add(blade);

  // Wooden handle
  const handle = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.07, 1.2, 16), MP({ color: 0x78350f }));
  handle.rotation.x = Math.PI / 2;
  handle.position.set(0, 0.1, -0.6);
  grp.add(handle);

  // Solid chemical powder on blade
  const powder = new THREE.Mesh(new THREE.BoxGeometry(0.2, 0.06, 0.6), MP({ color: powderColor }));
  powder.position.set(0, 0.14, 0.85);
  grp.add(powder);

  const homePos = grp.position.clone();
  const draggableItem = {
    id,
    name: `ملعقة ${chemicalName}`,
    chemicalName,
    root: grp,
    hitMesh: blade,
    homePos,
    targets: [],
    emptyPowder: () => { powder.visible = false; },
    resetPowder: () => { powder.visible = true; },
    onDropEmpty: () => grp.position.copy(homePos)
  };
  DraggableManager.register(draggableItem);
  return draggableItem;
}

// Digital / Analog Laboratory Multimeter
function createVoltmeter({ id = 'voltmeter', pos = [0, 0, 0] }) {
  const grp = new THREE.Group();
  grp.position.set(...pos);

  // Enclosure
  const box = new THREE.Mesh(new THREE.BoxGeometry(1.6, 1.1, 0.9), MP({ color: 0x1e293b, roughness: 0.6 }));
  box.position.y = 0.55;
  box.castShadow = true;
  grp.add(box);

  // Dial face canvas
  const dialCanvas = document.createElement('canvas');
  dialCanvas.width = dialCanvas.height = 256;
  const dx = dialCanvas.getContext('2d');
  dx.fillStyle = '#f8fafc';
  dx.fillRect(0, 0, 256, 256);
  dx.strokeStyle = '#0f172a';
  dx.lineWidth = 4;
  dx.beginPath();
  dx.arc(128, 190, 90, Math.PI * 0.8, Math.PI * 0.2, false);
  dx.stroke();
  dx.fillStyle = '#7c3aed';
  dx.font = 'bold 34px Tajawal, monospace';
  dx.textAlign = 'center';
  dx.fillText('0.00 V', 128, 120);

  const dialTex = new THREE.CanvasTexture(dialCanvas);
  dialTex.encoding = THREE.sRGBEncoding;

  const dialMesh = new THREE.Mesh(new THREE.PlaneGeometry(1.3, 0.85), MP({ map: dialTex }));
  dialMesh.position.set(0, 0.62, 0.46);
  grp.add(dialMesh);

  // Needle mesh
  const needle = new THREE.Mesh(new THREE.BoxGeometry(0.04, 0.65, 0.02), MP({ color: 0xdc2626 }));
  needle.position.set(0, 0.55, 0.48);
  needle.rotation.z = 0.55;
  grp.add(needle);

  function setVoltage(volts) {
    const v = cl(volts, 0, 3.0);
    // swing needle from right to left
    needle.rotation.z = 0.55 - (v / 2.0) * 1.1;
    dx.fillStyle = '#f8fafc';
    dx.fillRect(40, 70, 176, 70);
    dx.fillStyle = '#7c3aed';
    dx.fillText(`${v.toFixed(2)} V`, 128, 120);
    dialTex.needsUpdate = true;
    $('#hudSensors').innerHTML = `<span class="sensor-badge">⚡ فرق الجهد: <b>${v.toFixed(2)} V</b></span>`;
  }
  setVoltage(0.00);

  return { root: grp, setVoltage };
}

// Particle Stream Generator (for electrons, bubbles, vapors)
function createParticleSwarm(count, color, size = 0.08) {
  const particles = [];
  for (let i = 0; i < count; i++) {
    const p = makeSphere(size, color, 0, -10, 0, { transparent: true, opacity: 0.85 });
    p.visible = false;
    labMasterGroup.add(p);
    particles.push({ mesh: p, offset: Math.random() });
  }
  return particles;
}

function resetCamera() {
  view(curViewMode || 'book');
  showToast('تمت إعادة ضبط زاوية الرؤية 🎯');
}


// ==========================================
// 5. THE 10 INTERACTIVE EXPERIMENTS
// ==========================================
const EXPERIMENTS = [
  // ----------------------------------------------------
  // EXPERIMENT 1: الكشف عن الحديد في أملاحه
  // ----------------------------------------------------
  {
    n: 'الكشف عن الحديد في أملاحه',
    u: 'الوحدة الأولى: العناصر الانتقالية',
    unitId: 1,
    p: [22, 23],
    st: [
      ['تجهيز الأنابيب', 'عندنا أنبوبتان: الأولى بها محلول حديد ثنائي (Fe²⁺) أخضر باهت، والثانية بها محلول حديد ثلاثي (Fe³⁺) أصفر مصفر.'],
      ['إضافة هيدروكسيد الصوديوم', 'أضف هيدروكسيد الصوديوم (NaOH) بالقطارة: يتكون في الأولى راسب أخضر باهت جيلاتيني Fe(OH)₂، وفي الثانية راسب بني محمر Fe(OH)₃.'],
      ['كاشف الثيوسيانات (KSCN)', 'أضف قطرات من ثيوسيانات البوتاسيوم (KSCN) إلى أنبوبة الحديد الثلاثي: يتحول المحلول فوراً إلى اللون الأحمر الدموي المميز!']
    ],
    setup: function() {
      // Rack & Tubes
      const rack = createTestTubeRack(3, 1.2);
      rack.position.set(-1.6, 0, 0);
      labMasterGroup.add(rack);

      const tubeFe2 = createTestTube({
        radius: 0.36, height: 2.5,
        liquidColor: 0x86efac, liquidLevel: 0.55,
        pos: [-2.2, 0.1, 0]
      });
      labMasterGroup.add(tubeFe2.root);

      const tubeFe3 = createTestTube({
        radius: 0.36, height: 2.5,
        liquidColor: 0xfde047, liquidLevel: 0.55,
        pos: [-1.0, 0.1, 0]
      });
      labMasterGroup.add(tubeFe3.root);

      // 3D Floating Labels
      const lblFe2 = make3DLabel('Fe²⁺ حديد ثنائي', -2.2, 3.2, 0, '#166534', 0.7);
      labMasterGroup.add(lblFe2);
      const lblFe3 = make3DLabel('Fe³⁺ حديد ثلاثي', -1.0, 3.2, 0, '#b45309', 0.7);
      labMasterGroup.add(lblFe3);

      // Droppers
      const dropNaOH = createDropperBottle({
        id: 'dropNaOH', name: 'هيدروكسيد الصوديوم', formula: 'NaOH',
        liquidColor: 0xe2e8f0, bottleColor: 0x475569,
        pos: [-3.4, 0, 0.8]
      });
      labMasterGroup.add(dropNaOH.root);

      const dropKSCN = createDropperBottle({
        id: 'dropKSCN', name: 'ثيوسيانات البوتاسيوم', formula: 'KSCN',
        liquidColor: 0xfee2e2, bottleColor: 0x991b1b,
        pos: [0.4, 0, 0.8]
      });
      labMasterGroup.add(dropKSCN.root);

      // Dropper Targets
      dropNaOH.targets = [
        {
          id: 'fe2', pos: tubeFe2.root.position, radius: 1.4,
          onDrop: () => {
            dropNaOH.dispenseDrops(tubeFe2.root.position, () => {
              tubeFe2.setPrecipitate(0x15803d, 0.95);
              tubeFe2.setLevel(0.68);
              audio.playSuccess();
              $('#hudEq').innerHTML = 'Fe²⁺ + 2OH⁻ → <b>Fe(OH)₂↓</b> (راسب أخضر باهت متسخ)';
              showToast('تكون راسب هيدروكسيد الحديد الثنائي الأخضر الباهت!');
            });
          }
        },
        {
          id: 'fe3', pos: tubeFe3.root.position, radius: 1.4,
          onDrop: () => {
            dropNaOH.dispenseDrops(tubeFe3.root.position, () => {
              tubeFe3.setPrecipitate(0x9a3412, 0.95);
              tubeFe3.setLevel(0.68);
              audio.playSuccess();
              $('#hudEq').innerHTML = 'Fe³⁺ + 3OH⁻ → <b>Fe(OH)₃↓</b> (راسب بني محمر جيلاتيني)';
              showToast('تكون راسب هيدروكسيد الحديد الثلاثي البني المحمر!');
            });
          }
        }
      ];

      dropKSCN.targets = [
        {
          id: 'fe3', pos: tubeFe3.root.position, radius: 1.4,
          onDrop: () => {
            dropKSCN.dispenseDrops(tubeFe3.root.position, () => {
              tubeFe3.setColor(0x880808);
              tubeFe3.setLevel(0.68);
              audio.playSuccess();
              $('#hudEq').innerHTML = 'Fe³⁺ + 3SCN⁻ → <b>[Fe(SCN)₃]</b> (لون أحمر دموي مميز)';
              showToast('ظهور اللون الأحمر الدموي المميز لأيون Fe³⁺!');
            });
          }
        }
      ];

      // Shelf chips
      renderShelf([
        { name: 'قطارة NaOH', icon: '💧', onClick: () => dropNaOH.targets[0].onDrop() },
        { name: 'قطارة KSCN', icon: '🩸', onClick: () => dropKSCN.targets[0].onDrop() },
        { name: 'أنبوبة Fe²⁺', icon: '🧪', onClick: () => showToast('محلول كبريتات الحديد الثنائي FeSO₄') },
        { name: 'أنبوبة Fe³⁺', icon: '🧪', onClick: () => showToast('محلول كلوريد الحديد الثلاثي FeCl₃') }
      ]);

      $('#hudEq').innerHTML = 'الكشف عن أملاح الحديد: Fe²⁺ و Fe³⁺';
      $('#hudHint').innerHTML = '👉 اسحب قطارة NaOH وأسقط قطرات في أنبوبة Fe²⁺ أو Fe³⁺';

      return {
        update: (dt, t) => {},
        stepAction: (stepIdx) => {
          if (stepIdx === 1) dropNaOH.targets[0].onDrop();
          if (stepIdx === 2) dropKSCN.targets[0].onDrop();
        }
      };
    }
  },

  // ----------------------------------------------------
  // EXPERIMENT 2: حرارة الذوبان (طارد وماص للحرارة)
  // ----------------------------------------------------
  {
    n: 'حرارة الذوبان (طارد وماص للحرارة)',
    u: 'الوحدة الثانية: الطاقة الحرارية المصاحبة لتغيرات المادة',
    unitId: 2,
    p: [33],
    st: [
      ['تجهيز الكأسين والميزان', 'عندنا كأسان بهما ماء نقي بدرجة حرارة الغرفة (25°C)، وميزان حرارة زجاجي وساق تحريك.'],
      ['ذوبان نترات الأمونيوم (ماص)', 'نضيف ملعقة من نترات الأمونيوم (NH₄NO₃) للكأس الأولى ونحرك: تنخفض درجة الحرارة إلى 12°C ويتكون صقيع على الكأس (ماص للحرارة ΔH > 0).'],
      ['ذوبان هيدروكسيد الصوديوم (طارد)', 'نضيف ملعقة من هيدروكسيد الصوديوم (NaOH) للكأس الثانية: ترتفع درجة الحرارة بسرعة إلى 68°C ويتصاعد بخار ماء (طارد للحرارة ΔH < 0).']
    ],
    setup: function() {
      const beaker1 = createBeaker({ radius: 0.85, height: 1.8, liquidColor: 0x93c5fd, liquidLevel: 0.6, pos: [-2.5, 0, 0] });
      labMasterGroup.add(beaker1.root);

      const beaker2 = createBeaker({ radius: 0.85, height: 1.8, liquidColor: 0x93c5fd, liquidLevel: 0.6, pos: [-0.6, 0, 0] });
      labMasterGroup.add(beaker2.root);

      const lblB1 = make3DLabel('كأس 1: NH₄NO₃', -2.5, 2.5, 0, '#0284c7', 0.7);
      labMasterGroup.add(lblB1);
      const lblB2 = make3DLabel('كأس 2: NaOH', -0.6, 2.5, 0, '#dc2626', 0.7);
      labMasterGroup.add(lblB2);

      // Frost particle mesh on beaker 1
      const frostMesh = new THREE.Mesh(
        new THREE.CylinderGeometry(0.88, 0.88, 1.2, 24, 1, true),
        MP({ color: 0xffffff, transparent: true, opacity: 0.0, roughness: 0.9 })
      );
      frostMesh.position.set(-2.5, 0.7, 0);
      labMasterGroup.add(frostMesh);

      // Steam vapor particles on beaker 2
      const steamSwarm = createParticleSwarm(14, 0xffffff, 0.09);

      // Thermometer
      const thermo = createThermometer({ id: 'thermo', pos: [-1.5, 0, 1.4] });
      labMasterGroup.add(thermo.root);

      // Spatulas
      const spatNH4 = createSpatula({ id: 'spatNH4', name: 'نترات الأمونيوم', chemicalName: 'NH₄NO₃', powderColor: 0xffffff, pos: [-3.8, 0, 0.8] });
      labMasterGroup.add(spatNH4.root);

      const spatNaOH = createSpatula({ id: 'spatNaOH', name: 'هيدروكسيد الصوديوم', chemicalName: 'NaOH', powderColor: 0xf1f5f9, pos: [0.8, 0, 0.8] });
      labMasterGroup.add(spatNaOH.root);

      // Stirring rod
      const rod = createStirringRod({ pos: [-1.6, 0, -1.2] });
      labMasterGroup.add(rod.root);

      let steamActive = false;

      spatNH4.targets = [{
        id: 'b1', pos: beaker1.root.position, radius: 1.5,
        onDrop: () => {
          spatNH4.emptyPowder();
          audio.playPour(0.6);
          thermo.root.position.set(-2.5, 0, 0);
          thermo.setTemp(12.0);
          frostMesh.material.opacity = 0.75;
          audio.playSuccess();
          $('#hudEq').innerHTML = 'NH₄NO₃(s) + H₂O → NH₄⁺ + NO₃⁻  (<b>ΔH = +25.7 kJ/mol ماص للحرارة ❄</b>)';
          showToast('انخفاض درجة الحرارة وتكون صقيع: تفاعل ماص للحرارة!');
        }
      }];

      spatNaOH.targets = [{
        id: 'b2', pos: beaker2.root.position, radius: 1.5,
        onDrop: () => {
          spatNaOH.emptyPowder();
          audio.playPour(0.6);
          thermo.root.position.set(-0.6, 0, 0);
          thermo.setTemp(68.5);
          steamActive = true;
          audio.playSuccess();
          $('#hudEq').innerHTML = 'NaOH(s) + H₂O → Na⁺ + OH⁻  (<b>ΔH = -44.5 kJ/mol طارد للحرارة 🔥</b>)';
          showToast('ارتفاع درجة الحرارة وتصاعد بخار الماء: تفاعل طارد للحرارة!');
        }
      }];

      renderShelf([
        { name: 'ملعقة NH₄NO₃', icon: '❄️', onClick: () => spatNH4.targets[0].onDrop() },
        { name: 'ملعقة NaOH', icon: '🔥', onClick: () => spatNaOH.targets[0].onDrop() },
        { name: 'ميزان الحرارة', icon: '🌡️', onClick: () => showToast(`قراءة الميزان الحالية: ${thermo.getTemp()} °C`) },
        { name: 'ساق التحريك', icon: '🥢', onClick: () => { audio.playBubble(); showToast('تم تحريك المحلول وتسريع الذوبان!'); } }
      ]);

      $('#hudEq').innerHTML = 'حرارة الذوبان: التفاعلات الماصة والطاردة للحرارة';
      $('#hudHint').innerHTML = '👉 اسحب ملعقة نترات الأمونيوم أو هيدروكسيد الصوديوم وأسقطها في الكأس';

      return {
        update: (dt, t) => {
          if (steamActive) {
            steamSwarm.forEach((p, i) => {
              p.mesh.visible = true;
              const progress = ((t * 0.8 + p.offset) % 1);
              p.mesh.position.set(-0.6 + Math.sin(progress * 8 + i) * 0.25, 1.8 + progress * 1.8, Math.cos(progress * 6 + i) * 0.25);
              p.mesh.material.opacity = (1 - progress) * 0.6;
            });
          }
        },
        stepAction: (stepIdx) => {
          if (stepIdx === 1) spatNH4.targets[0].onDrop();
          if (stepIdx === 2) spatNaOH.targets[0].onDrop();
        }
      };
    }
  },

  // ----------------------------------------------------
  // EXPERIMENT 3: تفاعل الأكسدة والاختزال التلقائي
  // ----------------------------------------------------
  {
    n: 'تفاعل الأكسدة والاختزال التلقائي',
    u: 'الوحدة الثالثة: الطاقة الكهربائية والأكسدة والاختزال',
    unitId: 3,
    p: [49, 50],
    st: [
      ['الشريحة والمحلول', 'معنا محلول كبريتات النحاس (CuSO₄) الأزرق النقي، وشريحة خارصين (Zn) فضية لامعة.'],
      ['غمس الشريحة في المحلول', 'اغمس شريحة الخارصين في المحلول: تتأكسد ذرات الخارصين وتذوب، بينما تختزل أيونات النحاس الزرقاء (Cu²⁺) وتترسب كطبقة إسفنجية بنية حمراء على الشريحة.'],
      ['اكتمال التفاعل', 'يبهت لون المحلول الأزرق تدريجياً حتى يصبح رائقاً عديم اللون، وتتغطى الشريحة بالكامل بطبقة سميكة من النحاس الأحمر.']
    ],
    setup: function() {
      const beaker = createBeaker({ radius: 1.1, height: 2.1, liquidColor: 0x0284c7, liquidLevel: 0.65, pos: [-1.6, 0, 0] });
      labMasterGroup.add(beaker.root);

      const lblB = make3DLabel('محلول CuSO₄ الأزرق', -1.6, 2.8, 0, '#0284c7', 0.8);
      labMasterGroup.add(lblB);

      // Silvery Zinc Strip (Draggable)
      const znGrp = new THREE.Group();
      znGrp.position.set(-3.2, 0, 0.8);
      const znMesh = new THREE.Mesh(
        new THREE.BoxGeometry(0.16, 2.6, 0.7),
        MP({ color: 0x94a3b8, metalness: 0.85, roughness: 0.3 })
      );
      znMesh.position.y = 1.3;
      znMesh.castShadow = true;
      znGrp.add(znMesh);

      // Reddish copper coating mesh
      const cuCoat = new THREE.Mesh(
        new THREE.BoxGeometry(0.18, 1.6, 0.72),
        MP({ color: 0xb45309, metalness: 0.6, roughness: 0.5, transparent: true, opacity: 0.0 })
      );
      cuCoat.position.y = 0.8;
      znGrp.add(cuCoat);

      labMasterGroup.add(znGrp);

      // Micro bubbles swarm
      const bubbles = createParticleSwarm(12, 0xffffff, 0.04);

      let reactionActive = false;
      let coatProgress = 0;

      const znItem = {
        id: 'stripZn', name: 'شريحة الخارصين (Zn)',
        root: znGrp, hitMesh: znMesh,
        homePos: znGrp.position.clone(),
        targets: [{
          id: 'beakerCu', pos: beaker.root.position, radius: 1.4,
          onDrop: () => {
            znGrp.position.set(-1.6, 0.2, 0);
            reactionActive = true;
            audio.playSuccess();
            $('#hudEq').innerHTML = 'Zn(s) + Cu²⁺(aq) → <b>Zn²⁺(aq) + Cu(s)↓</b>';
            showToast('بدء تفاعل الإحلال: ترسب النحاس وبهتان اللون الأزرق!');
          }
        }],
        onDropEmpty: () => znGrp.position.copy(znItem.homePos)
      };
      DraggableManager.register(znItem);

      renderShelf([
        { name: 'شريحة الخارصين Zn', icon: '🪙', onClick: () => znItem.targets[0].onDrop() },
        { name: 'كأس CuSO₄', icon: '🧪', onClick: () => showToast('محلول كبريتات النحاس الزرقاء') }
      ]);

      $('#hudEq').innerHTML = 'Zn + CuSO₄ → ZnSO₄ + Cu';
      $('#hudHint').innerHTML = '👉 اسحب شريحة الخارصين Zn واغمسها داخل كأس كبريتات النحاس';

      return {
        update: (dt, t) => {
          if (reactionActive) {
            coatProgress = Math.min(1, coatProgress + dt * 0.3);
            cuCoat.material.opacity = coatProgress * 0.95;
            // Fade blue liquid to clear ZnSO4
            const blueCol = new THREE.Color(0x0284c7);
            const clearCol = new THREE.Color(0xe0f2fe);
            beaker.setColor(blueCol.lerp(clearCol, coatProgress));

            bubbles.forEach((p, i) => {
              p.mesh.visible = coatProgress < 0.98;
              const prog = ((t * 0.9 + p.offset) % 1);
              p.mesh.position.set(-1.6 + (Math.sin(i * 4) * 0.3), 0.3 + prog * 1.3, (Math.cos(i * 3) * 0.3));
              p.mesh.material.opacity = (1 - prog) * 0.8;
            });
          }
        },
        stepAction: (stepIdx) => {
          if (stepIdx >= 1) znItem.targets[0].onDrop();
        }
      };
    }
  },

  // ----------------------------------------------------
  // EXPERIMENT 4: الخلية الجلفانية (خلية دانيال Zn / Cu)
  // ----------------------------------------------------
  {
    n: 'الخلية الجلفانية (خلية دانيال Zn / Cu)',
    u: 'الوحدة الثالثة: الطاقة الكهربائية والأكسدة والاختزال',
    unitId: 3,
    p: [51, 52],
    st: [
      ['تركيب نصفي الخلية', 'نصف خلية الخارصين: شريحة Zn في محلول ZnSO₄ (مصعد سالـب). نصف خلية النحاس: شريحة Cu في محلول CuSO₄ (مهبط موجب).'],
      ['وضع القنطرة الملحية', 'نضع القنطرة الملحية (أنبوبة U بها إلكتروليت) لمعادلة الشحنات الكهربائية بين الكأسين ومنع تراكم الأيونات.'],
      ['توصيل الفولتميتر وسريان التيار', 'عند غلق الدائرة، ينحرف مؤشر الفولتميتر إلى 1.10V، ويضيء المصباح، وتتدفق الإلكترونات عبر السلك الخارجي من الخارصين إلى النحاس.']
    ],
    setup: function() {
      // Beaker 1: ZnSO4 + Zn plate
      const beakerZn = createBeaker({ radius: 0.85, height: 1.8, liquidColor: 0xe2e8f0, liquidLevel: 0.65, pos: [-2.6, 0, 0] });
      labMasterGroup.add(beakerZn.root);
      const znPlate = makeBox(0.14, 2.4, 0.6, 0x94a3b8, -2.6, 1.2, 0, { metalness: 0.8 });
      labMasterGroup.add(znPlate);
      const lblZn = make3DLabel('Zn مصعد (−)', -2.6, 2.7, 0, '#475569', 0.7);
      labMasterGroup.add(lblZn);

      // Beaker 2: CuSO4 + Cu plate
      const beakerCu = createBeaker({ radius: 0.85, height: 1.8, liquidColor: 0x0284c7, liquidLevel: 0.65, pos: [-0.6, 0, 0] });
      labMasterGroup.add(beakerCu.root);
      const cuPlate = makeBox(0.14, 2.4, 0.6, 0xb45309, -0.6, 1.2, 0, { metalness: 0.8 });
      labMasterGroup.add(cuPlate);
      const lblCu = make3DLabel('Cu مهبط (+)', -0.6, 2.7, 0, '#b45309', 0.7);
      labMasterGroup.add(lblCu);

      // Salt Bridge U-Tube (Draggable)
      const bridgeGrp = new THREE.Group();
      bridgeGrp.position.set(-1.6, 0, 1.6);
      const bridgeCurve = new THREE.CatmullRomCurve3([
        new THREE.Vector3(-0.9, 0.6, 0),
        new THREE.Vector3(-0.9, 2.1, 0),
        new THREE.Vector3(0.9, 2.1, 0),
        new THREE.Vector3(0.9, 0.6, 0)
      ]);
      const bridgeTube = new THREE.Mesh(
        new THREE.TubeGeometry(bridgeCurve, 32, 0.12, 12, false),
        MP({ color: 0xfef08a, transparent: true, opacity: 0.65 })
      );
      bridgeGrp.add(bridgeTube);
      labMasterGroup.add(bridgeGrp);

      // Voltmeter with LED lamp
      const vMeter = createVoltmeter({ id: 'vm', pos: [-1.6, 0, -1.5] });
      labMasterGroup.add(vMeter.root);

      const lamp = new THREE.Mesh(new THREE.SphereGeometry(0.2, 16, 12), MP({ color: 0x475569 }));
      lamp.position.set(-1.6, 1.4, -1.5);
      labMasterGroup.add(lamp);

      // Connecting Wire
      const wireCurve = new THREE.CatmullRomCurve3([
        new THREE.Vector3(-2.6, 2.4, 0),
        new THREE.Vector3(-2.6, 3.2, -0.8),
        new THREE.Vector3(-1.6, 3.2, -1.5),
        new THREE.Vector3(-0.6, 3.2, -0.8),
        new THREE.Vector3(-0.6, 2.4, 0)
      ]);
      const wireMesh = new THREE.Mesh(new THREE.TubeGeometry(wireCurve, 32, 0.04, 10, false), MP({ color: 0xdc2626 }));
      labMasterGroup.add(wireMesh);

      // Golden electron particles
      const electrons = createParticleSwarm(12, 0xfacc15, 0.06);

      let circuitClosed = false;

      const bridgeItem = {
        id: 'saltBridge', name: 'القنطرة الملحية',
        root: bridgeGrp, hitMesh: bridgeTube,
        homePos: bridgeGrp.position.clone(),
        targets: [{
          id: 'cells', pos: new THREE.Vector3(-1.6, 0, 0), radius: 1.5,
          onDrop: () => {
            bridgeGrp.position.set(-1.6, 0, 0);
            circuitClosed = true;
            vMeter.setVoltage(1.10);
            lamp.material.emissive.setHex(0xfacc15);
            audio.playSuccess();
            $('#hudEq').innerHTML = 'E°cell = E°(Cu²⁺/Cu) − E°(Zn²⁺/Zn) = 0.34 − (−0.76) = <b>+1.10 V</b>';
            showToast('اكتملت الدائرة الكهربية: تدفق التيار وانحراف المؤشر إلى 1.10V!');
          }
        }],
        onDropEmpty: () => bridgeGrp.position.copy(bridgeItem.homePos)
      };
      DraggableManager.register(bridgeItem);

      renderShelf([
        { name: 'القنطرة الملحية', icon: '🌉', onClick: () => bridgeItem.targets[0].onDrop() },
        { name: 'الفولتميتر', icon: '⚡', onClick: () => showToast('مقياس الجهد: 1.10 V') },
        { name: 'لوح الخارصين', icon: '🪙', onClick: () => showToast('المصعد السالب: تحدث عنده الأكسدة') },
        { name: 'لوح النحاس', icon: '🪙', onClick: () => showToast('المهبط الموجب: تحدث عنده الاختزال') }
      ]);

      $('#hudEq').innerHTML = 'خلية دانيال الجلفانية القياسية: Zn | Zn²⁺ || Cu²⁺ | Cu';
      $('#hudHint').innerHTML = '👉 اسحب القنطرة الملحية وضعها بين الكأسين لغلق الدائرة الكهربية';

      return {
        update: (dt, t) => {
          if (circuitClosed) {
            electrons.forEach((p, i) => {
              p.mesh.visible = true;
              const prog = ((t * 0.45 + p.offset) % 1);
              p.mesh.position.copy(wireCurve.getPoint(prog));
            });
          }
        },
        stepAction: (stepIdx) => {
          if (stepIdx >= 1) bridgeItem.targets[0].onDrop();
        }
      };
    }
  },

  // ----------------------------------------------------
  // EXPERIMENT 5: فحص المركم الرصاصي (بطارية السيارة)
  // ----------------------------------------------------
  {
    n: 'فحص المركم الرصاصي (بطارية السيارة)',
    u: 'الوحدة الثالثة: الطاقة الكهربائية والأكسدة والاختزال',
    unitId: 3,
    p: [57, 58],
    st: [
      ['تركيب المركم الرصاصي', 'يتكون المركم من ألواح رصاص إسفنجي (Pb) كمصعد، وألواح ثاني أكسيد الرصاص (PbO₂) كمهبط، مغمورة في حمض كبريتيك مخفف (H₂SO₄).'],
      ['قياس الكثافة بالهيدروميتر', 'نسحب عينة من الحمض بالهيدروميتر: إذا كان المركم مشحوناً بالكامل تكون الكثافة بين 1.28 و 1.30 جم/سم³ والجهد 2.1V لكل خلية.'],
      ['التفريغ وإعادة الشحن', 'عند التفريغ يستهلك الحمض وتتحول الألواح إلى كبريتات الرصاص (PbSO₄) وتهبط الكثافة إلى 1.15 جم/سم³. وعند الشحن ينعكس التفاعل.']
    ],
    setup: function() {
      // Battery container
      const batteryBox = makeBox(2.8, 2.2, 1.8, 0x0f172a, -1.6, 1.1, 0, { transparent: true, opacity: 0.65 });
      labMasterGroup.add(batteryBox);

      // Pb plate (-)
      const pbPlate = makeBox(0.12, 1.8, 1.2, 0x64748b, -2.2, 1.1, 0);
      labMasterGroup.add(pbPlate);
      // PbO2 plate (+)
      const pbo2Plate = makeBox(0.12, 1.8, 1.2, 0x78350f, -1.0, 1.1, 0);
      labMasterGroup.add(pbo2Plate);

      // Acid liquid
      const acidMesh = makeBox(2.5, 1.4, 1.5, 0xbae6fd, -1.6, 0.75, 0, { transparent: true, opacity: 0.6 });
      labMasterGroup.add(acidMesh);

      // Hydrometer (Draggable)
      const hydroGrp = new THREE.Group();
      hydroGrp.position.set(-3.6, 0, 1.2);
      // Glass tube
      const hStem = new THREE.Mesh(new THREE.CylinderGeometry(0.16, 0.16, 2.4, 20), GLS);
      hStem.position.y = 1.2;
      hydroGrp.add(hStem);
      // Rubber suction bulb
      const hBulb = new THREE.Mesh(new THREE.SphereGeometry(0.3, 16, 12), MP({ color: 0xdc2626 }));
      hBulb.position.y = 2.5;
      hydroGrp.add(hBulb);
      // Internal float
      const hFloat = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 1.2, 16), MP({ color: 0x16a34a }));
      hFloat.position.y = 0.9;
      hydroGrp.add(hFloat);

      labMasterGroup.add(hydroGrp);

      const lblH = make3DLabel('1.28 g/cm³', -1.6, 3.2, 0, '#16a34a', 0.8);
      labMasterGroup.add(lblH);

      const hydroItem = {
        id: 'hydrometer', name: 'الهيدروميتر (مقياس الكثافة)',
        root: hydroGrp, hitMesh: hStem,
        homePos: hydroGrp.position.clone(),
        targets: [{
          id: 'battery', pos: new THREE.Vector3(-1.6, 0, 0), radius: 1.5,
          onDrop: () => {
            hydroGrp.position.set(-1.6, 0.6, 0);
            hFloat.position.y = 1.35; // float rises
            audio.playSuccess();
            $('#hudSensors').innerHTML = '<span class="sensor-badge">⚖️ كثافة الحمض: <b>1.28 g/cm³ (مشحون بالكامل)</b></span> <span class="sensor-badge">⚡ الجهد: <b>2.1 V</b></span>';
            showToast('تم قياس الكثافة: المركم مشحون بنسبة 100%!');
          }
        }],
        onDropEmpty: () => hydroGrp.position.copy(hydroItem.homePos)
      };
      DraggableManager.register(hydroItem);

      renderShelf([
        { name: 'الهيدروميتر', icon: '⚖️', onClick: () => hydroItem.targets[0].onDrop() },
        { name: 'فحص الجهد', icon: '⚡', onClick: () => showToast('جهد الخلية = 2.1 V') },
        { name: 'لوح Pb المصعد', icon: '⬛', onClick: () => showToast('رصاص إسفنجي Pb (-)') },
        { name: 'لوح PbO₂ المهبط', icon: '🟫', onClick: () => showToast('ثاني أكسيد الرصاص PbO₂ (+)') }
      ]);

      $('#hudEq').innerHTML = 'Pb + PbO₂ + 2H₂SO₄ ⇌ 2PbSO₄ + 2H₂O';
      $('#hudHint').innerHTML = '👉 اسحب الهيدروميتر واغطه في حمض المركم لقياس الكثافة';

      return {
        update: (dt, t) => {},
        stepAction: (stepIdx) => {
          if (stepIdx >= 1) hydroItem.targets[0].onDrop();
        }
      };
    }
  },

  // ----------------------------------------------------
  // EXPERIMENT 6: التحليل الكهربي للماء (جهاز هوفمان)
  // ----------------------------------------------------
  {
    n: 'التحليل الكهربي للماء (جهاز هوفمان)',
    u: 'الوحدة الثالثة: الطاقة الكهربائية والأكسدة والاختزال',
    unitId: 3,
    p: [61, 62],
    st: [
      ['تجهيز جهاز هوفمان', 'جهاز هوفمان مملوء بماء محمض بحمض الكبريتيك المخفف (لزيادة التوصيل الكهربي)، مع قطبين من البلاتين وصمامات علوية.'],
      ['إمرار التيار وتصاعد الغازين', 'عند تشغيل التيار الكهربي، يتصاعد غاز الهيدروجين (H₂) عند المهبط، وغاز الأكسجين (O₂) عند المصعد، بحيث يكون حجم H₂ ضعف حجم O₂ تماماً.'],
      ['الكشف عن الغازين', 'نفتح صمام الهيدروجين ونقرب شظية فيشتعل بفرقعة مميزة (Pop). ونقرب شظية متوهجة من صمام الأكسجين فتزداد توهجاً واشتعالاً.']
    ],
    setup: function() {
      const grp = new THREE.Group();
      grp.position.set(-1.6, 0, 0);

      // 3 Vertical Glass Tubes
      [-0.8, 0, 0.8].forEach((x, i) => {
        const tube = new THREE.Mesh(new THREE.CylinderGeometry(0.24, 0.24, 3.4, 24, 1, true), GLS);
        tube.position.set(x, 1.8, 0);
        grp.add(tube);
      });

      // Horizontal connecting bottom tube
      const cross = new THREE.Mesh(new THREE.CylinderGeometry(0.18, 0.18, 1.8, 20), GLS);
      cross.rotation.z = Math.PI / 2;
      cross.position.set(0, 0.5, 0);
      grp.add(cross);

      // Water columns in side tubes
      const waterH2 = new THREE.Mesh(new THREE.CylinderGeometry(0.22, 0.22, 1, 20), MP({ color: 0x60a5fa, transparent: true, opacity: 0.65 }));
      waterH2.position.set(-0.8, 1.8, 0);
      grp.add(waterH2);

      const waterO2 = new THREE.Mesh(new THREE.CylinderGeometry(0.22, 0.22, 1, 20), MP({ color: 0x60a5fa, transparent: true, opacity: 0.65 }));
      waterO2.position.set(0.8, 2.3, 0);
      grp.add(waterO2);

      // Labels
      const lblH2 = make3DLabel('مهبط (−) 2H₂', -0.8, 3.8, 0, '#2563eb', 0.7);
      grp.add(lblH2);
      const lblO2 = make3DLabel('مصعد (+) 1O₂', 0.8, 3.8, 0, '#dc2626', 0.7);
      grp.add(lblO2);

      labMasterGroup.add(grp);

      // Bubbles
      const h2Bubbles = createParticleSwarm(14, 0xffffff, 0.05);
      const o2Bubbles = createParticleSwarm(8, 0xffffff, 0.05);

      let isRunning = false;
      let gasVolume = 0;

      function togglePower() {
        isRunning = !isRunning;
        if (isRunning) {
          audio.playBubble();
          showToast('بدء التحليل الكهربائي للماء وتصاعد فقاعات الغازين!');
          $('#hudEq').innerHTML = '2H₂O(l) → <b>2H₂(g) [ضعف الحجم]</b> + <b>O₂(g)</b>';
        }
      }

      function testGas(type) {
        if (type === 'h2') {
          audio.playPop();
          showToast('💥 فرقعة مميزة (Pop): اشتعال غاز الهيدروجين!');
        } else {
          audio.playIgnite();
          showToast('🔥 ازدياد توهج الشظية: وجود غاز الأكسجين!');
        }
      }

      renderShelf([
        { name: 'تشغيل/إيقاف التيار', icon: '⚡', onClick: togglePower },
        { name: 'اختبار الهيدروجين H₂', icon: '💥', onClick: () => testGas('h2') },
        { name: 'اختبار الأكسجين O₂', icon: '🔥', onClick: () => testGas('o2') }
      ]);

      $('#hudEq').innerHTML = '2H₂O(l) → 2H₂(g) + O₂(g)  (نسبة الحجوم 2 : 1)';
      $('#hudHint').innerHTML = '👉 اضغط على زر تشغيل التيار لتشاهد انطلاق الغازين بنسبة 2 إلى 1';

      return {
        update: (dt, t) => {
          if (isRunning) {
            gasVolume = Math.min(1.5, gasVolume + dt * 0.15);
            // H2 drops twice as much as O2
            waterH2.scale.y = Math.max(0.1, 2.6 - gasVolume * 1.4);
            waterH2.position.y = 0.5 + waterH2.scale.y / 2;

            waterO2.scale.y = Math.max(0.1, 2.6 - gasVolume * 0.7);
            waterO2.position.y = 0.5 + waterO2.scale.y / 2;

            h2Bubbles.forEach((p, i) => {
              p.mesh.visible = true;
              const prog = ((t * 1.2 + p.offset) % 1);
              p.mesh.position.set(-2.4 + (Math.sin(i * 3) * 0.08), 0.5 + prog * 2.2, Math.cos(i * 2) * 0.08);
            });

            o2Bubbles.forEach((p, i) => {
              p.mesh.visible = true;
              const prog = ((t * 0.6 + p.offset) % 1);
              p.mesh.position.set(-0.8 + (Math.sin(i * 3) * 0.08), 0.5 + prog * 2.2, Math.cos(i * 2) * 0.08);
            });
          }
        },
        stepAction: (stepIdx) => {
          if (stepIdx === 1) togglePower();
          if (stepIdx === 2) testGas('h2');
        }
      };
    }
  },

  // ----------------------------------------------------
  // EXPERIMENT 7: الطلاء الكهربي بالفضة
  // ----------------------------------------------------
  {
    n: 'الطلاء الكهربي بالفضة',
    u: 'الوحدة الثالثة: الطاقة الكهربائية والأكسدة والاختزال',
    unitId: 3,
    p: [64, 65],
    st: [
      ['تركيب خلية الطلاء', 'نربط الملعقة النحاسية بالقطب السالب لتكون هي المهبط (−)، ولوح الفضة النقي بالقطب الموجب ليكون المصعد (+)، في محلول نترات الفضة (AgNO₃).'],
      ['إمرار التيار وهجرة أيونات الفضة', 'تتأكسد ذرات الفضة عند المصعد وتذوب كأيونات (Ag⁺)، ثم تهاجر نحو الملعقة لتختزل عليها وتترسب كطبقة فضية متماسكة.'],
      ['اكتمال الطلاء واكتساب البريق', 'تكتسي الملعقة النحاسية بطبقة براقة من الفضة اللامعة، ويقل وزن لوح الفضة بمقدار ما ترسب على الملعقة.']
    ],
    setup: function() {
      const bath = createBeaker({ radius: 1.2, height: 1.8, liquidColor: 0xe0f2fe, liquidLevel: 0.7, pos: [-1.6, 0, 0] });
      labMasterGroup.add(bath.root);

      // Silver plate (+ Anode)
      const agPlate = makeBox(0.16, 2.2, 0.7, 0xe2e8f0, -0.9, 1.2, 0, { metalness: 0.9, roughness: 0.1 });
      labMasterGroup.add(agPlate);
      const lblAg = make3DLabel('مصعد (+) لوح فضة', -0.9, 2.7, 0, '#475569', 0.7);
      labMasterGroup.add(lblAg);

      // Copper Spoon (- Cathode, Draggable)
      const spoonGrp = new THREE.Group();
      spoonGrp.position.set(-2.3, 1.2, 0);

      const spoonHandle = makeBox(0.08, 1.6, 0.12, 0xb45309, 0, 0.7, 0, { metalness: 0.8 });
      spoonGrp.add(spoonHandle);

      const spoonBowl = new THREE.Mesh(new THREE.SphereGeometry(0.35, 16, 12), MP({ color: 0xb45309, metalness: 0.8 }));
      spoonBowl.scale.set(0.7, 1.0, 0.35);
      spoonBowl.position.set(0, -0.1, 0);
      spoonGrp.add(spoonBowl);

      labMasterGroup.add(spoonGrp);

      const lblSpoon = make3DLabel('مهبط (−) ملعقة نحاس', -2.3, 2.7, 0, '#b45309', 0.7);
      labMasterGroup.add(lblSpoon);

      // Silver ions swarm
      const agIons = createParticleSwarm(10, 0xe2e8f0, 0.06);

      let platingActive = false;
      let plateProgress = 0;

      function startPlating() {
        platingActive = true;
        audio.playSuccess();
        $('#hudEq').innerHTML = 'المصعد: Ag → Ag⁺ + e⁻ | المهبط: <b>Ag⁺ + e⁻ → Ag(s) [طلاء فضة ناصع]</b>';
        showToast('بدء عملية الطلاء الكهربي بالفضة!');
      }

      renderShelf([
        { name: 'بدء الطلاء الكهربي', icon: '🥄', onClick: startPlating },
        { name: 'فحص لمعان الملعقة', icon: '✨', onClick: () => showToast(`نسبة اكتمال الطلاء: ${(plateProgress * 100).toFixed(0)}%`) }
      ]);

      $('#hudEq').innerHTML = 'الطلاء الكهربي: ترسب ذرات الفضة النقية على المهبط';
      $('#hudHint').innerHTML = '👉 اضغط على بدء الطلاء لملاحظة تحول الملعقة من النحاسي إلى الفضي اللامع';

      return {
        update: (dt, t) => {
          if (platingActive) {
            plateProgress = Math.min(1, plateProgress + dt * 0.25);
            const cuCol = new THREE.Color(0xb45309);
            const agCol = new THREE.Color(0xf1f5f9);
            const curCol = cuCol.lerp(agCol, plateProgress);
            spoonHandle.material.color.copy(curCol);
            spoonBowl.material.color.copy(curCol);
            spoonBowl.material.roughness = 0.1;

            agIons.forEach((p, i) => {
              p.mesh.visible = plateProgress < 0.98;
              const prog = ((t * 0.5 + p.offset) % 1);
              p.mesh.position.set(-0.9 - prog * 1.4, 0.6 + (Math.sin(i * 3) * 0.3), Math.cos(i * 2) * 0.2);
            });
          }
        },
        stepAction: (stepIdx) => {
          if (stepIdx >= 1) startPlating();
        }
      };
    }
  },

  // ----------------------------------------------------
  // EXPERIMENT 8: الكشف عن النشا والسكريات (اليود وفهلنج)
  // ----------------------------------------------------
  {
    n: 'الكشف عن النشا والسكريات (اليود وفهلنج)',
    u: 'الوحدة السادسة: الكيمياء الحيوية',
    unitId: 6,
    p: [113, 114],
    st: [
      ['تجهيز المحلولين والكواشف', 'الأنبوبة الأولى بها محلول النشا، والثانية بها محلول الجلوكوز (سكر مختزل). ومعنا كاشف اليود وكاشف فهلنج.'],
      ['كشف النشا باليود', 'نضيف قطرات من محلول اليود إلى أنبوبة النشا: يتحول المحلول فوراً إلى اللون الأزرق الداكن المسوّد المميز للنشا.'],
      ['كشف الجلوكوز بفهلنج والتسخين', 'نضيف كاشف فهلنج إلى الجلوكوز ونسخن على موقد بنسن: يتحول اللون من الأزرق إلى الأخضر ثم الأصفر ثم يتكون راسب أحمر طوبي (Cu₂O).']
    ],
    setup: function() {
      const rack = createTestTubeRack(2, 1.4);
      rack.position.set(-2.0, 0, 0);
      labMasterGroup.add(rack);

      const tubeStarch = createTestTube({ radius: 0.36, height: 2.4, liquidColor: 0xf8fafc, liquidLevel: 0.55, pos: [-2.6, 0.1, 0] });
      labMasterGroup.add(tubeStarch.root);
      const lblStarch = make3DLabel('محلول النشا', -2.6, 3.2, 0, '#475569', 0.7);
      labMasterGroup.add(lblStarch);

      const tubeGlucose = createTestTube({ radius: 0.36, height: 2.4, liquidColor: 0xe0f2fe, liquidLevel: 0.55, pos: [-1.4, 0.1, 0] });
      labMasterGroup.add(tubeGlucose.root);
      const lblGlucose = make3DLabel('محلول الجلوكوز', -1.4, 3.2, 0, '#0284c7', 0.7);
      labMasterGroup.add(lblGlucose);

      // Droppers
      const dropIodine = createDropperBottle({
        id: 'dropIodine', name: 'كاشف اليود', formula: 'I₂',
        liquidColor: 0x9a3412, bottleColor: 0x78350f, pos: [-3.8, 0, 0.8]
      });
      labMasterGroup.add(dropIodine.root);

      const dropFehling = createDropperBottle({
        id: 'dropFehling', name: 'كاشف فهلنج', formula: 'Fehling',
        liquidColor: 0x0284c7, bottleColor: 0x0369a1, pos: [-0.2, 0, 0.8]
      });
      labMasterGroup.add(dropFehling.root);

      // Bunsen Burner
      const burner = createBunsenBurner({ id: 'burner8', pos: [1.2, 0, 0], withTripod: false });
      labMasterGroup.add(burner.root);

      dropIodine.targets = [{
        id: 'starch', pos: tubeStarch.root.position, radius: 1.4,
        onDrop: () => {
          dropIodine.dispenseDrops(tubeStarch.root.position, () => {
            tubeStarch.setColor(0x0f172a); // dark blue black
            audio.playSuccess();
            $('#hudEq').innerHTML = 'نشا + يود (I₂) → <b>معقد أزرق داكن مسوّد مميز للنشا</b>';
            showToast('ظهور اللون الأزرق الداكن: إيجابي لوجود النشا!');
          });
        }
      }];

      dropFehling.targets = [{
        id: 'glucose', pos: tubeGlucose.root.position, radius: 1.4,
        onDrop: () => {
          dropFehling.dispenseDrops(tubeGlucose.root.position, () => {
            tubeGlucose.setColor(0x0ea5e9);
            burner.setLit(true);
            setTimeout(() => {
              tubeGlucose.setColor(0xd97706);
              setTimeout(() => {
                tubeGlucose.setPrecipitate(0xb91c1c, 0.95);
                audio.playSuccess();
                $('#hudEq').innerHTML = 'جلوكوز + فهلنج (تسخين) → <b>Cu₂O↓ (راسب أحمر طوبي/قرميدي)</b>';
                showToast('تكون راسب أحمر قرميدي: كشف فهلنج إيجابي للجلوكوز!');
              }, 1200);
            }, 1000);
          });
        }
      }];

      renderShelf([
        { name: 'كاشف اليود I₂', icon: '💧', onClick: () => dropIodine.targets[0].onDrop() },
        { name: 'كاشف فهلنج', icon: '🧪', onClick: () => dropFehling.targets[0].onDrop() },
        { name: 'موقد بنسن', icon: '🔥', onClick: () => burner.setLit(!burner.isLit()) }
      ]);

      $('#hudEq').innerHTML = 'كواشف السكريات: اليود للنشا وفهلنج للجلوكوز';
      $('#hudHint').innerHTML = '👉 أضف اليود للنشا لمشاهدة اللون الأزرق، وأضف فهلنج للجلوكوز وسخن';

      return {
        update: (dt, t) => {
          burner.updateFlame(t);
        },
        stepAction: (stepIdx) => {
          if (stepIdx === 1) dropIodine.targets[0].onDrop();
          if (stepIdx === 2) dropFehling.targets[0].onDrop();
        }
      };
    }
  },

  // ----------------------------------------------------
  // EXPERIMENT 9: تحضير الصابون في المعمل (التصبّن والتمليح)
  // ----------------------------------------------------
  {
    n: 'تحضير الصابون في المعمل (التصبّن)',
    u: 'الوحدة الثامنة: الصناعات الكيميائية',
    unitId: 8,
    p: [160, 161],
    st: [
      ['خلط الزيت والقلوي', 'نضع الزيت النباتي (الدهن) في الكأس ونضيف إليه محلول هيدروكسيد الصوديوم (NaOH 30%).'],
      ['التسخين والتحريك (التصبّن)', 'نشعل موقد بنسن ونحرك المزيج باستمرار بساق زجاجية حتى يحدث التصبن ويتكون خليط كريمي كثيف متجانس.'],
      ['التمليح وفصل الصابون', 'نضيف محلول ملح الطعام المركز (NaCl): تنخفض ذائبية الصابون وينفصل ويطفو ككتلة صلبة بيضاء نقية فوق الجلسرين.']
    ],
    setup: function() {
      const burner = createBunsenBurner({ id: 'burner9', pos: [-1.6, 0, 0], withTripod: true });
      labMasterGroup.add(burner.root);

      const beaker = createBeaker({ radius: 1.0, height: 1.9, liquidColor: 0xfacc15, liquidLevel: 0.55, pos: [-1.6, 2.7, 0] });
      labMasterGroup.add(beaker.root);

      // Reagent bottles
      const dropNaOH = createDropperBottle({ id: 'dropNaOH9', name: 'هيدروكسيد صوديوم', formula: 'NaOH', liquidColor: 0xe2e8f0, pos: [-3.6, 0, 0.8] });
      labMasterGroup.add(dropNaOH.root);

      const dropNaCl = createDropperBottle({ id: 'dropNaCl9', name: 'محلول الملح المركز', formula: 'NaCl', liquidColor: 0xf8fafc, bottleColor: 0x334155, pos: [0.4, 0, 0.8] });
      labMasterGroup.add(dropNaCl.root);

      const rod = createStirringRod({ pos: [-1.6, 2.8, 0] });
      labMasterGroup.add(rod.root);

      function doSaponification() {
        burner.setLit(true);
        audio.playBubble();
        setTimeout(() => {
          beaker.setColor(0xfef08a);
          showToast('عملية التصبن: تحلل الزيت وتكون الصابون والجلسرين!');
          $('#hudEq').innerHTML = 'دهن/زيت + 3NaOH → <b>صابون (أملاح الصوديوم للأحماض الدهنية) + جلسرين</b>';
        }, 1200);
      }

      function doSaltingOut() {
        audio.playPour(0.7);
        beaker.setPrecipitate(0xffffff, 0.95);
        audio.playSuccess();
        $('#hudEq').innerHTML = 'التمليح (Salting Out): إضافة NaCl تؤدي إلى <b>طفو الصابون الصلب وانفصاله</b>';
        showToast('انفصال الصابون النقي الصلب وطفوه على السطح!');
      }

      renderShelf([
        { name: 'إشعال الموقد والتصبن', icon: '🔥', onClick: doSaponification },
        { name: 'إضافة الملح (التمليح)', icon: '🧂', onClick: doSaltingOut },
        { name: 'ساق التحريك', icon: '🥢', onClick: () => showToast('تحريك المزيج وتسريع التفاعل') }
      ]);

      $('#hudEq').innerHTML = 'تحضير الصابون: تفاعل التصبن والتمليح بمحلول NaCl';
      $('#hudHint').innerHTML = '👉 أشعل الموقد لبدء التصبن، ثم أضف محلول الملح المركز لفصل الصابون';

      return {
        update: (dt, t) => {
          burner.updateFlame(t);
        },
        stepAction: (stepIdx) => {
          if (stepIdx === 1) doSaponification();
          if (stepIdx === 2) doSaltingOut();
        }
      };
    }
  },

  // ----------------------------------------------------
  // EXPERIMENT 10: التقطير التجزيئي للنفط الخام
  // ----------------------------------------------------
  {
    n: 'التقطير التجزيئي للنفط الخام',
    u: 'الوحدة السابعة: النفط والغاز الطبيعي',
    unitId: 7,
    p: [133, 134, 135],
    st: [
      ['تسخين النفط الخام في الفرن', 'يسخن النفط الخام في الفرن بدرجة حرارة تصل إلى 400°C فيتبخر بالكامل تقريباً ويدخل أسفل برج التقطير.'],
      ['صعود الأبخرة في برج التقطير', 'تصعد الأبخرة داخل البرج عبر صواني التكثف، فتبرد تدريجياً ويتكثف كل جزء عند درجة غليانه الخاصة.'],
      ['فصل المشتقات البترولية', 'يخرج الغاز الخفيف من قمة البرج، يليه البنزين (الجازولين)، ثم الكيروسين، ثم زيت الديزل، ويبقى الأسفلت كبقايا ثقيلة في القاع.']
    ],
    setup: function() {
      // Fractionating column body
      const tower = new THREE.Mesh(new THREE.CylinderGeometry(0.85, 0.85, 5.2, 32, 1, true), GLS);
      tower.position.set(-1.6, 2.7, 0);
      labMasterGroup.add(tower);

      // Bubble cap trays at 5 heights
      const trayHeights = [0.9, 1.8, 2.7, 3.6, 4.5];
      const trayColors = [0x1e293b, 0x78350f, 0xd97706, 0xfde047, 0xf8fafc];
      const fractionNames = ['أسفلت (>350°C)', 'ديزل (250-350°C)', 'كيروسين (180-250°C)', 'بنزين سيارات (40-100°C)', 'غازات بترولية (<20°C)'];

      trayHeights.forEach((h, idx) => {
        const tray = new THREE.Mesh(new THREE.CylinderGeometry(0.82, 0.82, 0.08, 28), MP({ color: trayColors[idx] }));
        tray.position.set(-1.6, h, 0);
        labMasterGroup.add(tray);

        // Side outlet tube and receiving flask
        const sideTube = makeCyl(0.06, 0.06, 0.9, 0x64748b, -0.7, h, 0);
        sideTube.rotation.z = Math.PI / 2;
        labMasterGroup.add(sideTube);

        const flask = createBeaker({ radius: 0.32, height: 0.65, liquidColor: trayColors[idx], liquidLevel: 0.6, pos: [-0.1, h - 0.2, 0] });
        labMasterGroup.add(flask.root);

        const lbl = make3DLabel(fractionNames[idx], 1.5, h, 0, '#0e7490', 0.65);
        labMasterGroup.add(lbl);
      });

      // Furnace at base
      const furnace = makeBox(1.6, 1.2, 1.4, 0x7f1d1d, -3.2, 0.6, 0);
      labMasterGroup.add(furnace);
      const burner = createBunsenBurner({ id: 'furnaceBurner', pos: [-3.2, 1.2, 0], withTripod: false });
      burner.setLit(true);
      labMasterGroup.add(burner.root);

      const vapors = createParticleSwarm(24, 0xfde047, 0.07);

      renderShelf([
        { name: 'بنزين السيارات C₅-C₁₀', icon: '⛽', onClick: () => showToast('البنزين: خفيف سريع الاشتعال يتكثف عند 40-100°C') },
        { name: 'الكيروسين C₁₀-C₁₆', icon: '✈️', onClick: () => showToast('الكيروسين: وقود الطائرات النفاثة يتكثف عند 180-250°C') },
        { name: 'زيت الديزل C₁₄-C₂₀', icon: '🚛', onClick: () => showToast('الديزل: وقود الشاحنات والمحركات الثقيلة') },
        { name: 'الأسفلت C₂₀+', icon: '🛣️', onClick: () => showToast('الأسفلت: بقايا ثقيلة تستخدم في تعبيد الطرق') }
      ]);

      $('#hudEq').innerHTML = 'فصل مكونات النفط الخام بالتقطير التجزيئي حسب اختلاف درجات الغليان';
      $('#hudHint').innerHTML = '👉 تفحص صواني التكثف وقوارير تجميع المشتقات البترولية المختلفة';

      return {
        update: (dt, t) => {
          burner.updateFlame(t);
          vapors.forEach((p, i) => {
            p.mesh.visible = true;
            const prog = ((t * 0.35 + p.offset) % 1);
            p.mesh.position.set(-1.6 + Math.sin(prog * 12 + i) * 0.3, 0.8 + prog * 4.2, Math.cos(prog * 10 + i) * 0.3);
          });
        },
        stepAction: (stepIdx) => {
          showToast(`عرض مرحلة: ${fractionNames[stepIdx * 2] || 'التقطير التجزيئي'}`);
        }
      };
    }
  }
];


// ==========================================
// 6. APPLICATION CONTROLLER & UI MANAGEMENT
// ==========================================
let curExp = 0;
let curStep = 0;
let curPgi = 0;
let activeExpObj = null;
let flipAnim = -1;
let flipDir = 1;
let nextExpIdx = 0;

// Scanned Textbook Pages Cache
const pageTextures = {};

function renderShelf(items) {
  const shelf = $('#labShelf');
  if (!shelf) return;
  shelf.innerHTML = items.map(item => `
    <div class="tool-chip" onclick="(${item.onClick.toString()})()">
      <span class="icon">${item.icon}</span>
      <span>${item.name}</span>
    </div>
  `).join('');
}

function updateScannedPage() {
  const exp = EXPERIMENTS[curExp];
  const pageNum = exp.p[curPgi];
  if (!pageTextures[pageNum] && PG[pageNum]) {
    const t = new THREE.TextureLoader().load(PG[pageNum]);
    t.encoding = THREE.sRGBEncoding;
    t.anisotropy = aniso;
    pageTextures[pageNum] = t;
  }
  if (pageTextures[pageNum]) {
    PR.material.map = pageTextures[pageNum];
    PR.material.needsUpdate = true;
  }
  $('#pg').textContent = `📄 صـ ${pageNum} (${curPgi + 1}/${exp.p.length})`;
}

function pgn() {
  const exp = EXPERIMENTS[curExp];
  curPgi = (curPgi + 1) % exp.p.length;
  updateScannedPage();
  audio.playClink();
}

function setStep(idx) {
  curStep = idx;
  const exp = EXPERIMENTS[curExp];
  const step = exp.st[curStep];

  // Update step buttons
  $$('.step-btn').forEach((btn, i) => {
    btn.classList.toggle('active', i === curStep);
  });

  $('#cap').innerHTML = `<b>${curStep + 1}. ${step[0]}:</b> ${step[1]}`;
  if (isNarrating) {
    say(step[1]);
  }
}

function buildStepButtons() {
  const exp = EXPERIMENTS[curExp];
  const container = $('#stp');
  if (!container) return;
  container.innerHTML = exp.st.map((s, i) => `
    <button class="step-btn ${i === 0 ? 'active' : ''}" onclick="setStep(${i})" title="${s[0]}">
      ${i + 1}
    </button>
  `).join('');
}

function autoStep() {
  if (activeExpObj && activeExpObj.stepAction) {
    activeExpObj.stepAction(curStep);
  }
}

function toggleFreeMode() {
  showToast('وضع التجربة الحرة مفعّل: يمكنك سحب أي مادة وخلطها بحرية!');
}

function resetExp() {
  loadExperiment(curExp);
  audio.playSuccess();
  showToast('تمت إعادة ترتيب المعمل والبدء من جديد');
}

function loadExperiment(idx) {
  curExp = idx;
  curStep = 0;
  curPgi = 0;

  // Clear existing apparatus
  while (labMasterGroup.children.length > 0) {
    const obj = labMasterGroup.children[0];
    labMasterGroup.remove(obj);
  }
  DraggableManager.clear();

  const exp = EXPERIMENTS[curExp];
  $('#expTitle').textContent = `${curExp + 1}. ${exp.n}`;
  $('#expUnit').textContent = exp.u;

  // Setup experiment 3D models
  activeExpObj = exp.setup();

  // Update UI and Textbook pages
  buildStepButtons();
  setStep(0);
  updateScannedPage();
  updateLeftPageText(exp);
}

// 3D Page Flip Navigation
function nav(d) {
  const target = curExp + d;
  if (target < 0 || target >= EXPERIMENTS.length || flipAnim >= 0) return;
  stopSpeak();
  tourActive = false;
  $('#tourb').textContent = '🎧 شرح كامل';

  nextExpIdx = target;
  flipDir = d;
  flipAnim = 0;
  audio.playClink();
}

function processPageFlip(dt) {
  if (flipAnim < 0) return;
  flipAnim += dt * 1.8;
  const curl = Math.sin(Math.min(flipAnim, 1) * Math.PI) * 1.35;
  if (flipDir > 0) {
    pivR.rotation.z = curl;
  } else {
    pivL.rotation.z = -curl;
  }

  // Switch scene halfway through flip
  if (flipAnim >= 0.5 && curExp !== nextExpIdx) {
    loadExperiment(nextExpIdx);
  }

  // Complete flip
  if (flipAnim >= 1.0) {
    pivR.rotation.z = 0;
    pivL.rotation.z = 0;
    flipAnim = -1;
  }
}

// ==========================================
// 7. SPEECH SYNTHESIS NARRATION
// ==========================================
let voicesList = [];
let isNarrating = true;
let tourActive = false;
let speechId = 0;

function loadVoices() {
  if (!('speechSynthesis' in window)) {
    $('#vnote').textContent = 'متصفحك لا يدعم الشرح الصوتي.';
    return;
  }
  voicesList = speechSynthesis.getVoices().filter(v => /^ar/i.test(v.lang)).sort((a, b) => {
    return (/ar-?YE/i.test(b.lang) - /ar-?YE/i.test(a.lang)) || (b.localService - a.localService);
  });
  const vs = $('#vs');
  if (vs) {
    vs.innerHTML = voicesList.map((v, i) => `
      <option value="${i}">${v.name} — ${v.lang}${v.localService ? ' (بدون إنترنت)' : ' (متصل)'}</option>
    `).join('');
  }
  const vnote = $('#vnote');
  if (vnote) {
    vnote.textContent = voicesList.length
      ? 'الشرح باللهجة اليمنية ومصمم لمنهاج الثالث الثانوي. اختر صوتاً محلياً ليعمل بدون إنترنت.'
      : 'لا يوجد صوت عربي مثبت على جهازك، يرجى تثبيت حزمة الصوت العربي من إعدادات الهاتف.';
  }
}
if ('speechSynthesis' in window) {
  speechSynthesis.onvoiceschanged = loadVoices;
}

function stopSpeak() {
  speechId++;
  if ('speechSynthesis' in window) speechSynthesis.cancel();
}

function say(text, onComplete) {
  const curId = ++speechId;
  if ('speechSynthesis' in window) speechSynthesis.cancel();
  const vIndex = +$('#vs')?.value || 0;
  const v = voicesList[vIndex];
  if (!v || !('speechSynthesis' in window)) {
    if (onComplete) setTimeout(() => { if (curId === speechId) onComplete(); }, Math.max(2000, text.length * 75));
    return;
  }
  const u = new SpeechSynthesisUtterance(text);
  u.voice = v;
  u.lang = v.lang;
  u.rate = +$('#rt')?.value || 0.9;
  u.onend = u.onerror = () => {
    if (curId === speechId && onComplete) onComplete();
  };
  speechSynthesis.speak(u);
}

function runTourStep(stepIdx) {
  if (!tourActive) return;
  setStep(stepIdx);
  autoStep();
  const exp = EXPERIMENTS[curExp];
  say(exp.st[stepIdx][1], () => {
    if (!tourActive) return;
    if (stepIdx < exp.st.length - 1) {
      setTimeout(() => runTourStep(stepIdx + 1), 700);
    } else {
      tourActive = false;
      $('#tourb').textContent = '🎧 شرح كامل';
      showToast('اكتمل الشرح الكامل للتجربة!');
    }
  });
}

function tour() {
  if (tourActive) {
    tourActive = false;
    stopSpeak();
    $('#tourb').textContent = '🎧 شرح كامل';
    return;
  }
  tourActive = true;
  $('#tourb').textContent = '⏹ إيقاف الشرح';
  runTourStep(0);
}

// ==========================================
// 8. MINISTERIAL QUIZZES & ASSESSMENTS
// ==========================================
const QUIZ_UNITS = [
  'العناصر الانتقالية',
  'الطاقة الحرارية المصاحبة لتغيرات المادة',
  'الطاقة الكهربائية وتفاعلات الأكسدة والاختزال',
  'الطاقة والتفاعلات النووية',
  'مركبات النيتروجين العضوية',
  'الكيمياء الحيوية',
  'النفط والغاز الطبيعي',
  'الصناعات الكيميائية',
  'كيمياء البيئة'
];

const ALL_QUESTIONS = [
  [1, 'العناصر الانتقالية الرئيسية هي عناصر الفئة:', ['s', 'p', 'd', 'f'], 2, 'تمتلئ فيها المستويات الفرعية d تدريجياً.'],
  [1, 'اللون الأحمر الدموي يظهر عند إضافة ثيوسيانات البوتاسيوم إلى أيونات:', ['Fe²⁺', 'Fe³⁺', 'Cu²⁺', 'Zn²⁺'], 1, 'هذا كشف نوعي مميز لأيون الحديد الثلاثي.'],
  [1, 'من أهم خواص العناصر الانتقالية في الجدول الدوري:', ['تكوّن مركبات ملوّنة', 'كلها غازات', 'لا تكوّن أيونات', 'كلها لا فلزات'], 0, 'مركباتها غالباً ملوّنة بسبب انتقال إلكترونات d وحالات تأكسدها متعددة.'],
  [2, 'التفاعل الطارد للحرارة تكون قيمة التغير في المحتوى الحراري ΔH فيه:', ['موجبة', 'سالبة', 'تساوي صفراً', 'لا يمكن قياسها'], 1, 'الطارد للحرارة يفقد طاقة حرارية للوسط فتكون ΔH سالبة.'],
  [2, 'حرارة التكوين القياسية لأي عنصر نقي في حالته القياسية تساوي:', ['صفراً', '+100 kJ', '−100 kJ', '1 kJ'], 0, 'اصطلاحاً بالاتفاق الدولي تساوي صفراً.'],
  [2, 'ينص قانون هس على أن حرارة التفاعل الكلية:', ['تعتمد على عدد الخطوات', 'لا تعتمد على مسار التفاعل بل على الحالتين الابتدائية والنهائية', 'تساوي دائماً صفراً', 'تزداد بمضاعفة الضغط'], 1, 'الحرارة دالة حالة تعتمد فقط على المتفاعلات والنواتج.'],
  [3, 'تحدث عملية الأكسدة في الخلية الجلفانية عند قطب:', ['المهبط (الكاثود)', 'المصعد (الأنود)', 'القنطرة الملحية', 'الفولتميتر'], 1, 'الأكسدة دائماً عند المصعد والاختزال عند المهبط.'],
  [3, 'في خلية دانيال (Zn / Cu) يكون الخارصين:', ['مهبطاً موجباً', 'مصعداً سالباً', 'قنطرة ملحية', 'إلكتروليتياً خاملاً'], 1, 'الخارصين أكثر نشاطاً فيتأكسد ويفقد الإلكترونات.'],
  [3, 'عند التحليل الكهربائي للماء تكون نسبة حجم الهيدروجين إلى الأكسجين:', ['1 : 1', '2 : 1', '1 : 2', '3 : 1'], 1, 'وفق المعادلة: 2H₂O → 2H₂ + O₂.'],
  [4, 'جسيم ألفا (α) المنبعث من الأنوية المشعة هو عبارة عن:', ['إلكترون سريع', 'نواة ذرة هيليوم ⁴₂He', 'بروتون منفرد', 'فوتون كهرومغناطيسي'], 1, 'يتكون من بروتونين ونيوترونين.'],
  [4, 'أشعة جاما (γ):', ['جسيمات موجبة', 'جسيمات سالبة', 'موجات كهرومغناطيسية عديمة الكتلة والشحنة', 'أنوية ذرات'], 2, 'إشعاع كهرومغناطيسي عالي الطاقة والنفاذية.'],
  [5, 'الصيغة العامة لمجموعة الأمين الأولي:', ['R–NH₂', 'R–COOH', 'R–OH', 'R–CHO'], 0, 'تتصل مجموعة NH₂ بمجموعة ألكيل.'],
  [5, 'الحمض الأميني يحتوي دائماً على مجموعتي:', ['أمين وكربوكسيل', 'هيدروكسيل وكربونيل', 'إستر وإيثر', 'ألكيل وهاليد'], 0, 'المجموعة الأمينية القاعدية NH₂ والكربوكسيلية الحمضية COOH.'],
  [6, 'الكاشف الذي يعطي لوناً أزرق داكناً مسوّداً مع النشا:', ['محلول فهلنج', 'محلول اليود', 'الفينولفثالين', 'كاشف بندكت'], 1, 'اليود هو الكاشف النوعي المميز للنشا.'],
  [6, 'الوحدة البنائية الأساسية لجزيئات البروتينات:', ['الجلوكوز', 'الأحماض الأمينية', 'الأحماض الدهنية', 'الجلسرين'], 1, 'ترتبط بروابط ببتيدية منتظمة.'],
  [7, 'تفصل مكونات النفط الخام في الصناعة بواسطة:', ['الترشيح البسيط', 'التقطير التجزيئي', 'التبلور', 'التسامي'], 1, 'بسبب التفاوت في درجات غليان الهيدروكربونات.'],
  [7, 'أي النواتج يخرج من قمة برج التقطير التجزيئي للنفط؟', ['الأسفلت الثقيل', 'الغازات البترولية الخفيفة', 'زيوت التشحيم', 'وقود الديزل'], 1, 'الأخف وزناً والأقل في درجات الغليان يصعد إلى أعلى البرج.'],
  [8, 'يُحضَّر الصابون في المختبر من خلال تفاعل:', ['الدهون والزيوت مع القلويات (التصبن)', 'الأحماض مع الفلزات', 'الماء مع الملح', 'الكحول مع الإيثر'], 0, 'عملية التصبن تعطي أملاح الأحماض الدهنية (الصابون) والجلسرين.'],
  [8, 'تضاف أملاح كلوريد الصوديوم NaCl في نهاية التصبن من أجل:', ['تلوين الصابون', 'ترسيب الصابون وفصله (التمليح)', 'إذابة الدهون', 'تبريد الوعاء'], 1, 'التمليح يقلل ذائبية الصابون فيطفو وينفصل.'],
  [9, 'الغاز الرئيسي المسبب لظاهرة الاحتباس الحراري:', ['ثاني أكسيد الكربون CO₂', 'غاز الأرجون', 'الهيليوم', 'النيتروجين الخامل'], 0, 'يحبس الأشعة تحت الحمراء في الغلاف الجوي.']
];

let activeQuizList = [];
let quizIdx = 0;
let quizScore = 0;
let quizAnswered = false;

function openQ() {
  stopSpeak();
  tourActive = false;
  $('#qz').hidden = false;
  showQuizMenu();
}

function closeQ() {
  $('#qz').hidden = true;
  stopSpeak();
}

function showQuizMenu() {
  $('#qb').innerHTML = `
    <h3 style="margin-top:0;color:#fff">📝 بنك الاختبارات والأسئلة الوزارية</h3>
    <p style="opacity:.9;font-size:13.5px;color:#fff">اختر وحدة دراسية للاختبار فيها، أو ابدأ الاختبار النهائي الشامل (15 سؤالاً عشوائياً):</p>
    <button class="qo" style="background:var(--acc);color:#fff!important" onclick="startQuiz(0)">🏆 الاختبار النهائي الشامل (15 سؤالاً)</button>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:6px;margin-top:10px">
      ${QUIZ_UNITS.map((unit, i) => `
        <button class="qo" style="color:#fff!important" onclick="startQuiz(${i + 1})">الوحدة ${i + 1}: ${unit}</button>
      `).join('')}
    </div>
  `;
}

function startQuiz(unitId) {
  if (unitId === 0) {
    activeQuizList = ALL_QUESTIONS.slice().sort(() => Math.random() - 0.5).slice(0, 15);
  } else {
    activeQuizList = ALL_QUESTIONS.filter(q => q[0] === unitId);
    if (!activeQuizList.length) activeQuizList = ALL_QUESTIONS.slice(0, 5);
  }
  activeQuizList.unitId = unitId;
  quizIdx = 0;
  quizScore = 0;
  renderQuestion();
}

function renderQuestion() {
  quizAnswered = false;
  if (quizIdx >= activeQuizList.length) {
    const pct = Math.round((quizScore / activeQuizList.length) * 100);
    audio.playSuccess();
    $('#qb').innerHTML = `
      <div style="text-align:center;padding:16px;color:#fff">
        <h2 style="color:var(--acc);margin:0">النتيجة: ${quizScore} من ${activeQuizList.length} (${pct}%)</h2>
        <p style="font-size:16px;font-weight:700;color:#fff">${pct >= 85 ? '🌟 ممتاز جداً! أداء بارع في الكيمياء!' : pct >= 65 ? '👍 جيد جداً! واصل المراجعة والتدريب.' : '📚 تحتاج لمزيد من المراجعة والتركيز على التجارب.'}</p>
        <button class="qo" style="background:var(--acc);color:#fff!important;margin:16px auto;max-width:260px" onclick="showQuizMenu()">العودة لقائمة الاختبارات</button>
      </div>
    `;
    return;
  }

  const q = activeQuizList[quizIdx];
  const options = q[2].map((opt, i) => [opt, i]).sort(() => Math.random() - 0.5);

  $('#qb').innerHTML = `
    <small style="color:var(--acc);font-weight:800">${activeQuizList.unitId ? 'الوحدة ' + activeQuizList.unitId : 'الاختبار الشامل'} · سؤال ${quizIdx + 1} من ${activeQuizList.length}</small>
    <h3 style="margin:8px 0 16px;color:#fff">${q[1]}</h3>
    ${options.map(opt => `
      <button class="qo" style="color:#fff!important" data-correct="${opt[1] === q[3] ? '1' : '0'}" onclick="handleAnswer(this)">${opt[0]}</button>
    `).join('')}
    <div id="quizExplain" style="margin-top:12px;color:#fff"></div>
  `;
}

function handleAnswer(btn) {
  if (quizAnswered) return;
  quizAnswered = true;
  const isOk = btn.dataset.correct === '1';
  if (isOk) {
    quizScore++;
    btn.classList.add('ok');
    audio.playSuccess();
  } else {
    btn.classList.add('no');
    $$('.qo[data-correct="1"]').forEach(b => b.classList.add('ok'));
    audio.playPop();
  }

  const q = activeQuizList[quizIdx];
  $('#quizExplain').innerHTML = `
    <div style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.2);border-radius:14px;padding:10px 14px;color:#fff">
      <p style="margin:0 0 8px;color:#fff"><b>${isOk ? 'إجابة صحيحة! ✅' : 'إجابة خاطئة ❌'}</b> ${q[4]}</p>
      <button class="qo" style="background:var(--acc);color:#fff!important;margin:0" onclick="quizIdx++;renderQuestion()">${quizIdx + 1 < activeQuizList.length ? 'السؤال التالي ⬅' : 'عرض النتيجة النهائية'}</button>
    </div>
  `;
}

// ==========================================
// 9. MAIN RENDERING ANIMATION LOOP
// ==========================================
let lastTime = performance.now();
let totalTime = 0;

function mainLoop(now) {
  const dt = Math.min((now - lastTime) / 1000, 0.05);
  lastTime = now;
  totalTime += dt;

  // Process 3D page flip
  processPageFlip(dt);

  // Update current experiment
  if (activeExpObj && activeExpObj.update) {
    activeExpObj.update(dt, totalTime);
  }

  // Smooth Camera Target & Position Interpolation (ultra-buttery two-finger pan & zoom)
  if (!camState.curTarget) camState.curTarget = camState.target.clone();
  camState.curTarget.lerp(camState.target, Math.min(1, dt * 9));

  if (autoOrbit) camState.orbitTheta += dt * 0.25;
  const phi = camState.orbitPhi;
  const theta = camState.orbitTheta;
  const r = camState.orbitRadius;

  camState.pos.set(
    camState.curTarget.x + r * Math.sin(phi) * Math.sin(theta),
    camState.curTarget.y + r * Math.cos(phi),
    camState.curTarget.z + r * Math.sin(phi) * Math.cos(theta)
  );

  cam.position.lerp(camState.pos, Math.min(1, dt * 8));
  cam.lookAt(camState.curTarget);

  R.render(S, cam);
  requestAnimationFrame(mainLoop);
}

// ==========================================
// 10. INITIALIZATION
// ==========================================
loadVoices();
loadExperiment(0);
requestAnimationFrame(mainLoop);

// Auto-fade touch hint after 6s
setTimeout(() => {
  const h = $('#touchHint');
  if (h) {
    h.style.opacity = '0';
    setTimeout(() => { if (h) h.style.display = 'none'; }, 600);
  }
}, 6000);