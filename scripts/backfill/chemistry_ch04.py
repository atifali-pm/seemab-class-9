# -*- coding: utf-8 -*-
"""Chemistry Chapter 4: Periodic Table and Periodicity of Properties. Her book p45 to 72."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import build
C = "#1e7a4a"; S = "chemistry"

def L(ref, slug, summary, note, script):
    return {"subject": S, "chapter": 4, "ref": ref, "slug": slug,
            "summary": summary, "note": note, "script": script}

LESSONS = [
L("4.1", "chem-ch04-periodic-table",
  "Periods and groups, and how the s and p blocks are laid out.",
  """
<h1><span class="emoji">📊</span> Chemistry Ch 4.1: The Periodic Table</h1>
<div class="sub">Chapter 4, Periodic Table and Periodicity · kitab ke page 45 se 72 · sections 4.1.1 aur 4.1.2</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Do simtein, do naam</span>
<b>Periods:</b> <b>aarzi (horizontal) qatarein</b>. Ek period mein chalne ka matlab hai usi shell mein electrons
barhte jana.<br>
<b>Groups:</b> <b>amoodi (vertical) column</b>. Ek group ke tamam elements ke <b>bairooni electrons barabar</b>
hote hain, isi liye un ki <b>khasoosiyat milti julti</b> hoti hai.</div>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Blocks: aakhri electron kahan gira</span>
Element ka <b>block</b> us sub-shell se tay hota hai jis mein <b>aakhri electron</b> jata hai.<br>
<b>s block:</b> Group 1 aur 2 (aur helium).<br>
<b>p block:</b> Group 13 se 18.<br>
Yani agar configuration <b>3s<sup>1</sup></b> par khatam ho to element <b>s block</b> ka hai.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Configuration se teen cheezein nikalna</span>
Sodium: 1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>6</sup> <b>3s<sup>1</sup></b><br>
<b>Period</b> = sab se bara shell number = <b>3</b>. <b>Group</b> = bairooni electrons = <b>1</b>.
<b>Block</b> = aakhri sub-shell = <b>s</b>.<br>
Teenon ek hi configuration se nikal aate hain. Yehi sawal imtihan mein aata hai.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>What is the difference between a <b>period</b> and a <b>group</b>? Why do elements of the same group behave alike?</li>
<li>An element has the configuration 1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>6</sup> 3s<sup>2</sup> 3p<sup>1</sup>.
Give its period, its group and its block, and explain how you worked each one out.</li>
</ol></div>
<!--KEY 1. Periods are horizontal rows, groups are vertical columns. Elements in a group have the same number of
outermost electrons, which is what decides chemical behaviour.
2. Highest shell is 3, so period 3. Outermost electrons 2+1 = 3, and it is a p block element, so group 13.
Block p, because the last electron entered a p sub-shell. -->
""",
  """السلام علیکم سیماب۔ آج باب چار شروع ہو رہا ہے، periodic table۔ لیکن پہلے ایک سوال۔

Periodic table میں سو سے زیادہ elements ہیں۔ کوئی بھی ان سب کی خصوصیات الگ الگ یاد نہیں رکھ سکتا۔ تو پھر سائنسدان کیسے بتا دیتے ہیں کہ کوئی نیا element کیسا برتاؤ کرے گا؟

جواب ترتیب میں ہے۔ آئیے دیکھتے ہیں۔

Periodic table میں دو سمتیں ہیں، اور دونوں کا الگ نام ہے۔

افقی قطاروں کو periods کہتے ہیں۔ یعنی بائیں سے دائیں جو لکیر جاتی ہے۔

اور عمودی columns کو groups کہتے ہیں۔ یعنی اوپر سے نیچے۔

اب اصل بات۔ ایک ہی group کے تمام elements کے بیرونی electrons برابر ہوتے ہیں۔ اور chemistry کا سارا برتاؤ بیرونی electrons سے طے ہوتا ہے۔

اسی لیے ایک group کے elements ایک جیسا برتاؤ کرتے ہیں۔ اور یہی اوپر والے سوال کا جواب ہے: کسی نئے element کے بارے میں اندازہ اس کے group سے لگایا جاتا ہے۔

اب blocks۔ Element کا block اس بات سے طے ہوتا ہے کہ اس کا آخری electron کس sub-shell میں گرا۔

اگر آخری electron s میں گیا تو element s block کا ہے۔ یہ group ایک اور دو ہیں۔

اور اگر p میں گیا تو p block کا۔ یہ group تیرہ سے اٹھارہ تک ہیں۔

اب ایک مثال، اور اس سے تینوں چیزیں ایک ساتھ نکل آئیں گی۔

Sodium کی configuration ہے: ایک s دو، دو s دو، دو p چھ، تین s ایک۔

Period کیسے نکالیں؟ سب سے بڑا shell نمبر دیکھیں۔ یہاں تین ہے۔ تو period تین۔

Group کیسے نکالیں؟ بیرونی electrons گنیں۔ یہاں تین s میں صرف ایک ہے۔ تو group ایک۔

اور block؟ آخری electron s میں گیا۔ تو s block۔

دیکھا؟ ایک ہی configuration سے period، group اور block تینوں نکل آئے۔ اور یہی سوال امتحان میں آتا ہے، اس لیے یہ تینوں قدم یاد رکھیں۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
"""),

L("4.2", "chem-ch04-group-and-ion-charge",
  "How the group number tells you the charge an element's ion will carry, and the five named families.",
  """
