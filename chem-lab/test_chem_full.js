const fs = require('fs');
const vm = require('vm');

console.log('=== STARTING AUTOMATED COMPREHENSIVE VERIFICATION SUITE ===');

// 1. Load standalone dist file
const distPath = '/mnt/sdcard/projects/teaching-app/chem-lab/dist/chem-lab-book.html';
const htmlContent = fs.readFileSync(distPath, 'utf-8');

// Extract scripts
const scriptMatches = [...htmlContent.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
console.log(`Found ${scriptMatches.length} script blocks in dist bundle.`);
if (scriptMatches.length < 2) throw new Error('Expected at least 2 script blocks (Three.js + App)');

const threeSource = scriptMatches[0];
const appSource = scriptMatches[1];

// 2. Setup mock browser DOM & WebGL environment
const makeMockEl = (tag = 'div') => {
  const listeners = {};
  const el = {
    tagName: tag.toUpperCase(),
    style: {},
    dataset: {},
    appendChild: (child) => {
      el.children.push(child);
      return child;
    },
    removeChild: (child) => {
      const idx = el.children.indexOf(child);
      if (idx !== -1) el.children.splice(idx, 1);
    },
    children: [],
    addEventListener: (type, fn) => {
      listeners[type] = listeners[type] || [];
      listeners[type].push(fn);
    },
    removeEventListener: (type, fn) => {
      if (listeners[type]) listeners[type] = listeners[type].filter(f => f !== fn);
    },
    click: () => {
      if (listeners['click']) listeners['click'].forEach(fn => fn({ target: el }));
    },
    get innerHTML() { return el._html || ''; },
    set innerHTML(val) {
      el._html = val;
      if (val === '') el.children = [];
    },
    textContent: '',
    hidden: false,
    className: '',
    classList: {
      add: (c) => { if (!el.className.includes(c)) el.className += ' ' + c; },
      remove: (c) => { el.className = el.className.replace(c, '').trim(); },
      toggle: (c, state) => {
        if (state) el.classList.add(c);
        else el.classList.remove(c);
      }
    },
    querySelector: (sel) => el.children[0] || makeMockEl(),
    querySelectorAll: (sel) => el.children,
    getContext: () => ({
      fillRect: () => {},
      strokeRect: () => {},
      clearRect: () => {},
      beginPath: () => {},
      closePath: () => {},
      moveTo: () => {},
      lineTo: () => {},
      bezierCurveTo: () => {},
      quadraticCurveTo: () => {},
      arc: () => {},
      ellipse: () => {},
      fill: () => {},
      stroke: () => {},
      clip: () => {},
      fillText: () => {},
      strokeText: () => {},
      drawImage: () => {},
      getImageData: () => ({ data: [] }),
      putImageData: () => {},
      measureText: () => ({ width: 100 }),
      createLinearGradient: () => ({ addColorStop: () => {} }),
      createRadialGradient: () => ({ addColorStop: () => {} }),
      roundRect: () => {},
      setLineDash: () => {},
      save: () => {},
      restore: () => {},
      translate: () => {},
      rotate: () => {},
      scale: () => {}
    })
  };
  return el;
};

const domStore = {};
function getOrCreateEl(id) {
  if (!domStore[id]) domStore[id] = makeMockEl();
  return domStore[id];
}

const mockLocalStorage = {
  store: {},
  getItem: (k) => mockLocalStorage.store[k] || null,
  setItem: (k, v) => { mockLocalStorage.store[k] = String(v); },
  removeItem: (k) => { delete mockLocalStorage.store[k]; },
  clear: () => { mockLocalStorage.store = {}; }
};

let currentTheme = 'light';
const mediaListeners = [];

const mockMatchMedia = (query) => ({
  matches: currentTheme === 'dark',
  media: query,
  addEventListener: (type, fn) => { if (type === 'change') mediaListeners.push(fn); },
  removeEventListener: (type, fn) => {}
});

global.window = {
  innerWidth: 1080,
  innerHeight: 1920,
  devicePixelRatio: 2,
  addEventListener: () => {},
  removeEventListener: () => {},
  matchMedia: mockMatchMedia,
  localStorage: mockLocalStorage,
  AudioContext: function() {
    return {
      sampleRate: 44100,
      currentTime: 0,
      destination: {},
      createBuffer: () => ({ getChannelData: () => new Float32Array(100) }),
      createBufferSource: () => ({ connect: () => {}, start: () => {}, stop: () => {}, buffer: null }),
      createGain: () => ({ connect: () => {}, gain: { setValueAtTime: () => {}, exponentialRampToValueAtTime: () => {} } }),
      createBiquadFilter: () => ({ connect: () => {}, type: '', frequency: { setValueAtTime: () => {} } }),
      createOscillator: () => ({ connect: () => {}, start: () => {}, stop: () => {}, frequency: { setValueAtTime: () => {} } })
    };
  },
  speechSynthesis: {
    speak: () => {},
    cancel: () => {},
    getVoices: () => []
  }
};
global.window.webkitAudioContext = global.window.AudioContext;
global.document = {
  getElementById: (id) => getOrCreateEl(id),
  querySelector: (sel) => {
    if (sel.startsWith('#')) return getOrCreateEl(sel.slice(1));
    return makeMockEl();
  },
  querySelectorAll: (sel) => [makeMockEl()],
  createElement: (tag) => makeMockEl(tag),
  createElementNS: (ns, tag) => makeMockEl(tag),
  documentElement: { style: {} }
};
global.Image = function() { return makeMockEl('img'); };
global.localStorage = mockLocalStorage;
global.matchMedia = mockMatchMedia;
global.innerWidth = 1080;
global.innerHeight = 1920;
global.devicePixelRatio = 2;
global.speechSynthesis = {
  onvoiceschanged: null,
  speak: () => {},
  cancel: () => {},
  getVoices: () => []
};
global.performance = { now: () => Date.now() };
global.requestAnimationFrame = () => {};

// 3. Load Three.js in VM
const sandbox = { ...global, console, setTimeout, clearTimeout, setInterval, clearInterval };
vm.createContext(sandbox);

vm.runInContext(threeSource, sandbox);
console.log('✓ Three.js loaded in sandbox. Version:', sandbox.THREE.REVISION);

// Mock WebGLRenderer inside sandbox
sandbox.THREE.WebGLRenderer = function() {
  return {
    setSize: () => {},
    setPixelRatio: () => {},
    render: () => {},
    outputEncoding: 0,
    capabilities: { getMaxAnisotropy: () => 16 },
    shadowMap: { enabled: true, type: 0 },
    domElement: makeMockEl('canvas')
  };
};

// 4. Load application script in VM
vm.runInContext(appSource, sandbox);
console.log('✓ Application script loaded into sandbox.');

const evalInVM = (code) => vm.runInContext(code, sandbox);

// 5. TEST: Verify QUESTIONS_DATA
console.log('\n--- TEST 1: Questions Data Schema ---');
const qData = evalInVM('QUESTIONS_DATA');
if (!qData || qData.schema_version !== '1.0') throw new Error('Invalid QUESTIONS_DATA schema_version');
if (!Array.isArray(qData.questions) || qData.questions.length !== 20) throw new Error('Expected 20 questions');

let linkedCount = 0;
qData.questions.forEach((q, idx) => {
  if (!q.id || !q.unitId || !q.q || !Array.isArray(q.options) || typeof q.answer !== 'number') {
    throw new Error(`Invalid question format at index ${idx}`);
  }
  if (q.reviewed !== false) throw new Error(`Question ${q.id} must have reviewed=false`);
  if (q.expId) linkedCount++;
});
console.log(`✓ Verified 20 questions successfully. ${linkedCount} questions linked to experiments.`);

// 6. TEST: Verify all 10 Experiments
console.log('\n--- TEST 2: All 10 3D Experiments ---');
const exps = evalInVM('EXPERIMENTS');
if (!Array.isArray(exps) || exps.length !== 10) throw new Error('Expected 10 experiments in EXPERIMENTS');

exps.forEach((exp, idx) => {
  if (exp.id !== `exp-${idx + 1}`) throw new Error(`Experiment ${idx + 1} has invalid id: ${exp.id}`);
  
  evalInVM(`loadExperiment(${idx})`);
  const activeObj = evalInVM('activeExpObj');
  if (!activeObj) throw new Error(`Experiment ${exp.id} (${exp.n}) failed to return activeExpObj`);
  
  // Test each step
  for (let s = 0; s < exp.st.length; s++) {
    evalInVM(`setStep(${s})`);
    if (activeObj.stepAction) {
      activeObj.stepAction(s);
    }
  }
  
  // Test update tick
  if (activeObj.update) {
    activeObj.update(0.016, 1.0);
  }
  console.log(`  ✓ [${exp.id}] ${exp.n}: Passed all ${exp.st.length} steps`);
});

// 7. TEST: StorageManager Persistence
console.log('\n--- TEST 3: StorageManager (localStorage with try/catch) ---');
const SM = evalInVM('StorageManager');
SM.init();
SM.saveProgress('exp-4', 2);
const prog = SM.getProgress();
if (!prog || prog.expId !== 'exp-4' || prog.stepIdx !== 2) throw new Error('saveProgress / getProgress failed');

SM.saveQuizResult(1, 3, 3);
SM.saveQuizResult(1, 2, 3); // second attempt
const u1Res = SM.getUnitResult(1);
if (!u1Res || u1Res.bestScore !== 3 || u1Res.lastScore !== 2 || u1Res.attempts !== 2) {
  throw new Error('saveQuizResult / getUnitResult tracking failed');
}

SM.recordMistake('chem-q1');
SM.recordMistake('chem-q3');
if (!SM.getMistakes().includes('chem-q1') || !SM.getMistakes().includes('chem-q3')) {
  throw new Error('recordMistake failed');
}

SM.removeMistake('chem-q1');
if (SM.getMistakes().includes('chem-q1') || !SM.getMistakes().includes('chem-q3')) {
  throw new Error('removeMistake failed');
}
console.log('✓ StorageManager all operations verified successfully.');

// 8. TEST: Quiz System, Mistake Review, and Sparse Unit Handling
console.log('\n--- TEST 4: Quiz System & Review Features ---');
// Test sparse unit handling (< 3 questions)
evalInVM('startQuiz(4)'); // Unit 4 has only 2 questions (Q10, Q11)
const qbEl = domStore['qb'];
if (!qbEl.innerHTML.includes('قيد الإضافة')) {
  throw new Error('Sparse unit did not display "قيد الإضافة" message');
}
console.log('  ✓ Units with < 3 questions properly show "بنك الأسئلة قيد الإضافة"');

// Test normal unit quiz
evalInVM('startQuiz(1)'); // Unit 1 has 3 questions (Q1, Q2, Q3)
if (evalInVM('activeQuizList').length !== 3) throw new Error('Expected 3 questions in Unit 1 quiz');

// Test answering
const q0 = evalInVM('activeQuizList')[0];
const mockBtn = makeMockEl();
mockBtn.dataset = { correct: '1' };
evalInVM('handleAnswer')(mockBtn);
if (evalInVM('quizScore') !== 1) throw new Error('Quiz score not incremented on correct answer');

// Test Review Mistakes flow
evalInVM('startMistakesReview()');
if (evalInVM('activeQuizList').length !== 1 || evalInVM('activeQuizList')[0].id !== 'chem-q3') {
  throw new Error('startMistakesReview failed to queue only wrong questions');
}
console.log('  ✓ Mistakes review flow verified.');

// 9. TEST: QualityManager
console.log('\n--- TEST 5: QualityManager Modes & Toggle ---');
const QM = evalInVM('QualityManager');
QM.setMode('low', false);
if (QM.mode !== 'low') throw new Error('QualityManager setMode low failed');
QM.setMode('medium', false);
if (QM.mode !== 'medium') throw new Error('QualityManager setMode medium failed');
QM.setMode('high', false);
if (QM.mode !== 'high') throw new Error('QualityManager setMode high failed');
console.log('✓ QualityManager modes verified.');

// 10. TEST: Theme change listener
console.log('\n--- TEST 6: Scene Background Theme Listener ---');
currentTheme = 'dark';
mediaListeners.forEach(fn => fn({ matches: true }));
const S = evalInVM('S');
const darkBg = S.background.getHexString();
if (darkBg !== '14100c') throw new Error(`Expected dark background 14100c, got: ${darkBg}`);

currentTheme = 'light';
mediaListeners.forEach(fn => fn({ matches: false }));
const lightBg = S.background.getHexString();
if (lightBg !== 'e9dcc8') throw new Error(`Expected light background e9dcc8, got: ${lightBg}`);
console.log('✓ Scene background dynamically switches between light (0xe9dcc8) and dark (0x14100c).');

// 11. TEST: renderShelf with addEventListener
console.log('\n--- TEST 7: renderShelf with addEventListener ---');
let shelfClicked = false;
evalInVM('renderShelf')([
  { icon: '🧪', name: 'أداة اختبار', onClick: () => { shelfClicked = true; } }
]);
const shelfEl = domStore['labShelf'];
if (shelfEl.children.length !== 1) throw new Error('renderShelf failed to create element');
shelfEl.children[0].click();
if (!shelfClicked) throw new Error('renderShelf addEventListener did not trigger click callback');
console.log('✓ renderShelf safely attaches click handler without string conversion.');

console.log('\n======================================================');
console.log('🎉 ALL 7 TEST SUITES PASSED FLAWLESSLY WITH 0 ERRORS!');
console.log('======================================================\n');
