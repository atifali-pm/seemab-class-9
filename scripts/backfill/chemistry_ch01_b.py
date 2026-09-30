# -*- coding: utf-8 -*-
"""Chemistry Chapter 1, lessons 1.2 to 1.6. Her book p7 to 14."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import build

C = "#1e7a4a"
S = "chemistry"

LESSONS = [
{
 "subject": S, "chapter": 1, "ref": "1.2", "slug": "chem-ch01-branches",
 "summary": "The twelve branches of chemistry your book names, what each one studies, and how to tell the confusable pairs apart.",
 "note": """
<h1><span class="emoji">🌳</span> Chemistry Ch 1.2: Branches of Chemistry</h1>
<div class="sub">Chapter 1, Nature of Chemistry in Science · kitab ke page 7 se 14 · <b>12 branches</b></div>
<p>Chemistry itni bari hai ke ek insan poori nahin parh sakta. Is liye ise <b>12 hisson</b> mein baanta gaya hai.
Har hissa ek khaas sawal ka jawab deta hai.</p>
<table>
<tr><th style="width:26%">Branch</th><th style="width:74%">Kya parhti hai</th></tr>
<tr><td><b>Organic</b></td><td>Carbon wale maddey (magar carbonates, bicarbonates, oxides aur carbides is mein nahin)</td></tr>
<tr><td><b>Inorganic</b></td><td>Baqi tamam elements aur compounds, organic ke ilawa</td></tr>
<tr><td><b>Physical</b></td><td>Maddey ki structure aur tabdeeli ke <b>qawaneen aur theories</b></td></tr>
<tr><td><b>Analytical</b></td><td>Tareeqe aur aalaat jin se composition aur properties maloom ki jati hain</td></tr>
<tr><td><b>Biochemistry</b></td><td>Zinda ajsam ke andar physical aur chemical tabdeeliyan</td></tr>
<tr><td><b>Environmental</b></td><td>Wo chemical aur zehreele maddey jo mahol ko ganda karte hain</td></tr>
<tr><td><b>Industrial</b></td><td>Chemical maddon ki <b>bari paimane</b> par tayari</td></tr>
<tr><td><b>Medicinal</b></td><td>Dawaon aur jismani targets ke darmiyan amal</td></tr>
<tr><td><b>Polymer</b></td><td>Polymers: nylon, polyethylene, Teflon</td></tr>
<tr><td><b>Geochemistry</b></td><td>Zameen ki crust ke elements: chattanein, minerals, mitti</td></tr>
<tr><td><b>Nuclear</b></td><td>Atom ke <b>nucleus</b> ke andar tabdeeliyan</td></tr>
<tr><td><b>Astrochemistry</b></td><td>Sitaron aur dumdar sitaron mein chemical amal</td></tr>
</table>
<div class="box warn"><span class="t"><span class="emoji">⚠️</span> Do joriyan jo imtihan mein ulti ho jati hain</span>
<b>Organic banam Inorganic:</b> carbon wale organic. Lekin <b>carbonates, bicarbonates, oxides aur carbides</b>
carbon rakhne ke bawajood <b>inorganic</b> hain. Ye istisna yaad rakhein, yehi poochha jata hai.<br>
<b>Physical banam Analytical:</b> Physical <b>kyun</b> poochhti hai (qanoon aur theory). Analytical <b>kitna aur kaunsa</b>
poochhti hai (naap aur pehchan).</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Name any <b>six</b> branches of chemistry from your book and write one line on what each studies.</li>
<li>Organic chemistry deals with carbon compounds. Name the four carbon containing substances your book
<b>excludes</b> from it, and say which branch they belong to instead.</li>
</ol></div>
<!--KEY 1. Any six of the twelve in the table, one line each.
2. Carbonates, bicarbonates, oxides and carbides. They belong to inorganic chemistry. -->
""",
 "script": """السلام علیکم سیماب۔ آج Chemistry کے باب ایک کا دوسرا حصہ ہے، branches of chemistry۔ لیکن پہلے ایک سوال۔

فرض کریں کوئی آپ سے کہے کہ ساری Chemistry پڑھ لو۔ ساری۔ ستاروں سے لے کر آپ کے خون کے اندر تک۔ کیا یہ ممکن ہے؟

نہیں۔ اور یہی وجہ ہے کہ Chemistry کو حصوں میں بانٹا گیا ہے۔ آپ کی کتاب بارہ حصے بتاتی ہے، اور ہر حصے کا اپنا ایک سوال ہے۔

