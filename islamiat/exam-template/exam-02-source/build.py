import json
from collections import Counter
import os
HERE=os.path.dirname(os.path.abspath(__file__))
Q=json.load(open(os.path.join(HERE,'questions-version-b.json'))); L=["الف","ب","ج","د"]
SLO_T="مذکورہ صحابیات کی علمی و طبی خدمات کا جائزہ لے سکیں۔"
Q[23]=("حضرت شفا رضی اللہ عنہا سے مروی احادیث کی تعداد ہے:",["بارہ","دس","چودہ","سولہ"],0,6,"۱۳۵",SLO_T,
 "حضرت شفا رضی اللہ عنہا نے نبی کریم ﷺ اور حضرت عمر رضی اللہ عنہ سے احادیث روایت کیں، جن کی تعداد <b>بارہ</b> ہے۔")
Q[24]=("زمانہ جاہلیت میں بھی لکھنا پڑھنا جاننے والی اور مشہور طبیبہ صحابیہ تھیں:",["حضرت ام سلیم","حضرت ام عطیہ","حضرت زینب","حضرت شفا"],3,6,"۱۳۵",SLO_T,
 "<b>حضرت شفا</b> رضی اللہ عنہا زمانہ جاہلیت میں بھی لکھنا پڑھنا جانتی تھیں اور مشہور طبیبہ تھیں۔ حضرت ام عطیہ بھی زخمیوں کی مرہم پٹی کرتی تھیں، اس لیے فرق یاد رکھیں: پڑھی لکھی اور مشہور طبیبہ = حضرت شفا۔")
Q[25]=("حضرت ام عطیہ رضی اللہ عنہا عہدِ رسالت میں کتنے معرکوں میں شریک ہوئیں؟",["تین","پانچ","سات","نو"],2,6,"۱۳۶","مذکورہ صحابیات کی سیرت اور معاشرتی کردار سے واقف ہو سکیں۔",
 "حضرت ام عطیہ رضی اللہ عنہا <b>سات</b> معرکوں میں شریک ہوئیں، جن میں مجاہدین کے لیے کھانا پکاتیں، سامان کی حفاظت کرتیں، مریضوں کی تیمارداری اور زخمیوں کی مرہم پٹی کرتیں۔")
Q[26]=("حضرت انس بن مالک رضی اللہ عنہ کی والدہ کا نام ہے:",["حضرت ام سلیم","حضرت شفا","حضرت ام عطیہ","حضرت زینب"],0,6,"۱۳۶","مذکورہ صحابیات کے حالاتِ زندگی اور مقام و مرتبہ سے واقف ہو سکیں۔",
 "حضرت انس رضی اللہ عنہ کی والدہ <b>حضرت ام سلیم</b> رضی اللہ عنہا ہیں، جنھوں نے انھیں نبی کریم ﷺ کی خدمت کے لیے پیش کیا اور انھوں نے دس برس تک آپ ﷺ کی خدمت کی۔")

SECB2_EN="What services did Hazrat Umm Sulaim (may Allah be pleased with her) perform during the battles?"
SECB2_UR="حضرت ام سلیم رضی اللہ تعالیٰ عنہا نے غزوات میں کیا خدمات انجام دیں؟"

# ---------------- hygiene + syllabus guard ----------------
c=Counter(L[q[2]] for q in Q)
dups=[i+1 for i,q in enumerate(Q) if len(set(q[1]))!=4]
banned=["ام ایمن","ام عمارہ","حضرت اسماء","عبد اللہ بن زبیر"]
alltext=json.dumps(Q,ensure_ascii=False)+SECB2_UR
hits=[b for b in banned if b in alltext]
print("count",len(Q),"balance",dict(c),"dups",dups or "none","bab",dict(sorted(Counter(q[3] for q in Q).items())))
print("out-of-syllabus names found:",hits or "none")
assert len(Q)==30 and not dups and not hits and sorted(c.values())==[7,7,8,8]

