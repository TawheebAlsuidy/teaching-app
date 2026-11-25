/* Offline Full-Text Search, Bookmarks, and Personal Notes Manager */
(function (global) {
  "use strict";

  function escHtml(s) {
    return String(s || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function renderPanel(container, ctx) {
    var notes = ctx.state.notes || {};
    var bookmarks = ctx.state.bookmarks || {};
    var blocks = (ctx.lesson && ctx.lesson.blocks) || [];

    container.innerHTML =
      '<div class="tk-quiz-card">' +
      '<div style="font-weight:700;margin-bottom:6px;">البحث الفوري داخل الكتاب والدرس (أوفلاين)</div>' +
      '<input type="search" id="tkSearchInput" class="tk-input" placeholder="ابحث عن كلمة عربية أو إنجليزية أو عنوان درس...">' +
      '<div id="tkSearchResults" style="margin-top:8px;"></div></div>' +
      '<div class="tk-quiz-card">' +
      '<div style="font-weight:700;margin-bottom:6px;">الإشارات المرجعية والملاحظات المحفوظة</div>' +
      '<div id="tkNotesList"></div></div>';

    var input = document.getElementById("tkSearchInput");
    var results = document.getElementById("tkSearchResults");
    var notesList = document.getElementById("tkNotesList");

    function runSearch() {
      var q = (input.value || "").trim().toLowerCase();
      if (!q) {
        results.innerHTML = '<small style="color:var(--muted)">اكتب للبحث في الفهرس والفقرات وقائمة المفردات.</small>';
        return;
      }
      var hits = [];
      (ctx.book.units || []).forEach(function (u) {
        (u.lessons || []).forEach(function (ls) {
          if ((ls.code + " " + ls.title + " " + (ls.title_ar || "")).toLowerCase().indexOf(q) >= 0) {
            hits.push({ kind: "lesson", label: ls.code + " · " + ls.title, lessonId: ls.id });
          }
        });
      });
      blocks.forEach(function (b) {
        var txt = (b.content && (b.content.text || (b.content.lines || []).join(" "))) || "";
        if (txt.toLowerCase().indexOf(q) >= 0) {
          hits.push({ kind: "block", label: "ص " + b.source.page + ": " + txt.slice(0, 85), blockId: b.id });
        }
      });
      var wg = ctx.lesson.word_glossary_map || {};
      Object.keys(wg).forEach(function (w) {
        var info = wg[w];
        if (w.toLowerCase().indexOf(q) >= 0 || (info.ar && info.ar.indexOf(q) >= 0)) {
          hits.push({ kind: "word", label: w + " — " + (info.ar || ""), word: w });
        }
      });

      if (!hits.length) {
        results.innerHTML = "<small>لا توجد نتائج مطابقة.</small>";
        return;
      }
      results.innerHTML = "";
      hits.slice(0, 14).forEach(function (h) {
        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "tk-opt-btn";
        btn.textContent = h.label;
        btn.addEventListener("click", function () {
          if (h.kind === "lesson") {
            ctx.loadLesson(h.lessonId);
          } else if (h.kind === "block") {
            ctx.switchMainView("lesson");
            setTimeout(function () { global.ThakerQuiz.highlightEvidence(h.blockId); }, 100);
          } else if (h.kind === "word" && global.ThakerSubjectEnglish) {
            global.ThakerSubjectEnglish.showWordPopup(h.word, ctx);
          }
        });
        results.appendChild(btn);
      });
    }

    input.addEventListener("input", runSearch);
    runSearch();

    var bmKeys = Object.keys(bookmarks).filter(function (k) { return bookmarks[k]; });
    var noteKeys = Object.keys(notes).filter(function (k) { return notes[k]; });
    if (!bmKeys.length && !noteKeys.length) {
      notesList.innerHTML = '<small style="color:var(--muted)">لم تضف إشارات أو ملاحظات بعد. يمكنك استخدام أيقونة 🔖 أو 📝 على أي فقرة.</small>';
    } else {
      notesList.innerHTML = "";
      bmKeys.forEach(function (bid) {
        var div = document.createElement("div");
        div.style.cssText = "padding:6px 0;border-bottom:1px dashed var(--stroke);";
        div.innerHTML = "🔖 <strong>إشارة محفوظة:</strong> " + escHtml(bid);
        notesList.appendChild(div);
      });
      noteKeys.forEach(function (bid) {
        var div = document.createElement("div");
        div.style.cssText = "padding:6px 0;border-bottom:1px dashed var(--stroke);";
        div.innerHTML = "📝 <strong>" + escHtml(bid) + ":</strong> " + escHtml(notes[bid]);
        notesList.appendChild(div);
      });
    }
  }

  function promptNote(blockId, ctx) {
    var existing = (ctx.state.notes && ctx.state.notes[blockId]) || "";
    var val = global.prompt("أضف أو عدّل ملاحظتك الشخصية لهذا الجزء (اتركه فارغاً للحذف):", existing);
    if (val === null) return;
    ctx.state.notes = ctx.state.notes || {};
    if (val.trim()) {
      ctx.state.notes[blockId] = val.trim();
    } else {
      delete ctx.state.notes[blockId];
    }
    ctx.persistState();
    ctx.rerenderBlocks();
  }

  global.ThakerSearchNotes = {
    renderPanel: renderPanel,
    promptNote: promptNote
  };
})(window);