<h1><span class="emoji">🔢</span> Chemistry Ch 4.2: Group Number and Ion Charge</h1>
<div class="sub">Chapter 4, Periodic Table and Periodicity · kitab ke page 45 se 72</div>
<p>Is safhay ka faida bohat bara hai: <b>group number dekh kar ion ka charge bataya ja sakta hai</b>, bina kuch
yaad kiye.</p>
<table>
<tr><th style="width:16%">Group</th><th style="width:34%">Naam</th><th style="width:22%">Ion ka charge</th><th style="width:28%">Misal</th></tr>
<tr><td>1</td><td><b>Alkali metals</b></td><td><b>+1</b></td><td>Na<sup>+</sup>, K<sup>+</sup></td></tr>
<tr><td>2</td><td><b>Alkaline earth metals</b></td><td><b>+2</b></td><td>Mg<sup>2+</sup>, Ca<sup>2+</sup></td></tr>
<tr><td>16</td><td><b>Chalcogens</b></td><td><b>-2</b></td><td>O<sup>2-</sup>, S<sup>2-</sup></td></tr>
<tr><td>17</td><td><b>Halogens</b></td><td><b>-1</b></td><td>Cl<sup>-</sup>, F<sup>-</sup></td></tr>
<tr><td>18</td><td><b>Noble gases</b></td><td><b>koi nahin</b></td><td>He, Ne, Ar</td></tr>
</table>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Usool, aur wajah</span>
Har atom <b>noble gas jaisi</b> bairooni shell chahta hai, yani <b>8 electrons</b>.<br>
Group 1 ke paas <b>ek zyada</b> hai, to wo <b>de</b> deta hai: charge <b>+1</b>.<br>
Group 17 ke paas <b>ek kam</b> hai, to wo <b>le</b> leta hai: charge <b>-1</b>.<br>
Aur noble gases ke paas <b>poore 8</b> hain, is liye wo <b>kuch nahin karte</b>: koi ion nahin.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Name the families of groups 1, 2, 16, 17 and 18, and give the charge each one's ion carries.</li>
<li>Explain <b>why</b> a group 2 element forms a 2+ ion while a group 17 element forms a 1- ion.</li>
</ol></div>
<!--KEY 1. Group 1 alkali metals, +1. Group 2 alkaline earth metals, +2. Group 16 chalcogens, -2. Group 17
halogens, -1. Group 18 noble gases, no ion.
2. Atoms become stable by reaching a full outer shell of eight electrons. A group 2 element has two more than the
nearest noble gas, so it loses two and becomes 2+. A group 17 element has one fewer, so it gains one and
becomes 1-. -->
""",
  """السلام علیکم سیماب۔ آج کا سبق چھوٹا ہے مگر بہت کام کا، کیونکہ آج کے بعد آپ کو ion کے charge یاد کرنے کی ضرورت نہیں رہے گی۔ آپ انہیں نکال سکیں گی۔

پہلے ایک سوال۔ Sodium کا ion ہمیشہ مثبت ایک ہوتا ہے۔ Magnesium کا ہمیشہ مثبت دو۔ اور chlorine کا ہمیشہ منفی ایک۔ یہ ہمیشہ کیوں؟ کوئی ان کو مجبور تو نہیں کرتا۔

جواب ایک اصول میں ہے، اور وہ اصول یہ ہے: ہر atom چاہتا ہے کہ اس کی بیرونی shell بھری ہوئی ہو، یعنی اس میں آٹھ electrons ہوں۔ یہی noble gas والی حالت ہے، اور یہی سب سے مستحکم ہے۔

اب دیکھیں کیا ہوتا ہے۔

Group ایک کے پاس بیرونی shell میں ایک electron زیادہ ہے۔ آٹھ تک پہنچنے کے لیے سات اور لینے پڑیں گے، جو مشکل ہے۔ تو آسان راستہ یہ ہے کہ وہ ایک دے دے۔ ایک منفی گیا، تو charge مثبت ایک ہو گیا۔ ان کو alkali metals کہتے ہیں۔

Group دو کے پاس دو زیادہ ہیں۔ تو وہ دو دے دیتے ہیں، اور charge مثبت دو ہو جاتا ہے۔ ان کو alkaline earth metals کہتے ہیں۔

اب دوسری طرف چلیں۔

Group سترہ کے پاس ایک کم ہے۔ صرف ایک لے لیں تو آٹھ پورے۔ تو وہ ایک لے لیتے ہیں، اور charge منفی ایک ہو جاتا ہے۔ ان کو halogens کہتے ہیں۔

Group سولہ کے پاس دو کم ہیں۔ تو وہ دو لے لیتے ہیں، اور charge منفی دو۔ ان کو chalcogens کہتے ہیں۔

اور group اٹھارہ؟ ان کے پاس پہلے ہی پورے آٹھ ہیں۔ انہیں نہ دینے کی ضرورت ہے نہ لینے کی۔ اسی لیے وہ کوئی ion نہیں بناتے، اور انہیں noble gases کہتے ہیں۔ Noble کا مطلب ہی یہ ہے کہ وہ کسی کے ساتھ ملتے جلتے نہیں۔

تو اصول ایک جملے میں: جس کے پاس زیادہ ہیں وہ دیتا ہے اور مثبت ہو جاتا ہے، جس کے پاس کم ہیں وہ لیتا ہے اور منفی ہو جاتا ہے، اور جس کے پاس پورے ہیں وہ کچھ نہیں کرتا۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
"""),

L("4.3", "chem-ch04-periodicity",
  "Shielding effect, atomic size, ionization energy, electron affinity and electronegativity, and how each changes across a period and down a group.",
  """
<h1><span class="emoji">📉</span> Chemistry Ch 4.3: Periodicity of Properties</h1>
<div class="sub">Chapter 4 · kitab ke page 45 se 72 · sections 4.3.1 se 4.3.5, paanchon rujhanat</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Paanch istilahein</span>
<b>Shielding effect:</b> andar wale electrons bairooni electron ko nucleus ki kheench se <b>bachate</b> hain.<br>
<b>Atomic size:</b> atom ka nasf qutar (radius).<br>
<b>Ionization energy:</b> bairooni electron <b>nikalne</b> ke liye darkar energy.<br>
<b>Electron affinity:</b> electron <b>lene</b> par kharij hone wali energy.<br>
<b>Electronegativity:</b> bond ke electrons ko apni taraf <b>kheenchne</b> ki salahiyat.</div>
<h2><span class="emoji">📋</span> Paanchon ka rujhan</h2>
<table>
<tr><th style="width:40%">Property</th><th style="width:30%">Period mein (bayein se dayein)</th><th style="width:30%">Group mein (oopar se neeche)</th></tr>
<tr><td>Shielding effect</td><td>Taqreeban <b>wohi</b></td><td><b>Barhta</b> hai</td></tr>
<tr><td>Atomic size</td><td><b>Ghatta</b> hai</td><td><b>Barhta</b> hai</td></tr>
<tr><td>Ionization energy</td><td><b>Barhti</b> hai</td><td><b>Ghatti</b> hai</td></tr>
<tr><td>Electron affinity</td><td><b>Barhti</b> hai</td><td><b>Ghatti</b> hai</td></tr>
<tr><td>Electronegativity</td><td><b>Barhti</b> hai</td><td><b>Ghatti</b> hai</td></tr>
</table>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Paanch yaad karne ki zaroorat nahin, sirf ek</span>
Sab kuch <b>atomic size</b> se nikalta hai, ulta.<br>
Atom <b>chhota</b> = bairooni electron nucleus ke <b>qareeb</b> = kheench <b>zyada</b> = nikalna <b>mushkil</b> aur
lena <b>asaan</b>. Yani ionization energy, electron affinity aur electronegativity <b>teenon barh</b> jati hain.<br>
Period mein size ghatta hai, to teenon barhti hain. Group mein size barhta hai, to teenon ghatti hain.
<b>Bas size yaad rakhein, baqi khud nikal aayega.</b></div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Define <b>shielding effect</b>, <b>ionization energy</b> and <b>electronegativity</b>.</li>
<li>Copy the trend table for all five properties, across a period and down a group, and explain in one or two
sentences why ionization energy rises across a period.</li>
</ol></div>
<!--KEY 1. Shielding: inner electrons screen the outer electron from the nucleus. Ionization energy: the energy
needed to remove the outermost electron. Electronegativity: an atom's ability to attract the shared electrons of
a bond toward itself.
2. The table as given. Across a period the atomic size decreases, so the outer electron sits closer to the
nucleus and is held more tightly, which means more energy is needed to remove it. -->
""",
  """السلام علیکم سیماب۔ آج کا سبق پانچ چیزوں کا ہے، اور بظاہر یہ یاد کرنے والا لگتا ہے۔ لیکن میں آپ کو ایک بات بتاتا ہوں: ان پانچوں کو یاد کرنے کی ضرورت نہیں۔ صرف ایک یاد رکھیں، باقی چار خود نکل آتے ہیں۔ پہلے سوال۔

