#!/usr/bin/env python3
"""
Build offline interactive HTML book + lazy lesson JS modules + offline human review HTMLs.
"""
import argparse
import glob
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import validate_book  # noqa: E402


ORIGIN_AR = {
    "from_book": ("من الكتاب", "#D1FAE5", "#065F46"),
    "educational_addition": ("إضافة تعليمية", "#E0F2FE", "#075985"),
    "for_enrichment": ("للتوسع", "#EDE9FE", "#5B21B6"),
    "proposed_solution": ("حل مقترح", "#FEF3C7", "#92400E"),
}


def build_index_html(book_meta):
    title = html.escape(book_meta.get("title_ar") or book_meta.get("title") or "كتاب تفاعلي")
    is_english = book_meta.get("subject") == "english"
    lang_script = '<script src="../../engine/js/subjects/english.js"></script>\n' if is_english else ""
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=2.0, user-scalable=yes">
<title>{title} — ذاكر</title>
<link rel="stylesheet" href="../../engine/vendor/fonts/fonts.css">
<link rel="stylesheet" href="../../engine/vendor/katex/katex.min.css">
<link rel="stylesheet" href="../../engine/styles/engine.css">
</head>
<body data-mode="study">
<header class="tk-header">
  <div class="tk-header-top">
    <button type="button" class="tk-icon-btn" id="tkBackBtn" aria-label="رجوع">↩</button>
    <div class="tk-title-wrap">
      <div class="tk-book-kicker" id="tkBookKicker">{title}</div>
      <div class="tk-lesson-title" id="tkHeaderTitle">جاري التحميل...</div>
    </div>
    <button type="button" class="tk-icon-btn" data-nav-view="toc" aria-label="الفهرس">☰</button>
  </div>
  <div class="tk-progress-bar"><div class="tk-progress-fill" id="tkProgressFill"></div></div>
  <div class="tk-mode-bar">
    <div class="tk-seg-group" role="tablist" aria-label="أوضاع القراءة">
      <button type="button" class="tk-seg-btn" data-set-mode="read">قراءة</button>
      <button type="button" class="tk-seg-btn active" data-set-mode="study">دراسة</button>
      <button type="button" class="tk-seg-btn" data-set-mode="practice">تدريب</button>
    </div>
    <div class="tk-tool-row">
      <button type="button" class="tk-mini-btn" id="tkFontMinus" aria-label="تصغير الخط">A-</button>
      <button type="button" class="tk-mini-btn" id="tkFontPlus" aria-label="تكبير الخط">A+</button>
      <button type="button" class="tk-mini-btn" id="tkThemeBtn">نهار</button>
    </div>
  </div>
</header>

<main class="tk-main">
  <section id="view-lesson"><div id="tkLessonContent"></div></section>
  <section id="view-practice" style="display:none;"><div id="tkPracticeContent"></div></section>
  <section id="view-flashcards" style="display:none;"><div id="tkFlashcardsContent"></div></section>
  <section id="view-search" style="display:none;"><div id="tkSearchContent"></div></section>
  <section id="view-toc" style="display:none;"><div id="tkTocContent"></div></section>
</main>

<div id="tkWordPop" class="tk-word-pop" role="dialog" aria-label="معنى الكلمة"></div>
<div id="tkToast" class="tk-toast" role="status" aria-live="polite"></div>

<div id="tkBackdrop" class="tk-backdrop"></div>
<section id="tkSheet" class="tk-sheet" role="dialog" aria-label="التفاصيل التفاعلية">
  <div class="tk-sheet-head">
    <strong id="tkSheetTitle">تفاصيل</strong>
    <button type="button" class="tk-act-mini" id="tkSheetClose" aria-label="إغلاق">✕</button>
  </div>
  <div class="tk-sheet-tabs" id="tkSheetTabs"></div>
  <div class="tk-sheet-body" id="tkSheetBody"></div>
</section>

<nav class="tk-bottom-bar" aria-label="التنقل السريع">
  <button type="button" class="tk-nav-item active" data-nav-view="lesson">📖<span>الدرس</span></button>
  <button type="button" class="tk-nav-item" data-nav-view="practice">📝<span>التمارين والاختبار</span></button>
  <button type="button" class="tk-nav-item" data-nav-view="flashcards">🗂️<span>البطاقات</span></button>
  <button type="button" class="tk-nav-item" data-nav-view="search">🔍<span>بحث وملاحظات</span></button>
  <button type="button" class="tk-nav-item" data-nav-view="toc">📚<span>الفهرس</span></button>
</nav>

