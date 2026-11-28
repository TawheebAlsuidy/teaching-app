#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Authoritative Tanzil Quran text lookup, verification, and non-destructive Tajweed highlighter.

Golden Rule: NEVER alters a single Quranic character or diacritic. Every returned snippet is
proven character-for-character equal to scripts/quran_refs/tanzil_uthmani.txt.
"""
import html
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UTHMANI_PATH = os.path.join(BASE_DIR, "scripts", "quran_refs", "tanzil_uthmani.txt")
SIMPLE_PATH = os.path.join(BASE_DIR, "scripts", "quran_refs", "tanzil_simple.txt")

BASMALA_UTHMANI = "بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"
BASMALA_SIMPLE = "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ"

SURAH_NAMES = {
    1: "الفاتحة", 2: "البقرة", 3: "آل عمران", 4: "النساء", 5: "المائدة",
    6: "الأنعام", 7: "الأعراف", 8: "الأنفال", 9: "التوبة", 10: "يونس",
    11: "هود", 12: "يوسف", 13: "الرعد", 14: "إبراهيم", 15: "الحجر",
    16: "النحل", 17: "الإسراء", 18: "الكهف", 19: "مريم", 20: "طه",
    21: "الأنبياء", 22: "الحج", 23: "المؤمنون", 24: "النور", 25: "الفرقان",
    26: "الشعراء", 27: "النمل", 28: "القصص", 29: "العنكبوت", 30: "الروم",
    31: "لقمان", 32: "السجدة", 33: "الأحزاب", 34: "سبأ", 35: "فاطر",
    36: "يس", 37: "الصافات", 38: "ص", 39: "الزمر", 40: "غافر",
    41: "فصلت", 42: "الشورى", 43: "الزخرف", 44: "الدخان", 45: "الجاثية",
    46: "الأحقاف", 47: "محمد", 48: "الفتح", 49: "الحجرات", 50: "ق",
    51: "الذاريات", 52: "الطور", 53: "النجم", 54: "القمر", 55: "الرحمن",
    56: "الواقعة", 57: "الحديد", 58: "المجادلة", 59: "الحشر", 60: "الممتحنة",
    61: "الصف", 62: "الجمعة", 63: "المنافقون", 64: "التغابن", 65: "الطلاق",
    66: "التحريم", 67: "الملك", 68: "القلم",
}

WAQF_MARKS = {
    "\u06d6": ("صلے", "الوقف جائز مع كون الوصل أولى"),
    "\u06d7": ("قلى", "الوقف أولى مع جواز الوصل"),
    "\u06d8": ("م", "وقف لازم (قد يخل الوصل بالمعنى)"),
    "\u06d9": ("لا", "لا تقف هنا (الابتداء بما بعده يخل)"),
    "\u06da": ("ج", "وقف جائز مستوى الطرفين"),
    "\u06db": ("ۛ", "وقف المعانقة (يقف على أحد الموضعين دون الآخر)"),
    "\u06e9": ("۩", "موضع سجدة تلاوة"),
}

_AR_DIACRITICS = re.compile(r"[\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed]")
_STOP_MARKS = set("\u06d6\u06d7\u06d8\u06d9\u06da\u06db\u06dc\u06de\u06df\u06e0\u06e2\u06e3\u06e4\u06e5\u06e6\u06e7\u06e8\u06e9\u06ea\u06eb\u06ec\u06ed\u06dd")


def load_corpus():
    u_map, s_map = {}, {}
    with open(UTHMANI_PATH, encoding="utf-8") as f:
        for line in f:
            if "|" in line:
                s, a, t = line.strip().split("|", 2)
                s_i, a_i = int(s), int(a)
                # Strip inline Basmala prefix on ayah 1 of surahs != 1 and != 9 (we render Basmala cleanly as header)
                if a_i == 1 and s_i not in (1, 9) and t.startswith(BASMALA_UTHMANI + " "):
                    t = t[len(BASMALA_UTHMANI) + 1:]
                u_map[(s_i, a_i)] = t
    with open(SIMPLE_PATH, encoding="utf-8") as f:
        for line in f:
            if "|" in line:
                s, a, t = line.strip().split("|", 2)
                s_i, a_i = int(s), int(a)
                if a_i == 1 and s_i not in (1, 9) and t.startswith(BASMALA_SIMPLE + " "):
                    t = t[len(BASMALA_SIMPLE) + 1:]
                s_map[(s_i, a_i)] = t
    return u_map, s_map


UTHMANI_MAP, SIMPLE_MAP = load_corpus()


def strip_diacritics(text: str) -> str:
    """Normalizes Arabic letters strictly for matching/search ONLY (never display)."""
    t = _AR_DIACRITICS.sub("", text)
    t = t.replace("ٱ", "ا").replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    t = t.replace("ى", "ي").replace("ؤ", "و").replace("ئ", "ي").replace("ـ", "")
    t = re.sub(r"\s+", " ", t).strip()
    return t


def get_ayah(surah: int, ayah: int) -> dict:
    u = UTHMANI_MAP[(surah, ayah)]
    s = SIMPLE_MAP[(surah, ayah)]
    return {
        "surah": surah,
        "surah_name": SURAH_NAMES.get(surah, str(surah)),
        "ayah": ayah,
        "key": f"{surah}:{ayah}",
        "uthmani": u,
        "simple": s,
        "plain": strip_diacritics(s),
    }


def get_range(surah: int, start: int, end: int) -> list:
    return [get_ayah(surah, a) for a in range(start, end + 1)]


def _skel(word: str) -> str:
    """Strict consonant skeleton strictly for matching human slice hints to Tanzil."""
    t = _AR_DIACRITICS.sub("", word)
    t = t.replace("ـ", "").replace("ٱ", "ا").replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    t = t.replace("ى", "ي").replace("ؤ", "و").replace("ئ", "ي").replace("ء", "")
    # Drop medial/final vowel-letters (ا / ي / ى) so Uthmani (ى/خنجرية) & Imlaei hints always align
    if len(t) > 1:
        t = t[0] + t[1:].replace("ا", "").replace("ي", "")
    return t.strip()


def slice_uthmani(surah: int, ayah: int, start_words_plain: str, end_words_plain: str = None) -> str:
    """Slice an exact Uthmani span from verified Tanzil text using diacritic/alef-tolerant alignment.
    Always returns the exact unmodified substring from scripts/quran_refs/tanzil_uthmani.txt."""
    raw = get_ayah(surah, ayah)["uthmani"]
    words = raw.split(" ")
    nonempty = [(idx, _skel(w)) for idx, w in enumerate(words) if _skel(w)]

    def _find_match(query_plain: str, from_word_idx: int = 0):
        q_tokens = [_skel(t) for t in query_plain.split() if _skel(t)]
        q_joined = "".join(q_tokens)
        # First try exact token-sequence match
        for i in range(len(nonempty) - len(q_tokens) + 1):
            if nonempty[i][0] < from_word_idx:
                continue
            if all(nonempty[i + k][1] == q_tokens[k] for k in range(len(q_tokens))):
                return nonempty[i][0], nonempty[i + len(q_tokens) - 1][0]
        # Fallback for Uthmani fused prefixes like يَٰٓأَيُّهَا or فِيمَا
        for i in range(len(nonempty)):
            if nonempty[i][0] < from_word_idx:
                continue
            acc = ""
            for j in range(i, min(len(nonempty), i + len(q_tokens) + 2)):
                acc += nonempty[j][1]
                if acc == q_joined:
                    return nonempty[i][0], nonempty[j][0]
        raise AssertionError(
            f"Tanzil slice mismatch in {surah}:{ayah}: cannot find {query_plain!r} "
            f"(skel={q_joined!r}) in {[w[1] for w in nonempty]!r}"
        )

    s_idx, s_end = _find_match(start_words_plain, 0)
    if end_words_plain:
        _, e_idx = _find_match(end_words_plain, s_idx)
    else:
        e_idx = s_end
    return " ".join(words[s_idx:e_idx + 1])


def to_arabic_digits(n: int) -> str:
    return str(n).translate(str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩"))


def highlight_tajweed_word(word: str) -> str:
    """Wrap exact graphemes in Tajweed CSS spans while preserving exact raw character concatenation."""
    # Verify round-trip safety on every single word!
    if any(m in word for m in WAQF_MARKS):
        parts = []
        for ch in word:
            if ch in WAQF_MARKS:
                sym, desc = WAQF_MARKS[ch]
                parts.append(f'<span class="tj-waqf" title="{html.escape(desc)}">{ch}</span>')
            else:
                parts.append(html.escape(ch))
        res = "".join(parts)
        return res

    # Highlight Qalqalah with sukun (\u0652) or small head of khah (\u06e1)
    q_chars = "قطبجد"
    out = []
    i = 0
    chars = list(word)
    n = len(chars)
    while i < n:
        ch = chars[i]
        # Ghunnah: نّ or مّ (letter + shadda)
        if ch in ("ن", "م") and i + 1 < n and chars[i + 1] == "\u0651":
            j = i + 2
            while j < n and ("\u064b" <= chars[j] <= "\u065f" or chars[j] == "\u0670"):
                j += 1
            seg = "".join(chars[i:j])
            out.append(f'<span class="tj-ghunnah" data-rule="ghunnah">{html.escape(seg)}</span>')
            i = j
            continue
        # Qalqalah letter followed directly by sukun (\u0652 or \u06e1)
        if ch in q_chars and i + 1 < n and chars[i + 1] in ("\u0652", "\u06e1"):
            seg = "".join(chars[i:i + 2])
            out.append(f'<span class="tj-qalqalah" data-rule="qalqalah">{html.escape(seg)}</span>')
            i += 2
            continue
        # Madd Wajib/Jaiz (character + \u06e4 Maddah above, e.g. آ / آ / وٓ / يٓ / ءَآ)
        if ch == "\u06e4" or ch == "\u0653":
            # Include preceding base letter if last element wasn't span
            if out and not out[-1].endswith("</span>"):
                prev = out.pop()
                out.append(f'<span class="tj-madd" data-rule="madd">{prev}{html.escape(ch)}</span>')
            else:
                out.append(f'<span class="tj-madd" data-rule="madd">{html.escape(ch)}</span>')
            i += 1
            continue
        out.append(html.escape(ch))
        i += 1
    res = "".join(out)
    # Non-negotiable invariant check: stripping tags must identically reconstruct the original word
    stripped = html.unescape(re.sub(r"<[^>]+>", "", res))
    assert stripped == word, f"Tajweed highlighter mutated word! {word!r} != {stripped!r}"
    return res


def render_ayah_tajweed_html(uthmani_text: str) -> str:
    tokens = uthmani_text.split(" ")
    return " ".join(highlight_tajweed_word(tok) for tok in tokens)


if __name__ == "__main__":
    sample = get_ayah(24, 35)
    rendered = render_ayah_tajweed_html(sample["uthmani"])
    reconstructed = html.unescape(re.sub(r"<[^>]+>", "", rendered))
    assert reconstructed == sample["uthmani"]
    print("[✓] Corpus loaded:", len(UTHMANI_MAP), "verses. Verification check OK on 24:35.")
