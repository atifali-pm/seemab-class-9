#!/usr/bin/env python3
"""Render one backfill lesson: a one page note PDF, an Urdu script, and the audio.

Content for each lesson is written by hand in scripts/backfill/<subject>_chNN.py
and passed in here, so this file only does layout, rendering and bookkeeping.
"""
import json
import os
import subprocess
import sys

ROOT = "/home/atif/projects/education/seemab/class-9"
NOTES = os.path.join(ROOT, "seemab-reports", "revision")
AUDIO = os.path.join(NOTES, "audio")
PLAN = os.path.join(ROOT, "seemab-reports", "lesson-plan.json")
SUMS = os.path.join(ROOT, "seemab-reports", "summaries.json")
TTS = os.path.join(ROOT, "scripts", "tts_mixed.py")

CSS = """@page{size:A5;margin:5mm}
*{box-sizing:border-box}
body{font-family:"Noto Sans","DejaVu Sans",sans-serif;color:#1f2430;font-size:7.7pt;line-height:1.3;margin:0}
.emoji{font-family:"Noto Color Emoji";font-style:normal}
.ur{font-family:"Noto Nastaliq Urdu",serif;direction:rtl;text-align:right;line-height:2;font-size:8.2pt}
h1{font-size:11.6pt;color:var(--c);margin:0 0 .4mm;line-height:1.15}
.sub{color:#5b6475;font-size:7.2pt;margin-bottom:1.6mm}
h2{font-size:8.6pt;color:#fff;background:var(--c);padding:.7mm 2mm;border-radius:1.5mm;margin:1.6mm 0 .9mm}
p{margin:.5mm 0}
.box{border-radius:1.4mm;padding:.9mm 1.9mm;margin:.8mm 0}
.box .t{font-weight:bold;font-size:7.8pt;display:block;margin-bottom:.3mm}
.def{background:#e8f1fc;border-left:3px solid #1d5fa8}.def .t{color:#1d5fa8}
.eg{background:#e7f6ee;border-left:3px solid #1e7a4a}.eg .t{color:#1e7a4a}
.trick{background:#fff6d8;border-left:3px solid #e0a800}.trick .t{color:#8a6200}
.quiz{background:#f2ecfb;border-left:3px solid #6a3fa0}.quiz .t{color:#6a3fa0}
.warn{background:#fdecec;border-left:3px solid #a8202a}.warn .t{color:#a8202a}
table{border-collapse:collapse;width:100%;font-size:7.3pt;margin:.8mm 0}
th{background:var(--c);color:#fff;padding:.6mm 1.2mm;text-align:left}
td{border:1px solid #d7dce5;padding:.6mm 1.2mm;vertical-align:top}
tr:nth-child(even) td{background:#f6f8fb}
ol.q{margin:.5mm 0 0;padding-left:4.4mm;font-size:7.7pt}
ol.q li{margin:.9mm 0}
.foot{color:#5b6475;font-size:6.8pt;border-top:1px solid #d7dce5;margin-top:2mm;padding-top:1mm}
"""


def render_note(lesson, body_html, colour, dest):
    html = ("<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
            "<title>%s</title><style>:root{--c:%s}%s</style></head><body>%s"
            "<div class='foot'>Revision note, %s Chapter %s, section %s. "
            "Built from your own textbook.</div></body></html>"
            % (lesson["title"], colour, CSS, body_html,
               lesson["subject_label"], lesson["chapter"], lesson["ref"]))
    tmp = dest.replace(".pdf", ".html")
    open(tmp, "w", encoding="utf-8").write(html)
    subprocess.run(["google-chrome", "--headless=new", "--no-pdf-header-footer",
                    "--disable-gpu", "--print-to-pdf=" + dest, "file://" + tmp],
                   capture_output=True)
    os.remove(tmp)                      # the repo keeps PDFs, not intermediates
    txt = subprocess.run(["pdftotext", dest, "-"], capture_output=True).stdout.decode("utf-8", "ignore")
    pages = subprocess.run(["pdfinfo", dest], capture_output=True).stdout.decode()
    npages = next((l.split()[-1] for l in pages.splitlines() if l.startswith("Pages")), "?")
    return npages, txt.count("—"), ("KEY-" in txt or "Marking:" in txt)


def render_audio(script_text, slug, date, target_words):
    sp = os.path.join(AUDIO, "%s-STORY-script-urdu.txt" % slug)
    open(sp, "w", encoding="utf-8").write(script_text)
    mp3 = os.path.join(AUDIO, "%s-URDU-audio-%s.mp3" % (slug, date))
    subprocess.run(["python3", TTS, sp, mp3], capture_output=True)
    ogg = os.path.join(AUDIO, "ogg", "%s-%s.ogg" % (slug, date))
    os.makedirs(os.path.dirname(ogg), exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-i", mp3, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                    "-c:a", "libopus", "-b:a", "64k", "-vbr", "on",
                    "-ar", "24000", "-ac", "1", ogg], capture_output=True)
    d = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", mp3], capture_output=True).stdout.decode().strip()
    return float(d or 0) / 60, len(script_text.split())


def _topic_key(slug):
    """Match how the site normalises a filename into a lesson key."""
    sys.path.insert(0, "/home/atif/projects/education/seemab-edu")
    import build as sitebuild
    return sitebuild.topic_key(slug)


def mark_done(ref_key, note_rel, audio_slug, summary):
    plan = json.load(open(PLAN, encoding="utf-8"))
    for l in plan["lessons"]:
        if (l["subject"], l["chapter"], l["ref"]) == ref_key:
            l["note"] = note_rel
            l["audio"] = audio_slug
            l["done"] = True
    json.dump(plan, open(PLAN, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    sums = json.load(open(SUMS, encoding="utf-8"))
    sums[_topic_key(audio_slug)] = summary
    json.dump(sums, open(SUMS, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def build(lessons, colour, date="2026-09-30"):
    plan = {(l["subject"], l["chapter"], l["ref"]): l
            for l in json.load(open(PLAN, encoding="utf-8"))["lessons"]}
    for item in lessons:
        key = (item["subject"], item["chapter"], item["ref"])
        meta = plan.get(key)
        if not meta:
            print("  !! not in the plan:", key)
            continue
        dest = os.path.join(NOTES, item["slug"] + "-notes-%s.pdf" % date)
        npages, em, leak = render_note(meta, item["note"], colour, dest)
        mins, words = render_audio(item["script"], item["slug"], date, meta["target_words"])
        mark_done(key, os.path.relpath(dest, ROOT), item["slug"], item["summary"])
        flag = ""
        if em:
            flag += " EM-DASH!"
        if leak:
            flag += " KEY-LEAK!"
        print("  %-34s note %sp  audio %.1f min (target %.1f, %d words)%s"
              % (item["ref"] + " " + meta["title"][:26], npages, mins,
                 meta["target_minutes"], words, flag))
