"""Build Islamiat exam-03 (exam.html + answer-key.html) from questions.json.

Usage:  python3 build.py && ./render.sh
Runs the answer-key hygiene checks and a syllabus guard before writing anything.
Render with Chrome headless only (wkhtmltopdf mangles Nastaliq).
"""
import json, os, re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, "questions.json")))
M, SH, LG = D["mcqs"], D["short"], D["long"]
LAT = "ABCD"

# ---------------- hygiene checks ----------------
letters = "".join(LAT[q["ans"]] for q in M)
cnt = Counter(letters)
assert len(M) == 10, "need 10 MCQs"
assert sorted(cnt.values()) == [2, 2, 3, 3] and len(cnt) == 4, f"letter balance {cnt}"
assert not re.search(r"(.)\1\1", letters), "three of the same letter in a row"
assert "ABCD" not in letters and "DCBA" not in letters, "cyclic pattern"
for i, q in enumerate(M, 1):
    assert len(set(o.strip() for o in q["ops"])) == 4, f"duplicate option in MCQ {i}"
assert sum(s["marks"] for s in SH) == 12 and sum(s["marks"] for s in LG) == 16
bab_spread = Counter(q["bab"] for q in M)
assert dict(bab_spread) == {1: 1, 2: 2, 3: 3, 4: 1, 6: 2, 7: 1}, bab_spread
assert all(s["bab"] in (1, 2, 3, 4) for s in LG), "no detailed question from Bab 6/7"
assert [s["bab"] for s in SH][0] in (1, 2) and SH[1]["bab"] in (3, 4) and SH[2]["bab"] in (6, 7)

# ---------------- syllabus guard ----------------
ALLOWED_LONG_NAMES = ["عبد اللہ بن عمرو بن العاص"]
BANNED = ["ام ایمن", "امِ ایمن", "ام عمارہ", "حضرت اسماء", "اسماء بنت", "عبد اللہ بن زبیر",
          "تبوک", "حجۃ الوداع", "وصال", "کعب بن مالک", "غدیر", "صلہ رحمی",
          "زید بن علی", "عمرو بن العاص", "جابر بن عبد اللہ", "صوفیہ", "علماء و مفکرین",
          "غیبت", "بہتان", "پردہ پوشی", "اخلاص", "توہم", "جادو", "منصوبہ بندی",
          "سود کی", "جہاد", "گواہی", "خواتین کے ساتھ", "اندازِ تربیت", "صحت اور فراغت"]
alltext = json.dumps(D, ensure_ascii=False)
for ok in ALLOWED_LONG_NAMES:
    alltext = alltext.replace(ok, "")
hits = [b for b in BANNED if b in alltext]
print("letters", " ".join(letters), dict(sorted(cnt.items())), "| bab", dict(sorted(bab_spread.items())))
print("untaught names found:", hits or "none")
assert not hits, hits

BAB_UR = ["", "اوّل", "دوم", "سوم", "چہارم", "پنجم", "ششم", "ہفتم"]

CSS = """@page { size:A4; margin:10mm 9mm; }
:root{--urdu:'Noto Nastaliq Urdu',serif;--latin:'Times New Roman',Times,serif;--gold:#B8860B;--blue:#35658F;}
*{box-sizing:border-box} body{margin:0;font-family:var(--latin);font-size:12pt;color:#000;background:#fff;direction:rtl}
.ur{font-family:var(--urdu);line-height:2.05}
.ltr{direction:ltr;unicode-bidi:isolate}
.saw{font-family:'Noto Naskh Arabic',serif;font-size:1em;line-height:1}
.header-box{border:2.5px solid #000;padding:6px 10px 8px;text-align:center}
.examname{font-size:15pt;font-weight:bold}
.subject{font-size:14pt;font-weight:bold;margin-top:2px}
.subject-ur{font-family:var(--urdu);font-size:15pt;line-height:1.95}
.syllabus{font-size:10.5pt;margin-top:2px}
.syllabus-ur{font-family:var(--urdu);font-size:11.5pt;line-height:1.95}
.info-row{display:flex;justify-content:space-between;margin:6px 2px 6px;font-size:12.5pt;font-weight:bold;direction:ltr}
.section-bar{background:var(--gold);color:#fff;font-size:13.5pt;font-weight:bold;padding:2px 9px;margin:9px 0 6px;display:flex;justify-content:space-between;align-items:center;break-after:avoid}
.section-bar-blue{background:var(--blue)}
.section-bar>span:first-child{direction:ltr}
.section-bar .ur{font-size:14pt;line-height:1.75}
"""

