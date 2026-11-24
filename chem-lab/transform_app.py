import os, sys, re, json

with open('/mnt/sdcard/projects/teaching-app/chem-lab/src/raw_extracted_app.js', 'r', encoding='utf-8') as f:
    js_text = f.read()

# 1. Add id: 'exp-X' to each of the 10 experiments
for i in range(1, 11):
    pattern = rf'(//\s*EXPERIMENT\s+{i}:[^\n]*\n\s*//[^\n]*\n\s*\{{\s*\n\s*)n:'
    replacement = rf'\1id: "exp-{i}",\n    n:'
    js_text, count = re.subn(pattern, replacement, js_text)
    if count == 0:
        print(f'Warning: failed to add id to experiment {i}')
    else:
        print(f'✓ Added id: exp-{i}')

# 2. Replace renderShelf function
old_shelf = '''function renderShelf(items) {
  const shelf = $('#labShelf');
  if (!shelf) return;
  shelf.innerHTML = items.map(item => `
    <div class="tool-chip" onclick="(${item.onClick.toString()})()">
      <span class="icon">${item.icon}</span>
      <span>${item.name}</span>
    </div>
  `).join('');
}'''

new_shelf = '''function renderShelf(items) {
  const shelf = $('#labShelf');
  if (!shelf) return;
  shelf.innerHTML = '';
  if (!Array.isArray(items)) return;
  items.forEach(item => {
    const chip = document.createElement('div');
    chip.className = 'tool-chip';
    chip.innerHTML = '<span class="icon">' + item.icon + '</span><span>' + item.name + '</span>';
    chip.addEventListener('click', () => {
      if (typeof item.onClick === 'function') {
        item.onClick();
      }
    });
    shelf.appendChild(chip);
  });
}'''

if old_shelf in js_text:
    js_text = js_text.replace(old_shelf, new_shelf)
    print('✓ Replaced renderShelf with addEventListener')
else:
    print('Warning: old_shelf exact match not found!')

