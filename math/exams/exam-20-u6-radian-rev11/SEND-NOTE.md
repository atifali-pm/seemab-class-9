# Maths exam-20: Unit 6 radian measure and sector, with Unit 11 probability revision

**Built and SENT 2026-10-01 on Atif's instruction ("send Seemab Maths exam today with notes and audios").**
38 marks = 10 MCQ + 3 x 4 + 2 x 8, 1h30m, no optional questions. One page. Answer key HELD until she submits.
Source kept at `math/exam-template/exam-20-source/` (wkhtmltopdf).

## Shape

| Section | New: Unit 6 (6.1 radian, 6.2 sector) | Revision: Unit 11 probability | Total |
|---|---|---|---|
| A, MCQs 10 x 1 | 7 | 3 | 10 |
| B, Short 3 x 4 | 12 | 0 | 12 |
| C, Long 2 x 8 | 8 (Q.5) | 8 (Q.6) | 16 |
| **Total** | **27 (71%)** | **11 (29%)** | **38** |

## Sent alongside it

- `seemab-reports/revision/math-u06-part2-aasan-notes-2026-10-01.pdf`, one page on radian measure, arc length
  and sector area.
- `seemab-reports/revision/audio/ogg/math-u06-part2-2026-10-01.ogg`, 5 minutes, Urdu.

Both quiz questions on that note are on this paper: the radian definition with the 150 degree conversion
(Q.4(i) and Q.2(i)), and the r = 14 cm arc = 22 cm sector (Q.5(iii)).

## The revision half is aimed at one recorded failure

On Maths exam-19 (2026-09-23, 43/50) **Q.6 on probability was not attempted at all**, the single largest loss
on that paper. Q.6 here is that question re-set: same shape, different numbers (5 red, 4 green, 3 blue against
exam-19's 5 red, 3 green, 2 blue), with the sub-parts changed so it cannot be answered from memory. Any genuine
attempt is the thing to look for, not the mark.

## Verification

- Every one of the 19 numeric answers independently re-derived in Python, not taken from the draft: all four
  numeric MCQs, both Q.2 conversions, both Q.3 sector results, all three Q.5 parts and all six Q.6 probabilities.
- Book content checked by reading her own p118 as an image: `l = r0` from 6.2.1 and `A = 1/2 r^2 0` from 6.2.2,
  both derived on that page.
- **Repeat check** run against all 19 prior Maths papers with `pdftotext -layout`. One real collision found and
  fixed: "The probability of an impossible event is" was already an MCQ on an earlier paper, so MCQ 8 became the
  fair-coin item instead. The answer stayed C so the letter balance did not move. Two further hits were false
  alarms: "270 degrees" appears only as a distractor in a polygon question, and the bag-of-balls shape is the
  deliberate exam-19 re-test described above.
- Answer letters **C A B D C A B C D A**, balance A=3 B=2 C=3 D=2, none consecutive.
- No em dashes in either file.
