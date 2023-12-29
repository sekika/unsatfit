debfile = python3-unsatfit_latest_all.deb

all:

up:
	make test-swrc
	rsync -avz --delete --exclude swrcfit/data/__pycache__ --exclude swrcfit/img/swrc.png --exclude swrcfit/img/*.json --exclude swrcfit/data/server.txt -e ssh ./ swatch:unsatfit/
	ssh swatch "make swrc"
	w3m -dump https://seki.webmasters.gr.jp/swrc/

test:
	cd dev; ./test.py

test-swrc:
	swrcfit/index.py -c
	swrcfit/index.py -t

format:
	cd unsatfit; autopep8 -i unsatfit.py
	cd swrcfit; autopep8 -i *.py
	cd swrcfit/data; autopep8 -i *.py
	- flake8 unsatfit/unsatfit.py | grep -v "E501"
	- flake8 swrcfit/index.py | grep -v "E501"

deb:
	python3 setup.py --command-packages=stdeb.command bdist_deb
	cd deb_dist; rm -f ${debfile}; cp `ls *.deb | tail -n 1` $(debfile)
