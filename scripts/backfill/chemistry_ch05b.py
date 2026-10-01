# -*- coding: utf-8 -*-
"""Chemistry Chapter 5, lessons 5.3 to 5.6. Her book p73 to 94."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import build
C = "#1e7a4a"; S = "chemistry"

def L(ref, slug, summary, note, script):
    return {"subject": S, "chapter": 5, "ref": ref, "slug": slug,
            "summary": summary, "note": note, "script": script}

LESSONS = [
L("5.3", "chem-ch05-types-of-bonds",
  "The four bond types: ionic, covalent, polar against nonpolar, and the coordinate bond where one atom supplies both electrons.",
  """
<h1><span class="emoji">\U0001F91D</span> Chemistry Ch 5.3: Types of Bonds</h1>
<div class="sub">Chapter 5 &middot; sections 5.3.1 se 5.3.4 &middot; kitab ke page 73 se 94</div>
<div class="box def"><span class="t"><span class="emoji">\U0001F4D6</span> 5.3.1 Ionic Bond</span>
Ek atom electron <b>de</b> deta hai, doosra <b>le</b> leta hai. Dene wala <b>cation</b> (+) banta hai aur lene
wala <b>anion</b> (&minus;). Phir ye ulte charge <b>ek doosre ko kheenchte</b> hain, aur wohi ionic bond hai.<br>
<b>Kitab ki misalein:</b> NaCl, MgF<sub>2</sub>, MgO, NaF. Dikhane ke liye <b>electron dot aur cross</b> diagram
banate hain.</div>
<div class="box def"><span class="t"><span class="emoji">\U0001F4D6</span> 5.3.2 Covalent Bond</span>
Dono atoms electron <b>share</b> karte hain, koi deta leta nahin.<br>
<b>Single bond:</b> ek jora share (H<sub>2</sub>, F<sub>2</sub>, CH<sub>4</sub>, H<sub>2</sub>O)<br>
<b>Double bond:</b> do jore (O<sub>2</sub>, CO<sub>2</sub>) &nbsp;&nbsp;
<b>Triple bond:</b> teen jore (N<sub>2</sub>, HCN)</div>
<div class="box trick"><span class="t"><span class="emoji">\U0001F9E0</span> 5.3.3 Polar aur Nonpolar, aur farq kaise pehchanein</span>
Share karne ka matlab ye nahin ke <b>barabar</b> share ho raha hai.<br>
<b>Nonpolar:</b> dono atoms ek jaise, electronegativity ka farq <b>nahin</b>, to electrons <b>beech</b> mein rehte
hain. Misal: H<sub>2</sub>, O<sub>2</sub>, N<sub>2</sub>.<br>
<b>Polar:</b> ek atom zyada electronegative, wo electrons <b>apni taraf</b> kheench leta hai. Us par halka
<b>manfi</b> aur doosre par halka <b>musbat</b> charge aa jata hai. Misal: H<sub>2</sub>O, HCl.<br>
<span style="color:#5b6475">Paani ki saari khasoosiyat isi polarity se aati hain.</span></div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> 5.3.4 Coordinate Covalent Bond</span>
Ye bhi share hi hai, magar ek farq ke saath: <b>dono electrons ek hi atom</b> dete hain. Doosra atom sirf
<b>khaali jagah</b> deta hai.<br>
Dene wale ke paas <b>lone pair</b> hona zaroori hai.<br>
<b>Kitab ki teen misalein:</b> NH<sub>4</sub><sup>+</sup> (ammonia nitrogen apna lone pair H<sup>+</sup> ko deta
hai), H<sub>3</sub>O<sup>+</sup> (paani ki oxygen), aur NH<sub>3</sub>&middot;BF<sub>3</sub>.</div>
<div class="box quiz"><span class="t"><span class="emoji">\U0001F9EA</span> Quiz</span>
<ol class="q">
<li>Explain how an <b>ionic</b> bond forms and how a <b>covalent</b> bond forms, with two examples of each from
your book. Then name a molecule with a single, a double and a triple bond.</li>
<li>What is the difference between a <b>polar</b> and a <b>nonpolar</b> covalent bond? Then define a
<b>coordinate covalent</b> bond and give the three examples your book provides.</li>
</ol></div>
<!--KEY 1. Ionic: one atom loses electrons to become a cation, the other gains them to become an anion, and the
opposite charges attract (NaCl, MgO, MgF2, NaF). Covalent: both atoms share electrons (H2, CH4, H2O, F2). Single
H2 or CH4; double O2 or CO2; triple N2 or HCN.
2. In a nonpolar covalent bond the atoms have equal or near-equal electronegativity so the shared electrons sit
midway (H2, O2). In a polar covalent bond one atom is more electronegative and pulls the shared pair toward
itself, giving it a slight negative and the other a slight positive charge (H2O, HCl). A coordinate covalent bond
is one where both shared electrons come from the same atom, which must have a lone pair; the other atom supplies
only the empty space. Examples: NH4+, H3O+, NH3-BF3. -->
""",
  """السلام علیکم سیماب۔ آج باب پانچ کا سب سے بڑا سبق ہے: bonds کی قسمیں۔ چار قسمیں ہیں، اور ہر ایک کی اپنی پہچان ہے۔ پہلے ایک سوال۔

