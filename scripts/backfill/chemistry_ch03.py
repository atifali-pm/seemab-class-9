# -*- coding: utf-8 -*-
"""Chemistry Chapter 3: Atomic Structure. Her book p27 to 44."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import build
C = "#1e7a4a"; S = "chemistry"

LESSONS = [
{
 "subject": S, "chapter": 3, "ref": "3.1", "slug": "chem-ch03-atomic-models",
 "summary": "Dalton, Rutherford's gold foil experiment, why his model failed, Bohr's five postulates, and the quantum mechanical model.",
 "note": """
<h1><span class="emoji">⚛️</span> Chemistry Ch 3.1: Atomic Models</h1>
<div class="sub">Chapter 3, Atomic Structure · kitab ke page 27 se 44</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Dalton (1803), chaar postulates</span>
1. Atom <b>na toray ja sakne wala</b> hai. 2. Ek hi element ke atoms <b>bilkul ek jaise</b> hain.
3. Atoms <b>sadah tanasub</b> mein jurte hain. 4. Atoms <b>na banaye ja sakte hain na khatam kiye</b>.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Rutherford ka gold foil experiment</span>
<b>Polonium</b> se nikalne wale <b>alpha particles</b> ko <b>0.00004 cm</b> moti sone ki warq par maara.<br>
<b>Teen nataij:</b> atom ka zyadatar hissa <b>khaali</b> hai; nucleus <b>chhota, kasif aur positive</b> hai;
electrons nucleus ke gird ghoomte hain.</div>
<div class="box warn"><span class="t"><span class="emoji">⚠️</span> Rutherford ka model nakaam kyun hua</span>
Ghoomta hua electron <b>accelerating charge</b> hai, aur usay <b>musalsal energy</b> chhorni chahiye thi. Phir wo
<b>continuous spectrum</b> deta, jo kabhi dekha hi nahin gaya. Ye defect yaad rakhein, sawal banta hai.</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Bohr (1913), paanch postulates</span>
1. Electrons <b>daairawi orbits</b> mein ghoomte hain. 2. Energy nucleus se <b>faasle ke mutanasib</b>.
3. Angular momentum <b>quantized</b> hai (<b>h/2&pi;</b>). 4. Orbit badalte waqt roshni <b>jazb ya kharij</b>.
5. <b>&Delta;E = E<sub>2</sub> &minus; E<sub>1</sub></b>.</div>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Quantum Mechanical Model, aur teen naam</span>
Ab <b>orbit</b> nahin, <b>orbital</b> hai: wo ilaqa jahan electron <b>milne ka imkaan</b> sab se zyada ho.<br>
<b>de Broglie (1924):</b> electron ki <b>dohri fitrat</b>, lehar bhi aur zarra bhi.<br>
<b>Heisenberg (1927):</b> electron ki <b>jagah aur momentum</b> dono ek saath theek maloom nahin ho sakte.<br>
<b>Davisson aur Germer (1927):</b> tajurbe se electron ki <b>lehar</b> wali fitrat sabit ki.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Describe Rutherford's gold foil experiment and the three conclusions he drew. Then state the defect that made
his planetary model fail.</li>
<li>Write Bohr's five postulates, and name the three scientists behind the quantum mechanical model with what
each contributed.</li>
</ol></div>
<!--KEY 1. Alpha particles from polonium fired at gold foil 0.00004 cm thick. Conclusions: most of the atom is
empty space; the nucleus is small, dense and positive; electrons orbit the nucleus. Defect: an orbiting electron
is an accelerating charge, so it should radiate energy continuously and give a continuous spectrum, which is not
observed. 2. The five postulates as listed. de Broglie: dual nature of electrons. Heisenberg: position and
momentum cannot both be known exactly. Davisson and Germer: experimentally confirmed the wave nature. -->
""",
 "script": """السلام علیکم سیماب۔ آج Chemistry کے باب تین کی دہرائی ہے، atomic models۔ لیکن پہلے ایک سوال۔

Rutherford نے سونے کی ایک بہت باریک ورق پر alpha particles ماریں۔ زیادہ تر سیدھی گزر گئیں، مگر کچھ واپس پلٹ آئیں۔ Rutherford نے کہا کہ یہ ایسا ہی ہے جیسے آپ ٹشو پیپر پر توپ کا گولہ ماریں اور وہ واپس آپ پر آ گرے۔

اس ایک تجربے نے atom کی پوری تصویر بدل دی۔ کیسے؟ آئیے ترتیب سے دیکھتے ہیں۔

سب سے پہلے Dalton، اٹھارہ سو تین میں۔ اس کے چار postulates تھے۔ ایک، atom توڑا نہیں جا سکتا۔ دو، ایک ہی element کے atoms بالکل ایک جیسے ہوتے ہیں۔ تین، atoms سادہ تناسب میں جڑتے ہیں۔ اور چار، atoms نہ بنائے جا سکتے ہیں نہ ختم کیے جا سکتے ہیں۔

پھر Rutherford آیا۔ اس نے polonium سے نکلنے والی alpha particles کو سونے کی ورق پر مارا، جو صرف صفر اعشاریہ صفر صفر صفر صفر چار سینٹی میٹر موٹی تھی۔

اور تین نتیجے نکالے۔ پہلا، atom کا زیادہ تر حصہ خالی ہے، اسی لیے زیادہ تر particles سیدھی گزر گئیں۔ دوسرا، بیچ میں ایک چھوٹا، کثیف اور مثبت nucleus ہے، اسی سے ٹکرا کر کچھ واپس آئیں۔ اور تیسرا، electrons اس nucleus کے گرد گھومتے ہیں۔

