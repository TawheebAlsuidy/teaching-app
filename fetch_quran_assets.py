#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Download real human reciter audio (Al-Husary Muallim) and check/mirror offline assets."""
import json
import os
import shutil
import sys
import time
import urllib.request

BASE = "/media/tawheeb/New Volume3/ذاكر/teaching-app"
AUDIO_PRIMARY = f"{BASE}/assets/curriculum/grade12/quran/audio"
AUDIO_MIRRORS = [
    f"{BASE}/thaker-android-src/assets/curriculum/grade12/quran/audio",
    f"{BASE}/thaker-android-src/assets/assets/curriculum/grade12/quran/audio",
]


def fetch_with_retry(url, retries=6, timeout=25):
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:
            last_err = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"Failed fetching {url}: {last_err}")


def download_verses(verse_keys):
    for d in [AUDIO_PRIMARY] + AUDIO_MIRRORS:
        os.makedirs(d, exist_ok=True)
    ok = 0
    total_bytes = 0
    for surah, ayah in verse_keys:
        fn = f"{surah:03d}{ayah:03d}.mp3"
        dst = os.path.join(AUDIO_PRIMARY, fn)
        if not os.path.exists(dst) or os.path.getsize(dst) < 1024:
            urls = [
                f"https://mirrors.quranicaudio.com/everyayah/Husary_Muallim_128kbps/{fn}",
                f"https://mirrors.quranicaudio.com/everyayah/Husary_64kbps/{fn}",
            ]
            data = None
            last_e = None
            for url in urls:
                try:
                    data = fetch_with_retry(url, retries=4, timeout=20)
                    break
                except Exception as e:
                    last_e = e
            if data is None:
                raise RuntimeError(f"Failed downloading {fn} from all Husary mirrors: {last_e}")
            if not (data[:3] == b"ID3" or (data[0] == 0xFF and (data[1] & 0xE0) == 0xE0)):
                raise ValueError(f"Invalid MP3 frame for {fn}")
            with open(dst, "wb") as f:
                f.write(data)
        sz = os.path.getsize(dst)
        total_bytes += sz
        for m in AUDIO_MIRRORS:
            shutil.copy2(dst, os.path.join(m, fn))
        ok += 1
    print(f"[✓] {ok}/{len(verse_keys)} Husary Muallim MP3 files ready ({total_bytes / (1024*1024):.2f} MB).")


if __name__ == "__main__":
    # Initial batch: Surah An-Nur (24:1..64)
    verses = [(24, a) for a in range(1, 65)]
    if len(sys.argv) > 1:
        verses = [tuple(map(int, x.split(":"))) for x in sys.argv[1:]]
    download_verses(verses)