Share کرنا تو انصاف کی بات لگتی ہے نا؟ دو atoms نے electrons share کر لیے، برابر برابر۔

مگر کیا share کرنا ہمیشہ برابر ہوتا ہے؟ جواب ہے نہیں۔ اور اسی ایک بات سے پانی کی ساری خصوصیات نکلتی ہیں۔ تھوڑا صبر کریں۔

پہلے پہلی قسم، ionic bond۔

اس میں ایک atom electron دے دیتا ہے اور دوسرا لے لیتا ہے۔ دینے والا cation بن جاتا ہے، یعنی مثبت۔ اور لینے والا anion، یعنی منفی۔

اور پھر؟ پھر یہ دونوں الٹے charge ایک دوسرے کو کھینچتے ہیں۔ بس وہی کھینچ ionic bond ہے۔

کتاب کی مثالیں: NaCl یعنی نمک، MgF دو، MgO، اور NaF۔ اور انہیں دکھانے کے لیے electron dot اور cross diagram بناتے ہیں، جس میں ایک atom کے electrons نقطوں سے اور دوسرے کے کراس سے دکھائے جاتے ہیں۔

دوسری قسم، covalent bond۔

اس میں کوئی دیتا لیتا نہیں۔ دونوں مل کر electrons share کرتے ہیں۔

اور share کتنے جوڑوں کا ہو، اس سے bond کا نام بدلتا ہے۔ ایک جوڑا share ہو تو single bond، جیسے H دو، CH چار، اور پانی۔ دو جوڑے ہوں تو double bond، جیسے O دو اور CO دو۔ اور تین جوڑے ہوں تو triple bond، جیسے N دو اور HCN۔

اب تیسری قسم، اور یہیں اوپر والے سوال کا جواب ہے۔

Share کرنا برابر نہیں ہوتا۔

اگر دونوں atoms ایک جیسے ہوں، جیسے H دو میں دونوں hydrogen، تو electronegativity برابر ہے۔ کوئی زیادہ نہیں کھینچ سکتا۔ تو electrons بیچ میں رہتے ہیں۔ اسے nonpolar کہتے ہیں۔

لیکن اگر ایک atom زیادہ electronegative ہو، تو وہ electrons کو اپنی طرف کھینچ لیتا ہے۔ اب electrons بیچ میں نہیں رہے، ایک طرف جھک گئے۔

اور اس کا نتیجہ؟ جس طرف electrons گئے وہاں ہلکا منفی charge، اور دوسری طرف ہلکا مثبت۔ اسے polar کہتے ہیں۔

پانی اسی لیے polar ہے۔ oxygen، hydrogen سے زیادہ electronegative ہے، تو وہ electrons اپنی طرف کھینچ لیتی ہے۔ اور پانی کی ساری خصوصیات، اس کا چیزیں گھولنا، اس کا سطحی تناؤ، سب اسی ایک بات سے آتی ہیں۔

