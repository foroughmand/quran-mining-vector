from util import *
import math
import sys
quran = loadQuranDic()

root, rootReff = loadRootReff()
rootIndex = listToDicIndex(root)
print >>sys.stderr, rootIndex

def computeAyeRoots(s, a):
	roots = []
	for w, swr in quran[s][a].items():
		for sw, r in swr.items():
			roots.append(rootIndex[r])
	return roots

rootCos = []
for r in range(len(root)):
	a = []
	for r2 in range(len(root)):
		a.append(1/math.sqrt(1+rootReff[r][r2]))
	rootCos.append(a)

ayeRoots = {}
for s, awswr in quran.items():
	ayeRoots[s] = {}
	for a, wswr in awswr.items():
		ayeRoots[s][a] = computeAyeRoots(s, a)

#ayeDot = {}
for s, awswr in quran.items():
	#ayeDot[s] = {}
	for a, wswr in awswr.items():
		#ayeDot[s][a] = {}
		print >>sys.stderr, 'D ', s, a
		for s2, awswr2 in quran.items():
			#ayeDot[s][a][s2] = {}
			for a2, wswr2 in awswr2.items():
				d = 0
				for r in ayeRoots[s][a]:
					for r2 in ayeRoots[s2][a2]:
						d += rootCos[r][r2] #1/(1+rootReff[r][r2])
				#ayeDot[s][a][s2][a2] = d
				print s, a, s2, a2, d

#for s, awswr in quran.items():
#	for a, wswr in awswr.items():
#		print '%d:%d'%(s,a),
#print
#
#for s, awswr in quran.items():
#	for a, wswr in awswr.items():
#		for s2, awswr in quran.items():
#			for a2, wswr in awswr.items():
#				print ayeDot[s][a][s2][a2],
#		print
