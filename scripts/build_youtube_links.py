#!/usr/bin/env python3
"""Build youtube-links.md files for each subject from extracted playlist data."""
import re
from pathlib import Path
from collections import defaultdict

REPO = Path("/home/atif/projects/education/seemab/class-9")
PLAYLIST_DIR = Path("/tmp/playlists")


def read_playlist(name):
    """Read a playlist file and return list of (idx, title, url) tuples.

    Format: idx|title|url, but title may contain pipes. URL is the last field
    (always starts with https://), so we split from the right to get URL first.
    """
    entries = []
    f = PLAYLIST_DIR / f"{name}.txt"
    if not f.exists():
        return entries
    for line in f.read_text().splitlines():
        if not line.strip():
            continue
        # URL is always the last segment (after the last pipe)
        head, _, url = line.rpartition("|")
        if not url.startswith("http"):
            continue
        # Head is "idx|title" where title may itself contain pipes
        idx, _, title = head.partition("|")
        entries.append((idx.strip(), title.strip(), url.strip()))
    return entries


def extract_chapter_num(title, patterns):
    """Try each regex pattern, return first matching chapter/unit number as int."""
    for pat in patterns:
        m = re.search(pat, title, re.IGNORECASE)
        if m:
            try:
                return int(m.group(1))
            except ValueError:
                pass
    return None


def group_by_chapter(entries, patterns):
    """Group entries by chapter. Returns dict {chapter_num: [entries]} + unmatched list."""
    grouped = defaultdict(list)
    unmatched = []
    for e in entries:
        ch = extract_chapter_num(e[1], patterns)
        if ch is not None:
            grouped[ch].append(e)
        else:
            unmatched.append(e)
    return grouped, unmatched


def render_chapter_section(ch_num, entries, ch_title=""):
    lines = [f"### Chapter {ch_num}" + (f" — {ch_title}" if ch_title else "")]
    lines.append("")
    lines.append("| # | Title | URL |")
    lines.append("|---|---|---|")
    for idx, title, url in entries:
        safe_title = title.replace("|", "\\|")
        lines.append(f"| {idx} | {safe_title} | [watch]({url}) |")
    lines.append("")
    return "\n".join(lines)


def render_flat_section(entries, heading="Videos"):
    lines = [f"### {heading}", "", "| # | Title | URL |", "|---|---|---|"]
    for idx, title, url in entries:
        safe_title = title.replace("|", "\\|")
        lines.append(f"| {idx} | {safe_title} | [watch]({url}) |")
    lines.append("")
    return "\n".join(lines)


# =============================================================================
# MATH
# =============================================================================

def build_math():
    main = read_playlist("math")
    topic = read_playlist("math-topic")
    ch_titles = {
        1: "Real Numbers", 2: "Logarithms", 3: "Sets and Relations",
        4: "Factorization & Algebraic Manipulation", 5: "Linear Equations & Inequalities",
        6: "Trigonometry and Bearing", 7: "Coordinate Geometry",
        8: "Geometry of Straight Lines", 9: "Geometry and Polygons",
        10: "Practical Geometry", 11: "Basic Statistics",
    }
    patterns = [r"chapter\s*(\d+)", r"unit\s*(\d+)", r"\bex\.?\s*(\d+)\.", r"exercise\s*(\d+)\."]

    # main playlist grouped by chapter
    grouped_main, un_main = group_by_chapter(main, patterns)
    grouped_topic, un_topic = group_by_chapter(topic, patterns)

    out = ["# Math — YouTube Video Links (NBF / Federal Board Class 9)", ""]
    out.append("## Two playlists available")
    out.append("")
    out.append("### Primary: **MathPhysics** channel — exercise-by-exercise")
    out.append("[Full Playlist](https://www.youtube.com/playlist?list=PLzHxfZr8Ce_nGXfrK-V3iaiU4YYBZWhlS) — 72 videos, covers Units 1-11 including all exercises and miscellaneous exercises.")
    out.append("")
    out.append("### Topic-level: **deep-dive per exercise question**")
    out.append("[Full Playlist](https://www.youtube.com/playlist?list=PLI-NxcTUPiPybCp6szIeu5gA_fBqNZUjr) — 27 videos, Unit 1 only currently, broken down question-by-question.")
    out.append("")
    out.append("**Verified:** NBF / Federal Board Class 9, current edition (New Book 2025).")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Videos organized by unit (primary playlist)")
    out.append("")
    for ch in sorted(grouped_main.keys()):
        out.append(render_chapter_section(ch, grouped_main[ch], ch_titles.get(ch, "")))

    if un_main:
        out.append(render_flat_section(un_main, "Other videos (full-book MCQs etc.)"))

    if grouped_topic or un_topic:
        out.append("---")
        out.append("")
        out.append("## Topic-level deep-dive (secondary playlist, Unit 1)")
        out.append("")
        for ch in sorted(grouped_topic.keys()):
            out.append(render_chapter_section(ch, grouped_topic[ch], ch_titles.get(ch, "") + " (deep-dive)"))
        if un_topic:
            out.append(render_flat_section(un_topic, "Topic-level: other"))

    (REPO / "math/notes/youtube-links.md").write_text("\n".join(out))
    print(f"Math: {len(main)} main + {len(topic)} topic videos")