اور چوتھی قسم، coordinate covalent bond۔

یہ بھی share ہی ہے، مگر ایک فرق کے ساتھ: دونوں electrons ایک ہی atom دیتا ہے۔ دوسرا atom صرف خالی جگہ دیتا ہے۔

اور دینے والے کے پاس lone pair ہونا ضروری ہے، یعنی ایسا جوڑا جو پہلے سے کسی bond میں نہ لگا ہو۔

کتاب تین مثالیں دیتی ہے۔ NH چار مثبت، جہاں ammonia کی nitrogen اپنا lone pair hydrogen ion کو دیتی ہے۔ H تین O مثبت، جہاں پانی کی oxygen یہی کرتی ہے۔ اور NH تین BF تین۔

تو چار قسمیں: ionic یعنی دینا لینا، covalent یعنی برابر share، polar یعنی جھکا ہوا share، اور coordinate یعنی ایک ہی کا دیا ہوا جوڑا۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
"""),

L("5.4", "chem-ch05-intermolecular-forces",
  "Forces between molecules rather than inside them: dipole-dipole attraction and hydrogen bonding with N, O or F.",
  """
<h1><span class="emoji">\U0001F4A7</span> Chemistry Ch 5.4: Intermolecular Forces</h1>
<div class="sub">Chapter 5 &middot; kitab ke page 73 se 94</div>
<p>Ek sawal. Paani sau digree par ubalta hai. Lekin H<sub>2</sub>S, jo paani se <b>bhaari</b> hai, manfi saath
digree par hi gas ban jati hai. Bhaari cheez pehle ubal gayi? Ye ulta kyun hai?</p>
<div class="box trick"><span class="t"><span class="emoji">\U0001F9E0</span> Pehle ek farq jo sab kuch khol deta hai</span>
<b>Intramolecular force:</b> molecule ke <b>andar</b>, atoms ke darmiyan. Yehi ionic aur covalent bond hain,
aur ye <b>mazboot</b> hain.<br>
<b>Intermolecular force:</b> molecule ke <b>bahar</b>, ek molecule aur doosre molecule ke darmiyan. Ye
<b>kamzor</b> hain.<br>
<span style="color:#5b6475">Aur ubalne ka taalluq <b>intermolecular</b> se hai, kyunke ubalte waqt molecules ek
doosre se alag hote hain, tootte nahin.</span></div>
<div class="box def"><span class="t"><span class="emoji">\U0001F4D6</span> Do qism ki intermolecular forces</span>
<b>1. Dipole dipole forces:</b> polar molecules mein ek sira halka musbat aur doosra halka manfi hota hai. Ek
molecule ka musbat sira doosre ke manfi sire ko <b>kheenchta</b> hai.<br>
<b>2. Hydrogen bonding:</b> ye dipole dipole ki <b>sab se mazboot</b> shakal hai. Ye tab banti hai jab hydrogen
<b>N, O ya F</b> ke saath jura ho.</div>
<div class="box warn"><span class="t"><span class="emoji">⚠️</span> Teen harf jo yaad rakhne hain: N, O, F</span>
Hydrogen bonding sirf in <b>teen</b> ke saath banti hai. Kyun? Kyunke ye teenon <b>bohat chhote</b> aur
<b>bohat electronegative</b> hain, to wo hydrogen ka electron poori tarah apni taraf kheench lete hain aur
hydrogen taqreeban nanga proton reh jata hai.<br>
<b>Aur yehi oopar wale sawal ka jawab hai:</b> paani mein hydrogen bonding hai, H<sub>2</sub>S mein nahin
(kyunke S in teen mein nahin hai). Isi liye paani ko alag karne ke liye zyada garmi chahiye.</div>
<div class="box quiz"><span class="t"><span class="emoji">\U0001F9EA</span> Quiz</span>
<ol class="q">
<li>Explain the difference between <b>intramolecular</b> and <b>intermolecular</b> forces, and say which of them
decides a substance's boiling point.</li>
<li>Name the two intermolecular forces your book gives. For <b>hydrogen bonding</b>, name the three elements
hydrogen must be bonded to, and use it to explain why water boils at a much higher temperature than
H<sub>2</sub>S.</li>
</ol></div>
<!--KEY 1. Intramolecular forces act inside a molecule, between its atoms, and are the ionic and covalent bonds;
they are strong. Intermolecular forces act between separate molecules and are weak. Boiling point depends on the
intermolecular forces, because boiling separates molecules from each other rather than breaking them apart.
2. Dipole-dipole forces and hydrogen bonding. Hydrogen bonding needs hydrogen bonded to nitrogen, oxygen or
fluorine. Water has hydrogen bonding because H is bonded to O; H2S does not, because sulphur is not one of the
three. The extra energy needed to break those hydrogen bonds is why water boils far higher despite being
lighter. -->
""",
  """السلام علیکم سیماب۔ آج کا سبق ایک عجیب سوال سے شروع ہوتا ہے، اور اس کا جواب بہت خوبصورت ہے۔

