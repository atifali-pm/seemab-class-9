# YouTube Video Index — All Subjects (NBF / Federal Board Class 9)

Master index of verified YouTube playlists for every subject Seemab studies. Click a subject to jump to its per-chapter video table.

## Subjects

| Subject | Playlists | Total videos | Link to subject file |
|---|---|---|---|
| Math | 2 (MathPhysics full + topic-level Unit 1) | 99 | [math/notes/youtube-links.md](math/notes/youtube-links.md) |
| Physics | 1 (NBF FBISE, correct unit order) | 21 | [physics/notes/youtube-links.md](physics/notes/youtube-links.md) |
| Chemistry | 2 (Complete Exercise + topic-level Ch 1) | 31 | [chemistry/notes/youtube-links.md](chemistry/notes/youtube-links.md) |
| Biology | 3 (One-Shot 2026 + Short Q&A + topic-level Ch 5) | 38 | [biology/notes/youtube-links.md](biology/notes/youtube-links.md) |
| English | 2 (Complete Exercise 2026 + topic-level Unit 1) | 13 | [english/notes/youtube-links.md](english/notes/youtube-links.md) |
| Urdu | 1 (chapters + ghazals + nazams) | 19 | [urdu/notes/youtube-links.md](urdu/notes/youtube-links.md) |
| Islamiat | 1 (FBISE Islamiat New Book) | 29 | [islamiat/notes/youtube-links.md](islamiat/notes/youtube-links.md) |

**Total: 250 verified NBF / Federal Board Class 9 videos across 12 playlists.**

## Seemab's current chapters — one-click access

| Subject | Current chapter | Best video |
|---|---|---|
| Chemistry | Ch 6 — Stoichiometry | [Complete Exercise](https://www.youtube.com/watch?v=zx21GpWIn5g) |
| Physics | Unit 5 — Pressure & Deformation | [Short Response Qs](https://www.youtube.com/watch?v=yuGGQ_TD2K0) |
| Biology | Ch 7 — Metabolism | [One Shot chapter overview](https://www.youtube.com/watch?v=ZzEOc4kOfGM) + [Short Q&A](https://www.youtube.com/watch?v=aIm7Kixg6yA) |
| Math | Unit 4 — Factorization | [Ex 4.1](https://www.youtube.com/watch?v=NSynzQ3svK8), [4.2](https://www.youtube.com/watch?v=d6EOm_bE5-M), [4.3](https://www.youtube.com/watch?v=8kuBoUA-R6c), [4.4](https://www.youtube.com/watch?v=pinocid8Qq4), [4.5](https://www.youtube.com/watch?v=nBjSoMO-iAQ), [4.6](https://www.youtube.com/watch?v=KZQvHRMvOu8), [4.7](https://www.youtube.com/watch?v=bqeSawUxYF0), [4.8](https://www.youtube.com/watch?v=20jdFtUJe3g) |

## How these were built

1. Atif shared each subject's playlist URL on 2026-04-16.
2. Each playlist was verified as NBF / Federal Board Class 9 via the first video's title.
3. Full playlist contents extracted using `yt-dlp --flat-playlist`.
4. A Python script parsed titles and organized videos by chapter/unit into the per-subject `youtube-links.md` files.

## Re-running the extraction

To refresh these files (e.g., if a channel adds new videos):

```bash
# Extract all playlists in parallel
bash /tmp/extract_playlists.sh  # not persisted — see git history or regenerate as needed
# Rebuild subject markdown files
python3 /tmp/build_youtube_links.py
```
