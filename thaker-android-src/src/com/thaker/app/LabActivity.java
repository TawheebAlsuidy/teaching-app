package com.thaker.app;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;
import android.webkit.JavascriptInterface;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;

public class LabActivity extends Activity {

    private WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);

        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED, WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED);

        enableImmersiveMode();
        setContentView(R.layout.activity_lab);

        webView = findViewById(R.id.lab_webview);
        setupWebView();

        View btnExit = findViewById(R.id.btn_exit_to_hub);
        if (btnExit != null) {
            btnExit.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    confirmExit();
                }
            });
        }
    }

    private void enableImmersiveMode() {
        View decorView = getWindow().getDecorView();
        decorView.setSystemUiVisibility(
            View.SYSTEM_UI_FLAG_LAYOUT_STABLE
            | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
            | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
            | View.SYSTEM_UI_FLAG_FULLSCREEN
            | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
            | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
        );
    }

    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        if (hasFocus) {
            enableImmersiveMode();
        }
    }

    private void setupWebView() {
        WebSettings ws = webView.getSettings();
        ws.setJavaScriptEnabled(true);
        ws.setDomStorageEnabled(true);
        ws.setDatabaseEnabled(true);
        ws.setAllowFileAccess(true);
        ws.setAllowContentAccess(true);
        ws.setAllowFileAccessFromFileURLs(true);
        ws.setAllowUniversalAccessFromFileURLs(true);
        ws.setMediaPlaybackRequiresUserGesture(false);
        ws.setBuiltInZoomControls(false);
        ws.setDisplayZoomControls(false);
        ws.setSupportZoom(true);
        ws.setUseWideViewPort(true);
        ws.setLoadWithOverviewMode(true);
        ws.setCacheMode(WebSettings.LOAD_NO_CACHE);

        webView.clearCache(true);
        webView.setLayerType(View.LAYER_TYPE_HARDWARE, null);
        webView.setWebChromeClient(new WebChromeClient());
        webView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                return false;
            }
        });

        webView.addJavascriptInterface(new Object() {
            @JavascriptInterface
            public void returnToHome() {
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        returnToMain();
                    }
                });
            }
        }, "ThakerBridge");

        String htmlAsset = getIntent().getStringExtra("html_asset");
        if (htmlAsset == null || htmlAsset.isEmpty() || htmlAsset.contains("/") || htmlAsset.contains("..")) {
            htmlAsset = "chem-lab-book.html";
        }
        webView.loadUrl("file:///android_asset/" + htmlAsset);
    }

    private void returnToMain() {
        Intent intent = new Intent(LabActivity.this, MainActivity.class);
        intent.putExtra("no_auto_launch", true);
        intent.addFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP);
        startActivity(intent);
        finish();
    }

    private void confirmExit() {
        returnToMain();
    }

    @Override
    public void onBackPressed() {
        returnToMain();
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (webView != null) webView.onResume();
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (webView != null) webView.onPause();
    }

    @Override
    protected void onDestroy() {
        if (webView != null) webView.destroy();
        super.onDestroy();
    }
}