Periodic table میں بائیں سے دائیں جائیں تو atoms چھوٹے ہوتے جاتے ہیں۔ عجیب بات ہے نا؟ electrons تو بڑھ رہے ہیں، تو atom بڑا ہونا چاہیے۔ پھر چھوٹا کیوں ہو رہا ہے؟

وجہ یہ ہے کہ ساتھ ساتھ protons بھی بڑھ رہے ہیں، اور نیا electron اسی shell میں جا رہا ہے۔ تو nucleus کی کھینچ بڑھ جاتی ہے اور پوری shell اندر کو سکڑ جاتی ہے۔

اب پانچ اصطلاحات۔

Shielding effect: اندر والے electrons بیرونی electron کو nucleus کی کھینچ سے بچاتے ہیں، جیسے ڈھال۔

Atomic size: atom کا نصف قطر۔

Ionization energy: بیرونی electron نکالنے کے لیے درکار energy۔

Electron affinity: electron لینے پر خارج ہونے والی energy۔

اور electronegativity: bond کے electrons کو اپنی طرف کھینچنے کی صلاحیت۔

اب وہ ایک بات جو سب کچھ کھول دیتی ہے۔ سب کچھ atomic size سے نکلتا ہے، اور الٹا نکلتا ہے۔

سوچیں۔ اگر atom چھوٹا ہے تو بیرونی electron nucleus کے قریب ہے۔ قریب ہے تو کھینچ زیادہ ہے۔ کھینچ زیادہ ہے تو اسے نکالنا مشکل ہے، یعنی ionization energy زیادہ۔ اور نیا electron لینا آسان ہے، یعنی electron affinity زیادہ۔ اور دوسروں کے electrons کھینچنا بھی آسان ہے، یعنی electronegativity زیادہ۔

تو تینوں ایک ساتھ چلتی ہیں، اور تینوں size کے الٹ چلتی ہیں۔

اب لگائیں۔ Period میں بائیں سے دائیں size گھٹتا ہے۔ تو تینوں بڑھیں گی۔

اور group میں اوپر سے نیچے size بڑھتا ہے، کیونکہ نئی shell آ جاتی ہے۔ تو تینوں گھٹیں گی۔

اور shielding effect؟ وہ group میں نیچے بڑھتا ہے، کیونکہ اندر والی shells زیادہ ہو جاتی ہیں۔ اور period میں تقریباً وہی رہتا ہے، کیونکہ اندر والی shells وہی رہتی ہیں۔

تو پوری table کا خلاصہ: size یاد رکھیں، اور باقی سب اس کے الٹ لکھ دیں۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
"""),

L("4.4", "chem-ch04-characteristic-properties",
  "Metallic character, reactivity and density, the alkali metals, and how to place an unknown element.",
  """
<h1><span class="emoji">🔩</span> Chemistry Ch 4.4: Characteristic Properties</h1>
<div class="sub">Chapter 4 · kitab ke page 45 se 72 · sections 4.4.1 se 4.4.6</div>
<table>
<tr><th style="width:34%">Property</th><th style="width:33%">Period mein</th><th style="width:33%">Group mein (neeche)</th></tr>
<tr><td><b>Metallic character</b></td><td>Ghatta hai</td><td><b>Barhta</b> hai</td></tr>
<tr><td><b>Reactivity</b> (Group 1)</td><td>not applicable</td><td><b>Barhti</b> hai</td></tr>
<tr><td><b>Density</b></td><td>not applicable</td><td><b>Barhti</b> hai</td></tr>
</table>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Metallic character ka matlab</span>
Dhat hone ka matlab hai <b>electron denay ki aamadgi</b>. Group mein neeche atom <b>bara</b> hota hai, bairooni
electron <b>door</b> hota hai, is liye <b>asaani se</b> nikal jata hai. Isi liye neeche jate hue dhat pan barhta hai.<br>
Aur period mein dayein jate hue atom chhota hota hai, electron mazbooti se pakra hota hai, is liye dhat pan ghatta hai.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Alkali metals (Group 1) ki khasoosiyat</span>
Naram, kam kasafat wali, aur <b>bohat</b> reactive. Paani se mila kar hydrogen deti hain.<br>
Neeche jate hue <b>reactivity barhti</b> hai: Li se Na, Na se K, aur K sab se zyada tez.<br>
<b>Peshangoi:</b> agar Group 1 ke kisi naye element ke baare mein poochha jaye, to jo rujhan oopar hai wohi aage
barha kar jawab likhein. Yehi kitab ka section 4.4.5 hai.</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Anjaan element ki jagah dhoondna</span>
Us ki <b>electronic configuration</b> likhein. Sab se bara shell = <b>period</b>. Bairooni electrons =
<b>group</b>. Aakhri sub-shell = <b>block</b>. Phir us group ki khasoosiyat us par lagu kar dein.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>How do <b>metallic character</b>, <b>reactivity</b> and <b>density</b> change as you go down a group? Explain
the reason for the metallic character trend.</li>
<li>Give three properties of the alkali metals, and explain how you would predict the behaviour of an unknown
group 1 element placed below potassium.</li>
</ol></div>
<!--KEY 1. Going down a group, metallic character increases, reactivity (group 1) increases and density
increases. Metallic character increases because the atom gets larger, the outer electron is further from the
nucleus and is lost more easily, and metallic character is the readiness to give up electrons.
2. Alkali metals are soft, have low density and are very reactive, reacting with water to give hydrogen. For an
unknown element below potassium, continue the trend: it would be even more reactive, even more metallic, and
denser than potassium. -->
""",
  """السلام علیکم سیماب۔ آج کا سبق پچھلے سبق کا جوڑ ہے۔ کل ہم نے size کا اصول سیکھا تھا۔ آج دیکھیں گے کہ اسی اصول سے دھاتوں کا برتاؤ کیسے نکلتا ہے۔

