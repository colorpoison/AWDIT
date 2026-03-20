#!/bin/bash

BASE_DIR="histories/FinalTest"

for dir in "$BASE_DIR"/*/; do
    folder_name=$(basename "$dir")
    
    echo "Running benchmark for: $folder_name"
    ./run_awdit_benchmark.sh "$dir"
done
