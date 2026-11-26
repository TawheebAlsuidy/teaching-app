/* Offline Storage Layer: IndexedDB + localStorage fallback + Android ThakerBridge sync */
(function (global) {
  "use strict";

  var DB_NAME = "thaker_books_db";
  var DB_VER = 1;
  var STORE_NAME = "kv";
  var LS_PREFIX = "thaker_book_v3_";
  var dbPromise = null;
  var memoryCache = {};

  function openDb() {
    if (dbPromise) return dbPromise;
    dbPromise = new Promise(function (resolve) {
      if (!global.indexedDB || (global.location && global.location.protocol === "file:")) {
        resolve(null);
        return;
      }
      var settled = false;
      var timer = setTimeout(function () {
        if (!settled) { settled = true; resolve(null); }
      }, 250);
      try {
        var req = global.indexedDB.open(DB_NAME, DB_VER);
        req.onupgradeneeded = function (ev) {
          var db = ev.target.result;
          if (!db.objectStoreNames.contains(STORE_NAME)) {
            db.createObjectStore(STORE_NAME);
          }
        };
        req.onsuccess = function (ev) {
          if (!settled) { settled = true; clearTimeout(timer); resolve(ev.target.result); }
        };
        req.onerror = function () {
          if (!settled) { settled = true; clearTimeout(timer); resolve(null); }
        };
        req.onblocked = function () {
          if (!settled) { settled = true; clearTimeout(timer); resolve(null); }
        };
      } catch (e) {
        if (!settled) { settled = true; clearTimeout(timer); resolve(null); }
      }
    });
    return dbPromise;
  }

  function lsGet(key, fallback) {
    try {
      var raw = global.localStorage.getItem(LS_PREFIX + key);
      return raw ? JSON.parse(raw) : fallback;
    } catch (e) {
      return memoryCache[key] !== undefined ? memoryCache[key] : fallback;
    }
  }

  function lsSet(key, val) {
    memoryCache[key] = val;
    try {
      global.localStorage.setItem(LS_PREFIX + key, JSON.stringify(val));
    } catch (e) { /* quota or private mode */ }
  }

  async function idbGet(key, fallback) {
    var local = lsGet(key, undefined);
    var db = await openDb();
    if (!db) return local !== undefined ? local : fallback;
    return new Promise(function (resolve) {
      try {
        var tx = db.transaction(STORE_NAME, "readonly");
        var req = tx.objectStore(STORE_NAME).get(key);
        req.onsuccess = function () {
          if (req.result !== undefined) {
            resolve(req.result);
          } else {
            resolve(local !== undefined ? local : fallback);
          }
        };
        req.onerror = function () {
          resolve(local !== undefined ? local : fallback);
        };
      } catch (e) {
        resolve(local !== undefined ? local : fallback);
      }
    });
  }

  async function idbSet(key, val) {
    lsSet(key, val);
    var db = await openDb();
    if (!db) return;
    try {
      var tx = db.transaction(STORE_NAME, "readwrite");
      tx.objectStore(STORE_NAME).put(val, key);
    } catch (e) { /* ignore */ }
  }

  function defaultState(subject) {
    return {
      subject: subject,
      lastLessonId: null,
      lastPage: 1,
      mode: "study",
      theme: "light",
      fontScale: 1,
      useAmiri: false,
      bookmarks: {},
      highlights: {},
      notes: {},
      quizResults: {},
      leitner: {},
      completedLessons: {}
    };
  }

  var stateCache = null;

  async function loadState(subject) {
    var base = defaultState(subject);
    var saved = await idbGet("state_" + subject, null);
    stateCache = Object.assign({}, base, saved || {});
    return stateCache;
  }

  async function saveState(subject, nextState) {
    stateCache = nextState;
    await idbSet("state_" + subject, nextState);
  }

  function syncAndroidBridge(bookTitle, pageNum, pct, unitId, sectionTitle) {
    try {
      if (global.ThakerBridge && typeof global.ThakerBridge.updateProgress === "function") {
        global.ThakerBridge.updateProgress(
          String(bookTitle || ""),
          Number(pageNum || 1),
          Math.max(0, Math.min(100, Math.round(pct || 0))),
          String(unitId || ""),
          String(sectionTitle || "")
        );
      }
    } catch (e) { /* safe fallback outside Android */ }
  }

  global.ThakerStorage = {
    loadState: loadState,
    saveState: saveState,
    syncAndroidBridge: syncAndroidBridge,
    getSync: function () { return stateCache; }
  };
})(window);
