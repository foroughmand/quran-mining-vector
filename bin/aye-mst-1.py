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

for s in range(1, 115):
#for s in range(36, 37):
	dots = loadAyeDot(s)
	INF = 1000000000
	sure_len = len(dots)
	maxk = sure_len

	A = [[INF for i in range(sure_len+1)] for k in range(maxk+1)]
	A[0][0] = 0
	P = [[-1 for i in range(sure_len+1)] for k in range(maxk+1)]
	for k in range(1, maxk+1):
		for i in range(1, sure_len + 1):
			#Fill A[k][i]: a[0] .. a[i-1]
			cost = 0.0
			for j in reversed(range(i)):
				for jj in range(j, i):
					#print >>sys.stderr, s, j+1, jj+1, i
					if dots[j][jj] > 0:
						cost += dots[j][jj] / math.sqrt( dots[j][j] * dots[jj][jj] ) #ayeLen[s][j+1] / ayeLen[s][jj+1]
				newCost = max(cost, A[k-1][j]) # / (i-j) / (i-j+1) * 2
				if A[k][i] > newCost:
					A[k][i] = newCost
					P[k][i] = j
	#for k in range(1, maxk+1):
	#	print >>sys.stderr, 'K=', k
	#	for i in range(1, sure_len + 1):
	#		print >>sys.stderr, A[k][i],
	#	print >>sys.stderr
	#print '\n'.join([' '.join(map(str, recP(P, k, sure_len))) for k in range(len(P))])
	for k in range(1, maxk+1):
		print s, k, A[k][sure_len], 
		print ' '.join(map(str, recP(P, k, sure_len)))
	sys.stdout.flush()


