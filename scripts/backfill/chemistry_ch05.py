# -*- coding: utf-8 -*-
"""Chemistry Chapter 5: Chemical Bonding. Her book p73 to 94."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import build
C = "#1e7a4a"; S = "chemistry"

def L(ref, slug, summary, note, script):
    return {"subject": S, "chapter": 5, "ref": ref, "slug": slug,
            "summary": summary, "note": note, "script": script}

LESSONS = [
L("5.1", "chem-ch05-why-atoms-react",
  "Why atoms bond at all: the octet rule, the duplet rule for the small atoms, and why noble gases do nothing.",
  """
<h1><span class="emoji">\U0001F9F2</span> Chemistry Ch 5.1: Why Do Atoms React?</h1>
<div class="sub">Chapter 5, Chemical Bonding &middot; kitab ke page 73 se 94</div>
<p>Ek sawal se shuru karte hain. Sodium paani mein daalein to aag pakar leta hai. Chlorine zehreeli gas hai.
Magar <b>helium</b> ko aap kuch bhi kar lein, wo kisi se nahin milta. Kyun? Ek element itna be-niyaz kyun hai?</p>
<div class="box def"><span class="t"><span class="emoji">\U0001F4D6</span> Jawab: bhari hui bairooni shell</span>
Noble gases ki bairooni shell <b>poori bhari</b> hoti hai. Wo pehle hi <b>mustahkam (stable)</b> hain, is liye
unhein kuch karne ki zaroorat hi nahin.<br>
Aur baqi tamam atoms <b>yehi halat</b> hasil karna chahte hain. Isi khwahish ka naam <b>chemical bonding</b> hai.</div>
<div class="box trick"><span class="t"><span class="emoji">\U0001F9E0</span> Do usool, aur dono yaad rakhne hain</span>
<b>Octet rule:</b> atom apni bairooni shell mein <b>8 electrons</b> chahta hai.<br>
<b>Duplet rule:</b> magar kuch chhote atoms ke liye <b>2 hi kaafi</b> hain, kyunke un ki pehli shell mein gunjaish
hi 2 ki hai. Ye hain <b>hydrogen, lithium aur beryllium</b>.<br>
<span style="color:#5b6475">Sawal mein aksar poochha jata hai ke octet aur duplet mein farq kya hai. Jawab: tadaad
ka, 8 banam 2, aur kaun se atoms par lagu hota hai.</span></div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Teen raaste, aur teen qism ke bond</span>
Atom mustahkam hone ke liye teen mein se ek kaam karta hai:<br>
<b>1. Electron de deta hai</b> &rarr; cation banta hai<br>
<b>2. Electron le leta hai</b> &rarr; anion banta hai<br>
<b>3. Electron share kar leta hai</b> &rarr; covalent bond banta hai<br>
Pehle do mil kar <b>ionic bond</b> banate hain. Teesra <b>covalent</b>. Baqi poora chapter inhi teen raaston ki
tafseel hai.</div>
<div class="box quiz"><span class="t"><span class="emoji">\U0001F9EA</span> Quiz</span>
<ol class="q">
<li>Why do noble gases not react? State the <b>octet rule</b> and the <b>duplet rule</b>, and name the three
elements the duplet rule applies to.</li>
<li>Name the <b>three</b> ways an atom can achieve a stable outer shell, and say which type of bond each one
leads to.</li>
</ol></div>
<!--KEY 1. Noble gases already have a complete outer shell, so they are stable and have no need to gain, lose or
share electrons. Octet rule: an atom tends to achieve eight electrons in its outermost shell. Duplet rule: for
hydrogen, lithium and beryllium two electrons complete the first shell, which holds only two.
2. Losing electrons (forms a cation), gaining electrons (forms an anion), or sharing electrons. Losing and
gaining together give an ionic bond; sharing gives a covalent bond. -->
""",
  """السلام علیکم سیماب۔ آج Chemistry کا باب پانچ شروع ہو رہا ہے: chemical bonding۔ لیکن پہلے ایک سوال۔

Sodium کو پانی میں ڈالیں تو آگ لگ جاتی ہے۔ Chlorine ایک زہریلی گیس ہے۔ یہ دونوں بہت reactive ہیں۔

مگر helium؟ آپ اسے گرم کریں، ٹھنڈا کریں، کسی کے ساتھ ملائیں، وہ کچھ نہیں کرتا۔ بالکل خاموش۔

تو سوال یہ ہے: ایک element اتنا بے نیاز کیوں ہے، اور باقی اتنے بے چین کیوں ہیں؟

جواب ایک لفظ میں ہے: shell۔

