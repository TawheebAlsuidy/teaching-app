package com.thaker.app;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.os.Bundle;
import android.speech.tts.TextToSpeech;
import android.view.View;
import android.webkit.JavascriptInterface;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import java.util.Locale;

public class LabActivity extends Activity {

    private WebView webView;
    private String htmlAsset = "thaker-interactive-book.html";
    private TextToSpeech tts;
    private volatile boolean ttsReady = false;

    @SuppressLint({"SetJavaScriptEnabled", "JavascriptInterface"})
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lab);

        tts = new TextToSpeech(this, new TextToSpeech.OnInitListener() {
            @Override
            public void onInit(int status) {
                ttsReady = (status == TextToSpeech.SUCCESS);
            }
        });

        String requested = getIntent().getStringExtra("html_asset");
        if (requested != null && !requested.trim().isEmpty()) {
            htmlAsset = requested.trim();
        }
        int startPage = getIntent().getIntExtra("start_page", 0);
        String startTab = getIntent().getStringExtra("start_tab");

        ThakerStore.unlockLabBadge(this);

        webView = findViewById(R.id.webview);
        WebSettings ws = webView.getSettings();
        ws.setJavaScriptEnabled(true);
        ws.setDomStorageEnabled(true);
        ws.setAllowFileAccess(true);
        ws.setAllowFileAccessFromFileURLs(true);
        ws.setAllowUniversalAccessFromFileURLs(true);
        ws.setBuiltInZoomControls(true);
        ws.setDisplayZoomControls(false);
        ws.setUseWideViewPort(true);
        ws.setLoadWithOverviewMode(true);
        webView.setLayerType(View.LAYER_TYPE_HARDWARE, null);

        webView.addJavascriptInterface(new Object() {
            @JavascriptInterface
            public void returnToHome() {
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        finish();
                    }
                });
            }

            @JavascriptInterface
            public void updateProgress(String bookTitle, int pageNum, int pct, String unitId, String sectionTitle) {
                String cleanTitle = (bookTitle != null && !bookTitle.trim().isEmpty()) ? bookTitle.trim() : getBookTitleForAsset(htmlAsset);
                String sub = (sectionTitle != null && !sectionTitle.trim().isEmpty())
                        ? (sectionTitle.trim() + " · صفحة " + pageNum)
                        : ("صفحة " + pageNum);
                ThakerStore.saveReadingProgress(LabActivity.this, assetToKey(htmlAsset), cleanTitle, sub, "html", htmlAsset, pageNum, pct);
                if (unitId != null && !unitId.trim().isEmpty()) {
                    int lvl = pct >= 70 ? 3 : (pct >= 25 ? 2 : 1);
                    ThakerStore.setUnitMastery(LabActivity.this, unitId.trim(), Math.max(lvl, ThakerStore.getUnitMastery(LabActivity.this, unitId.trim(), 0)));
                }
            }

            @JavascriptInterface
            public boolean isTtsAvailable() {
                return ttsReady && tts != null;
            }

            @JavascriptInterface
            public boolean speak(final String text, final String lang) {
                if (!ttsReady || tts == null || text == null || text.trim().isEmpty()) {
                    return false;
                }
                final String tag = (lang == null || lang.trim().isEmpty()) ? "en-GB" : lang.trim();
                final Locale loc = Locale.forLanguageTag(tag.replace('_', '-'));
                int res = tts.setLanguage(loc);
                if (res == TextToSpeech.LANG_MISSING_DATA || res == TextToSpeech.LANG_NOT_SUPPORTED) {
                    if (tag.toLowerCase(Locale.US).startsWith("en")) {
                        res = tts.setLanguage(Locale.US);
                    }
                }
                if (res == TextToSpeech.LANG_MISSING_DATA || res == TextToSpeech.LANG_NOT_SUPPORTED) {
                    return false;
                }
                tts.speak(text.trim(), TextToSpeech.QUEUE_FLUSH, null, "thaker_tts");
                return true;
            }
        }, "ThakerBridge");

        webView.setWebViewClient(new WebViewClient());
        webView.setWebChromeClient(new WebChromeClient());

        StringBuilder url = new StringBuilder("file:///android_asset/").append(htmlAsset);
        if (startPage > 0 || (startTab != null && !startTab.isEmpty())) {
            url.append("#");
            boolean needAmp = false;
            if (startPage > 0) {
                url.append("page=").append(startPage);
                needAmp = true;
            }
            if (startTab != null && !startTab.isEmpty()) {
                if (needAmp) url.append("&");
                url.append("tab=").append(startTab);
            }
        }
        webView.loadUrl(url.toString());
    }

    private String assetToKey(String asset) {
        if (asset.contains("thaker-interactive")) return "sci_p2";
        if (asset.contains("science-9th")) return "sci_p1_lab";
        if (asset.contains("math-9th")) return "math_lab";
        if (asset.contains("physics-12th")) return "phys_12";
        if (asset.contains("biology-12th")) return "bio_12";
        if (asset.contains("chemistry-12th") || asset.contains("chem-lab")) return "chem_12";
        return "chem_12";
    }

    private String getBookTitleForAsset(String asset) {
        if (asset.contains("thaker-interactive")) return "العلوم - الجزء الثاني";
        if (asset.contains("science-9th")) return "العلوم 3D - الصف التاسع";
        if (asset.contains("math-9th")) return "الرياضيات 3D - الصف التاسع";
        if (asset.contains("physics-12th")) return "الفيزياء - الثالث الثانوي";
        if (asset.contains("biology-12th")) return "الأحياء - الثالث الثانوي";
        if (asset.contains("chem-lab")) return "مختبر الكيمياء 3D - الثالث الثانوي";
        return "الكيمياء - الثالث الثانوي";
    }

    @Override
    public void onBackPressed() {
        if (webView != null && webView.canGoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (tts != null) tts.stop();
        if (webView != null) webView.onPause();
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (webView != null) webView.onResume();
    }

    @Override
    protected void onDestroy() {
        if (tts != null) {
            tts.stop();
            tts.shutdown();
        }
        if (webView != null) webView.destroy();
        super.onDestroy();
    }
}
