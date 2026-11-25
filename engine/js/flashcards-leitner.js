/* 5-Box Leitner Spaced-Repetition Flashcard Engine */
(function (global) {
  "use strict";

  var INTERVAL_DAYS = { 1: 0, 2: 1, 3: 2, 4: 4, 5: 7 };

  function escHtml(s) {
    return String(s || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function ensureLessonCards(ctx) {
    var leitner = ctx.state.leitner || {};
    var changed = false;
    (ctx.lesson.flashcards || []).forEach(function (fc) {
      if (!leitner[fc.id]) {
        leitner[fc.id] = {
          id: fc.id,
          front: fc.front,
          back: fc.back,
          tag: fc.tag || "",
          origin: fc.origin || "from_book",
          page_ref: fc.page_ref || 1,
          audio_src: fc.audio_src || null,
          box: 1,
          nextReview: 0
        };
        changed = true;
      }
    });
    ctx.state.leitner = leitner;
    if (changed) ctx.persistState();
    return leitner;
  }

  function addCustomWordCard(ctx, word, meaningAr, pos, pageRef, audioSrc) {
    var id = "wl-" + word.toLowerCase().replace(/[^a-z0-9]+/g, "-");
    var leitner = ctx.state.leitner || {};
    if (!leitner[id]) {
      leitner[id] = {
        id: id,
        front: word + (pos ? " (" + pos + ")" : ""),
        back: meaningAr,
        tag: "Word List",
        origin: "from_book",
        page_ref: pageRef || 112,
        audio_src: audioSrc || null,
        box: 1,
        nextReview: 0
      };
      ctx.state.leitner = leitner;
      ctx.persistState();
      if (global.ThakerSpeech) global.ThakerSpeech.showToast("أضيفت البطاقة إلى صندوق Leitner (1)");
    } else if (global.ThakerSpeech) {
      global.ThakerSpeech.showToast("البطاقة موجودة بالفعل في مجموعتك");
    }
  }

  function renderPanel(container, ctx) {
    var leitner = ensureLessonCards(ctx);
    var cards = Object.keys(leitner).map(function (k) { return leitner[k]; });
    var counts = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0 };
    var now = Date.now();
    var due = [];
    cards.forEach(function (c) {
      counts[c.box || 1] = (counts[c.box || 1] || 0) + 1;
      if ((c.nextReview || 0) <= now) due.push(c);
    });
    if (!due.length && cards.length) due = cards.slice();

    container.innerHTML =
      '<div class="tk-meta-row"><div class="tk-tag-group">' +
      '<span class="tk-origin tk-origin-from_book">بطاقات المراجعة (Leitner)</span>' +
      '<span class="tk-page-badge">الإجمالي: ' + cards.length + ' · للمراجعة: ' + due.length + "</span></div></div>" +
      '<div class="tk-leitner-grid">' +
      [1, 2, 3, 4, 5].map(function (b) {
        return '<div class="tk-box-pill">صندوق ' + b + "<br>" + (counts[b] || 0) + "</div>";
      }).join("") +
      "</div><div id='tkLeitnerCardSlot'></div>";

    var slot = document.getElementById("tkLeitnerCardSlot");
    if (!due.length) {
      slot.innerHTML = "<p>لا توجد بطاقات متاحة حالياً.</p>";
      return;
    }

    var idx = 0;
    var flipped = false;

    function drawCard() {
      if (idx >= due.length) idx = 0;
      var c = due[idx];
      slot.innerHTML =
        '<div class="tk-flashcard">' +
        '<div class="tk-meta-row" style="justify-content:center;">' +
        '<span class="tk-page-badge">صندوق ' + (c.box || 1) + ' · مرجع ص ' + escHtml(c.page_ref || 1) + "</span></div>" +
        '<div style="font-size:20px;font-weight:700;" dir="auto">' + escHtml(c.front) + "</div>" +
        (flipped ? '<div style="border-top:1px dashed var(--stroke);padding-top:8px;font-size:17px;" dir="auto">' + escHtml(c.back) + "</div>" : "") +
        '<div class="tk-hint-row" style="justify-content:center;">' +
        '<button type="button" class="tk-btn" id="tkFlipBtn">' + (flipped ? "إخفاء الجواب" : "اقلب البطاقة") + "</button>" +
        '<button type="button" class="tk-audio-btn" id="tkCardSpeakBtn">🔊 استمع</button>' +
        "</div>" +
        (flipped
          ? '<div class="tk-hint-row" style="justify-content:center;">' +
            '<button type="button" class="tk-btn tk-btn-primary" id="tkCardKnowBtn">✓ أتقنتها (ترقية)</button>' +
            '<button type="button" class="tk-btn" id="tkCardMissBtn">↺ أخطأت فيها (صندوق 1)</button></div>'
          : "") +
        "</div>";

      document.getElementById("tkFlipBtn").addEventListener("click", function () {
        flipped = !flipped;
        drawCard();
      });
      document.getElementById("tkCardSpeakBtn").addEventListener("click", function () {
        if (global.ThakerSpeech) global.ThakerSpeech.speak(c.front.replace(/\s*\([^)]*\)/g, ""), c.audio_src, "en-GB");
      });
      var knowBtn = document.getElementById("tkCardKnowBtn");
      var missBtn = document.getElementById("tkCardMissBtn");
      if (knowBtn) {
        knowBtn.addEventListener("click", function () {
          c.box = Math.min(5, (c.box || 1) + 1);
          c.nextReview = Date.now() + (INTERVAL_DAYS[c.box] || 1) * 86400000;
          ctx.state.leitner[c.id] = c;
          ctx.persistState();
          flipped = false;
          idx++;
          renderPanel(container, ctx);
        });
      }
      if (missBtn) {
        missBtn.addEventListener("click", function () {
          c.box = 1;
          c.nextReview = 0;
          ctx.state.leitner[c.id] = c;
          ctx.persistState();
          flipped = false;
          idx++;
          renderPanel(container, ctx);
        });
      }
    }

    drawCard();
  }

  global.ThakerLeitner = {
    renderPanel: renderPanel,
    addCustomWordCard: addCustomWordCard
  };
})(window);
