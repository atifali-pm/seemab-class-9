#!/usr/bin/env bash
# Render an RTL Urdu/Arabic exam HTML file to PDF with Chrome headless.
# Never use wkhtmltopdf for these papers: it cannot shape Nastaliq.
set -euo pipefail
in="$1"
out="${2:-${in%.html}.pdf}"
google-chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer --print-to-pdf="$out" "$in"
echo "$out"
