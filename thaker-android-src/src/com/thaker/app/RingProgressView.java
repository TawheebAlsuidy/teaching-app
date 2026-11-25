package com.thaker.app;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.RectF;
import android.view.View;

public class RingProgressView extends View {
    private int progress = 0;
    private int max = 100;
    private String centerText = "0%";
    private int ringColor = 0xFF059669;
    private int trackColor = 0xFFDCE8E0;
    private int textColor = 0xFF0F291E;

    private final Paint trackPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final Paint arcPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final Paint textPaint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final RectF arcBounds = new RectF();

    public RingProgressView(Context context) {
        super(context);
        float dp = context.getResources().getDisplayMetrics().density;
        trackPaint.setStyle(Paint.Style.STROKE);
        trackPaint.setStrokeWidth(6.5f * dp);
        trackPaint.setStrokeCap(Paint.Cap.ROUND);

        arcPaint.setStyle(Paint.Style.STROKE);
        arcPaint.setStrokeWidth(6.5f * dp);
        arcPaint.setStrokeCap(Paint.Cap.ROUND);

        textPaint.setTextAlign(Paint.Align.CENTER);
        textPaint.setTextSize(14f * dp);
        textPaint.setFakeBoldText(true);
    }

    public void configure(int progress, int max, String label, int ringColor, int textColor) {
        this.progress = Math.max(0, progress);
        this.max = Math.max(1, max);
        this.centerText = label != null ? label : (progress + "%");
        this.ringColor = ringColor;
        this.textColor = textColor;
        invalidate();
    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        float w = getWidth();
        float h = getHeight();
        float stroke = arcPaint.getStrokeWidth();
        float pad = stroke / 2f + 2f;
        arcBounds.set(pad, pad, w - pad, h - pad);

        trackPaint.setColor(trackColor);
        arcPaint.setColor(ringColor);
        textPaint.setColor(textColor);

        canvas.drawOval(arcBounds, trackPaint);
        float sweep = 360f * Math.min(progress, max) / (float) max;
        canvas.drawArc(arcBounds, -90f, sweep, false, arcPaint);

        Paint.FontMetrics fm = textPaint.getFontMetrics();
        float ty = h / 2f - (fm.ascent + fm.descent) / 2f;
        canvas.drawText(centerText, w / 2f, ty, textPaint);
    }
}
