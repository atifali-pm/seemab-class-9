#!/usr/bin/env python3
"""Pull the quiz questions and their answers out of the note sources.

Every note ends with two questions, and its answers sit in an HTML comment that
never reaches the PDF she reads. This collects both into one file so the website
can ask the question, take her attempt, and then show the model answer.

Output: seemab-reports/quiz.json
"""
import glob
import html
import json
import os
import re

ROOT = "/home/atif/projects/education/seemab/class-9"
OUT = os.path.join(ROOT, "seemab-reports", "quiz.json")

# a lesson block ends at the next page break or the end of the file
QUIZ = re.compile(r'<div class="(?:box )?quiz">(.*?)</div>\s*(?=<!--|</div>)', re.S)
LI = re.compile(r"<li[^>]*>(.*?)</li>", re.S)
QR = re.compile(r'<div class="qr">(.*?)</div>', re.S)
KEY = re.compile(r"<!--\s*KEY[-\s]?([A-Z]*)\s*(.*?)-->", re.S)
H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)


def clean(s):
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return " ".join(s.split()).strip()


def blocks(text):
    """Split a source into one chunk per lesson, so a quiz keeps its own answers."""
    parts = re.split(r'(?=<div class="pg")', text)
    if len(parts) > 1:
        return parts
    # a backfill file holds one lesson per note string
    return re.split(r'(?=<h1)', text)


def harvest(path, label):
    out = []
    text = open(path, encoding="utf-8").read()
    for b in blocks(text):
        qm = QUIZ.search(b)
        if not qm:
            continue
        qs = [clean(x) for x in LI.findall(qm.group(1))] or [clean(x) for x in QR.findall(qm.group(1))]
        qs = [q for q in qs if len(q) > 15]
        if not qs:
            continue
        km = KEY.search(b)
        ans = clean(km.group(2)) if km else ""
        hm = H1.search(b)
        title = clean(hm.group(1)) if hm else label
        out.append({"title": title, "source": label,
                    "questions": qs, "answer": ans})
    return out


def main():
    items = []
    for p in sorted(glob.glob(os.path.join(ROOT, "seemab-reports", "daily", "sources", "*.html"))):
        items += harvest(p, "Daily notes " + os.path.basename(p).replace("aasan-notes-", "").replace(".html", ""))
    for p in sorted(glob.glob(os.path.join(ROOT, "scripts", "backfill", "*_ch*.py"))):
        items += harvest(p, os.path.basename(p).replace(".py", "").replace("_", " "))

    with_ans = [i for i in items if i["answer"]]
    json.dump({"generated": "2026-10-01", "items": items},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("lessons with a quiz : %d" % len(items))
    print("questions in total   : %d" % sum(len(i["questions"]) for i in items))
    print("with a model answer  : %d" % len(with_ans))
    missing = [i["title"][:52] for i in items if not i["answer"]]
    if missing:
        print("\nno answer found for:")
        for m in missing[:10]:
            print("   -", m)
    print("\nwritten to", OUT)


if __name__ == "__main__":
    main()
