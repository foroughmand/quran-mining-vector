DATA= ../data/root-reff.dat  ../data/quran-roots.dat ../data/aye-dot2.dat ../data/root-reff-36.dat ../data/aye-mst-1-36.dat ../data/aye-mst-2.dat 
DATA_OLD=../data/quran-roots.dat
APP= build-aye-dot

ALL: $(APP) $(DATA)


build-aye-dot: build-aye-dot.cc
	g++ build-aye-dot.cc -o build-aye-dot -O2


../data/root-reff.dat: build-root-reff.py
	python build-root-reff.py > ../data/root-reff.dat

../data/root-reff-36.dat: build-root-reff.py
	python build-root-reff.py 36 > ../data/root-reff-36.dat

../data/aye-dot.dat: build-aye-dot.py ../data/root-reff.dat
	python build-aye-dot.py > ../data/aye-dot.dat

../data/quran-roots.dat:  build-quran-roots.py
	python build-quran-roots.py > ../data/quran-roots.dat

../data/aye-dot2.dat: build-aye-dot ../data/root-reff.dat
	./build-aye-dot > ../data/aye-dot2.dat

../data/aye-mst-1-36.dat: aye-mst-1.py ../data/aye-dot2.dat ../data/aye-dot-36.dat
	python aye-mst-1.py > ../data/aye-mst-1-36.dat

../data/aye-mst-2.dat: aye-mst-1.py ../data/aye-dot-36.dat
	python aye-mst-1.py > ../data/aye-mst-2.dat 2>e

../data/aye-dot-norm-36.dat: build-aye-norm-dot-1.py
	python build-aye-norm-dot-1.py 
