VERSION := $(shell python3 -c "from unsatfit import __version__; print(__version__)")
PYTHON := python3
DISTDIR := dist
PKGDIR := $(DISTDIR)/unsatfit-$(VERSION)

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

sdist: $(DISTDIR)/unsatfit-$(VERSION).tar.gz

$(DISTDIR)/unsatfit-$(VERSION).tar.gz:
	@mkdir -p $(DISTDIR)
	python3 -m build --sdist --outdir $(DISTDIR)

deb: sdist
	@mkdir -p $(PKGDIR)
	tar -xzf $(DISTDIR)/unsatfit-$(VERSION).tar.gz -C $(DISTDIR)
	fpm -s dir -t deb \
	    --name unsatfit \
	    --version $(VERSION) \
	    --license MIT \
	    --maintainer "Katsutoshi Seki" \
	    --description "Fit soil water retention and unsaturated hydraulic conductivity functions" \
	    --prefix /usr/local \
	    $(PKGDIR)
