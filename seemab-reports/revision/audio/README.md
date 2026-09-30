# Recorded lessons

**The audio files in here are not in git.** Only the scripts are.

Each recording is built from its own script, and those are tracked:

    <topic>-STORY-script-urdu.txt      the script, in Urdu, with English technical terms
    <topic>-URDU-audio-<date>.mp3      the render        (not in git)
    ogg/<topic>-<date>.ogg             the WhatsApp voice note (not in git)

To rebuild one:

    python3 scripts/tts_mixed.py <topic>-STORY-script-urdu.txt out.mp3
    ffmpeg -i out.mp3 -af "loudnorm=I=-16:TP=-1.5:LRA=11" \
      -c:a libopus -b:a 64k -vbr on -ar 24000 -ac 1 ogg/<topic>-<date>.ogg

`scripts/tts_mixed.py` reads Quranic ayat and Arabic hadith in an Arabic voice
(`ar-SA-HamedNeural`) and everything else in Urdu (`ur-PK-UzmaNeural`). Mark a
passage `{{ar}} ... {{/ar}}` to force Arabic; otherwise it is detected from the
harakat, since fully vocalised text is Quranic and Urdu prose is not.

Why they are out of git: recording the whole syllabus is roughly a gigabyte of
audio, and this repository is public and already large. The scripts are a few
hundred kilobytes and regenerate everything. The website uploads the audio to
Cloudflare Pages straight from this folder, so nothing about delivery changes.

**These files only exist on this machine.** They are not backed up by the repo.
