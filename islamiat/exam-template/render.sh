#!/usr/bin/env bash
# Render an Urdu/RTL Islamiat paper to PDF.
# wkhtmltopdf CANNOT do this: its QtWebKit mangles Nastaliq letter shaping into
# unreadable garbage (verified 2026-09-10). Chrome headless shapes it correctly.
set -euo pipefail
[ $# -eq 1 ] || { echo "usage: render.sh <file.html>"; exit 1; }
in="$1"; out="${in%.html}.pdf"
google-chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --print-to-pdf="$out" "$in"
echo "wrote $out ($(pdfinfo "$out" | awk '/^Pages/{print $2}') pages)"
