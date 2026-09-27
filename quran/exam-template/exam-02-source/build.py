#!/usr/bin/env python3
"""Build Quran exam-02 (paper + answer key) HTML, run the key-hygiene checks,
and render both with Chrome headless (never wkhtmltopdf).

Usage: python3 build.py            -> writes exam.html, answers.html here
       python3 build.py --render   -> also renders PDFs into the exam dir
"""
import os, re, subprocess, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(REPO, "quran", "exams", "exam-02-taha-luqman-naml-sajdah-maryam-anbiya-hajj")
L = "ABCD"

# (english stem, urdu stem, [4 urdu options], correct index, reason (en), source)
MCQ = [
 ("Hearing the recitation of Surah Taha, who accepted Islam?",
  "سورۃ طٰہٰ کی تلاوت سن کر کون مسلمان ہوئے؟",
  ["حضرت عثمان غنی رضی اللہ عنہ", "حضرت عمر فاروق رضی اللہ عنہ", "حضرت علی رضی اللہ عنہ", "حضرت زبیر رضی اللہ عنہ"], 1,
  "The تعارف says Hazrat Umar Farooq (RA) went to his sister's house, heard her recite Surah Taha, Islam entered his heart and he accepted it at that very moment.",
  "Surah Taha, تعارف, book p.18 (PDF p.21)"),
 ("According to the account of the hijrat to Habsha in the Surah Maryam lesson, the first hijrat to Habsha took place in which year of Prophethood?",
  "سورۃ مریم کے سبق میں ہجرتِ حبشہ کے بیان کے مطابق حبشہ کی طرف پہلی ہجرت نبوت کے کس سال میں ہوئی؟",
  ["پہلے سال", "تیسرے سال", "دسویں سال", "پانچویں سال"], 3,
  "The ہجرتِ حبشہ paragraph: eleven men and four women migrated, among them Hazrat Usman (RA) and Hazrat Ruqayya (RA); \"this was the first hijrat to Habsha, and it was the fifth year of Prophethood\".",
  "Surah Maryam, تعارف / ہجرتِ حبشہ, book p.4 (PDF p.7)"),
 ("Why was Surah Taha given this name?",
  "سورۃ طٰہٰ کا یہ نام کیوں رکھا گیا؟",
  ["یہ سورت حروفِ مقطعات \"طٰہٰ\" سے شروع ہوتی ہے", "اس میں بہت سے انبیاء کرام کا تذکرہ ہے", "اس کی ایک آیت، آیتِ سجدہ ہے", "اس میں ایک دانا شخص کی اپنے بیٹے کو نصیحتیں ہیں"], 0,
  "The تعارف: Surah Taha is one of the surahs named after حروفِ مقطعات; it opens with \"طٰہٰ\" and is named for that. The three distractors are the naming reasons the book gives for Al-Anbiya (p.34), As-Sajdah (p.145) and Luqman (p.137), so none fits Taha.",
  "Surah Taha, تعارف, book p.18 (PDF p.21)"),
 ("Among the Arabs, Hazrat Luqman was famous as a:",
  "حضرت لقمان اہلِ عرب میں کس حیثیت سے مشہور تھے؟",
  ["تاجر", "شاعر", "حکیم و دانا", "خطیب"], 2,
  "The تعارف: Hazrat Luqman was famous among the Arabs as a very wise and learned man (عقل مند اور دانش ور); poets mentioned him in their verses as a حکیم یعنی دانا. He was mentioned BY poets, he was not a poet.",
  "Surah Luqman, تعارف, book p.137 (PDF p.140)"),
 ("According to Surah Al-Hajj, hajj began in the time of which prophet?",
  "سورۃ الحج کے مطابق حج کا آغاز کس نبی کے زمانے میں ہوا؟",
  ["حضرت ابراہیم علیہ السلام", "حضرت موسیٰ علیہ السلام", "حضرت سلیمان علیہ السلام", "حضرت عیسیٰ علیہ السلام"], 0,
  "The تعارف: the surah tells how hajj began in the time of Hazrat Ibrahim (AS) and what its basic rites are, which is why it is named Surah Al-Hajj.",
  "Surah Al-Hajj, تعارف, book p.48 (PDF p.51)"),
 ("According to the مضامین of Surah An-Naml, Hazrat Sulaiman (AS) was the son of:",
  "سورۃ النمل کے مضامین کے مطابق حضرت سلیمان علیہ السلام کس کے بیٹے تھے؟",
  ["حضرت زکریا علیہ السلام", "حضرت داؤد علیہ السلام", "حضرت ابراہیم علیہ السلام", "حضرت موسیٰ علیہ السلام"], 1,
  "The مضامین state that Hazrat Sulaiman (AS) was the son of Hazrat Dawood (AS), and that Allah gave him wealth, rule and splendour and many miracles.",
  "Surah An-Naml, مضامین, book p.88 (PDF p.91)"),
 ("According to Surah Taha, how should the people of truth deal with those who deny the truth?",
  "سورۃ طٰہٰ کے مطابق حق والوں کو حق کا انکار کرنے والوں کے معاملے میں کس چیز کا مظاہرہ کرنا چاہیے؟",
  ["جلد بازی", "زبردست غصہ", "شعلہ بیانی", "صبر و تحمل"], 3,
  "The مضامین close: Allah does not seize a nation at once for its disbelief but gives it respite, so the people of truth should keep inviting to the deen with patience and must not show haste or impatience with those who deny. (Same item as the book's own مشق 1(iii).)",
  "Surah Taha, مضامین, book p.18-19 (PDF p.21-22)"),
 ("According to the مضامین of Surah Al-Anbiya, the Prophet (SAW) was sent as a complete mercy for:",
  "سورۃ الانبیاء کے مضامین کے مطابق حضرت محمد صلی اللہ علیہ وسلم کو کن کے لیے سراپا رحمت بنا کر بھیجا گیا؟",
  ["تمام جہانوں کے لیے", "صرف اہلِ مکہ کے لیے", "صرف اہلِ عرب کے لیے", "صرف مسلمانوں کے لیے"], 0,
  "The last line of the مضامین: the Prophet (SAW) was sent as سراپا رحمت for تمام جہانوں (all the worlds).",
  "Surah Al-Anbiya, مضامین, book p.34 (PDF p.37)"),
 ("According to the علمی و عملی نکات of Surah As-Sajdah, Allah makes those who are patient and firmly believe in His ayat:",
  "سورۃ السجدہ کے علمی و عملی نکات کے مطابق صبر کرنے والوں اور اللہ تعالیٰ کی آیات پر یقین رکھنے والوں کو اللہ تعالیٰ کیا بناتا ہے؟",
  ["فرشتہ", "صاحبِ ثروت", "لوگوں کا رہنما", "شاعر"], 2,
  "The last نکتہ (As-Sajdah 24) says Allah makes those who are patient and believe firmly in His ayat the guides (رہنما) of people. The book's own مشق item 1(iii) has the same answer.",
  "Surah As-Sajdah, علمی و عملی نکات, book p.146 (PDF p.149)"),
 ("Surah Al-Hajj is called a unique (منفرد) surah because:",
  "سورۃ الحج کو ایک منفرد سورت کیوں کہا گیا ہے؟",
  ["اس کی تمام آیات حج کے بارے میں ہیں", "اس کا کچھ حصہ مدنی ہے اور کچھ مکی", "یہ قرآن مجید کی سب سے لمبی سورت ہے", "یہ حروفِ مقطعات سے شروع ہوتی ہے"], 1,
  "The تعارف calls Surah Al-Hajj a unique (منفرد) surah because part of it is Madani and part is Makki: its revelation began in Makkah before the hijrat and was completed in Madinah after it.",
  "Surah Al-Hajj, تعارف, book p.48 (PDF p.51)"),
]