CSS="""@page { size:A4; margin:9mm 8mm; }
:root{--urdu:'Noto Nastaliq Urdu',serif;--latin:'Times New Roman',Times,serif;--gold:#DAA520;--blue:#4682B4;}
*{box-sizing:border-box} body{margin:0;font-family:var(--latin);font-size:12pt;color:#000;direction:rtl}
.ur{font-family:var(--urdu);line-height:2.05}
.header-box{border:2.5px solid #000;padding:6px 10px 8px;text-align:center;page-break-after:avoid}
.board{font-size:16pt;font-weight:bold;letter-spacing:.4px} .examname{font-size:14pt;font-weight:bold;margin-top:2px}
.subject{font-size:13.5pt;font-weight:bold;margin-top:2px} .subject-ur{font-family:var(--urdu);font-size:15pt;line-height:1.9;margin-top:1px}
.syllabus{font-size:11pt;font-weight:bold;margin-top:3px} .syllabus-ur{font-family:var(--urdu);font-size:12pt;line-height:1.9}
.section-bar{background:var(--gold);color:#fff;font-size:14pt;font-weight:bold;padding:3px 9px;margin:8px 0 5px;page-break-after:avoid;display:flex;justify-content:space-between}
.section-bar-blue{background:var(--blue)} .section-bar>span:first-child{direction:ltr}
.section-bar .ur{font-family:var(--urdu);font-size:15pt;line-height:1.7}
"""
HEAD_SYL="""<div class="syllabus">Syllabus: Bab 1, 2, 3, 4, 6 and 7 &mdash; only the lessons covered in class</div>
<div class="syllabus-ur">نصاب: باب اوّل، دوم، سوم، چہارم، ششم اور ہفتم &mdash; صرف وہ اسباق جو کلاس میں پڑھائے جا چکے ہیں</div>"""

# ---------------- EXAM ----------------
rows="\n".join(
 f'<tr><td class="qn">{i}</td><td class="qt">{q[0]}</td>'+"".join(f'<td class="op">{o}</td>' for o in q[1])+
 '<td class="ans-cell"><span class="bub"></span></td></tr>' for i,q in enumerate(Q,1))
