# -*- coding: utf-8 -*-
"""Chemistry Chapter 2: Matter. Her book p15 to 26."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import build

C = "#1e7a4a"
S = "chemistry"

LESSONS = [
{
 "subject": S, "chapter": 2, "ref": "2.1", "slug": "chem-ch02-states-of-matter",
 "summary": "The four states of matter plus the two exotic ones, and Table 2.1 comparing density, compressibility and fluidity.",
 "note": """
<h1><span class="emoji">🧊</span> Chemistry Ch 2.1: States of Matter</h1>
<div class="sub">Chapter 2, Matter · kitab ke page 15 se 26</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Pehle bunyad</span>
<b>Matter</b> wo har cheez hai jis mein <b>mass</b> ho aur jo <b>jagah ghere</b>. Matter atoms se bana hai, aur
atom hi har maddey ka building block hai.<br>
Aur riyasatein (states) alag kyun hoti hain? Sirf <b>atoms ki tarteeb (arrangement)</b> ki wajah se.</div>
<table>
<tr><th style="width:18%">State</th><th style="width:44%">Pehchan</th><th style="width:38%">Misalein</th></tr>
<tr><td><b>Solid</b></td><td>Shakl bhi mutayyan, volume bhi. Zarray bilkul paas paas.</td><td>Barf, heera, dhatein</td></tr>
<tr><td><b>Liquid</b></td><td>Volume mutayyan, magar shakl bartan wali.</td><td>Paani, tel, doodh, shehad</td></tr>
<tr><td><b>Gas</b></td><td>Na shakl mutayyan na volume. Zarray door door.</td><td>O<sub>2</sub>, H<sub>2</sub>, N<sub>2</sub></td></tr>
<tr><td><b>Plasma</b></td><td>Bohat <b>ionized</b> gas, electrons alag ho jate hain, bijli chalati hai.</td>
<td>Sooraj, aasmani bijli, welding ka arc</td></tr>
</table>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Do exotic states, ye aksar bhool jati hain</span>
<b>BEC (Bose Einstein Condensate):</b> <b>absolute zero</b> ke qareeb, yani <b>-273.14&deg;C</b>, jahan saaray zarray
ek hi quantum state mein aa jate hain. Misal: rubidium ke atoms.<br>
<b>Liquid Crystals:</b> liquid aur solid ke <b>darmiyan</b>. Bahti liquid ki tarah hain magar tarteeb solid wali.
Misal: <b>LCD</b> screens, yani aap ka mobile.</div>
<h2><span class="emoji">📋</span> Table 2.1: teenon ka muqabla</h2>
<table>
<tr><th style="width:34%">Property</th><th style="width:22%">Gas</th><th style="width:22%">Liquid</th><th style="width:22%">Solid</th></tr>
<tr><td>Density</td><td>Low</td><td>High</td><td>High</td></tr>
<tr><td>Compressibility</td><td><b>Very</b></td><td>Moderate</td><td><b>Not</b></td></tr>
<tr><td>Fluidity</td><td>Can flow</td><td>Can flow</td><td>Cannot flow</td></tr>
</table>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Name the <b>four</b> states of matter with one example of each, then name the <b>two</b> exotic states and say
what makes each one special.</li>
<li>Copy Table 2.1, comparing density, compressibility and fluidity for gas, liquid and solid.</li>
</ol></div>
<!--KEY 1. Solid (ice/diamond/metals), liquid (water/oil/milk), gas (O2/H2/N2), plasma (sun, lightning, welding
arc). Exotic: BEC, formed near absolute zero (-273.14 C) where particles share one quantum state; liquid crystals,
between liquid and solid, flowing like a liquid but with ordered structure, used in LCDs.
2. Density: low, high, high. Compressibility: very, moderate, not. Fluidity: can flow, can flow, cannot flow. -->
""",
 "script": """السلام علیکم سیماب۔ آج Chemistry کے باب دو کی دہرائی شروع ہو رہی ہے، اور پہلا موضوع ہے states of matter۔ لیکن پہلے ایک سوال۔

آپ سب جانتی ہیں کہ مادے کی تین حالتیں ہوتی ہیں: ٹھوس، مائع اور گیس۔ لیکن سورج کس حالت میں ہے؟ سورج نہ ٹھوس ہے، نہ مائع، اور گیس بھی نہیں ہے۔ تو پھر کیا ہے؟