SURAHS_EN = "Surah Maryam, Surah Taha, Surah Al-Anbiya, Surah Al-Hajj, Surah An-Naml, Surah Luqman, Surah As-Sajdah"
SURAHS_UR = "سورۃ مریم، سورۃ طٰہٰ، سورۃ الانبیاء، سورۃ الحج، سورۃ النمل، سورۃ لقمان، سورۃ السجدہ"

SEC_B = [
 ("Which three stages of the life of Hazrat Musa (AS) are described in Surah Taha? Also write the خلاصہ (summary) of Surah Taha.",
  "سورۃ طٰہٰ میں حضرت موسیٰ علیہ السلام کی زندگی کے کون سے تین مراحل بیان کیے گئے ہیں؟ نیز سورۃ طٰہٰ کا خلاصہ لکھیں۔", "3 + 1"),
 ("Write any four علمی و عملی نکات (scholarly and practical points) of Surah An-Naml.",
  "سورۃ النمل کے علمی و عملی نکات میں سے کوئی چار تحریر کیجیے۔", "4 × 1"),
 ("Write two فضیلتیں (virtues) of Surah As-Sajdah, and write its خلاصہ (summary).",
  "سورۃ السجدہ کی دو فضیلتیں تحریر کیجیے اور اس کا خلاصہ لکھیے۔", "2 + 2"),
]
SEC_C = [
 ("In the light of Surah Taha, describe the account of Hazrat Musa (AS) and Firaun: how Allah sent him to Firaun, the contest with the magicians, and the end of Firaun.",
  "سورۃ طٰہٰ کی روشنی میں حضرت موسیٰ علیہ السلام اور فرعون کا واقعہ تفصیل سے بیان کریں: اللہ تعالیٰ نے انھیں فرعون کی طرف کیسے بھیجا، جادوگروں سے مقابلہ، اور فرعون کا انجام۔"),
 ("In the light of Surah Luqman, describe in detail the advice (نصیحتیں) Hazrat Luqman gave to his son.",
  "سورۃ لقمان کی روشنی میں حضرت لقمان کی اپنے بیٹے کو کی گئی نصیحتیں تفصیل سے بیان کریں۔"),
]