HEADER = lambda title_extra: f"""<div class="header-box">
<div class="examname">Exam-03{title_extra}</div>
<div class="subject">Islamiat (Compulsory) &nbsp;|&nbsp; Class 9</div>
<div class="subject-ur">اسلامیات (لازمی) برائے جماعت نہم</div>
<div class="syllabus">Syllabus: lessons taught in class from Bab 1, 2, 3, 4, 6 and 7 (Punjab board textbook)</div>
<div class="syllabus-ur">نصاب: باب اوّل، دوم، سوم، چہارم، ششم اور ہفتم کے وہ اسباق جو کلاس میں پڑھائے جا چکے ہیں</div>
</div>"""

# ---------------- EXAM ----------------
def mcq_block(i, q):
    ops = "".join(
        f'<div class="op"><span class="ol ltr">({LAT[k]})</span><span class="ur ot">{o}</span></div>'
        for k, o in enumerate(q["ops"]))
    return (f'<div class="mcq"><div class="stem"><span class="qn ltr">{i}.</span>'
            f'<span class="ur qt">{q["q"]}</span></div><div class="ops">{ops}</div></div>')

def q_block(s):
    return (f'<div class="qrow"><div class="qhead"><span class="ltr">{s["no"]}</span>'
            f'<span class="marks ltr">{s["marks"]} Marks</span></div>'
            f'<div class="q-en">{s["en"]}</div><div class="q-ur">{s["ur"]}</div></div>')

exam = f"""<meta charset="utf-8"><title>Islamiat Exam-03</title>
<style>{CSS}
.instr{{border:1.5px solid #000;padding:4px 10px 5px;margin-bottom:6px}}
.instr h4{{margin:0 0 2px;font-size:11.5pt;direction:ltr;text-align:left}}
.instr ol{{margin:0;padding:0 18px 0 0}}
.instr li{{margin-bottom:2px}}
.instr .en{{font-size:10.5pt;direction:ltr;text-align:left;line-height:1.3}}
.instr .u{{font-family:var(--urdu);font-size:10.5pt;line-height:1.95}}
.mcq{{border:1px solid #777;padding:5px 8px 3px;margin-bottom:5px;break-inside:avoid}}
.stem{{display:flex;gap:8px;align-items:baseline}}
.qn{{font-weight:bold;font-size:11.5pt;min-width:22px}}
.qt{{font-size:12.5pt;flex:1}}
.ops{{display:grid;grid-template-columns:1fr 1fr;column-gap:14px;padding-right:28px}}
.op{{display:flex;gap:6px;align-items:baseline}}
.ol{{font-weight:bold;font-size:11pt}}
.ot{{font-size:12pt;line-height:1.95}}
.qrow{{border:1px solid #000;padding:5px 10px 6px;margin-bottom:8px;break-inside:avoid}}
.qhead{{display:flex;justify-content:space-between;align-items:baseline;font-weight:bold;font-size:12pt}}
.marks{{font-size:11pt;white-space:nowrap}}
.q-en{{direction:ltr;text-align:left;font-size:12pt;line-height:1.4;margin-top:2px}}
.q-ur{{font-family:var(--urdu);font-size:13pt;line-height:2.1;margin-top:1px}}
.endmark{{text-align:center;font-weight:bold;font-size:11.5pt;margin-top:10px;direction:ltr}}
</style>
{HEADER("")}
<div class="info-row"><span>Total Marks: 38</span><span>Time Allowed: 1 hour 45 minutes</span></div>
<div class="instr"><h4>Instructions / ہدایات</h4><ol>
<li><div class="en">Attempt all questions. There are no choices (no OR) anywhere in this paper.</div>
<div class="u">تمام سوالات حل کریں۔ اس پرچے میں کسی سوال میں اختیار <span class="ltr">(OR)</span> نہیں ہے۔</div></li>
<li><div class="en">For Section A, write the MCQ number with its letter, for example: 5. D. When you finish, check that every number matches the letter you chose.</div>
<div class="u">حصہ اوّل میں سوال نمبر کے ساتھ حرف لکھیں، جیسا کہ اوپر انگریزی مثال میں دکھایا گیا ہے۔ آخر میں ہر نمبر کو دوبارہ دیکھیں کہ لکھا ہوا حرف وہی ہے جو آپ نے چنا تھا۔</div></li>
<li><div class="en">Answer every part separately. When a question asks for two differences or four points, write that many as separate numbered points.</div>
<div class="u">ہر جزو کا جواب الگ لکھیں۔ جہاں دو فرق یا چار نکات مانگے گئے ہوں، اتنے ہی الگ الگ نمبر وار نکات لکھیں۔</div></li>
</ol></div>
<div class="section-bar"><span>SECTION A: Multiple Choice Questions (10 &times; 1 = 10)</span><span class="ur">حصہ اوّل: کثیر الانتخابی سوالات</span></div>
{"".join(mcq_block(i, q) for i, q in enumerate(M, 1))}
<div class="section-bar"><span>SECTION B: Short Questions (3 &times; 4 = 12)</span><span class="ur">حصہ دوم: مختصر سوالات</span></div>
{"".join(q_block(s) for s in SH)}
<div class="section-bar section-bar-blue"><span>SECTION C: Detailed Questions (2 &times; 8 = 16)</span><span class="ur">حصہ سوم: تفصیلی سوالات</span></div>
{"".join(q_block(s) for s in LG)}
<div class="endmark">End of Question Paper &nbsp;|&nbsp; <span class="ur">اختتامِ پرچہ</span></div>
"""

