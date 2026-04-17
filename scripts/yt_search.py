#!/usr/bin/env python3
"""
YouTube Data API v3 search — find videos for Seemab's NBF/Federal Board Class 9 curriculum.

Usage:
  yt_search.py "Chemistry Stoichiometry Class 9 NBF"
  yt_search.py --subject chemistry --chapter 6 --topic "empirical formula"
  yt_search.py --subject physics --unit 5

Ranks results by how well the title/description match NBF / Federal Board / Class 9
/ 2025-2026 edition signals. Returns top N videos with direct URLs.

API key setup:
  1. Go to https://console.cloud.google.com/
  2. Create a project (or use existing)
  3. Enable "YouTube Data API v3"
  4. Create an API key (Credentials -> Create Credentials -> API key)
  5. Save the key to: ~/.seemab-yt-api-key  (chmod 600)

Quota: 100 units per search. Default daily limit is 10,000 units = 100 searches/day.
"""

import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
import urllib.error
from datetime import datetime

API_KEY_FILE = os.path.expanduser("~/.seemab-yt-api-key")
USAGE_LOG = os.path.expanduser("~/.seemab-yt-api-usage.log")
CACHE_DIR = os.path.expanduser("~/.seemab-yt-cache")

# Rough chapter-title reference for more specific queries
CHAPTER_TITLES = {
    "chemistry": {
        1: "Nature of Chemistry", 2: "Matter", 3: "Atomic Structure",
        4: "Periodic Table", 5: "Chemical Bonding", 6: "Stoichiometry",
        7: "Electrochemistry", 8: "Energetics", 9: "Chemical Equilibrium",
        10: "Acids Bases and Salts", 11: "Environmental Chemistry Air",
        12: "Environmental Chemistry Water", 13: "Organic Chemistry",
        14: "Hydrocarbons", 15: "Biochemistry", 16: "Empirical Data",
        17: "Separation Techniques", 18: "Qualitative Analysis",
        19: "Chromatography",
    },
    "physics": {
        1: "Physical Quantities Measurement", 2: "Kinematics",
        3: "Dynamics Newton Laws", 4: "Dynamics Torque Friction",
        5: "Pressure Deformation Hookes Law", 6: "Work Energy",
        7: "Density Temperature", 8: "Magnetism", 9: "Nature of Science",
    },
    "biology": {
        1: "Science of Biology", 2: "Biodiversity", 3: "The Cell",
        4: "Cell Cycle", 5: "Tissues Organs Organ Systems",
        6: "Molecular Biology", 7: "Metabolism", 8: "Plant Physiology",
        9: "Plant Reproduction", 10: "Evolution",
    },
    "math": {
        1: "Real Numbers", 2: "Logarithms", 3: "Sets Relations",
        4: "Factorization Algebraic Manipulation",
        5: "Linear Equations Inequalities",
        6: "Trigonometry Bearing", 7: "Coordinate Geometry",
        8: "Geometry Straight Lines", 9: "Geometry Polygons",
        10: "Practical Geometry", 11: "Basic Statistics",
    },
}


def get_api_key() -> str:
    if os.path.exists(API_KEY_FILE):
        return open(API_KEY_FILE).read().strip()
    key = os.environ.get("YOUTUBE_API_KEY")
    if key:
        return key
    sys.stderr.write(f"""ERROR: No YouTube API key found.

Set it up in one of two ways:
  1. Create file: {API_KEY_FILE}
     (chmod 600 {API_KEY_FILE})
     Then paste your API key on a single line inside.
  2. Or set env var: export YOUTUBE_API_KEY=<your-key>

Get a key at: https://console.cloud.google.com/
(Enable "YouTube Data API v3", then Credentials -> Create API key)
""")
    sys.exit(2)


def log_usage(query: str, units: int) -> None:
    """Simple per-day usage log for monitoring quota."""
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(USAGE_LOG, "a") as f:
        f.write(f"{stamp}\t{units}\t{query}\n")


def today_usage() -> int:
    """Return total units used today."""
    if not os.path.exists(USAGE_LOG):
        return 0
    today = datetime.now().strftime("%Y-%m-%d")
    total = 0
    with open(USAGE_LOG) as f:
        for line in f:
            if line.startswith(today):
                parts = line.split("\t", 2)
                if len(parts) >= 2:
                    try:
                        total += int(parts[1])
                    except ValueError:
                        pass
    return total


