/* Interactive Quiz, Activity & Progressive 3-Level Hint Engine */
(function (global) {
  "use strict";

  function escHtml(s) {
    return String(s || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function highlightEvidence(blockId) {
    if (!blockId) return;
    var el = document.getElementById("blk-" + blockId) || document.querySelector('[data-block-id="' + blockId + '"]');
    if (!el) return;
    el.scrollIntoView({ behavior: "smooth", block: "center" });
    el.classList.add("is-evidence-pulse");
    setTimeout(function () { el.classList.remove("is-evidence-pulse"); }, 2200);
  }

  function renderQuestionCard(q, ctx, examLockedHints) {
    var card = document.createElement("div");
    card.className = "tk-quiz-card";
    card.setAttribute("data-qid", q.id);

    var headHtml =
      '<div class="tk-meta-row"><div class="tk-tag-group">' +
      '<span class="tk-origin tk-origin-educational_addition">اختبر نفسك</span>' +
      (q.evidence_block_id ? '<button type="button" class="tk-hint-btn" data-evidence="' + escHtml(q.evidence_block_id) + '">اذهب للدليل</button>' : "") +
      "</div></div>" +
      '<div class="tk-content-body" style="font-weight:700;" dir="auto">' + escHtml(q.stem) + "</div>";
    card.innerHTML = headHtml;

    var evBtn = card.querySelector("[data-evidence]");
    if (evBtn) {
      evBtn.addEventListener("click", function () {
        if (global.ThakerSheet) global.ThakerSheet.close();
        highlightEvidence(q.evidence_block_id);
      });
    }

    var feedbackEl = document.createElement("div");
    var optsWrap = document.createElement("div");

    if (q.options && q.options.length) {
      q.options.forEach(function (opt, idx) {
        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "tk-opt-btn";
        btn.setAttribute("dir", "auto");
        btn.innerHTML = "<span>" + escHtml(opt.text) + "</span>";
        btn.addEventListener("click", function () {
          optsWrap.querySelectorAll(".tk-opt-btn").forEach(function (b) {
            b.classList.remove("is-correct", "is-wrong");
          });
          if (opt.is_correct) {
            btn.classList.add("is-correct");
            feedbackEl.className = "tk-feedback ok";
            feedbackEl.innerHTML = "<strong>إجابة صحيحة:</strong> " + escHtml(q.explain || "أحسنت!");
            if (ctx && ctx.recordAnswer) ctx.recordAnswer(q.id, true);
          } else {
            btn.classList.add("is-wrong");
            feedbackEl.className = "tk-feedback bad";
            feedbackEl.innerHTML =
              "<strong>لماذا هذا الخيار غير صحيح؟</strong> " +
              escHtml(opt.why_wrong || "راجع النص الأصلي للمقارنة.");
            if (ctx && ctx.recordAnswer) ctx.recordAnswer(q.id, false);
          }
          if (opt.audio_src && global.ThakerSpeech) {
            global.ThakerSpeech.speak(opt.text, opt.audio_src, "en-GB");
          }
        });
        optsWrap.appendChild(btn);
      });
    }
    card.appendChild(optsWrap);

    // 3-Level Progressive Hint Ladder
    var hints = q.hints || [];
    if (hints.length && !examLockedHints) {
      var hintIdx = 0;
      var hintRow = document.createElement("div");
      hintRow.className = "tk-hint-row";
      var hintBtn = document.createElement("button");
      hintBtn.type = "button";
      hintBtn.className = "tk-hint-btn";
      hintBtn.textContent = "تلميح (1 / " + hints.length + ")";
      var hintBox = document.createElement("div");
      hintBtn.addEventListener("click", function () {
        if (hintIdx < hints.length) {
          var labels = ["تلميح المفهوم", "تلميح الخطوة الأولى", "الحل مع التعليل"];
          var item = document.createElement("div");
          item.className = "tk-edu-callout";
          item.innerHTML = "<strong>" + (labels[hintIdx] || ("تلميح " + (hintIdx + 1))) + ":</strong> " + escHtml(hints[hintIdx]);
          hintBox.appendChild(item);
          hintIdx++;
          if (hintIdx < hints.length) {
            hintBtn.textContent = "تلميح (" + (hintIdx + 1) + " / " + hints.length + ")";
          } else {
            hintBtn.disabled = true;
            hintBtn.textContent = "عرضت كل التلميحات";
          }
        }
      });
      hintRow.appendChild(hintBtn);
      card.appendChild(hintRow);
      card.appendChild(hintBox);
    }

    card.appendChild(feedbackEl);
    return card;
  }

  function renderQuestionsInto(container, questions, ctx, examLockedHints) {
    container.innerHTML = "";
    questions.forEach(function (q) {
      container.appendChild(renderQuestionCard(q, ctx, examLockedHints));
    });
  }

  function renderHintLadder(parent, hints) {
    if (!hints || !hints.length) return;
    var idx = 0;
    var row = document.createElement("div");
    row.className = "tk-hint-row";
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "tk-hint-btn";
    btn.textContent = "تلميح متدرج (1 / " + hints.length + ")";
    var box = document.createElement("div");
    btn.addEventListener("click", function () {
      if (idx < hints.length) {
        var labels = ["المفهوم", "الخطوة الأولى", "الحل والتعليل"];
        var div = document.createElement("div");
        div.className = "tk-edu-callout";
        div.innerHTML = "<strong>" + (labels[idx] || "تلميح") + ":</strong> " + escHtml(hints[idx]);
        box.appendChild(div);
        idx++;
        if (idx < hints.length) {
          btn.textContent = "تلميح متدرج (" + (idx + 1) + " / " + hints.length + ")";
        } else {
          btn.disabled = true;
          btn.textContent = "انتهت التلميحات";
        }
      }
    });
    row.appendChild(btn);
    parent.appendChild(row);
    parent.appendChild(box);
  }

  function renderActivityCard(act, ctx) {
    var card = document.createElement("div");
    card.className = "tk-quiz-card";
    card.setAttribute("id", "act-" + act.id);

    var solBadge = act.solution_origin === "proposed_solution"
      ? '<span class="tk-origin tk-origin-proposed_solution">حل مقترح</span>'
      : "";
    card.innerHTML =
      '<div class="tk-meta-row"><div class="tk-tag-group">' +
      '<span class="tk-origin tk-origin-from_book">من الكتاب</span>' +
      solBadge +
      '<span class="tk-page-badge">' + escHtml(act.source.book) + " ص " + escHtml(act.source.page) + "</span>" +
      "</div></div>" +
      '<div class="tk-content-body" dir="ltr" style="font-weight:700;margin-bottom:8px;">' +
      escHtml(act.prompt_literal) + "</div>";

    if (act.prompt_ar) {
      var pAr = document.createElement("div");
      pAr.style.cssText = "font-size:13.5px;color:var(--muted);margin-bottom:10px;";
      pAr.textContent = act.prompt_ar;
      card.appendChild(pAr);
    }

    if (act.picture_items && act.picture_items.length) {
      var pGrid = document.createElement("div");
      pGrid.className = "tk-pic-grid";
      pGrid.style.marginBottom = "10px";
      act.picture_items.forEach(function (pi) {
        var pc = document.createElement("div");
        pc.className = "tk-pic-card";
        pc.innerHTML = '<div class="tk-pic-num">' + escHtml(pi.num) + '</div><img src="' + escHtml(pi.img) + '" alt="Item ' + escHtml(pi.num) + '">';
        pGrid.appendChild(pc);
      });
      card.appendChild(pGrid);
    }

    // Matching Pictures (e.g., 1.1 A)
    if (act.type === "matching" && act.items && act.items.length) {
      var selects = [];
      act.items.forEach(function (it) {
        var row = document.createElement("div");
        row.className = "tk-match-row";
        row.setAttribute("dir", "ltr");
        var lbl = document.createElement("div");
        lbl.innerHTML = "<strong>" + escHtml(it.letter) + "</strong> · " + escHtml(it.word) +
          (it.ar ? ' <small style="color:var(--muted)" dir="rtl">(' + escHtml(it.ar) + ")</small>" : "");
        var sel = document.createElement("select");
        sel.className = "tk-select";
        sel.setAttribute("aria-label", "Choose number for " + it.word);
        var optEmpty = document.createElement("option");
        optEmpty.value = "";
        optEmpty.textContent = "اختر الرقم";
        sel.appendChild(optEmpty);
        var choices = act.choices || [];
        choices.forEach(function (ch) {
          var o = document.createElement("option");
          o.value = String(ch.value);
          o.textContent = String(ch.value) + " — " + ch.label;
          sel.appendChild(o);
        });
        selects.push({ item: it, sel: sel });
        row.appendChild(lbl);
        row.appendChild(sel);
        card.appendChild(row);
      });

      var actBtns = document.createElement("div");
      actBtns.className = "tk-hint-row";
      var checkBtn = document.createElement("button");
      checkBtn.type = "button";
      checkBtn.className = "tk-btn tk-btn-primary";
      checkBtn.textContent = "تحقق من المطابقة";
      var fb = document.createElement("div");
      checkBtn.addEventListener("click", function () {
        var score = 0;
        selects.forEach(function (pair) {
          var chosen = pair.sel.value;
          var ok = String(chosen) === String(pair.item.answer);
          pair.sel.style.borderColor = ok ? "var(--primary)" : "var(--danger)";
          if (ok) score++;
        });
        fb.className = "tk-feedback " + (score === selects.length ? "ok" : "bad");
        fb.textContent = "النتيجة: " + score + " من " + selects.length +
          (score === selects.length ? " — ممتاز!" : " — راجع الخانات الحمراء وطابق مع الصور.");
      });
      var revealBtn = document.createElement("button");
      revealBtn.type = "button";
      revealBtn.className = "tk-btn";
      revealBtn.textContent = "إظهار الحل المقترح";
      revealBtn.addEventListener("click", function () {
        selects.forEach(function (pair) {
          pair.sel.value = String(pair.item.answer);
          pair.sel.style.borderColor = "var(--primary)";
        });
        fb.className = "tk-feedback ok";
        fb.textContent = "تم تعبئة الحلول المقترحة لمطابقتها مع صور ص 1.";
      });
      actBtns.appendChild(checkBtn);
      actBtns.appendChild(revealBtn);
      card.appendChild(actBtns);
      card.appendChild(fb);
    }

    // Fill in the blanks (e.g., 1.1 B)
    if (act.type === "fill_blank" && act.items && act.items.length) {
      if (act.word_bank && act.word_bank.length) {
        var wbDiv = document.createElement("div");
        wbDiv.className = "tk-edu-callout";
        wbDiv.setAttribute("dir", "ltr");
        wbDiv.innerHTML = "<strong>Word bank:</strong> " + act.word_bank.map(escHtml).join(" · ");
        card.appendChild(wbDiv);
      }
      var blankInputs = [];
      act.items.forEach(function (it) {
        var row = document.createElement("div");
        row.style.cssText = "padding:8px 0;border-bottom:1px dashed var(--stroke);";
        row.setAttribute("dir", "ltr");
        var txt = document.createElement("div");
        txt.style.marginBottom = "6px";
        txt.textContent = it.num + ". " + it.prompt;
        row.appendChild(txt);
        var controls = document.createElement("div");
        controls.style.cssText = "display:flex;gap:6px;flex-wrap:wrap;";
        var answers = Array.isArray(it.answers) ? it.answers : [it.answer];
        answers.forEach(function (ans, bIdx) {
          var sel = document.createElement("select");
          sel.className = "tk-select";
          var e0 = document.createElement("option");
          e0.value = "";
          e0.textContent = "اختر الكلمة (" + (bIdx + 1) + ")";
          sel.appendChild(e0);
          (act.word_bank || []).forEach(function (w) {
            var o = document.createElement("option");
            o.value = w;
            o.textContent = w;
            sel.appendChild(o);
          });
          blankInputs.push({ sel: sel, expected: ans, explain: it.explain });
          controls.appendChild(sel);
        });
        row.appendChild(controls);
        card.appendChild(row);
      });
      var btnRow = document.createElement("div");
      btnRow.className = "tk-hint-row";
      var verifyBtn = document.createElement("button");
      verifyBtn.type = "button";
      verifyBtn.className = "tk-btn tk-btn-primary";
      verifyBtn.textContent = "تصحيح الفراغات";
      var fb2 = document.createElement("div");
      verifyBtn.addEventListener("click", function () {
        var right = 0;
        blankInputs.forEach(function (bi) {
          var ok = bi.sel.value.trim().toLowerCase() === String(bi.expected).toLowerCase();
          bi.sel.style.borderColor = ok ? "var(--primary)" : "var(--danger)";
          if (ok) right++;
        });
        fb2.className = "tk-feedback " + (right === blankInputs.length ? "ok" : "bad");
        fb2.textContent = "صحيح: " + right + " من " + blankInputs.length + ".";
      });
      var solBtn = document.createElement("button");
      solBtn.type = "button";
      solBtn.className = "tk-btn";
      solBtn.textContent = "عرض الإجابات المقترحة";
      solBtn.addEventListener("click", function () {
        blankInputs.forEach(function (bi) {
          bi.sel.value = bi.expected;
          bi.sel.style.borderColor = "var(--primary)";
        });
        fb2.className = "tk-feedback ok";
        fb2.textContent = "تم عرض الإجابات المقترحة كاملة.";
      });
      btnRow.appendChild(verifyBtn);
      btnRow.appendChild(solBtn);
      card.appendChild(btnRow);
      card.appendChild(fb2);
    }

    // Comprehension Questions (e.g., 1.4 A)
    if (act.type === "comprehension" && act.items && act.items.length) {
      act.items.forEach(function (it) {
        var box = document.createElement("div");
        box.style.cssText = "padding:9px 0;border-bottom:1px dashed var(--stroke);";
        box.innerHTML = '<div dir="ltr" style="font-weight:600;margin-bottom:6px;">' + escHtml(it.num + ". " + it.question) + "</div>";
        var inp = document.createElement("input");
        inp.type = "text";
        inp.className = "tk-input";
        inp.setAttribute("dir", "ltr");
        inp.placeholder = "اكتب إجابتك بالإنجليزية ثم راجع الحل المقترح...";
        box.appendChild(inp);
        var rev = document.createElement("button");
        rev.type = "button";
        rev.className = "tk-hint-btn";
        rev.style.marginTop = "6px";
        rev.textContent = "عرض الإجابة النموذجية المقترحة";
        var ansDiv = document.createElement("div");
        rev.addEventListener("click", function () {
          ansDiv.className = "tk-feedback ok";
          ansDiv.innerHTML = '<div dir="ltr"><strong>Model answer:</strong> ' + escHtml(it.model_answer) + "</div>" +
            (it.explain_ar ? '<div dir="rtl" style="margin-top:4px;">' + escHtml(it.explain_ar) + "</div>" : "");
        });
        box.appendChild(rev);
        box.appendChild(ansDiv);
        card.appendChild(box);
      });
    }

    // Writing / Guided Speaking Steps (e.g., 1.4 B)
    if (act.type === "guided_steps" && act.steps && act.steps.length) {
      if (act.guidance_literal) {
        var g = document.createElement("p");
        g.setAttribute("dir", "ltr");
        g.style.cssText = "background:var(--bg);padding:10px;border-radius:10px;border:1px solid var(--stroke);margin-bottom:8px;";
        g.textContent = act.guidance_literal;
        card.appendChild(g);
      }
      var outputs = [];
      act.steps.forEach(function (st) {
        var row = document.createElement("div");
        row.style.marginBottom = "8px";
        row.innerHTML = '<label style="display:block;font-weight:700;font-size:13px;margin-bottom:4px;">' + escHtml(st.label_ar) + "</label>";
        var inp = document.createElement("input");
        inp.className = "tk-input";
        inp.setAttribute("dir", "ltr");
        inp.placeholder = st.placeholder || "";
        outputs.push(inp);
        row.appendChild(inp);
        card.appendChild(row);
      });
      var assembleBtn = document.createElement("button");
      assembleBtn.type = "button";
      assembleBtn.className = "tk-btn tk-btn-primary";
      assembleBtn.textContent = "تجميع الوصف وقراءته صوتياً";
      var outBox = document.createElement("div");
      assembleBtn.addEventListener("click", function () {
        var para = outputs.map(function (el) { return el.value.trim() || el.placeholder; }).filter(Boolean).join(" ");
        outBox.className = "tk-feedback ok";
        outBox.setAttribute("dir", "ltr");
        outBox.textContent = para;
        if (global.ThakerSpeech) global.ThakerSpeech.speak(para, act.sample_audio_src || null, "en-GB");
      });
      card.appendChild(assembleBtn);
      card.appendChild(outBox);
    }

    renderHintLadder(card, act.hints || []);
    return card;
  }

  function renderTimedExamPanel(mount, checks, ctx) {
    mount.innerHTML = "";
    var allQ = [];
    (checks || []).forEach(function (c) {
      (c.questions || []).forEach(function (q) { allQ.push(q); });
    });
    if (!allQ.length) return;

    var bar = document.createElement("div");
    bar.className = "tk-quiz-card";
    bar.innerHTML =
      '<div class="tk-meta-row"><strong>وضع الاختبار السريع للدرس (' + allQ.length + ' أسئلة)</strong>' +
      '<button type="button" class="tk-btn tk-btn-primary" id="tkStartTimedBtn">بدء اختبار مؤقّت (دقيقتان)</button></div>' +
      '<div id="tkTimedTimer" style="font-weight:700;color:var(--warn);"></div>' +
      '<div id="tkTimedHost"></div>';
    mount.appendChild(bar);

    var startBtn = document.getElementById("tkStartTimedBtn");
    var timerEl = document.getElementById("tkTimedTimer");
    var hostEl = document.getElementById("tkTimedHost");
    var timerHandle = null;

    startBtn.addEventListener("click", function () {
      clearInterval(timerHandle);
      var sec = 120;
      timerEl.textContent = "الوقت المتبقي: 02:00";
      renderQuestionsInto(hostEl, allQ, ctx, true);
      timerHandle = setInterval(function () {
        sec--;
        var m = String(Math.floor(sec / 60)).padStart(2, "0");
        var s = String(sec % 60).padStart(2, "0");
        timerEl.textContent = "الوقت المتبقي: " + m + ":" + s;
        if (sec <= 0) {
          clearInterval(timerHandle);
          timerEl.textContent = "انتهى وقت الاختبار! يمكنك مراجعة الإجابات الآن.";
        }
      }, 1000);
    });
  }

  global.ThakerQuiz = {
    renderQuestionCard: renderQuestionCard,
    renderQuestionsInto: renderQuestionsInto,
    renderActivityCard: renderActivityCard,
    renderTimedExamPanel: renderTimedExamPanel,
    highlightEvidence: highlightEvidence
  };
})(window);