exam=f'''<!doctype html><html lang="ur" dir="rtl"><head><meta charset="utf-8"><title>Islamiat Revision Test — Taught Syllabus (Version B)</title>
<style>{CSS}
.info-row{{display:flex;justify-content:space-between;margin:6px 2px 5px;font-size:12.5pt;font-weight:bold;direction:ltr}}
.namebar{{display:flex;justify-content:space-between;margin:0 2px 6px;font-size:11.5pt}}
.namebar span{{border-bottom:1px dotted #000;min-width:31%;padding-bottom:1px}}
.instr{{border:1.5px solid #000;padding:5px 9px 6px;margin-bottom:7px}}
.instr h4{{margin:0 0 2px;font-size:11.5pt;direction:ltr;text-align:left}}
.instr ol{{margin:0;padding-right:17px;padding-left:0}} .instr li{{font-family:var(--urdu);font-size:11pt;line-height:1.95}}
table{{width:100%;border-collapse:collapse}} .mcq{{font-family:var(--urdu)}} .mcq thead{{display:table-header-group}}
.mcq th{{background:#eee;border:1px solid #000;font-size:10.5pt;padding:2px;font-family:var(--latin)}}
.mcq td{{border:1px solid #000;padding:2px 5px;font-size:11.5pt;line-height:1.88;vertical-align:middle}}
.mcq td.qn{{width:4%;text-align:center;font-family:var(--latin);font-size:10.5pt}} .mcq td.qt{{width:34%}} .mcq td.op{{width:14.5%}}
.mcq td.ans-cell{{width:4%;text-align:center}} .mcq tr{{page-break-inside:avoid}}
.bub{{display:inline-block;width:13px;height:13px;border:1.4px solid #333;border-radius:50%}}
.qrow{{border:1px solid #000;padding:6px 9px 7px;margin-bottom:7px;page-break-inside:avoid}}
.qhead{{display:flex;justify-content:space-between;align-items:baseline;font-weight:bold;font-size:12pt}} .qhead>span:first-child{{direction:ltr}}
.marks{{font-family:var(--latin);font-size:11pt;white-space:nowrap;padding-right:8px;direction:ltr}}
.q-en{{font-family:var(--latin);direction:ltr;text-align:left;font-size:12pt;line-height:1.45}}
.q-ur{{font-family:var(--urdu);font-size:12.5pt;line-height:2.05;margin-top:2px}}
.lines{{margin-top:5px}} .lines div{{border-bottom:1px dotted #999;height:20px}}
.foot{{margin-top:9px;border-top:1.5px solid #000;padding-top:5px;font-size:10.5pt;display:flex;justify-content:space-between}} .foot span{{direction:ltr}}
.endmark{{text-align:center;font-weight:bold;font-size:11.5pt;margin-top:6px;letter-spacing:1px}}
</style></head><body>
<div class="header-box"><div class="board">OPF GIRLS COLLEGE, F-8/2, ISLAMABAD</div><div class="examname">Revision Test 2026</div>
<div class="subject">Islamiyat (Compulsory) &mdash; Class 9</div><div class="subject-ur">اسلامیات (لازمی) &mdash; جماعت نہم</div>{HEAD_SYL}</div>
<div class="info-row"><span>Total Marks: 46</span><span>Time Allowed: 2 Hours</span><span>Version: B</span></div>
<div class="namebar"><span>Name / نام:</span><span>Roll No / رول نمبر:</span><span>Date / تاریخ:</span></div>
<div class="instr"><h4>Instructions / ہدایات</h4><ol>
<li>تمام سوالات حل کرنا لازمی ہیں۔ کوئی سوال اختیاری نہیں ہے۔</li>
<li>حصہ اوّل میں درست جواب کے خانے کو مکمل سیاہ کریں۔ کاٹ پیٹ یا ایک سے زیادہ خانے بھرنے کی صورت میں نمبر نہیں ملے گا۔</li>
<li>حصہ دوم اور حصہ سوم کے جوابات دیے گئے خانوں کے اندر صاف اور واضح تحریر میں لکھیں۔</li>
<li>جہاں قرآنی آیت یا حدیث لکھنی ہو، اس کا ترجمہ بھی ساتھ تحریر کریں۔</li></ol></div>
<div class="section-bar"><span>SECTION A &mdash; Multiple Choice Questions (30 &times; 1 = 30)</span><span class="ur">حصہ اوّل</span></div>
<table class="mcq"><thead><tr><th>#</th><th>Question / سوال</th><th>A / الف</th><th>B / ب</th><th>C / ج</th><th>D / د</th><th>Ans</th></tr></thead><tbody>
{rows}
</tbody></table>
<div class="section-bar"><span>SECTION B &mdash; Short Questions (2 &times; 4 = 8)</span><span class="ur">حصہ دوم</span></div>
<div class="qrow"><div class="qhead"><span>Q.2 (i)</span><span class="marks">4 Marks</span></div>
<div class="q-en">Write any two outcomes of the Battle of Hunain.</div><div class="q-ur">غزوہ حنین کے کوئی سے دو نتائج تحریر کریں۔</div>
<div class="lines"><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div></div>
<div class="qrow"><div class="qhead"><span>Q.2 (ii)</span><span class="marks">4 Marks</span></div>
<div class="q-en">{SECB2_EN}</div><div class="q-ur">{SECB2_UR}</div>
<div class="lines"><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div></div>
<div class="section-bar section-bar-blue"><span>SECTION C &mdash; Detailed Question (1 &times; 8 = 8)</span><span class="ur">حصہ سوم</span></div>
<div class="qrow"><div class="qhead"><span>Q.3</span><span class="marks">8 Marks</span></div>
<div class="q-en">Describe in detail the compilation and codification of the Holy Quran. Your answer should cover all three stages: the era of the Prophet ﷺ, the era of Hazrat Abu Bakr, and the era of Hazrat Usman.</div>
<div class="q-ur">جمع و تدوینِ قرآن مجید کی تفصیل بیان کریں۔ جواب میں تینوں ادوار شامل ہونے چاہییں: عہدِ نبوی ﷺ، عہدِ حضرت ابو بکر صدیق رضی اللہ عنہ، اور عہدِ حضرت عثمان غنی رضی اللہ عنہ۔</div>
<div class="lines"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div></div>
<div class="foot"><span>Syllabus: taught lessons of Bab 1, 2, 3, 4, 6, 7</span><span>Teacher's Signature: ____________________</span></div>
<div class="endmark">&mdash; End of Question Paper / اختتامِ پرچہ &mdash;</div></body></html>'''
open('exam.html','w').write(exam)

