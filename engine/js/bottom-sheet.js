/* 6-Tab Interactive Bottom Sheet + Reference Page Zoom Viewer */
(function (global) {
  "use strict";

  var TABS = [
    { key: "simple_explain", label: "شرح مبسّط" },
    { key: "diagram", label: "رسم" },
    { key: "simulation", label: "محاكاة / تجربة" },
    { key: "example", label: "مثال" },
    { key: "self_check", label: "اختبر نفسك" },
    { key: "page_ref", label: "مرجع الصفحة" }
  ];

  var currentCtx = null;
  var currentPayload = null;
  var currentTab = "simple_explain";

  function escHtml(s) {
    return String(s || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function originPill(origin) {
    var map = {
      from_book: ["من الكتاب", "tk-origin-from_book"],
      educational_addition: ["إضافة تعليمية", "tk-origin-educational_addition"],
      for_enrichment: ["للتوسع", "tk-origin-for_enrichment"],
      proposed_solution: ["حل مقترح", "tk-origin-proposed_solution"]
    };
    var item = map[origin] || map.educational_addition;
    return '<span class="tk-origin ' + item[1] + '">' + item[0] + "</span>";
  }

  function openSheet(ctx, payload, initialTab) {
    currentCtx = ctx;
    currentPayload = payload;
    currentTab = initialTab || "simple_explain";
    renderSheet();
    document.getElementById("tkBackdrop").classList.add("open");
    document.getElementById("tkSheet").classList.add("open");
  }

  function closeSheet() {
    document.getElementById("tkBackdrop").classList.remove("open");
    document.getElementById("tkSheet").classList.remove("open");
  }

  function renderTabBody(tabKey) {
    var tabsData = (currentPayload && currentPayload.tabs) || {};
    var body = document.getElementById("tkSheetBody");
    body.innerHTML = "";

    if (tabKey === "simple_explain") {
      var se = tabsData.simple_explain;
      if (!se) {
        body.innerHTML = '<p>لا يوجد شرح إضافي لهذا المقطع.</p>';
        return;
      }
      body.innerHTML =
        '<div class="tk-meta-row"><div class="tk-tag-group">' +
        originPill(se.origin || "educational_addition") +
        '<span class="tk-page-badge">مرجع ص ' + escHtml(se.page_ref || 1) + "</span></div></div>" +
        '<div class="tk-content-body" dir="rtl">' + se.html + "</div>";
      return;
    }

    if (tabKey === "diagram") {
      var dg = tabsData.diagram;
      if (!dg) {
        body.innerHTML = "<p>لا يوجد رسم توضيحي إضافي لهذا البند.</p>";
        return;
      }
      body.innerHTML =
        '<div class="tk-meta-row"><div class="tk-tag-group">' +
        originPill(dg.origin || "educational_addition") +
        '<span class="tk-page-badge">مرجع ص ' + escHtml(dg.page_ref || 1) + "</span></div></div>" +
        '<div style="background:#fff;border:1px solid var(--stroke);border-radius:12px;padding:10px;overflow-x:auto;">' +
        (dg.svg || "") + "</div>" +
        (dg.caption ? '<p style="margin-top:8px;font-size:13.5px;color:var(--muted)">' + escHtml(dg.caption) + "</p>" : "");
      return;
    }

    if (tabKey === "simulation") {
      var sim = tabsData.simulation;
      if (!sim) {
        body.innerHTML = "<p>لا توجد محاكاة مرتبطة بهذه الكتلة؛ يمكنك استكشاف التجارب في قسم الأنشطة.</p>";
        return;
      }
      body.innerHTML =
        '<div class="tk-meta-row"><div class="tk-tag-group">' +
        originPill(sim.origin || "educational_addition") +
        '<span class="tk-page-badge">نشاط تفاعلي · ص ' + escHtml(sim.page_ref || 1) + "</span></div></div>" +
        '<div id="tkSimMount"></div>';
      var mount = document.getElementById("tkSimMount");
      if (global.ThakerSubjectEnglish && typeof global.ThakerSubjectEnglish.renderSimulation === "function") {
        global.ThakerSubjectEnglish.renderSimulation(mount, sim, currentCtx);
      }
      return;
    }

    if (tabKey === "example") {
      var ex = tabsData.example;
      if (!ex) {
        body.innerHTML = "<p>لا يوجد مثال إضافي مسجل لهذه النقطة.</p>";
        return;
      }
      body.innerHTML =
        '<div class="tk-meta-row"><div class="tk-tag-group">' +
        originPill(ex.origin || "educational_addition") +
        '<span class="tk-page-badge">مرجع ص ' + escHtml(ex.page_ref || 1) + "</span></div></div>" +
        '<div class="tk-content-body">' + ex.html + "</div>";
      return;
    }

    if (tabKey === "self_check") {
      var chkId = tabsData.self_check_ref;
      var checks = (currentCtx && currentCtx.lesson && currentCtx.lesson.section_checks) || [];
      var targetCheck = checks.find(function (c) { return c.id === chkId; }) || checks[0];
      if (!targetCheck || !targetCheck.questions || !targetCheck.questions.length) {
        body.innerHTML = "<p>اختبر نفسك متاح أسفل الدرس في تبويب الاختبارات.</p>";
        return;
      }
      body.innerHTML =
        '<div class="tk-meta-row"><div class="tk-tag-group">' +
        originPill(targetCheck.origin || "educational_addition") +
        '<span class="tk-page-badge">تحقّق فوري · ص ' + escHtml(targetCheck.page_ref || 1) + "</span></div></div>" +
        '<div id="tkSheetQuizMount"></div>';
      if (global.ThakerQuiz) {
        global.ThakerQuiz.renderQuestionsInto(document.getElementById("tkSheetQuizMount"), targetCheck.questions, currentCtx, false);
      }
      return;
    }

    if (tabKey === "page_ref") {
      var pr = tabsData.page_ref;
      if (!pr || !pr.image) {
        body.innerHTML = "<p>صورة مرجع الصفحة غير متوفرة.</p>";
        return;
      }
      body.innerHTML =
        '<div class="tk-meta-row"><div class="tk-tag-group">' +
        originPill("from_book") +
        '<span class="tk-page-badge">' + escHtml(pr.book || "PB") + " · ص " + escHtml(pr.page || 1) +
        (pr.pdf_page ? " (PDF ص " + escHtml(pr.pdf_page) + ")" : "") + "</span></div>" +
        '<button type="button" class="tk-btn" id="tkToggleZoomBtn">تكبير الصفحة</button></div>' +
        '<div class="tk-ref-img-wrap" id="tkRefZoomBox"><img src="' + escHtml(pr.image) + '" alt="مرجع صفحة الكتاب"></div>';
      var zoomBtn = document.getElementById("tkToggleZoomBtn");
      var box = document.getElementById("tkRefZoomBox");
      if (zoomBtn && box) {
        zoomBtn.addEventListener("click", function () {
          var z = box.classList.toggle("zoomed");
          zoomBtn.textContent = z ? "تصغير الصفحة" : "تكبير الصفحة";
        });
      }
    }
  }

  function renderSheet() {
    var titleEl = document.getElementById("tkSheetTitle");
    var tabsEl = document.getElementById("tkSheetTabs");
    titleEl.textContent = (currentPayload && currentPayload.label) || "تفاصيل تعليمية";
    tabsEl.innerHTML = "";
    TABS.forEach(function (t) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "tk-tab-btn" + (t.key === currentTab ? " active" : "");
      btn.textContent = t.label;
      btn.addEventListener("click", function () {
        currentTab = t.key;
        renderSheet();
      });
      tabsEl.appendChild(btn);
    });
    renderTabBody(currentTab);
  }

  function initEvents() {
    var backdrop = document.getElementById("tkBackdrop");
    var closeBtn = document.getElementById("tkSheetClose");
    if (backdrop) backdrop.addEventListener("click", closeSheet);
    if (closeBtn) closeBtn.addEventListener("click", closeSheet);
  }

  global.ThakerSheet = {
    init: initEvents,
    open: openSheet,
    close: closeSheet
  };
})(window);
