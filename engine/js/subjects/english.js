/* English Subject Module: Clickable Words + Glossary Popup + Picture Matching + Simulations */
(function (global) {
  "use strict";

  function escHtml(s) {
    return String(s || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function normalizeWord(raw) {
    return String(raw || "")
      .toLowerCase()
      .replace(/^[^a-z0-9]+|[^a-z0-9'-]+$/gi, "");
  }

  function lookupWord(raw, ctx) {
    var norm = normalizeWord(raw);
    if (!norm) return null;
    var map = (ctx.lesson && ctx.lesson.word_glossary_map) || {};
    var bookGloss = (ctx.book && ctx.book.glossary) || {};
    if (map[norm]) return { key: norm, data: map[norm] };
    // Try simple plural/inflection fallback against known lesson glossary keys
    var candidates = [norm.replace(/s$/, ""), norm.replace(/es$/, ""), norm.replace(/ies$/, "y")];
    for (var i = 0; i < candidates.length; i++) {
      if (map[candidates[i]]) return { key: candidates[i], data: map[candidates[i]] };
    }
    if (bookGloss[norm]) return { key: norm, data: bookGloss[norm] };
    return null;
  }

  function showWordPopup(rawWord, ctx) {
    var pop = document.getElementById("tkWordPop");
    if (!pop) return;
    var clean = rawWord.replace(/^[^a-zA-Z0-9']+|[^a-zA-Z0-9']+$/g, "");
    if (!clean) return;
    var found = lookupWord(clean, ctx);
    var entry = found ? found.data : null;
    var displayWord = found ? found.key : clean;
    var audioSrc = entry && entry.audio_src ? entry.audio_src : null;

    pop.innerHTML =
      '<div class="tk-meta-row" style="margin-bottom:4px;">' +
      '<div class="tk-tag-group">' +
      '<strong dir="ltr" style="font-size:18px;color:var(--primary-deep);">' + escHtml(displayWord) + "</strong>" +
      (entry && entry.pos ? '<span class="tk-page-badge">' + escHtml(entry.pos) + "</span>" : "") +
      (entry && entry.in_book_wordlist ? '<span class="tk-origin tk-origin-from_book">Word List · WB ص ' + escHtml(entry.wb_page || 112) + "</span>" : "") +
      "</div>" +
      '<button type="button" class="tk-act-mini" id="tkCloseWordPop" aria-label="إغلاق">✕</button></div>' +
      '<div dir="rtl" style="font-size:15.5px;margin-bottom:8px;">' +
      (entry && entry.ar
        ? escHtml(entry.ar) + (entry.note_ar ? '<div style="font-size:13px;color:var(--muted);margin-top:3px;">' + escHtml(entry.note_ar) + "</div>" : "")
        : '<span style="color:var(--muted)">كلمة إنجليزية في السياق — استمع لنطقها أو أضفها للمراجعة.</span>') +
      "</div>" +
      '<div class="tk-hint-row">' +
      '<button type="button" class="tk-audio-btn" id="tkPopSpeakBtn">🔊 نطق</button>' +
      '<button type="button" class="tk-btn" id="tkPopAddCardBtn">🗂️ أضف لبطاقات Leitner</button>' +
      "</div>";

    pop.classList.add("open");
    document.getElementById("tkCloseWordPop").addEventListener("click", function () {
      pop.classList.remove("open");
    });
    document.getElementById("tkPopSpeakBtn").addEventListener("click", function () {
      if (global.ThakerSpeech) global.ThakerSpeech.speak(displayWord, audioSrc, "en-GB");
    });
    document.getElementById("tkPopAddCardBtn").addEventListener("click", function () {
      if (global.ThakerLeitner) {
        global.ThakerLeitner.addCustomWordCard(
          ctx,
          displayWord,
          (entry && entry.ar) || "مراجعة المفردات",
          entry && entry.pos,
          (entry && entry.wb_page) || 112,
          audioSrc
        );
      }
    });
  }

  function renderInteractiveText(parent, text, ctx, recallTargets) {
    var tokens = String(text || "").split(/(\s+)/);
    var map = (ctx.lesson && ctx.lesson.word_glossary_map) || {};
    var targets = {};
    (recallTargets || []).forEach(function (w) { targets[w.toLowerCase()] = true; });

    tokens.forEach(function (tok) {
      if (/^\s+$/.test(tok)) {
        parent.appendChild(document.createTextNode(tok));
        return;
      }
      var norm = normalizeWord(tok);
      var span = document.createElement("span");
      span.className = "tk-word-tok";
      if (norm && (map[norm] || lookupWord(norm, ctx))) {
        span.classList.add("has-glossary");
      }
      if (norm && targets[norm]) {
        span.classList.add("tk-recall-target");
        span.title = "اضغط لكشف الكلمة في وضع التدريب";
      }
      span.textContent = tok;
      span.addEventListener("click", function () {
        if (document.body.getAttribute("data-mode") === "practice" && span.classList.contains("tk-recall-target")) {
          span.classList.toggle("revealed");
          return;
        }
        if (norm) showWordPopup(tok, ctx);
      });
      parent.appendChild(span);
    });
  }

  function renderSimulation(mount, sim, ctx) {
    if (sim.type === "describing_builder") {
      mount.innerHTML =
        '<p dir="rtl" style="margin-bottom:8px;">كوّن وصفاً سليماً لأي شيء باستخدام قوالب <strong>1.1</strong> واستمع لنطقه:</p>' +
        '<div style="display:grid;gap:8px;">' +
        '<input id="tkSimObj" class="tk-input" dir="ltr" value="A ruler" placeholder="Object (e.g. A ball / A book)">' +
        '<select id="tkSimRel" class="tk-select" dir="ltr">' +
        '<option value="is">is + adjective (shape)</option>' +
        '<option value="has">has + animal covering</option>' +
        '<option value="is made of">is made of + material</option>' +
        "</select>" +
        '<select id="tkSimVal" class="tk-select" dir="ltr">' +
        '<option value="straight">straight (Shape)</option>' +
        '<option value="round">round (Shape)</option>' +
        '<option value="rectangular">rectangular (Shape)</option>' +
        '<option value="curved">curved (Shape)</option>' +
        '<option value="square">square (Shape)</option>' +
        '<option value="triangular">triangular (Shape)</option>' +
        '<option value="hair">hair (Covering)</option>' +
        '<option value="feathers">feathers (Covering)</option>' +
        '<option value="skin">skin (Covering)</option>' +
        '<option value="fur">fur (Covering)</option>' +
        '<option value="scales">scales (Covering)</option>' +
        '<option value="wool">wool (Covering)</option>' +
        '<option value="wood">wood (Made of)</option>' +
        '<option value="glass">glass (Made of)</option>' +
        '<option value="paper">paper (Made of)</option>' +
        '<option value="plastic">plastic (Made of)</option>' +
        '<option value="metal">metal (Made of)</option>' +
        '<option value="cloth">cloth (Made of)</option>' +
        "</select>" +
        '<div id="tkSimOut" class="tk-edu-callout" dir="ltr" style="font-weight:700;font-size:17px;">A ruler is straight.</div>' +
        '<button type="button" class="tk-audio-btn" id="tkSimPlayBtn">🔊 استمع للجملة</button></div>';

      var obj = document.getElementById("tkSimObj");
      var rel = document.getElementById("tkSimRel");
      var val = document.getElementById("tkSimVal");
      var out = document.getElementById("tkSimOut");
      function upd() {
        out.textContent = (obj.value.trim() || "This object") + " " + rel.value + " " + val.value + ".";
      }
      obj.addEventListener("input", upd);
      rel.addEventListener("change", upd);
      val.addEventListener("change", upd);
      document.getElementById("tkSimPlayBtn").addEventListener("click", function () {
        if (global.ThakerSpeech) global.ThakerSpeech.speak(out.textContent, null, "en-GB");
      });
      return;
    }

    if (sim.type === "cama_comparator") {
      var traits = [
        { k: "hump", label: "السنام (Hump)", father: "له سنام", mother: "بلا سنام", rama: "بلا سنام (مثل الأم: Unlike its father, it has no hump)" },
        { k: "ears_tail", label: "الأذنان والذيل", father: "أذنان قصيرتان وذيل طويل", mother: "أذنان طويلتان وذيل قصير", rama: "أذنان قصيرتان وذيل طويل (مثل الأب: Like its father)" },
        { k: "size", label: "الحجم", father: "الأكبر حجماً", mother: "أصغر من الجمل", rama: "أكبر من اللاما لكنه أصغر من الجمل" },
        { k: "coat", label: "الغطاء / الصوف", father: "شعر قليل القيمة (hair coat)", mother: "صوف طويل ثقيل وثمين", rama: "غطاء صوف ثمين كاللاما (heavy valuable wool)" }
      ];
      mount.innerHTML =
        '<p dir="rtl" style="margin-bottom:8px;">اضغط على أي صفة لمقارنة الكاما (Rama) بأبيه الجمل وأمه اللاما وفق نص PB ص 3:</p>' +
        '<div id="tkCamaBtns" class="tk-hint-row"></div>' +
        '<div id="tkCamaCard" class="tk-edu-callout" style="margin-top:10px;"></div>';
      var btns = document.getElementById("tkCamaBtns");
      var card = document.getElementById("tkCamaCard");
      function showTrait(t) {
        card.innerHTML =
          "<strong>" + escHtml(t.label) + "</strong><br>" +
          "🐪 <strong>الجمل (الأب):</strong> " + escHtml(t.father) + "<br>" +
          "🦙 <strong>اللاما (الأم):</strong> " + escHtml(t.mother) + "<br>" +
          "✨ <strong>راما الكاما:</strong> " + escHtml(t.rama);
      }
      traits.forEach(function (t, i) {
        var b = document.createElement("button");
        b.type = "button";
        b.className = "tk-btn";
        b.textContent = t.label;
        b.addEventListener("click", function () { showTrait(t); });
        btns.appendChild(b);
        if (i === 0) showTrait(t);
      });
      return;
    }

    mount.innerHTML = "<p>أداة تفاعلية لهذا القسم قيد العرض المباشر في الدرس.</p>";
  }

  global.ThakerSubjectEnglish = {
    renderInteractiveText: renderInteractiveText,
    showWordPopup: showWordPopup,
    renderSimulation: renderSimulation
  };
})(window);
