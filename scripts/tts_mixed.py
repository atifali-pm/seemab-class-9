#!/usr/bin/env python3
"""Render a lesson script where Quranic ayat and Arabic hadith are recited by an
Arabic voice and everything else is spoken in Urdu.

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

HARAKAT = re.compile(r"[ً-ْٰۖ-ۭ]")
ARABIC_CH = re.compile(r"[؀-ۿ]")
EXPLICIT = re.compile(r"\{\{ar\}\}(.*?)\{\{/ar\}\}", re.S)
# A gap this short between two recited runs is part of the same ayah, not prose.
BRIDGE_MAX = 5


def _vocalised(tok):
    return len(HARAKAT.findall(tok)) >= 2


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
    """Explicit {{ar}} markers first, auto-detection for everything else."""
    out, pos = [], 0
    for m in EXPLICIT.finditer(text):
        if m.start() > pos:
            out += _auto_segments(text[pos:m.start()])
        out.append((True, m.group(1).strip()))
        pos = m.end()
    if pos < len(text):
        out += _auto_segments(text[pos:])
    return [(a, t) for a, t in out if t.strip()]


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
    a = ap.parse_args()

    text = open(a.script, encoding="utf-8").read()
    segs = segments(text)
    n_ar = sum(1 for is_ar, _ in segs if is_ar)
    print("%d segments, %d recited in Arabic" % (len(segs), n_ar))

    tmp = tempfile.mkdtemp(prefix="tts_mixed_")
    parts, pause = [], os.path.join(tmp, "pause.mp3")
    silence(0.45, pause)

    for i, (is_ar, chunk) in enumerate(segs):
        dest = os.path.join(tmp, "%03d.mp3" % i)
        voice = a.arabic_voice if is_ar else a.urdu_voice
        rate = a.arabic_rate if is_ar else a.rate
        if not say(chunk, voice, rate, dest):
            continue
        if is_ar:
            parts.append(pause)          # a beat before the ayah
        parts.append(dest)
        if is_ar:
            parts.append(pause)          # and one after, before the translation
        if is_ar:
            print("   AR: %s" % chunk[:70])

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