Noble gases کی بیرونی shell پوری بھری ہوئی ہوتی ہے۔ وہ پہلے ہی مستحکم ہیں۔ انہیں کسی سے کچھ نہیں چاہیے۔

اور باقی تمام atoms؟ وہ بھی یہی حالت چاہتے ہیں۔ اور اسی خواہش کا نام chemical bonding ہے۔

غور کریں یہ کتنی سادہ بات ہے۔ پوری Chemistry کا سب سے بڑا باب ایک ہی خواہش پر کھڑا ہے: ہر atom noble gas جیسا بننا چاہتا ہے۔

اب دو اصول، اور دونوں یاد رکھنے ہیں۔

پہلا، octet rule۔ atom اپنی بیرونی shell میں آٹھ electrons چاہتا ہے۔ Octet کا مطلب ہی آٹھ ہے۔

دوسرا، duplet rule۔ کچھ چھوٹے atoms کے لیے صرف دو ہی کافی ہیں۔ کیوں؟ کیونکہ ان کی پہلی shell میں گنجائش ہی دو کی ہے۔ ان کے لیے دو ہی پورے ہیں۔

اور یہ کون سے atoms ہیں؟ تین ہیں: hydrogen، lithium اور beryllium۔ یہ تین نام یاد کر لیں، کیونکہ سوال انہی پر بنتا ہے۔

اب تیسری اور آخری بات، جو پورے باب کا نقشہ ہے۔

اگر atom کو آٹھ چاہیے، تو وہ حاصل کیسے کرے؟ تین راستے ہیں۔

پہلا، وہ electron دے دے۔ ایسا دھاتیں کرتی ہیں، اور دینے سے وہ cation بن جاتی ہیں، یعنی مثبت۔

دوسرا، وہ electron لے لے۔ ایسا غیر دھاتیں کرتی ہیں، اور لینے سے وہ anion بن جاتی ہیں، یعنی منفی۔

اور تیسرا، وہ electron share کر لے۔ یعنی نہ دے نہ لے، بلکہ دونوں مل کر استعمال کریں۔

اب دیکھیں ان تینوں سے کیا بنتا ہے۔ پہلا اور دوسرا ایک ساتھ ہوں تو ionic bond بنتا ہے، کیونکہ ایک نے دیا اور دوسرے نے لیا۔ اور تیسرے سے covalent bond بنتا ہے۔

بس یہی پورے باب کا خلاصہ ہے۔ باقی سارا باب انہی تین راستوں کی تفصیل ہے۔

تو آج کی تین باتیں۔ ایک، atoms اس لیے جڑتے ہیں کہ وہ noble gas جیسے مستحکم ہونا چاہتے ہیں۔ دو، octet یعنی آٹھ، اور duplet یعنی دو، اور duplet صرف hydrogen، lithium اور beryllium کے لیے۔ اور تین، تین راستے: دینا، لینا، یا share کرنا۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
"""),

L("5.2", "chem-ch05-chemical-bonds",
  "What a chemical bond is, and how electropositive and electronegative elements decide which bond forms.",
  """