پانی سو ڈگری پر ابلتا ہے۔ یہ آپ جانتی ہیں۔

اب H دو S لیں، یعنی hydrogen sulphide۔ یہ پانی سے بھاری ہے، کیونکہ sulphur، oxygen سے بھاری ہے۔ عام اصول یہ ہے کہ بھاری چیز دیر سے ابلتی ہے۔

مگر H دو S منفی ساٹھ ڈگری پر ہی گیس بن جاتی ہے۔ یعنی کمرے کے درجہ حرارت پر بھی وہ گیس ہے۔

تو بھاری چیز پہلے ابل گئی اور ہلکی بعد میں؟ یہ الٹا کیوں ہے؟ جواب آخر میں۔

پہلے ایک فرق جو سب کچھ کھول دیتا ہے۔

Intramolecular force وہ ہے جو molecule کے اندر کام کرتی ہے، یعنی atoms کے درمیان۔ یہی ionic اور covalent bond ہیں۔ اور یہ بہت مضبوط ہیں۔

اور intermolecular force وہ ہے جو molecule کے باہر کام کرتی ہے، یعنی ایک پورے molecule اور دوسرے پورے molecule کے درمیان۔ اور یہ کمزور ہے۔

اب غور کریں۔ جب پانی ابلتا ہے تو کیا ہوتا ہے؟ کیا H اور O الگ ہو جاتے ہیں؟ نہیں۔ بھاپ بھی H دو O ہی ہے۔

ابلنے میں صرف یہ ہوتا ہے کہ ایک molecule دوسرے سے الگ ہو جاتا ہے۔

تو ابلنے کا تعلق intramolecular سے نہیں، intermolecular سے ہے۔ یہ بات بہت اہم ہے۔

اب کتاب دو قسم کی intermolecular forces بتاتی ہے۔

پہلی، dipole dipole forces۔ یاد ہے کل polar molecules؟ ان میں ایک سرا ہلکا مثبت ہوتا ہے اور دوسرا ہلکا منفی۔ تو ایک molecule کا مثبت سرا دوسرے کے منفی سرے کو کھینچتا ہے۔ بالکل مقناطیس کی طرح۔

اور دوسری، hydrogen bonding۔ یہ dipole dipole کی سب سے مضبوط شکل ہے۔

اور اب سب سے ضروری بات۔ Hydrogen bonding ہر جگہ نہیں بنتی۔ یہ صرف اس وقت بنتی ہے جب hydrogen تین میں سے کسی ایک کے ساتھ جڑا ہو: N، O، یا F۔

یہ تین حرف یاد کر لیں۔ N، O، F۔ نائٹروجن، آکسیجن، فلورین۔

کیوں صرف یہ تین؟ کیونکہ یہ تینوں بہت چھوٹے اور بہت electronegative ہیں۔ وہ hydrogen کا electron اتنی زور سے اپنی طرف کھینچ لیتے ہیں کہ hydrogen تقریباً ننگا proton رہ جاتا ہے۔ اور وہی ننگا proton دوسرے molecule کو زور سے کھینچتا ہے۔

اور اب اوپر والے سوال کا جواب۔

