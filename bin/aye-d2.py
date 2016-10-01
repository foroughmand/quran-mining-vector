from util import *
import math

quran = loadQuranDic()
ayeLen = computeAyeLen(quran)

def sign(x):
	if x < 0: return -1
	if x > 0: return 1
	return 0

#for s in range(1, 115):
for s in range(36, 37):
	dots = loadAyeDotNormalized(s)
	sure_len = len(dots)
	d = [[0 for j in range(sure_len+1)] for i in range(sure_len)]
	for i in range(sure_len):
		s = 0
		for j in range(i, sure_len+1):
			ts = 0
			for jj in range(i, j):
				ts += dots[j-1][jj]
			s += ts
			d[i][j] = s

	d1 = [[0 for j in range(sure_len+1)] for i in range(sure_len)]
	d2 = [[0 for j in range(sure_len+1)] for i in range(sure_len)]
	for i in range(sure_len):
		for j in range(i, sure_len):
			d1[i][j] = d[i][j+1] - d[i][j]
		for j in range(i+1, sure_len):
			d2[i][j] = d[i][j-1] - 2 * d[i][j] + d[i][j+1]

	for i in range(sure_len):
		print >>sys.stderr, ' '.join(['{:.2f}'.format(dd) for dd in d[i] ])
	print >>sys.stderr 
	print >>sys.stderr,  'D1:'
	for i in range(sure_len):
		print >>sys.stderr,  ' '.join(['{:.2f}'.format(dd) for dd in d1[i] ])
	print >>sys.stderr 
	print >>sys.stderr,  'D2:'
	for i in range(sure_len):
		print >>sys.stderr,  ' '.join(['{:.2f}'.format(dd) for dd in d2[i] ])
	
	#D2[i,j]: For ayes [i, .., j-1 j) who good is to choose j-1 as the last element. Better = more negative
	#A[i]: For ayes [0, .., i), what is the best partitioning, such that i-1 is the last element of the last partition
	INF = 1000000000
	A = [INF for i in range(sure_len)]
	A[0] = 0
	P = [-1 for i in range(sure_len)]
	minA, minAP = 0, -1
	for i in range(sure_len):
		for j in range(i):
			if A[i] > A[j] + sign(d2[j][i]):
				A[i] = A[j] + sign(d2[j][i])
				P[i] = j
		if minA > A[i]:
			minA = A[i]
			minAP = i
	print >>sys.stderr, 'A:'
	for i in range(sure_len):
		print >>sys.stderr, ' ', i, A[i], P[i], A[P[i]], d2[P[i]][i]

	print >>sys.stderr, P
	
	L = [sure_len]
	##p = sure_len-2
	p = minAP
	while p >= 0:
		L.insert(0, p)
		p = P[p]

	print ' '.join(['{:d}'.format(l+1) for l in  L])