جواب ابھی آئے گا۔ پہلے بنیاد۔

Matter وہ ہر چیز ہے جس میں mass ہو اور جو جگہ گھیرے۔ اور matter atoms سے بنا ہے۔ اب غور کرنے والی بات یہ ہے: برف، پانی اور بھاپ، تینوں میں atoms بالکل ایک جیسے ہیں۔ پھر فرق کیا ہے؟ صرف ترتیب کا۔ atoms کی arrangement بدل جاتی ہے، اور حالت بدل جاتی ہے۔

پہلی حالت، solid۔ اس کی شکل بھی متعین ہے اور volume بھی۔ ذرے بالکل پاس پاس جڑے ہوئے۔ مثال: برف، ہیرا، دھاتیں۔

دوسری، liquid۔ اس کا volume متعین ہے مگر شکل نہیں۔ جس برتن میں ڈالو وہی شکل لے لیتا ہے۔ مثال: پانی، تیل، دودھ، شہد۔

تیسری، gas۔ نہ شکل متعین نہ volume۔ ذرے دور دور۔ مثال: oxygen، hydrogen، nitrogen۔

اور اب چوتھی، اور یہی اوپر والے سوال کا جواب ہے: plasma۔ یہ بہت زیادہ ionized گیس ہوتی ہے، جس میں electrons اپنے atoms سے الگ ہو چکے ہوتے ہیں۔ اور اسی لیے یہ بجلی چلاتی ہے۔ سورج plasma ہے۔ آسمانی بجلی plasma ہے۔ اور welding کا arc بھی plasma ہے۔

اب دو اور حالتیں، جنہیں کتاب exotic کہتی ہے، اور یہی امتحان میں بھول جاتی ہیں۔

پہلی، BEC، یعنی Bose Einstein Condensate۔ یہ absolute zero کے قریب بنتی ہے، یعنی منفی دو سو تہتر اعشاریہ ایک چار ڈگری سینٹی گریڈ پر۔ اتنی ٹھنڈ میں سارے ذرے ایک ہی quantum state میں آ جاتے ہیں۔ مثال: rubidium کے atoms۔

اور دوسری، liquid crystals۔ یہ liquid اور solid کے بیچ میں ہے۔ بہتی liquid کی طرح ہے مگر ترتیب solid والی رکھتی ہے۔ اور یہ آپ کے ہاتھ میں ہے: LCD screen کا L C D کا مطلب ہی liquid crystal display ہے۔

اب آخر میں Table دو نقطہ ایک، جو اکثر لکھوائی جاتی ہے۔ اس میں تین properties ہیں۔

Density: gas میں کم، liquid میں زیادہ، solid میں زیادہ۔

Compressibility، یعنی دبائی جا سکتی ہے یا نہیں: gas بہت زیادہ، liquid درمیانی، اور solid بالکل نہیں۔

