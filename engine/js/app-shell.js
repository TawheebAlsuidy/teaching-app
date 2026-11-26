/* Unified Thaker Book Shell: Lazy Lesson Loader + Deep Links + Renderer */
(function (global) {
  "use strict";

  global.__THAKER_LESSONS__ = global.__THAKER_LESSONS__ || {};
  var activeView = "lesson";
  var loadedScripts = {};
  var ctx = {
    book: null,
    lesson: null,
    state: null,
    persistState: function () {},
    loadLesson: function () {},
    switchMainView: function () {},
    rerenderBlocks: function () {},
    recordAnswer: function () {}
  };

  function escHtml(s) {
    return String(s || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function parseHash() {
    var raw = (global.location.hash || "").replace(/^#/, "");
    var out = {};
    if (!raw) return out;
    raw.split("&").forEach(function (pair) {
      var kv = pair.split("=");
      if (kv.length >= 2) {
        out[decodeURIComponent(kv[0])] = decodeURIComponent(kv.slice(1).join("="));
      }
    });
    return out;
  }

  function loadScriptOnce(src) {
    return new Promise(function (resolve, reject) {
      if (loadedScripts[src]) {
        resolve();
        return;
      }
      var s = document.createElement("script");
      s.src = src;
      s.onload = function () {
        loadedScripts[src] = true;
        resolve();
      };
      s.onerror = function () { reject(new Error("Failed to load " + src)); };
      document.head.appendChild(s);
    });
  }

  function originPill(origin) {
    var map = {
      from_book: ["من الكتاب", "tk-origin-from_book"],
      educational_addition: ["إضافة تعليمية", "tk-origin-educational_addition"],
      for_enrichment: ["للتوسع", "tk-origin-for_enrichment"],
      proposed_solution: ["حل مقترح", "tk-origin-proposed_solution"]
    };
    var item = map[origin] || map.from_book;
    return '<span class="tk-origin ' + item[1] + '">' + item[0] + "</span>";
  }

  function renderBlocks() {
    var main = document.getElementById("tkLessonContent");
    if (!main || !ctx.lesson) return;
    main.innerHTML = "";
    var lesson = ctx.lesson;

    // Lesson Banner
    var banner = document.createElement("section");
    banner.className = "tk-lesson-banner";
    var refsHtml = (lesson.lesson.source_refs || []).map(function (r) {
      var imgKey = (r.book || "pb").toLowerCase() + "_" + r.book_page;
      var imgPath = (lesson.lesson.reference_images && lesson.lesson.reference_images[imgKey]) || "";
      return '<button type="button" class="tk-ref-chip" data-ref-book="' + escHtml(r.book) + '" data-ref-page="' +
        escHtml(r.book_page) + '" data-ref-pdf="' + escHtml(r.pdf_page) + '" data-ref-img="' + escHtml(imgPath) + '">📄 مرجع ' +
        escHtml(r.book) + " ص " + escHtml(r.book_page) + "</button>";
    }).join("");
    banner.innerHTML =
      '<div class="tk-tag-group"><span class="tk-unit-pill">Unit ' + escHtml(lesson.unit.number) + " · " + escHtml(lesson.unit.title) + "</span>" +
      '<span class="tk-origin tk-origin-from_book">من الكتاب</span></div>' +
      '<h1 class="tk-banner-h1" dir="' + escHtml(lesson.lesson.direction || "ltr") + '">' +
      escHtml(lesson.lesson.code + " · " + lesson.lesson.title) + "</h1>" +
      (lesson.lesson.title_ar ? '<div style="font-size:14px;color:var(--muted);">' + escHtml(lesson.lesson.title_ar) + "</div>" : "") +
      '<div class="tk-banner-refs">' + refsHtml + "</div>";
    banner.querySelectorAll("[data-ref-img]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        global.ThakerSheet.open(ctx, {
          label: "مرجع صفحة الكتاب",
          tabs: {
            page_ref: {
              book: btn.getAttribute("data-ref-book"),
              page: btn.getAttribute("data-ref-page"),
              pdf_page: btn.getAttribute("data-ref-pdf"),
              image: btn.getAttribute("data-ref-img")
            }
          }
        }, "page_ref");
      });
    });
    main.appendChild(banner);

    // Content Blocks
    (lesson.blocks || []).forEach(function (blk) {
      var card = document.createElement("article");
      var isBm = Boolean(ctx.state.bookmarks && ctx.state.bookmarks[blk.id]);
      var hasNote = Boolean(ctx.state.notes && ctx.state.notes[blk.id]);
      var isHl = Boolean(ctx.state.highlights && ctx.state.highlights[blk.id]);
      card.className = "tk-block" + (isHl ? " is-highlighted" : "");
      card.id = "blk-" + blk.id;
      card.setAttribute("data-block-id", blk.id);

      var metaRow = document.createElement("div");
      metaRow.className = "tk-meta-row";
      metaRow.innerHTML =
        '<div class="tk-tag-group">' +
        originPill(blk.origin || "from_book") +
        '<span class="tk-page-badge">' + escHtml(blk.source.book + " ص " + blk.source.page) + "</span>" +
        "</div>" +
        '<div class="tk-block-actions">' +
        '<button type="button" class="tk-act-mini ' + (isHl ? "active" : "") + '" data-act="hl" title="تمييز">🖍</button>' +
        '<button type="button" class="tk-act-mini ' + (isBm ? "active" : "") + '" data-act="bm" title="إشارة مرجعية">🔖</button>' +
        '<button type="button" class="tk-act-mini ' + (hasNote ? "active" : "") + '" data-act="note" title="ملاحظة">📝</button>' +
        "</div>";
      metaRow.querySelector('[data-act="hl"]').addEventListener("click", function () {
        ctx.state.highlights[blk.id] = !ctx.state.highlights[blk.id];
        ctx.persistState();
        renderBlocks();
      });
      metaRow.querySelector('[data-act="bm"]').addEventListener("click", function () {
        ctx.state.bookmarks[blk.id] = !ctx.state.bookmarks[blk.id];
        ctx.persistState();
        renderBlocks();
      });
      metaRow.querySelector('[data-act="note"]').addEventListener("click", function () {
        global.ThakerSearchNotes.promptNote(blk.id, ctx);
      });
      card.appendChild(metaRow);

      var bodyEl = document.createElement("div");
      bodyEl.className = "tk-content-body" + (blk.type === "heading" ? " tk-content-heading" : "");
      bodyEl.setAttribute("dir", blk.dir || "ltr");

      var useEnglish = lesson.subject === "english" && (blk.dir || "ltr") === "ltr" && global.ThakerSubjectEnglish;
      if (blk.content && blk.content.lines && blk.content.lines.length) {
        blk.content.lines.forEach(function (ln) {
          var p = document.createElement("div");
          p.style.marginBottom = "4px";
          if (useEnglish) {
            global.ThakerSubjectEnglish.renderInteractiveText(p, ln, ctx, blk.recall_words);
          } else {
            p.textContent = ln;
          }
          bodyEl.appendChild(p);
        });
      } else if (blk.content && blk.content.text) {
        if (useEnglish) {
          global.ThakerSubjectEnglish.renderInteractiveText(bodyEl, blk.content.text, ctx, blk.recall_words);
        } else {
          bodyEl.textContent = blk.content.text;
        }
      }

      if (blk.content && blk.content.picture_items && blk.content.picture_items.length) {
        var grid = document.createElement("div");
        grid.className = "tk-pic-grid";
        blk.content.picture_items.forEach(function (pi) {
          var pc = document.createElement("div");
          pc.className = "tk-pic-card";
          pc.innerHTML = '<div class="tk-pic-num">' + escHtml(pi.num) + '</div><img src="' + escHtml(pi.img) + '" alt="Item ' + escHtml(pi.num) + '">';
          grid.appendChild(pc);
        });
        bodyEl.appendChild(grid);
      }

      if (blk.content && blk.content.image) {
        var mf = document.createElement("div");
        mf.className = "tk-media-frame";
        mf.innerHTML = '<img src="' + escHtml(blk.content.image) + '" alt="' + escHtml(blk.content.caption || "") + '">';
        bodyEl.appendChild(mf);
      }

      card.appendChild(bodyEl);

      // Personal note display if set
      if (hasNote) {
        var noteDiv = document.createElement("div");
        noteDiv.className = "tk-edu-callout";
        noteDiv.textContent = "📝 ملاحظتك: " + ctx.state.notes[blk.id];
        card.appendChild(noteDiv);
      }

      // Inline educational note (shown in study mode, hidden in read mode via CSS)
      if (blk.edu_note_html) {
        var ed = document.createElement("div");
        ed.className = "tk-edu-callout";
        ed.innerHTML = '<div class="tk-tag-group" style="margin-bottom:4px;">' + originPill("educational_addition") +
          '<span class="tk-page-badge">مرجع ص ' + escHtml(blk.source.page) + "</span></div>" + blk.edu_note_html;
        card.appendChild(ed);
      }

      // Study footer: audio + bottom sheet hotspot
      var hasAudio = Boolean(blk.audio_src);
      var hasSpot = Boolean(blk.interactive_spot && blk.interactive_spot.enabled);
      if (hasAudio || hasSpot) {
        var sf = document.createElement("div");
        sf.className = "tk-study-footer";
        if (hasAudio) {
          var ab = document.createElement("button");
          ab.type = "button";
          ab.className = "tk-audio-btn";
          ab.textContent = "🔊 استمع للنص";
          ab.addEventListener("click", function () {
            var spTxt = blk.content.text || (blk.content.lines || []).join(" ");
            global.ThakerSpeech.speak(spTxt, blk.audio_src, "en-GB");
          });
          sf.appendChild(ab);
        }
        if (hasSpot) {
          var sb = document.createElement("button");
          sb.type = "button";
          sb.className = "tk-spot-btn";
          sb.textContent = "💡 " + (blk.interactive_spot.label || "شرح وتفصيل (6 تبويبات)");
          sb.addEventListener("click", function () {
            global.ThakerSheet.open(ctx, blk.interactive_spot, "simple_explain");
          });
          sf.appendChild(sb);
        }
        card.appendChild(sf);
      }

      main.appendChild(card);
    });

    // Collapsible Extensions ("للتوسع" collapsed by default)
    (lesson.extensions || []).forEach(function (ext) {
      var det = document.createElement("details");
      det.className = "tk-collapse";
      det.innerHTML =
        "<summary><span>" + originPill("for_enrichment") + " " + escHtml(ext.title) + "</span>" +
        '<span class="tk-page-badge">مرجع ص ' + escHtml(ext.page_ref || 1) + "</span></summary>" +
        '<div class="tk-collapse-body">' + ext.html + "</div>";
      main.appendChild(det);
    });

    if (typeof global.renderMathInElement === "function") {
      try {
        global.renderMathInElement(main, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false }
          ]
        });
      } catch (e) {}
    }
  }

  function renderPracticeSection() {
    var sec = document.getElementById("tkPracticeContent");
    if (!sec || !ctx.lesson) return;
    sec.innerHTML = '<div class="tk-section-title"><span>📝 تمارين كتاب التمارين والاختبار التفاعلي</span></div>';
    (ctx.lesson.activities || []).forEach(function (act) {
      sec.appendChild(global.ThakerQuiz.renderActivityCard(act, ctx));
    });
    if ((ctx.lesson.section_checks || []).length) {
      var h = document.createElement("div");
      h.className = "tk-section-title";
      h.innerHTML = "<span>✅ اختبر نفسك (مع سبب الخطأ والتلميحات)</span>";
      sec.appendChild(h);
      ctx.lesson.section_checks.forEach(function (chk) {
        var wrap = document.createElement("div");
        global.ThakerQuiz.renderQuestionsInto(wrap, chk.questions || [], ctx, false);
        sec.appendChild(wrap);
      });
      var timedHost = document.createElement("div");
      sec.appendChild(timedHost);
      global.ThakerQuiz.renderTimedExamPanel(timedHost, ctx.lesson.section_checks, ctx);
    }
  }

  function renderTocSection() {
    var toc = document.getElementById("tkTocContent");
    if (!toc || !ctx.book) return;
    toc.innerHTML = '<div class="tk-section-title"><span>📚 فهرس الكتاب التفاعلي</span></div>';
    (ctx.book.units || []).forEach(function (u) {
      var card = document.createElement("div");
      card.className = "tk-quiz-card";
      card.innerHTML = '<div style="font-weight:700;margin-bottom:8px;">Unit ' + escHtml(u.number) + ": " + escHtml(u.title) + "</div>";
      (u.lessons || []).forEach(function (ls) {
        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "tk-opt-btn";
        var ready = Boolean(ls.built);
        btn.innerHTML = '<span>' + escHtml(ls.code + " · " + ls.title) + '</span><span class="tk-page-badge">' +
          (ready ? ("PB ص " + ls.pb_page) : "قريباً") + "</span>";
        if (!ready) {
          btn.disabled = true;
          btn.style.opacity = "0.55";
        } else {
          btn.addEventListener("click", function () { loadLesson(ls.id); });
        }
        card.appendChild(btn);
      });
      toc.appendChild(card);
    });
  }

  function switchMainView(view) {
    activeView = view;
    var views = ["lesson", "practice", "flashcards", "search", "toc"];
    views.forEach(function (v) {
      var el = document.getElementById("view-" + v);
      if (el) el.style.display = v === view ? "block" : "none";
    });
    document.querySelectorAll("[data-nav-view]").forEach(function (b) {
      b.classList.toggle("active", b.getAttribute("data-nav-view") === view);
    });
    if (view === "flashcards") {
      global.ThakerLeitner.renderPanel(document.getElementById("tkFlashcardsContent"), ctx);
    } else if (view === "search") {
      global.ThakerSearchNotes.renderPanel(document.getElementById("tkSearchContent"), ctx);
    } else if (view === "toc") {
      renderTocSection();
    }
    global.scrollTo({ top: 0, behavior: "auto" });
  }

  function updateProgressBar() {
    var bookLessons = [];
    (ctx.book.units || []).forEach(function (u) {
      (u.lessons || []).forEach(function (l) { if (l.built) bookLessons.push(l); });
    });
    var doneCount = Object.keys(ctx.state.completedLessons || {}).length;
    var pct = bookLessons.length ? Math.round((doneCount / bookLessons.length) * 100) : 25;
    if (pct < 15 && ctx.lesson) pct = 15;
    var fill = document.getElementById("tkProgressFill");
    if (fill) fill.style.width = pct + "%";
    if (ctx.lesson) {
      global.ThakerStorage.syncAndroidBridge(
        ctx.book.title_ar || ctx.book.title,
        ctx.lesson.lesson.source_refs[0].book_page,
        pct,
        ctx.lesson.unit.id,
        ctx.lesson.lesson.title
      );
    }
  }

  async function loadLesson(lessonId, options) {
    try {
      await loadScriptOnce("lessons/" + lessonId + ".js");
      var lessonObj = global.__THAKER_LESSONS__[lessonId];
      if (!lessonObj) throw new Error("Missing lesson registry: " + lessonId);
      ctx.lesson = lessonObj;
      ctx.state.lastLessonId = lessonId;
      ctx.state.lastPage = lessonObj.lesson.source_refs[0].book_page;
      ctx.persistState();

      document.getElementById("tkBookKicker").textContent = ctx.book.title_ar || ctx.book.title;
      var hdrEl = document.getElementById("tkHeaderTitle");
      hdrEl.setAttribute("dir", lessonObj.lesson.direction || "auto");
      hdrEl.textContent = lessonObj.lesson.code + " · " + lessonObj.lesson.title;

      renderBlocks();
      renderPracticeSection();
      updateProgressBar();
      switchMainView((options && options.view) || "lesson");

      if (options && options.tab === "page_ref") {
        var r0 = lessonObj.lesson.source_refs[0];
        var imgK = r0.book.toLowerCase() + "_" + r0.book_page;
        global.ThakerSheet.open(ctx, {
          label: "مرجع صفحة الكتاب",
          tabs: { page_ref: { book: r0.book, page: r0.book_page, pdf_page: r0.pdf_page, image: lessonObj.lesson.reference_images[imgK] } }
        }, "page_ref");
      } else if (options && options.spot) {
        var targetBlk = (lessonObj.blocks || []).find(function (b) { return b.id === options.spot; });
        if (targetBlk && targetBlk.interactive_spot) {
          global.ThakerSheet.open(ctx, targetBlk.interactive_spot, options.tab || "simple_explain");
        }
      }
    } catch (e) {
      global.ThakerSpeech.showToast("تعذّر تحميل الدرس (" + lessonId + "): " + (e && e.message ? e.message : e));
    }
  }

  async function boot() {
    try {
      var book = global.__THAKER_BOOK__;
      if (!book) {
        global.ThakerSpeech.showToast("تعذّر العثور على بيانات الكتاب book.js");
        return;
      }
      ctx.book = book;
      ctx.state = await global.ThakerStorage.loadState(book.subject);

      var hash = parseHash();
      if (hash.mode && ["read", "study", "practice"].indexOf(hash.mode) >= 0) {
        ctx.state.mode = hash.mode;
      }

      ctx.persistState = function () {
        global.ThakerStorage.saveState(book.subject, ctx.state);
      };
      ctx.loadLesson = loadLesson;
      ctx.switchMainView = switchMainView;
      ctx.rerenderBlocks = renderBlocks;
      ctx.recordAnswer = function (qid, ok) {
        ctx.state.quizResults[qid] = ok;
        if (ok && ctx.lesson) {
          ctx.state.completedLessons[ctx.lesson.lesson.id] = true;
        }
        ctx.persistState();
        updateProgressBar();
      };

      global.ThakerMode.init(ctx);
      global.ThakerSheet.init();

      document.querySelectorAll("[data-nav-view]").forEach(function (b) {
        b.addEventListener("click", function () {
          switchMainView(b.getAttribute("data-nav-view"));
        });
      });

      var backBtn = document.getElementById("tkBackBtn");
      if (backBtn) {
        backBtn.addEventListener("click", function () {
          if (global.ThakerBridge && typeof global.ThakerBridge.returnToHome === "function") {
            global.ThakerBridge.returnToHome();
          } else {
            switchMainView("toc");
          }
        });
      }

      var targetLesson = hash.lesson || ctx.state.lastLessonId || book.default_lesson;
      await loadLesson(targetLesson, { tab: hash.tab, view: hash.view, spot: hash.spot });
    } catch (err) {
      if (global.ThakerSpeech) {
        global.ThakerSpeech.showToast("خطأ أثناء التهيئة: " + (err && err.message ? err.message : err));
      }
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})(window);