پہلا، Organic chemistry۔ یہ carbon والے مادوں کو دیکھتی ہے۔ اور یہاں ایک بہت ضروری بات ہے جو امتحان میں آتی ہے: carbon ہونے کے باوجود کچھ چیزیں organic نہیں ہیں۔ وہ چار ہیں: carbonates، bicarbonates، oxides اور carbides۔ یہ چاروں inorganic ہیں۔ یہ استثنا یاد رکھیے گا۔

دوسرا، Inorganic chemistry۔ باقی تمام elements اور compounds۔

تیسرا، Physical chemistry۔ یہ مادے کی ساخت اور تبدیلی کے قوانین اور theories دیکھتی ہے۔

چوتھا، Analytical chemistry۔ یہ وہ طریقے اور آلات ہیں جن سے پتہ چلتا ہے کہ کوئی چیز کس چیز سے بنی ہے۔

اب ذرا رکیے۔ Physical اور Analytical میں فرق کیا ہے؟ یہ دونوں طالبات الجھا دیتی ہیں۔ آسان طریقہ یہ ہے: Physical پوچھتی ہے کیوں، یعنی قانون کیا ہے۔ اور Analytical پوچھتی ہے کتنا اور کون سا، یعنی ناپ اور پہچان۔

پانچواں، Biochemistry، یعنی زندہ اجسام کے اندر کی تبدیلیاں۔ چھٹا، Environmental chemistry، یعنی وہ زہریلے مادے جو ماحول کو گندا کرتے ہیں۔ ساتواں، Industrial chemistry، یعنی بڑے پیمانے پر مادوں کی تیاری۔

آٹھواں، Medicinal chemistry، یعنی دواؤں اور جسم کے درمیان عمل۔ نواں، Polymer chemistry۔ اس میں nylon، polyethylene اور Teflon آتے ہیں۔ آپ کے گھر کا non-stick توا Teflon ہی ہے۔

دسواں، Geochemistry، یعنی زمین کی crust کے مادے: چٹانیں، minerals اور مٹی۔ گیارہواں، Nuclear chemistry، یعنی ایٹم کے nucleus کے اندر کی تبدیلیاں۔ اور بارہواں، Astrochemistry، یعنی ستاروں اور دمدار ستاروں میں ہونے والے chemical عمل۔

اب یاد کرنے کا ایک طریقہ۔ ان بارہ کو الگ الگ رٹنے کی بجائے یہ سوچیں کہ ہر branch کس جگہ کام کرتی ہے۔ زمین کے نیچے Geochemistry۔ زمین کے اوپر Environmental۔ آسمان میں Astrochemistry۔ جسم کے اندر Biochemistry اور Medicinal۔ کارخانے میں Industrial اور Polymer۔ اور ایٹم کے اندر Nuclear۔

جب جگہ یاد ہو جائے تو نام خود یاد رہتے ہیں۔

آپ کے دو quiz سوال صفحے پر ہیں۔ دوسرے میں وہی چار استثنا پوچھے گئے ہیں، اس لیے انہیں ابھی دہرا لیں: carbonates، bicarbonates، oxides اور carbides۔ خدا حافظ۔
""",
},
{
 "subject": S, "chapter": 1, "ref": "1.3", "slug": "chem-ch01-essential-questions",
 "summary": "The guiding question behind each branch of chemistry, which is how the book expects you to tell them apart.",
 "note": """
