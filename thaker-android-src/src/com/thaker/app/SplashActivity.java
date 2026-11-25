package com.thaker.app;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.view.View;

public class SplashActivity extends Activity {
    private boolean navigated = false;
    private final Handler handler = new Handler(Looper.getMainLooper());
    private final Runnable autoAdvance = new Runnable() {
        @Override
        public void run() {
            goNext();
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);

        View root = findViewById(R.id.splash_root);
        if (root != null) {
            root.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    goNext();
                }
            });
        }
        handler.postDelayed(autoAdvance, 1400);
    }

    private void goNext() {
        if (navigated) return;
        navigated = true;
        handler.removeCallbacks(autoAdvance);
        Class<?> target = ThakerStore.isOnboarded(this) ? MainActivity.class : OnboardingActivity.class;
        startActivity(new Intent(this, target));
        overridePendingTransition(android.R.anim.fade_in, android.R.anim.fade_out);
        finish();
    }

    @Override
    protected void onDestroy() {
        handler.removeCallbacks(autoAdvance);
        super.onDestroy();
    }
}
