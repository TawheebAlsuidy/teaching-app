#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Interactive Quran Engine (HTML Modals + JS) for Grade 12 Quran & Its Sciences Book.

Provides offline:
1. Mushaf Uthmani reader (Amiri Quran font) + non-destructive Tajweed coloring toggle + Waqf tooltips
2. Genuine human offline reciter audio player (Sheikh Mahmoud Khalil Al-Husary) with repeat x1/x3/x5 & speed control
3. Interactive Story & Scientific Visual Scenes (Ifk 6-step caravan trail + sequence drill,
   Nur Mishkah AI artwork, Istiizan home simulator, Cosmic Rain clouds, Ijaz, Makharij) + TTS narration
4. Interactive Taqwim (official 108 questions + model answers + 16 lesson MCQs) & Surah An-Nur Hifz tester
"""


QURAN_MODAL_HTML = r"""
<style id="quran-interactive-styles">
:root {
  --font-quran: 'Amiri Quran', 'Amiri', serif;
  --quran-emerald: #047857;
  --quran-emerald-deep: #064E3B;
  --quran-gold: #B45309;
  --quran-cream: #FFFDF7;
}
.quran-modal-backdrop {
  display: none; position: fixed; inset: 0; height: 100dvh; max-height: 100dvh;
  background: rgba(6, 30, 22, 0.78); backdrop-filter: blur(4px);
  z-index: 985; align-items: flex-end; justify-content: center; overflow: hidden;
}
.quran-modal-backdrop.open { display: flex; }
.quran-sheet {
  width: 100%; max-width: 720px; max-height: 92dvh;
  background: var(--quran-cream); color: #1E293B;
  border-top: 2px solid #D97706; border-radius: 26px 26px 0 0;
  display: flex; flex-direction: column; overflow: hidden;
  box-shadow: 0 -14px 48px rgba(0, 0, 0, 0.45);
}
.quran-sheet-head {
  padding: 12px 14px 10px; flex-shrink: 0;
  background: linear-gradient(135deg, #064E3B 0%, #047857 100%);
  color: #FFFBEB; display: flex; align-items: center; gap: 10px; justify-content: space-between;
}
.quran-sheet-body {
  flex: 1 1 auto; overflow-y: auto; -webkit-overflow-scrolling: touch;
  padding: 14px 14px calc(22px + env(safe-area-inset-bottom, 0px));
}
.quran-tabs-row {
  display: flex; gap: 6px; padding: 8px 12px; background: #ECFDF5;
  border-bottom: 1px solid #A7F3D0; overflow-x: auto; flex-shrink: 0;
}
.q-tab-btn {
  border: 1px solid #6EE7B7; background: #fff; color: #065F46; border-radius: 999px;
  padding: 7px 13px; font-size: 12.5px; font-weight: 800; cursor: pointer;
  white-space: nowrap; font-family: 'Cairo', 'Tajawal', sans-serif;
}
.q-tab-btn.active { background: #047857; color: #fff; border-color: #047857; }
.mushaf-frame {
  background: linear-gradient(180deg, #FFFDF5 0%, #FEF9EB 100%);
  border: 2px solid #D97706; border-radius: 18px; padding: 14px 14px 16px;
  box-shadow: inset 0 0 0 4px #FFFDF7, inset 0 0 0 5px rgba(180, 83, 9, 0.25);
  margin-bottom: 12px;
}
.mushaf-basmala {
  font-family: var(--font-quran); text-align: center; font-size: 21px;
  color: #064E3B; margin-bottom: 10px; line-height: 2;
}
.ayah-card {
  background: rgba(255, 255, 255, 0.85); border: 1px solid rgba(180, 83, 9, 0.2);
  border-radius: 14px; padding: 11px 12px; margin-bottom: 9px;
  transition: border-color 0.2s, box-shadow 0.2s, background 0.2s;
}
.ayah-card.playing {
  background: #FFFBEB; border-color: #D97706;
  box-shadow: 0 4px 16px rgba(217, 119, 6, 0.22);
}
.ayah-text-uthmani {
  font-family: var(--font-quran); font-size: 21px; line-height: 2.15;
  color: #111827; text-align: right; word-spacing: 2px;
}
.ayah-num-badge {
  display: inline-flex; align-items: center; justify-content: center;
  min-width: 28px; height: 28px; padding: 0 6px; border-radius: 999px;
  background: #FEF3C7; border: 1.5px solid #D97706; color: #92400E;
  font-size: 13px; font-weight: 800; margin: 0 4px; font-family: 'Amiri', serif;
}
.tajweed-on .tj-qalqalah { color: #DC2626; font-weight: 700; }
.tajweed-on .tj-ghunnah { color: #059669; font-weight: 700; }
.tajweed-on .tj-madd { color: #2563EB; font-weight: 700; }
.tj-waqf { color: #B45309; cursor: pointer; font-weight: 800; padding: 0 2px; }
.reciter-bar {
  background: #064E3B; color: #ECFDF5; border-radius: 14px; padding: 10px 12px;
  margin-bottom: 12px; display: flex; flex-wrap: wrap; align-items: center;
  gap: 8px; justify-content: space-between;
}
.reciter-btn {
  background: #10B981; color: #fff; border: none; border-radius: 999px;
  padding: 7px 14px; font-size: 12.5px; font-weight: 800; cursor: pointer;
  font-family: 'Cairo', 'Tajawal', sans-serif;
}
.reciter-chip {
  background: rgba(255, 255, 255, 0.14); color: #ECFDF5; border: 1px solid rgba(255, 255, 255, 0.28);
  border-radius: 999px; padding: 4px 10px; font-size: 11.5px; font-weight: 700; cursor: pointer;
}
.reciter-chip.active { background: #F59E0B; color: #1E293B; border-color: #FDE68A; }
.vocab-item-card {
  background: #FFFFFF; border-right: 4px solid #047857; border-radius: 12px;
  padding: 10px 12px; margin-bottom: 8px; box-shadow: 0 1px 4px rgba(0, 0, 0, 0.05);
}
.quran-badge-official {
  display: inline-block; background: #ECFDF5; color: #065F46; border: 1px solid #6EE7B7;
  border-radius: 999px; padding: 2px 9px; font-size: 11px; font-weight: 800;
}
.quran-badge-edu {
  display: inline-block; background: #FFFBEB; color: #92400E; border: 1px solid #FCD34D;
  border-radius: 999px; padding: 2px 9px; font-size: 11px; font-weight: 800;
}
.q-taqwim-card {
  background: #fff; border: 1px solid #E2E8F0; border-radius: 14px;
  padding: 12px; margin-bottom: 10px; box-shadow: 0 1px 5px rgba(0, 0, 0, 0.04);
}
.q-scene-stage {
  background: linear-gradient(180deg, #06281E 0%, #091E18 100%);
  border-radius: 16px; border: 1.5px solid #D97706; padding: 10px;
  margin-bottom: 12px; text-align: center; color: #FFFBEB; overflow: hidden;
}
.q-timeline-step {
  background: #FFFFFF; border: 1px solid #D1FAE5; border-right: 4px solid #059669;
  border-radius: 12px; padding: 10px 12px; margin-bottom: 8px;
}
.hotspot-box {
  border-width: 1.5px; justify-content: center; align-items: center; padding: 2px;
}
.hotspot-pill {
  font-size: 9.5px; padding: 3px 8px; white-space: nowrap;
}
@media (max-width: 480px) {
  .ayah-text-uthmani { font-size: 19px; line-height: 2.05; }
  .quran-sheet-head h3, .quran-sheet-head #qModalTitle { font-size: 14.5px; }
  .hotspot-pill { font-size: 9px; padding: 2px 6px; }
}
</style>

<!-- 1. QURAN MUSHAF, RECITER AUDIO & EXPLANATION MODAL -->
<div id="quranReaderModal" class="quran-modal-backdrop" onclick="if(event.target===this) closeQuranModal('quranReaderModal')">
  <div class="quran-sheet">
    <div class="quran-sheet-head">
      <div style="min-width:0; flex:1;">
        <div id="qModalTitle" style="font-size:15.5px; font-weight:800; line-height:1.35;">القرآن الكريم وعلومه</div>
        <div id="qModalSub" style="font-size:11.5px; color:#A7F3D0; margin-top:2px;">الشيخ محمود خليل الحصري · نص Tanzil العثماني الموثق</div>
      </div>
      <button onclick="closeQuranModal('quranReaderModal')" style="width:36px; height:36px; border-radius:10px; background:rgba(255,255,255,0.14); border:1px solid rgba(255,255,255,0.22); color:#fff; font-size:17px; cursor:pointer; flex-shrink:0;">✕</button>
    </div>
    <div class="quran-tabs-row">
      <button class="q-tab-btn active" id="qTabBtnMushaf" onclick="switchQuranModalTab('mushaf')">📜 المصحف والتلاوة</button>
      <button class="q-tab-btn" id="qTabBtnVocab" onclick="switchQuranModalTab('vocab')">🏷️ معاني الآيات</button>
      <button class="q-tab-btn" id="qTabBtnExplain" onclick="switchQuranModalTab('explain')">📖 الشرح والأهداف</button>
    </div>
    <div id="quranReaderBody" class="quran-sheet-body"></div>
  </div>
</div>

<!-- 2. QURAN STORY & INTERACTIVE SCENES MODAL -->
<div id="quranSceneModal" class="quran-modal-backdrop" onclick="if(event.target===this) closeQuranModal('quranSceneModal')">
  <div class="quran-sheet">
    <div class="quran-sheet-head">
      <div style="min-width:0; flex:1;">
        <div id="qSceneTitle" style="font-size:15.5px; font-weight:800; line-height:1.35;">المشهد التعليمي التفاعلي</div>
        <div id="qSceneSub" style="font-size:11.5px; color:#FDE68A; margin-top:2px;"></div>
      </div>
      <button onclick="closeQuranModal('quranSceneModal')" style="width:36px; height:36px; border-radius:10px; background:rgba(255,255,255,0.14); border:1px solid rgba(255,255,255,0.22); color:#fff; font-size:17px; cursor:pointer; flex-shrink:0;">✕</button>
    </div>
    <div id="qSceneBody" class="quran-sheet-body"></div>
  </div>
</div>

<!-- 3. QURAN TAQWIM & HIFZ TESTER MODAL -->
<div id="quranTaqwimModal" class="quran-modal-backdrop" onclick="if(event.target===this) closeQuranModal('quranTaqwimModal')">
  <div class="quran-sheet">
    <div class="quran-sheet-head">
      <div style="min-width:0; flex:1;">
        <div id="qTaqwimTitle" style="font-size:16px; font-weight:800;">التقويم واختبار الحفظ</div>
        <div id="qTaqwimSub" style="font-size:11.5px; color:#A7F3D0; margin-top:2px;">الأسئلة الرسمية الحرفية + اختبارات تفاعلية</div>
      </div>
      <button onclick="closeQuranModal('quranTaqwimModal')" style="width:36px; height:36px; border-radius:10px; background:rgba(255,255,255,0.14); border:1px solid rgba(255,255,255,0.22); color:#fff; font-size:17px; cursor:pointer; flex-shrink:0;">✕</button>
    </div>
    <div class="quran-tabs-row">
      <button class="q-tab-btn active" id="qtTabOfficial" onclick="switchTaqwimTab('official')">✍️ التقويم الرسمي</button>
      <button class="q-tab-btn" id="qtTabMcq" onclick="switchTaqwimTab('mcq')">✅ اختبار تقويم الدرس</button>
      <button class="q-tab-btn" id="qtTabHifz" onclick="switchTaqwimTab('hifz')">🧠 مختبر الحفظ</button>
    </div>
    <div id="qTaqwimBody" class="quran-sheet-body"></div>
  </div>
</div>
"""


QURAN_ENGINE_JS = r"""
// ========================================================
// GRADE 12 QURAN INTERACTIVE ENGINE (OFFLINE RECITER + SCENES + TAQWIM)
// ========================================================
const Q_VERSES = CURR_DATA?.verses || {};
const Q_SCENES = CURR_DATA?.scenes || {};
const Q_TAQWIM_DRILLS = CURR_DATA?.taqwim_drills || {};
const Q_HIFZ_DRILLS = CURR_DATA?.hifz_drills || {};
const Q_WAQF = CURR_DATA?.waqf_marks || {};
const Q_BASMALA = CURR_DATA?.basmala || '';

const qState = {
  lessonId: 'q-s1-01',
  tab: 'mushaf',
  tajweedOn: true,
  repeatCount: 1,
  remainingLoops: 0,
  playbackRate: 1.0,
  playingKey: '',
  playlist: [],
  playlistIdx: -1,
  taqwimTab: 'official',
  ifkOrder: [2, 5, 1, 6, 3, 4],
  istiizanScenario: 0,
  rainStage: 0
};

let qAudioEl = null;

function toArDigits(n) {
  const map = ['٠','١','٢','٣','٤','٥','٦','٧','٨','٩'];
  return String(n).replace(/\d/g, d => map[Number(d)]);
}

function resolveQuranAssetSrc(src) {
  if (!src) return '';
  return src;
}

function quranSpeakArabic(text) {
  if (!text) return;
  stopQuranReciter();
  if (window.ThakerBridge && typeof window.ThakerBridge.speak === 'function') {
    try {
      const ok = window.ThakerBridge.speak(text, 'ar');
      if (ok !== false) { showToast('🔊 جاري القراءة الصوتية للشرح...'); return; }
    } catch (e) {}
  }
  if ('speechSynthesis' in window) {
    try {
      window.speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(text);
      const voices = window.speechSynthesis.getVoices() || [];
      const arVoice = voices.find(v => (v.lang || '').toLowerCase().startsWith('ar'));
      if (arVoice) u.voice = arVoice;
      u.lang = 'ar-SA';
      u.rate = 0.94;
      window.speechSynthesis.speak(u);
      showToast(arVoice ? '🔊 جاري القراءة الصوتية...' : '🔊 تشغيل النطق عبر المتصفح (تحقق من دعم الصوت العربي بجهازك)');
      return;
    } catch (e) {}
  }
  showToast('النطق الصوتي التوضيحي يعتمد على محرك النطق في جهاز الأندرويد');
}

function stopQuranNarration() {
  if ('speechSynthesis' in window) { try { window.speechSynthesis.cancel(); } catch (e) {} }
}

function stopQuranReciter() {
  if (qAudioEl) {
    try { qAudioEl.pause(); qAudioEl.currentTime = 0; } catch (e) {}
  }
  qState.playingKey = '';
  qState.playlist = [];
  qState.playlistIdx = -1;
  document.querySelectorAll('.ayah-card.playing').forEach(el => el.classList.remove('playing'));
  const playAllBtn = document.getElementById('btnPlayAllLesson');
  if (playAllBtn) playAllBtn.textContent = '▶ استمع لتلاوة الدرس كاملة (الحصري)';
}

function playAyahKey(verseKey, playlistArr, playlistIdx) {
  const v = Q_VERSES[verseKey];
  if (!v || !v.audio_src) {
    showToast('التلاوة المدمجة متوفرة أوفلاين لقسم الحفظ والتفسير والشواهد؛ اقرأ نص التلاوة هنا بالتجويد الملوّن');
    return;
  }
  stopQuranNarration();
  if (qState.playingKey === verseKey && qAudioEl && !qAudioEl.paused && !playlistArr) {
    stopQuranReciter();
    return;
  }
  if (!qAudioEl) qAudioEl = new Audio();
  qAudioEl.playbackRate = qState.playbackRate;
  qState.playingKey = verseKey;
  qState.playlist = playlistArr || [];
  qState.playlistIdx = playlistArr ? (playlistIdx ?? 0) : -1;
  qState.remainingLoops = Math.max(0, (qState.repeatCount || 1) - 1);

  document.querySelectorAll('.ayah-card').forEach(el => {
    el.classList.toggle('playing', el.dataset.vkey === verseKey);
  });
  const activeCard = document.querySelector(`.ayah-card[data-vkey="${verseKey}"]`);
  if (activeCard) activeCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

  const playAllBtn = document.getElementById('btnPlayAllLesson');
  if (playAllBtn) playAllBtn.textContent = `⏹ إيقاف التلاوة (${v.surah_name}: ${toArDigits(v.ayah)})`;

  let triedAlt = false;
  qAudioEl.onerror = function() {
    if (!triedAlt && v.audio_src.indexOf('assets/curriculum') !== -1) {
      triedAlt = true;
      qAudioEl.src = v.audio_src.replace('assets/curriculum', 'curriculum');
      qAudioEl.play().catch(() => {});
    } else {
      showToast('تعذر فتح ملف الصوت المحلي للآية ' + verseKey);
      stopQuranReciter();
    }
  };
  qAudioEl.onended = function() {
    if (qState.remainingLoops > 0) {
      qState.remainingLoops -= 1;
      qAudioEl.currentTime = 0;
      qAudioEl.play().catch(() => {});
      return;
    }
    if (qState.playlist.length && qState.playlistIdx + 1 < qState.playlist.length) {
      const nextIdx = qState.playlistIdx + 1;
      playAyahKey(qState.playlist[nextIdx], qState.playlist, nextIdx);
    } else {
      stopQuranReciter();
    }
  };
  qAudioEl.src = v.audio_src;
  qAudioEl.play().catch(() => {});
}

function playAllCurrentLesson() {
  if (qState.playingKey) { stopQuranReciter(); return; }
  const l = LESSONS.find(x => x.id === qState.lessonId);
  if (!l || !l.surah) return;
  const keys = [];
  for (let a = l.ayah_start; a <= l.ayah_end; a++) {
    const k = `${l.surah}:${a}`;
    if (Q_VERSES[k]?.audio_src) keys.push(k);
  }
  if (!keys.length) {
    showToast('الصوت المدمج متاح لقسم الحفظ والتفسير وشواهد علوم القرآن لتقليل حجم الحزمة');
    return;
  }
  playAyahKey(keys[0], keys, 0);
}

function closeQuranModal(id) {
  document.getElementById(id)?.classList.remove('open');
  stopQuranReciter();
  stopQuranNarration();
}

function _getLessonByIdOrCurrent(lid) {
  if (lid) {
    const f = LESSONS.find(x => x.id === lid);
    if (f) return f;
  }
  const p = PAGES[state.curPageIdx] || PAGES[0] || {};
  return LESSONS.find(x => x.id === p.lesson_id) || LESSONS[0];
}

function openQuranReader(lessonId, initialTab) {
  const l = _getLessonByIdOrCurrent(lessonId);
  qState.lessonId = l.id;
  qState.tab = initialTab || (l.sectionId === 's2' ? 'explain' : 'mushaf');
  document.getElementById('qModalTitle').textContent = l.title;
  document.getElementById('qModalSub').textContent = l.surah
    ? `سورة ${Q_VERSES[`${l.surah}:${l.ayah_start}`]?.surah_name || ''} · الآيات (${toArDigits(l.ayah_start)}–${toArDigits(l.ayah_end)}) · ص ${toArDigits(l.p_start)}–${toArDigits(l.p_end)}`
    : `ثانياً: علوم القرآن · ص ${toArDigits(l.p_start)}–${toArDigits(l.p_end)}`;
  document.getElementById('quranReaderModal').classList.add('open');
  renderQuranModalContent();
}

function switchQuranModalTab(tab) {
  qState.tab = tab;
  renderQuranModalContent();
}

function renderQuranModalContent() {
  const l = _getLessonByIdOrCurrent(qState.lessonId);
  const body = document.getElementById('quranReaderBody');
  document.getElementById('qTabBtnMushaf').classList.toggle('active', qState.tab === 'mushaf');
  document.getElementById('qTabBtnVocab').classList.toggle('active', qState.tab === 'vocab');
  document.getElementById('qTabBtnExplain').classList.toggle('active', qState.tab === 'explain');

  if (qState.tab === 'mushaf') {
    if (!l.surah) {
      // Section 2: collect all citations into Mushaf tab
      const cits = [];
      (l.axes || []).forEach(ax => (ax.citations || []).forEach(c => {
        for (let a = c.start; a <= c.end; a++) cits.push(`${c.surah}:${a}`);
      }));
      body.innerHTML = `
        <div class="reciter-bar">
          <div><b>🎧 شواهد الآيات بصوت الشيخ الحصري</b><div style="font-size:11px; color:#A7F3D0;">جميع الشواهد موثقة من Tanzil وبصوت قارئ حقيقي أوفلاين</div></div>
        </div>
        ${cits.map(k => renderSingleAyahCard(k)).join('')}
      `;
      return;
    }

    const keys = [];
    for (let a = l.ayah_start; a <= l.ayah_end; a++) keys.push(`${l.surah}:${a}`);
    const hasOfflineAudio = keys.some(k => !!Q_VERSES[k]?.audio_src);
    const hasTajweedBar = l.sectionId === 's3' || qState.tajweedOn;

    body.innerHTML = `
      <div class="reciter-bar">
        <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap; width:100%; justify-content:space-between;">
          <div>
            <div style="font-size:13px; font-weight:800;">🎙️ القارئ: الشيخ محمود خليل الحصري</div>
            <div style="font-size:11px; color:#A7F3D0;">${hasOfflineAudio ? 'متاح كاملة أوفلاين آية بآية مع التكرار للحفظ' : 'النص العثماني التفاعلي + التجويد الملوّن (صوت التلاوة الكاملة لـ 5 سور مستثنى لتقليل حجم التطبيق)'}</div>
          </div>
          ${hasOfflineAudio ? `<button id="btnPlayAllLesson" class="reciter-btn" onclick="playAllCurrentLesson()">▶ استمع لتلاوة الدرس كاملة (الحصري)</button>` : ''}
        </div>
        <div style="display:flex; gap:6px; flex-wrap:wrap; width:100%; align-items:center; margin-top:4px;">
          <button class="reciter-chip ${qState.tajweedOn ? 'active' : ''}" onclick="qState.tajweedOn=!qState.tajweedOn; renderQuranModalContent();">🎨 تلوين التجويد: ${qState.tajweedOn ? 'مفعل' : 'إيقاف'}</button>
          ${hasOfflineAudio ? `
            <span style="font-size:11px;">التكرار:</span>
            ${[1, 3, 5].map(r => `<button class="reciter-chip ${qState.repeatCount===r?'active':''}" onclick="qState.repeatCount=${r}; renderQuranModalContent();">×${toArDigits(r)}</button>`).join('')}
            <span style="font-size:11px;">السرعة:</span>
            ${[0.85, 1.0, 1.15].map(sp => `<button class="reciter-chip ${qState.playbackRate===sp?'active':''}" onclick="qState.playbackRate=${sp}; if(qAudioEl) qAudioEl.playbackRate=${sp}; renderQuranModalContent();">${sp}x</button>`).join('')}
          ` : ''}
        </div>
      </div>
      ${qState.tajweedOn ? `
        <div style="display:flex; gap:8px; flex-wrap:wrap; font-size:11.5px; margin-bottom:10px; background:#fff; padding:8px 10px; border-radius:10px; border:1px solid #E2E8F0;">
          <span><b style="color:#DC2626;">● القلقلة</b> (قطب جد)</span>
          <span><b style="color:#059669;">● الغنة</b> (نّ / مّ)</span>
          <span><b style="color:#2563EB;">● المد الطويل</b> (الواجب/اللازم)</span>
          <span><b style="color:#B45309;">● علامات الوقف</b> (اضغط للتوضيح)</span>
        </div>
      ` : ''}
      ${l.tajweed_rule ? `
        <div style="background:#FFFBEB; border:1px solid #FCD34D; border-radius:12px; padding:10px 12px; margin-bottom:10px;">
          <span class="quran-badge-official">📌 المقرر في التلاوة: ${l.tajweed_rule}</span>
          <div style="font-size:12.5px; color:#78350F; line-height:1.8; margin-top:5px;">${l.official_note || ''}</div>
          <div style="font-size:12.5px; color:#1E293B; line-height:1.8; margin-top:3px;"><b>التوضيح:</b> ${l.tajweed_desc}</div>
        </div>
      ` : ''}
      <div class="mushaf-frame ${qState.tajweedOn ? 'tajweed-on' : ''}">
        ${(l.ayah_start === 1 && l.surah !== 9) ? `<div class="mushaf-basmala">${Q_BASMALA}</div>` : ''}
        ${keys.map(k => renderSingleAyahCard(k)).join('')}
      </div>
    `;
    body.querySelectorAll('.tj-waqf').forEach(el => {
      el.onclick = () => showToast('علامة وقف: ' + (el.getAttribute('title') || ''));
    });
  } else if (qState.tab === 'vocab') {
    const voc = l.vocab || [];
    if (!voc.length) {
      body.innerHTML = `<div style="text-align:center; padding:24px; color:#64748B;">هذا الدرس من قسم «${l.sectionId === 's2' ? 'علوم القرآن' : 'التلاوة'}» ولا يحتوي على جدول «معاني الآيات»؛ تفحّص تبويب «الشرح والأهداف» أو «المصحف».</div>`;
      return;
    }
    body.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; gap:8px; flex-wrap:wrap;">
        <span class="quran-badge-official">📖 من الكتاب الرسمي · معاني الآيات (${toArDigits(voc.length)} مفردات)</span>
        <button class="reciter-btn" style="background:#047857;" onclick="quranSpeakArabic(LESSONS.find(x=>x.id==='${l.id}').vocab.map(v=>v.phrase+'، معناه: '+v.meaning).join(' . '))">🔊 استمع لمعاني الكلمات</button>
      </div>
      ${voc.map(v => `
        <div class="vocab-item-card">
          <div style="display:flex; justify-content:space-between; align-items:center; gap:8px;">
            <div style="font-family:var(--font-quran); font-size:19px; color:#064E3B; font-weight:700;">﴿ ${v.phrase} ﴾</div>
            <span style="font-size:11px; color:#64748B;">(${v.ref})</span>
          </div>
          <div style="font-size:14px; color:#1E293B; margin-top:4px; line-height:1.8;">${v.meaning}</div>
        </div>
      `).join('')}
    `;
  } else {
    // Explain & Objectives & Story Timeline & Notes
    const allNarration = [];
    if (l.intro) allNarration.push(...l.intro.paragraphs);
    (l.axes || []).forEach(ax => { allNarration.push(ax.heading); allNarration.push(...ax.paragraphs); });
    if (l.tajweed_desc) allNarration.push(l.official_note || '', l.tajweed_desc);

    body.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; gap:8px; margin-bottom:12px; flex-wrap:wrap;">
        <span class="quran-badge-official">📖 محتوى الدرس الرسمي · ص ${toArDigits(l.p_start)}–${toArDigits(l.p_end)}</span>
        <div style="display:flex; gap:6px; flex-wrap:wrap;">
          <button class="reciter-btn" onclick="quranSpeakArabic(${JSON.stringify(allNarration.join(' . ')).replace(/"/g, '&quot;')})">🔊 استمع للشرح</button>
          <button class="reciter-btn" style="background:#B45309;" onclick="closeQuranModal('quranReaderModal'); openQuranTaqwim('${l.id}', 'official');">✍️ تقويم الدرس</button>
        </div>
      </div>
      ${l.objectives ? `
        <div class="q-taqwim-card" style="border-right:4px solid #D97706;">
          <div style="font-weight:800; color:#92400E; margin-bottom:6px;">🎯 الأهداف التعليمية من الكتاب:</div>
          <ul style="margin:0; padding-right:18px; line-height:1.85; font-size:13.5px;">
            ${l.objectives.map(o => `<li>${o}</li>`).join('')}
          </ul>
        </div>
      ` : ''}
      ${l.intro ? `
        <div class="q-taqwim-card" style="background:#ECFDF5; border-color:#6EE7B7;">
          <div style="font-weight:800; color:#065F46; margin-bottom:6px;">${l.intro.heading} (ص ${toArDigits(l.intro.page)}):</div>
          ${l.intro.paragraphs.map(p => `<p style="margin:0 0 6px; font-size:14px; line-height:1.9;">${p}</p>`).join('')}
        </div>
      ` : ''}
      ${(l.axes || []).map(ax => `
        <div class="q-taqwim-card">
          <div style="display:flex; justify-content:space-between; align-items:center; gap:6px; margin-bottom:6px;">
            <div style="font-weight:800; color:#064E3B; font-size:15px;">📌 ${ax.heading}</div>
            <span style="font-size:11px; color:#64748B;">ص ${toArDigits(ax.page)}</span>
          </div>
          ${ax.paragraphs.map(p => `<p style="margin:0 0 7px; font-size:14px; line-height:1.95; color:#1E293B;">${p}</p>`).join('')}
          ${(ax.after_paragraphs || []).map(p => `<p style="margin:0 0 7px; font-size:14px; line-height:1.95; color:#1E293B;">${p}</p>`).join('')}
          ${(ax.citations || []).map(c => {
            const cKeys = [];
            for (let a = c.start; a <= c.end; a++) cKeys.push(`${c.surah}:${a}`);
            return `<div style="margin-top:8px;">${cKeys.map(ck => renderSingleAyahCard(ck, true)).join('')}</div>`;
          }).join('')}
        </div>
      `).join('')}
      ${l.story_timeline ? `
        <div class="q-taqwim-card" style="background:#FFFBEB; border-color:#FCD34D;">
          <div style="display:flex; justify-content:space-between; align-items:center; gap:8px; margin-bottom:8px; flex-wrap:wrap;">
            <span style="font-weight:800; color:#92400E;">🗺️ التسلسل الزمني لحادثة الإفك</span>
            <button class="reciter-btn" style="background:#B45309; padding:5px 11px;" onclick="closeQuranModal('quranReaderModal'); openQuranScene('scene-ifk-map');">افتح المشهد التفاعلي والحوار الصوتي ‹</button>
          </div>
          ${l.story_timeline.map(st => `
            <div class="q-timeline-step">
              <div style="font-weight:800; color:#065F46; font-size:13.5px;">${toArDigits(st.step)}. ${st.title} <span style="font-size:11px; color:#64748B;">(ص ${toArDigits(st.page)})</span></div>
              <div style="font-size:13.5px; line-height:1.8; margin-top:3px;">${st.text}</div>
            </div>
          `).join('')}
        </div>
      ` : ''}
      ${(l.editorial_notes && l.editorial_notes.length) ? `
        <div class="q-taqwim-card" style="background:#FEF2F2; border-color:#FCA5A5;">
          <div style="font-weight:800; color:#991B1B; margin-bottom:4px;">🔍 تنبيه تدقيقي (مرصود في REVIEW_NEEDED.md):</div>
          <ul style="margin:0; padding-right:18px; font-size:12.5px; color:#7F1D1D; line-height:1.8;">
            ${l.editorial_notes.map(n => `<li>${n}</li>`).join('')}
          </ul>
        </div>
      ` : ''}
    `;
  }
}

function renderSingleAyahCard(vkey, isCompact) {
  const v = Q_VERSES[vkey];
  if (!v) return '';
  const bodyHtml = qState.tajweedOn ? v.tajweed_html : v.uthmani;
  const playCls = qState.playingKey === vkey ? 'playing' : '';
  return `
    <div class="ayah-card ${playCls}" data-vkey="${vkey}">
      <div class="ayah-text-uthmani" style="${isCompact ? 'font-size:18.5px;' : ''}">
        ${bodyHtml} <span class="ayah-num-badge">﴿${toArDigits(v.ayah)}﴾</span>
      </div>
      <div style="display:flex; justify-content:space-between; align-items:center; gap:6px; margin-top:6px; flex-wrap:wrap;">
        <span style="font-size:11.5px; color:#64748B; font-weight:700;">سورة ${v.surah_name} · آية ${toArDigits(v.ayah)}</span>
        ${v.audio_src
          ? `<button class="reciter-btn" style="padding:4px 11px; font-size:11.5px;" onclick="playAyahKey('${vkey}')">🎧 استمع (الحصري)</button>`
          : `<span style="font-size:11px; color:#94A3B8;">نص مصحفي موثق</span>`}
      </div>
    </div>
  `;
}

// ========================================================
// INTERACTIVE STORIES & VISUAL SCENES (IFK + NUR + ISTIIZAN + CON)
// ========================================================
function openQuranScene(sceneId) {
  const sc = Q_SCENES[sceneId] || Object.values(Q_SCENES)[0];
  if (!sc) return;
  stopQuranReciter();
  document.getElementById('qSceneTitle').textContent = sc.title;
  document.getElementById('qSceneSub').textContent = sc.subtitle;
  const body = document.getElementById('qSceneBody');

  let visualHtml = '';
  if (sc.kind === 'ai_image') {
    visualHtml = `
      <div class="q-scene-stage" style="padding:6px;">
        <img src="${sc.image_src}" alt="${sc.title}" style="width:100%; max-height:290px; object-fit:cover; border-radius:12px;"
             onerror="if(!this._alt){this._alt=true;this.src=this.src.replace('assets/curriculum','curriculum');}">
      </div>
    `;
  } else if (sc.kind === 'svg_ifk_caravan') {
    visualHtml = `
      <div class="q-scene-stage">
        <svg viewBox="0 0 600 230" style="width:100%; height:auto; display:block;">
          <defs>
            <linearGradient id="skyNight" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0B1F3A"/><stop offset="70%" stop-color="#1E3A5F"/><stop offset="100%" stop-color="#D97706" stop-opacity="0.35"/></linearGradient>
            <linearGradient id="sandGold" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#92400E"/><stop offset="50%" stop-color="#B45309"/><stop offset="100%" stop-color="#78350F"/></linearGradient>
          </defs>
          <rect width="600" height="230" rx="12" fill="url(#skyNight)"/>
          <circle cx="95" cy="38" r="14" fill="#FEF3C7" opacity="0.9"/>
          <circle cx="101" cy="34" r="12" fill="#0B1F3A"/>
          <circle cx="220" cy="28" r="2" fill="#FFFBEB"/><circle cx="340" cy="42" r="2" fill="#FFFBEB"/><circle cx="480" cy="26" r="2.2" fill="#FEF08A"/>
          <path d="M0,165 Q150,145 310,165 T600,158 L600,230 L0,230 Z" fill="url(#sandGold)"/>
          <!-- Route dashed path -->
          <path d="M98,175 Q235,140 355,172 T495,154" fill="none" stroke="#FDE68A" stroke-width="3" stroke-dasharray="8 6"/>
          <!-- Landmark 1: Al-Muraysi Camp -->
          <circle cx="98" cy="175" r="9" fill="#F59E0B" stroke="#FFF" stroke-width="2"/>
          <text x="98" y="205" fill="#FEF3C7" font-size="12.5" font-weight="bold" text-anchor="middle">١. معسكر المريسيع</text>
          <!-- Landmark 2: Empty Hawdaj / Necklace loss -->
          <rect x="225" y="136" width="38" height="22" rx="6" fill="#065F46" stroke="#FDE68A" stroke-width="2"/>
          <text x="244" y="128" fill="#A7F3D0" font-size="12.5" font-weight="bold" text-anchor="middle">٢. فقد العقد والهودج</text>
          <!-- Landmark 3: Safwan leads camel trail -->
          <circle cx="362" cy="170" r="8" fill="#10B981" stroke="#FFF" stroke-width="2"/>
          <text x="362" y="202" fill="#A7F3D0" font-size="12" font-weight="bold" text-anchor="middle">٣. المرافقة لشرف الطريق</text>
          <!-- Landmark 4: Madinah Minarets -->
          <g transform="translate(462,105)">
            <rect x="10" y="22" width="10" height="32" fill="#ECFDF5"/>
            <path d="M22,34 Q36,14 50,34 Z" fill="#10B981"/>
            <rect x="52" y="18" width="10" height="36" fill="#ECFDF5"/>
            <text x="36" y="72" fill="#FFFBEB" font-size="12" font-weight="bold" text-anchor="middle">٤. المدينة والنور (١١–٢٠)</text>
          </g>
        </svg>
      </div>
    `;
  } else if (sc.kind === 'svg_istiizan') {
    const scenarios = [
      {title: 'استئذان الضيف من الخارج (ص ٣٧)', text: 'يقف يمين أو يسار الباب (لا أمام الفتحة)، يسلم ويذكر اسمه صريحاً، يطرق برفق حتى ٣ مرات فإن لم يُؤذن له رجع راضياً.'},
      {title: 'الأوقات الثلاثة داخل البيت (ص ٧٩)', text: 'يستأذن الأطفال المميزون والمماليك قبل الفجر، وفي وقت القيلولة بالظهيرة، وبعد صلاة العشاء لأنها أوقات الخلوة.'},
      {title: 'الأماكن العامة غير المسكونة (ص ٣٨)', text: 'المتاجر والمطاعم والحدائق والمدارس المفتوحة لا تحتاج استئذاناً لدخول بهوها العام، مع وجوب الاستئذان للغرف المغلقة.'},
    ];
    const curS = scenarios[qState.istiizanScenario % scenarios.length];
    visualHtml = `
      <div class="q-scene-stage">
        <svg viewBox="0 0 560 200" style="width:100%; height:auto;">
          <rect width="560" height="200" rx="12" fill="#0F291E"/>
          <rect x="170" y="38" width="220" height="145" rx="10" fill="#1E3A2F" stroke="#F59E0B" stroke-width="2.5"/>
          <rect x="245" y="75" width="70" height="108" rx="6" fill="#92400E" stroke="#FDE68A" stroke-width="2"/>
          <circle cx="258" cy="130" r="4" fill="#FDE68A"/>
          <text x="280" y="60" fill="#FEF3C7" font-size="14" font-weight="bold" text-anchor="middle">البيت المسلم · حرمة وأمان</text>
          <rect x="35" y="92" width="115" height="44" rx="10" fill="#065F46" stroke="#34D399"/>
          <text x="92" y="119" fill="#ECFDF5" font-size="13" font-weight="bold" text-anchor="middle">الوقوف جانباً</text>
          <rect x="410" y="92" width="115" height="44" rx="10" fill="#065F46" stroke="#34D399"/>
          <text x="467" y="119" fill="#ECFDF5" font-size="13" font-weight="bold" text-anchor="middle">الاستئذان ثلاثاً</text>
        </svg>
        <div style="margin-top:8px; display:flex; gap:6px; justify-content:center; flex-wrap:wrap;">
          ${scenarios.map((it, idx) => `<button class="reciter-chip ${qState.istiizanScenario===idx?'active':''}" onclick="qState.istiizanScenario=${idx}; openQuranScene('scene-istiizan-house');">${idx+1}. ${it.title.split('(')[0]}</button>`).join('')}
        </div>
        <div style="margin-top:8px; background:rgba(255,255,255,0.08); border-radius:10px; padding:10px; font-size:13.5px; color:#ECFDF5;"><b>${curS.title}:</b> ${curS.text}</div>
      </div>
    `;
  } else if (sc.kind === 'svg_cosmic_rain') {
    visualHtml = `
      <div class="q-scene-stage">
        <svg viewBox="0 0 560 210" style="width:100%; height:auto;">
          <rect width="560" height="210" rx="12" fill="#0C192C"/>
          <circle cx="495" cy="44" r="24" fill="#FBBF24"/>
          <path d="M120,88 C120,62 155,48 180,58 C200,32 250,35 270,58 C300,45 340,65 335,92 Z" fill="#CBD5E1"/>
          <path d="M160,96 C175,70 230,52 275,68 C315,50 368,68 375,102 L145,102 Z" fill="#64748B"/>
          <line x1="210" y1="112" x2="202" y2="145" stroke="#38BDF8" stroke-width="3" stroke-linecap="round"/>
          <line x1="255" y1="112" x2="247" y2="148" stroke="#38BDF8" stroke-width="3" stroke-linecap="round"/>
          <circle cx="305" cy="128" r="5" fill="#E0F2FE"/>
          <polyline points="342,102 325,130 340,132 322,162" fill="none" stroke="#FDE047" stroke-width="3"/>
          <path d="M0,175 Q180,152 380,178 T560,170 L560,210 L0,210 Z" fill="#065F46"/>
          <text x="115" y="42" fill="#BAE6FD" font-size="13" font-weight="bold">يُزجي ← يؤلف ← ركاماً ← الودق والبرد ← البرق</text>
          <text x="280" y="196" fill="#A7F3D0" font-size="13" font-weight="bold" text-anchor="middle">﴿ يُزْجِي سَحَابًا ثُمَّ يُؤَلِّفُ بَيْنَهُ ثُمَّ يَجْعَلُهُ رُكَامًا ﴾ [النور: ٤٣]</text>
        </svg>
      </div>
    `;
  } else if (sc.kind === 'svg_ijaz') {
    visualHtml = `
      <div class="q-scene-stage">
        <svg viewBox="0 0 560 195" style="width:100%; height:auto;">
          <rect width="560" height="195" rx="12" fill="#091D26"/>
          ${[['١. البلاغة والبيان', '٢٤ كلمة ≡ ٢٤ كلمة', 38], ['٢. الإخبار بالغيب', 'الماضي والحاضر والمستقبل', 168], ['٣. التشريع المحكم', 'العدالة وصون الأسرة', 298], ['٤. السبق العلمي', 'الرتق/الفتق والأجنة', 428]].map(([t, s, x]) => `
            <rect x="${x}" y="35" width="112" height="118" rx="12" fill="#0F3542" stroke="#10B981" stroke-width="2"/>
            <text x="${x+56}" y="76" fill="#FDE68A" font-size="13" font-weight="bold" text-anchor="middle">${t}</text>
            <text x="${x+56}" y="114" fill="#E0F2FE" font-size="11.5" text-anchor="middle">${s}</text>
          `).join('')}
        </svg>
      </div>
    `;
  } else {
    visualHtml = `
      <div class="q-scene-stage">
        <svg viewBox="0 0 560 195" style="width:100%; height:auto;">
          <rect width="560" height="195" rx="12" fill="#07221B"/>
          ${[['الجوف', 'ا و ي المدية', 25, '#0EA5E9'], ['الحلق', 'ء هـ ع ح غ خ', 130, '#10B981'], ['اللسان (١٠)', '١٨ حرفاً', 235, '#F59E0B'], ['الشفتان', 'ف ب م و', 340, '#EC4899'], ['الخيشوم', 'الغنة (نّ مّ)', 445, '#8B5CF6']].map(([t, s, x, col]) => `
            <rect x="${x}" y="40" width="94" height="115" rx="12" fill="#0D2F26" stroke="${col}" stroke-width="2.2"/>
            <text x="${x+47}" y="82" fill="#FFF" font-size="14" font-weight="bold" text-anchor="middle">${t}</text>
            <text x="${x+47}" y="118" fill="#D1FAE5" font-size="12" text-anchor="middle">${s}</text>
          `).join('')}
        </svg>
      </div>
    `;
  }

  const lesson = LESSONS.find(l => l.id === sc.lessonId);
  const timelineHtml = (lesson && lesson.story_timeline) ? `
    <div style="margin-top:12px;">
      <div style="font-weight:800; color:#064E3B; margin-bottom:8px;">🧩 رتب أو راجع أحداث حادثة الإفك بالخطوات (٦ مراحل من ص ٢٤–٢٥):</div>
      ${lesson.story_timeline.map(st => `
        <div class="q-timeline-step">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <b style="color:#047857;">المرحلة ${toArDigits(st.step)}: ${st.title}</b>
            <button class="reciter-chip" style="background:#ECFDF5; color:#065F46; border-color:#6EE7B7;" onclick="quranSpeakArabic(${JSON.stringify(st.title + '. ' + st.text).replace(/"/g, '&quot;')})">🔊 استمع</button>
          </div>
          <div style="font-size:13.5px; line-height:1.85; margin-top:4px;">${st.text}</div>
        </div>
      `).join('')}
      <div class="q-taqwim-card" style="background:#ECFDF5; border-color:#6EE7B7; margin-top:10px;">
        <div style="font-weight:800; color:#065F46; margin-bottom:6px;">🎯 اختبار سريع: ما الترتيب الصحيح لحدثين من حادثة الإفك؟</div>
        <button class="reciter-btn" style="width:100%;" onclick="document.getElementById('ifkSeqResult').style.display='block'; playClickSound();">✅ تحقق من التسلسل التاريخي للحادثة</button>
        <div id="ifkSeqResult" style="display:none; margin-top:8px; font-size:13px; color:#064E3B; line-height:1.8;">
          <b>التسلسل الصحيح الموثق (ص ٢٤):</b> غزوة بني المصطلق ⇐ فقدان العقد ورحيل الهودج ⇐ حمل صفوان بن المعطل لها وصولاً للمدينة ⇐ إشاعة عبد الله بن أبي ⇐ نزول سورة النور (١١–٢٠) بالبراءة ⇐ تأسيس قواعد حسن الظن والتثبت ورد الإشاعات.
        </div>
      </div>
    </div>
  ` : '';

  body.innerHTML = `
    <div style="display:flex; justify-content:space-between; align-items:center; gap:8px; flex-wrap:wrap; margin-bottom:10px;">
      <span class="quran-badge-edu">${sc.badge}</span>
      <button class="reciter-btn" onclick="quranSpeakArabic(${JSON.stringify(sc.narration).replace(/"/g, '&quot;')})">🔊 استمع للشرح الصوتي الكامل</button>
    </div>
    ${visualHtml}
    <div class="q-taqwim-card">
      <div style="font-weight:800; color:#064E3B; margin-bottom:4px;">🎙️ نص الشرح التفاعلي (ص ${toArDigits(sc.page)}):</div>
      <div style="font-size:14px; line-height:1.95; color:#1E293B;">${sc.narration}</div>
    </div>
    ${timelineHtml}
  `;

  document.getElementById('quranSceneModal').classList.add('open');
}

// ========================================================
// INTERACTIVE TAQWIM & HIFZ TESTER MODAL
// ========================================================
function openQuranTaqwim(lessonId, tab) {
  const l = _getLessonByIdOrCurrent(lessonId);
  qState.lessonId = l.id;
  qState.taqwimTab = tab || 'official';
  document.getElementById('qTaqwimTitle').textContent = `تقويم: ${l.title}`;
  document.getElementById('qTaqwimSub').textContent = `الصفحات ص ${toArDigits(l.p_start)}–${toArDigits(l.p_end)}`;
  document.getElementById('quranTaqwimModal').classList.add('open');
  renderTaqwimModalContent();
}

function switchTaqwimTab(t) {
  qState.taqwimTab = t;
  renderTaqwimModalContent();
}

function renderTaqwimModalContent() {
  const l = _getLessonByIdOrCurrent(qState.lessonId);
  const body = document.getElementById('qTaqwimBody');
  document.getElementById('qtTabOfficial').classList.toggle('active', qState.taqwimTab === 'official');
  document.getElementById('qtTabMcq').classList.toggle('active', qState.taqwimTab === 'mcq');
  document.getElementById('qtTabHifz').classList.toggle('active', qState.taqwimTab === 'hifz');

  if (qState.taqwimTab === 'official') {
    const tqs = l.taqwim || [];
    if (!tqs.length) {
      body.innerHTML = `<div class="q-taqwim-card">دروس التلاوة الـ ١٨ تركز على التطبيق العملي للأحكام في المصحف؛ انتقل لتبويب «اختبار التقويم» أو اختبر نفسك في التجويد!</div>`;
      return;
    }
    body.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; gap:8px; margin-bottom:10px; flex-wrap:wrap;">
        <span class="quran-badge-official">📖 أسئلة التقويم الرسمية (${toArDigits(tqs.length)} أسئلة)</span>
        <button class="reciter-btn" onclick="switchTaqwimTab('mcq')">⚡ اختبر نفسك آلياً في هذا التقويم ‹</button>
      </div>
      ${tqs.map((item, idx) => `
        <div class="q-taqwim-card">
          <div style="font-weight:800; font-size:14px; color:#064E3B; line-height:1.85;">${toArDigits(item.num)} – ${item.q}</div>
          ${(item.citations || []).map(c => `<div style="font-family:var(--font-quran); font-size:17.5px; color:#92400E; background:#FFFBEB; padding:6px 10px; border-radius:8px; margin-top:6px;">﴿ ${c.text} ﴾ <span style="font-size:11px;">(${c.ref})</span></div>`).join('')}
          <div style="display:flex; gap:8px; margin-top:8px; flex-wrap:wrap;">
            <button class="reciter-btn" style="padding:5px 12px; font-size:12px;" onclick="const a=document.getElementById('tqAns_${idx}'); a.style.display=a.style.display==='block'?'none':'block';">👁️ الإجابة النموذجية</button>
            <button class="reciter-chip" style="background:#ECFDF5; color:#065F46; border-color:#6EE7B7;" onclick="quranSpeakArabic(${JSON.stringify('السؤال: ' + item.q + ' . الإجابة: ' + item.answer).replace(/"/g, '&quot;')})">🔊 استمع</button>
          </div>
          <div id="tqAns_${idx}" style="display:none; margin-top:8px; padding:9px 11px; border-radius:10px; background:#ECFDF5; border-right:3px solid #047857; font-size:13.5px; line-height:1.85; color:#064E3B;">
            <span class="quran-badge-edu" style="margin-bottom:4px;">إجابة مستخلصة من الكتاب</span><br>${item.answer}
          </div>
        </div>
      `).join('')}
    `;
  } else if (qState.taqwimTab === 'mcq') {
    const mcqs = Q_TAQWIM_DRILLS[l.id] || [];
    if (!mcqs.length) {
      openAssessmentModal(`quiz-qur-${l.sectionId}`);
      closeQuranModal('quranTaqwimModal');
      return;
    }
    body.innerHTML = `
      <div style="margin-bottom:10px;"><span class="quran-badge-edu">اختبار تقويم ${l.title}</span></div>
      ${mcqs.map((m, mi) => `
        <div class="q-taqwim-card" id="mcqCard_${mi}">
          <div style="font-weight:800; color:#064E3B; font-size:14.5px; margin-bottom:8px;">${toArDigits(mi + 1)}. ${m.q}</div>
          ${m.options.map((opt, oi) => `
            <button onclick="checkTaqwimMcq(${mi}, ${oi}, ${m.answer})" style="display:block; width:100%; text-align:right; margin-bottom:6px; padding:10px 12px; border-radius:10px; border:1px solid #CBD5E1; background:#F8FAFC; font-family:inherit; font-size:13.5px; font-weight:700; cursor:pointer;" id="mcqBtn_${mi}_${oi}">
              ${opt}
            </button>
          `).join('')}
          <div id="mcqFb_${mi}" style="display:none; margin-top:6px; padding:8px 10px; border-radius:10px; font-size:13px; line-height:1.7;"></div>
        </div>
      `).join('')}
      <button class="reciter-btn" style="width:100%; margin-top:8px;" onclick="closeQuranModal('quranTaqwimModal'); openAssessmentModal('quiz-qur-${l.sectionId}');">📝 افتح الاختبار الشامل للقسم بالكامل ‹</button>
    `;
  } else {
    // Hifz Memorization Drill
    const hz = Q_HIFZ_DRILLS[l.id] || Object.values(Q_HIFZ_DRILLS)[0];
    if (!hz) {
      body.innerHTML = `<div class="q-taqwim-card">اختر درساً من قسم الحفظ والتفسير (١–١٣) لاختبار حفظ آيات سورة النور.</div>`;
      return;
    }
    body.innerHTML = `
      <div class="reciter-bar">
        <div>
          <b>🧠 مختبر حفظ سورة النور (آية ${toArDigits(hz.ayah)})</b>
          <div style="font-size:11px; color:#A7F3D0;">أكمل الكلمة الناقصة بالرسم العثماني مع التلاوة الحقيقية للشيخ الحصري</div>
        </div>
        <button class="reciter-btn" onclick="playAyahKey('${hz.surah}:${hz.ayah}')">🎧 استمع للآية للمراجعة</button>
      </div>
      <div class="mushaf-frame">
        <div class="ayah-text-uthmani" id="hifzPromptBox">${hz.masked_uthmani} <span class="ayah-num-badge">﴿${toArDigits(hz.ayah)}﴾</span></div>
      </div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
        ${hz.options.map((w, wi) => `
          <button onclick="checkHifzOpt(${wi}, ${hz.answer}, '${l.id}')" id="hifzBtn_${wi}" style="padding:12px; border-radius:12px; border:1.5px solid #D97706; background:#FFFBEB; font-family:var(--font-quran); font-size:20px; color:#1E293B; cursor:pointer;">${w}</button>
        `).join('')}
      </div>
      <div id="hifzResultBox" style="display:none; margin-top:10px; padding:10px; border-radius:12px; font-size:14px; font-weight:700;"></div>
    `;
  }
}

function checkTaqwimMcq(mi, chosen, correct) {
  const l = _getLessonByIdOrCurrent(qState.lessonId);
  const m = (Q_TAQWIM_DRILLS[l.id] || [])[mi];
  if (!m) return;
  const ok = chosen === correct;
  m.options.forEach((_, idx) => {
    const b = document.getElementById(`mcqBtn_${mi}_${idx}`);
    if (!b) return;
    if (idx === correct) { b.style.background = '#D1FAE5'; b.style.borderColor = '#059669'; }
    else if (idx === chosen) { b.style.background = '#FEE2E2'; b.style.borderColor = '#DC2626'; }
  });
  const fb = document.getElementById(`mcqFb_${mi}`);
  fb.style.display = 'block';
  fb.style.background = ok ? '#ECFDF5' : '#FEF2F2';
  fb.style.color = ok ? '#065F46' : '#991B1B';
  fb.innerHTML = (ok ? '✅ أحسنت! ' : '❌ راجع الفكرة: ') + m.explain;
  playClickSound();
}

function checkHifzOpt(chosen, correct, lid) {
  const hz = Q_HIFZ_DRILLS[lid] || Object.values(Q_HIFZ_DRILLS)[0];
  hz.options.forEach((_, i) => {
    const b = document.getElementById(`hifzBtn_${i}`);
    if (!b) return;
    if (i === correct) { b.style.background = '#D1FAE5'; b.style.borderColor = '#059669'; }
    else if (i === chosen) { b.style.background = '#FEE2E2'; b.style.borderColor = '#DC2626'; }
  });
  const res = document.getElementById('hifzResultBox');
  res.style.display = 'block';
  res.style.background = chosen === correct ? '#ECFDF5' : '#FEF2F2';
  res.style.color = chosen === correct ? '#065F46' : '#991B1B';
  res.innerHTML = (chosen === correct ? '🌟 ما شاء الله! إتقان ممتاز للحفظ. ' : '📖 أعد سماع الآية وثبت الكلمة الصحيحة. ') +
    `<div style="font-family:var(--font-quran); font-size:18px; margin-top:6px; color:#111827;">${hz.full_uthmani}</div>`;
}

// ========================================================
// WIRE HOTSPOTS, FLOATING READER PILLS & OVERRIDES
// ========================================================
function openCurrentQuranReader() { openQuranReader(null, 'mushaf'); }
function openCurrentQuranTaqwim() { openQuranTaqwim(null, 'official'); }
function openCurrentQuranScene() {
  const l = _getLessonByIdOrCurrent(null);
  const sc = Object.values(Q_SCENES).find(s => s.lessonId === l.id) ||
             (l.id === 'q-s1-04' ? Q_SCENES['scene-ifk-map'] : null) ||
             (l.id === 'q-s1-12' ? Q_SCENES['scene-istiizan-house'] : null) ||
             (l.sectionId === 's3' ? Q_SCENES['scene-makharij-tajweed'] : Q_SCENES['scene-ifk-map']);
  openQuranScene(sc.id);
}

const baseOpenTextExplanationForQuran = openTextExplanation;
openTextExplanation = function(refId) {
  if (typeof BOOK_SUBJECT_KEY !== 'undefined' && BOOK_SUBJECT_KEY === 'quran' && EXPLANATIONS[refId]) {
    const exp = EXPLANATIONS[refId];
    const lid = refId.replace(/^exp-/, '');
    if (LESSONS.find(l => l.id === lid)) {
      openQuranReader(lid, 'explain');
      return;
    }
  }
  baseOpenTextExplanationForQuran(refId);
};

const baseHandleHotspotClickForQuran = handleHotspotClick;
handleHotspotClick = function(item) {
  if (typeof BOOK_SUBJECT_KEY !== 'undefined' && BOOK_SUBJECT_KEY === 'quran') {
    playClickSound();
    if (item.type === 'quran_reader') { openQuranReader(item.lesson_ref, 'mushaf'); return; }
    if (item.type === 'quran_scene') { openQuranScene(item.scene_ref); return; }
    if (item.type === 'quran_taqwim') { openQuranTaqwim(item.lesson_ref, 'official'); return; }
  }
  baseHandleHotspotClickForQuran(item);
};

const baseOpenDedicatedLabForQuran = (typeof openDedicatedLabForPage === 'function') ? openDedicatedLabForPage : null;
openDedicatedLabForPage = function() {
  if (typeof BOOK_SUBJECT_KEY !== 'undefined' && BOOK_SUBJECT_KEY === 'quran') {
    openCurrentQuranReader();
    return;
  }
  if (baseOpenDedicatedLabForQuran) baseOpenDedicatedLabForQuran();
};

// Inject clean Quran reader quick-launch bar inside floating pills container
(function setupQuranFloatingActions() {
  const pill = document.getElementById('hotspotSummaryPill');
  if (!pill || !pill.parentElement) return;
  const wrap = pill.parentElement;
  wrap.style.gap = '6px';
  pill.style.padding = '7px 11px';
  pill.style.fontSize = '11.5px';

  const bMushaf = document.createElement('button');
  bMushaf.className = 'hotspot-summary-pill';
  bMushaf.style.cssText = 'background:linear-gradient(135deg,#047857,#064E3B); padding:7px 11px; font-size:11.5px;';
  bMushaf.innerHTML = '<span>🕌 المصحف والحصري</span>';
  bMushaf.onclick = openCurrentQuranReader;

  const bScene = document.createElement('button');
  bScene.className = 'hotspot-summary-pill';
  bScene.style.cssText = 'background:linear-gradient(135deg,#B45309,#92400E); padding:7px 11px; font-size:11.5px;';
  bScene.innerHTML = '<span>🖼️ القصة والمشاهد</span>';
  bScene.onclick = openCurrentQuranScene;

  const bTaqwim = document.createElement('button');
  bTaqwim.className = 'hotspot-summary-pill';
  bTaqwim.style.cssText = 'background:linear-gradient(135deg,#0F766E,#115E59); padding:7px 11px; font-size:11.5px;';
  bTaqwim.innerHTML = '<span>✍️ التقويم والحفظ</span>';
  bTaqwim.onclick = openCurrentQuranTaqwim;

  wrap.appendChild(bMushaf);
  wrap.appendChild(bScene);
  wrap.appendChild(bTaqwim);
})();
"""
