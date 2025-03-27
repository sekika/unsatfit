#!/bin/sh
echo '=== autopep8'
autopep8 -i --aggressive ../unsatfit/*.py
autopep8 -i --aggressive ../swrcfit/*.py
autopep8 -i test_model.py

echo '=== mypy'
mypy ../unsatfit/_*.py

echo '=== flake8'
flake8 --ignore=E501,E741,W503 ../unsatfit/*.py
flake8 --ignore=E501,E741 ../swrcfit/index.py