# 3. Add StorageManager and QualityManager and ThemeListener
helpers = '''
// ==========================================
// UTILITY: Fisher-Yates Shuffle
// ==========================================
function shuffle(array) {
  const arr = array.slice();
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// ==========================================
// STORAGE MANAGER (localStorage with safe try/catch)
// ==========================================
const StorageManager = {
  VERSION: '1.0',
  mem: {},
  _get(k) {
    try {
      const v = localStorage.getItem('chem_' + k);
      return v ? JSON.parse(v) : null;
    } catch (e) {
      return this.mem[k] || null;
    }
  },
  _set(k, val) {
    try {
      localStorage.setItem('chem_' + k, JSON.stringify(val));
    } catch (e) {}
    this.mem[k] = val;
  },
  init() {
    try {
      const v = this._get('storage_version');
      if (v !== this.VERSION) {
        this._set('storage_version', this.VERSION);
      }
    } catch (e) {}
  },
  saveProgress(expId, stepIdx) {
    this._set('progress', { expId, stepIdx, time: Date.now() });
  },
  getProgress() {
    return this._get('progress');
  },
  saveQuizResult(unitId, score, total) {
    const all = this._get('unit_results') || {};
    const prev = all[unitId] || { bestScore: 0, attempts: 0 };
    all[unitId] = {
      lastScore: score,
      bestScore: Math.max(prev.bestScore || 0, score),
      total: total,
      attempts: (prev.attempts || 0) + 1,
      lastDate: Date.now()
    };
    this._set('unit_results', all);
  },
  getUnitResult(unitId) {
    const all = this._get('unit_results') || {};
    return all[unitId] || null;
  },
  recordMistake(qId) {
    const list = this._get('wrong_questions') || [];
    if (!list.includes(qId)) {
      list.push(qId);
      this._set('wrong_questions', list);
    }
  },
  removeMistake(qId) {
    let list = this._get('wrong_questions') || [];
    list = list.filter(id => id !== qId);
    this._set('wrong_questions', list);
  },
  getMistakes() {
    return this._get('wrong_questions') || [];
  },
  saveAudioSettings(settings) {
    this._set('audio_settings', settings);
  },
  getAudioSettings() {
    return this._get('audio_settings');
  },
  setQualityMode(mode) {
    this._set('quality_mode', mode);
  },
  getQualityMode() {
    return this._get('quality_mode');
  }
};

// ==========================================
// PERFORMANCE & QUALITY MANAGER
// ==========================================
const QualityManager = {
  mode: 'high',
  fpsHistory: [],
  lastFrameTime: performance.now(),
  prompted: false,
  init() {
    const saved = StorageManager.getQualityMode();
    if (saved) {
      this.setMode(saved, false);
    } else {
      this.setMode('high', false);
    }
  },
  setMode(m, notify = true) {
    this.mode = m;
    StorageManager.setQualityMode(m);
    if (typeof R === 'undefined' || !R) return;
    if (m === 'low') {
      R.setPixelRatio(1.0);
      R.shadowMap.enabled = false;
    } else if (m === 'medium') {
      R.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.5));
      R.shadowMap.enabled = true;
      R.shadowMap.type = THREE.PCFShadowMap;
    } else {
      R.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2.0));
      R.shadowMap.enabled = true;
      R.shadowMap.type = THREE.PCFSoftShadowMap;
    }
    const btn = $('#qualityBtn');
    if (btn) {
      const labels = { low: '⚡ منخفض', medium: '⚡ متوسط', high: '⚡ عالٍ' };
      btn.textContent = labels[m] || '⚡ عالٍ';
    }
    if (notify) showToast('تم ضبط الجودة إلى: ' + (m === 'low' ? 'منخفض (أداء سريع)' : m === 'medium' ? 'متوسط' : 'عالٍ (أعلى دقة)'));
  },
  toggle() {
    const modes = ['high', 'medium', 'low'];
    const next = modes[(modes.indexOf(this.mode) + 1) % modes.length];
    this.setMode(next, true);
  },
  tick(now) {
    const dt = now - this.lastFrameTime;
    this.lastFrameTime = now;
    if (dt <= 0 || dt > 200) return;
    this.fpsHistory.push(dt);
    if (this.fpsHistory.length > 60) this.fpsHistory.shift();

    if (!this.prompted && this.fpsHistory.length >= 60 && this.mode !== 'low') {
      const avgDt = this.fpsHistory.reduce((a, b) => a + b, 0) / this.fpsHistory.length;
      if (avgDt > 35) {
        this.prompted = true;
        showToast('⚡ لزيادة سلاسة الرسوم على هذا الجهاز، يمكنك خفض الجودة من الزر العلوى');
      }
    }
  }
};
function toggleQualityMode() {
  QualityManager.toggle();
}

// Scene Background Theme Change Listener
const themeMedia = window.matchMedia('(prefers-color-scheme: dark)');
function updateThemeBackground(e) {
  const isDark = e ? e.matches : themeMedia.matches;
  if (typeof S !== 'undefined' && S) {
    S.background = new THREE.Color(isDark ? 0x14100c : 0xe9dcc8);
  }
}
themeMedia.addEventListener('change', updateThemeBackground);
'''

# Prepend PW, PH, and helpers to js_text
js_text = 'const PW = 2.83, PH = 4;\n' + helpers + '\n' + js_text

# 4. In setStep and loadExperiment, save progress
js_text = js_text.replace(
    'function setStep(idx) {\n  curStep = idx;\n  const exp = EXPERIMENTS[curExp];',
    'function setStep(idx) {\n  curStep = idx;\n  const exp = EXPERIMENTS[curExp];\n  StorageManager.saveProgress(exp.id || (\'exp-\' + (curExp + 1)), curStep);'
)

