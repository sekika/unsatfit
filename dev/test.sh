#!/bin/sh
# Change to this directory
cd `echo $0 | sed -e 's/[^/]*$//'`
echo '=== test SWRC Fit'
./test.py

echo '=== test unsatfit models'
./test_model.py -n 5
