#!/bin/sh
# Change to this directory
cd `echo $0 | sed -e 's/[^/]*$//'`
echo '=== test'
./test.py

echo '=== autopep8'
autopep8 -i --aggressive ../unsatfit/*.py

echo '=== package'
# https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/
cd ..
python3 setup.py sdist
python3 setup.py bdist_wheel
twine check dist/*

echo '=== mypy'
mypy ../unsatfit/_*.py

echo '=== flake8'
flake8 --ignore=E501,E741 ../unsatfit/*.py