<h1><span class="emoji">❓</span> Chemistry Ch 1.3: Essential Questions</h1>
<div class="sub">Chapter 1, Nature of Chemistry in Science · kitab ke page 7 se 14</div>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Is safhay ka poora nuqta</span>
Pichhle safhay par hum ne <b>12 branches ke naam</b> yaad kiye. Ab kitab ek aur kaam karti hai: har branch ke
saath <b>ek sawal</b> jorti hai. Kyun? Kyunke naam bhool sakta hai, magar sawal yaad reh jata hai.<br>
Jab aap ko yaad ho ke koi branch <b>kya poochhti hai</b>, to us ka kaam khud bakhud yaad aa jata hai.</div>
<table>
<tr><th style="width:30%">Branch</th><th style="width:70%">Us ka bunyadi sawal</th></tr>
<tr><td>Physical</td><td>Ye tabdeeli <b>kyun</b> hoti hai, aur is ka qanoon kya hai?</td></tr>
<tr><td>Organic</td><td>Is carbon wale maddey ki <b>banawat</b> kya hai?</td></tr>
<tr><td>Inorganic</td><td>Ye element ya compound kaise <b>amal</b> karta hai?</td></tr>
<tr><td>Analytical</td><td>Is namoonay mein <b>kya kya</b> hai aur <b>kitna</b> hai?</td></tr>
<tr><td>Biochemistry</td><td>Jism ke andar ye amal <b>kaise</b> hota hai?</td></tr>
<tr><td>Environmental</td><td>Ye maddah mahol ko <b>kitna nuqsan</b> de raha hai?</td></tr>
<tr><td>Medicinal</td><td>Ye dawa jism par <b>asar kaise</b> karti hai?</td></tr>
<tr><td>Polymer</td><td>Chhote unit mil kar <b>bara molecule</b> kaise banate hain?</td></tr>
<tr><td>Geochemistry</td><td>Zameen ki crust mein ye maddah <b>kahan</b> hai?</td></tr>
<tr><td>Nuclear</td><td>Nucleus ke andar <b>kya</b> badal raha hai?</td></tr>
<tr><td>Astronomy</td><td>Sitaron mein <b>kaunsa</b> chemical amal chal raha hai?</td></tr>
</table>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Is ka faida imtihan mein</span>
Agar sawal ho "kaunsi branch ye kaam karti hai", to seedha naam mat dhoondein. Pehle <b>sawal</b> pehchanein.
Misal: "ek paani ke namoonay mein lead kitna hai" ye <b>kitna</b> wala sawal hai, to jawab <b>Analytical</b> hai.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Write the essential question behind <b>Analytical</b>, <b>Physical</b> and <b>Biochemistry</b>.</li>
<li>A scientist is finding out how much lead is in a water sample. Which branch is this, and why?</li>
</ol></div>
<!--KEY 1. Analytical: what is in this sample and how much. Physical: why does this change happen and what law
governs it. Biochemistry: how does this process happen inside a living body.
2. Analytical chemistry, because the question is "how much", which is measurement and identification. -->
""",
 "script": """السلام علیکم سیماب۔ آج کا صفحہ چھوٹا ہے مگر بہت کام کا ہے۔ کل ہم نے Chemistry کی بارہ branches کے نام یاد کیے تھے۔ آج ہم دیکھیں گے کہ ان کو یاد رکھنے کا ایک آسان طریقہ کیا ہے۔

پہلے ایک سوال۔ فرض کریں امتحان میں لکھا ہو: ایک سائنسدان پانی کے نمونے میں lead کی مقدار معلوم کر رہا ہے۔ یہ کون سی branch ہے؟

اب اگر آپ نے صرف نام رٹے ہوں تو آپ سوچیں گی: Environmental؟ کیونکہ پانی ہے۔ یا Inorganic؟ کیونکہ lead ایک metal ہے۔ اور آپ الجھ جائیں گی۔

لیکن کتاب ایک اور چیز دیتی ہے، اور وہی اصل چابی ہے۔ ہر branch کے ساتھ ایک بنیادی سوال جڑا ہوا ہے۔ اور جب آپ سوال پہچان لیں تو نام خود آ جاتا ہے۔

Physical chemistry کا سوال ہے: یہ تبدیلی کیوں ہوتی ہے، اور اس کا قانون کیا ہے۔

Analytical chemistry کا سوال ہے: اس نمونے میں کیا کیا ہے، اور کتنا ہے۔

اب واپس اوپر والے سوال پر چلیں۔ lead کی مقدار معلوم کرنا۔ یہ کتنا والا سوال ہے۔ تو جواب ہے Analytical chemistry۔ پانی کا ذکر آپ کو بھٹکا رہا تھا۔

Biochemistry کا سوال ہے: جسم کے اندر یہ عمل کیسے ہوتا ہے۔ Medicinal کا سوال ہے: یہ دوا جسم پر اثر کیسے کرتی ہے۔ Environmental کا سوال ہے: یہ مادہ ماحول کو کتنا نقصان دے رہا ہے۔

Polymer کا سوال ہے: چھوٹے unit مل کر بڑا molecule کیسے بناتے ہیں۔ Nuclear کا سوال ہے: nucleus کے اندر کیا بدل رہا ہے۔ اور Geochemistry کا سوال ہے: زمین کی crust میں یہ مادہ کہاں ہے۔

