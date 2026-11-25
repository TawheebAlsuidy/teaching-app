#!/usr/bin/env python3
"""
Strict Validator for Thaker Grade 12 Interactive Textbook JSONs.
Implements Golden Rules + Amendment #8 checks.
"""
import argparse
import glob
import json
import os
import re
import sys

PLACEHOLDER_PATTERNS = [
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\bFIXME\b", re.IGNORECASE),
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"وهكذا\s+في\s+بقية"),
    re.compile(r"\bplaceholder\b", re.IGNORECASE),
]

BAD_CHAR_RE = re.compile(r"[\uFFFD\uFB50-\uFDFF\uFE70-\uFEFF]")
MOJIBAKE_RE = re.compile(r"[≤≥ƒ†‡•‰‹›™œžŸ¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÃÂâ€]")

# Strip allowed LTR islands / LaTeX before checking unexpected Latin chars in RTL Arabic blocks
STRIP_LATEX_RE = re.compile(r"\$\$[\s\S]*?\$\$|\$[^$\n]+\$")
STRIP_HTML_LTR_RE = re.compile(
    r'<bdi[^>]*dir=["\']ltr["\'][^>]*>[\s\S]*?</bdi>|<span[^>]*dir=["\']ltr["\'][^>]*>[\s\S]*?</span>|<code[^>]*>[\s\S]*?</code>',
    re.IGNORECASE,
)
STRIP_TAGS_RE = re.compile(r"<[^>]+>")


def check_placeholders(val, path, errors):
    if isinstance(val, str):
        s = val.strip()
        if s in ("...", "…", "[...]", "???", "---"):
            errors.append(f"[{path}] قيمة نصية مؤقتة مرفوضة: {s!r}")
        for pat in PLACEHOLDER_PATTERNS:
            if pat.search(s):
                errors.append(f"[{path}] نص يحتوي على علامة نقص/مؤقت ({pat.pattern}): {s[:60]!r}")
    elif isinstance(val, dict):
        for k, v in val.items():
            check_placeholders(v, f"{path}.{k}", errors)
    elif isinstance(val, list):
        for i, v in enumerate(val):
            check_placeholders(v, f"{path}[{i}]", errors)


def check_arabic_integrity(text, path, errors, strict_latin=False):
    if not text:
        return
    if BAD_CHAR_RE.search(text):
        errors.append(f"[{path}] النص العربي يحتوي رموز استبدال أو أشكال عرض مشوّهة (FFFD / FB50-FEFF).")
    if MOJIBAKE_RE.search(text):
        errors.append(f"[{path}] النص يحتوي محارف ترميز مشوّهة (mojibake): {text[:80]!r}")
    if strict_latin:
        cleaned = STRIP_TAGS_RE.sub(" ", STRIP_HTML_LTR_RE.sub(" ", STRIP_LATEX_RE.sub(" ", text)))
        # Detect ASCII letters inside strict Arabic book text
        m = re.search(r"[A-Za-z]{2,}|[A-Za-z]", cleaned)
        if m:
            errors.append(
                f"[{path}] النص العربي يحتوي حروفاً لاتينية غير متوقعة ({m.group(0)!r}) دون عزل <bdi dir=\"ltr\">."
            )


def validate_question(q, path, errors):
    qtype = q.get("type", "mcq")
    if not q.get("stem") or not str(q["stem"]).strip():
        errors.append(f"[{path}] السؤال يفتقد نص السؤال (stem).")
    if qtype in ("mcq", "true_false", "error_spot"):
        opts = q.get("options")
        if not isinstance(opts, list) or len(opts) < 2:
            errors.append(f"[{path}] سؤال {qtype} يجب أن يحتوي خيارين على الأقل.")
            return
        correct_count = sum(1 for o in opts if o.get("is_correct") is True)
        if correct_count != 1:
            errors.append(
                f"[{path}] سؤال {qtype} يجب أن يحتوي إجابة صحيحة واحدة بالضبط (الموجود: {correct_count})."
            )
        for idx, o in enumerate(opts):
            if o.get("is_correct") is not True:
                ww = o.get("why_wrong")
                if not ww or not str(ww).strip():
                    errors.append(f"[{path}.options[{idx}]] خيار خاطئ بدون تعليل why_wrong.")


