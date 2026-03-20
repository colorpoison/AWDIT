#!/bin/bash

TOP_DIR="${1:-./top_level_folder}"

TOP_NAME=$(basename "$TOP_DIR")

OUTPUT_FILE="test_results/result_${TOP_NAME}.txt"

> "$OUTPUT_FILE"

for c in "$TOP_DIR"/*/; do
    [ -d "$c" ] || continue

    echo "Processing folder: $c"

    start_time=$(date +%s.%N)

    for file in "$c"*; do
        [ -f "$file" ] || continue

        timeout 30s target/release/awdit check -i mixed "$file" > /dev/null 2>&1
        if [ $? -eq 124 ]; then
            echo "Timeout on file: $file"
        fi
    done

    end_time=$(date +%s.%N)

    elapsed=$(echo "$end_time - $start_time" | bc)

    echo "$(basename "$c"): $elapsed seconds" >> "$OUTPUT_FILE"
done

echo "Done. Results saved to $OUTPUT_FILE"