# 5. In mainLoop(now), call QualityManager.tick(now)
js_text = js_text.replace(
    'function mainLoop(now) {\n  const dt = Math.min((now - lastTime) / 1000, 0.05);',
    'function mainLoop(now) {\n  QualityManager.tick(now);\n  const dt = Math.min((now - lastTime) / 1000, 0.05);'
)

# 6. Replace old Quiz system with new enhanced theme-driven quiz system
quiz_start_pos = js_text.find('// 8. MINISTERIAL QUIZZES & ASSESSMENTS')
quiz_end_pos = js_text.find('// 9. MAIN RENDERING ANIMATION LOOP')

if quiz_start_pos != -1 and quiz_end_pos != -1:
    new_quiz_system = '''// 8. MINISTERIAL QUIZZES & ASSESSMENTS
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

let activeQuizList = [];
let quizIdx = 0;
let quizScore = 0;
let quizAnswered = false;

function getAllQuestions() {
  if (typeof QUESTIONS_DATA !== 'undefined' && QUESTIONS_DATA && QUESTIONS_DATA.questions) {
    return QUESTIONS_DATA.questions;
  }
  return [];
}

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
  const allQ = getAllQuestions();
  let unitsHtml = '';
  for (let i = 0; i < QUIZ_UNITS.length; i++) {
    const uId = i + 1;
    const unit = QUIZ_UNITS[i];
    const res = StorageManager.getUnitResult(uId);
    const count = allQ.filter(q => q.unitId === uId).length;
    let badge = '';
    if (res) {
      badge = '<span class="badge-unit-score">أفضل نتيجة: ' + res.bestScore + '/' + res.total + ' (' + Math.round((res.bestScore / res.total) * 100) + '%)</span>';
    } else if (count < 3) {
      badge = '<span class="badge-unit-score" style="background:rgba(234,179,8,0.2);color:#ca8a04">قيد الإضافة</span>';
    } else {
      badge = '<span class="badge-unit-score" style="opacity:0.75">لم يُختبر بعد</span>';
    }
    unitsHtml += '<button class="qo" onclick="startQuiz(' + uId + ')">' +
                 '<div><b>الوحدة ' + uId + ':</b> ' + unit + '</div>' +
                 badge + '</button>';
  }

  $('#qb').innerHTML = '<h3 style="margin-top:0;color:var(--fg)">📝 بنك الاختبارات والأسئلة الوزارية</h3>' +
    '<p style="opacity:.9;font-size:13.5px;color:var(--fg)">اختر وحدة دراسية للاختبار فيها، أو ابدأ الاختبار النهائي الشامل (15 سؤالاً عشوائياً):</p>' +
    '<button class="qo" style="background:var(--acc);color:#fff!important;text-align:center;font-size:15px;margin-bottom:12px" onclick="startQuiz(0)">🏆 الاختبار النهائي الشامل (15 سؤالاً)</button>' +
    '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:8px;margin-top:6px">' +
    unitsHtml +
    '</div>';
}

function startQuiz(unitId) {
  const allQ = getAllQuestions();
  if (unitId === 0) {
    activeQuizList = shuffle(allQ).slice(0, 15);
  } else {
    activeQuizList = allQ.filter(q => q.unitId === unitId);
    if (activeQuizList.length < 3) {
      $('#qb').innerHTML = '<div style="text-align:center;padding:28px 16px;">' +
        '<div style="font-size:42px;margin-bottom:12px">⏳</div>' +
        '<h3 style="margin:0 0 10px;color:var(--fg)">بنك الأسئلة قيد الإضافة</h3>' +
        '<p style="opacity:.85;font-size:14px;color:var(--fg);margin-bottom:20px;line-height:1.6">' +
        'يجري حالياً مراجعة واعتماد بنك الأسئلة الوزارية الخاص بوحدة: <b>' + QUIZ_UNITS[unitId - 1] + '</b>.<br>' +
        'سوف تتاح قريباً في التحديث القادم بإذن الله.' +
        '</p>' +
        '<button class="qo" style="background:var(--acc);color:#fff!important;margin:0 auto;max-width:240px;text-align:center" onclick="showQuizMenu()">العودة لقائمة الاختبارات</button>' +
        '</div>';
      return;
    }
    activeQuizList = shuffle(activeQuizList);
  }
  activeQuizList.unitId = unitId;
  quizIdx = 0;
  quizScore = 0;
  renderQuestion();
}

function startMistakesReview() {
  const allQ = getAllQuestions();
  const mistakeIds = StorageManager.getMistakes();
  activeQuizList = allQ.filter(q => mistakeIds.includes(q.id));
  if (activeQuizList.length === 0) {
    showToast('لا توجد أسئلة خاطئة مسجلة حالياً!');
    showQuizMenu();
    return;
  }
  activeQuizList = shuffle(activeQuizList);
  activeQuizList.unitId = 'review';
  quizIdx = 0;
  quizScore = 0;
  renderQuestion();
}

function renderQuestion() {
  quizAnswered = false;
  if (quizIdx >= activeQuizList.length) {
    const pct = Math.round((quizScore / activeQuizList.length) * 100);
    audio.playSuccess();

    if (activeQuizList.unitId && activeQuizList.unitId !== 'review') {
      StorageManager.saveQuizResult(activeQuizList.unitId, quizScore, activeQuizList.length);
    }

    const wrongCount = StorageManager.getMistakes().length;
    let reviewBtn = '';
    if (wrongCount > 0) {
      reviewBtn = '<button class="qo" style="background:var(--warning);color:#fff!important;margin:12px auto;max-width:260px;text-align:center" onclick="startMistakesReview()">' +
        '🔁 راجع أخطائي (' + wrongCount + ' سؤال)</button>';
    }

    $('#qb').innerHTML = '<div style="text-align:center;padding:16px;color:var(--fg)">' +
      '<h2 style="color:var(--acc);margin:0 0 10px">النتيجة: ' + quizScore + ' من ' + activeQuizList.length + ' (' + pct + '%)</h2>' +
      '<p style="font-size:15px;font-weight:700;color:var(--fg);margin-bottom:16px">' +
      (pct >= 85 ? '🌟 ممتاز جداً! أداء بارع في الكيمياء!' : pct >= 65 ? '👍 جيد جداً! واصل المراجعة والتدريب.' : '📚 تحتاج لمزيد من المراجعة والتركيز على التجارب.') +
      '</p>' +
      reviewBtn +
      '<button class="qo" style="background:var(--acc);color:#fff!important;margin:8px auto;max-width:260px;text-align:center" onclick="showQuizMenu()">العودة لقائمة الاختبارات</button>' +
      '</div>';
    return;
  }

  const q = activeQuizList[quizIdx];
  const options = shuffle(q.options.map((opt, i) => [opt, i]));

  const unitLabel = activeQuizList.unitId === 'review'
    ? 'مراجعة الأخطاء السابقة'
    : (activeQuizList.unitId ? 'الوحدة ' + activeQuizList.unitId : 'الاختبار الشامل');

  let optsHtml = '';
  options.forEach(opt => {
    optsHtml += '<button class="qo" data-correct="' + (opt[1] === q.answer ? '1' : '0') + '" onclick="handleAnswer(this)">' +
                opt[0] + '</button>';
  });

  $('#qb').innerHTML = '<small style="color:var(--acc);font-weight:800">' + unitLabel + ' · سؤال ' + (quizIdx + 1) + ' من ' + activeQuizList.length + '</small>' +
    '<h3 style="margin:8px 0 16px;color:var(--fg);line-height:1.5">' + q.q + '</h3>' +
    '<div class="q-opts">' + optsHtml + '</div>' +
    '<div id="quizExplain" style="margin-top:12px"></div>';
}

function handleAnswer(btn) {
  if (quizAnswered) return;
  quizAnswered = true;
  const isOk = btn.dataset.correct === '1';
  const q = activeQuizList[quizIdx];

  if (isOk) {
    quizScore++;
    btn.classList.add('ok');
    audio.playSuccess();
    StorageManager.removeMistake(q.id);
  } else {
    btn.classList.add('no');
    $$('.qo[data-correct="1"]').forEach(b => b.classList.add('ok'));
    audio.playPop();
    StorageManager.recordMistake(q.id);
  }

  let expReviewBtn = '';
  if (q.expId) {
    expReviewBtn = '<button class="qo" style="background:var(--acc-dark);color:#fff!important;margin-top:8px;text-align:center" onclick="reviewLinkedExp(&quot;' + q.expId + '&quot;, ' + (q.page || 'null') + ')">⚗️ راجع التجربة في المعمل والكتاب</button>';
  }

  $('#quizExplain').innerHTML = '<div class="quiz-explain-card">' +
    '<p style="margin:0 0 8px;color:var(--fg);line-height:1.5">' +
    '<b>' + (isOk ? 'إجابة صحيحة! ✅' : 'إجابة خاطئة ❌') + '</b> ' + q.explain +
    '</p>' +
    '<div style="display:flex;flex-direction:column;gap:6px">' +
    expReviewBtn +
    '<button class="qo" style="background:var(--acc);color:#fff!important;margin:0;text-align:center" onclick="quizIdx++;renderQuestion()">' +
    (quizIdx + 1 < activeQuizList.length ? 'السؤال التالي ⬅' : 'عرض النتيجة النهائية') +
    '</button>' +
    '</div></div>';
}

function reviewLinkedExp(expId, pageNum) {
  closeQ();
  const expIdx = EXPERIMENTS.findIndex(e => e.id === expId);
  if (expIdx !== -1) {
    loadExperiment(expIdx);
    if (pageNum && EXPERIMENTS[expIdx].p && EXPERIMENTS[expIdx].p.includes(pageNum)) {
      curPgi = EXPERIMENTS[expIdx].p.indexOf(pageNum);
      updateScannedPage();
    }
    view('lab');
    showToast('انتقلت إلى تجربة: ' + EXPERIMENTS[expIdx].n);
  }
}
'''
    js_text = js_text[:quiz_start_pos] + new_quiz_system + '\n\n' + js_text[quiz_end_pos:]
    print('✓ Injected new theme-driven quiz system with mistake review and experiment linking')