<h1><span class="emoji">\U0001F517</span> Chemistry Ch 5.2: Chemical Bonds</h1>
<div class="sub">Chapter 5, Chemical Bonding &middot; kitab ke page 73 se 94</div>
<div class="box def"><span class="t"><span class="emoji">\U0001F4D6</span> Chemical bond kya hai</span>
Wo <b>kheench (force of attraction)</b> jo do atoms ko aapas mein <b>jore</b> rakhti hai.<br>
Bond banta tab hai jab atoms mil kar <b>pehle se kam energy</b> wali halat mein pohanch jayein. Kam energy ka
matlab hai <b>zyada mustahkam</b>.</div>
<div class="box trick"><span class="t"><span class="emoji">\U0001F9E0</span> Do lafz jo faisla karte hain</span>
<b>Electropositive:</b> wo element jo electron <b>asaani se de</b> deta hai. Ye <b>dhatein</b> hain, aur periodic
table ke <b>bayein</b> taraf hain.<br>
<b>Electronegative:</b> wo element jo electron <b>apni taraf kheenchta</b> hai. Ye <b>ghair dhatein</b> hain, aur
<b>dayein</b> taraf hain.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Isi se bond ki qism tay hoti hai</span>
<table>
<tr><th style="width:52%">Kaun kis se mil raha hai</th><th style="width:48%">Kaunsa bond</th></tr>
<tr><td><b>Dhat + ghair dhat</b> (electropositive + electronegative)</td><td><b>Ionic</b>: ek deta hai, doosra leta hai</td></tr>
<tr><td><b>Ghair dhat + ghair dhat</b> (dono electronegative)</td><td><b>Covalent</b>: dono share karte hain</td></tr>
<tr><td><b>Dhat + dhat</b> (dono electropositive)</td><td><b>Metallic</b>: electron ka samundar</td></tr>
</table>
<span style="color:#5b6475">Yani sawal mein do element diye jayein to pehle dekhein ke wo table mein <b>kahan</b>
hain. Us se bond ki qism khud bakhud nikal aati hai.</span></div>
<div class="box quiz"><span class="t"><span class="emoji">\U0001F9EA</span> Quiz</span>
<ol class="q">
<li>Define a <b>chemical bond</b>, and explain in terms of energy why atoms form one.</li>
<li>Explain the difference between an <b>electropositive</b> and an <b>electronegative</b> element, say where
each sits in the periodic table, and give the type of bond formed by metal plus non-metal, non-metal plus
non-metal, and metal plus metal.</li>
</ol></div>
<!--KEY 1. A chemical bond is the force of attraction that holds two atoms together. Atoms bond because the
combined state has lower energy than the separate atoms, and lower energy means greater stability.
2. An electropositive element gives up electrons easily; these are the metals on the left of the periodic table.
An electronegative element attracts electrons to itself; these are the non-metals on the right. Metal plus
non-metal gives an ionic bond, non-metal plus non-metal gives a covalent bond, metal plus metal gives a metallic
bond. -->
""",
  """السلام علیکم سیماب۔ آج کا سبق چھوٹا ہے مگر اس کے بعد آپ کسی بھی دو elements کو دیکھ کر بتا سکیں گی کہ ان کے درمیان کون سا bond بنے گا۔ پہلے ایک سوال۔

امتحان میں لکھا ہو: sodium اور chlorine کے درمیان کون سا bond ہے؟ یا carbon اور oxygen کے درمیان؟ یا دو لوہے کے atoms کے درمیان؟

کیا آپ کو ہر جوڑی یاد کرنی پڑے گی؟ نہیں۔ ایک آسان اصول ہے، اور وہ آج سیکھیں گے۔

پہلے definition۔ Chemical bond وہ کھینچ ہے جو دو atoms کو آپس میں جوڑے رکھتی ہے۔

اور bond بنتا کیوں ہے؟ کتاب کہتی ہے: جب atoms مل کر پہلے سے کم energy والی حالت میں پہنچ جائیں۔

یہ نکتہ اہم ہے۔ کم energy کا مطلب ہے زیادہ مستحکم۔ قدرت میں ہر چیز کم energy کی طرف جاتی ہے۔ پتھر پہاڑ سے نیچے گرتا ہے، اوپر نہیں چڑھتا۔ اسی طرح atoms بھی اسی حالت میں جاتے ہیں جہاں energy کم ہو۔

اب دو لفظ، اور یہی سارا فیصلہ کرتے ہیں۔

Electropositive وہ element ہے جو electron آسانی سے دے دیتا ہے۔ یہ دھاتیں ہیں، اور یہ periodic table کے بائیں طرف ہیں۔

Electronegative وہ element ہے جو electron اپنی طرف کھینچتا ہے۔ یہ غیر دھاتیں ہیں، اور یہ دائیں طرف ہیں۔

اب اوپر والے سوال کا جواب۔ تین صورتیں ہیں۔

پہلی، دھات اور غیر دھات مل رہے ہوں۔ یعنی ایک دینے والا اور ایک لینے والا۔ تو ionic bond بنے گا۔ Sodium اور chlorine یہی ہیں۔

دوسری، دونوں غیر دھاتیں ہوں۔ یعنی دونوں لینا چاہتے ہیں، کوئی دینے کو تیار نہیں۔ تو وہ share کریں گے، اور covalent bond بنے گا۔ Carbon اور oxygen یہی ہیں۔

اور تیسری، دونوں دھاتیں ہوں۔ یعنی دونوں دینا چاہتے ہیں۔ تو metallic bond بنے گا، جس میں electrons کا سمندر بن جاتا ہے۔ لوہے کے دو atoms یہی ہیں۔

تو اصول صرف اتنا ہے: دیکھیں دونوں element periodic table میں کہاں ہیں۔ بائیں اور دائیں ملیں تو ionic۔ دونوں دائیں ہوں تو covalent۔ دونوں بائیں ہوں تو metallic۔

کوئی جوڑی یاد کرنے کی ضرورت نہیں۔ صرف جگہ دیکھنی ہے۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
"""),
]

if __name__ == "__main__":
    build(LESSONS, C)
