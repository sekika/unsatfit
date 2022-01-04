#!/bin/sh
# Change to this directory
cd `echo $0 | sed -e 's/[^/]*$//'`
echo 'flake8'
flake8 ../unsatfit/unsatfit.py | sed -e 's/^.*unsatfitu\///' | grep -v E501
# Check description
# echo "Checking README.rst."
# python3 ../setup.py --long-description | rst2html.py > /dev/null

# https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/
cd ..
python3 setup.py sdist
python3 setup.py bdist_wheel
twine check dist/*