else:
    print('Warning: quiz markers not found!')

# 7. In initialization: initialize StorageManager, QualityManager, and restore progress
init_old = '''loadVoices();
loadExperiment(0);
requestAnimationFrame(mainLoop);'''

init_new = '''loadVoices();
StorageManager.init();
QualityManager.init();

// Restore saved progress if available
const savedProg = StorageManager.getProgress();
let initExpIdx = 0;
let initStepIdx = 0;
if (savedProg && savedProg.expId) {
  const foundIdx = EXPERIMENTS.findIndex(e => e.id === savedProg.expId);
  if (foundIdx !== -1) {
    initExpIdx = foundIdx;
    if (typeof savedProg.stepIdx === 'number' && savedProg.stepIdx < EXPERIMENTS[foundIdx].st.length) {
      initStepIdx = savedProg.stepIdx;
    }
  }
}

loadExperiment(initExpIdx);
if (initStepIdx > 0) {
  setStep(initStepIdx);
}
requestAnimationFrame(mainLoop);'''

if init_old in js_text:
    js_text = js_text.replace(init_old, init_new)
    print('✓ Injected Storage and Quality initialization')
else:
    print('Warning: init_old not found!')

out_app_path = '/mnt/sdcard/projects/teaching-app/chem-lab/src/app.js'
with open(out_app_path, 'w', encoding='utf-8') as f:
    f.write(js_text)

print(f'✓ Successfully generated {out_app_path} ({len(js_text)} chars)')