تو آج کی ایک بات: نام مت ڈھونڈیں، سوال پہچانیں۔ کتنا مطلب Analytical۔ کیوں مطلب Physical۔ جسم کے اندر مطلب Biochemistry۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
{
 "subject": S, "chapter": 1, "ref": "1.4", "slug": "chem-ch01-daily-life",
 "summary": "Five everyday uses your book gives, one for each branch: medicines, batteries, forensics, car batteries and water purification.",
 "note": """
<h1><span class="emoji">🏠</span> Chemistry Ch 1.4: Daily Life Applications</h1>
<div class="sub">Chapter 1, Nature of Chemistry in Science · kitab ke page 7 se 14</div>
<p>Kitab yahan har branch ko <b>ghar ki ek cheez</b> se jor deti hai. Ye paanch misalein yaad kar lein, sawal
seedha inhi se banta hai.</p>
<table>
<tr><th style="width:28%">Branch</th><th style="width:72%">Roz marra ki misal</th></tr>
<tr><td><b>Organic</b></td><td><b>Dawaein banana</b> (proteins aur enzymes ki madad se)</td></tr>
<tr><td><b>Inorganic</b></td><td><b>Lithium ion batteries</b>, jo aap ke mobile mein hain</td></tr>
<tr><td><b>Analytical</b></td><td><b>Forensic chemistry</b>: jism ke maaye, haddiyan, reshay aur drugs pehchanna</td></tr>
<tr><td><b>Physical</b></td><td><b>Electrochemistry</b>, gaari ki battery ke andar</td></tr>
<tr><td><b>Environmental</b></td><td><b>Paani ki safai</b>: sedimentation, filtration, disinfection</td></tr>
</table>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Paani ki safai ke teen qadam, tarteeb se</span>
<b>1. Sedimentation:</b> paani ko thehrne dena, bhaari mail neeche baith jata hai.<br>
<b>2. Filtration:</b> chhan kar baqi zarray nikalna.<br>
<b>3. Disinfection:</b> keeray maar dena, aam tor par chlorine se.<br>
Teenon ka naam aur <b>tarteeb</b> dono poochhe ja sakte hain.</div>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Mobile aur gaari ka farq</span>
Dono mein battery hai, magar kitab ne inhein <b>alag</b> branches ke saath rakha hai.<br>
<b>Mobile ki Li-ion battery = Inorganic.</b> <b>Gaari ki battery ka electrochemistry = Physical.</b>
Ye jori aksar ulti ho jati hai.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Write the everyday application your book gives for <b>Organic</b>, <b>Inorganic</b> and <b>Analytical</b> chemistry.</li>
<li>Name the three steps of water purification <b>in order</b>, and say which branch of chemistry this belongs to.</li>
</ol></div>
<!--KEY 1. Organic: synthesising medicines (proteins and enzymes). Inorganic: lithium ion batteries.
Analytical: forensic chemistry, identifying body fluids, bones, fibres and drugs.
2. Sedimentation, then filtration, then disinfection. Environmental chemistry. -->
""",
 "script": """السلام علیکم سیماب۔ آج کا صفحہ سب سے آسان ہے، کیونکہ آج کی ساری مثالیں آپ کے اپنے گھر سے ہیں۔

پہلے ایک سوال۔ آپ کے ہاتھ میں جو موبائل ہے، اور باہر جو گاڑی کھڑی ہے، دونوں میں battery ہے۔ لیکن کتاب نے ان دونوں کو Chemistry کی دو الگ الگ branches کے ساتھ رکھا ہے۔ کیوں؟ تھوڑی دیر میں جواب آئے گا۔

کتاب یہاں پانچ مثالیں دیتی ہے۔

پہلی، Organic chemistry۔ اس کا کام ہے دوائیں بنانا، proteins اور enzymes کی مدد سے۔ آپ کو بخار ہو اور امی panadol دیں، وہ Organic chemistry کا کام ہے۔

دوسری، Inorganic chemistry۔ اس کی مثال ہے lithium ion battery۔ یہ وہی battery ہے جو آپ کے موبائل میں ہے۔

تیسری، Analytical chemistry۔ اس کی مثال ہے forensic chemistry۔ یہ وہ کام ہے جو پولیس کی lab میں ہوتا ہے: جسم کے مائع، ہڈیاں، ریشے اور drugs پہچاننا۔

چوتھی، Physical chemistry۔ اس کی مثال ہے electrochemistry، اور وہ گاڑی کی battery کے اندر ہوتی ہے۔

اب اوپر والے سوال کا جواب مل گیا۔ موبائل کی battery Inorganic کے ساتھ ہے، اور گاڑی کی battery Physical کے ساتھ۔ یہ جوڑی امتحان میں الٹی ہو جاتی ہے، اس لیے اسے ابھی پکا کر لیں۔

اور پانچویں، Environmental chemistry۔ اس کی مثال ہے پانی کی صفائی۔ اور اس کے تین قدم ہیں، ترتیب کے ساتھ۔

پہلا، sedimentation، یعنی پانی کو ٹھہرنے دینا تاکہ بھاری میل نیچے بیٹھ جائے۔ دوسرا، filtration، یعنی چھان کر باقی ذرے نکالنا۔ اور تیسرا، disinfection، یعنی جراثیم مار دینا، عام طور پر chlorine سے۔

یہ تینوں نام اور ان کی ترتیب دونوں پوچھی جا سکتی ہے، اس لیے ترتیب سے یاد رکھیں: پہلے ٹھہراؤ، پھر چھانو، پھر جراثیم مارو۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
{
 "subject": S, "chapter": 1, "ref": "1.5", "slug": "chem-ch01-science-tech-eng",
 "summary": "The book's definitions of science, technology and engineering, how they differ, and what a chemical engineer does.",
 "note": """
<h1><span class="emoji">⚙️</span> Chemistry Ch 1.5: Science, Technology and Engineering</h1>
<div class="sub">Chapter 1, Nature of Chemistry in Science · kitab ke page 7 se 14</div>
<p>Ye teen lafz roz marra mein ek jaise bol diye jate hain. Kitab in ka <b>saaf farq</b> karti hai, aur yehi
farq imtihan mein poochha jata hai.</p>
<div class="box def"><span class="t"><span class="emoji">📖</span> Teenon ki definition</span>
<b>Science:</b> kainaat ke baare mein ilm ko <b>bananay aur tarteeb denay</b> ka ek systematic tareeqa.<br>
<b>Technology:</b> us scientific ilm ko <b>amli kaamon</b> par lagana: aalaat, machinein aur systems.<br>
<b>Engineering:</b> science aur mathematics ka istemal kar ke systems aur structures <b>design aur tameer</b> karna.</div>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Teenon ko alag rakhne ka asaan tareeqa</span>
<b>Science jaanti hai. Technology istemal karti hai. Engineering banati hai.</b><br>
Ek misal se: bijli ke qawaneen samajhna <b>Science</b> hai. Un se bulb banana <b>Technology</b> hai. Poore
shehar ka bijli ka nizam design karna <b>Engineering</b> hai.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Chemical engineers kya karte hain</span>
Kitab khaas taur par chemical engineers ka zikr karti hai. Ye wo log hain jo <b>banane ke tareeqe (manufacturing
processes)</b> tayar karte hain, aur paanch cheezon ke liye:<br>
<b>chemicals, fuels, food, medicines aur polymers.</b><br>
Yani lab mein ek chhoti si beaker mein jo amal hota hai, use poore karkhane ke paimane par chalana, wo chemical
engineer ka kaam hai.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Define <b>science</b>, <b>technology</b> and <b>engineering</b> in the words of your book, and give one example
that shows the difference between them.</li>
<li>What do <b>chemical engineers</b> do, and name the five things your book says they make processes for?</li>
</ol></div>
<!--KEY 1. Science: a systematic process of constructing and organising knowledge about the universe.
Technology: applying scientific knowledge to practical applications, such as tools, machines and systems.
Engineering: using science and mathematics to design and construct systems and structures. Example: understanding
the laws of electricity is science, making a bulb is technology, designing a city's power system is engineering.
2. Chemical engineers develop manufacturing processes, for chemicals, fuels, food, medicines and polymers. -->
""",
 "script": """السلام علیکم سیماب۔ آج تین لفظوں کا فرق سمجھنا ہے: science، technology اور engineering۔ ہم روز مرہ میں یہ تینوں ایک جیسے بول دیتے ہیں، لیکن کتاب ان کا صاف فرق کرتی ہے، اور یہی فرق امتحان میں پوچھا جاتا ہے۔

پہلے ایک مثال، اور اس کے بعد تینوں definition خود سمجھ آ جائیں گی۔

سوچیں بجلی کے بارے میں۔ کسی نے سب سے پہلے یہ دریافت کیا کہ بجلی کیسے بہتی ہے، اس کے قوانین کیا ہیں۔ یہ کام science تھا۔

پھر کسی نے ان قوانین کو استعمال کر کے bulb بنایا۔ یہ کام technology تھا۔

اور پھر کسی نے پورے شہر کا بجلی کا نظام design کیا: تار کہاں جائیں گے، کتنا load ہو گا، کہاں transformer لگے گا۔ یہ کام engineering تھا۔

اب کتاب کی definition سنیے۔

Science وہ systematic طریقہ ہے جس سے کائنات کے بارے میں علم بنایا اور ترتیب دیا جاتا ہے۔

Technology اس scientific علم کو عملی کاموں پر لگانا ہے، یعنی آلات، مشینیں اور systems بنانا۔

اور Engineering science اور mathematics کو استعمال کر کے systems اور structures design اور تعمیر کرنا ہے۔

یاد رکھنے کا سب سے آسان طریقہ یہ ہے: Science جانتی ہے۔ Technology استعمال کرتی ہے۔ Engineering بناتی ہے۔

تین لفظ: جانتی، استعمال کرتی، بناتی۔ بس یہی ترتیب یاد رکھ لیں۔

اب آخری بات، اور یہ آپ کی کتاب خاص طور پر لکھتی ہے۔ Chemical engineers کون ہیں اور کیا کرتے ہیں؟

یہ وہ لوگ ہیں جو بنانے کے طریقے، یعنی manufacturing processes، تیار کرتے ہیں۔ اور کن چیزوں کے لیے؟ پانچ چیزیں کتاب گنواتی ہے: chemicals، fuels، food، medicines اور polymers۔

ذرا سوچیں یہ کام کتنا بڑا ہے۔ lab میں ایک چھوٹی سی beaker میں کوئی عمل کامیاب ہو جائے، یہ ایک بات ہے۔ لیکن اسی عمل کو پورے کارخانے کے پیمانے پر، ہزاروں لیٹر میں، محفوظ طریقے سے چلانا بالکل دوسری بات ہے۔ وہی chemical engineer کا کام ہے۔

تو آج کی دو باتیں۔ ایک، Science جانتی ہے، Technology استعمال کرتی ہے، Engineering بناتی ہے۔ اور دو، chemical engineers پانچ چیزوں کے manufacturing processes بناتے ہیں۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
{
 "subject": S, "chapter": 1, "ref": "1.6", "slug": "chem-ch01-applications",
 "summary": "The book's four worked examples: rusting iron, solar energy, french fries and plastic bags, each showing science, technology and engineering together.",
 "note": """
<h1><span class="emoji">🔬</span> Chemistry Ch 1.6: Applications, the four examples</h1>
<div class="sub">Chapter 1, Nature of Chemistry in Science · kitab ke page 7 se 14 · Examples 1.1 se 1.4</div>
<p>Pichhle safhay par teen lafz alag alag samjhe. Ab kitab <b>chaar misalein</b> deti hai jahan teenon
<b>ek saath</b> kaam karte hain. Ye chaaron yaad karein, sawal inhi se aata hai.</p>
<table>
<tr><th style="width:10%">#</th><th style="width:30%">Misal</th><th style="width:60%">Is mein hota kya hai</th></tr>
<tr><td>1.1</td><td><b>Lohe ka zang (rusting)</b></td>
<td>Loha, hawa ki oxygen aur paani mil kar zang banate hain. Science samajhti hai ke kyun, phir us se bachne ka
tareeqa banaya jata hai.</td></tr>
<tr><td>1.2</td><td><b>Solar energy</b></td>
<td>Tarteeb yaad rakhein: <b>photovoltaic cells &rarr; solar panels &rarr; poora nizam</b>. Cell science hai,
panel technology hai, aur poora nizam engineering hai.</td></tr>
<tr><td>1.3</td><td><b>French fries</b></td>
<td>Organic chemistry amal mein: aalu ke <b>carbohydrates</b>, aur tel ka <b>nikala jana (extraction)</b>.</td></tr>
<tr><td>1.4</td><td><b>Plastic bags</b></td>
<td>Chhote <b>monomers</b> jur kar <b>polyethylene</b> ka <b>polymer</b> banate hain.</td></tr>
</table>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Solar wali misal sab se zyada poochhi jati hai</span>
Kyunke us mein <b>teen qadam tarteeb se</b> hain. Ek chhota <b>photovoltaic cell</b> roshni ko bijli banata hai.
Bohat se cells mila kar ek <b>solar panel</b> banta hai. Aur bohat se panels, taarein, batteries aur switches mila
kar poora <b>infrastructure</b> banta hai. Chhote se bare ki taraf: cell, panel, nizam.</div>
<div class="box warn"><span class="t"><span class="emoji">⚠️</span> Plastic bag wali misal mein lafz ka dhyan</span>
<b>Monomer</b> chhota ek unit hai. <b>Polymer</b> bohat se monomers ka lamba silsila hai. <b>Polyethylene</b> us
polymer ka naam hai. Teenon alag lafz hain, ek doosre ki jagah mat likhein.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Name the four examples your book gives in section 1.6, and write one line on each.</li>
<li>For solar energy, write the <b>three stages in order</b> from the smallest part to the whole system. Then
explain the difference between a <b>monomer</b> and a <b>polymer</b> using the plastic bag example.</li>
</ol></div>
<!--KEY 1. Example 1.1 rusting of iron; 1.2 harnessing solar energy; 1.3 organic chemistry in action, french
fries; 1.4 plastic bags. One line each as in the table.
2. Photovoltaic cells, then solar panels, then the wider infrastructure. A monomer is a single small unit; a
polymer is many monomers joined into a long chain. In a plastic bag the monomers join to form the polymer
polyethylene. -->
""",
 "script": """السلام علیکم سیماب۔ آج باب ایک کا آخری صفحہ ہے۔ کل ہم نے تین لفظ الگ الگ سمجھے تھے: science، technology اور engineering۔ آج کتاب چار مثالیں دیتی ہے جہاں یہ تینوں ایک ساتھ کام کرتے ہیں۔

پہلی مثال، لوہے کا زنگ۔ لوہا، ہوا کی oxygen اور پانی، تینوں مل کر زنگ بناتے ہیں۔ پہلے science نے سمجھا کہ یہ ہوتا کیوں ہے۔ اور جب وجہ سمجھ آ گئی تو اس سے بچنے کا طریقہ بنا: paint، grease، galvanising۔ یعنی پہلے جاننا، پھر بچانا۔

دوسری مثال، solar energy۔ اور یہ سب سے زیادہ پوچھی جاتی ہے، کیونکہ اس میں تین قدم ترتیب سے ہیں۔ غور سے سنیے۔

سب سے پہلے ایک چھوٹا سا photovoltaic cell ہوتا ہے، جو روشنی کو بجلی میں بدلتا ہے۔ پھر بہت سے cells ملا کر ایک solar panel بنتا ہے۔ اور پھر بہت سے panels، تاریں، batteries اور switches ملا کر پورا نظام، یعنی infrastructure بنتا ہے۔

ترتیب یاد رکھیں: cell، پھر panel، پھر پورا نظام۔ چھوٹے سے بڑے کی طرف۔

تیسری مثال، french fries۔ جی ہاں، french fries۔ یہ Organic chemistry کی عملی مثال ہے۔ اس میں دو چیزیں ہیں: آلو کے carbohydrates، اور تیل کا نکالا جانا، یعنی extraction۔

چوتھی مثال، plastic bags۔ اور یہاں تین لفظوں کا فرق یاد رکھنا ہے۔

Monomer ایک چھوٹا سا اکیلا unit ہے۔ Polymer بہت سے monomers کا لمبا سلسلہ ہے۔ اور polyethylene اسی polymer کا نام ہے۔

ایک آسان تصویر ذہن میں رکھیں: monomer ایک موتی ہے، اور polymer موتیوں کی لمبی مالا۔ پلاسٹک کی تھیلی ایسی ہی ایک مالا ہے۔

یہ تینوں لفظ ایک دوسرے کی جگہ مت لکھیے گا، کیونکہ امتحان میں انہی کا فرق پوچھا جاتا ہے۔

تو آج کی چار مثالیں: زنگ، solar energy، french fries اور plastic bags۔ اور ان میں سے solar والی ترتیب اور plastic والے تین لفظ، یہ دو چیزیں سب سے زیادہ نمبر دلاتی ہیں۔

اس کے ساتھ باب ایک مکمل ہو گیا۔ آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
]

if __name__ == "__main__":
    build(LESSONS, C)