# =============================================================================
# PHYSICS
# =============================================================================

def build_physics():
    entries = read_playlist("physics")
    ch_titles = {
        1: "Physical Quantities & Measurement", 2: "Kinematics",
        3: "Dynamics-I", 4: "Dynamics-II", 5: "Pressure & Deformation",
        6: "Work & Energy", 7: "Density & Temperature",
        8: "Magnetism", 9: "Nature of Science",
    }
    patterns = [r"unit\s*(\d+)", r"chapter\s*(\d+)"]
    grouped, un = group_by_chapter(entries, patterns)

    out = ["# Physics — YouTube Video Links (NBF / FBISE Class 9)", ""]
    out.append("[Full Playlist](https://www.youtube.com/playlist?list=PLDSXrcPEv-zX8QFHVh_kJMtquhjMISyLg) — 21 videos, current NBF edition, unit numbers match Seemab's book.")
    out.append("")
    out.append("**Verified:** NBF / FBISE Class 9, unit numbering aligned with Seemab's current textbook.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Videos organized by unit")
    out.append("")
    for ch in sorted(grouped.keys()):
        out.append(render_chapter_section(ch, grouped[ch], ch_titles.get(ch, "")))
    if un:
        out.append(render_flat_section(un, "Other videos"))

    (REPO / "physics/notes/youtube-links.md").write_text("\n".join(out))
    print(f"Physics: {len(entries)} videos")


# =============================================================================
# CHEMISTRY
# =============================================================================

def build_chemistry():
    main = read_playlist("chemistry")
    topic = read_playlist("chemistry-topic")
    ch_titles = {
        1: "Nature of Chemistry in Science", 2: "Matter", 3: "Atomic Structure",
        4: "Periodic Table and Periodicity", 5: "Chemical Bonding",
        6: "Stoichiometry", 7: "Electrochemistry", 8: "Energetics",
        9: "Chemical Equilibrium", 10: "Acids, Bases and Salts",
        11: "Environmental Chemistry — Air", 12: "Environmental Chemistry — Water",
        13: "Organic Chemistry", 14: "Hydrocarbons", 15: "Biochemistry",
        16: "Empirical Data Collection & Analysis", 17: "Separation Techniques",
        18: "Qualitative Analysis", 19: "Chromatography",
    }
    patterns = [r"chapter\s*(\d+)"]
    grouped_main, un_main = group_by_chapter(main, patterns)
    grouped_topic, un_topic = group_by_chapter(topic, patterns)

    out = ["# Chemistry — YouTube Video Links (NBF / Federal Board Class 9)", ""]
    out.append("## Two playlists available")
    out.append("")
    out.append("### Primary: **Complete Exercise per chapter**")
    out.append("[Full Playlist](https://www.youtube.com/playlist?list=PLlsg14empYaqHcT71nLmMZf9FKdSG3joQ) — 19 videos, one per chapter (Ch 1-19), complete exercise solutions.")
    out.append("")
    out.append("### Topic-level: **deep-dive per topic**")
    out.append("[Full Playlist](https://www.youtube.com/playlist?list=PLI-NxcTUPiPwRyLnf_Vetfk0PZFBa2PXh) — 12 videos, Chapter 1 only currently, broken into individual topics.")
    out.append("")
    out.append("**Verified:** NBF / Federal Board Class 9, New Book 2025.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Videos organized by chapter (primary playlist)")
    out.append("")
    for ch in sorted(grouped_main.keys()):
        out.append(render_chapter_section(ch, grouped_main[ch], ch_titles.get(ch, "")))

    if grouped_topic or un_topic:
        out.append("---")
        out.append("")
        out.append("## Topic-level deep-dive (secondary playlist)")
        out.append("")
        for ch in sorted(grouped_topic.keys()):
            out.append(render_chapter_section(ch, grouped_topic[ch], ch_titles.get(ch, "") + " (deep-dive)"))
        if un_topic:
            out.append(render_flat_section(un_topic, "Topic-level: other"))

    (REPO / "chemistry/notes/youtube-links.md").write_text("\n".join(out))
    print(f"Chemistry: {len(main)} main + {len(topic)} topic videos")


