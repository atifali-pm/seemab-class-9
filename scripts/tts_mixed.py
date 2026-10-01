#!/usr/bin/env python3
"""Render a lesson script in three voices.

    Urdu     the teaching, in ur-PK-UzmaNeural
    Arabic   Quranic ayat and Arabic hadith, recited by ar-SA-HamedNeural
    English  the book's own words, read by en-GB-SoniaNeural

An Urdu voice reading a full English definition sounds wrong, but switching voice
for a single embedded technical term would sound choppy. So only a run of six or
more English words counts as a quotation; shorter runs stay in the Urdu voice.

Both Urdu and Arabic use the same script, so the Arabic is found by its
vocalisation: Quranic text carries full harakat, Urdu prose carries almost none.
A passage can also be marked explicitly with {{ar}} ... {{/ar}}, which always wins.

    python3 tts_mixed.py script.txt out.mp3 [--rate=-15%]
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile

VENV = "/home/atif/.local/share/tts-venv/bin/edge-tts"
URDU_VOICE = "ur-PK-UzmaNeural"
ARABIC_VOICE = "ar-SA-HamedNeural"
ENGLISH_VOICE = "en-GB-SoniaNeural"

HARAKAT = re.compile(r"[ً-ْٰۖ-ۭ]")
ARABIC_CH = re.compile(r"[؀-ۿ]")
EXPLICIT = re.compile(r"\{\{(ar|en)\}\}(.*?)\{\{/\1\}\}", re.S)
# a quoted definition, not a stray technical term
LATIN_RUN = re.compile(r"[A-Za-z][A-Za-z0-9.,'\-]*(?:\s+[A-Za-z][A-Za-z0-9.,'\-]*)*")
MIN_EN_WORDS = 6
# A gap this short between two recited runs is part of the same ayah, not prose.
BRIDGE_MAX = 5


def _vocalised(tok):
    return len(HARAKAT.findall(tok)) >= 2


def _split_english(chunk):
    """Pull long English quotations out of an Urdu chunk."""
    out, pos = [], 0
    for m in LATIN_RUN.finditer(chunk):
        run = m.group(0)
        if len(run.split()) < MIN_EN_WORDS:
            continue
        if m.start() > pos:
            out.append(("ur", chunk[pos:m.start()]))
        out.append(("en", run))
        pos = m.end()
    if pos < len(chunk):
        out.append(("ur", chunk[pos:]))
    return [(k, t) for k, t in out if t.strip()]


def _auto_segments(text):
    """Split one plain chunk into [(is_arabic, text)] by runs of vocalised words."""
    toks = [t for t in re.split(r"(\s+)", text) if t]
    flags = []
    for t in toks:
        flags.append(None if not t.strip() else _vocalised(t))

    # Absorb a short unvocalised word sitting between two recited words: a word
    # like "فِي" carries one harakat and would otherwise cut an ayah in half.
    for i, f in enumerate(flags):
        if f is not False:
            continue
        t = toks[i].strip()
        if len(t) > BRIDGE_MAX or not ARABIC_CH.search(t):
            continue
        before = next((flags[j] for j in range(i - 1, -1, -1) if flags[j] is not None), None)
        after = next((flags[j] for j in range(i + 1, len(flags)) if flags[j] is not None), None)
        if before and after:
            flags[i] = True

    out = []
    for t, f in zip(toks, flags):
        if f is None:
            if out:
                out[-1][1] += t
            continue
        if out and out[-1][0] == f:
            out[-1][1] += t
        else:
            out.append([f, t])
    return [(a, b.strip()) for a, b in out if b.strip()]


def segments(text):
    """[(kind, text)] with kind in ur / ar / en. Explicit markers always win."""
    staged, pos = [], 0
    for m in EXPLICIT.finditer(text):
        if m.start() > pos:
            staged += [(("ar" if a else "auto"), t) for a, t in _auto_segments(text[pos:m.start()])]
        staged.append((m.group(1), m.group(2).strip()))
        pos = m.end()
    if pos < len(text):
        staged += [(("ar" if a else "auto"), t) for a, t in _auto_segments(text[pos:])]

    out = []
    for kind, t in staged:
        if not t.strip():
            continue
        if kind == "auto":
            out += _split_english(t)
        else:
            out.append((kind, t))
    return [(k, t.strip()) for k, t in out if t.strip()]


def say(text, voice, rate, dest):
    cmd = [VENV, "--voice", voice, "--text", text, "--write-media", dest]
    if rate:
        cmd.insert(3, "--rate=" + rate)
    r = subprocess.run(cmd, capture_output=True)
    ok = r.returncode == 0 and os.path.exists(dest) and os.path.getsize(dest) > 500
    if not ok:
        sys.stderr.write("TTS failed for: %r\n%s\n" % (text[:60], r.stderr.decode()[:300]))
    return ok


def silence(seconds, dest):
    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i",
                    "anullsrc=r=24000:cl=mono", "-t", str(seconds),
                    "-c:a", "libmp3lame", "-b:a", "48k", dest], capture_output=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("out")
    ap.add_argument("--rate", default="-15%")
    # Arabic recitation is naturally slower; do not speed it up with the prose.
    ap.add_argument("--arabic-rate", default="-25%")
    ap.add_argument("--urdu-voice", default=URDU_VOICE)
    ap.add_argument("--arabic-voice", default=ARABIC_VOICE)
    ap.add_argument("--english-voice", default=ENGLISH_VOICE)
    # the book's wording is read steadily, a touch slower than the Urdu around it
    ap.add_argument("--english-rate", default="-8%")
    a = ap.parse_args()

    text = open(a.script, encoding="utf-8").read()
    segs = segments(text)
    n_ar = sum(1 for k, _ in segs if k == "ar")
    n_en = sum(1 for k, _ in segs if k == "en")
    print("%d segments: %d Arabic, %d English quotations, rest Urdu"
          % (len(segs), n_ar, n_en))

    tmp = tempfile.mkdtemp(prefix="tts_mixed_")
    parts, pause = [], os.path.join(tmp, "pause.mp3")
    silence(0.45, pause)

    VOICES = {"ur": (a.urdu_voice, a.rate),
              "ar": (a.arabic_voice, a.arabic_rate),
              "en": (a.english_voice, a.english_rate)}
    for i, (kind, chunk) in enumerate(segs):
        dest = os.path.join(tmp, "%03d.mp3" % i)
        voice, rate = VOICES[kind]
        if not say(chunk, voice, rate, dest):
            continue
        if kind != "ur":
            parts.append(pause)          # a beat before the quotation
        parts.append(dest)
        if kind != "ur":
            parts.append(pause)          # and one after, before the Urdu resumes
            print("   %s: %s" % (kind.upper(), chunk[:68]))

    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as fh:
        for p in parts:
            fh.write("file '%s'\n" % p)
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst,
                    "-c:a", "libmp3lame", "-b:a", "48k", "-ar", "24000", "-ac", "1",
                    a.out], capture_output=True)
    d = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", a.out], capture_output=True).stdout.decode().strip()
    print("wrote %s  (%.1f min)" % (a.out, float(d or 0) / 60))


if __name__ == "__main__":
    main()
