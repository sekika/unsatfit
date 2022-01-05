#!/bin/sh
# Change to this directory
cd `echo $0 | sed -e 's/[^/]*$//'`
echo 'test'
./test.py

echo 'flake8'
flake8 ../unsatfit/unsatfit.py | sed -e 's/^.*unsatfitu\///' | grep -v E501

# https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/
cd ..
python3 setup.py sdist
python3 setup.py bdist_wheel
twine check dist/*