def validate_lesson_data(data, book_root=None, check_assets=False):
    errors = []
    required_top = ["schema_version", "subject", "book_title", "unit", "lesson", "blocks"]
    for key in required_top:
        if key not in data:
            errors.append(f"حقل أساسي مفقود: {key}")
    if errors:
        return errors

    check_placeholders(data, "lesson", errors)
    subject = data.get("subject", "")

    for i, blk in enumerate(data.get("blocks", [])):
        bpath = f"blocks[{i}]({blk.get('id', '?')})"
        origin = blk.get("origin")
        src = blk.get("source") or {}
        if origin == "from_book":
            if not src.get("book") or not isinstance(src.get("page"), int) or src.get("page", 0) <= 0:
                errors.append(f"[{bpath}] كتلة من الكتاب (from_book) بدون مرجع صفحة صالح source.book/source.page.")
        elif not isinstance(src.get("page"), int) and not blk.get("page_ref"):
            errors.append(f"[{bpath}] كتلة بدون مرجع صفحة.")

        btype = blk.get("type", "")
        if btype in ("quote_quran", "verse"):
            ver = blk.get("verified")
            if not ver or not str(ver).strip():
                errors.append(f"[{bpath}] كتلة {btype} بدون حقل verified موثّق.")

        bdir = blk.get("dir", "rtl")
        content = blk.get("content") or {}
        texts = []
        if content.get("text"):
            texts.append(("text", str(content["text"])))
        for li, line in enumerate(content.get("lines") or []):
            texts.append((f"lines[{li}]", str(line)))

        for field_name, txt in texts:
            if bdir == "rtl":
                # Strict Latin check on native Arabic blocks (unless inside isolated ltr tags / LaTeX)
                strict = origin == "from_book" and subject != "english"
                check_arabic_integrity(txt, f"{bpath}.{field_name}", errors, strict_latin=strict)
            elif re.search(r"[\u0600-\u06FF]", txt):
                check_arabic_integrity(txt, f"{bpath}.{field_name}", errors, strict_latin=False)

        if blk.get("edu_note_html"):
            check_arabic_integrity(str(blk["edu_note_html"]), f"{bpath}.edu_note_html", errors, strict_latin=False)

        spot = blk.get("interactive_spot") or {}
        if spot.get("enabled"):
            tabs = spot.get("tabs") or {}
            if tabs.get("simple_explain", {}).get("html"):
                check_arabic_integrity(tabs["simple_explain"]["html"], f"{bpath}.simple_explain", errors)
            pr = tabs.get("page_ref") or {}
            if check_assets and book_root and pr.get("image"):
                full = os.path.join(book_root, pr["image"])
                if not os.path.exists(full):
                    errors.append(f"[{bpath}] صورة مرجع الصفحة غير موجودة: {pr['image']}")

        if check_assets and book_root:
            if blk.get("audio_src") and not os.path.exists(os.path.join(book_root, blk["audio_src"])):
                errors.append(f"[{bpath}] ملف الصوت غير موجود: {blk['audio_src']}")
            if content.get("image") and not os.path.exists(os.path.join(book_root, content["image"])):
                errors.append(f"[{bpath}] صورة المحتوى غير موجودة: {content['image']}")
            for pi in content.get("picture_items") or []:
                if pi.get("img") and not os.path.exists(os.path.join(book_root, pi["img"])):
                    errors.append(f"[{bpath}] صورة العنصر غير موجودة: {pi['img']}")

    for ai, act in enumerate(data.get("activities", [])):
        apath = f"activities[{ai}]({act.get('id', '?')})"
        src = act.get("source") or {}
        if act.get("origin") == "from_book":
            if not src.get("book") or not isinstance(src.get("page"), int) or src.get("page", 0) <= 0:
                errors.append(f"[{apath}] نشاط من الكتاب بدون مرجع صفحة صالح.")

    for ci, chk in enumerate(data.get("section_checks", [])):
        cpath = f"section_checks[{ci}]({chk.get('id', '?')})"
        if not chk.get("page_ref"):
            errors.append(f"[{cpath}] مجموعة أسئلة بدون page_ref.")
        for qi, q in enumerate(chk.get("questions", [])):
            validate_question(q, f"{cpath}.questions[{qi}]({q.get('id', '?')})", errors)
            for opt in q.get("options", []):
                if opt.get("why_wrong"):
                    check_arabic_integrity(opt["why_wrong"], f"{cpath}.{q.get('id')}.why_wrong", errors)

    for fi, fc in enumerate(data.get("flashcards", [])):
        if not fc.get("page_ref"):
            errors.append(f"[flashcards[{fi}]] بطاقة تعليمية بدون page_ref.")
        if check_assets and book_root and fc.get("audio_src"):
            if not os.path.exists(os.path.join(book_root, fc["audio_src"])):
                errors.append(f"[flashcards[{fi}]] ملف صوت البطاقة غير موجود: {fc['audio_src']}")

    if check_assets and book_root:
        for k, rel in (data.get("lesson", {}).get("reference_images") or {}).items():
            if not os.path.exists(os.path.join(book_root, rel)):
                errors.append(f"[reference_images.{k}] صورة المرجع غير موجودة: {rel}")

    return errors


def main():
    ap = argparse.ArgumentParser(description="Validate Thaker curriculum JSON files")
    ap.add_argument("paths", nargs="+", help="JSON files or directories")
    ap.add_argument("--book-root", default=None, help="Built book root for checking asset files")
    ap.add_argument("--check-assets", action="store_true", help="Verify audio/image file paths on disk")
    args = ap.parse_args()

    files = []
    for p in args.paths:
        if os.path.isdir(p):
            files.extend(sorted(glob.glob(os.path.join(p, "**", "*.json"), recursive=True)))
        else:
            files.append(p)

    lesson_files = [f for f in files if os.path.basename(f) not in ("book.json", "glossary.json")]
    total_err = 0
    for lf in lesson_files:
        with open(lf, encoding="utf-8") as fh:
            data = json.load(fh)
        errs = validate_lesson_data(data, book_root=args.book_root, check_assets=args.check_assets)
        if errs:
            total_err += len(errs)
            print(f"FAIL: {lf} ({len(errs)} errors)")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"PASS: {lf}")

    sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()