def cache_get(query: str) -> dict | None:
    """Retrieve cached response for a query (avoids burning quota on repeats)."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    safe = re.sub(r"[^a-zA-Z0-9_-]", "_", query)[:80]
    path = os.path.join(CACHE_DIR, f"{safe}.json")
    if os.path.exists(path):
        # Cache is valid for 7 days
        age_days = (datetime.now().timestamp() - os.path.getmtime(path)) / 86400
        if age_days < 7:
            return json.load(open(path))
    return None


def cache_put(query: str, data: dict) -> None:
    os.makedirs(CACHE_DIR, exist_ok=True)
    safe = re.sub(r"[^a-zA-Z0-9_-]", "_", query)[:80]
    path = os.path.join(CACHE_DIR, f"{safe}.json")
    with open(path, "w") as f:
        json.dump(data, f)


def search(query: str, max_results: int = 15, use_cache: bool = True) -> dict:
    if use_cache:
        cached = cache_get(query)
        if cached:
            return cached

    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "relevanceLanguage": "en",
        "key": get_api_key(),
    }
    full_url = f"{url}?{urllib.parse.urlencode(params)}"

    try:
        with urllib.request.urlopen(full_url, timeout=20) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")
        sys.stderr.write(f"HTTP {e.code} from YouTube API:\n{err}\n")
        sys.exit(1)

    log_usage(query, 100)
    cache_put(query, data)
    return data


def score_video(item: dict, target_years: tuple[int, ...] = (2026, 2025)) -> tuple[int, list[str]]:
    """Score a video's relevance to NBF/Federal Board/Class 9. Return (score, reasons)."""
    title = item["snippet"]["title"]
    description = item["snippet"].get("description", "")
    channel = item["snippet"]["channelTitle"]
    combined = f"{title} {description} {channel}".lower()

    score = 0
    reasons: list[str] = []

    # Strong publisher/board signals (heavy weight)
    if re.search(r"\bnbf\b", combined):
        score += 5; reasons.append("NBF")
    if "national book foundation" in combined:
        score += 5; reasons.append("NationalBookFoundation")
    if "federal board" in combined or re.search(r"\bfbise\b", combined):
        score += 5; reasons.append("FederalBoard")

    # Class level (required — penalize if missing)
    if "class 9" in combined or "9th class" in combined or "class ix" in combined:
        score += 3; reasons.append("Class9")
    else:
        score -= 5; reasons.append("NO_Class9_mention")

    # Edition year freshness
    for i, year in enumerate(target_years):
        if str(year) in combined:
            bonus = 4 - i  # 4 for 2026, 3 for 2025, etc.
            score += bonus
            reasons.append(f"Year{year}")
            break

    # Quality/format signals
    if "one shot" in combined or "complete exercise" in combined or "full exercise" in combined:
        score += 2; reasons.append("ComprehensiveFormat")
    if "new book" in combined:
        score += 2; reasons.append("NewBook")

    # Negative signals (competing curricula)
    if re.search(r"punjab board|punjab curriculum|pctb", combined):
        score -= 6; reasons.append("NEG_PunjabBoard")
    if re.search(r"sindh board", combined):
        score -= 6; reasons.append("NEG_SindhBoard")
    if re.search(r"cbse|ncert", combined):
        score -= 6; reasons.append("NEG_IndianCBSE")
    if re.search(r"cambridge|igcse|o.?level", combined):
        score -= 4; reasons.append("NEG_Cambridge")

    return score, reasons


def build_query(args: argparse.Namespace) -> str:
    if args.query:
        return args.query

    parts = []
    if args.subject:
        parts.append(args.subject.capitalize())
    if args.chapter or args.unit:
        n = args.chapter or args.unit
        label = "Chapter" if args.subject in ("chemistry", "biology") else "Unit"
        parts.append(f"{label} {n}")
        chmap = CHAPTER_TITLES.get(args.subject or "", {})
        if n in chmap:
            parts.append(chmap[n])
    if args.topic:
        parts.append(args.topic)

    parts += ["Class 9", "National Book Foundation", "Federal Board"]
    return " ".join(parts)


def render_markdown(query: str, scored: list[tuple[int, list[str], dict]], top_n: int) -> str:
    lines = [
        f"## YouTube search: `{query}`",
        "",
        f"**Top {min(top_n, len(scored))} results** ranked by NBF/Federal Board/Class 9 signal strength.",
        "",
        "| Rank | Score | Title | Channel | Published | URL | Signals |",
        "|---|---|---|---|---|---|---|",
    ]
    for rank, (score, reasons, item) in enumerate(scored[:top_n], 1):
        vid = item["id"]["videoId"]
        title = item["snippet"]["title"].replace("|", "\\|")
        channel = item["snippet"]["channelTitle"]
        pub = item["snippet"]["publishedAt"][:10]
        signals = ", ".join(reasons[:5])
        lines.append(f"| {rank} | {score} | {title} | {channel} | {pub} | [watch](https://www.youtube.com/watch?v={vid}) | {signals} |")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("query", nargs="?", help="Free-text query (or use --subject etc.)")
    parser.add_argument("--subject", choices=list(CHAPTER_TITLES.keys()) + ["urdu", "english", "islamiat"])
    parser.add_argument("--chapter", type=int, help="Chapter number (for Chemistry/Biology)")
    parser.add_argument("--unit", type=int, help="Unit number (for Math/Physics)")
    parser.add_argument("--topic", help="Specific topic within the chapter (optional)")
    parser.add_argument("--max-results", type=int, default=15, help="Max results to fetch from YouTube (default 15)")
    parser.add_argument("--top", type=int, default=5, help="How many top-ranked results to show (default 5)")
    parser.add_argument("--format", choices=["markdown", "json", "urls"], default="markdown")
    parser.add_argument("--no-cache", action="store_true", help="Skip the 7-day local cache")
    parser.add_argument("--quota", action="store_true", help="Show today's quota usage and exit")
    args = parser.parse_args()

    if args.quota:
        used = today_usage()
        print(f"Today's usage: {used} units ({used // 100} searches). Default daily quota: 10,000 units.")
        return

    query = build_query(args)
    if not query.strip():
        parser.error("Provide a query (positional or via --subject/--chapter/--unit)")

    data = search(query, max_results=args.max_results, use_cache=not args.no_cache)
    items = data.get("items", [])

    scored = []
    for item in items:
        if item.get("id", {}).get("kind") != "youtube#video":
            continue
        s, reasons = score_video(item)
        scored.append((s, reasons, item))
    scored.sort(key=lambda x: -x[0])

    if args.format == "json":
        out = [{"score": s, "reasons": r, "item": i} for s, r, i in scored[:args.top]]
        print(json.dumps(out, indent=2))
    elif args.format == "urls":
        for _, _, item in scored[:args.top]:
            print(f"https://www.youtube.com/watch?v={item['id']['videoId']}")
    else:
        print(render_markdown(query, scored, args.top))


if __name__ == "__main__":
    main()
