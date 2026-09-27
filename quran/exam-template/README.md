# Tarjuma-tul-Quran exam sources

These are the HTML sources for Quran exam-01. Everywhere else in this repo only PDFs are kept, but a right-to-left Urdu and Arabic paper cannot be rebuilt from its PDF, so the sources live here, the same exception as `islamiat/exam-template/`.

| File | What it is |
|---|---|
| `exam-01-v2-exam.html` | **Current paper, sent 2026-09-11.** 50 marks, Sections A to C, 2 hours 30 minutes. |
| `exam-01-v2-answers.html` | Current answer key (not sent yet). |
| `exam-01-v1-with-section-D-exam.html` | First version, 65 marks, with a Section D translation section. Sent first, then replaced. |
| `exam-01-v1-with-section-D-answers.html` | First key, including full Urdu and English translations of Maryam 30-36, Al-Anbiya 30-35 and Al-Hajj 65-69. |
| `exam-02-source/build.py` | **Exam-02** (38 marks, 1 hour 45 minutes, no OR). Holds every question, the key and the hygiene checks; `python3 build.py --render` rewrites `exam.html` / `answers.html` beside it and renders both PDFs into `exams/exam-02-taha-luqman-naml-sajdah-maryam-anbiya-hajj/`. |

Version 2 was made from Version 1 by removing Section D and changing only the header (marks, time, version, the Section D instruction). Sections A to C are identical.

**Do not bring Section D back.** Seemab's class does not write tarjuma (she said so on 2026-09-11).

## Rendering

```
./render.sh exam-01-v2-exam.html exam.pdf
```

Chrome headless only. Fonts: `Noto Naskh Arabic` for ayat, `Noto Nastaliq Urdu` for Urdu, both already installed. Keep Urdu MCQ options in the 2x2 grid; four narrow option columns make Nastaliq wrap one word per line.

## Checking an edit

Do not compare Urdu text pulled out of two PDFs with `pdftotext`: Nastaliq extraction changes between renders even when nothing changed. Diff the HTML sources, and compare only the English words of the two PDFs.