پہلے ایک سوال۔ Group ایک کی دھاتیں پانی میں ڈالو تو رد عمل ہوتا ہے۔ Lithium ڈالو تو ہلکا سا۔ Sodium ڈالو تو تیز۔ اور potassium ڈالو تو آگ لگ جاتی ہے۔

تینوں ایک ہی group میں ہیں۔ پھر نیچے والا زیادہ خطرناک کیوں ہے؟

جواب وہی ہے جو کل تھا: size۔

دیکھیں۔ دھات ہونے کا مطلب کیا ہے؟ اس کا مطلب ہے electron دینے کی آمادگی۔ جو جتنی آسانی سے electron دے، وہ اتنی ہی زیادہ دھات ہے۔

اب group میں نیچے جائیں۔ atom بڑا ہوتا جاتا ہے۔ بیرونی electron nucleus سے دور ہوتا جاتا ہے۔ اور دور ہونے کا مطلب ہے کھینچ کمزور۔ تو electron آسانی سے نکل جاتا ہے۔

اسی لیے نیچے جاتے ہوئے دھات پن بڑھتا ہے۔ اور اسی لیے potassium، جو sodium سے نیچے ہے، زیادہ شدت سے رد عمل کرتا ہے۔

اور period میں؟ دائیں جاتے ہوئے atom چھوٹا ہوتا ہے، electron مضبوطی سے پکڑا ہوتا ہے، تو دھات پن گھٹتا ہے۔ اسی لیے بائیں طرف دھاتیں ہیں اور دائیں طرف غیر دھاتیں۔

اب تین رجحان ایک ساتھ، group میں نیچے جاتے ہوئے۔ Metallic character بڑھتا ہے۔ Reactivity بڑھتی ہے۔ اور density بھی بڑھتی ہے۔

اب alkali metals، یعنی group ایک، کی خصوصیات۔ یہ نرم ہوتی ہیں، ان کی کثافت کم ہوتی ہے، اور یہ بہت reactive ہوتی ہیں۔ پانی سے مل کر hydrogen دیتی ہیں۔

اور آخر میں ایک مہارت جو کتاب خاص طور پر سکھاتی ہے: پیشن گوئی۔

اگر امتحان میں کسی ایسے element کے بارے میں پوچھا جائے جو آپ نے پڑھا ہی نہیں، تو گھبرائیں نہیں۔ اس کی configuration لکھیں۔ سب سے بڑا shell نمبر period بتا دے گا۔ بیرونی electrons group بتا دیں گے۔ اور آخری sub-shell block بتا دے گی۔

پھر اس group کا جو رجحان ہے وہی آگے بڑھا دیں۔ مثلاً اگر وہ potassium سے نیچے ہے تو وہ potassium سے بھی زیادہ reactive ہو گا، زیادہ دھاتی ہو گا، اور زیادہ کثیف ہو گا۔

یہی طریقہ ہے۔ آپ کو element جاننے کی ضرورت نہیں، صرف جگہ جاننے کی ضرورت ہے۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
"""),

L("4.5", "chem-ch04-transition-elements",
  "The five properties that mark out the transition elements, including variable oxidation states and their use as catalysts.",
  """
<h1><span class="emoji">🎨</span> Chemistry Ch 4.5: Transition Elements</h1>
<div class="sub">Chapter 4 · kitab ke page 45 se 72</div>
<p>Periodic table ke <b>darmiyan</b> wala chaura hissa. Ye <b>d block</b> ke elements hain: iron, copper, zinc,
nickel, chromium.</p>
<div class="box def"><span class="t"><span class="emoji">📖</span> Paanch khasoosiyat, ye hi poochhi jati hain</span>
<b>1. Ooonchi density.</b><br>
<b>2. Ooonche melting points.</b><br>
<b>3. Mukhtalif oxidation states</b> (variable), yani ek hi dhat alag alag charge le sakti hai.<br>
<b>4. Rangeen compounds</b> banate hain.<br>
<b>5. Catalysts</b> ke tor par kaam karte hain.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Ghar se misalein</span>
<b>Variable oxidation states:</b> iron Fe<sup>2+</sup> bhi banata hai aur Fe<sup>3+</sup> bhi. Isi liye zang ka
rang alag alag hota hai.<br>
<b>Rangeen compounds:</b> copper ke compounds <b>neele sabz</b>, aur isi liye purani tambe ki chhat sabz par jati hai.<br>
<b>Catalysts:</b> Haber's process mein <b>iron</b>, aur contact process mein vanadium.</div>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Rang aur catalyst, dono ki ek hi wajah</span>
Ye dono <b>d sub-shell</b> ke adhoore bharne se aate hain. Adhoori d sub-shell electrons ko aane jaane deti hai,
isi se rang bhi banta hai aur catalyst wala kaam bhi hota hai.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Name the <b>five</b> characteristic properties of the transition elements your book gives.</li>
<li>Give one everyday example of a transition metal showing variable oxidation states, and one of a transition
metal acting as a catalyst.</li>
</ol></div>
<!--KEY 1. High density, high melting points, variable oxidation states, coloured compounds, and they act as
catalysts. 2. Iron forms both Fe2+ and Fe3+. Iron is the catalyst in Haber's process (vanadium in the contact
process is also acceptable). -->
""",
  """السلام علیکم سیماب۔ آج کا سبق periodic table کے بیچ والے حصے کا ہے: transition elements۔

پہلے ایک سوال۔ آپ نے پرانی عمارتوں پر تانبے کی چھتیں دیکھی ہوں گی۔ تانبا نیا ہو تو سرخی مائل بھورا ہوتا ہے۔ مگر پرانی چھتیں سبز ہو جاتی ہیں۔ کیوں؟

