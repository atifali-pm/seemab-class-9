
## 1 October 2026 (Thursday, 1 page + 5 min per subject)

| Subject | Covered today | Next |
|---|---|---|
| Physics | **7.4 Plasma, 7.5 motion and temperature** (p174 to 176). This was part 7C, which had been skipped: the 30 Sep package jumped from 7B to 7.8 | 7.6, then 7E (7.10 to 7.12) |
| Chemistry | **11.5 Acid rain** (p159 to 160) | rest of Ch 11 P2: catalytic converters, strategies, protection |
| Biology | **source and sink, phloem sap, pressure flow, 8.3 gas exchange** (p121) | rest of 8.3, then homeostasis and excretion (p122 to 125) |
| Mathematics | **6.1 radian, 6.2 arc and sector** (p117 to 121) | **6.3 unit circle and the 30/45/60 ratios** (p122 to 124), already drafted |
| Islamiat | **Bab 4: تکبر (1) and حسد (2)** (p85 to 86). Takabbur had not gone out either | next numbered akhlaq item in Bab 4 |
| Quran | **Surah Al-Hajj, the six Hajj teachings** (the half missed on exam-03 Q.4) | awaiting Atif's word on a new surah |

Sent with Maths exam-20. Six audios, 25m35s total. Islamiat and Quran audio carry their ayat and hadith in the
Arabic voice for the first time.

**Tomorrow is FRIDAY: 2 pages per subject and 10 minutes of audio each.**

## Resume point, 1 October 2026, 4pm

**Backfill: 33 of 145.** Chemistry chapters 1 to 5 complete. To continue:

    python3 scripts/backfill/chemistry_ch06.py     # write this file first, Ch 6 is next, 7 lessons
    python3 scripts/build_quiz.py                  # re-collect the questions
    cd ../../seemab-edu && python3 build.py && npx wrangler pages deploy dist --project-name seemab-edu

Each chapter file follows `scripts/backfill/chemistry_ch05.py`: a LESSONS list of
{ref, slug, summary, note, script}, then `build(LESSONS, C)`. The renderer writes the
note PDF, the Urdu script, the audio, and marks the lesson done in lesson-plan.json.

**Order to work in:** Chemistry 6, 7, 8, 10 (9 has no index yet), then Physics, then
Biology, then Islamiat. Content for each chapter comes from the per-chapter memory
reference file, not from re-reading the book.

**Still needing a topic index before they can be planned:** the seven Maths units,
Islamiat Bab 2 to 4, Chemistry Chapter 9.

**Do not confuse the backfill with the daily package.** The backfill is revision of
chapters already finished. The daily package is the live programme and follows
`feedback-follow-the-plan-daily`: check the day first, because **Friday and Saturday
are 2 pages per subject and 10 minutes of audio**, and read the part maps before
choosing any topic.
