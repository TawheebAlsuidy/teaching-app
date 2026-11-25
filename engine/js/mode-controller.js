/* Mode, Theme, Typography & Top Bar Controller */
(function (global) {
  "use strict";

  var MODES = ["read", "study", "practice"];
  var THEMES = ["light", "sepia", "dark"];

  function applyVisualState(state) {
    document.body.setAttribute("data-mode", MODES.indexOf(state.mode) >= 0 ? state.mode : "study");
    document.documentElement.setAttribute("data-theme", THEMES.indexOf(state.theme) >= 0 ? state.theme : "light");
    document.documentElement.style.setProperty("--scale", String(state.fontScale || 1));
    document.body.classList.toggle("use-amiri", Boolean(state.useAmiri));

    document.querySelectorAll("[data-set-mode]").forEach(function (btn) {
      var active = btn.getAttribute("data-set-mode") === state.mode;
      btn.classList.toggle("active", active);
      btn.setAttribute("aria-pressed", active ? "true" : "false");
    });

    var themeBtn = document.getElementById("tkThemeBtn");
    if (themeBtn) {
      var labels = { light: "نهار", sepia: "ورق", dark: "ليلي" };
      themeBtn.textContent = labels[state.theme] || "نهار";
    }
  }

  function initController(ctx) {
    applyVisualState(ctx.state);

    document.querySelectorAll("[data-set-mode]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        ctx.state.mode = btn.getAttribute("data-set-mode");
        applyVisualState(ctx.state);
        ctx.persistState();
      });
    });

    var themeBtn = document.getElementById("tkThemeBtn");
    if (themeBtn) {
      themeBtn.addEventListener("click", function () {
        var idx = THEMES.indexOf(ctx.state.theme);
        ctx.state.theme = THEMES[(idx + 1) % THEMES.length];
        applyVisualState(ctx.state);
        ctx.persistState();
      });
    }

    var fontPlus = document.getElementById("tkFontPlus");
    var fontMinus = document.getElementById("tkFontMinus");
    if (fontPlus) {
      fontPlus.addEventListener("click", function () {
        ctx.state.fontScale = Math.min(1.45, Math.round(((ctx.state.fontScale || 1) + 0.1) * 10) / 10);
        applyVisualState(ctx.state);
        ctx.persistState();
      });
    }
    if (fontMinus) {
      fontMinus.addEventListener("click", function () {
        ctx.state.fontScale = Math.max(0.85, Math.round(((ctx.state.fontScale || 1) - 0.1) * 10) / 10);
        applyVisualState(ctx.state);
        ctx.persistState();
      });
    }
  }

  global.ThakerMode = {
    init: initController,
    applyVisualState: applyVisualState
  };
})(window);