لیکن یہیں ایک مسئلہ کھڑا ہو گیا، اور یہ امتحان میں پوچھا جاتا ہے۔

Rutherford کا model کہتا تھا کہ electron nucleus کے گرد گھومتا ہے۔ مگر physics کا قانون کہتا ہے کہ گھومتا ہوا charge مسلسل energy خارج کرتا ہے۔ تو electron کو energy کھوتے کھوتے nucleus میں گر جانا چاہیے تھا۔ اور اس سے continuous spectrum بننا چاہیے تھا۔ مگر ایسا کبھی دیکھا ہی نہیں گیا۔

تو Bohr آیا، انیس سو تیرہ میں، اور پانچ postulates دیے۔

ایک، electrons دائروی orbits میں گھومتے ہیں۔ دو، ان کی energy nucleus سے فاصلے کے متناسب ہے۔ تین، angular momentum quantized ہے، یعنی h تقسیم دو pi۔ چار، orbit بدلتے وقت روشنی جذب یا خارج ہوتی ہے۔ اور پانچ، delta E برابر ہے E دو منفی E ایک۔

اور آخر میں quantum mechanical model۔ اس میں سب سے بڑی تبدیلی یہ ہے کہ اب orbit نہیں رہا، orbital آ گیا۔

فرق سمجھیں۔ Orbit ایک مقررہ راستہ ہے، جیسے ریل کی پٹری۔ اور orbital وہ علاقہ ہے جہاں electron ملنے کا امکان سب سے زیادہ ہو۔ یعنی اب ہم یہ نہیں کہتے کہ electron کہاں ہے، صرف یہ کہتے ہیں کہ کہاں ہونے کا امکان ہے۔

