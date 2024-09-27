'''
python getCorrelsByGene.py [AMR Gene Mat] [AMR Pheno Mat]
'''

from sys import argv
import math
import numpy as np

def parseMat(fNm):
	f = open(fNm)

	head = f.readline().strip('\n').split('\t')
	gHsh = {}
	for i in f:
		i = i.strip('\n').split('\t')
		gid = i[0]
		for j in range(1,len(i)):
			try:
				i[j] = float(i[j])
			except:
				i[j] = float('Nan')
		gHsh[gid] = i[1:]

	f.close()

	return head[1:], gHsh

def getGIDLst(genHsh, phnHsh):
	gid = {}
	for i in genHsh:
		gid[i] = 1
	for i in phnHsh:
		if i not in gid:
			gid[i] = 0
		gid[i] += 1

	dLst = []
	for i in gid:
		if gid[i] < 2:
			dLst.append(i)

	for i in dLst:
		del gid[i]

	return list(sorted(gid))

def makeArr(hsh, ind, gids):
	arr = []
	for i in gids:
		arr.append(hsh[i][ind])

	return arr

def getCorrel(arrG, arrP):
	dLst = []
	arrG_F = []
	arrP_F = []
	for i in range(0,len(arrG)):
		if math.isnan(arrG[i]) or math.isnan(arrP[i]):
			continue
		arrG_F.append(arrG[i])
		arrP_F.append(arrP[i])

	cM = np.corrcoef(arrG_F, arrP_F)
	corr = cM[0, 1]

	return corr

def getCorrels(genHsh, phnHsh, genOrd, phnOrd, gids):
	correls = {}

	for i in range(0,len(genOrd)):
		gen = genOrd[i]
		arrG = makeArr(genHsh, i, gids)
		correls[gen] = {}
		for j in range(0,len(phnOrd)):
			phn = phnOrd[j]
			arrP = makeArr(phnHsh, j, gids)

			corr = getCorrel(arrG, arrP)

			correls[gen][phn] = corr

	return correls

def main():
	genOrd, genHsh = parseMat(argv[1])
	phnOrd, phnHsh = parseMat(argv[2])

	gids = getGIDLst(genHsh, phnHsh)

	correls = getCorrels(genHsh, phnHsh, genOrd, phnOrd, gids)

	for i in correls:
		for j in correls[i]:
			if math.isnan(correls[i][j]):
				continue
			print('\t'.join( [ i, j, str(correls[i][j]) ] ))

if __name__ == '__main__':
	main()
