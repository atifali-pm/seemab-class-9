#!/usr/bin/env bash
# Build and render Islamiat exam-03. Chrome headless only: wkhtmltopdf mangles Nastaliq.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
out="$here/../../exams/exam-03-bab1-2-3-4-6-7"
mkdir -p "$out"
python3 "$here/build.py"
for f in exam answer-key; do
  google-chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
    --print-to-pdf="$out/$f.pdf" "file://$here/$f.html" 2>/dev/null
  echo "wrote $out/$f.pdf ($(pdfinfo "$out/$f.pdf" | awk '/^Pages/{print $2}') pages)"
done