اور اس کے پیچھے تین نام ہیں۔ de Broglie، انیس سو چوبیس، جس نے کہا electron لہر بھی ہے اور ذرہ بھی۔ Heisenberg، انیس سو ستائیس، جس نے کہا electron کی جگہ اور momentum دونوں ایک ساتھ ٹھیک معلوم نہیں ہو سکتے۔ اور Davisson اور Germer، اسی سال، جنہوں نے تجربے سے electron کی لہر والی فطرت ثابت کر دی۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
{
 "subject": S, "chapter": 3, "ref": "3.2", "slug": "chem-ch03-subatomic-particles",
 "summary": "Proton, neutron and electron: their charges and masses, why an atom is neutral, and how each bends in an electric field.",
 "note": """
<h1><span class="emoji">🔴</span> Chemistry Ch 3.2: Subatomic Particles</h1>
<div class="sub">Chapter 3, Atomic Structure · kitab ke page 27 se 44</div>
<table>
<tr><th style="width:26%">Particle</th><th style="width:20%">Charge</th><th style="width:54%">Mass</th></tr>
<tr><td><b>Proton</b></td><td><b>+1</b></td><td>~1 amu (1.6726 &times; 10<sup>-27</sup> kg)</td></tr>
<tr><td><b>Neutron</b></td><td><b>0</b></td><td>~1 amu (1.6749 &times; 10<sup>-27</sup> kg)</td></tr>
<tr><td><b>Electron</b></td><td><b>-1</b></td><td>~<b>1/1836</b> amu (9.11 &times; 10<sup>-31</sup> kg)</td></tr>
</table>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Mass ka asal nuqta</span>
Proton aur neutron ka mass taqreeban <b>barabar</b> hai. Lekin electron ka mass sirf <b>1/1836</b> hissa hai.<br>
Isi liye atom ka <b>poora mass nucleus</b> mein hai. Electrons ka mass ginti mein hi nahin aata.</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Nucleus aur nuclear force</span>
Nucleus mein <b>protons aur neutrons</b> hote hain, aur dono ko mila kar <b>nucleons</b> kehte hain.<br>
Ab sawal: saaray protons positive hain, to ek doosre ko dhakelna chahiye. Phir nucleus tootta kyun nahin?<br>
Jawab: <b>nuclear force</b> (strong force), jo protons aur neutrons ko aapas mein jakar rakhti hai.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Electric field mein teenon ka raweyya</span>
<b>Protons</b> <b>negative</b> plate ki taraf murte hain (kyunke wo positive hain).<br>
<b>Electrons</b> <b>positive</b> plate ki taraf murte hain.<br>
<b>Neutrons</b> <b>bilkul seedhe</b> chale jate hain, kyunke un par charge hai hi nahin.<br>
Aur ek baat: neutral atom mein <b>protons ki tadaad = electrons ki tadaad</b>, isi liye atom par koi charge nahin.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Make a table of the three subatomic particles with their charge and mass. Then explain why almost all the mass
of an atom is in the nucleus.</li>
<li>How does each of the three behave in an electric field, and why? What holds the nucleus together despite the
protons repelling each other?</li>
</ol></div>
<!--KEY 1. Proton +1, ~1 amu; neutron 0, ~1 amu; electron -1, ~1/1836 amu. The proton and neutron each weigh about
1 amu while the electron is only 1/1836 of that, so the nucleus carries essentially all the mass.
2. Protons deflect toward the negative plate, electrons toward the positive plate, neutrons travel straight
because they carry no charge. The nuclear force (strong force) binds protons and neutrons together. -->
""",
 "script": """السلام علیکم سیماب۔ آج کا موضوع ہے subatomic particles، یعنی atom کے اندر کے تین ذرے۔ لیکن پہلے ایک سوال۔

nucleus کے اندر سارے protons مثبت ہیں۔ اور آپ جانتی ہیں کہ دو مثبت چیزیں ایک دوسری کو دھکیلتی ہیں۔ تو پھر nucleus پھٹ کیوں نہیں جاتا؟ جواب آخر میں۔

پہلے تینوں ذرے۔

Proton کا charge مثبت ایک ہے، اور mass تقریباً ایک amu۔

Neutron کا charge صفر ہے، اور mass بھی تقریباً ایک amu۔

اور electron کا charge منفی ایک ہے، مگر mass صرف ایک بٹا اٹھارہ سو چھتیس amu۔

اب اس آخری نمبر پر ذرا رکیے۔ ایک بٹا اٹھارہ سو چھتیس۔ یعنی electron اتنا ہلکا ہے کہ اگر proton ایک کلو کا ہو تو electron آدھے گرام سے بھی کم ہو گا۔

اور اسی سے ایک بہت اہم نتیجہ نکلتا ہے: atom کا سارا mass nucleus میں ہے۔ electrons کا وزن گنتی میں ہی نہیں آتا۔ یہ بات امتحان میں پوچھی جاتی ہے۔

اب nucleus کی ساخت۔ اس میں protons اور neutrons ہوتے ہیں، اور دونوں کو ملا کر nucleons کہتے ہیں۔ یہ لفظ یاد رکھیں۔

اور اب اوپر والے سوال کا جواب۔ nucleus اس لیے نہیں پھٹتا کیونکہ اس میں ایک اور طاقت کام کر رہی ہے: nuclear force، جسے strong force بھی کہتے ہیں۔ یہ protons اور neutrons کو جکڑ کر رکھتی ہے، اور یہ اتنی مضبوط ہے کہ مثبت ذروں کی باہمی دھکیل پر غالب آ جاتی ہے۔

اب آخری بات، اور یہ سوال اکثر آتا ہے۔ اگر ان تینوں کو electric field میں سے گزارا جائے تو کیا ہو گا؟

Protons منفی plate کی طرف مڑیں گے، کیونکہ وہ خود مثبت ہیں اور مخالف چیزیں کھنچتی ہیں۔

Electrons مثبت plate کی طرف مڑیں گے، اسی اصول سے۔

اور neutrons بالکل سیدھے چلے جائیں گے، کیونکہ ان پر charge ہے ہی نہیں، تو انہیں کوئی کھینچ ہی نہیں سکتا۔

اور ایک آخری نکتہ۔ ایک neutral atom میں protons کی تعداد electrons کی تعداد کے برابر ہوتی ہے۔ اسی لیے پورا atom غیر جانبدار رہتا ہے۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
{
 "subject": S, "chapter": 3, "ref": "3.3", "slug": "chem-ch03-atomic-number",
 "summary": "Atomic number Z and mass number A, how to find the neutrons, and what radioactive decay does.",
 "note": """
<h1><span class="emoji">🔢</span> Chemistry Ch 3.3: Atomic Number and Mass Number</h1>
<div class="sub">Chapter 3, Atomic Structure · kitab ke page 27 se 44</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Do number, aur un ka farq</span>
<b>Atomic number (Z)</b> = nucleus mein <b>protons</b> ki tadaad.<br>
Ye har element ke liye <b>mukhtalif</b> hai, aur yehi element ki <b>shanakht</b> aur periodic table mein us ki
<b>jagah</b> tay karta hai.<br>
<b>Mass number / Nucleon number (A)</b> = <b>protons + neutrons</b>.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Neutrons nikalne ka formula</span>
<b>Neutrons = A &minus; Z</b><br>
Misal: sodium ka A = 23 aur Z = 11. To neutrons = 23 &minus; 11 = <b>12</b>.<br>
Aur neutral atom mein electrons = protons = Z = <b>11</b>.</div>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Kaunsa number element badalta hai</span>
Agar <b>protons</b> badal jayein to <b>element hi badal jata hai</b>. Agar sirf <b>neutrons</b> badlein to element
wohi rehta hai, bas us ka <b>isotope</b> ban jata hai. Yehi agle safhay ka moazoo hai.</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Radioactivity</span>
Jo isotopes <b>ghair mustahkam</b> hon wo <b>radioactive decay</b> se guzarte hain, yani toot kar doosra element
ban jate hain.<br>
Kitab ki do misalein: <b>C-14 &rarr; N-14</b> aur <b>U-238 &rarr; Pb-206</b>.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Define <b>atomic number</b> and <b>mass number</b>. An atom has A = 35 and Z = 17: how many protons, neutrons
and electrons does it have?</li>
<li>What is <b>radioactive decay</b>? Give the two examples your book provides.</li>
</ol></div>
<!--KEY 1. Atomic number Z is the number of protons in the nucleus and identifies the element. Mass number A is
protons plus neutrons. For A=35, Z=17: 17 protons, 35-17=18 neutrons, and 17 electrons in a neutral atom.
2. Unstable isotopes break down into another element. C-14 decays to N-14; U-238 decays to Pb-206. -->
""",
 "script": """السلام علیکم سیماب۔ آج کا سبق چھوٹا ہے مگر اس کے بغیر اگلا سبق سمجھ نہیں آئے گا۔ موضوع ہے atomic number اور mass number۔

پہلے ایک سوال۔ کاربن اور nitrogen میں فرق کیا ہے؟ دونوں atoms ہیں، دونوں میں protons، neutrons اور electrons ہیں۔ تو ان کو الگ کیا بناتا ہے؟

جواب صرف ایک نمبر ہے۔ آئیے دیکھتے ہیں۔

Atomic number، جسے Z لکھتے ہیں، nucleus میں protons کی تعداد ہے۔ اور یہ ہر element کے لیے مختلف ہے۔ یہی element کی شناخت ہے، اور یہی periodic table میں اس کی جگہ طے کرتا ہے۔

تو اوپر والے سوال کا جواب مل گیا۔ کاربن کے چھ protons ہیں، nitrogen کے سات۔ بس یہی فرق ہے۔ ایک proton کم یا زیادہ، اور element ہی بدل گیا۔

اب دوسرا نمبر۔ Mass number، جسے A لکھتے ہیں، protons اور neutrons کو ملا کر بنتا ہے۔ اسے nucleon number بھی کہتے ہیں، کیونکہ nucleons کا مطلب ہی protons جمع neutrons ہے۔

اور اب ایک formula جو ہر سوال میں کام آتا ہے۔ Neutrons برابر ہیں A منفی Z۔

ایک مثال لیتے ہیں۔ Sodium کا A تئیس ہے اور Z گیارہ۔ تو neutrons کتنے ہوئے؟ تئیس منفی گیارہ، یعنی بارہ۔ اور neutral atom میں electrons protons کے برابر ہوتے ہیں، یعنی گیارہ۔

اب ایک بہت ضروری بات، جو اگلے سبق کی بنیاد ہے۔

اگر protons بدل جائیں تو element ہی بدل جاتا ہے۔ لیکن اگر صرف neutrons بدلیں تو element وہی رہتا ہے، بس اس کا isotope بن جاتا ہے۔ یہ بات ذہن میں رکھیں۔

اور آخر میں radioactivity۔ کچھ isotopes غیر مستحکم ہوتے ہیں۔ وہ ٹوٹ کر دوسرا element بن جاتے ہیں، اور اسی کو radioactive decay کہتے ہیں۔

کتاب دو مثالیں دیتی ہے۔ C چودہ ٹوٹ کر N چودہ بن جاتا ہے۔ اور U دو سو اڑتیس ٹوٹ کر Pb دو سو چھ بن جاتا ہے، یعنی سیسہ۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
{
 "subject": S, "chapter": 3, "ref": "3.4", "slug": "chem-ch03-relative-atomic-mass",
 "summary": "Relative atomic mass measured against carbon-12, what 1 amu means, and why the values are not whole numbers.",
 "note": """
<h1><span class="emoji">⚖️</span> Chemistry Ch 3.4: Relative Atomic Mass</h1>
<div class="sub">Chapter 3, Atomic Structure · kitab ke page 27 se 44</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Paimana: Carbon-12</span>
Atom itna chhota hai ke us ka mass gram mein likhna na mumkin hai. Is liye hum use kisi aur se <b>mila kar</b>
naapte hain, aur wo paimana hai <b>C-12</b>, jo <b>1961</b> se standard hai.<br>
<b>1 amu = ek C-12 atom ke mass ka 1/12 hissa.</b><br>
<b>Relative atomic mass</b> yani kisi atom ka mass, C-12 ke 1/12 hisse ke muqable mein.</div>
<h2><span class="emoji">📋</span> Kitab ki table ke numbers</h2>
<table>
<tr><th>H</th><th>N</th><th>O</th><th>Na</th><th>Al</th><th>S</th><th>Cl</th><th>Fe</th></tr>
<tr><td>1.008</td><td>14.0067</td><td>15.9994</td><td>22.9898</td><td>26.9815</td><td>32.06</td><td>35.453</td><td>55.847</td></tr>
</table>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Ye number poore (whole) kyun nahin hain</span>
Chlorine ka 35.453 hai, 35 nahin. Kyun?<br>
Kyunke qudrat mein chlorine do shaklon mein milta hai: <b>Cl-35</b> aur <b>Cl-37</b>. Jo number table mein hai wo
dono ka <b>auzan ke saath aosat (weighted average)</b> hai.<br>
Yani ye number kisi ek atom ka nahin, poori qudrati mixture ka hai. Yehi agle safhay, isotopes, ka raasta hai.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Define <b>relative atomic mass</b> and <b>1 amu</b>. Which atom is the standard, and since which year?</li>
<li>The relative atomic mass of chlorine is 35.453, not a whole number. Explain why.</li>
</ol></div>
<!--KEY 1. Relative atomic mass is the mass of an atom compared with one twelfth of the mass of a carbon-12 atom.
1 amu is the mass of one C-12 atom divided by 12. The standard is carbon-12, used since 1961.
2. Because chlorine occurs naturally as two isotopes, Cl-35 and Cl-37, and the tabulated value is the weighted
average of them according to their natural abundance, not the mass of any single atom. -->
""",
 "script": """السلام علیکم سیماب۔ آج کا سبق ایک سوال سے شروع ہوتا ہے جو بظاہر عجیب لگتا ہے۔

آپ کی کتاب کی table میں chlorine کا relative atomic mass لکھا ہے پینتیس اعشاریہ چار پانچ تین۔ اب سوچیں۔ atom کے اندر protons اور neutrons ہوتے ہیں، اور دونوں پورے ذرے ہیں۔ آپ آدھا proton تو نہیں رکھ سکتیں۔ تو پھر یہ اعشاریہ کہاں سے آیا؟

یہ سوال اچھا ہے، اور اس کا جواب آج کے سبق کی جان ہے۔ پہلے بنیاد۔

Atom اتنا چھوٹا ہے کہ اس کا وزن گرام میں لکھنا ناممکن ہے۔ نمبر اتنا چھوٹا ہو گا کہ اعشاریے کے بعد چھبیس صفر لگانے پڑیں گے۔

تو سائنسدانوں نے ایک آسان راستہ نکالا۔ انہوں نے کہا: چلو ایک atom کو پیمانہ مان لیتے ہیں، اور باقی سب کو اسی سے ملا کر ناپتے ہیں۔

اور وہ پیمانہ ہے carbon بارہ، جو انیس سو اکسٹھ سے standard چلا آ رہا ہے۔

تعریف یہ ہے: ایک amu کا مطلب ہے ایک C بارہ atom کے mass کا بارہواں حصہ۔ اور relative atomic mass کا مطلب ہے کسی atom کا وزن، اسی بارہویں حصے کے مقابلے میں۔

یعنی جب ہم کہتے ہیں oxygen کا سولہ ہے، تو مطلب یہ ہے کہ oxygen کا atom C بارہ کے بارہویں حصے سے سولہ گنا بھاری ہے۔

اب کتاب کی table کے کچھ نمبر۔ Hydrogen ایک اعشاریہ صفر صفر آٹھ۔ Nitrogen چودہ اعشاریہ صفر صفر چھ سات۔ Oxygen پندرہ اعشاریہ نو نو نو چار۔ Sodium بائیس اعشاریہ نو آٹھ نو آٹھ۔ اور iron پچپن اعشاریہ آٹھ چار سات۔

اور اب اوپر والے سوال کا جواب۔

Chlorine قدرت میں ایک شکل میں نہیں ملتا۔ وہ دو شکلوں میں ملتا ہے: Cl پینتیس اور Cl سینتیس۔ دونوں chlorine ہی ہیں، بس neutrons کی تعداد الگ ہے۔

اور جو نمبر table میں لکھا ہے، وہ کسی ایک atom کا نہیں۔ وہ دونوں کا اوزان کے ساتھ اوسط ہے، یعنی weighted average، اس حساب سے کہ قدرت میں کون سی شکل کتنی ہے۔

اسی لیے وہ پورا نمبر نہیں آتا۔ اور یہی بات ہمیں اگلے سبق تک لے جاتی ہے، جس کا نام ہے isotopes۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
{
 "subject": S, "chapter": 3, "ref": "3.5", "slug": "chem-ch03-isotopes",
 "summary": "Isotopes of hydrogen, carbon, chlorine and uranium with their abundances, how to average their masses, and what isotopes are used for in medicine and dating.",
 "note": """
<h1><span class="emoji">👥</span> Chemistry Ch 3.5: Isotopes</h1>
<div class="sub">Chapter 3, Atomic Structure · kitab ke page 27 se 44 · sections 3.5 se 3.5.7</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Isotopes</span>
Aise atoms jin ka <b>atomic number ek</b> ho magar <b>mass number alag</b>, yani <b>neutrons alag</b>.<br>
Lafz Greek se hai: <b>isos</b> = ek jaisa, <b>tope</b> = jagah. Sab se pehle <b>Soddy</b> ne istemal kiya.<br>
Isotopes <b>chemically ek jaise</b> hote hain, farq sirf <b>physical properties</b> ka hai.</div>
<table>
<tr><th style="width:24%">Element</th><th style="width:76%">Us ke isotopes</th></tr>
<tr><td><b>Hydrogen</b></td><td><b>Protium</b> H-1, koi neutron nahin, <b>99.99%</b> &middot; <b>Deuterium</b> H-2,
1 neutron, 0.0015% &middot; <b>Tritium</b> H-3, 2 neutrons, <b>radioactive</b></td></tr>
<tr><td><b>Carbon</b></td><td>C-12 (98.8%) &middot; C-13 (1.1%) &middot; C-14 (0.009%)</td></tr>
<tr><td><b>Chlorine</b></td><td>Cl-35 (<b>75.77%</b>, 17p + 18n) &middot; Cl-37 (<b>24.23%</b>, 17p + 20n)</td></tr>
<tr><td><b>Uranium</b></td><td>U-234 (0.006%) &middot; U-235 (<b>0.72%</b>, reactor aur bomb mein) &middot; U-238 (99.27%)</td></tr>
</table>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Heavy water aur relative atomic mass</span>
<b>Heavy water (D<sub>2</sub>O):</b> melting point <b>3.81&deg;C</b>, boiling point <b>101.2&deg;C</b>,
density <b>1.1044 g/cm<sup>3</sup></b>. Aam paani se teenon zyada hain.<br>
<b>Weighted average:</b> har isotope ka mass &times; us ki fiisad, phir jama, phir 100 se taqseem.
Chlorine: (35 &times; 75.77 + 37 &times; 24.23) &divide; 100 = <b>35.48</b>, jo table ke 35.453 ke bohat qareeb hai.</div>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Isotopes ke istemal, yaad rakhne layak</span>
<b>Tibbi:</b> I-131 <b>thyroid</b>, Na-24 <b>khoon ka bahao</b>, I-123 <b>dimagh ki tasveer</b>, Co-60
<b>cancer ka ilaj</b>.<br>
<b>Tehqeeq:</b> C-14 photosynthesis ka raasta dekhne ke liye, S-35 molecule ki banawat ke liye.<br>
<b>Carbon dating:</b> <b>C-14</b> se carbon wali cheezon ki <b>umar</b> maloom ki jati hai: chattanein, mitti, mummies.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Define <b>isotopes</b>. Name the three isotopes of hydrogen with their neutrons, and give the two isotopes of
chlorine with their percentages.</li>
<li>Calculate the relative atomic mass of chlorine from Cl-35 (75.77%) and Cl-37 (24.23%). Then give <b>four</b>
uses of isotopes, naming the isotope in each case.</li>
</ol></div>
<!--KEY 1. Isotopes are atoms of the same element with the same atomic number but different mass numbers, that is
different numbers of neutrons. Protium H-1 (no neutron), deuterium H-2 (1 neutron), tritium H-3 (2 neutrons).
Chlorine: Cl-35 at 75.77% and Cl-37 at 24.23%.
2. (35 x 75.77 + 37 x 24.23) / 100 = (2651.95 + 896.51)/100 = 35.48. Uses, any four: I-131 for the thyroid, Na-24
for blood flow, I-123 for brain imaging, Co-60 for cancer treatment, C-14 for tracing photosynthesis and for
carbon dating, S-35 for molecular structure. -->
""",
 "script": """السلام علیکم سیماب۔ آج کا موضوع ہے isotopes۔ اور یہ باب تین کا سب سے زیادہ کام آنے والا سبق ہے، کیونکہ اس سے سوال بھی بنتے ہیں اور حساب بھی۔

پہلے ایک سوال۔ آپ نے سنا ہو گا کہ سائنسدان ممی کی عمر بتا دیتے ہیں، یا کسی ہڈی کی، کہ یہ پانچ ہزار سال پرانی ہے۔ وہ یہ کیسے جانتے ہیں؟ کوئی وہاں موجود تو نہیں تھا۔ جواب اسی سبق میں ہے۔

پہلے تعریف۔ Isotopes وہ atoms ہیں جن کا atomic number ایک ہو مگر mass number الگ ہو۔ یعنی protons برابر، مگر neutrons الگ۔

لفظ Greek سے آیا ہے۔ isos کا مطلب ایک جیسا، اور tope کا مطلب جگہ۔ یعنی periodic table میں ایک ہی جگہ پر بیٹھنے والے۔ یہ لفظ سب سے پہلے Soddy نے استعمال کیا۔

اور ایک اہم بات: isotopes chemically بالکل ایک جیسے ہوتے ہیں۔ فرق صرف physical properties کا ہوتا ہے۔

اب کتاب کی مثالیں۔

Hydrogen کے تین isotopes ہیں۔ Protium، جس میں کوئی neutron نہیں، اور یہ ننانوے اعشاریہ ننانوے فیصد ہے۔ Deuterium، جس میں ایک neutron ہے۔ اور tritium، جس میں دو neutrons ہیں اور جو radioactive ہے۔

اور جب deuterium سے پانی بنے تو اسے heavy water کہتے ہیں۔ اس کے تین نمبر یاد رکھیں: melting point تین اعشاریہ آٹھ ایک، boiling point ایک سو ایک اعشاریہ دو، اور density ایک اعشاریہ ایک صفر چار چار۔ تینوں عام پانی سے زیادہ ہیں۔

Carbon کے تین isotopes: C بارہ اٹھانوے اعشاریہ آٹھ فیصد، C تیرہ ایک اعشاریہ ایک فیصد، اور C چودہ صفر اعشاریہ صفر صفر نو فیصد۔

Chlorine کے دو: Cl پینتیس پچھتر اعشاریہ سات سات فیصد، اور Cl سینتیس چوبیس اعشاریہ دو تین فیصد۔

اور uranium کے تین، جن میں سے U دو سو پینتیس سب سے اہم ہے، کیونکہ وہی reactors اور bombs میں استعمال ہوتا ہے، حالانکہ وہ صرف صفر اعشاریہ سات دو فیصد ہے۔

اب حساب، جو امتحان میں آتا ہے۔ Chlorine کا relative atomic mass نکالیں۔

طریقہ یہ ہے: ہر isotope کا mass اس کے فیصد سے ضرب دیں، پھر جمع کریں، پھر سو سے تقسیم۔

پینتیس ضرب پچھتر اعشاریہ سات سات برابر چھبیس سو اکاون اعشاریہ نو پانچ۔ اور سینتیس ضرب چوبیس اعشاریہ دو تین برابر آٹھ سو چھیانوے اعشاریہ پانچ ایک۔ دونوں کا جمع پینتیس سو اڑتالیس اعشاریہ چار چھ۔ سو سے تقسیم کریں تو پینتیس اعشاریہ چار آٹھ۔

اور کتاب میں لکھا ہے پینتیس اعشاریہ چار پانچ تین۔ بالکل قریب۔ کل والا سوال اب حل ہو گیا۔

اور اب ممی والا سوال۔ اس کا جواب ہے carbon dating۔ C چودہ کی مدد سے carbon رکھنے والی چیزوں کی عمر معلوم کی جاتی ہے: چٹانیں، مٹی اور ممیاں۔

اور آخر میں طبی استعمال، چار نام۔ I ایک سو اکتیس thyroid کے لیے۔ Na چوبیس خون کے بہاؤ کے لیے۔ I ایک سو تئیس دماغ کی تصویر کے لیے۔ اور Co ساٹھ cancer کے علاج کے لیے۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
{
 "subject": S, "chapter": 3, "ref": "3.6", "slug": "chem-ch03-cations-anions",
 "summary": "Cations and anions: which one loses electrons, which gains, and which side of the periodic table each comes from.",
 "note": """
<h1><span class="emoji">➕</span> Chemistry Ch 3.6: Cations and Anions</h1>
<div class="sub">Chapter 3, Atomic Structure · kitab ke page 27 se 44</div>
<p>Neutral atom mein protons aur electrons barabar hote hain. Jab ye barabari <b>toot</b> jaye to atom par charge
aa jata hai, aur usay <b>ion</b> kehte hain.</p>
<table>
<tr><th style="width:20%"></th><th style="width:26%">Kya karta hai</th><th style="width:24%">Charge</th><th style="width:30%">Aam tor par</th></tr>
<tr><td><b>Cation</b></td><td>Electrons <b>khota</b> hai</td><td><b>Positive</b></td><td><b>Metals</b></td></tr>
<tr><td><b>Anion</b></td><td>Electrons <b>leta</b> hai</td><td><b>Negative</b></td><td><b>Non-metals</b></td></tr>
</table>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Kitab ki misalein</span>
<b>Cations:</b> Na &rarr; Na<sup>+</sup> (ek electron khoya) &middot; Mg &rarr; Mg<sup>2+</sup> (do khoye)<br>
<b>Anions:</b> O &rarr; O<sup>2-</sup> (do liye) &middot; F &rarr; F<sup>-</sup> (ek liya)</div>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Naam ulta mat karein</span>
Yaad rakhne ka tareeqa: <b>cation</b> mein "t" ko <b>plus ka nishan</b> samjhein, to cation = positive.<br>
Aur ek aur baat jo ulti lagti hai: electron <b>khone</b> se charge <b>positive</b> hota hai. Kyun? Kyunke electron
negative tha. Negative nikal gaya, to positive baqi bacha.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Define <b>cation</b> and <b>anion</b>, say which type of element usually forms each, and give two examples of
each from your book.</li>
<li>Magnesium forms Mg<sup>2+</sup>. Explain what happened to its electrons and why the charge is positive.</li>
</ol></div>
<!--KEY 1. A cation is a positive ion formed when an atom loses electrons, typically a metal (Na to Na+,
Mg to Mg2+). An anion is a negative ion formed when an atom gains electrons, typically a non-metal (O to O2-,
F to F-). 2. Magnesium lost two electrons. Electrons carry negative charge, so removing two negatives leaves the
atom with two more protons than electrons, giving a 2+ charge. -->
""",
 "script": """السلام علیکم سیماب۔ آج کا سبق مختصر ہے مگر اس میں ایک بات ایسی ہے جو پہلی بار الٹی لگتی ہے۔ موضوع ہے cations اور anions۔

پہلے ایک سوال۔ ایک atom اپنا electron کھو دے۔ electron منفی ہوتا ہے۔ تو atom پر کیا charge آنا چاہیے؟

زیادہ تر طالبات پہلی بار کہتی ہیں: منفی کھویا تو منفی ہو جائے گا۔ مگر جواب الٹا ہے۔ آئیے دیکھتے ہیں کیوں۔

پہلے بنیاد۔ ایک neutral atom میں protons اور electrons برابر ہوتے ہیں۔ مثبت اور منفی برابر، تو کل charge صفر۔

اب جب یہ برابری ٹوٹ جائے، تو atom پر charge آ جاتا ہے۔ اور اسی کو ion کہتے ہیں۔

Cation وہ ion ہے جو electrons کھو دیتا ہے، اور اس پر مثبت charge آتا ہے۔ اور یہ عام طور پر دھاتیں بناتی ہیں۔

Anion وہ ion ہے جو electrons لے لیتا ہے، اور اس پر منفی charge آتا ہے۔ اور یہ عام طور پر غیر دھاتیں بناتی ہیں۔

اب اوپر والے سوال کا جواب۔ سوچیں ایک atom میں گیارہ protons ہیں اور گیارہ electrons۔ برابر، تو charge صفر۔ اب ایک electron نکل گیا۔ اب گیارہ protons ہیں مگر صرف دس electrons۔ تو ایک مثبت زیادہ رہ گیا۔ اسی لیے charge مثبت ہو گیا۔

یعنی منفی نکل جائے تو مثبت بچتا ہے۔ یہ بات ایک بار سمجھ آ جائے تو کبھی نہیں بھولتی۔

اب کتاب کی مثالیں۔ Sodium ایک electron کھو کر Na مثبت بنتا ہے۔ Magnesium دو electrons کھو کر Mg دو مثبت بنتا ہے۔ یہ دونوں دھاتیں ہیں، اور دونوں cations ہیں۔

دوسری طرف oxygen دو electrons لے کر O دو منفی بنتا ہے۔ اور fluorine ایک electron لے کر F منفی بنتا ہے۔ یہ دونوں غیر دھاتیں ہیں، اور دونوں anions ہیں۔

اور نام یاد رکھنے کا ایک آسان طریقہ۔ لفظ cation میں جو t ہے، اسے جمع کا نشان سمجھ لیں۔ تو cation مطلب مثبت۔ اور باقی anion خود بخود منفی رہ جاتا ہے۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
{
 "subject": S, "chapter": 3, "ref": "3.7", "slug": "chem-ch03-electronic-configuration",
 "summary": "Shells and sub-shells, how many electrons each holds, the energy order, and the Aufbau principle.",
 "note": """
<h1><span class="emoji">🪜</span> Chemistry Ch 3.7: Electronic Configuration</h1>
<div class="sub">Chapter 3, Atomic Structure · kitab ke page 27 se 44</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Shells aur sub-shells</span>
<b>Shells</b> ko harfon se likhte hain: <b>K = 1, L = 2, M = 3, N = 4</b>.<br>
Har shell ke andar <b>sub-shells</b> hoti hain, aur har ek ki apni gunjaish hai:<br>
<b>s = 2</b> electrons &middot; <b>p = 6</b> &middot; <b>d = 10</b> &middot; <b>f = 14</b></div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Auf Bau Principle</span>
Electrons hamesha <b>sab se kam energy wali sub-shell pehle</b> bharte hain.<br>
Energy ki tarteeb: <b>1s &lt; 2s &lt; 2p &lt; 3s &lt; 3p &lt; 4s &lt; 3d ...</b></div>
<div class="box warn"><span class="t"><span class="emoji">⚠️</span> 4s pehle, 3d baad mein</span>
Ghor karein: <b>4s</b> ka number bara hai magar wo <b>3d se pehle</b> aata hai. Ye galti sab se zyada hoti hai.<br>
Wajah: shell ka number nahin, <b>energy</b> ahem hai, aur 4s ki energy 3d se kam hai. Tarteeb <b>ratt lein</b>.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Likhne ka tareeqa</span>
Sodium (Z = 11), yani 11 electrons: <b>1s<sup>2</sup> 2s<sup>2</sup> 2p<sup>6</sup> 3s<sup>1</sup></b><br>
Ginti kar lein: 2 + 2 + 6 + 1 = 11. Ye ginti <b>hamesha</b> karein, yehi check hai.<br>
<b>Notation:</b> mass number <b>oopar bayein</b>, atomic number <b>neeche bayein</b>, charge <b>oopar dayein</b>.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Name the first four shells with their numbers, and give the maximum electrons each sub-shell can hold.</li>
<li>State the <b>Auf Bau principle</b>, write the energy order up to 3d, and give the electronic configuration of
sodium (Z = 11). Explain why 4s fills before 3d.</li>
</ol></div>
<!--KEY 1. K=1, L=2, M=3, N=4. s holds 2, p holds 6, d holds 10, f holds 14.
2. Electrons fill the lowest energy sub-shell first. Order: 1s < 2s < 2p < 3s < 3p < 4s < 3d. Sodium:
1s2 2s2 2p6 3s1 (2+2+6+1 = 11). 4s fills before 3d because filling follows energy, not shell number, and the
4s sub-shell has lower energy than 3d. -->
""",
 "script": """السلام علیکم سیماب۔ آج باب تین کا آخری سبق ہے: electronic configuration۔ یعنی electrons atom کے اندر بیٹھتے کیسے ہیں۔

پہلے ایک سوال، اور یہ وہی سوال ہے جہاں سب سے زیادہ غلطی ہوتی ہے۔

ترتیب لکھتے وقت ہم لکھتے ہیں چار s پہلے، اور تین d بعد میں۔ اب غور کریں: چار تین سے بڑا ہے۔ تو پھر چار والا پہلے کیوں آ گیا؟ جواب آخر میں۔

پہلے بنیاد۔ Electrons nucleus کے گرد shells میں بیٹھتے ہیں۔ اور shells کو حروف سے لکھتے ہیں: K یعنی ایک، L یعنی دو، M یعنی تین، اور N یعنی چار۔

ہر shell کے اندر چھوٹے خانے ہوتے ہیں، جنہیں sub-shells کہتے ہیں۔ اور ہر ایک کی اپنی گنجائش ہے۔

s میں دو electrons آ سکتے ہیں۔ p میں چھ۔ d میں دس۔ اور f میں چودہ۔

یہ چار نمبر یاد کر لیں: دو، چھ، دس، چودہ۔ ہر بار چار کا اضافہ۔ اسی لیے یاد رکھنا آسان ہے۔

اب اصول۔ اسے Auf Bau principle کہتے ہیں، اور یہ کہتا ہے کہ electrons ہمیشہ سب سے کم energy والی sub-shell پہلے بھرتے ہیں۔

اور energy کی ترتیب یہ ہے: ایک s، پھر دو s، پھر دو p، پھر تین s، پھر تین p، پھر چار s، اور پھر تین d۔

اور یہیں اوپر والے سوال کا جواب ہے۔

Electrons shell کا نمبر نہیں دیکھتے۔ وہ energy دیکھتے ہیں۔ اور چار s کی energy تین d سے کم ہے۔ اسی لیے چار s پہلے بھرتا ہے، حالانکہ اس کا نمبر بڑا ہے۔

یہ بات رٹ لیں، کیونکہ یہیں سب سے زیادہ نمبر کٹتے ہیں۔

اب ایک مثال۔ Sodium کا atomic number گیارہ ہے، یعنی گیارہ electrons۔

پہلے ایک s میں دو۔ باقی بچے نو۔ پھر دو s میں دو۔ باقی بچے سات۔ پھر دو p میں چھ۔ باقی بچا ایک۔ اور وہ تین s میں چلا گیا۔

تو sodium کی configuration ہوئی: ایک s دو، دو s دو، دو p چھ، تین s ایک۔

اور اب ایک عادت جو ہمیشہ بچاتی ہے: آخر میں گنتی کر لیں۔ دو جمع دو جمع چھ جمع ایک برابر گیارہ۔ اور atomic number بھی گیارہ تھا۔ ٹھیک ہے۔

یہ گنتی ہر بار کریں۔ اگر یہ نہ ملے تو کہیں غلطی ہے۔

اور آخری بات، notation کی۔ mass number اوپر بائیں طرف، atomic number نیچے بائیں طرف، اور charge اوپر دائیں طرف۔

اس کے ساتھ باب تین مکمل ہو گیا۔ آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
]

if __name__ == "__main__":
    build(LESSONS, C)
