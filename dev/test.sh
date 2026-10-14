#!/bin/sh
set -eu

# Change to this directory
cd "$(dirname "$0")"
echo '=== test SWRC Fit'
./test.py

echo '=== test unsatfit models'
./test_model.py -n 5
