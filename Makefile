all:

up:
	make test-swrc
	rsync -avz --delete --exclude swrcfit/data/__pycache__ --exclude swrcfit/img/swrc.png --exclude swrcfit/img/*.json --exclude swrcfit/data/server.txt -e ssh ./ swatch:unsatfit/
	ssh swatch "make swrc"
	w3m -dump https://seki.webmasters.gr.jp/swrc/

test:
	cd dev; ./test.sh

test-swrc:
	swrcfit/index.py -c
	swrcfit/index.py -t

format:
	cd dev; ./format.sh

deb:
	python3 setup.py --command-packages=stdeb.command bdist_deb