# ---------------- KEY ----------------
BAB=["","اوّل","دوم","سوم","چہارم","پنجم","ششم","ہفتم"]
akrows=[]
for i,(qt,ops,ci,bab,pg,slo,exp) in enumerate(Q,1):
    opts=" &nbsp;•&nbsp; ".join((f'<b class="ok">({L[k]}) {o} ✔</b>' if k==ci else f'({L[k]}) {o}') for k,o in enumerate(ops))
    akrows.append(f'<div class="ak"><div class="akq"><span class="qno">{i}.</span><span class="ur">{qt}</span><span class="badge">1</span></div>'
                  f'<div class="ur opts">{opts}</div><div class="ur exp">{exp}</div>'
                  f'<div class="cite"><span class="ur">باب {BAB[bab]} &nbsp;|&nbsp; کتاب صفحہ {pg} &nbsp;|&nbsp; SLO: {slo}</span></div></div>')
key=f'''<!doctype html><html lang="ur" dir="rtl"><head><meta charset="utf-8"><title>Islamiat Answer Key — Taught Syllabus (Version B)</title>
<style>{CSS}
.ak{{border:1px solid #ccc;border-right:4px solid var(--blue);background:#fafafa;padding:5px 9px 6px;margin-bottom:6px;page-break-inside:avoid}}
.akq{{display:flex;gap:7px;align-items:baseline}} .qno{{font-family:var(--latin);font-weight:bold;font-size:11pt;direction:ltr}}
.akq .ur{{flex:1;font-size:12pt;font-weight:bold}}
.badge{{font-family:var(--latin);font-size:10pt;font-weight:bold;background:#e8e8e8;border:1px solid #bbb;border-radius:4px;padding:0 5px;direction:ltr}}
.opts{{font-size:11.5pt;margin-top:1px}} .ok{{color:#127a2e}} .exp{{font-size:11pt;margin-top:2px;color:#222}}
.cite{{font-size:9.5pt;color:#555;margin-top:2px;border-top:1px dotted #bbb;padding-top:2px}} .cite .ur{{font-size:10pt;line-height:1.8}}
.abox{{border:1px solid #999;border-right:4px solid var(--blue);background:#fafafa;padding:7px 10px 8px;margin-bottom:9px;page-break-inside:avoid}}
.aq{{display:flex;justify-content:space-between;align-items:baseline;font-weight:bold}} .aq>span:first-child{{direction:ltr;font-size:11.5pt}}
.a-en{{font-family:var(--latin);direction:ltr;text-align:left;font-size:11.5pt;margin-top:2px}}
.a-ur{{font-family:var(--urdu);font-size:12pt;line-height:2.1;margin-top:3px}} .a-ur ul{{padding-right:18px;padding-left:0;margin:3px 0}}
.note{{border:1.5px solid #000;padding:6px 10px;margin-top:9px;font-size:10.5pt;page-break-inside:avoid}} .note .ur{{font-size:11pt}}
table.bal{{width:auto;border-collapse:collapse;margin-top:4px;direction:ltr}} table.bal td,table.bal th{{border:1px solid #666;padding:1px 10px;font-size:10.5pt;font-family:var(--latin)}}
</style></head><body>
<div class="header-box"><div class="board">OPF GIRLS COLLEGE, F-8/2, ISLAMABAD</div><div class="examname">Revision Test 2026 &mdash; ANSWER KEY (Version B)</div>
<div class="subject">Islamiyat (Compulsory) &mdash; Class 9</div><div class="subject-ur">اسلامیات (لازمی) &mdash; جماعت نہم</div>{HEAD_SYL}</div>
<div class="section-bar"><span>SECTION A &mdash; MCQ Answers (30 &times; 1 = 30)</span><span class="ur">حصہ اوّل</span></div>
{"".join(akrows)}
<div class="section-bar"><span>SECTION B &mdash; Short Answers (2 &times; 4 = 8)</span><span class="ur">حصہ دوم</span></div>
<div class="abox"><div class="aq"><span>Q.2 (i) &mdash; two outcomes of the Battle of Hunain</span><span class="badge">4</span></div>
<div class="a-en">Bab 3, book pages 44&ndash;46 (the book's own exercise, مشق صفحہ ۴۶ سوال ۲(ii)). SLO: غزوہ حنین کے نتائج و اسباق جان سکیں۔</div>
<div class="a-ur"><b>کوئی سے دو نتائج، ہر ایک کے ۲ نمبر:</b><ul>
<li>مسلمانوں کو فتح حاصل ہوئی اور بنو ہوازن و بنو ثقیف کی طاقت ٹوٹ گئی۔</li>
<li>مالِ غنیمت اور قیدی بڑی تعداد میں حاصل ہوئے، جو بعد میں نبی کریم ﷺ نے نہایت فراخ دلی سے تقسیم فرمائے اور ہوازن کے قیدی واپس کر دیے۔</li>
<li>یہ واضح ہوا کہ کامیابی کثرتِ تعداد سے نہیں بلکہ اللہ کی مدد اور توکل سے ملتی ہے۔</li>
<li>طائف اور اطراف کے قبائل کے لیے اسلام قبول کرنے کی راہ ہموار ہوئی۔</li></ul>
<b>مارکنگ:</b> کوئی بھی دو درست نتائج پورے نمبر کے مستحق ہیں۔ صرف واقعہ بیان کرنے پر، نتیجہ بتائے بغیر، آدھے نمبر دیے جائیں۔</div></div>
<div class="abox"><div class="aq"><span>Q.2 (ii) &mdash; services of Hazrat Umm Sulaim in the battles</span><span class="badge">4</span></div>
<div class="a-en">Bab 6, صحابیات, book page 136 (the book's own exercise, مشق صفحہ ۱۴۰ سوال ۲(iii)). SLO: {SLO_T}</div>
<div class="a-ur"><b>چار نکات، ہر ایک کا ۱ نمبر:</b><ul>
<li>حضرت ام سلیم رضی اللہ عنہا نے غزوات میں حصہ لیا۔ نبی کریم ﷺ انصار کی چند عورتوں کو، اور خصوصاً حضرت ام سلیم کو، غزوات میں اپنے ساتھ رکھتے تھے۔</li>
<li>وہ لوگوں کو پانی پلاتی تھیں۔</li>
<li>زخمیوں کی مرہم پٹی کرتی تھیں۔</li>
<li>غزوہ احد، غزوہ خیبر اور غزوہ حنین میں شرکت فرمائی۔</li></ul>
<b>مارکنگ:</b> چوتھے نمبر کے لیے تین میں سے کم از کم دو غزوات کے نام درست ہونے چاہییں۔ حضرت ام عطیہ کی خدمات (کھانا پکانا، سامان کی حفاظت) لکھنے پر نمبر نہ دیے جائیں، وہ دوسری صحابیہ ہیں۔</div></div>
<div class="section-bar section-bar-blue"><span>SECTION C &mdash; Detailed Answer (1 &times; 8 = 8)</span><span class="ur">حصہ سوم</span></div>
<div class="abox"><div class="aq"><span>Q.3 &mdash; compilation and codification of the Holy Quran</span><span class="badge">8</span></div>
<div class="a-en">Bab 1, book pages 1&ndash;3. The book's own تفصیلی question (مشق صفحہ ۳، سوال ۳(i)), and one of the two permitted openings for Q7 of the annual paper. SLO: قرآن مجید کی جمع و تدوین کے مراحل جان سکیں۔</div>
<div class="a-ur"><ul>
<li><b>تمہید (۱):</b> لفظِ قرآن &rdquo;قِرَاءَۃ&ldquo; سے ہے، یعنی کثرت سے پڑھی جانے والی کتاب۔ اللہ تعالیٰ نے خود اس کی حفاظت کا ذمہ لیا: &rdquo;اِنَّا نَحْنُ نَزَّلْنَا الذِّكْرَ وَاِنَّا لَهٗ لَحٰفِظُوْنَ&ldquo; (سورۃ الحجر: ۹)۔</li>
<li><b>عہدِ نبوی ﷺ (۲):</b> وحی نازل ہوتے ہی صحابہ کرام اسے یاد فرما لیتے اور کاتبینِ وحی اسے لکھ بھی لیتے تھے۔ لکھنے کے لیے پتھر کی سلیں، چمڑا، کھجور کی چھال اور اونٹ کے شانے کی ہڈیاں استعمال ہوتیں۔</li>
<li><b>عہدِ حضرت ابو بکر صدیق (۲):</b> جنگِ یمامہ میں سیکڑوں حفاظِ کرام شہید ہو گئے۔ حضرت عمر فاروق رضی اللہ عنہ کے مشورے پر حضرت ابو بکر صدیق رضی اللہ عنہ نے جمع و تدوین کا فیصلہ فرمایا اور <b>حضرت زید بن ثابت</b> رضی اللہ عنہ کو، جو کاتبِ وحی تھے، سربراہ مقرر کیا۔ یوں قرآن ایک مصحف کی صورت میں جمع ہوا۔</li>
<li><b>نسخے کی حفاظت (۱):</b> یہ نسخہ پہلے حضرت ابو بکر صدیق، پھر حضرت عمر فاروق، اور پھر <b>حضرت حفصہ</b> رضی اللہ عنہا کے پاس محفوظ رہا۔</li>
<li><b>عہدِ حضرت عثمان غنی (۲):</b> مختلف علاقوں میں قراءتوں اور لہجوں کا اختلاف پیدا ہوا تو حضرت عثمان غنی رضی اللہ عنہ نے حضرت حفصہ رضی اللہ عنہا سے وہی نسخہ منگوا کر اس کی نقول تیار کروائیں، مختلف صوبوں میں بھجوائیں اور تمام مسلمانوں کو <b>ایک قراءت</b> پر متحد فرما دیا۔</li></ul>
<b>مارکنگ:</b> کل ۸ نمبر۔ تینوں ادوار کا ذکر لازمی ہے؛ کوئی ایک دور مکمل چھوٹ جائے تو ۲ نمبر کاٹے جائیں۔ آیت بغیر ترجمے کے لکھی جائے تو آدھا نمبر کاٹا جائے۔</div></div>
<div class="note"><b>Answer-key hygiene checks (run on the final option order)</b>
<table class="bal"><tr><th>A / الف</th><th>B / ب</th><th>C / ج</th><th>D / د</th><th>Total</th></tr>
<tr><td>{c['الف']}</td><td>{c['ب']}</td><td>{c['ج']}</td><td>{c['د']}</td><td>30</td></tr></table>
<div style="margin-top:4px">Letter balance is even. No question repeats an option. Every MCQ carries its bab, book page and printed SLO.</div>
<div class="ur" style="margin-top:5px"><b>ورژن B میں تبدیلی:</b> صحابیات میں سے صرف حضرت شفا، حضرت ام سلیم اور حضرت ام عطیہ رضی اللہ عنہن پڑھائی گئی ہیں۔ ورژن A کے سوالات ۲۴ تا ۲۷ اور حصہ دوم کا سوال ۲(ii) حضرت ام ایمن، حضرت ام عمارہ اور حضرت اسماء کے بارے میں تھے، اس لیے انھیں بدل دیا گیا ہے۔ <b>باب پنجم سے ایک بھی سوال شامل نہیں۔</b></div>
</div></body></html>'''
open('answer-key.html','w').write(key)
print("html written")
