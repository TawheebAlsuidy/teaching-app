#!/usr/bin/env python3
"""
Generate low-bitrate offline Opus/OGG speech audio via local Piper + PyAV.
"""
import argparse
import glob
import hashlib
import json
import os
import subprocess
import sys

PIPER_PY = "/tmp/thaker_piper_venv/bin/python"
VOICE_ONNX = "/tmp/piper_voices/en_GB-alan-low.onnx"


def encode_piper_ogg(text, out_ogg, force=False):
    os.makedirs(os.path.dirname(out_ogg), exist_ok=True)
    if os.path.exists(out_ogg) and not force and os.path.getsize(out_ogg) > 200:
        return os.path.getsize(out_ogg)

    tmp_wav = out_ogg + ".tmp.wav"
    proc = subprocess.run(
        [PIPER_PY, "-m", "piper", "-m", VOICE_ONNX, "-f", tmp_wav],
        input=text.encode("utf-8"),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"Piper failed for {text!r}: {proc.stderr.decode('utf-8', 'ignore')}")

    # Convert WAV -> Ogg Opus 24kbps mono using PyAV inside piper venv
    conv_code = (
        "import av, sys\n"
        "inp = av.open(sys.argv[1])\n"
        "out = av.open(sys.argv[2], 'w', format='ogg')\n"
        "st = out.add_stream('libopus', rate=48000, layout='mono')\n"
        "st.bit_rate = 24000\n"
        "res = av.AudioResampler(format='s16', layout='mono', rate=48000)\n"
        "for fr in inp.decode(audio=0):\n"
        "    for rf in res.resample(fr):\n"
        "        for p in st.encode(rf): out.mux(p)\n"
        "for p in st.encode(None): out.mux(p)\n"
        "out.close(); inp.close()\n"
    )
    subprocess.run([PIPER_PY, "-c", conv_code, tmp_wav, out_ogg], check=True)
    if os.path.exists(tmp_wav):
        os.remove(tmp_wav)
    return os.path.getsize(out_ogg)


def safe_slug(text):
    h = hashlib.sha1(text.encode("utf-8")).hexdigest()[:8]
    clean = "".join(c.lower() if c.isalnum() else "_" for c in text).strip("_")[:28]
    return f"{clean}_{h}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--subject", required=True)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    if not os.path.exists(PIPER_PY) or not os.path.exists(VOICE_ONNX):
        print("ERROR: Piper venv or voice model missing at /tmp/thaker_piper_venv or /tmp/piper_voices", file=sys.stderr)
        sys.exit(1)

    content_dir = os.path.join("content", args.subject)
    book_assets = os.path.join("books", args.subject, "assets")
    lesson_files = sorted(
        f for f in glob.glob(os.path.join(content_dir, "**", "*.json"), recursive=True)
        if os.path.basename(f) not in ("book.json", "glossary.json")
    )

    total_files = 0
    total_bytes = 0
    for lf in lesson_files:
        with open(lf, encoding="utf-8") as fh:
            data = json.load(fh)
        lid = data["lesson"]["id"]

        # 1. Word glossary entries
        for word, meta in (data.get("word_glossary_map") or {}).items():
            if meta.get("audio_src"):
                out_path = os.path.join("books", args.subject, meta["audio_src"])
                total_bytes += encode_piper_ogg(word, out_path, force=args.force)
                total_files += 1

        # 2. Reading blocks & flashcards with audio_src
        for blk in data.get("blocks", []):
            if blk.get("audio_src"):
                txt = blk.get("speech_text") or blk.get("content", {}).get("text") or " ".join(blk.get("content", {}).get("lines") or [])
                out_path = os.path.join("books", args.subject, blk["audio_src"])
                total_bytes += encode_piper_ogg(txt, out_path, force=args.force)
                total_files += 1

        for fc in data.get("flashcards", []):
            if fc.get("audio_src"):
                txt = fc.get("speech_text") or fc["front"].split("(")[0].strip()
                out_path = os.path.join("books", args.subject, fc["audio_src"])
                total_bytes += encode_piper_ogg(txt, out_path, force=args.force)
                total_files += 1

    print(f"Audio ready for {args.subject}: {total_files} OGG/Opus files ({total_bytes/1024:.1f} KB)")


if __name__ == "__main__":
    main()
