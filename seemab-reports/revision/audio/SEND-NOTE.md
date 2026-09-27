# Audio lessons, send note

## Voice, as of 2026-09-25

Atif compared five renderings of the same passage and chose **`ur-PK-UzmaNeural`**, a native Pakistani
female voice, reading **Urdu script**. His reasoning: Roman is easier for Seemab to read, Urdu is easier
for her to listen to. So the notes stay Roman and the audio goes native Urdu. Full rule in the
`aasan-notes-format` memory.

Every script exists twice: `<stem>-STORY-script.txt` is the original Roman, and
`<stem>-STORY-script-urdu.txt` is the Urdu that is actually spoken. Technical terms stay in Latin letters
inside the Urdu sentence so they keep their English pronunciation. Pace is `-20%` for Maths, `-10%` for
Islamiat.

## SENT to Shumail 2026-09-25, evening

Send the covering message first, then these in order, because each ends with a hook into the next.

1. math-u03-part3B-URDU-audio-2026-09-25.mp3 (6:20)
2. math-u03-part3C-URDU-audio-2026-09-25.mp3 (7:17)
3. islamiat-bab3b-husn-e-sulook-URDU-audio-2026-09-25.mp3 (6:20)
4. islamiat-bab3b-andaz-e-tarbiyat-URDU-audio-2026-09-25.mp3 (6:17)

Twenty six minutes in total.

## Still on the old voice, not converted yet

`phys-u07-part7A`, `phys-u07-part7B`, `math-u03-part3A`, `chem-ch10-part1`, `chem-ch10-part2`. These are
the `-STORY-audio-` files, read by `en-IN-NeerjaNeural` from the Roman scripts. Convert them to Uzma
before they go out.

**The two Physics ones are also blocked on her attempt.** Physics Paper 17 went out 25 September at 12:07
with the key held. Quiz question 2 on that paper is the measuring cylinder, 120 g empty and 160 g with
50 mL. The Part 7A note gives her the question but does not work it out; the Part 7A audio does work it
out and says 0.8 g/mL and 800 kg/m³. Do not send it until her attempt is in.

## Covering message

Assalam o alaikum Seemab beta.

Ye aaj ke chaaron notes ke audio lessons hain. Is dafa awaaz nayi hai, poori Urdu mein, taake sunne mein
asaan lage. Har lesson 6 se 7 minute ka hai.

Ye kitab parh kar sunane wali cheez nahin hai. Har lesson ek kahani ki tarah hai, ghar ki asaan misalon ke
saath. Har audio ek sawal se shuru hota hai, aur aakhir mein usi sawal ka jawab aap khud de deti hain.

Sunne ka tareeqa: notes saamne rakhne ki zaroorat nahin. Chalte phirte, khana khate hue, ya sone se pehle
sunn lein. Jo baat audio mein samajh aa jaye, us ke baad wohi notes parhna bohat asaan ho jata hai.

Tarteeb ye hai:
1. Maths Unit 3 Part 3B: Associative aur Distributive laws
2. Maths Unit 3 Part 3C: Venn diagram wale word problems
3. Islamiat Bab 3(ب): Khawateen se husn e sulook
4. Islamiat Bab 3(ب): Nabi kareem ﷺ ka andaz e tarbiyat

Ek ke baad doosra suniye, kyunke har lesson ke aakhir mein agle sabaq ka chhota sa hint hai. Maze se
suniye.

## What actually went, 25 September evening

Urdu set (`ur-PK-UzmaNeural`, Urdu script): 3B 6:20, 3C 7:17, husn-e-sulook 6:20, andaz-e-tarbiyat 6:17.
English set (`en-IN-NeerjaNeural`, English script): 3B 6:59, 3C 7:47, husn-e-sulook 7:23,
andaz-e-tarbiyat 7:42. Each set went with its own covering message, files in listening order.

The English scripts are `<stem>-STORY-script-english.txt`. They are the same lesson, same stories, same
book references and the same exam-technique close, written in English rather than translated line by line.
She was told to use the Urdu one to understand and the English one the day before a paper, because the
paper is answered in English.

**Delivery lesson learned:** the Urdu four were first sent with `send_audio_message` and arrived as
WhatsApp voice notes, carrying Atif's own avatar and with no way for her to save them. He asked for MP3
files instead, so all eight went again through `send_file`. The rule is now in the `audio-as-mp3-file`
memory: always `send_file`, never a voice note. The stray voice notes are still in her chat and she was
told to ignore them.