پانی میں hydrogen، oxygen کے ساتھ جڑا ہے۔ O تین میں سے ایک ہے۔ تو پانی میں hydrogen bonding ہے، اور وہ مضبوط ہے۔

مگر H دو S میں hydrogen، sulphur کے ساتھ جڑا ہے۔ اور sulphur ان تین میں نہیں ہے۔ تو اس میں hydrogen bonding نہیں بنتی۔

اسی لیے پانی کے molecules ایک دوسرے کو زور سے پکڑے ہوئے ہیں، اور انہیں الگ کرنے کے لیے بہت زیادہ گرمی چاہیے۔ اور H دو S کے molecules ڈھیلے ہیں، تو وہ ذرا سی گرمی میں بکھر جاتے ہیں۔

بھاری ہونا کوئی معنی نہیں رکھتا۔ پکڑ کتنی مضبوط ہے، یہ معنی رکھتا ہے۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
"""),

L("5.5", "chem-ch05-structure-and-properties",
  "How bonding decides properties: melting points, conduction in ionic compounds, and why graphite conducts while diamond does not.",
  """
<h1><span class="emoji">\U0001F48E</span> Chemistry Ch 5.5: Bonding, Structure and Properties</h1>
<div class="sub">Chapter 5 &middot; sections 5.5.1 se 5.5.3 &middot; kitab ke page 73 se 94</div>
<h2><span class="emoji">\U0001F4CB</span> Ionic aur Covalent compounds ka muqabla</h2>
<table>
<tr><th style="width:34%">Khasoosiyat</th><th style="width:33%">Ionic</th><th style="width:33%">Covalent</th></tr>
<tr><td>Melting / boiling point</td><td><b>Ooncha</b></td><td><b>Neecha</b></td></tr>
<tr><td>Halat (kamre ke temp par)</td><td>Aam tor par <b>thos</b></td><td>Aksar maaye ya gas</td></tr>
<tr><td>Bijli chalana</td><td><b>Pighli ya ghuli</b> halat mein haan</td><td>Aam tor par <b>nahin</b></td></tr>
<tr><td>Paani mein ghulna</td><td>Aam tor par ghul jate hain</td><td>Aksar nahin</td></tr>
</table>
<div class="box trick"><span class="t"><span class="emoji">\U0001F9E0</span> Ionic compound thos halat mein bijli kyun nahin chalata</span>
Bijli chalane ke liye charge ka <b>chalna</b> zaroori hai.<br>
<b>Thos halat mein</b> ions apni jagah par <b>jakre</b> hue hain, hil nahin sakte. To bijli nahin chalti.<br>
<b>Pighla dein ya paani mein ghol dein</b> to ions <b>azad</b> ho jate hain aur chal sakte hain. Ab bijli chalti hai.<br>
Yani ions wohi hain, bas <b>harkat</b> ka farq hai. Ye sawal har saal aata hai.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> 5.5.1 Graphite aur 5.5.2 Diamond</span>
Dono <b>khalis carbon</b> hain, magar banawat alag hai (ye aap Chapter 2 mein parh chuki hain).<br>
<b>Graphite:</b> tehon mein, har carbon <b>teen</b> se jura, chautha electron <b>azad</b>. Is liye <b>naram</b>
aur <b>bijli chalata</b> hai.<br>
<b>Uses:</b> lubricant, electrode, pencil.<br>
<b>Diamond:</b> har carbon <b>chaar</b> se jura, koi azad electron nahin. Is liye <b>sab se sakht</b> aur bijli
<b>nahin</b> chalata.<br>
<b>Uses:</b> kaatne ke auzaar, zewar.</div>
<div class="box warn"><span class="t"><span class="emoji">⚠️</span> Tezab bhi bijli chalate hain</span>
Kitab khaas taur par likhti hai ke tezab paani mein <b>ions</b> dete hain, aur isi liye un ka mahlool bijli
chalata hai. Wajah wohi hai: azad ions.</div>
<div class="box quiz"><span class="t"><span class="emoji">\U0001F9EA</span> Quiz</span>
<ol class="q">
<li>Compare ionic and covalent compounds for melting point, state at room temperature, conduction of electricity
and solubility in water.</li>
<li>Explain why an ionic compound does <b>not</b> conduct electricity when solid but <b>does</b> when molten or
dissolved. Then give two uses each for graphite and diamond, with the reason behind each use.</li>
</ol></div>
<!--KEY 1. Ionic: high melting and boiling points, usually solid at room temperature, conduct when molten or
dissolved, usually soluble in water. Covalent: low melting and boiling points, often liquid or gas, generally do
not conduct, often insoluble.
2. Conduction needs charges that can move. In the solid the ions are locked in place in the lattice, so nothing
moves and no current flows. Melting or dissolving frees the ions to move, so the current flows. The ions are the
same; only their freedom to move changes. Graphite: lubricant and pencils (layers slide), electrodes (free fourth
electron conducts). Diamond: cutting tools and jewellery (hardest substance, from its rigid four-bond network). -->
""",
  """السلام علیکم سیماب۔ آج دیکھیں گے کہ bond کی قسم سے چیز کی خصوصیات کیسے طے ہوتی ہیں۔ پہلے ایک سوال۔

