#!/usr/bin/env python3
"""Turn the raw topic map into the lesson plan the backfill actually builds.

Two rules, both agreed with Atif on 2026-09-30:

1. Sub-topics under one parent become a single lesson. Chemistry 4.3.1 to 4.3.5
   are the five periodicity trends and they teach as one lesson on trends, not
   as five fragments.
2. A lesson's recording is sized to how much the book actually has on it, from
   about two minutes up to five, instead of padding everything to five.
"""
import io
import json
import re
from collections import OrderedDict

MAP = "/home/atif/projects/education/seemab/class-9/seemab-reports/topic-map.json"
OUT = "/home/atif/projects/education/seemab/class-9/seemab-reports/lesson-plan.json"

# words per minute for ur-PK-UzmaNeural at -15%, measured over 8 recordings
WPM = 135
MEM = "/home/atif/.claude/projects/-home-atif-projects-education-seemab-class-9/memory/"
# how much the book has on a topic -> how long the lesson should run
SIZES = [(400, 300), (900, 420), (1600, 560), (10 ** 9, 680)]


def _ref_file(subject, chapter):
    import os
    for pat in ("reference_%s_ch%02d.md", "reference_%s_unit%02d.md", "reference_%s_bab%02d.md"):
        p = MEM + pat % (subject, chapter)
        if os.path.exists(p):
            return p
    return None


_CACHE = {}


def content_len(subject, chapter, refs):
    """Characters the reference notes devote to these topics, as a size proxy."""
    key = (subject, chapter)
    if key not in _CACHE:
        p = _ref_file(subject, chapter)
        _CACHE[key] = io.open(p, encoding="utf-8").read().splitlines() if p else []
    lines = _CACHE[key]
    wanted = {r for r in refs}
    total, grabbing = 0, False
    for ln in lines:
        m = re.match(r"^\s*(?:#{2,4}\s*|-\s*|\*\s*)([0-9]+\.[0-9](?:\.[0-9])?)\s+", ln)
        if m:
            grabbing = m.group(1) in wanted
            if grabbing:
                total += len(ln)
            continue
        if grabbing:
            total += len(ln)
    return total


def parent(ref):
    """'4.3.2' -> '4.3'.  '4.3' -> '4.3'.  '(الف)' -> itself."""
    if not re.match(r"^\d+\.\d", ref):
        return ref
    bits = ref.split(".")
    return ".".join(bits[:2]) if len(bits) > 2 else ref


def main():
    topics = json.load(open(MAP, encoding="utf-8"))["topics"]
    groups = OrderedDict()
    for t in topics:
        key = (t["subject"], t["chapter"], parent(t["ref"]))
        groups.setdefault(key, []).append(t)

    lessons = []
    for (subject, chapter, ref), members in groups.items():
        # The parent's own entry, if the book has one, gives the lesson its name.
        head = next((m for m in members if m["ref"] == ref), None)
        kids = [m for m in members if m is not head]
        title = head["title"] if head else members[0]["title"]
        clen = content_len(subject, chapter, [m["ref"] for m in members])
        words = next(w for lim, w in SIZES if clen <= lim)
        lessons.append({
            "subject": subject,
            "subject_label": members[0]["subject_label"],
            "chapter": chapter,
            "ref": ref,
            "title": title,
            "covers": [{"ref": m["ref"], "title": m["title"]} for m in members],
            "source_chars": clen,
            "target_words": words,
            "target_minutes": round(words / WPM, 1),
            "slug": "%s-ch%02d-%s" % (subject, chapter,
                                      re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:36]),
            "note": None,
            "audio": None,
            "done": False,
        })

    json.dump({"generated": "2026-09-30", "lessons": lessons},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    from collections import Counter
    c = Counter(l["subject_label"] for l in lessons)
    mins = sum(l["target_minutes"] for l in lessons)
    print("LESSON PLAN (topics merged, audio sized to content)\n")
    for k, v in c.most_common():
        m = sum(l["target_minutes"] for l in lessons if l["subject_label"] == k)
        print("  %-12s %3d lessons   %5.0f min of audio" % (k, v, m))
    print("\n  %-12s %3d lessons   %5.0f min  (%.1f hours)" % ("TOTAL", len(lessons), mins, mins / 60))
    print("  was %d separate topics at 5 min each = %.1f hours" % (len(topics), len(topics) * 5 / 60))
    print("\n  written to", OUT)


if __name__ == "__main__":
    main()