اور دوسرا سوال۔ لوہے کا زنگ کبھی نارنجی ہوتا ہے، کبھی گہرا بھورا۔ ایک ہی لوہا، دو رنگ کیوں؟

دونوں سوالوں کا جواب ایک ہی ہے، اور وہ آج کے سبق میں ہے۔

Transition elements وہ ہیں جو periodic table کے بیچ میں ہیں۔ یہ d block کے elements ہیں۔ Iron، copper، zinc، nickel، chromium، یہ سب اسی میں آتے ہیں۔

اور کتاب ان کی پانچ خصوصیات بتاتی ہے۔ یہی پوچھی جاتی ہیں، اس لیے پانچوں گن لیں۔

پہلی، ان کی density اونچی ہوتی ہے۔ اسی لیے لوہا اٹھانے میں بھاری لگتا ہے۔

دوسری، ان کے melting points اونچے ہوتے ہیں۔ اسی لیے لوہے کو پگھلانے کے لیے بھٹی چاہیے۔

تیسری، اور یہ سب سے اہم ہے: یہ مختلف oxidation states رکھتے ہیں۔ یعنی ایک ہی دھات الگ الگ charge لے سکتی ہے۔

اور یہیں زنگ والے سوال کا جواب ہے۔ Iron دو مثبت بھی بنتا ہے اور تین مثبت بھی۔ اور دونوں کا رنگ الگ ہوتا ہے۔ اسی لیے زنگ کا رنگ ایک جیسا نہیں ہوتا۔

چوتھی خصوصیت، یہ رنگین compounds بناتے ہیں۔ اور یہیں تانبے والی چھت کا جواب ہے۔ تانبے کے compounds نیلے سبز ہوتے ہیں، اور وقت کے ساتھ چھت پر وہی تہہ بن جاتی ہے۔

اور پانچویں، یہ catalysts کے طور پر کام کرتے ہیں۔ Haber's process میں iron catalyst ہے۔

اب ایک دلچسپ بات۔ رنگ اور catalyst، یہ دونوں ایک ہی وجہ سے ہیں۔

دونوں d sub-shell کے ادھورے بھرنے سے آتے ہیں۔ جب d sub-shell آدھی بھری ہو تو electrons آسانی سے آ جا سکتے ہیں۔ اسی آمد و رفت سے رنگ بنتا ہے، اور اسی سے catalyst والا کام ہوتا ہے۔

تو ایک ہی وجہ، دو نتیجے۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
"""),

L("4.6", "chem-ch04-lanthanides-actinides",
  "The two rows printed below the table: where they really belong and why they are separated.",
  """
<h1><span class="emoji">📏</span> Chemistry Ch 4.6: Lanthanides and Actinides</h1>
<div class="sub">Chapter 4 · kitab ke page 45 se 72</div>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Ye neeche alag kyun chhapi hain</span>
Periodic table ke <b>neeche</b> do alag qatarein hoti hain. Ye <b>bahar</b> nahin hain, balke asal mein table ke
<b>andar</b> hi ki hain.<br>
Agar inhein apni jagah par rakha jaye to table itni <b>chaurai</b> ho jati hai ke safhay par aati hi nahin. Is liye
inhein neeche utar kar chhapa jata hai. Wajah sirf <b>jagah</b> ki hai, chemistry ki nahin.</div>
<table>
<tr><th style="width:28%">Qataar</th><th style="width:72%">Tafseel</th></tr>
<tr><td><b>Lanthanides</b></td><td><b>Period 6</b>, lanthanum ke baad. Inhein <b>rare earth elements</b> bhi
kehte hain. Aakhri electron <b>f</b> sub-shell mein jata hai.</td></tr>
<tr><td><b>Actinides</b></td><td><b>Period 7</b>, actinium ke baad. In mein <b>uranium</b> aur <b>plutonium</b>
aate hain. Zyadatar <b>radioactive</b> hain.</td></tr>
</table>
<div class="box def"><span class="t"><span class="emoji">📖</span> f block</span>
Dono qatarein <b>f block</b> ki hain, kyunke in ka aakhri electron f sub-shell mein jata hai.<br>
Yaad rakhein: <b>s block</b> bayein, <b>p block</b> dayein, <b>d block</b> darmiyan, aur <b>f block</b> neeche.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>What are the <b>lanthanides</b> and <b>actinides</b>, which periods do they belong to, and which block are
they in?</li>
<li>Why are these two rows printed separately below the main table? Name two actinides.</li>
</ol></div>
<!--KEY 1. The lanthanides follow lanthanum in period 6 and the actinides follow actinium in period 7. Both are
f block elements, because their last electron enters an f sub-shell. The lanthanides are also called the rare
earth elements. 2. They are printed below only to keep the table narrow enough to fit a page; chemically they
belong inside period 6 and period 7. Two actinides: uranium and plutonium. -->
""",
  """السلام علیکم سیماب۔ آج کا سبق سب سے چھوٹا ہے، مگر اس میں ایک سوال کا جواب ہے جو شاید آپ کے ذہن میں آیا ہو۔

Periodic table دیکھیں۔ نیچے الگ سے دو قطاریں چھپی ہوتی ہیں، باقی table سے کٹی ہوئی۔ کیا وہ periodic table کا حصہ نہیں ہیں؟ انہیں باہر کیوں نکالا گیا ہے؟

جواب دلچسپ ہے، اور یہ chemistry کی وجہ سے نہیں ہے۔ یہ صرف کاغذ کی وجہ سے ہے۔

وہ دونوں قطاریں اصل میں table کے اندر ہی کی ہیں۔ اگر انہیں ان کی اصل جگہ پر رکھا جائے تو table اتنی چوڑی ہو جائے گی کہ کتاب کے صفحے پر آئے گی ہی نہیں۔ اس لیے انہیں نیچے اتار کر چھاپ دیا جاتا ہے۔

بس اتنی سی بات ہے۔ جگہ کا مسئلہ، اور کچھ نہیں۔

اب یہ دونوں قطاریں ہیں کیا۔

پہلی قطار lanthanides کہلاتی ہے۔ یہ period چھ میں آتی ہے، lanthanum کے بعد۔ انہیں rare earth elements بھی کہتے ہیں۔

اور دوسری قطار actinides کہلاتی ہے۔ یہ period سات میں آتی ہے، actinium کے بعد۔ اور اس میں وہ نام آتے ہیں جو آپ نے سنے ہوں گے: uranium اور plutonium۔ ان میں سے زیادہ تر radioactive ہیں۔