<script src="../../engine/vendor/katex/katex.min.js"></script>
<script src="../../engine/vendor/katex/contrib/auto-render.min.js"></script>
<script src="../../engine/js/storage.js"></script>
<script src="../../engine/js/speech.js"></script>
<script src="../../engine/js/mode-controller.js"></script>
<script src="../../engine/js/quiz-engine.js"></script>
<script src="../../engine/js/bottom-sheet.js"></script>
<script src="../../engine/js/flashcards-leitner.js"></script>
<script src="../../engine/js/search-notes.js"></script>
{lang_script}<script src="book.js"></script>
<script src="../../engine/js/app-shell.js"></script>
</body>
</html>
"""


def build_review_html(subject, data):
    """Offline human-review HTML: page image side-by-side with block-by-block extracted JSON."""
    lid = data["lesson"]["id"]
    title = f"{data['lesson']['code']} · {data['lesson']['title']}"
    refs = data["lesson"].get("reference_images", {})
    ref_options = ""
    first_img = ""
    for k, rel in refs.items():
        img_href = f"../../books/{subject}/{rel}"
        if not first_img:
            first_img = img_href
        ref_options += f'<option value="{html.escape(img_href)}">{html.escape(k.upper())} ({html.escape(rel)})</option>'

    blocks_html = []
    for blk in data.get("blocks", []):
        o_label, o_bg, o_fg = ORIGIN_AR.get(blk.get("origin", "from_book"), ORIGIN_AR["from_book"])
        src = blk.get("source", {})
        c = blk.get("content", {})
        txt = html.escape(c.get("text") or "\n".join(c.get("lines") or []))
        blocks_html.append(
            f'<div class="blk">'
            f'<div class="meta">'
            f'<span class="badge" style="background:{o_bg};color:{o_fg}">{o_label}</span>'
            f'<span class="pill">{html.escape(blk["id"])} · {html.escape(blk["type"])} · {html.escape(src.get("book",""))} ص {html.escape(str(src.get("page","")))}</span>'
            f'</div>'
            f'<pre class="txt" dir="{html.escape(blk.get("dir","ltr"))}">{txt}</pre>'
            + (f'<div class="note"><strong>إضافة تعليمية:</strong> {blk["edu_note_html"]}</div>' if blk.get("edu_note_html") else "")
            + f'</div>'
        )

    acts_html = []
    for act in data.get("activities", []):
        o_label, o_bg, o_fg = ORIGIN_AR.get(act.get("origin", "from_book"), ORIGIN_AR["from_book"])
        src = act.get("source", {})
        acts_html.append(
            f'<div class="blk">'
            f'<div class="meta"><span class="badge" style="background:{o_bg};color:{o_fg}">{o_label}</span>'
            f'<span class="pill">{html.escape(act["id"])} · {html.escape(src.get("book",""))} ص {html.escape(str(src.get("page","")))}</span></div>'
            f'<div class="txt" dir="ltr">{html.escape(act.get("prompt_literal",""))}</div>'
            f'<details><summary>عرض العناصر والحل المقترح ({len(act.get("items") or act.get("steps") or [])})</summary>'
            f'<pre class="json">{html.escape(json.dumps(act.get("items") or act.get("steps") or [], ensure_ascii=False, indent=2))}</pre>'
            f'</details></div>'
        )

    checks_html = []
    for chk in data.get("section_checks", []):
        for q in chk.get("questions", []):
            opts_li = "".join(
                f'<li style="color:{"#065F46" if o.get("is_correct") else "#991B1B"}">'
                f'{html.escape(o["text"])} {"✓" if o.get("is_correct") else "✗ — " + html.escape(o.get("why_wrong",""))}'
                f"</li>"
                for o in q.get("options", [])
            )
            checks_html.append(
                f'<div class="blk"><div class="meta"><span class="pill">{html.escape(q["id"])} · {html.escape(q.get("type",""))} · دليل: {html.escape(q.get("evidence_block_id",""))}</span></div>'
                f'<div class="txt" dir="auto"><strong>{html.escape(q["stem"])}</strong></div><ul>{opts_li}</ul></div>'
            )

    notes_audit = ""
    if data.get("extraction_audit"):
        notes_audit = "<h3>ملاحظات التدقيق والاستخراج الأولي</h3><pre class=\"json\">" + html.escape(
            json.dumps(data["extraction_audit"], ensure_ascii=False, indent=2)
        ) + "</pre>"

    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>مراجعة بشرية — {html.escape(title)}</title>
<style>
body {{ font-family: system-ui, -apple-system, sans-serif; margin: 0; background: #F1F5F9; color: #0F172A; }}
header {{ background: #064E3B; color: #fff; padding: 12px 16px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; }}
.grid {{ display: grid; grid-template-columns: 1fr; gap: 12px; padding: 12px; }}
@media (min-width: 960px) {{ .grid {{ grid-template-columns: 45% 55%; align-items: start; }} .pane-img {{ position: sticky; top: 12px; }} }}
.pane {{ background: #fff; border: 1px solid #CBD5E1; border-radius: 12px; padding: 12px; }}
.pane img {{ width: 100%; height: auto; border: 1px solid #E2E8F0; border-radius: 8px; margin-top: 8px; }}
.blk {{ border: 1px solid #E2E8F0; border-radius: 10px; padding: 10px; margin-bottom: 10px; background: #F8FAFC; }}
.meta {{ display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 6px; }}
.badge {{ padding: 2px 8px; border-radius: 999px; font-size: 12px; font-weight: 700; }}
.pill {{ padding: 2px 8px; border-radius: 8px; background: #E2E8F0; font-size: 12px; }}
pre.txt {{ white-space: pre-wrap; font-family: inherit; margin: 4px 0; line-height: 1.65; }}
pre.json {{ white-space: pre-wrap; font-size: 12px; background: #fff; padding: 8px; border-radius: 8px; overflow-x: auto; }}
.note {{ margin-top: 6px; background: #E0F2FE; padding: 6px 9px; border-radius: 8px; font-size: 13px; }}
select {{ padding: 6px 10px; border-radius: 8px; border: 1px solid #CBD5E1; font-size: 14px; }}
</style>
</head>
<body>
<header>
  <div><strong>أداة المراجعة البشرية (أوفلاين): {html.escape(title)}</strong> · درس: {html.escape(lid)}</div>
  <div><select id="refSel" onchange="document.getElementById('refImg').src=this.value">{ref_options}</select></div>
</header>
<div class="grid">
  <section class="pane pane-img">
    <strong>صورة الصفحة الأصلية من الكتاب</strong>
    <img id="refImg" src="{html.escape(first_img)}" alt="Reference page">
  </section>
  <section class="pane">
    <h3>النصوص المستخرجة كتلةً كتلة ({len(data.get("blocks", []))})</h3>
    {"".join(blocks_html)}
    <h3>أنشطة كتاب التمارين ({len(data.get("activities", []))})</h3>
    {"".join(acts_html)}
    <h3>الأسئلة والاختبارات الذاتية</h3>
    {"".join(checks_html)}
    {notes_audit}
  </section>
</div>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--subject", required=True)
    args = ap.parse_args()

    content_root = os.path.join("content", args.subject)
    book_out = os.path.join("books", args.subject)
    qa_out = os.path.join("QA", args.subject)
    os.makedirs(os.path.join(book_out, "lessons"), exist_ok=True)
    os.makedirs(qa_out, exist_ok=True)

    with open(os.path.join(content_root, "book.json"), encoding="utf-8") as fh:
        book_meta = json.load(fh)

    lesson_files = sorted(
        f for f in glob.glob(os.path.join(content_root, "**", "*.json"), recursive=True)
        if os.path.basename(f) not in ("book.json", "glossary.json")
    )
    if not lesson_files:
        print(f"No lesson JSONs under {content_root}", file=sys.stderr)
        sys.exit(1)

    all_errors = []
    built_ids = set()
    for lf in lesson_files:
        with open(lf, encoding="utf-8") as fh:
            data = json.load(fh)
        errs = validate_book.validate_lesson_data(data, book_root=book_out, check_assets=True)
        if errs:
            all_errors.extend((lf, errs))
            continue

        lid = data["lesson"]["id"]
        built_ids.add(lid)
        js_path = os.path.join(book_out, "lessons", f"{lid}.js")
        with open(js_path, "w", encoding="utf-8") as out:
            out.write(f"window.__THAKER_LESSONS__ = window.__THAKER_LESSONS__ || {{}};\n")
            out.write(f"window.__THAKER_LESSONS__[{json.dumps(lid)}] = ")
            json.dump(data, out, ensure_ascii=False)
            out.write(";\n")

        rev_path = os.path.join(qa_out, f"{lid}_review.html")
        with open(rev_path, "w", encoding="utf-8") as rfh:
            rfh.write(build_review_html(args.subject, data))

    if all_errors:
        for lf, errs in all_errors:
            print(f"VALIDATION FAILED: {lf}", file=sys.stderr)
            for e in errs:
                print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    for u in book_meta.get("units", []):
        for ls in u.get("lessons", []):
            ls["built"] = ls["id"] in built_ids

    glossary_path = os.path.join(content_root, "glossary.json")
    if os.path.exists(glossary_path):
        with open(glossary_path, encoding="utf-8") as gfh:
            book_meta["glossary"] = json.load(gfh)

    with open(os.path.join(book_out, "book.js"), "w", encoding="utf-8") as bfh:
        bfh.write("window.__THAKER_BOOK__ = ")
        json.dump(book_meta, bfh, ensure_ascii=False)
        bfh.write(";\n")

    with open(os.path.join(book_out, "index.html"), "w", encoding="utf-8") as hfh:
        hfh.write(build_index_html(book_meta))

    print(f"Built {args.subject}: {len(built_ids)} lessons -> {book_out}/ and review HTMLs -> {qa_out}/")


if __name__ == "__main__":
    main()
