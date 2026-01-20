#!/bin/sh
set -e
for f in ../*.py; do
  python3 "$f"
done
rm *.png