# ---------------------------------------------------------------- checks
def checks():
    letters = "".join(L[m[3]] for m in MCQ)
    c = Counter(letters)
    assert len(MCQ) == 10
    assert sorted(c.values()) == [2, 2, 3, 3], c
    assert not re.search(r"(.)\1\1", letters), "three of one letter in a row"
    for i in range(len(letters) - 7):  # no 4-long repeating cycle
        assert letters[i:i+4] != letters[i+4:i+8], "cyclic pattern"
    for i, m in enumerate(MCQ, 1):
        norm = [re.sub(r"\s+", " ", o).strip() for o in m[2]]
        assert len(set(norm)) == 4, f"duplicate option in MCQ {i}"
    banned = ["فرقان", "شعراء", "شعرآء", "قصص", "عنکبوت", "روم", "یٰسٓ", "یسین", "فاطر", "سبا", "صافات", "احقاف", "ترجمہ کیجیے", "بامحاورہ"]
    blob = str(MCQ) + str(SEC_B) + str(SEC_C)
    hits = [b for b in banned if b in blob]
    assert not hits, hits
    assert "—" not in blob and " - " not in blob
    ayat_items = sum(1 for m in MCQ if "آیات" in m[1] and "کتنی" in m[1])
    assert ayat_items <= 1
    print("MCQ letters:", letters, dict(sorted(c.items())), "| options unique | no out-of-syllabus surah | no em dash")
    return letters