نمک لیں۔ خشک نمک کو بجلی کے دو تاروں کے بیچ رکھیں، bulb نہیں جلے گا۔ بالکل نہیں۔

اب اسی نمک کو پانی میں گھول دیں، اور وہی تار اس پانی میں ڈالیں۔ bulb جل اٹھے گا۔

نمک وہی ہے۔ ions وہی ہیں۔ تو فرق کیا پڑا؟ جواب تھوڑی دیر میں۔

پہلے ionic اور covalent compounds کا مقابلہ، چار باتوں میں۔

پہلی، melting point۔ Ionic کا اونچا، covalent کا نیچا۔ اسی لیے نمک ٹھوس ہے اور کمرے میں پڑا رہتا ہے، جبکہ بہت سے covalent مادے مائع یا گیس ہوتے ہیں۔

دوسری، حالت۔ Ionic عام طور پر ٹھوس، covalent اکثر مائع یا گیس۔

تیسری، بجلی چلانا۔ یہی آج کا اصل سوال ہے۔

اور چوتھی، پانی میں گھلنا۔ Ionic عام طور پر گھل جاتے ہیں، covalent اکثر نہیں۔

اب اوپر والے سوال کا جواب۔

بجلی چلنے کے لیے کیا چاہیے؟ charge کا چلنا۔ کوئی ایسی چیز جو حرکت کر سکے اور charge لے جا سکے۔

اب ٹھوس نمک میں ions موجود ہیں، سوڈیم مثبت اور کلورائیڈ منفی۔ لیکن وہ جالی میں اپنی جگہ جکڑے ہوئے ہیں۔ ہل ہی نہیں سکتے۔

اور جو ہل نہ سکے وہ charge لے کر کہیں نہیں جا سکتا۔ اسی لیے bulb نہیں جلتا۔

اب نمک کو پانی میں گھولیں۔ جالی ٹوٹ جاتی ہے اور ions آزاد ہو جاتے ہیں۔ اب وہ تیر سکتے ہیں، حرکت کر سکتے ہیں۔ اور حرکت کرتے ہی وہ charge لے جانے لگتے ہیں۔

تو bulb جل اٹھتا ہے۔

یاد رکھیں: ions وہی ہیں، صرف حرکت کا فرق ہے۔ اور یہی سوال ہر سال امتحان میں آتا ہے۔

اور یہی بات پگھلانے پر بھی لاگو ہے۔ نمک کو پگھلا دیں تو بھی ions آزاد ہو جاتے ہیں اور بجلی چلتی ہے۔

اب دو مثالیں جو آپ باب دو میں پڑھ چکی ہیں، مگر اب وجہ سمجھ آئے گی۔

Graphite اور diamond، دونوں خالص carbon۔

Graphite میں ہر carbon تین دوسرے carbon سے جڑا ہے۔ تو چوتھا electron آزاد رہ جاتا ہے۔ اور آزاد electron کا مطلب ہے بجلی چل سکتی ہے۔ اور تہیں پھسلتی ہیں، تو وہ نرم بھی ہے۔