# =============================================================================
# BIOLOGY
# =============================================================================

def build_biology():
    oneshot = read_playlist("biology-oneshot")
    qa = read_playlist("biology-qa")
    topic = read_playlist("biology-topic")
    ch_titles = {
        1: "Science of Biology", 2: "Biodiversity", 3: "The Cell",
        4: "Cell Cycle", 5: "Tissues, Organs, Organ Systems",
        6: "Molecular Biology", 7: "Metabolism", 8: "Plant Physiology",
        9: "Plant Reproduction", 10: "Evolution",
    }
    patterns = [r"chapter\s*(\d+)"]
    g_oneshot, u_oneshot = group_by_chapter(oneshot, patterns)
    g_qa, u_qa = group_by_chapter(qa, patterns)
    g_topic, u_topic = group_by_chapter(topic, patterns)

    out = ["# Biology — YouTube Video Links (NBF / Federal Board Class 9)", ""]
    out.append("## Three playlists available")
    out.append("")
    out.append("### Primary: **One-Shot chapter overviews (2026)**")
    out.append("[Full Playlist](https://www.youtube.com/playlist?list=PLBKBA4bPlKl5FWC8bbiZHpmsC7D6NU9wz) — 21 videos, comprehensive single-video-per-chapter walkthroughs, Federal Board New Book 2026.")
    out.append("")
    out.append("### Alternative: **Short Questions & Answers (2025)**")
    out.append("[Full Playlist](https://www.youtube.com/playlist?list=PLlsg14empYarKx6xKCurBuReLIhQJR-A_) — 8 videos, short-question solutions per chapter. Best for exam prep.")
    out.append("")
    out.append("### Topic-level: **Chapter 5 deep-dive**")
    out.append("[Full Playlist](https://www.youtube.com/playlist?list=PLI-NxcTUPiPzT3l0vv2X2eX5WOzCVjk5F) — 9 videos, Chapter 5 only currently, broken into individual topics.")
    out.append("")
    out.append("**Verified:** NBF / Federal Board Class 9, New Book 2025/2026 editions.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Videos organized by chapter")
    out.append("")
    all_chapters = sorted(set(list(g_oneshot.keys()) + list(g_qa.keys()) + list(g_topic.keys())))
    for ch in all_chapters:
        out.append(f"### Chapter {ch} — {ch_titles.get(ch, '')}")
        out.append("")
        if ch in g_oneshot:
            out.append(render_flat_section(g_oneshot[ch], "One-Shot (primary)"))
        if ch in g_qa:
            out.append(render_flat_section(g_qa[ch], "Short Questions & Answers"))
        if ch in g_topic:
            out.append(render_flat_section(g_topic[ch], "Topic-level deep-dive"))

    (REPO / "biology/notes/youtube-links.md").write_text("\n".join(out))
    print(f"Biology: {len(oneshot)} oneshot + {len(qa)} qa + {len(topic)} topic videos")


# =============================================================================
# ENGLISH
# =============================================================================