اور دونوں قطاریں f block کی ہیں۔ یاد ہے block کیسے طے ہوتا ہے؟ آخری electron جس sub-shell میں جائے۔ ان دونوں کا آخری electron f sub-shell میں جاتا ہے، اس لیے یہ f block ہیں۔

تو اب پوری table کا نقشہ ذہن میں بٹھا لیں۔

s block بائیں طرف۔ p block دائیں طرف۔ d block بیچ میں۔ اور f block نیچے، الگ چھپا ہوا، مگر اصل میں چھٹے اور ساتویں period کے اندر کا۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
"""),

L("4.7", "chem-ch04-halogens",
  "The halogens: their appearance, why reactivity falls down the group, displacement reactions and hydrogen halide stability.",
  """
<h1><span class="emoji">🧂</span> Chemistry Ch 4.7: The Halogens (Group 17)</h1>
<div class="sub">Chapter 4 · kitab ke page 45 se 72</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Pehchan</span>
Bairooni configuration <b>ns<sup>2</sup> np<sup>5</sup></b>, yani <b>7 bairooni electrons</b>. Sirf <b>ek</b> ki
kami hai, is liye ye <b>bohat reactive</b> hain aur <b>-1</b> ion banate hain.<br>
<b>Shakal:</b> F<sub>2</sub> halka peela gas &middot; Cl<sub>2</sub> sabzi maael peela gas &middot; Br<sub>2</sub>
surkhi maael bhoora <b>maaye</b> &middot; I<sub>2</sub> bhoori siyah <b>thos</b>.<br>
Neeche jate hue <b>density barhti</b> hai aur <b>reactivity ghatti</b> hai.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Do tarteebein jo yaad karni hain</span>
<b>Reactivity aur displacement:</b> <b>F<sub>2</sub> &gt; Cl<sub>2</sub> &gt; Br<sub>2</sub> &gt; I<sub>2</sub></b><br>
Yani oopar wala neeche wale ko us ke namak se <b>nikal</b> deta hai. Misal: Cl<sub>2</sub> + 2KBr &rarr; 2KCl +
Br<sub>2</sub>. Ulta nahin hoga.<br>
<b>Hydrogen halides ki garmi se mazbooti:</b> <b>HF &gt; HCl &gt; HBr &gt; HI</b><br>
Yani HF sab se mazboot hai aur HI sab se jaldi toot jata hai.</div>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Dono tarteebein ek jaisi hain</span>
Dono mein <b>F sab se oopar aur I sab se neeche</b>. Wajah wohi purani: F ka atom <b>sab se chhota</b> hai, to wo
electron ko sab se zyada zor se kheenchta hai. Isi se reactivity bhi zyada aur bond bhi mazboot.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Give the appearance and physical state of the four halogens, and say how density and reactivity change down
the group.</li>
<li>Write the displacement order and the thermal stability order of the hydrogen halides. Will Br<sub>2</sub>
displace Cl<sub>2</sub> from KCl? Explain.</li>
</ol></div>
<!--KEY 1. F2 pale yellow gas, Cl2 greenish yellow gas, Br2 reddish brown liquid, I2 brownish black solid.
Down the group density increases and reactivity decreases.
2. Displacement: F2 > Cl2 > Br2 > I2. Thermal stability: HF > HCl > HBr > HI. No, bromine will not displace
chlorine, because chlorine is above bromine and therefore more reactive; only a more reactive halogen displaces a
less reactive one. -->
""",
  """السلام علیکم سیماب۔ آج group سترہ کا سبق ہے، halogens۔ اور آج دو ترتیبیں یاد کرنی ہیں، مگر دونوں ایک ہی ہیں، اس لیے کام آدھا ہے۔

پہلے ایک سوال۔ اگر chlorine کو potassium bromide میں ڈالیں تو bromine باہر نکل آتی ہے۔ لیکن اگر bromine کو potassium chloride میں ڈالیں تو کچھ نہیں ہوتا۔ ایک طرف چلتا ہے، دوسری طرف نہیں۔ کیوں؟

پہلے پہچان۔ Halogens کی بیرونی configuration ہے n s دو n p پانچ، یعنی سات بیرونی electrons۔ آٹھ پورے کرنے کے لیے صرف ایک کی کمی ہے۔ اسی لیے یہ بہت reactive ہیں اور منفی ایک ion بناتے ہیں۔

اب ان کی شکلیں، اور یہ پوچھی جاتی ہیں۔

Fluorine ہلکی پیلی گیس ہے۔ Chlorine سبزی مائل پیلی گیس۔ Bromine سرخی مائل بھورا مائع۔ اور iodine بھوری سیاہ ٹھوس۔

غور کریں: اوپر سے نیچے جاتے ہوئے گیس سے مائع اور پھر ٹھوس۔ یعنی نیچے جاتے ہوئے density بڑھتی ہے۔

اور reactivity؟ وہ نیچے جاتے ہوئے گھٹتی ہے۔ یہ دھاتوں کے الٹ ہے، اس لیے دھیان رکھیں۔

اب پہلی ترتیب، displacement کی۔ F دو، پھر Cl دو، پھر Br دو، پھر I دو۔

اور اس کا مطلب ہے: جو اوپر ہے وہ نیچے والے کو اس کے نمک سے نکال دیتا ہے۔

تو اوپر والے سوال کا جواب مل گیا۔ Chlorine، bromine سے اوپر ہے، اس لیے وہ bromine کو نکال دیتی ہے۔ مگر bromine، chlorine سے نیچے ہے، اس لیے وہ chlorine کو نہیں نکال سکتی۔ طاقتور کمزور کو نکالتا ہے، الٹا نہیں ہوتا۔

اب دوسری ترتیب، hydrogen halides کی گرمی سے مضبوطی۔ HF، پھر HCl، پھر HBr، پھر HI۔

یعنی HF سب سے مضبوط ہے اور HI سب سے جلدی ٹوٹ جاتا ہے۔

اور اب دیکھیں دونوں ترتیبیں ایک جیسی ہیں۔ دونوں میں F سب سے اوپر اور I سب سے نیچے۔

وجہ وہی پرانی ہے: fluorine کا atom سب سے چھوٹا ہے۔ چھوٹا ہے تو کھینچ سب سے زیادہ۔ اسی لیے وہ سب سے زیادہ reactive بھی ہے اور اس کا bond بھی سب سے مضبوط ہے۔

تو ایک ترتیب یاد کریں، دونوں کام ہو جائیں گے۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
"""),

L("4.8", "chem-ch04-noble-gases",
  "Why the noble gases do nothing: full outer shells, single atoms, and what they are used for.",
  """