# ---------------- KEY ----------------
def ak_mcq(i, q):
    opts = " &nbsp;•&nbsp; ".join(
        (f'<b class="ok">({LAT[k]}) {o} ✔</b>' if k == q["ans"] else f'({LAT[k]}) {o}')
        for k, o in enumerate(q["ops"]))
    slo_cls = "cite ltr" if re.match(r"[A-Za-z]", q["slo"]) else "cite ur"
    return (f'<div class="ak"><div class="akq"><span class="qno ltr">{i}.</span><span class="ur">{q["q"]}</span>'
            f'<span class="badge ltr">Ans: {LAT[q["ans"]]}</span></div>'
            f'<div class="ur opts">{opts}</div><div class="ur exp">{q["why"]}</div>'
            f'<div class="cite ltr">Source: Bab {q["bab"]}, {q["lesson"]}, book page p.{q["page"]}</div>'
            f'<div class="{slo_cls}">SLO: {q["slo"]}</div></div>')

def ak_written(s, with_head=True):
    pts = "".join(f"<li>{p}</li>" for p in s["points"])
    head = f'<b>{s["head"]}</b>' if with_head and s.get("head") else ""
    return (f'<div class="abox"><div class="aq"><span class="ltr">{s["no"]}: {s["en"]}</span>'
            f'<span class="badge ltr">{s["marks"]}</span></div>'
            f'<div class="q-ur2">{s["ur"]}</div>'
            f'<div class="a-src">Source: {s["src"].split(" SLO")[0]}</div>'
            f'<div class="cite ur">SLO{s["src"].split(" SLO",1)[1]}</div>'
            f'<div class="a-ur">{head}<ul>{pts}</ul><b>مارکنگ:</b> {s["marking"]}</div></div>')

