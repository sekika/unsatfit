all:
	cp clay2362/*.csv .
	./VGM.py
	mv VG.png VG-2362.png
	cp gilat/*.csv .
	./VGM.py
	mv VG.png VG-gilat.png
	./KBC.py
	./DVC.py
	./DBC.py
	./PE.py
	./multi.py
	./contour.py
	rm *.csv
	git add .; git commit -m up; git push

