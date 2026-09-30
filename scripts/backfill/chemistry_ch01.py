# -*- coding: utf-8 -*-
"""Chemistry Chapter 1: Nature of Chemistry in Science. Her book p7 to 14."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import build

C = "#1e7a4a"
S = "chemistry"

LESSONS = [
{
 "subject": S, "chapter": 1, "ref": "1.1", "slug": "chem-ch01-definition",
 "summary": "What chemistry actually studies, the book's definition word for word, and what green chemistry means.",
 "note": """
<h1><span class="emoji">⚗️</span> Chemistry Ch 1.1: Definition of Chemistry</h1>
<div class="sub">Chapter 1, Nature of Chemistry in Science &middot; kitab ke page 7 se 14</div>
<p>Ek sawal se shuru karte hain. Aap ke ghar mein doodh rakha reh jaye to kharab ho jata hai. Loha baarish mein
rakha rahe to zang lag jata hai. Roti tawe par pak kar bhoori ho jati hai. <b>Teenon mein ek hi cheez ho rahi hai.</b>
Kya? Jawab is safhay par hai.</p>
<div class="box def"><span class="t"><span class="emoji">📖</span> Kitab ki definition, yehi likhni hai</span>
Chemistry wo science hai jo <b>kainaat ke maddon (materials of the universe)</b> ka mutalea karti hai aur un
tabdeeliyon ka jo un mein aati hain.<br>
Ye teen cheezon se taalluq rakhti hai: maddey ki <b>composition</b> (kis cheez se bana hai), <b>structure</b>
(kaise juda hua hai), aur <b>properties</b> (wo karta kya hai), aur saath hi maddey aur energy mein aane wali
<b>tabdeeliyan</b>.</div>
<div class="box trick"><span class="t"><span class="emoji">🧠</span> Yaad rakhne ka tareeqa</span>
Physics poochhti hai cheez <b>harkat</b> kaise karti hai. Biology poochhti hai cheez <b>zinda</b> kaise rehti hai.
Chemistry poochhti hai cheez <b>badalti</b> kaise hai, aur badalne ke baad wo kya ban jati hai.<br>
Doodh, loha aur roti, teenon mein maddah badal raha hai. Isi liye teenon Chemistry hain.</div>
<div class="box def"><span class="t"><span class="emoji">🌿</span> Green Chemistry</span>
Kitab ek aur istilah deti hai: <b>green chemistry</b>. Ye chemistry ki wo shakl hai jo <b>khatarnaak maddon
(hazardous substances) ka istemal kam</b> karti hai.<br>
Yani maqsad sirf ye nahin ke cheez ban jaye, balke ye bhi ke banate waqt zameen aur hawa ko nuqsan kam se kam ho.</div>
<div class="box eg"><span class="t"><span class="emoji">✏️</span> Teen lafz jo alag alag hain</span>
<b>Composition:</b> paani hydrogen aur oxygen se bana hai.<br>
<b>Structure:</b> un do hydrogen aur ek oxygen ka aapas mein jurne ka andaz.<br>
<b>Properties:</b> paani sau digree par ubalta hai aur cheezon ko ghol leta hai.<br>
Sawal mein teenon ke naam aa sakte hain, is liye teenon ka farq yaad rakhein.</div>
<div class="box quiz"><span class="t"><span class="emoji">🧪</span> Quiz</span>
<ol class="q">
<li>Define <b>chemistry</b> in the words of your book, and name the three things about matter that it studies.</li>
<li>What is <b>green chemistry</b>? Give one reason why it matters.</li>
</ol></div>
<!--KEY 1. Chemistry is the science that investigates the materials of the universe and the changes they undergo.
The three: composition, structure and properties (of matter), plus changes in matter and energy.
2. Green chemistry reduces the use of hazardous substances. It matters because it cuts harm to health and the
environment while still producing what is needed. -->
""",
 "script": """السلام علیکم سیماب۔ آج Chemistry کے پہلے باب کی دہرائی ہے۔ لیکن پہلے ایک سوال۔

آپ کے گھر میں دودھ رکھا رہ جائے تو خراب ہو جاتا ہے۔ لوہے کا دروازہ بارش میں رہے تو اس پر زنگ لگ جاتا ہے۔ اور روٹی توے پر پک کر بھوری ہو جاتی ہے۔

اب سوچیے۔ یہ تین بالکل الگ الگ چیزیں لگتی ہیں۔ دودھ، لوہا، روٹی۔ لیکن تینوں میں ایک ہی بات ہو رہی ہے۔ کیا؟

جواب یہ ہے کہ تینوں میں مادہ خود بدل رہا ہے۔ دودھ دودھ نہیں رہا، لوہا لوہا نہیں رہا، آٹا آٹا نہیں رہا۔ اور جب مادہ بدلتا ہے، وہیں Chemistry شروع ہو جاتی ہے۔

اب کتاب کی definition سنیے، یہی امتحان میں لکھنی ہے۔ Chemistry وہ science ہے جو کائنات کے مادوں کا مطالعہ کرتی ہے، اور ان تبدیلیوں کا جو ان میں آتی ہیں۔

اور یہ تین چیزوں کو دیکھتی ہے۔ پہلی، composition، یعنی چیز بنی کس سے ہے۔ دوسری، structure، یعنی وہ چیزیں آپس میں جڑی کیسے ہوئی ہیں۔ اور تیسری، properties، یعنی وہ چیز کرتی کیا ہے۔

ایک مثال سے تینوں صاف ہو جائیں گے۔ پانی لیجیے۔ اس کی composition یہ ہے کہ وہ hydrogen اور oxygen سے بنا ہے۔ اس کی structure یہ ہے کہ دو hydrogen اور ایک oxygen کس انداز میں جڑے ہوئے ہیں۔ اور اس کی properties یہ ہیں کہ وہ سو ڈگری پر ابلتا ہے اور چیزوں کو گھول لیتا ہے۔

امتحان میں یہ تینوں لفظ اکٹھے بھی پوچھے جا سکتے ہیں، اس لیے ان کا فرق یاد رکھیں۔

اب ایک اور لفظ جو کتاب دیتی ہے، green chemistry۔ یہ chemistry کی وہ شکل ہے جو خطرناک مادوں کا استعمال کم کرتی ہے۔

سوچیے اس کا مطلب کیا ہے۔ پہلے صرف یہ دیکھا جاتا تھا کہ چیز بن گئی یا نہیں۔ اب یہ بھی دیکھا جاتا ہے کہ بناتے وقت ہوا اور زمین کو کتنا نقصان پہنچا۔ یہ نئی سوچ ہے اور اسی کا نام green chemistry ہے۔

تو آج کی دو باتیں۔ ایک، Chemistry مادے کی تبدیلی کا علم ہے، اور وہ composition، structure اور properties دیکھتی ہے۔ اور دو، green chemistry کا مطلب ہے خطرناک مادے کم کرنا۔

آپ کے دو quiz سوال صفحے پر ہیں۔ خدا حافظ۔
""",
},
]

if __name__ == "__main__":
    build(LESSONS, C)