grid = "".join(f"<td>{i}. {LAT[q['ans']]}</td>" for i, q in enumerate(M, 1))
key = f"""<meta charset="utf-8"><title>Islamiat Exam-03 Answer Key</title>
<style>{CSS}
table.grid{{border-collapse:collapse;direction:ltr;margin:4px auto 6px}}
table.grid td{{border:1px solid #444;padding:2px 9px;font-weight:bold;font-size:11.5pt}}
.ak{{border:1px solid #ccc;border-right:4px solid var(--blue);background:#fafafa;padding:7px 9px 4px;margin-bottom:6px;break-inside:avoid}}
.akq{{display:flex;gap:7px;align-items:baseline}} .qno{{font-weight:bold;font-size:11pt}}
.akq .ur{{flex:1;font-size:12pt;font-weight:bold}}
.badge{{font-size:10pt;font-weight:bold;background:#e8e8e8;border:1px solid #bbb;border-radius:4px;padding:0 5px;white-space:nowrap}}
.opts{{font-size:11.5pt}} .ok{{color:#127a2e}} .exp{{font-size:11pt;color:#222}}
.cite{{font-size:9.5pt;color:#444}} .cite.ltr{{text-align:left;border-top:1px dotted #bbb;padding-top:1px}}
.cite.ur{{font-size:10pt;line-height:1.85}}
.abox{{border:1px solid #999;border-right:4px solid var(--blue);background:#fafafa;padding:9px 10px 7px;margin-bottom:9px}}
.aq{{display:flex;justify-content:space-between;align-items:baseline;font-weight:bold;gap:8px}}
.aq>span:first-child{{font-size:11.5pt;text-align:left}}
.q-ur2{{font-family:var(--urdu);font-size:12pt;line-height:2}}
.a-src{{direction:ltr;text-align:left;font-size:10.5pt;margin-top:1px;color:#333}}
.a-ur{{font-family:var(--urdu);font-size:11.5pt;line-height:2.05;margin-top:3px}}
.a-ur ul{{padding:0 18px 0 0;margin:3px 0}} .a-ur li{{break-inside:avoid;padding-top:5px}}
.note{{border:1.5px solid #000;padding:5px 10px;margin-top:8px;font-size:10.5pt;break-inside:avoid}}
.note p{{margin:2px 0;direction:ltr;text-align:left}}
</style>
{HEADER(": ANSWER KEY")}
<div class="info-row"><span>Total Marks: 38</span><span>Time Allowed: 1 hour 45 minutes</span></div>
<div class="section-bar"><span>SECTION A: MCQ Answers (10 &times; 1 = 10)</span><span class="ur">حصہ اوّل</span></div>
<table class="grid"><tr>{grid}</tr></table>
{"".join(ak_mcq(i, q) for i, q in enumerate(M, 1))}
<div class="section-bar"><span>SECTION B: Short Answers (3 &times; 4 = 12)</span><span class="ur">حصہ دوم</span></div>
{"".join(ak_written(s) for s in SH)}
<div class="section-bar section-bar-blue"><span>SECTION C: Detailed Answers (2 &times; 8 = 16)</span><span class="ur">حصہ سوم</span></div>
{"".join(ak_written(s, False) for s in LG)}
<div class="note"><b>Build checks (run by script on the final option order)</b>
<p>Answer letters: {" ".join(letters)} &nbsp;|&nbsp; A {cnt['A']}, B {cnt['B']}, C {cnt['C']}, D {cnt['D']}. No letter three times running, no ABCD cycle, no repeated option inside a question.</p>
<p>MCQ spread: Bab 1 = 1, Bab 2 = 2, Bab 3 = 3, Bab 4 = 1, Bab 6 = 2, Bab 7 = 1. Bab 5 = 0. Detailed questions only from Bab 2 and Bab 3.</p>
<p>Re-tests of exam-02 slips, reworded: Fatah-e-Makkah cause (MCQ 4), Hazrat Abbas at Hunain (MCQ 5), hasad vs rashk (MCQ 7), Shifa vs Umm Atiya (MCQ 8). From the school First Term paper: Waqoof-e-Arafah vs Tawaf-e-Ziarat (MCQ 3), Hilf-ul-Fuzool vs Hudaybiyah (MCQ 6).</p>
</div>
"""

for name, html in (("exam.html", exam), ("answer-key.html", key)):
    html = html.replace("ﷺ", '<span class="saw">ﷺ</span>')
    html = re.sub(r"\((p\.\d+(?: to p\.\d+)?)\)", r'<span class="ltr">(\1)</span>', html)
    assert "—" not in html and "&mdash;" not in html and " - " not in html, f"dash found in {name}"
    open(os.path.join(HERE, name), "w").write(html)
print("html written")
