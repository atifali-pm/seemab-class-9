#!/usr/bin/env python3
"""Build the topic manifest for the backfill.

Every chapter Seemab has already studied is broken into the topics her book
actually has. The per-chapter reference notes already carry that breakdown, in
three different shapes depending on when they were written, so all three are
parsed here rather than re-reading 800 image-only book pages.

Output: seemab-reports/topic-map.json, which drives note and audio generation
and is also what the website lists.
"""
import glob
import json
import os
import re

MEM = "/home/atif/.claude/projects/-home-atif-projects-education-seemab-class-9/memory/"
OUT = "/home/atif/projects/education/seemab/class-9/seemab-reports/topic-map.json"

# What she has already been taught, from project_current_chapters.
STUDIED = {
    "physics":   [1, 2, 3, 4, 5, 6, 9],
    "chemistry": list(range(1, 11)),
    "biology":   list(range(1, 8)),
    "islamiat":  [1, 2, 3, 4],
    "math":      [1, 2, 4, 5, 7, 10, 11],
}
LABEL = {"physics": "Physics", "chemistry": "Chemistry", "biology": "Biology",
         "islamiat": "Islamiat", "math": "Mathematics", "quran": "Tarjuma-tul-Quran"}

# "### 4.1 Title", "- 4.1 Title", "  - 4.3.2 Title"
NUMBERED = re.compile(r"^\s*(?:#{2,4}\s*|-\s*|\*\s*)([0-9]+\.[0-9](?:\.[0-9])?)\s+([^\n(]{3,70})")
# Islamiat lessons: "- **(الف) ...**"
URDU_LESSON = re.compile(r"^\s*-\s*\*\*\((الف|ب|ج|د|ہ)\)\s*([^*]{3,90})\*\*")


def clean(s):
    s = re.sub(r"\[\[[^\]]*\]\]", "", s)
    s = re.sub(r"[*_`]", "", s)
    return " ".join(s.split()).strip(" .:-,")


def parse(path):
    out, seen = [], set()
    for line in open(path, encoding="utf-8"):
        m = NUMBERED.match(line)
        if m:
            num, title = m.group(1), clean(m.group(2))
            if not title or num in seen:
                continue
            seen.add(num)
            out.append({"ref": num, "title": title})
            continue
        m = URDU_LESSON.match(line)
        if m:
            title = clean(m.group(2))
            key = m.group(1)
            if title and key not in seen:
                seen.add(key)
                out.append({"ref": "(%s)" % key, "title": title})
    return out


def main():
    manifest, missing = [], []
    for subject, chapters in STUDIED.items():
        for ch in chapters:
            pats = [MEM + "reference_%s_ch%02d.md" % (subject, ch),
                    MEM + "reference_%s_unit%02d.md" % (subject, ch),
                    MEM + "reference_%s_bab%02d.md" % (subject, ch)]
            path = next((p for p in pats if os.path.exists(p)), None)
            if not path:
                missing.append("%s ch%d" % (subject, ch))
                continue
            topics = parse(path)
            if not topics:
                missing.append("%s ch%d (file exists, no topics parsed)" % (subject, ch))
                continue
            for t in topics:
                manifest.append({
                    "subject": subject,
                    "subject_label": LABEL[subject],
                    "chapter": ch,
                    "ref": t["ref"],
                    "title": t["title"],
                    "slug": "%s-ch%02d-%s" % (subject, ch,
                                              re.sub(r"[^a-z0-9]+", "-", t["title"].lower()).strip("-")[:38]),
                    "note": None,      # filled in when the note PDF is built
                    "audio": None,     # filled in when the recording is made
                })
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({"generated": "2026-09-30", "topics": manifest}, fh,
                  ensure_ascii=False, indent=1)

    by_sub = {}
    for t in manifest:
        by_sub.setdefault(t["subject_label"], []).append(t)
    print("TOPIC MAP for chapters already studied\n")
    for k in sorted(by_sub, key=lambda x: -len(by_sub[x])):
        chs = sorted({t["chapter"] for t in by_sub[k]})
        print("  %-18s %3d topics across %d chapters %s" % (k, len(by_sub[k]), len(chs), chs))
    print("\n  TOTAL %d topics -> %d notes + %d audio lessons" % (len(manifest), len(manifest), len(manifest)))
    if missing:
        print("\n  NO TOPIC INDEX YET (needs reading the book itself):")
        for m in missing:
            print("    -", m)
    print("\n  written to", OUT)


if __name__ == "__main__":
    main()
