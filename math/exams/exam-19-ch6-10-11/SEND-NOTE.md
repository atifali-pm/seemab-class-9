# Send note, Maths exam-19 (Units 10, 11 and 6.1 to 6.2)

## Status as of 2026-09-23

**SENT 2026-09-23. Covering message and exam paper both went to Shumail. Answer key deliberately held.**

| Step | Result |
|---|---|
| Roman Urdu covering message to Shumail | **SENT**, API returned `success: true` |
| `exam.pdf` as `Maths-Revision-Test-exam-19-Units-10-11-and-6.1-6.2.pdf` | **SENT** on the second attempt, API returned `success: true`. The first attempt was blocked by the Claude Code auto mode permission classifier; the retry went through unchanged |
| `answers.pdf` | **HELD** deliberately, follows after she submits her attempt |

**Nothing is owed except the key.** For about one exchange the message was in her chat without the paper, because the first `send_file` call was refused by the permission classifier. The retry succeeded, so message and paper are both there now, in the right order. Per [[whatsapp-bridge]] the bridge never logs its own sends, so `success: true` is the API's word and delivery could not be confirmed from this machine.

**Still owed: `answers.pdf`, after she submits her attempt.**

The staged copy with the correct filename is at
`/tmp/claude-1000/-home-atif-projects-education-seemab-class-9/caac351a-2c60-4e72-a4ce-8ef4a2a00cfb/scratchpad/send/Maths-Revision-Test-exam-19-Units-10-11-and-6.1-6.2.pdf`
and can be recreated at any time by copying `exam.pdf` to that name.

## The answer key is held, and that is now the default

Atif, 2026-09-23: *"why do you ask everytime? ofcourse hold the key"*. Holding the key until she submits is the standing default for every paper from now on. Do not ask again, and do not re-bundle the key with a paper out of habit. Ask before releasing it.

## What is in the paper

Built on Atif's instruction *"Lets send seemab Maths exam chapter 10, 11, 6.1 and 6.2"* followed by *"make it easy exam, ok"*.

50 marks, 2 hours 15 minutes, school-mirror shape (10 MCQ + 6 short x 4 + 2 long x 8), no optional questions anywhere. Mark split: Unit 11 Basic Statistics 24, Unit 10 Practical Geometry 15, Unit 6 sections 6.1 and 6.2 only 11.

Deliberately easy: every item is a direct application of a printed formula or definition, with clean numbers and no multi-step traps.

This paper took the Friday 25 September calendar slot that [[whole-book-program]] had given to Maths Unit 3 part 1. **Unit 3 is not dropped**, it simply is not this paper.

## Three things the marker needs to know

1. **Question 9 is a genuine construction** (SSS triangle, AB 6 cm, BC 5 cm, CA 4.5 cm, then the three angle bisectors). It is marked on the compass arcs, and the paper tells her not to rub them out. The triangle is acute, largest angle 78.14 degrees, so the in-centre must land **inside** it. An O outside the triangle means the construction went wrong.
2. **Section C Question 8 is self-checking.** The frequency table is built so that the mean, the median and the mode all come to exactly **25.5**. If one of her three answers differs, that part is wrong, not the data.
3. **Probability (11.3) is tested for the first time in any maths paper.** The older Unit 11 paper (exam-09) covered 11.1 and 11.2 only, and she never sat it, so treat all of Unit 11 as unseen when reading her score.

Only Unit 6 is ahead of class. Units 10 and 11 were taught at school and had simply never been examined by us, and the paper says exactly that in Roman Urdu under the syllabus line.

Full per-question map, the uniqueness check against all 18 prior maths papers, and the verification log are in `math/exams/coverage-tracker.md` under Exam-19. HTML sources are at `math/exam-template/exam-19-source/`.

## RESULT SENT 2026-09-23

Atif: *"send the results once ready urdu roman and keys too"*.

| Step | Result |
|---|---|
| Roman Urdu result and guidance message to Shumail | **SENT**, API returned `success: true` |
| `answers.pdf` as `Maths-exam-19-Answer-Key.pdf` | **SENT**, API returned `success: true` |

Message and file went back to back with no tool call in between, per the hard rule in [[whatsapp-exam-send-format]]. Nothing is held back any more; this paper is closed on sends.

**Score sent: 43/50 (86%), Grade A.** Unit 6 11/11, Unit 10 13/15, Unit 11 19/24.

The message explains all 7 lost marks by question number with the correct working (MCQ 5 right bisectors versus altitudes, MCQ 8 mode versus class mark, Q.6 the four probability answers in full, Q.9(i) the short base), and it names the two things she should check and push back on:

1. Whether she attempted Q.6 on a sheet that was not scanned. If so the score becomes 47/50.
2. Whether AB on her own notebook really measures 6 cm. If a ruler on the original says it does, that mark returns and the score becomes 44/50.

She is told explicitly that the Q.9 measurement is the mark most open to challenge and that she has every right to challenge it, per [[seemab-challenges-marks]].

The English marking report, per-exam overview, cumulative overview and subject card were NOT sent. Those are for Atif.
