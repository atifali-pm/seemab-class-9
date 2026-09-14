# Urdu / RTL exam template (Islamiat only)

The reference implementation is **exam-01-bab5**. These two files are that paper's source, kept deliberately as a reusable template. Everywhere else in this repo only the PDF is committed; this is the one exception, because a right-to-left Urdu paper cannot be re-derived from a PDF and re-doing this CSS from scratch each time would be wasteful.

## The one rule that matters: render with Chrome, never wkhtmltopdf

Verified on 2026-09-10 with a side-by-side test. **wkhtmltopdf 0.12.6 cannot shape Nastaliq.** It produced overlapping, mangled, unreadable Urdu: "سوال نمبر ۱" came out as a garbled four-character fragment, and "جنگِ یمامہ" rendered as nonsense. Its QtWebKit engine simply lacks the shaping support. Chrome headless renders the same HTML perfectly, including right-to-left table column order and Arabic diacritics.

```
./render.sh mypaper.html
```

Because of this, the wkhtmltopdf-specific advice in the main exam-template memory does not apply here: no `--margin-*` flags, no `.page { width: 100% }` workaround, and the `<sup>` flattening fix from the revision-test format is irrelevant.

## What differs from the English template

| | English papers | This template |
|---|---|---|
| Renderer | wkhtmltopdf | **Chrome headless** |
| Direction | LTR | `dir="rtl"` on `<html>` |
| Body font | Times New Roman | `Noto Nastaliq Urdu` for Urdu, Times for Latin |
| Line height | 1.3 / 1.5 | **~2.05** (Nastaliq descends steeply and clips below this) |
| Pagination | `@page` + wkhtml margins | `@page { size:A4; margin:9mm 8mm }` |
| Language | English | Bilingual: English line, Urdu line under it, mirroring the school's own Islamiat paper |

## RTL gotchas that already bit once

- **Latin runs inside an RTL flex box get reordered.** "4 Marks" rendered as "Marks 4" and "Teacher's Signature:" as ":Teacher's Signature". Fix: put `direction:ltr` on any span holding Latin text or digits (`.marks`, `.foot span`, `.qhead>span:first-child`).
- **Table columns mirror automatically.** With `dir="rtl"`, the first `<th>` lands on the right. So write the header in logical order (#, Question, A, B, C, D, Ans) and it displays correctly right-to-left. Do not hand-reverse it.
- **Repeat the MCQ header across pages** with `<thead>` plus `.mcq thead{display:table-header-group}`. Chrome honours this; a 30-row table spans three pages without it.
- **The ﷺ glyph is very tall** and stacks badly inside a narrow option cell, pushing the row height up. Keep it in wide question text, drop it from short option cells.

## Structure carried over from the English gold standard

Header box (2.5px border, board name, exam name, subject, **syllabus line, required**), info row, instructions box, gold `#DAA520` Section A and B bars, blue `#4682B4` Section C bar, MCQ table with bubble circles, answer boxes with a 4px blue border (on the **right** here, not the left), inline mark badges, footer and end-of-paper marker.

The answer key additionally prints, per the answer-key hygiene rule, the **book page and the SLO beside every single MCQ**, and closes with a letter-balance table.

## Per-exam source data

`exam-02-source/` holds the question JSON and build script for exam-02, so its paper and key can be regenerated. Keep doing this for future Islamiat papers: an Urdu paper cannot be rebuilt from its PDF.