<h1><span class="emoji">🎈</span> Chemistry Ch 4.8: Noble Gases (Group 18)</h1>
<div class="sub">Chapter 4 · kitab ke page 45 se 72</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Teen khasoosiyat</span>
<b>1. Inert:</b> ye kisi se amal nahin karte.<br>
<b>2. Mono-atomic:</b> ye <b>akele atom</b> ki shakl mein rehte hain. Baqi gases jori (O<sub>2</sub>,
N<sub>2</sub>) banati hain, ye nahin.<br>
<b>3. Bhari hui bairooni shell:</b> helium ke paas <b>2</b>, baqi sab ke paas <b>8</b>.</div>
<table>
<tr><th style="width:26%">Gas</th><th style="width:74%">Bairooni configuration</th></tr>
<tr><td>Helium (He)</td><td>1s<sup>2</sup> &nbsp; (sirf <b>2</b>, kyunke pehli shell mein 2 hi aate hain)</td></tr>
<tr><td>Neon (Ne)</td><td>2s<sup>2</sup> 2p<sup>6</sup></td></tr>
<tr><td>Argon (Ar)</td><td>3s<sup>2</sup> 3p<sup>6</sup></td></tr>
</table>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Inert hone ki wajah, aur do nateeje</span>
Jab bairooni shell <b>poori bhari</b> ho to atom ko na electron <b>denay</b> ki zaroorat hai na <b>lenay</b> ki.
Wo pehle hi mustahkam hai.<br>
Isi se dono baqi baatein nikal aati hain: wo <b>ion nahin</b> banate, aur wo doosre atom se <b>jorta</b> bhi nahin,
is liye <b>akela</b> rehta hai, yani mono-atomic.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Isi be-amli ka faida</span>
Helium ghubbaron mein, kyunke wo halki hai aur <b>aag nahin pakarti</b>. Neon roshni wale signon mein. Aur argon
bulb ke andar, taake filament jal na jaye.<br>
Yani in ka faida hi ye hai ke ye <b>kuch nahin karte</b>.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Give the three characteristic properties of the noble gases, and write the outer electronic configuration of
helium, neon and argon.</li>
<li>Explain why the noble gases are both <b>inert</b> and <b>mono-atomic</b>. Why does helium have 2 outer
electrons rather than 8?</li>
</ol></div>
<!--KEY 1. Inert, mono-atomic, and they have full outer shells. He 1s2, Ne 2s2 2p6, Ar 3s2 3p6.
2. A full outer shell means the atom has no need to gain or lose electrons, so it does not react (inert) and does
not bond to another atom, so it stays as a single atom (mono-atomic). Helium has only 2 because the first shell
holds a maximum of 2 electrons, so 2 is already full for it. -->
""",
  """السلام علیکم سیماب۔ آج group اٹھارہ کا سبق ہے، noble gases۔ اور آج کا موضوع عجیب ہے، کیونکہ آج ہم ان elements کی بات کریں گے جن کی خاص بات یہ ہے کہ وہ کچھ نہیں کرتے۔

پہلے ایک سوال۔ آپ نے سنا ہو گا کہ غباروں میں helium بھرتے ہیں۔ hydrogen بھی ہلکی ہے، اور helium سے بھی ہلکی۔ تو hydrogen کیوں نہیں بھرتے؟

جواب آخر میں، پہلے خصوصیات۔

کتاب تین خصوصیات بتاتی ہے۔

پہلی، یہ inert ہیں، یعنی کسی سے عمل نہیں کرتے۔

دوسری، یہ mono-atomic ہیں، یعنی اکیلے atom کی شکل میں رہتے ہیں۔ یہ بات غور کرنے والی ہے۔ oxygen O دو بن کر رہتی ہے، nitrogen N دو بن کر۔ مگر helium صرف He رہتا ہے۔ اکیلا۔

اور تیسری، ان کی بیرونی shell بھری ہوئی ہوتی ہے۔ helium کے پاس دو، اور باقی سب کے پاس آٹھ۔

اب configurations۔ Helium ایک s دو۔ Neon دو s دو، دو p چھ۔ اور Argon تین s دو، تین p چھ۔

اور یہاں ایک سوال اٹھتا ہے جو اکثر پوچھا جاتا ہے: helium کے پاس آٹھ کیوں نہیں، صرف دو کیوں؟

جواب یہ ہے کہ پہلی shell میں گنجائش ہی صرف دو کی ہے۔ تو helium کے لیے دو ہی پورے ہیں۔ اس کی shell بھری ہوئی ہے۔

اب اصل نکتہ۔ یہ inert کیوں ہیں؟

سوچیں۔ باقی سارے atoms عمل کرتے ہی اس لیے ہیں کہ وہ اپنی بیرونی shell پوری کرنا چاہتے ہیں۔ کوئی electron دینا چاہتا ہے، کوئی لینا چاہتا ہے۔

مگر noble gases کی shell پہلے ہی پوری ہے۔ انہیں نہ دینے کی ضرورت ہے نہ لینے کی۔ وہ پہلے ہی مستحکم ہیں۔

اور اسی ایک بات سے باقی دونوں خصوصیات نکل آتی ہیں۔ وہ ion نہیں بناتے، کیونکہ electron کا لین دین ہی نہیں کرتے۔ اور وہ کسی دوسرے atom سے جڑتے بھی نہیں، اس لیے اکیلے رہتے ہیں۔

اب غبارے والا جواب۔ Hydrogen آگ پکڑ لیتی ہے، اور helium نہیں پکڑتی، کیونکہ وہ inert ہے۔ اسی لیے غباروں میں helium بھرتے ہیں۔

اور یہی ان کا سب سے بڑا فائدہ ہے۔ Neon روشنی والے signs میں، اور argon بلب کے اندر تاکہ filament جل نہ جائے۔ ان کا کام ہی یہ ہے کہ وہ کچھ نہ کریں۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
"""),

L("4.9", "chem-ch04-metals-vs-nonmetals",
  "The full comparison of metals and non-metals: conductivity, malleability, melting points and how they form ions.",
  """
