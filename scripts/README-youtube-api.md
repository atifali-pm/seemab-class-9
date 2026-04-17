# YouTube API Setup — One-Time Setup for Seemab's Video Search

The `yt_search.py` tool uses the **YouTube Data API v3** to find NBF/Federal Board Class 9 videos on demand and rank them by relevance (publisher, board, class level, edition year).

## One-time setup (~5 minutes)

### Step 1 — Get a free API key from Google Cloud Console

1. Go to **https://console.cloud.google.com/**
2. Create a new project called **"Seemab Class 9"** (or use any existing project).
3. From the left menu: **APIs & Services → Library**.
4. Search for **"YouTube Data API v3"** and click **Enable**.
5. Go to **APIs & Services → Credentials**.
6. Click **Create Credentials → API key**. Copy the key.
7. (Recommended) Click **Restrict key** and limit it to only "YouTube Data API v3".

### Step 2 — Save the key locally

```bash
# Paste your API key on a single line inside this file
echo 'PASTE_YOUR_KEY_HERE' > ~/.seemab-yt-api-key
chmod 600 ~/.seemab-yt-api-key
```

That's it. The script will automatically pick it up.

## Usage

### Free-text query

```bash
python3 scripts/yt_search.py "Chemistry Stoichiometry empirical formula Class 9 NBF"
```

### By subject + chapter

```bash
python3 scripts/yt_search.py --subject chemistry --chapter 6
python3 scripts/yt_search.py --subject physics --unit 5
python3 scripts/yt_search.py --subject biology --chapter 7 --topic "photosynthesis"
```

### Output formats

```bash
--format markdown    # default — a ranked table
--format json        # machine-readable for scripting
--format urls        # one URL per line, for piping
```

### Check quota usage

```bash
python3 scripts/yt_search.py --quota
# Shows units used today and remaining quota.
```

## How the ranking works

Each video is scored against signals in the title + description + channel name:

| Signal | Points |
|---|---|
| Mentions "NBF" / "National Book Foundation" | +5 each |
| Mentions "Federal Board" / "FBISE" | +5 |
| Mentions "Class 9" / "9th Class" | +3 |
| Published in 2026 | +4 |
| Published in 2025 | +3 |
| Says "One Shot" / "Complete Exercise" / "Full Exercise" | +2 |
| Says "New Book" | +2 |
| Mentions Punjab Board / PCTB | **−6** |
| Mentions Sindh Board | **−6** |
| Mentions CBSE / NCERT (Indian curriculum) | **−6** |
| Mentions Cambridge / IGCSE / O Level | **−4** |
| No "Class 9" mention | **−5** |

Videos with negative scores are still returned but sorted to the bottom. This lets you see competing-curriculum results to spot false positives.

## Quota budget

- **100 units per search** (standard YouTube API rate)
- **Default free daily quota:** 10,000 units = **100 searches/day**
- Results are cached locally for 7 days in `~/.seemab-yt-cache/`, so repeated queries don't burn quota.

Typical use (a few searches per day when asking for specific chapters) stays well within free limits.

## Files this tool touches

- `~/.seemab-yt-api-key` — your API key (never committed to repo)
- `~/.seemab-yt-api-usage.log` — daily usage log for quota tracking
- `~/.seemab-yt-cache/` — 7-day query cache

None of these are in the repo.