def build_english():
    primary = read_playlist("english-primary")
    alt = read_playlist("english-alt")
    unit_titles = {
        1: "Hazrat Muhammad: A Mercy",
        7: "Mowing by Robert Frost",
    }
    patterns = [r"unit\s*(\d+)", r"chapter\s*(\d+)"]
    g_primary, u_primary = group_by_chapter(primary, patterns)
    g_alt, u_alt = group_by_chapter(alt, patterns)

    out = ["# English — YouTube Video Links (NBF / Federal Board Class 9)", ""]
    out.append("## Two playlists available")
    out.append("")
    out.append("### Primary: **Complete exercise per unit (2026 edition)**")
    out.append("[Full Playlist](https://www.youtube.com/playlist?list=PLlsg14empYaoH0Y2f_dnIM6tVKQKYE5gN) — 7 videos, one per unit, complete exercise solutions.")
    out.append("")
    out.append("### Alternative: **Topic-level breakdown (Unit 1 only, 2025)**")
    out.append("[Full Playlist](https://www.youtube.com/playlist?list=PLBKBA4bPlKl7HSHymn6OaQwoV08IIKItp) — 6 videos, Unit 1 only, broken into Comprehension, Glossary, Q&A, Conditional Sentences, Proofreading/Precis.")
    out.append("")
    out.append("**Verified:** NBF / Federal Board Class 9, New Book 2025/2026.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Primary playlist: one video per unit")
    out.append("")
    for ch in sorted(g_primary.keys()):
        out.append(render_chapter_section(ch, g_primary[ch], unit_titles.get(ch, "")))
    if u_primary:
        out.append(render_flat_section(u_primary, "Other"))

    out.append("---")
    out.append("")
    out.append("## Alternative playlist: Unit 1 topic-level")
    out.append("")
    for ch in sorted(g_alt.keys()):
        out.append(render_chapter_section(ch, g_alt[ch], unit_titles.get(ch, "") + " (deep-dive)"))
    if u_alt:
        out.append(render_flat_section(u_alt, "Other"))

    (REPO / "english/notes/youtube-links.md").write_text("\n".join(out))
    print(f"English: {len(primary)} primary + {len(alt)} alt videos")


# =============================================================================
# URDU
# =============================================================================

def build_urdu():
    entries = read_playlist("urdu")
    patterns = [r"chapter\s*(\d+)", r"ghazal\s*(\d+)", r"unit\s*(\d+)"]
    grouped, un = group_by_chapter(entries, patterns)

    out = ["# Urdu — YouTube Video Links (NBF / Federal Board Class 9)", ""]
    out.append("[Full Playlist](https://www.youtube.com/playlist?list=PLDSXrcPEv-zXo9U8Z4L_gEG331BMbql7R) — 19 videos, chapters and ghazals from Seemab's Urdu New Book.")
    out.append("")
    out.append("**Verified:** NBF / FBISE Class 9 New Book.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## All videos (chapters and ghazals)")
    out.append("")
    out.append(render_flat_section(entries, "Full playlist"))

    (REPO / "urdu/notes/youtube-links.md").write_text("\n".join(out))
    print(f"Urdu: {len(entries)} videos")


# =============================================================================
# ISLAMIAT
# =============================================================================

def build_islamiat():
    entries = read_playlist("islamiat")
    patterns = [r"chapter\s*(\d+)", r"chap\.?\s*(\d+)", r"unit\s*(\d+)"]
    grouped, un = group_by_chapter(entries, patterns)

    out = ["# Islamiat — YouTube Video Links (FBISE Class 9)", ""]
    out.append("[Full Playlist](https://www.youtube.com/playlist?list=PL-eKXvogdP9EPiSroilAwT3Drc2nq8fTP) — 29 videos, FBISE Islamiat New Book Class 9.")
    out.append("")
    out.append("**Verified:** FBISE Class 9 Islamiat New Book.")
    out.append("")
    out.append("---")
    out.append("")
    if grouped:
        out.append("## Videos organized by chapter")
        out.append("")
        for ch in sorted(grouped.keys()):
            out.append(render_chapter_section(ch, grouped[ch]))
    if un:
        out.append(render_flat_section(un, "Other / by topic (not chapter-tagged in title)"))

    (REPO / "islamiat/notes/youtube-links.md").write_text("\n".join(out))
    print(f"Islamiat: {len(entries)} videos")


if __name__ == "__main__":
    build_math()
    build_physics()
    build_chemistry()
    build_biology()
    build_english()
    build_urdu()
    build_islamiat()
    print("\nDone. All subject files regenerated with populated video tables.")