<h1><span class="emoji">⚖️</span> Chemistry Ch 4.9: Metals and Non-Metals Compared</h1>
<div class="sub">Chapter 4 · kitab ke page 45 se 72 · section 4.9</div>
<table>
<tr><th style="width:36%">Property</th><th style="width:32%">Metals</th><th style="width:32%">Non-metals</th></tr>
<tr><td>Thermal conductivity</td><td><b>Ache</b> conductor</td><td>Khraab (insulators)</td></tr>
<tr><td>Electrical conductivity</td><td><b>Ache</b> conductor</td><td>Khraab (graphite istisna)</td></tr>
<tr><td>Malleability</td><td><b>Peet kar chaadar</b> ban jati hai</td><td><b>Bhurbhure</b> (brittle), toot jate hain</td></tr>
<tr><td>Ductility</td><td><b>Taar</b> khinch jati hai</td><td>Nahin khinchti</td></tr>
<tr><td>Melting / boiling point</td><td>Aam tor par <b>ooncha</b></td><td>Aam tor par <b>neecha</b></td></tr>
<tr><td>Ion banana</td><td>Electron <b>khote</b> hain &rarr; <b>cation</b></td><td>Electron <b>lete</b> hain &rarr; <b>anion</b></td></tr>
<tr><td>Table mein jagah</td><td><b>Bayein</b> taraf</td><td><b>Dayein</b> taraf</td></tr>
</table>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Saari table ek hi baat se nikalti hai</span>
Dhat mein electrons <b>azad</b> hote hain, poore maddey mein ghoomte hue, aur isi ko <b>sea of electrons</b> kehte
hain.<br>
Azad electrons <b>bijli</b> le jate hain, aur <b>garmi</b> bhi. Aur jab aap dhat ko peetein to atoms ki tehen
<b>phisal</b> jati hain magar electron ka samundar unhein jore rakhta hai, is liye wo <b>tootti nahin, phail</b>
jati hai. Yehi malleability aur ductility hai.<br>
Non-metal mein electrons bandhay hue hain, is liye na bijli chalti hai aur na wo phailta hai, bas <b>toot</b> jata hai.</div>
<div class="box warn"><span class="t"><span class="emoji">⚠️</span> Do istisna yaad rakhein</span>
<b>Graphite</b> ek non-metal hai magar <b>bijli chalata</b> hai, kyunke us mein chautha electron azad hai.<br>
<b>Mercury</b> ek dhat hai magar kamre ke temperature par <b>maaye</b> hai.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Compare metals and non-metals for thermal and electrical conductivity, malleability and ductility, and
melting point. Say which side of the periodic table each is on.</li>
<li>Explain, using the idea of free electrons, why metals conduct electricity and can be hammered into sheets
while non-metals are brittle. Give one exception to each rule.</li>
</ol></div>
<!--KEY 1. Metals are good thermal and electrical conductors, malleable and ductile, usually with high melting
and boiling points, and sit on the left. Non-metals are poor conductors, brittle and not ductile, usually with
low melting points, and sit on the right.
2. In a metal the outer electrons are free and move through the whole structure (a sea of electrons). Those free
electrons carry current and heat. When a metal is hammered the layers of atoms slide while the electron sea keeps
them bonded, so it flattens instead of breaking. In a non-metal the electrons are held in fixed bonds, so there
is nothing to carry current and the rigid bonds snap, making it brittle. Exceptions: graphite is a non-metal that
conducts; mercury is a metal that is liquid at room temperature. -->
""",
  """السلام علیکم سیماب۔ آج باب چار کا آخری سبق ہے: دھاتوں اور غیر دھاتوں کا مقابلہ۔ اور آج آپ کو ایک پوری table یاد کرنے کی ضرورت نہیں۔ صرف ایک تصویر ذہن میں بٹھا لیں، اور ساری table خود نکل آئے گی۔

پہلے ایک سوال۔ لوہے کی چادر پر ہتھوڑا ماریں تو وہ پھیل جاتی ہے، ٹوٹتی نہیں۔ لیکن کوئلے کے ٹکڑے پر ہتھوڑا ماریں تو وہ چکنا چور ہو جاتا ہے۔ دونوں ٹھوس ہیں۔ فرق کیا ہے؟

جواب ایک لفظ میں ہے: آزاد electrons۔

دھات کے اندر بیرونی electrons کسی ایک atom کے نہیں ہوتے۔ وہ پورے مادے میں آزاد گھومتے رہتے ہیں۔ اسے sea of electrons کہتے ہیں، یعنی electrons کا سمندر۔

اب اس ایک تصویر سے ساری table نکالتے ہیں۔

پہلا، بجلی۔ بجلی چلانے کے لیے آزاد charge چاہیے۔ دھات میں وہ موجود ہے، تو دھات بجلی چلاتی ہے۔ غیر دھات میں electrons bond میں بندھے ہوئے ہیں، تو وہ نہیں چلاتی۔

دوسرا، گرمی۔ وہی آزاد electrons گرمی بھی لے جاتے ہیں۔ اسی لیے چمچ کا ایک سرا گرم کریں تو دوسرا بھی گرم ہو جاتا ہے۔

تیسرا، اور یہی اوپر والے سوال کا جواب ہے۔ جب آپ دھات پر ہتھوڑا مارتی ہیں تو atoms کی تہیں ایک دوسری پر پھسل جاتی ہیں۔ مگر electron کا سمندر انہیں جوڑے رکھتا ہے، اس لیے وہ ٹوٹتی نہیں، پھیل جاتی ہے۔ اسی کو malleability کہتے ہیں۔

اور اسی طرح تار کھینچی جا سکتی ہے، جسے ductility کہتے ہیں۔

غیر دھات میں electrons اپنی جگہ بندھے ہوئے ہیں۔ تہیں پھسل نہیں سکتیں۔ تو زور لگاؤ تو bond ٹوٹ جاتے ہیں اور وہ چکنا چور ہو جاتی ہے۔ اسی کو brittle کہتے ہیں۔

چوتھا، melting point۔ دھاتوں کا عام طور پر اونچا، غیر دھاتوں کا نیچا۔

پانچواں، ion بنانا۔ دھاتیں electron کھو کر cation بناتی ہیں۔ غیر دھاتیں electron لے کر anion بناتی ہیں۔

اور چھٹا، جگہ۔ دھاتیں بائیں طرف، غیر دھاتیں دائیں طرف۔

اور آخر میں دو استثنا، جو امتحان میں پوچھے جاتے ہیں۔

Graphite ایک غیر دھات ہے مگر بجلی چلاتا ہے، کیونکہ اس میں چوتھا electron آزاد ہوتا ہے۔ یہ بات آپ باب دو میں پڑھ چکی ہیں۔

اور mercury ایک دھات ہے مگر کمرے کے درجہ حرارت پر مائع ہوتی ہے۔

اس کے ساتھ باب چار مکمل ہو گیا۔ آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
"""),
]

if __name__ == "__main__":
    build(LESSONS, C)
