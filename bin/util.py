import sys, os, math

def loadQuranBasic(initQuran, addToQuran):
	quran = initQuran()
	for l in open('../../data/quranic-corpus-morphology-0.4.txt'):
		l = l.strip();
		if l == "" or l[0] == '#' or l[0] != '(':
			continue
		x = l.split('\t')
		loc = [int(a) for a in x[0][1:-1].split(':')]
		root = None
		for f in x[3].split('|'):
			nv = f.split(':')
			if len(nv) == 2 and nv[0] == 'ROOT':
				root = nv[1]
		s, a, w, sw = loc[0], loc[1], loc[2], loc[3]
		if root is not None:
			addToQuran(quran, s, a, w, sw, root)
	return quran

def loadQuranDic():
	def addToQuranDic(quran, s, a, w, sw, root):
		if s not in quran: quran[s] = {}
		if a not in quran[s]: quran[s][a] = {}
		if w not in quran[s][a]: quran[s][a][w] = {}
		quran[s][a][w][sw] = root
	return loadQuranBasic(lambda: {}, addToQuranDic)

def loadQuranTuple():
	def addToQuranTuple(quran, s, a, w, sw, root):
		quran[(s, a, w, sw)] = root
	return loadQuranBasic(lambda: {}, addToQuranTuple)


def loadRootReff():
	f = open('../data/root-reff.dat')
	l = f.readline().strip()
	rootByIndex = l.split()
	rootReff = []
	for l in f:
		x = l.strip().split()
		rootReff.append([float(v) for v in x])
	f.close()
	return rootByIndex, rootReff

def listToDicIndex(l):
	d = {}
	for i, v in enumerate(l):
		d[v] = i
	return d

def loadAyeDot(sure=None):
	f_sure_name = '../data/aye-dot-%d.dat' % (sure)

	if sure == None or not os.path.isfile(f_sure_name):
		f = open('../data/aye-dot2.dat')
		addr = [tuple(map(int, x.split(':'))) for x in f.readline().split()]
		dots = []
		if sure != None:
			for l, (s, a) in zip(f, addr):
				if s == sure:
					dots.append([float(x) for x, (s2, a2) in zip(l.strip().split(), addr) if s2 == sure])
			addr = [(s,a) for (s, a) in addr if s == sure]
		else:
			for l in f:
				dots.append([float(x) for x in l.strip().split()])
		f.close()
	if sure != None:
	  	if os.path.isfile(f_sure_name):
			f = open(f_sure_name)
			addr = [tuple(map(int, x.split(':'))) for x in f.readline().split()]
			dots = []
			for l in f:
				dots.append([float(x) for x in l.strip().split()])
			f.close()
		else:
			f = open(f_sure_name, 'w')
			print >>f, " ".join([':'.join(map(str, x)) for x in addr])
			for d in dots:
				print >>f, ' '.join(map(str, d))
			f.close()
	return dots

def loadAyeDotNormalized(sure=None):
	dots = loadAyeDot(sure)
	for i in range(len(dots)):
		for j in range(len(dots)):
			if dots[i][i] > 0 and dots[j][j] > 0:
				dots[i][j] /= math.sqrt(dots[i][i] * dots[j][j])
			else:
				dots[i][j] = 0.0
	return dots
	

def computeAyeLen(quran):
	ayeLen = {}
	for s, awswr in quran.items():
		ayeLen[s] = {}
		maxa = 1
		for a, wswr in awswr.items():
			cnt = 0
			for w, swr in wswr.items():
				for sw, r in swr.items():
					cnt += 1
			ayeLen[s][a] = cnt
			maxa = max(maxa, a)
		for a in range(1, maxa):
			if a not in ayeLen[s]:
				ayeLen[s][a] = 0
	return ayeLen

def sqr(x): return x * x

