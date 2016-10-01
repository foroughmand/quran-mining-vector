from util import *
import sys
quran = loadQuranDic()

for s, awswr in quran.items():
	for a, wswr in awswr.items():
		for w, swr in wswr.items():
			for sw, r in swr.items():
				print s, a, w, sw, r
