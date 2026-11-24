package com.thaker.app;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.graphics.Bitmap;
import android.graphics.Matrix;
import android.graphics.PointF;
import android.graphics.pdf.PdfRenderer;
import android.os.Bundle;
import android.os.Environment;
import android.os.Handler;
import android.os.Looper;
import android.os.ParcelFileDescriptor;
import android.view.GestureDetector;
import android.view.MotionEvent;
import android.view.ScaleGestureDetector;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.SeekBar;
import android.widget.TextView;
import android.widget.Toast;

import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class BookViewerActivity extends Activity {

    private String bookKey = "sci_p1";
    private int curPageIndex = 0;
    private int totalPages = 1;

    private ParcelFileDescriptor pfd;
    private PdfRenderer renderer;
    private ExecutorService renderExecutor;
    private Handler mainHandler;

    private ImageView imageView;
    private ProgressBar progressBar;
    private View topToolbar;
    private View bottomToolbar;
    private TextView tvBookTitle;
    private TextView tvUnitName;
    private TextView tvPageIndicator;
    private SeekBar pageSeekBar;

    // Zoom & Pan Matrix
    private Matrix matrix = new Matrix();
    private Matrix savedMatrix = new Matrix();
    private static final int MODE_NONE = 0;
    private static final int MODE_DRAG = 1;
    private static final int MODE_ZOOM = 2;
    private int touchMode = MODE_NONE;
    private PointF startPoint = new PointF();
    private PointF midPoint = new PointF();
    private float oldDist = 1f;
    private float currentScale = 1f;

    private ScaleGestureDetector scaleDetector;
    private GestureDetector gestureDetector;
    private boolean toolbarsVisible = true;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtil.apply(this);
        super.onCreate(savedInstanceState);

        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED, WindowManager.LayoutParams.FLAG_HARDWARE_ACCELERATED);

        setContentView(R.layout.activity_book_viewer);

        bookKey = getIntent().getStringExtra("book_key");
        if (bookKey == null) bookKey = "sci_p1";
        curPageIndex = getIntent().getIntExtra("start_page", 0);

        renderExecutor = Executors.newSingleThreadExecutor();
        mainHandler = new Handler(Looper.getMainLooper());

        imageView = findViewById(R.id.pdf_image_view);
        progressBar = findViewById(R.id.pdf_progress);
        topToolbar = findViewById(R.id.top_toolbar);
        bottomToolbar = findViewById(R.id.bottom_toolbar);
        tvBookTitle = findViewById(R.id.tv_viewer_book_title);
        tvUnitName = findViewById(R.id.tv_viewer_unit_name);
        tvPageIndicator = findViewById(R.id.tv_page_indicator);
        pageSeekBar = findViewById(R.id.page_seekbar);

        tvBookTitle.setText(getBookDisplayName(bookKey));

        setupGestures();
        setupControls();
        openPdfDocument();
    }

    private String getBookDisplayName(String key) {
        if ("sci_p1".equals(key)) return "علوم - الجزء الأول (الصف التاسع)";
        if ("sci_p2".equals(key)) return "علوم - الجزء الثاني (الصف التاسع)";
        if ("math_p1".equals(key)) return "رياضيات - الجزء الأول (الصف التاسع)";
        if ("math_p2".equals(key)) return "رياضيات - الجزء الثاني (الصف التاسع)";
        return "كتاب المنهج المدرسي";
    }

    private String getBookFileName(String key) {
        if ("sci_p1".equals(key)) return "science_part1_9th.pdf";
        if ("sci_p2".equals(key)) return "science_part2_9th.pdf";
        if ("math_p1".equals(key)) return "mathematics_part1_9th.pdf";
        if ("math_p2".equals(key)) return "mathematics_part2_9th.pdf";
        return "science_part1_9th.pdf";
    }

    private File resolvePdfFile(String key) {
        String fn = getBookFileName(key);

        // 1. First priority: App private internal files (100% permission-free, guaranteed to work)
        File internalFile = new File(getFilesDir(), fn);
        if (internalFile.exists() && internalFile.length() > 50000) {
            return internalFile;
        }

        // 2. Extract from bundled APK assets into internal private files
        try {
            InputStream in = getAssets().open("curriculum/9th/" + fn);
            File tempFile = new File(getFilesDir(), fn + ".tmp");
            FileOutputStream out = new FileOutputStream(tempFile);
            byte[] buf = new byte[65536];
            int len;
            while ((len = in.read(buf)) > 0) {
                out.write(buf, 0, len);
            }
            in.close();
            out.flush();
            out.close();
            if (tempFile.exists() && tempFile.length() > 50000) {
                tempFile.renameTo(internalFile);
                return internalFile;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        // 3. Fallback: try external storage ONLY if test open succeeds without permission error
        try {
            File[] candidates = new File[]{
                new File("/mnt/sdcard/projects/teaching-app/المنهج/تاسع/" + fn),
                new File(Environment.getExternalStorageDirectory(), "projects/teaching-app/المنهج/تاسع/" + fn),
                new File("/sdcard/projects/teaching-app/المنهج/تاسع/" + fn)
            };
            for (File cand : candidates) {
                if (cand.exists() && cand.canRead()) {
                    ParcelFileDescriptor testPfd = ParcelFileDescriptor.open(cand, ParcelFileDescriptor.MODE_READ_ONLY);
                    testPfd.close();
                    return cand;
                }
            }
        } catch (Throwable ignored) {}

        return null;
    }

    private void openPdfDocument() {
        progressBar.setVisibility(View.VISIBLE);
        renderExecutor.execute(new Runnable() {
            @Override
            public void run() {
                try {
                    File file = resolvePdfFile(bookKey);
                    if (file == null || !file.exists()) {
                        mainHandler.post(new Runnable() {
                            @Override
                            public void run() {
                                progressBar.setVisibility(View.GONE);
                                Toast.makeText(BookViewerActivity.this, "تعذر العثور على ملف الكتاب في مجلد المنهج!", Toast.LENGTH_LONG).show();
                            }
                        });
                        return;
                    }

                    pfd = ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY);
                    renderer = new PdfRenderer(pfd);
                    totalPages = renderer.getPageCount();

                    if (curPageIndex < 0) curPageIndex = 0;
                    if (curPageIndex >= totalPages) curPageIndex = totalPages - 1;

                    mainHandler.post(new Runnable() {
                        @Override
                        public void run() {
                            progressBar.setVisibility(View.GONE);
                            pageSeekBar.setMax(Math.max(0, totalPages - 1));
                            pageSeekBar.setProgress(curPageIndex);
                            renderCurrentPage();
                        }
                    });
                } catch (final Exception e) {
                    mainHandler.post(new Runnable() {
                        @Override
                        public void run() {
                            progressBar.setVisibility(View.GONE);
                            Toast.makeText(BookViewerActivity.this, "خطأ أثناء فتح الكتاب: " + e.getMessage(), Toast.LENGTH_LONG).show();
                        }
                    });
                }
            }
        });
    }

    private void renderCurrentPage() {
        if (renderer == null || curPageIndex < 0 || curPageIndex >= totalPages) return;
        progressBar.setVisibility(View.VISIBLE);

        final int targetPage = curPageIndex;
        renderExecutor.execute(new Runnable() {
            @Override
            public void run() {
                try {
                    PdfRenderer.Page page = renderer.openPage(targetPage);
                    int screenW = getResources().getDisplayMetrics().widthPixels;
                    int screenH = getResources().getDisplayMetrics().heightPixels;

                    // Scale to fit screen width while keeping sharp resolution
                    int renderW = Math.max(screenW, page.getWidth() * 2);
                    int renderH = (int) ((float) renderW * page.getHeight() / page.getWidth());

                    final Bitmap bitmap = Bitmap.createBitmap(renderW, renderH, Bitmap.Config.ARGB_8888);
                    page.render(bitmap, null, null, PdfRenderer.Page.RENDER_MODE_FOR_DISPLAY);
                    page.close();

                    mainHandler.post(new Runnable() {
                        @Override
                        public void run() {
                            progressBar.setVisibility(View.GONE);
                            imageView.setImageBitmap(bitmap);
                            resetZoomMatrix(bitmap);
                            updateUiInfo();
                        }
                    });
                } catch (Exception e) {
                    e.printStackTrace();
                    mainHandler.post(new Runnable() {
                        @Override
                        public void run() {
                            progressBar.setVisibility(View.GONE);
                        }
                    });
                }
            }
        });
    }

    private void resetZoomMatrix(Bitmap bitmap) {
        if (bitmap == null) return;
        int viewW = imageView.getWidth();
        int viewH = imageView.getHeight();
        if (viewW <= 0 || viewH <= 0) {
            viewW = getResources().getDisplayMetrics().widthPixels;
            viewH = getResources().getDisplayMetrics().heightPixels;
        }

        matrix.reset();
        float scale = (float) viewW / bitmap.getWidth();
        matrix.postScale(scale, scale);
        float dy = (viewH - bitmap.getHeight() * scale) / 2f;
        if (dy > 0) matrix.postTranslate(0, dy);

        currentScale = 1f;
        imageView.setImageMatrix(matrix);
    }

    private void updateUiInfo() {
        tvPageIndicator.setText("صفحة " + (curPageIndex + 1) + " من " + totalPages);
        pageSeekBar.setProgress(curPageIndex);
        tvUnitName.setText(getUnitNameForPage(bookKey, curPageIndex + 1));
    }

    private String getUnitNameForPage(String key, int page) {
        if ("sci_p1".equals(key)) {
            if (page < 21) return "الوحدة 1: المحاليل وتطبيقاتها";
            if (page < 47) return "الوحدة 2: التفاعلات الكيميائية";
            if (page < 67) return "الوحدة 3: الصوت وانتقاله";
            if (page < 99) return "الوحدة 4: الضوء والرؤية";
            if (page < 125) return "الوحدة 5: الإخراج في الكائنات الحية";
            if (page < 151) return "الوحدة 6: التكاثر في الكائنات الحية";
            return "الوحدة 7: أمراض الجهازين البولي والتناسلي";
        } else if ("sci_p2".equals(key)) {
            if (page < 25) return "الوحدة 8: الكهرباء الساكنة والتيار";
            if (page < 55) return "الوحدة 9: المغناطيسية والكهرومغناطيسية";
            if (page < 81) return "الوحدة 10: الطاقة وتحولاتها";
            if (page < 105) return "الوحدة 11: البيئة والتوازن البيئي";
            if (page < 131) return "الوحدة 12: علوم الأرض والمعادن";
            return "الوحدة 13: الفضاء والنظام الشمسي";
        } else if ("math_p1".equals(key)) {
            if (page < 32) return "الوحدة 1: المجموعات والعلاقات";
            if (page < 40) return "الوحدة 2: التطبيقات";
            if (page < 61) return "الوحدة 3: مجموعة الأعداد الحقيقية R";
            if (page < 94) return "الوحدة 4: تحليل المقادير الجبرية";
            return "الوحدة 5: الكسور الجبرية والعمليات عليها";
        } else {
            if (page < 45) return "الوحدة 5: الهندسة المستوية (الدائرة)";
            if (page < 80) return "الوحدة 6: حساب المثلثات";
            if (page < 111) return "الوحدة 7: التحويلات الهندسية والتكبير";
            return "الوحدة 8: الإحصاء والاحتمالات";
        }
    }

    private void setupControls() {
        findViewById(R.id.btn_back_viewer).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });

        findViewById(R.id.btn_prev_page).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (curPageIndex > 0) {
                    curPageIndex--;
                    renderCurrentPage();
                }
            }
        });

        findViewById(R.id.btn_next_page).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (curPageIndex < totalPages - 1) {
                    curPageIndex++;
                    renderCurrentPage();
                }
            }
        });

        findViewById(R.id.btn_reset_zoom).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (imageView.getDrawable() != null) {
                    matrix.reset();
                    currentScale = 1f;
                    imageView.setImageMatrix(matrix);
                    Toast.makeText(BookViewerActivity.this, "تمت إعادة ضبط التكبير", Toast.LENGTH_SHORT).show();
                }
            }
        });

        findViewById(R.id.btn_open_unit_index).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showJumpUnitDialog();
            }
        });

        tvPageIndicator.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showJumpPageDialog();
            }
        });

        pageSeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                if (fromUser && progress >= 0 && progress < totalPages) {
                    curPageIndex = progress;
                    renderCurrentPage();
                }
            }
            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {}
            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {}
        });
    }

    private void setupGestures() {
        scaleDetector = new ScaleGestureDetector(this, new ScaleGestureDetector.SimpleOnScaleGestureListener() {
            @Override
            public boolean onScale(ScaleGestureDetector detector) {
                float factor = detector.getScaleFactor();
                currentScale *= factor;
                currentScale = Math.max(0.8f, Math.min(currentScale, 4.0f));
                matrix.postScale(factor, factor, detector.getFocusX(), detector.getFocusY());
                imageView.setImageMatrix(matrix);
                return true;
            }
        });

        gestureDetector = new GestureDetector(this, new GestureDetector.SimpleOnGestureListener() {
            @Override
            public boolean onSingleTapConfirmed(MotionEvent e) {
                toggleToolbars();
                return true;
            }

            @Override
            public boolean onDoubleTap(MotionEvent e) {
                if (currentScale > 1.2f) {
                    currentScale = 1.0f;
                    matrix.reset();
                } else {
                    currentScale = 2.0f;
                    matrix.postScale(2.0f, 2.0f, e.getX(), e.getY());
                }
                imageView.setImageMatrix(matrix);
                return true;
            }

            @Override
            public boolean onFling(MotionEvent e1, MotionEvent e2, float velocityX, float velocityY) {
                if (currentScale <= 1.1f && e1 != null && e2 != null) {
                    float diffX = e2.getX() - e1.getX();
                    if (diffX > 100 && curPageIndex > 0) {
                        curPageIndex--;
                        renderCurrentPage();
                        return true;
                    } else if (diffX < -100 && curPageIndex < totalPages - 1) {
                        curPageIndex++;
                        renderCurrentPage();
                        return true;
                    }
                }
                return false;
            }
        });

        imageView.setOnTouchListener(new View.OnTouchListener() {
            @Override
            public boolean onTouch(View v, MotionEvent event) {
                scaleDetector.onTouchEvent(event);
                gestureDetector.onTouchEvent(event);

                switch (event.getAction() & MotionEvent.ACTION_MASK) {
                    case MotionEvent.ACTION_DOWN:
                        savedMatrix.set(matrix);
                        startPoint.set(event.getX(), event.getY());
                        touchMode = MODE_DRAG;
                        break;
                    case MotionEvent.ACTION_POINTER_DOWN:
                        oldDist = spacing(event);
                        if (oldDist > 10f) {
                            savedMatrix.set(matrix);
                            midPoint(midPoint, event);
                            touchMode = MODE_ZOOM;
                        }
                        break;
                    case MotionEvent.ACTION_MOVE:
                        if (touchMode == MODE_DRAG && currentScale > 1.05f) {
                            matrix.set(savedMatrix);
                            matrix.postTranslate(event.getX() - startPoint.x, event.getY() - startPoint.y);
                            imageView.setImageMatrix(matrix);
                        }
                        break;
                    case MotionEvent.ACTION_UP:
                    case MotionEvent.ACTION_POINTER_UP:
                        touchMode = MODE_NONE;
                        break;
                }
                return true;
            }
        });
    }

    private float spacing(MotionEvent event) {
        float x = event.getX(0) - event.getX(1);
        float y = event.getY(0) - event.getY(1);
        return (float) Math.sqrt(x * x + y * y);
    }

    private void midPoint(PointF point, MotionEvent event) {
        float x = event.getX(0) + event.getX(1);
        float y = event.getY(0) + event.getY(1);
        point.set(x / 2, y / 2);
    }

    private void toggleToolbars() {
        toolbarsVisible = !toolbarsVisible;
        topToolbar.setVisibility(toolbarsVisible ? View.VISIBLE : View.GONE);
        bottomToolbar.setVisibility(toolbarsVisible ? View.VISIBLE : View.GONE);
    }

    private void showJumpPageDialog() {
        final EditText input = new EditText(this);
        input.setHint("أدخل رقم الصفحة (1 - " + totalPages + ")");
        input.setInputType(android.text.InputType.TYPE_CLASS_NUMBER);

        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("الانتقال إلى صفحة");
        builder.setView(input);
        builder.setPositiveButton("انتقال", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                try {
                    int p = Integer.parseInt(input.getText().toString().trim());
                    if (p >= 1 && p <= totalPages) {
                        curPageIndex = p - 1;
                        renderCurrentPage();
                    } else {
                        Toast.makeText(BookViewerActivity.this, "رقم الصفحة خارج النطاق!", Toast.LENGTH_SHORT).show();
                    }
                } catch (Exception ignored) {}
            }
        });
        builder.setNegativeButton("إلغاء", null);
        builder.show();
    }

    private void showJumpUnitDialog() {
        final String[] units;
        final int[] pages;

        if ("sci_p1".equals(bookKey)) {
            units = new String[]{
                "الوحدة 1: المحاليل وتطبيقاتها (ص 1)",
                "الوحدة 2: التفاعلات الكيميائية (ص 21)",
                "الوحدة 3: الصوت وانتقاله (ص 47)",
                "الوحدة 4: الضوء والرؤية (ص 67)",
                "الوحدة 5: الإخراج في الكائنات الحية (ص 99)",
                "الوحدة 6: التكاثر في الكائنات الحية (ص 125)",
                "الوحدة 7: أمراض الجهازين البولي والتناسلي (ص 151)"
            };
            pages = new int[]{1, 21, 47, 67, 99, 125, 151};
        } else if ("sci_p2".equals(bookKey)) {
            units = new String[]{
                "الوحدة 8: الكهرباء الساكنة والتيار (ص 1)",
                "الوحدة 9: المغناطيسية والكهرومغناطيسية (ص 25)",
                "الوحدة 10: الطاقة ومصادرها (ص 55)",
                "الوحدة 11: البيئة والتوازن البيئي (ص 81)",
                "الوحدة 12: علوم الأرض والمعادن (ص 105)",
                "الوحدة 13: الفضاء والنظام الشمسي (ص 131)"
            };
            pages = new int[]{1, 25, 55, 81, 105, 131};
        } else if ("math_p1".equals(bookKey)) {
            units = new String[]{
                "الوحدة 1: المجموعات والعلاقات (ص 7)",
                "الوحدة 2: التطبيقات وخواصها (ص 32)",
                "الوحدة 3: مجموعة الأعداد الحقيقية R (ص 40)",
                "الوحدة 4: تحليل المقادير الجبرية (ص 61)",
                "الوحدة 5: الكسور الجبرية والعمليات عليها (ص 94)",
                "تمارين عامة ومسائل وزارية (ص 160)"
            };
            pages = new int[]{7, 32, 40, 61, 94, 160};
        } else {
            units = new String[]{
                "الوحدة 5: الهندسة المستوية (الدائرة) (ص 5)",
                "الوحدة 6: حساب المثلثات (ص 45)",
                "الوحدة 7: التحويلات الهندسية والتكبير (ص 80)",
                "الوحدة 8: الإحصاء والاحتمالات (ص 111)"
            };
            pages = new int[]{5, 45, 80, 111};
        }

        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setTitle("فهرس الوحدات - اختر وحدة:");
        builder.setItems(units, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                curPageIndex = pages[which] - 1;
                renderCurrentPage();
            }
        });
        builder.setNegativeButton("إلغاء", null);
        builder.show();
    }

    @Override
    protected void onDestroy() {
        if (renderExecutor != null) renderExecutor.shutdown();
        try {
            if (renderer != null) renderer.close();
            if (pfd != null) pfd.close();
        } catch (Exception ignored) {}
        super.onDestroy();
    }
}