CSS = r"""
@page { size: A4; margin: 10mm 10mm; }
* { box-sizing: border-box; }
body { font-family: Georgia, "Times New Roman", serif; color: #111; margin: 0; font-size: 12pt; }
.ur { font-family: "Noto Nastaliq Urdu", serif; direction: rtl; text-align: right; font-size: 13pt; line-height: 2.35; }
.en { direction: ltr; font-size: 11.5pt; line-height: 1.45; }
.header-box { border: 2.5px solid #000; padding: 6px 12px; text-align: center; }
.board-name { font-size: 15pt; font-weight: bold; letter-spacing: .4px; }
.exam-title { font-size: 13pt; margin-top: 2px; font-weight: bold; }
.subject-line { font-size: 14pt; font-weight: bold; margin-top: 2px; }
.subject-ur { font-family: "Noto Nastaliq Urdu", serif; font-size: 14pt; line-height: 2.1; }
.syl { font-size: 10.5pt; margin-top: 2px; }
.syl-ur { font-family: "Noto Nastaliq Urdu", serif; font-size: 11pt; line-height: 2.1; direction: rtl; }
.info-row { display: flex; justify-content: space-between; border: 1.5px solid #000; border-top: none; padding: 4px 12px; font-size: 12.5pt; font-weight: bold; }
.instr { border: 1.5px solid #000; margin-top: 6px; padding: 4px 12px; font-size: 11pt; page-break-inside: avoid; }
.instr ol { margin: 2px 0; padding-inline-start: 18px; }
.instr li { margin-bottom: 2px; }
.instr li .ur { font-size: 11.5pt; line-height: 2.1; }
.section-bar { background: #DAA520; color: #fff; font-size: 13.5pt; font-weight: bold; text-align: center; padding: 3px 4px; margin-top: 10px; page-break-after: avoid; }
.section-bar .ur { color: #fff; font-size: 13pt; text-align: center; line-height: 2.0; }
.blue { background: #4682B4; } .green { background: #2E8B57; }
table.mcq { width: 100%; border-collapse: collapse; margin-top: 5px; table-layout: fixed; }
table.mcq td, table.mcq th { border: 1px solid #000; padding: 4px 8px; vertical-align: top; }
table.mcq th { background: #f0e6c8; font-size: 11pt; }
table.mcq tr { page-break-inside: avoid; }
td.qnum { width: 6%; text-align: center; font-weight: bold; font-size: 13pt; vertical-align: middle !important; }
.opt-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 3px 12px; margin-top: 2px; direction: rtl; }
.opt-item { border: 1px solid #ccc; border-radius: 3px; padding: 0 8px; background: #fdfdfa; display: flex; align-items: center; gap: 8px; }
.opt-item .ol { font-family: Georgia, serif; font-weight: bold; font-size: 11.5pt; direction: ltr; white-space: nowrap; }
.opt-item .ur { font-size: 12.5pt; line-height: 2.2; }
.qbox { border: 1px solid #000; padding: 5px 10px; margin-top: 6px; page-break-inside: avoid; }
.qhead { display: flex; justify-content: space-between; font-weight: bold; }
.marks { direction: ltr; white-space: nowrap; font-weight: bold; }
.endm { text-align: center; margin-top: 12px; font-weight: bold; }
/* key */
.ka { border-bottom: 1px dashed #999; padding: 5px 2px; page-break-inside: avoid; }
.correct { color: #0a6b0a; font-weight: bold; }
.cite { color: #444; font-size: 10pt; font-style: italic; }
.mb { display: inline-block; background: #e8e8e8; border: 1px solid #bbb; border-radius: 4px; padding: 0 6px; font-weight: bold; font-size: 10pt; margin: 0 3px; direction: ltr; }
.ansbox { border: 1px solid #000; border-left: 4px solid #4682B4; background: #fafafa; padding: 6px 12px; margin-top: 8px; }
.ansbox ol { margin: 3px 0; padding-inline-start: 22px; }
.ansbox li { margin-bottom: 3px; }
.ansbox li .ur { line-height: 2.2; font-size: 12.5pt; }
.letters { font-family: monospace; font-size: 13pt; font-weight: bold; }
"""

def header(title_extra):
    return f"""<div class="header-box">
<div class="board-name">Punjab Curriculum &amp; Textbook Board (PECTAA)</div>
<div class="exam-title">Practice Examination 2026: Exam-02{title_extra}</div>
<div class="subject-line">Tarjuma-tul-Quran-ul-Majeed, Class 9</div>
<div class="subject-ur">ترجمۃ القرآن المجید، جماعت نہم</div>
<div class="syl">Syllabus: {SURAHS_EN}</div>
<div class="syl-ur">نصاب: {SURAHS_UR}</div>
</div>
<div class="info-row"><div>Total Marks: 38</div><div>Time: 1 Hour 45 Minutes</div><div>Exam-02</div></div>"""

def exam_html():
    rows = []
    for i, m in enumerate(MCQ, 1):
        opts = "".join(f'<div class="opt-item"><span class="ol">({L[k]})</span><span class="ur">{o}</span></div>' for k, o in enumerate(m[2]))
        rows.append(f"""<tr><td class="qnum">{i}</td><td><div class="en">{m[0]}</div><div class="ur">{m[1]}</div><div class="opt-grid">{opts}</div></td></tr>""")
    b = "".join(f"""<div class="qbox"><div class="qhead"><span>({r})</span><span class="marks">{q[2]} = 4 Marks</span></div>
<div class="en">{q[0]}</div><div class="ur">{q[1]}</div></div>""" for r, q in zip(["i", "ii", "iii"], SEC_B))
    cq = [f"""<div class="qbox"><div class="qhead"><span>Q.{n}</span><span class="marks">8 Marks</span></div>
<div class="en">{q[0]}</div><div class="ur">{q[1]}</div></div>""" for n, q in zip([3, 4], SEC_C)]
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Tarjuma Quran Majeed Exam-02</title><style>{CSS}</style></head><body>
{header("")}
<div class="instr"><b>Instructions / ہدایات</b><ol>
<li>Attempt ALL questions. There are no choices (no OR) anywhere in this paper.
<div class="ur">تمام سوالات حل کریں۔ اس پرچے میں کوئی اختیاری سوال (OR) نہیں ہے۔</div></li>
<li>For Section A, write each MCQ number with the letter you choose, for example <b>1. C</b>. When you finish, count ten answers and check that every number matches its letter.
<div class="ur">حصہ اول میں ہر سوال کا نمبر اور اپنے جواب کا حرف لکھیں، مثلاً 1. C۔ آخر میں دس جوابات گنیں اور دیکھ لیں کہ ہر نمبر کے ساتھ درست حرف لکھا ہے۔</div></li>
<li>In Sections B and C, write the question number and answer every part separately. Answers may be written in Urdu or English.
<div class="ur">حصہ دوم اور سوم میں سوال کا نمبر لکھیں اور ہر جز کا جواب الگ الگ لکھیں۔ جواب اردو یا انگریزی میں لکھ سکتی ہیں۔</div></li>
</ol></div>