اسی لیے graphite کے استعمال: lubricant، electrode، اور پنسل۔

Diamond میں ہر carbon چار سے جڑا ہے۔ کوئی electron آزاد نہیں بچتا۔ تو بجلی نہیں چلتی۔ اور پوری جالی سخت ہے، تو وہ سب سے سخت مادہ ہے۔

اسی لیے diamond کے استعمال: کاٹنے کے اوزار، اور زیور۔

اور آخر میں ایک بات جو کتاب خاص طور پر لکھتی ہے: تیزاب بھی بجلی چلاتے ہیں۔ وجہ وہی ہے، کیونکہ وہ پانی میں ions دیتے ہیں۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
"""),

L("5.6", "chem-ch05-metallic-bonds",
  "The sea of delocalised electrons, and how one picture explains why metals conduct, bend and shine.",
  """
<h1><span class="emoji">\U0001F529</span> Chemistry Ch 5.6: Metallic Bonds</h1>
<div class="sub">Chapter 5 &middot; sections 5.6 aur 5.6.1 &middot; kitab ke page 73 se 94</div>
<div class="box def"><span class="t"><span class="emoji">\U0001F4D6</span> Electron sea model</span>
Dhat ke atoms apne bairooni electrons <b>chhor</b> dete hain. Ye electrons kisi <b>ek</b> atom ke nahin rehte,
balke poore maddey mein <b>azadana ghoomte</b> hain.<br>
In ko <b>delocalised electrons</b> kehte hain, aur is tasveer ko <b>sea of electrons</b> kaha jata hai.<br>
To dhat kya hai? <b>Musbat ions ki jaali, jo electron ke samundar mein doobi hui hai.</b> Aur yehi kheench
metallic bond hai.</div>
<div class="box trick"><span class="t"><span class="emoji">\U0001F9E0</span> Ek tasveer, chaar khasoosiyat</span>
<b>Bijli chalati hai:</b> azad electrons charge le jate hain.<br>
<b>Garmi chalati hai:</b> wohi electrons garmi bhi le jate hain.<br>
<b>Malleable (peet kar chaadar):</b> peetne par atoms ki tehen <b>phisal</b> jati hain, magar electron ka samundar
unhein jore rakhta hai, is liye dhat <b>tootti nahin, phailti</b> hai.<br>
<b>Ductile (taar):</b> wohi wajah.<br>
<b>Chamak:</b> azad electrons roshni ko wapas <b>parchhati</b> hain.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> 5.6.1 Sanaat mein ye khasoosiyat kyun ahem hain</span>
<b>Taanba (copper):</b> bijli ki taar, kyunke wo sab se acha conductor aur ductile hai.<br>
<b>Aluminium:</b> bartan aur foil, kyunke wo halka aur malleable hai.<br>
<b>Loha aur steel:</b> imaraton ka dhancha, kyunke wo mazboot hai.<br>
<span style="color:#5b6475">Yani har istemal ke peechhe ek khasoosiyat hai, aur har khasoosiyat ke peechhe wohi
ek tasveer: electron ka samundar.</span></div>
<div class="box quiz"><span class="t"><span class="emoji">\U0001F9EA</span> Quiz</span>
<ol class="q">
<li>Describe the <b>electron sea model</b> of metallic bonding, and define a <b>delocalised</b> electron.</li>
<li>Using that model, explain why metals <b>conduct electricity</b> and why they are <b>malleable</b>. Then give
one industrial use each for copper, aluminium and iron, with the property behind it.</li>
</ol></div>
<!--KEY 1. In a metal the atoms release their outermost electrons, which no longer belong to any one atom but
move freely throughout the whole structure. These are delocalised electrons, and the picture is called the sea of
electrons: a lattice of positive metal ions immersed in that sea, with the attraction between them being the
metallic bond.
2. Conduction: the free electrons carry charge through the metal. Malleability: when hammered, layers of ions
slide over one another while the electron sea keeps them bonded, so the metal flattens rather than shattering.
Copper for electrical wiring (best conductor, ductile); aluminium for foil and utensils (light, malleable); iron
and steel for building frames (strength). -->
""",
  """السلام علیکم سیماب۔ آج باب پانچ کا آخری سبق ہے: metallic bonds۔ اور آج ایک ہی تصویر ذہن میں بٹھانی ہے، جس سے دھاتوں کی ساری خصوصیات نکل آتی ہیں۔ پہلے ایک سوال۔

