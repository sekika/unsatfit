all: format test

test:
	cd ..; python3 -m pip install -e . --use-pep517
	./test.sh

format:
	./format.sh
