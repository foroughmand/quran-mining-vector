from util import *
quran = loadQuranDic()
import numpy as np

sureArg = None
if len(sys.argv) >= 2:
	sureArg = int(sys.argv[1])

rootIndex = {}
for s, awswr in quran.items():
	for a, wswr in awswr.items():
		for w, swr in wswr.items():
			for sw, r in swr.items():
				if r not in rootIndex:
					rootIndex[r] = len(rootIndex)

rootGraph = np.zeros([len(rootIndex), len(rootIndex)])
for s, awswr in quran.items():
	if sureArg != None and s != sureArg: continue
	for a, wswr in awswr.items():
		prevRoot = None
		for w, swr in wswr.items():
			for sw, r in swr.items():
				if prevRoot is not None:
					#if r not in rootGraph[prevRoot]: rootGraph[prevRoot][r] = 0
					#if prevRoot not in rootGraph[r]: rootGraph[r][prevRoot] = 0
					#rootGraph[r][prevRoot] = rootGraph[prevRoot][r] += 1
					rI, prI = rootIndex[r], rootIndex[prevRoot]
					if rI == prI: continue
					rootGraph[rI][prI] -= 1
					rootGraph[prI][rI] -= 1
					rootGraph[rI][rI] += 1
					rootGraph[prI][prI] += 1
				prevRoot = r

B = np.linalg.pinv(rootGraph)
for i, v in enumerate(rootIndex):
	print v,
print
for i in range(len(rootGraph)):
	for j in range(len(rootGraph)):
		print rootGraph[i,i]+rootGraph[j,j]-2*rootGraph[i,j],
	print
