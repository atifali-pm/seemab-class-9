# Islamiat chapters-ocr — read this before using these files

**These PDFs have NO text layer.** They are the same page-image splits as `islamiat/chapters/`, copied here only so the tooling finds them at the conventional `chapters-ocr/compressed/` path.

Urdu OCR is not available on this machine: tesseract has only `eng` and `osd` installed (no `urd` pack) and the local `ocrmypdf` is broken. `pdftotext` on any of these returns nothing but the aggregator watermark.

**So read them as images, never with pdftotext:**

```
pdftoppm -jpeg -r 115 -f <page> -l <page> chapters-ocr/compressed/<bab>.pdf /tmp/pg
```

115 dpi is comfortably legible for Nastaliq. Use 240 dpi when a dense table row needs re-checking.

Page 1 of each bab file is the bab heading plus the first lesson's حاصلاتِ تعلّم (SLO) box, which is what the SLO-citation rule needs.

| File | Book pages | Pages |
|---|---|---|
| bab-00-front-matter | cover, title, فہرست | 4 |
| bab-01-quran-majeed-aur-hadees-e-nabvi | 1-11 | 11 |
| bab-02-imaniyat-o-ibadat | 12-40 | 29 |
| bab-03-seerat-un-nabi | 41-78 | 38 |
| bab-04-akhlaq-o-aadab | 79-93 | 15 |
| bab-05-husn-e-muamlat-o-muasharat | 94-111 | 18 |
| bab-06-mashaheer-e-islam | 112-151 | 40 |
| bab-07-islami-taleemat-aur-asr-e-hazir | 152-162 | 11 |
| bab-08-pairing-scheme-aur-model-paper | 163-166 | 4 |

Within a bab file: **file page = book page − (first book page of that bab) + 1.**