<div class="section-bar">SECTION A: Multiple Choice Questions (10 &times; 1 = 10 Marks)<div class="ur">حصہ اول: معروضی سوالات</div></div>
<table class="mcq"><colgroup><col style="width:6%"><col style="width:94%"></colgroup>
<tr><th>No.</th><th>Question and options (write the number and the letter, e.g. 1. C)</th></tr>
{''.join(rows)}
</table>

<div class="section-bar blue">SECTION B: Short Questions (3 &times; 4 = 12 Marks)<div class="ur">حصہ دوم: مختصر سوالات (تمام اجزا لازمی ہیں)</div></div>
<div class="qbox" style="border:none;padding:0 2px;margin-top:4px"><b>Q.2</b> Answer all three parts. <span class="ur" style="display:inline;line-height:1.9">سوال نمبر 2: تینوں اجزا کے جوابات لکھیں۔</span></div>
{b}

<div style="page-break-inside:avoid"><div class="section-bar green">SECTION C: Detailed Questions (2 &times; 8 = 16 Marks)<div class="ur">حصہ سوم: تفصیلی سوالات (دونوں سوالات لازمی ہیں)</div></div>
{cq[0]}</div>{cq[1]}
<div class="endm">End of Question Paper</div>
</body></html>"""

# ---------------------------------------------------------------- key
B_KEY = [
 ("(i) Surah Taha: three stages of Hazrat Musa's (AS) life, and the خلاصہ", "3 + 1", [
   ("From the birth of Hazrat Musa (AS) until his hijrat to Madyan.", "حضرت موسیٰ علیہ السلام کی پیدائش سے مدین ہجرت فرمانے تک۔", "1"),
   ("The hijrat from Madyan towards the Sahra-e-Sina (Sinai desert).", "مدین سے صحرائے سینا کی طرف ہجرت۔", "1"),
   ("The period after the hijrat to the Sahra-e-Sina until his passing (وصال).", "صحرائے سینا ہجرت کے بعد سے وصال تک کا دور۔", "1"),
   ("خلاصہ: a detailed account of Hazrat Musa (AS), and then the statement of Tawheed, Risalat and Aakhirat.", "خلاصہ: حضرت موسیٰ علیہ السلام کا تفصیلی تذکرہ اور پھر توحید، رسالت اور آخرت کا بیان۔", "1"),
  ], "Source: Surah Taha, تعارف (خلاصہ) and مضامین, book p.18 (PDF p.21). The stages must be the book's three; \"childhood, prophethood, Firaun\" style guesses do not earn the stage marks."),
 ("(ii) Surah An-Naml: any four علمی و عملی نکات", "4 &times; 1", [
   ("Establishing salah, paying zakat and having complete certainty in the Hereafter is the real success. (An-Naml 3)", "نماز قائم کرنا، زکوٰۃ ادا کرنا اور آخرت پر یقینِ کامل رکھنا ہی اصل کامیابی ہے۔", "1"),
   ("Like Hazrat Sulaiman (AS), we should live our lives thanking Allah for His blessings. (19)", "حضرت سلیمان علیہ السلام کی طرح ہمیں بھی اللہ تعالیٰ کی نعمتوں کا شکر ادا کرتے ہوئے زندگی گزارنی چاہیے۔", "1"),
   ("All our mental and physical abilities and every blessing of this world are Allah's favour. (40-73)", "ہماری تمام ذہنی و جسمانی صلاحیتیں اور دنیا کی تمام نعمتیں اللہ تعالیٰ کا فضل ہیں۔", "1"),
   ("Only Allah hears the cry of the helpless and distressed, so in every hardship we should call on Allah alone. (62)", "اللہ تعالیٰ ہی لاچار اور پریشان حال لوگوں کی فریاد سنتا ہے، اس لیے ہر مصیبت میں صرف اللہ تعالیٰ کو پکارنا چاہیے۔", "1"),
   ("Allah is the giver of rizq; we must not displease Him by earning through haram means. (64)", "رزق عطا فرمانے والا اللہ تعالیٰ ہے، ہمیں حرام طریقوں سے رزق حاصل کر کے اللہ تعالیٰ کو ناراض نہیں کرنا چاہیے۔", "1"),
   ("Those who deny the truth are like the dead, the deaf and the blind; they cannot take advice from the Quran. (80-81)", "حق کا انکار کرنے والے مُردوں، بہروں اور اندھوں کی طرح ہیں، جنھیں قرآن مجید سے کوئی نصیحت حاصل نہیں ہو سکتی۔", "1"),
   ("Those who call to the deen should keep warning people through the Quran. (91)", "دین کی دعوت دینے والوں کو قرآن مجید کے ذریعے لوگوں کو خبردار کرتے رہنا چاہیے۔", "1"),
   ("Allah is fully aware of whatever we do, and it will be decided on the Day of Qiyamah. (93)", "ہم جو اعمال بھی کرتے ہیں اللہ تعالیٰ کو ان کی خوب خبر ہے اور قیامت کے دن ان کا فیصلہ ہو جائے گا۔", "1"),
  ], "Source: Surah An-Naml, علمی و عملی نکات, book p.89 (PDF p.92). The book lists eight; any four, one mark each. The meaning in her own words is enough."),
 ("(iii) Surah As-Sajdah: two فضیلتیں and the خلاصہ", "2 + 2", [
   ("The Prophet (SAW) had a special love for Surah As-Sajdah: Hazrat Jabir (RA) says he would not sleep at night until he had recited Surah As-Sajdah and Surah Al-Mulk. (Al-Jami as-Saghir 6903)", "حضرت محمد صلی اللہ علیہ وسلم کو سورۃ السجدہ سے خاص محبت تھی۔ آپ رات کو اس وقت تک نہ سوتے جب تک سورۃ السجدہ اور سورۃ الملک کی تلاوت نہ فرما لیتے۔", "1"),
   ("On Friday the Prophet (SAW) often recited Surah As-Sajdah in the first rakat of the Fajr prayer. (Sahih Bukhari 1068)", "آپ صلی اللہ علیہ وسلم جمعہ کے دن نمازِ فجر کی پہلی رکعت میں اکثر سورۃ السجدہ تلاوت فرمایا کرتے تھے۔", "1"),
   ("خلاصہ, first half: proving the basic beliefs of Islam, Tawheed, Risalat and Aakhirat.", "اسلام کے بنیادی عقائد توحید، رسالت اور آخرت کا اثبات", "1"),
   ("خلاصہ, second half: answering the objections of the disbelievers.", "اور کفار کے اعتراضات کا جواب۔", "1"),
  ], "Source: Surah As-Sajdah, تعارف, book p.145 (PDF p.148). Virtues: accept any two of (a) special love for the surah, (b) recited it with Al-Mulk every night before sleeping, (c) recited it in the first rakat of Friday Fajr (the key rows above group (a) and (b); if she writes them as two separate virtues, give both marks). Her own wording is fine; the surah's name reason (ayat-e-sajdah 15) or other names are not virtues and earn nothing here."),
]

C_KEY = [
 ("Q.3 Surah Taha: Hazrat Musa (AS) and Firaun", [
   ("Allah called Hazrat Musa (AS) in the sacred valley of Tuwa, told him to take off his shoes, and chose him as His messenger. (Taha 11-13, p.20)", "اللہ تعالیٰ نے مقدس وادی طُویٰ میں حضرت موسیٰ علیہ السلام کو ندا دی اور انھیں رسول چن لیا۔"),
   ("He was given two signs: his staff, thrown down, became a running snake, and his hand came out shining white without any defect. (17-22, p.21)", "دو نشانیاں: عصا ڈالا تو دوڑتا ہوا سانپ بن گیا، اور ہاتھ بغل سے بغیر کسی عیب کے سفید چمک دار نکلا۔"),
   ("He was told to go to Firaun, who had rebelled. He prayed for his chest to be opened and his tongue freed, and for his brother Harun (AS) as his helper; the prayer was granted. (24-36, p.21)", "فرعون کے پاس جانے کا حکم؛ سینہ کھلنے اور بھائی ہارون علیہ السلام کو مددگار بنانے کی دعا، جو قبول ہوئی۔"),
   ("Both brothers were told to speak gently to Firaun, so that he might take advice or fear; Allah said, do not fear, I am with you, hearing and seeing. (43-46, p.22)", "دونوں کو فرعون سے نرمی سے بات کرنے کا حکم؛ اللہ تعالیٰ نے فرمایا ڈرو نہیں، میں تمھارے ساتھ ہوں۔"),
   ("They asked Firaun to send the Bani Israil with them and stop tormenting them. Firaun asked who their Rabb was; Musa (AS) said: our Rabb gave everything its form and then guided it. (47-50, p.22-23)", "بنی اسرائیل کو ساتھ بھیجنے کا مطالبہ؛ فرعون کا سوال \"تمھارا رب کون ہے؟\" اور حضرت موسیٰ علیہ السلام کا جواب۔"),
   ("Firaun called the signs magic and set a contest; Musa (AS) fixed the day of the festival (جشن کا دن), with the people gathered in the forenoon. (56-59, p.23)", "فرعون نے نشانیوں کو جادو کہا اور مقابلہ طے ہوا؛ جشن کے دن، دن چڑھے لوگ جمع ہوں۔"),
   ("The magicians threw their ropes and sticks, which seemed to run; Musa (AS) felt some fear, Allah told him not to fear and to throw his staff, and it swallowed what they had made. (65-69, p.24)", "جادوگروں کی رسیاں اور لاٹھیاں دوڑتی محسوس ہوئیں؛ حکم ہوا عصا ڈالو، وہ ان کا سب بنایا ہوا نگل گیا۔"),
   ("The magicians fell into sajdah and believed in the Rabb of Harun and Musa. Firaun threatened to cut their hands and feet on opposite sides and crucify them on palm trunks, but they stood firm. (70-73, p.24-25)", "جادوگر سجدے میں گر کر ایمان لے آئے؛ فرعون نے ہاتھ پاؤں کاٹنے اور سولی کی دھمکی دی، مگر وہ ثابت قدم رہے۔"),
   ("Allah told Musa (AS) to take His servants out by night and make a dry path through the sea; Firaun chased them with his army and the sea covered them, so Firaun and his people were destroyed. Allah saved the Bani Israil. (77-80, p.25)", "رات کو بندوں کو لے جانے اور سمندر میں خشک راستہ بنانے کا حکم؛ فرعون لشکر سمیت پیچھا کرتے ہوئے سمندر میں غرق ہوا۔"),
  ], "Nine creditable points; 1 mark each up to 8. For full marks the answer should reach all three parts the question names (being sent, the magicians, the end). A point needs the event, not only a heading. Source: Surah Taha translation band, book p.20-25 (PDF p.23-28), with the مضامین on p.18 for the overall shape. Material from Samiri and the calf (p.26) is correct but outside the question, so it earns nothing."),
 ("Q.4 Surah Luqman: Hazrat Luqman's advice to his son", [
   ("Never associate anything with Allah (shirk); shirk is a very great wrong (ظلمِ عظیم). (Luqman 13)", "اے میرے پیارے بیٹے! کبھی شرک مت کرنا، بے شک شرک بہت بڑا ظلم ہے۔"),
   ("Even a deed the weight of a mustard seed, hidden in a rock, in the heavens or in the earth, Allah will bring it forth. (16)", "اگر کوئی عمل رائی کے دانے کے برابر بھی ہو، چٹان میں ہو یا آسمانوں یا زمین میں، اللہ اسے حاضر فرما دے گا۔"),
   ("Keep establishing salah. (17)", "نماز قائم کرتے رہنا۔"),
   ("Command others to do good and stop them from evil, while acting on it yourself. (17)", "خود عمل کرتے ہوئے دوسروں کو بھی اچھے کام کا حکم دینا اور برے کام سے منع کرنا۔"),
   ("If a calamity comes, be patient; these are matters of great resolve. (17)", "اگر کوئی مصیبت آ جائے تو اس پر صبر کرنا۔"),
   ("Deal with people in a good way; do not turn your cheek away from people. (18)", "لوگوں سے اچھے طریقے سے پیش آنا، لوگوں سے بے رخی نہ کرنا۔"),
   ("Do not walk on the earth arrogantly; Allah does not like any arrogant boaster. (18)", "زمین پر اکڑ اکڑ کر مت چلنا، اللہ تکبر کرنے والے فخر کرنے والے کو پسند نہیں فرماتا۔"),
   ("Be moderate in life: moderate in your walk, and likewise moderate in speaking. (19)", "زندگی کے معاملات میں میانہ روی؛ چال ڈھال میں بھی اور بولنے میں بھی میانہ روی۔"),
   ("Keep your voice low; the most disliked of voices is the voice of the donkey. (19)", "اپنی آواز کو دھیما رکھنا؛ سب سے بری آواز گدھے کی آواز ہے۔"),
  ], "Nine creditable points; 1 mark each up to 8. Source: Surah Luqman, مضامین, book p.137 (PDF p.140), which lists eight of the pieces of advice, plus the mustard seed from ayah 16 on book p.140; confirmed against the translation of ayat 13-19 on book p.140 (PDF p.143). Kindness to parents (ayat 14-15) is Allah's own command in the middle of the passage, not Luqman's words, so it is not counted as one of his نصیحتیں."),
]

def key_html(letters):
    a = []
    for i, m in enumerate(MCQ, 1):
        a.append(f"""<div class="ka"><b>{i}.</b> {m[0]} &nbsp; <span class="correct">Answer: {L[m[3]]}</span>
