/* 3-Path Offline Pronunciation Controller: Piper OGG -> Android ThakerBridge.speak -> Web Speech API */
(function (global) {
  "use strict";

  var currentAudio = null;
  var toastTimer = null;

  function showToast(msg) {
    var el = document.getElementById("tkToast");
    if (!el) return;
    el.textContent = msg;
    el.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      el.classList.remove("show");
    }, 3400);
  }

  function stopAll() {
    if (currentAudio) {
      try {
        currentAudio.pause();
        currentAudio.currentTime = 0;
      } catch (e) {}
      currentAudio = null;
    }
    if (global.speechSynthesis && typeof global.speechSynthesis.cancel === "function") {
      try { global.speechSynthesis.cancel(); } catch (e) {}
    }
  }

  function playPath3WebSpeech(text, lang) {
    if (!global.speechSynthesis || typeof global.SpeechSynthesisUtterance !== "function") {
      showToast("تعذّر تشغيل النطق التلقائي: محرك النطق غير متوفر على هذا الجهاز.");
      return false;
    }
    try {
      var voices = global.speechSynthesis.getVoices ? global.speechSynthesis.getVoices() : [];
      var targetPrefix = String(lang || "en").split("-")[0].toLowerCase();
      var hasMatch = voices.length === 0 || voices.some(function (v) {
        return v.lang && v.lang.toLowerCase().indexOf(targetPrefix) === 0;
      });
      if (!hasMatch && voices.length > 0) {
        showToast("لم يُعثر على صوت مفعّل للغة المطلوبة (" + lang + ") في إعدادات الجهاز.");
        return false;
      }
      var u = new global.SpeechSynthesisUtterance(text);
      u.lang = lang || "en-GB";
      u.rate = 0.92;
      u.onerror = function () {
        showToast("تعذّر تشغيل النطق التلقائي: محرك النطق غير متوفر أو يحتاج تفعيل TTS.");
      };
      global.speechSynthesis.speak(u);
      return true;
    } catch (e) {
      showToast("تعذّر تشغيل النطق التلقائي على هذا المتصفح.");
      return false;
    }
  }

  function playPath2AndroidBridge(text, lang) {
    try {
      if (global.ThakerBridge && typeof global.ThakerBridge.speak === "function") {
        return Boolean(global.ThakerBridge.speak(String(text), String(lang || "en-GB")));
      }
    } catch (e) {}
    return false;
  }

  function speak(text, audioSrc, lang) {
    var cleanText = String(text || "").trim();
    var targetLang = lang || "en-GB";
    stopAll();

    // Path 1: Pre-generated Piper .ogg (Opus) offline asset
    if (audioSrc) {
      try {
        var audio = new Audio(audioSrc);
        currentAudio = audio;
        var fellBack = false;
        var fallback = function () {
          if (fellBack) return;
          fellBack = true;
          if (!playPath2AndroidBridge(cleanText, targetLang)) {
            playPath3WebSpeech(cleanText, targetLang);
          }
        };
        audio.onerror = fallback;
        var p = audio.play();
        if (p && typeof p.catch === "function") {
          p.catch(fallback);
        }
        return "piper_ogg";
      } catch (e) { /* fall through */ }
    }

    // Path 2: Native Android TextToSpeech via ThakerBridge.speak(text, lang)
    if (playPath2AndroidBridge(cleanText, targetLang)) {
      return "android_tts";
    }

    // Path 3: Web Speech API fallback with clear Arabic notice
    playPath3WebSpeech(cleanText, targetLang);
    return "web_speech";
  }

  global.ThakerSpeech = {
    speak: speak,
    stopAll: stopAll,
    showToast: showToast
  };
})(window);
