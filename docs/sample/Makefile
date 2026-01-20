all:
	cp clay2362/*.csv .
	./VGM.py
	mv VG.svg VG-2362.svg
	cp gilat/*.csv .
	./VGM.py
	mv VG.svg VG-gilat.svg
	./KBC.py
	./DVC.py
	./DBC.py
	./PE.py
	./multi.py
	./contour.py
	rm *.csv
	git add .; git commit -m up; git push