<div class="ur">{m[1]} &nbsp;<b>جواب: ({L[m[3]]})</b> {m[2][m[3]]}</div>
{m[4]}<div class="cite">Source: {m[5]}</div></div>""")
    b = []
    for title, marks, pts, src in B_KEY:
        lis = "".join(f'<li>{e} <span class="mb">{mk}</span><div class="ur">{u}</div></li>' for e, u, mk in pts)
        b.append(f'<div class="ansbox"><b>{title}</b> <span class="mb">{marks}</span><ol>{lis}</ol><div class="cite">{src}</div></div>')
    c = []
    for title, pts, src in C_KEY:
        lis = "".join(f'<li>{e} <span class="mb">1</span><div class="ur">{u}</div></li>' for e, u in pts)
        c.append(f'<div class="ansbox"><b>{title}</b> <span class="mb">8</span><ol>{lis}</ol><div class="cite">{src}</div></div>')
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Tarjuma Quran Majeed Exam-02 Answer Key</title><style>{CSS}
body {{ font-size: 11.5pt; }}</style></head><body>
{header(": ANSWER KEY")}
<div class="instr"><b>Section A answer string:</b> <span class="letters">{' '.join(f'{i}.{x}' for i, x in enumerate(letters, 1))}</span>
&nbsp; (A&times;3, B&times;3, C&times;2, D&times;2). Every MCQ, question and marking point is taken from the page images of her PCTB/PECTAA book; printed page + 3 = PDF page.</div>
<div class="section-bar">SECTION A: MCQs (10 Marks)</div>
{''.join(a)}
<div class="section-bar blue">SECTION B: Short Questions (12 Marks)</div>
{''.join(b)}
<div class="section-bar green">SECTION C: Detailed Questions (16 Marks)</div>
{''.join(c)}
<div class="endm">End of Answer Key</div>
</body></html>"""

def main():
    letters = checks()
    for name, html in (("exam.html", exam_html()), ("answers.html", key_html(letters))):
        assert "—" not in html, name
        open(os.path.join(HERE, name), "w", encoding="utf-8").write(html)
    if "--render" in sys.argv:
        os.makedirs(OUT, exist_ok=True)
        for name in ("exam", "answers"):
            pdf = os.path.join(OUT, name + ".pdf")
            subprocess.run(["google-chrome", "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                            f"--print-to-pdf={pdf}", "file://" + os.path.join(HERE, name + ".html")],
                           check=True, capture_output=True)
            pages = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
            print(pdf, re.search(r"Pages:\s+(\d+)", pages).group(1), "pages")

if __name__ == "__main__":
    main()