دھاتیں بجلی چلاتی ہیں۔ گرمی چلاتی ہیں۔ پیٹو تو پھیل جاتی ہیں، ٹوٹتی نہیں۔ تار بن جاتی ہیں۔ اور چمکتی بھی ہیں۔

پانچ الگ الگ خصوصیات۔ کیا ان کی پانچ الگ وجہیں ہیں؟

نہیں۔ ایک ہی وجہ ہے۔ اور وہ یہ ہے۔

دھات کے atoms اپنے بیرونی electrons چھوڑ دیتے ہیں۔ اور یہ چھوڑے ہوئے electrons کسی ایک atom کے نہیں رہتے۔ وہ پورے مادے میں آزادانہ گھومتے رہتے ہیں۔

ان کو delocalised electrons کہتے ہیں۔ Delocalised کا مطلب ہی یہ ہے کہ ان کی کوئی مقررہ جگہ نہیں۔

اور اس پوری تصویر کو sea of electrons کہتے ہیں، یعنی electrons کا سمندر۔

تو دھات ہے کیا؟ مثبت ions کی ایک جالی، جو electrons کے سمندر میں ڈوبی ہوئی ہے۔ اور انہی دونوں کے درمیان کی کھینچ metallic bond ہے۔

اب اس ایک تصویر سے پانچوں خصوصیات نکالتے ہیں۔

پہلی، بجلی۔ بجلی چلنے کے لیے آزاد charge چاہیے۔ اور یہاں پورا سمندر ہی آزاد ہے۔ تو بجلی آسانی سے چلتی ہے۔

دوسری، گرمی۔ وہی آزاد electrons گرمی بھی لے جاتے ہیں۔ اسی لیے چمچ کا ایک سرا گرم کریں تو دوسرا بھی گرم ہو جاتا ہے۔

تیسری، malleability، یعنی پیٹ کر چادر بنانا۔ یہ سب سے دلچسپ ہے۔

جب آپ دھات پر ہتھوڑا مارتی ہیں تو atoms کی تہیں ایک دوسری پر پھسل جاتی ہیں۔ اب عام طور پر جب ذرے اپنی جگہ سے ہٹیں تو چیز ٹوٹ جاتی ہے۔

مگر یہاں نہیں ٹوٹتی۔ کیوں؟ کیونکہ electron کا سمندر ہر جگہ موجود ہے۔ تہیں جہاں بھی جائیں، سمندر انہیں جوڑے رکھتا ہے۔

تو دھات ٹوٹتی نہیں، پھیل جاتی ہے۔

چوتھی، ductility یعنی تار بننا۔ وجہ بالکل وہی ہے۔

اور پانچویں، چمک۔ آزاد electrons روشنی کو واپس پرچھاتے ہیں، اسی لیے دھات چمکتی ہے۔

دیکھا؟ پانچ خصوصیات، ایک ہی وجہ۔

اور آخر میں صنعت میں ان کا استعمال۔

تانبا بجلی کی تار کے لیے، کیونکہ وہ سب سے اچھا conductor ہے اور تار بن جاتا ہے۔

Aluminium برتن اور foil کے لیے، کیونکہ وہ ہلکا ہے اور پیٹا جا سکتا ہے۔

اور لوہا اور steel عمارتوں کے ڈھانچے کے لیے، کیونکہ وہ مضبوط ہے۔

ہر استعمال کے پیچھے ایک خصوصیت، اور ہر خصوصیت کے پیچھے وہی ایک تصویر: electron کا سمندر۔

اس کے ساتھ باب پانچ مکمل ہو گیا۔ آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
"""),
]

if __name__ == "__main__":
    build(LESSONS, C)
