from util import *
import math

quran = loadQuranDic()

def recP(P, k, i):
	r = [] # [k, i]
	while k >= 0:
		r.insert(0, i)
		i = P[k][i]
		k -= 1
	return r

ayeLen = computeAyeLen(quran)

#for s in range(36, 37):
for s in range(1, 115):
	dots = loadAyeDot(s)
	f = open('../data/aye-dot-norm-'+str(s)+'.dat', 'w')
	for a in range(len(dots)):
		for a2 in range(len(dots)):
			if dots[a][a2] == 0:
				v = 0
			else:
				#v = dots[a][a2] / math.sqrt( ayeLen[s][a+1] * ayeLen[s][a2+1])
				v = dots[a][a2] / math.sqrt( dots[a][a] * dots[a2][a2] )
			print >>f, v, 
		print >>f
	f.close()

