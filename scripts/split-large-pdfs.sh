#!/usr/bin/env bash
# Split OCR PDF chapters that exceed a size limit into multiple parts.
# Uses Ghostscript (gs) to extract page ranges.
#
# Usage: ./scripts/split-large-pdfs.sh [MAX_MB] [DIR ...]
#   MAX_MB  — maximum file size in MB (default: 10)
#   DIR     — directories to scan (default: all */chapters-ocr/ dirs)
#
# Example:
#   ./scripts/split-large-pdfs.sh 10 biology/chapters-ocr physics/chapters-ocr

set -euo pipefail

MAX_MB="${1:-10}"
shift 2>/dev/null || true
MAX_BYTES=$((MAX_MB * 1024 * 1024))

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Collect directories to scan
if [[ $# -gt 0 ]]; then
    DIRS=("$@")
else
    DIRS=()
    for d in "$REPO_ROOT"/*/chapters-ocr; do
        [[ -d "$d" ]] && DIRS+=("$d")
    done
fi

if [[ ${#DIRS[@]} -eq 0 ]]; then
    echo "No chapters-ocr directories found."
    exit 0
fi

split_pdf() {
    local pdf="$1"
    local filename basename dir
    dir="$(dirname "$pdf")"
    filename="$(basename "$pdf")"
    basename="${filename%.pdf}"

    local size
    size=$(stat -c%s "$pdf")
    if [[ $size -le $MAX_BYTES ]]; then
        return
    fi

    local total_pages
    total_pages=$(pdfinfo "$pdf" 2>/dev/null | awk '/^Pages:/{print $2}')
    if [[ -z "$total_pages" || "$total_pages" -le 1 ]]; then
        echo "  SKIP $filename — cannot determine page count or only 1 page"
        return
    fi

    local size_mb
    size_mb=$(awk "BEGIN{printf \"%.1f\", $size/1024/1024}")
    echo "  $filename (${size_mb} MB, ${total_pages} pages) — splitting..."

    # Estimate pages per part based on average page size
    local avg_page_bytes pages_per_part
    avg_page_bytes=$((size / total_pages))
    pages_per_part=$((MAX_BYTES / avg_page_bytes))
    # Ensure at least 1 page per part, and leave some margin (90% of limit)
    pages_per_part=$(( (MAX_BYTES * 9 / 10) / avg_page_bytes ))
    [[ $pages_per_part -lt 1 ]] && pages_per_part=1

    local part=1 start=1 end
    local parts_created=()

    while [[ $start -le $total_pages ]]; do
        end=$((start + pages_per_part - 1))
        [[ $end -gt $total_pages ]] && end=$total_pages

        local part_file="${dir}/${basename}-part${part}.pdf"

        gs -sDEVICE=pdfwrite \
           -dNOPAUSE -dBATCH -dQUIET \
           -dFirstPage="$start" -dLastPage="$end" \
           -sOutputFile="$part_file" \
           "$pdf"

        local part_size part_size_mb
        part_size=$(stat -c%s "$part_file")
        part_size_mb=$(awk "BEGIN{printf \"%.1f\", $part_size/1024/1024}")

        # If this part still exceeds the limit and has more than 1 page, re-split with fewer pages
        if [[ $part_size -gt $MAX_BYTES && $((end - start)) -gt 0 ]]; then
            rm "$part_file"
            # Reduce pages_per_part for this chunk
            local chunk_pages=$((end - start + 1))
            local new_ppp=$((chunk_pages * MAX_BYTES * 9 / 10 / part_size))
            [[ $new_ppp -lt 1 ]] && new_ppp=1

            local sub_start=$start
            while [[ $sub_start -le $end ]]; do
                local sub_end=$((sub_start + new_ppp - 1))
                [[ $sub_end -gt $end ]] && sub_end=$end

                part_file="${dir}/${basename}-part${part}.pdf"
                gs -sDEVICE=pdfwrite \
                   -dNOPAUSE -dBATCH -dQUIET \
                   -dFirstPage="$sub_start" -dLastPage="$sub_end" \
                   -sOutputFile="$part_file" \
                   "$pdf"

                part_size=$(stat -c%s "$part_file")
                part_size_mb=$(awk "BEGIN{printf \"%.1f\", $part_size/1024/1024}")
                echo "    -> ${basename}-part${part}.pdf (pages ${sub_start}-${sub_end}, ${part_size_mb} MB)"
                parts_created+=("$part_file")

                part=$((part + 1))
                sub_start=$((sub_end + 1))
            done
        else
            echo "    -> ${basename}-part${part}.pdf (pages ${start}-${end}, ${part_size_mb} MB)"
            parts_created+=("$part_file")
            part=$((part + 1))
        fi

        start=$((end + 1))
    done

    # Verify: total pages in parts should equal original
    local verify_pages=0
    for pf in "${parts_created[@]}"; do
        local pp
        pp=$(pdfinfo "$pf" 2>/dev/null | awk '/^Pages:/{print $2}')
        verify_pages=$((verify_pages + pp))
    done

    if [[ $verify_pages -eq $total_pages ]]; then
        echo "    OK — ${#parts_created[@]} parts, all ${total_pages} pages accounted for"
        # Remove original
        rm "$pdf"
        echo "    Removed original: $filename"
    else
        echo "    WARNING — page count mismatch (original: $total_pages, parts total: $verify_pages)"
        echo "    Keeping original file. Please verify manually."
    fi
}

for dir in "${DIRS[@]}"; do
    # Resolve relative to repo root
    [[ "$dir" != /* ]] && dir="$REPO_ROOT/$dir"

    if [[ ! -d "$dir" ]]; then
        echo "SKIP: $dir (not a directory)"
        continue
    fi

    echo "Scanning: $dir (limit: ${MAX_MB} MB)"

    # Process files that exceed the limit (skip already-split part files)
    while IFS= read -r -d '' pdf; do
        basename_check="$(basename "$pdf")"
        # Skip files that are already parts from a previous split
        if [[ "$basename_check" =~ -part[0-9]+\.pdf$ ]]; then
            continue
        fi
        split_pdf "$pdf"
    done < <(find "$dir" -maxdepth 1 -name '*.pdf' -size +"${MAX_MB}M" -print0 | sort -z)

    echo ""
done

echo "Done."