اور fluidity، یعنی بہہ سکتی ہے یا نہیں: gas بہہ سکتی ہے، liquid بہہ سکتی ہے، solid نہیں بہہ سکتی۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
{
 "subject": S, "chapter": 2, "ref": "2.2", "slug": "chem-ch02-element-compound-mixture",
 "summary": "Element, compound and mixture: the three definitions and the two tests that separate them, fixed ratio and how they come apart.",
 "note": """
<h1><span class="emoji">🔗</span> Chemistry Ch 2.2: Elements, Compounds and Mixtures</h1>
<div class="sub">Chapter 2, Matter · kitab ke page 15 se 26</div>
<p>Teen lafz jo roz istemal hote hain aur teenon ka farq imtihan mein poochha jata hai. Farq sirf <b>do sawalon</b>
se nikal aata hai, aur wo neeche box mein hain.</p>
<table>
<tr><th style="width:20%"></th><th style="width:46%">Kitab ki definition</th><th style="width:34%">Misalein</th></tr>
<tr><td><b>Element</b></td><td><b>Ek hi qism</b> ke atom. Chemically toray nahin ja sakte.</td>
<td>O<sub>2</sub>, Au (sona), C</td></tr>
<tr><td><b>Compound</b></td><td>Do ya zyada elements <b>chemically</b> jure, <b>fixed ratio</b> mein. Properties
asal elements se <b>bilkul alag</b>.</td><td>H<sub>2</sub>O, CO<sub>2</sub>, NaCl</td></tr>
<tr><td><b>Mixture</b></td><td>Do ya zyada maddey <b>physically</b> milay. <b>Koi fixed ratio nahin</b>. Alag kiye
ja sakte hain.</td><td>Hawa, namak ka paani, ret aur loha</td></tr>
</table>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Do sawal jo faisla kar dete hain</span>
<b>Sawal 1: ratio fix hai?</b> Paani hamesha do hydrogen aur ek oxygen, chahe kahin ka bhi ho. Fix hai, to
<b>compound</b>. Namak ka paani kam ya zyada namkeen ho sakta hai. Fix nahin, to <b>mixture</b>.<br>
<b>Sawal 2: alag kaise hoga?</b> Mixture <b>physical</b> tareeqe se alag ho jata hai (chhanna, magnet, ubalna).
Compound ke liye <b>chemical</b> amal chahiye.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Ek misal jo poori baat kholti hai</span>
Sodium ek dhat hai jo paani mein aag pakar leti hai. Chlorine ek zehreeli gas hai. Dono mila kar
<b>NaCl</b> banta hai, yani wo namak jo aap roz khati hain.<br>
Yehi compound ki pehchan hai: <b>nayi properties</b>, asal elements se bilkul alag.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Define <b>element</b>, <b>compound</b> and <b>mixture</b> in the words of your book, with one example of each.</li>
<li>Give <b>two</b> differences between a compound and a mixture, and explain why table salt is a compound and not
a mixture of sodium and chlorine.</li>
</ol></div>
<!--KEY 1. Element: made of one type of atom, cannot be broken down chemically (O2, Au, C). Compound: two or more
elements chemically combined in a fixed ratio, with properties different from its elements (H2O, CO2, NaCl).
Mixture: two or more substances physically mixed, no fixed ratio, separable (air, saltwater, sand and iron).
2. (i) A compound has a fixed ratio, a mixture does not. (ii) A compound needs a chemical change to separate, a
mixture separates physically. Salt is a compound because sodium and chlorine are chemically combined in a fixed
ratio and the result has completely different properties from either element. -->
""",
 "script": """السلام علیکم سیماب۔ آج تین لفظوں کا فرق ہے: element، compound اور mixture۔ یہ تینوں آپ روز سنتی ہیں، اور امتحان میں انہی کا فرق پوچھا جاتا ہے۔

پہلے ایک سوال۔ آپ کے کچن میں نمک رکھا ہے۔ نمک بنتا ہے sodium اور chlorine سے۔

اب سنیے یہ دونوں کیا ہیں۔ Sodium ایک ایسی دھات ہے جو پانی میں ڈالو تو آگ پکڑ لیتی ہے۔ اور chlorine ایک زہریلی گیس ہے، اتنی زہریلی کہ جنگوں میں استعمال ہوئی۔

تو سوال یہ ہے: ایک آگ پکڑنے والی دھات اور ایک زہریلی گیس، دونوں مل کر وہ چیز کیسے بن جاتی ہیں جو آپ روز کھاتی ہیں؟

جواب اسی سبق میں ہے۔ چلیں تینوں لفظ دیکھتے ہیں۔

Element وہ ہے جو ایک ہی قسم کے atoms سے بنا ہو، اور جسے chemically توڑا نہ جا سکے۔ مثال: oxygen، سونا، carbon۔

Compound وہ ہے جس میں دو یا زیادہ elements chemically جڑے ہوں، ایک متعین تناسب میں۔ اور اس کی properties اصل elements سے بالکل الگ ہوتی ہیں۔ مثال: پانی، carbon dioxide، نمک۔

اور mixture وہ ہے جس میں دو یا زیادہ مادے صرف physically ملے ہوں۔ کوئی متعین تناسب نہیں، اور انہیں الگ کیا جا سکتا ہے۔ مثال: ہوا، نمک والا پانی، ریت اور لوہا۔

اب واپس نمک پر۔ جواب مل گیا: نمک ایک compound ہے۔ اور compound کی سب سے بڑی پہچان یہی ہے کہ اس کی properties نئی ہوتی ہیں۔ sodium کی نہیں، chlorine کی نہیں، بالکل نئی۔

اب ایک آسان طریقہ، جس سے آپ ہر سوال میں فیصلہ کر سکیں گی۔ دو سوال پوچھیں۔

پہلا سوال: تناسب fix ہے؟ پانی ہمیشہ دو hydrogen اور ایک oxygen ہوتا ہے، چاہے دنیا میں کہیں کا بھی ہو۔ fix ہے، تو compound۔ لیکن نمک والا پانی کم نمکین بھی ہو سکتا ہے اور زیادہ بھی۔ fix نہیں، تو mixture۔

دوسرا سوال: الگ کیسے ہو گا؟ Mixture کو physical طریقے سے الگ کیا جا سکتا ہے: چھان لو، magnet لگا لو، ابال لو۔ لیکن compound کو توڑنے کے لیے chemical عمل چاہیے۔

بس یہی دو سوال۔ تناسب fix ہے یا نہیں، اور الگ کیسے ہو گا۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
{
 "subject": S, "chapter": 2, "ref": "2.3", "slug": "chem-ch02-allotropes",
 "summary": "Allotropy, and the three forms of carbon: graphite, diamond and buckyballs, with why one is soft and conducts while the other is the hardest thing there is.",
 "note": """
<h1><span class="emoji">💎</span> Chemistry Ch 2.3: Allotropes of Carbon</h1>
<div class="sub">Chapter 2, Matter · kitab ke page 15 se 26</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Allotropy</span>
Kisi element ki wo khasoosiyat ke wo <b>alag alag physical shaklon</b> mein mojood ho sakta hai.<br>
Yani atom wohi hain, sirf <b>jurne ka andaz</b> alag hai, aur isi se cheez bilkul badal jati hai.</div>
<table>
<tr><th style="width:18%">Shakal</th><th style="width:40%">Banawat</th><th style="width:42%">Properties</th></tr>
<tr><td><b>Graphite</b></td><td>Do rukhi (2D) <b>hexagonal tehen</b>. Tehon ke darmiyan bond <b>kamzor</b>.</td>
<td><b>Naram aur phisalna</b>, aur bijli ka <b>acha conductor</b></td></tr>
<tr><td><b>Diamond</b></td><td>Har carbon <b>chaar</b> doosre carbon se jura, <b>tetrahedral</b> shakal.</td>
<td>Sab se <b>sakht</b> maddah, melting point bohat <b>ooncha</b>, bijli <b>nahin</b> chalata</td></tr>
<tr><td><b>Buckyballs</b><br>(C-60, Fullerenes)</td><td>Football jaisi <b>khokhli</b> gaind: <b>20 hexagons + 12
pentagons</b>, 60 carbon atoms, har ek <b>teen</b> se jura.</td><td>Khokhla aur gol</td></tr>
</table>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Do sawal jo hamesha aate hain</span>
<b>Graphite naram kyun hai jab carbon itna mazboot hai?</b> Kyunke tehen ke <b>andar</b> bond mazboot hain magar
<b>tehon ke darmiyan</b> kamzor. Is liye tehen ek doosri par phisal jati hain. Pencil isi tarah likhti hai.<br>
<b>Diamond bijli kyun nahin chalata?</b> Kyunke har carbon apne <b>chaaron</b> electrons bond mein laga chuka hai,
to koi <b>free electron</b> bacha hi nahin. Graphite mein chautha electron azad hai, isi liye wo chalata hai.</div>
<div class="box warn"><span class="t"><span class="emoji">⚠️</span> Number yaad rakhein</span>
Buckyball: <b>60</b> carbon atoms, <b>20</b> hexagons, <b>12</b> pentagons, har atom <b>3</b> se jura.
Diamond mein har atom <b>4</b> se jura. Ye 3 aur 4 ka farq hi sab kuch badal deta hai.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Define <b>allotropy</b>, then name the three allotropes of carbon your book gives and describe the structure
of each.</li>
<li>Graphite and diamond are both pure carbon. Explain why graphite is soft and conducts electricity while
diamond is the hardest substance and does not conduct.</li>
</ol></div>
<!--KEY 1. Allotropy is the property of an element to exist in different physical forms. Graphite: 2D hexagonal
layers with weak bonds between layers. Diamond: each carbon bonded to four others in a tetrahedral arrangement.
Buckyballs (C-60/fullerenes): hollow football-like ring of 20 hexagons and 12 pentagons, 60 carbon atoms each
bonded to three others.
2. In graphite the bonds within a layer are strong but those between layers are weak, so layers slide over one
another, making it soft and slippery; its fourth electron is free, so it conducts. In diamond every carbon uses
all four electrons in bonds, giving a rigid tetrahedral network (hardest, very high melting point) and leaving no
free electrons, so it cannot conduct. -->
""",
 "script": """السلام علیکم سیماب۔ آج کا سبق میرے خیال میں پورے باب دو کا سب سے دلچسپ ہے۔ موضوع ہے allotropes۔ لیکن پہلے ایک سوال۔

آپ کی پنسل کے اندر جو کالا سیسہ ہے، اور آپ کی امی کی انگوٹھی میں جو ہیرا ہے، دونوں بالکل ایک ہی چیز سے بنے ہیں۔ دونوں خالص carbon ہیں۔ ایک ہی element۔

اب سوچیں۔ پنسل کا سیسہ اتنا نرم ہے کہ کاغذ پر رگڑو تو نشان چھوڑ دیتا ہے۔ اور ہیرا دنیا کی سخت ترین چیز ہے۔ ایک ہی element سے دو بالکل الٹی چیزیں کیسے بن گئیں؟

جواب اسی سبق میں ہے۔

پہلے definition۔ Allotropy کسی element کی وہ خصوصیت ہے کہ وہ الگ الگ physical شکلوں میں موجود ہو سکتا ہے۔ یعنی atoms وہی ہیں، صرف جڑنے کا انداز الگ ہے۔

اب carbon کی تین شکلیں۔

پہلی، graphite، یعنی پنسل والا سیسہ۔ اس میں carbon کے atoms چھ کونوں والی تہوں میں جڑے ہوتے ہیں۔ تہہ کے اندر bond مضبوط ہیں۔ لیکن تہوں کے درمیان bond کمزور ہیں۔

اور یہی جواب ہے۔ جب آپ پنسل رگڑتی ہیں تو تہیں ایک دوسری پر پھسل جاتی ہیں اور کاغذ پر رہ جاتی ہیں۔ graphite نرم اس لیے نہیں کہ carbon کمزور ہے، بلکہ اس لیے کہ تہوں کے بیچ کی پکڑ کمزور ہے۔

دوسری شکل، diamond۔ اس میں ہر carbon چار دوسرے carbon سے جڑا ہوتا ہے، اور شکل tetrahedral ہوتی ہے۔ یعنی ایک ٹھوس جالی، ہر طرف سے بندھی ہوئی۔ کوئی تہہ نہیں جو پھسل سکے۔ اسی لیے یہ سخت ترین ہے اور اس کا melting point بھی بہت اونچا ہے۔

اور اب ایک اور سوال جو امتحان میں آتا ہے۔ graphite بجلی چلاتا ہے مگر diamond نہیں۔ کیوں؟

carbon کے پاس چار electrons ہوتے ہیں جوڑنے کے لیے۔ diamond میں چاروں bond میں لگ جاتے ہیں، تو کوئی آزاد electron بچتا ہی نہیں۔ اور بجلی چلانے کے لیے آزاد electron چاہیے۔ graphite میں ہر carbon صرف تین سے جڑتا ہے، تو چوتھا آزاد رہ جاتا ہے، اور وہی بجلی چلاتا ہے۔

تیسری شکل، buckyballs، جنہیں fullerenes بھی کہتے ہیں۔ یہ فٹبال جیسی کھوکھلی گیند ہے۔ اور اس کے نمبر یاد رکھیں: ساٹھ carbon atoms، بیس hexagons، بارہ pentagons، اور ہر atom تین سے جڑا ہوا۔

تو آج کی بات ایک جملے میں: atoms وہی، ترتیب الگ، اور نتیجہ بالکل الٹا۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
{
 "subject": S, "chapter": 2, "ref": "2.4", "slug": "chem-ch02-solutions",
 "summary": "Solute and solvent, the three types of solution, saturated against unsaturated against supersaturated, and how temperature changes solubility.",
 "note": """
<h1><span class="emoji">🥤</span> Chemistry Ch 2.4: Solutions and Solubility</h1>
<div class="sub">Chapter 2, Matter · kitab ke page 15 se 26 · sections 2.4 aur 2.4.7 se 2.4.8</div>
<div class="box def"><span class="t"><span class="emoji">📖</span> Solution</span>
Ek <b>homogeneous</b> mixture jis ke zarray <b>1 nanometre se chhote</b> hon aur jo <b>mustahkam (stable)</b> ho.<br>
<b>Solute:</b> jo ghulta hai. <b>Solvent:</b> jo ghol raha hai.<br>
<b>Aqueous solution:</b> jo paani mein ghula ho. Paani ko <b>universal solvent</b> kaha jata hai.</div>
<table>
<tr><th style="width:22%">Qism</th><th style="width:78%">Misalein</th></tr>
<tr><td><b>Gaseous</b></td><td>Haber's process mein N<sub>2</sub> aur H<sub>2</sub>, dhund (fog), dhuan</td></tr>
<tr><td><b>Liquid</b></td><td>Carbonated drinks, sirka, brine (namkeen paani)</td></tr>
<tr><td><b>Solid</b></td><td>Nickel par hydrogen, amalgam, <b>alloys</b></td></tr>
</table>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Teen halatein, ye har baar poochhi jati hain</span>
<b>Unsaturated:</b> zyadatar se <b>kam</b> solute. Aur ghol sakta hai.<br>
<b>Saturated:</b> us temperature par <b>zyada se zyada</b> solute ghul chuka. Ab <b>dynamic equilibrium</b> hai.<br>
<b>Supersaturated:</b> saturated se bhi <b>zyada</b>. Ye <b>ghair mustahkam (unstable)</b> hai, aur banti hai
pehle <b>garam</b> kar ke phir <b>thanda</b> kar ke.<br>
Alag baat: <b>concentrated aur dilute</b> sirf solute ki <b>nisbatan miqdar</b> batate hain. Brine concentrated hai.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Solubility aur temperature</span>
<b>Solubility:</b> kisi khaas solvent mein, kisi khaas temperature par, zyada se zyada kitna solute ghul sakta hai.<br>
<b>Zyadatar solute:</b> temperature barhne se solubility <b>barhti</b> hai. KCl 34.7 se 56 g, NH<sub>4</sub>Cl 37.5 se 77 g.<br>
<b>Kuch ki kam hoti hai:</b> Ca(OH)<sub>2</sub> 0.173 se <b>0.066</b> g, aur Na<sub>2</sub>SO<sub>4</sub>.<br>
Ye do istisna yaad rakhein, sawal inhi par banta hai.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Define <b>solution</b>, <b>solute</b> and <b>solvent</b>, then name the three types of solution with one
example of each.</li>
<li>Explain the difference between <b>saturated</b>, <b>unsaturated</b> and <b>supersaturated</b> solutions, and
name two substances whose solubility <b>decreases</b> as temperature rises.</li>
</ol></div>
<!--KEY 1. A solution is a homogeneous mixture with particles smaller than 1 nm, and it is stable. The solute is
the substance dissolved; the solvent is the substance doing the dissolving. Types: gaseous (N2 and H2 in Haber's
process, fog, smoke), liquid (carbonated drinks, vinegar, brine), solid (hydrogen on nickel, amalgam, alloys).
2. Unsaturated holds less than the maximum and can dissolve more. Saturated holds the maximum at that temperature
and is in dynamic equilibrium. Supersaturated holds more than saturated, is unstable, and is made by heating then
cooling. Solubility falls with temperature for calcium hydroxide and sodium sulphate. -->
""",
 "script": """السلام علیکم سیماب۔ آج کا موضوع ہے solutions۔ اور یہ آپ کے کچن میں روز ہوتا ہے۔

پہلے ایک سوال۔ ایک گلاس ٹھنڈے پانی میں چینی ڈالیں اور ہلائیں۔ تھوڑی دیر بعد چینی گھلنا بند ہو جائے گی اور نیچے بیٹھ جائے گی۔ اب اسی گلاس کو گرم کریں۔ وہی بچی ہوئی چینی گھل جائے گی۔

سوال یہ ہے: چینی وہی تھی، پانی بھی وہی تھا۔ گرمی نے کیا بدل دیا؟ جواب آخر میں۔

پہلے definition۔ Solution ایک homogeneous mixture ہے جس کے ذرے ایک nanometre سے چھوٹے ہوں، اور جو مستحکم ہو۔

اس میں دو حصے ہوتے ہیں۔ Solute وہ ہے جو گھلتا ہے، یعنی چینی۔ اور solvent وہ ہے جو گھول رہا ہے، یعنی پانی۔ اور جب پانی solvent ہو تو اسے aqueous solution کہتے ہیں۔ پانی کو universal solvent کہا جاتا ہے، کیونکہ وہ سب سے زیادہ چیزیں گھولتا ہے۔

اب solutions کی تین قسمیں۔ Gaseous، جیسے Haber's process میں nitrogen اور hydrogen، یا دھند اور دھواں۔ Liquid، جیسے carbonated drinks، سرکہ، اور نمکین پانی۔ اور Solid، جیسے nickel پر hydrogen، amalgam، اور alloys۔

اب تین حالتیں، اور یہ ہر امتحان میں آتی ہیں۔

Unsaturated وہ ہے جس میں زیادہ سے کم solute ہو۔ یعنی ابھی اور گھل سکتا ہے۔

Saturated وہ ہے جس میں اس temperature پر زیادہ سے زیادہ solute گھل چکا ہو۔ اب اس میں dynamic equilibrium ہے۔

اور supersaturated وہ ہے جس میں saturated سے بھی زیادہ گھلا ہوا ہو۔ یہ غیر مستحکم ہوتا ہے، اور بنتا کیسے ہے؟ پہلے گرم کر کے، پھر ٹھنڈا کر کے۔

اور یہیں اوپر والے سوال کا جواب ہے۔ گرمی نے solubility بڑھا دی۔

Solubility کی definition یہ ہے: کسی خاص solvent میں، کسی خاص temperature پر، زیادہ سے زیادہ کتنا solute گھل سکتا ہے۔

زیادہ تر مادوں میں گرمی سے solubility بڑھتی ہے۔ KCl چونتیس اعشاریہ سات سے چھپن گرام تک، اور ammonium chloride سینتیس اعشاریہ پانچ سے ستتر گرام تک۔

لیکن اب ایک الٹی بات، اور یہی سوال بنتا ہے۔ کچھ مادوں کی solubility گرمی سے کم ہو جاتی ہے۔ calcium hydroxide صفر اعشاریہ ایک سات تین سے گر کر صفر اعشاریہ صفر چھ چھ گرام رہ جاتی ہے۔ اور sodium sulphate بھی ایسا ہی کرتا ہے۔

یہ دو نام یاد رکھیں، کیونکہ عام اصول کے خلاف ہیں اور اسی لیے پوچھے جاتے ہیں۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
{
 "subject": S, "chapter": 2, "ref": "2.5", "slug": "chem-ch02-colloids-suspensions",
 "summary": "Colloids and suspensions, the particle sizes that separate them from solutions, and the Tyndall effect.",
 "note": """
<h1><span class="emoji">🥛</span> Chemistry Ch 2.5: Colloids and Suspensions</h1>
<div class="sub">Chapter 2, Matter · kitab ke page 15 se 26</div>
<p>Pichhle safhay par solution tha. Ab do aur mixtures. Teenon ka farq sirf <b>ek cheez</b> se hai: <b>zarray ka
size</b>. Baqi sab usi se nikalta hai.</p>
<table>
<tr><th style="width:22%"></th><th style="width:24%">Zarray ka size</th><th style="width:54%">Pehchan aur misalein</th></tr>
<tr><td><b>Solution</b></td><td><b>1 nm se kam</b></td><td>Homogeneous, mustahkam. Namak ka paani.</td></tr>
<tr><td><b>Colloid</b></td><td><b>1 se 1000 nm</b></td><td><b>Heterogeneous</b>, <b>Tyndall effect</b> dikhata hai,
aur <b>alag nahin hota</b>. Doodh, nishasta, khoon, saabun.</td></tr>
<tr><td><b>Suspension</b></td><td><b>1000 nm se bara</b></td><td>Zarray <b>nazar aate</b> hain, aur rakha rahe to
<b>neeche baith</b> jate hain. Chalk ka paani, paint, gaara.</td></tr>
</table>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Tyndall effect, aur ise pehchanne ka tareeqa</span>
Jab roshni ka shuaa colloid mein se guzre to <b>raasta nazar aa jata hai</b>, kyunke zarray roshni ko bikher
dete hain.<br>
Aap ne ye dekha hua hai: andheray kamre mein khirki se aane wali dhoop ki lakeer, ya raat mein dhund mein gaari
ki headlight. Solution mein aisa nahin hota, kyunke us ke zarray bohat chhote hain.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Table 2.3 ke chaar farq, tarteeb se</span>
<b>1. Particle size:</b> chhota, darmiyana, bara.<br>
<b>2. Filtration:</b> solution aur colloid <b>filter paper se guzar</b> jate hain, suspension <b>ruk</b> jata hai.<br>
<b>3. Light scattering:</b> sirf <b>colloid</b> Tyndall effect dikhata hai.<br>
<b>4. Stability:</b> solution mustahkam, colloid mustahkam, suspension <b>baith</b> jata hai.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Give the particle size range for a <b>solution</b>, a <b>colloid</b> and a <b>suspension</b>, with one
example of each.</li>
<li>What is the <b>Tyndall effect</b>, and which of the three shows it? Then give two more differences between a
colloid and a suspension.</li>
</ol></div>
<!--KEY 1. Solution: below 1 nm (salt water). Colloid: 1 to 1000 nm (milk, starch, blood, soap). Suspension:
above 1000 nm (chalk in water, paints, muddy water).
2. The Tyndall effect is the scattering of light by particles so that the beam's path becomes visible. Only a
colloid shows it. Two further differences: a colloid passes through filter paper while a suspension is held back;
a colloid does not separate on standing while a suspension settles. -->
""",
 "script": """السلام علیکم سیماب۔ آج باب دو کا آخری سبق ہے: colloids اور suspensions۔ اور آج کی مثالیں سب آپ کے گھر سے ہیں۔

پہلے ایک سوال۔ رات کو دھند میں گاڑی کی headlight جلائیں تو روشنی کی پوری لکیر نظر آتی ہے، ہوا میں۔ لیکن صاف رات میں وہی headlight جلائیں تو لکیر نظر نہیں آتی، صرف آگے کی چیز روشن ہوتی ہے۔

سوال یہ ہے: روشنی وہی ہے۔ پھر ایک میں راستہ نظر آتا ہے اور دوسری میں کیوں نہیں؟ جواب آج کے سبق میں ہے۔

پہلے بنیادی بات۔ solution، colloid اور suspension، ان تینوں کا فرق صرف ایک چیز سے ہے: ذرے کا size۔ اور باقی سب باتیں اسی ایک سے نکلتی ہیں۔

Solution کے ذرے ایک nanometre سے چھوٹے ہوتے ہیں۔ اتنے چھوٹے کہ نظر ہی نہیں آتے۔ مثال: نمک والا پانی۔

Colloid کے ذرے ایک سے ایک ہزار nanometre کے درمیان ہوتے ہیں۔ یہ heterogeneous ہوتا ہے، مگر رکھا رہے تو الگ نہیں ہوتا۔ مثال: دودھ، نشاستہ، خون، اور صابن۔

اور suspension کے ذرے ایک ہزار nanometre سے بڑے ہوتے ہیں۔ یہ نظر آتے ہیں، اور رکھا رہے تو نیچے بیٹھ جاتے ہیں۔ مثال: چاک ملا پانی، paint، اور گارا۔

اب اوپر والے سوال کا جواب۔ اس کا نام ہے Tyndall effect۔

جب روشنی کی شعاع colloid میں سے گزرتی ہے تو ذرے اسے بکھیر دیتے ہیں، اور راستہ نظر آ جاتا ہے۔ دھند ایک colloid ہے، اسی لیے headlight کی لکیر نظر آتی ہے۔ صاف ہوا میں ایسے ذرے نہیں، اس لیے لکیر نہیں بنتی۔

آپ نے یہ اور بھی جگہ دیکھا ہو گا۔ اندھیرے کمرے میں کھڑکی سے آنے والی دھوپ کی لکیر، جس میں گرد کے ذرے چمکتے نظر آتے ہیں۔ وہی Tyndall effect ہے۔

اور یاد رکھیں: یہ صرف colloid دکھاتا ہے۔ solution نہیں دکھاتا، کیونکہ اس کے ذرے بہت چھوٹے ہیں۔

اب کتاب کی Table دو نقطہ تین کے چار فرق، ترتیب سے۔

پہلا، particle size: چھوٹا، درمیانہ، بڑا۔

دوسرا، filtration: solution اور colloid دونوں filter paper سے گزر جاتے ہیں، مگر suspension رک جاتا ہے۔

تیسرا، light scattering: صرف colloid Tyndall effect دکھاتا ہے۔

اور چوتھا، stability: solution مستحکم، colloid مستحکم، اور suspension بیٹھ جاتا ہے۔

اس کے ساتھ باب دو مکمل ہو گیا۔ آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
]

if __name__ == "__main__":
    build(LESSONS, C)
