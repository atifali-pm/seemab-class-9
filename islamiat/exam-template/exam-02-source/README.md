# exam-02 source data

Source for `islamiat/exams/exam-02-bab1-2-3-4-6-7/`, kept so the paper or key can be rebuilt without re-reading the book.

| File | What it is |
|---|---|
| `questions-version-b.json` | The 30 MCQs of **Version B** (the paper Seemab has). Each entry: question, 4 options, correct index (0 = الف), bab, book page, printed SLO, key explanation. |
| `questions-version-a-SENT-has-8-untaught-marks.json` | Version A, kept for the record only. MCQs 24 to 27 are on untaught صحابیات. Do not reuse. |
| `build.py` | Writes `exam.html` and `answer-key.html` for Version B into the current directory. Section B and C text is inside the script. It also runs the hygiene checks and a guard that fails if an untaught صحابیہ name appears. |

Rebuild:

```
cd /tmp && python3 /home/atif/projects/education/seemab/class-9/islamiat/exam-template/exam-02-source/build.py
google-chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer --print-to-pdf=exam.pdf exam.html
google-chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer --print-to-pdf=answer-key.pdf answer-key.html
```

Render with Chrome, never wkhtmltopdf (it mangles Nastaliq).
