'''
python makeMatrix.py [kmc out dir] [out pref]
'''

from sys import argv
from glob import glob
import os

cDir = os.getcwd()

if argv[1][-1] != '/':
	argv[1] += '/'

def getKmerOrder():
	f = open(cDir + '/zou/zou-plasmid-prediction/kmer_order.csv')

	cnt = 0
	kmerOrder = {}
	for i in f:
		i = i.strip('\n')
		kmerOrder[i] = cnt
		cnt += 1

	f.close()

	return kmerOrder

def parseKMC(fNm, kmerOrder):
	f = open(fNm)

	arr = ['0'] * len(kmerOrder)
	for i in f:
		i = i.strip('\n').split('\t')
		ind = kmerOrder[i[0]]
		arr[ind] = i[1]

	f.close()

	return arr

def parseKMCs(kDir, kmerOrder):
	fLst = glob(kDir + '*.kmrs')

	kHsh = {}
	for i in fLst:
		kHsh[os.path.basename(i)] = parseKMC(i, kmerOrder)

	return kHsh

def printMatrix(oPref, kHsh, kmerOrder):
	oOrd = open(oPref + '.order.lst', 'w')
	oMat = open(oPref + '.mat', 'w')

	arr = []
	for i in range(0,len(kmerOrder)):
		arr.append(str(i))
	oMat.write(',' + ','.join(arr) + '\n')

	for i in kHsh:
		oOrd.write(i + '\n')
		oMat.write(',' + ','.join(kHsh[i]) + '\n')

	oOrd.close()
	oMat.close()

def main():
	kmerOrder = getKmerOrder()
	kHsh = parseKMCs(argv[1], kmerOrder)
	printMatrix(argv[2], kHsh, kmerOrder)

if __name__ == '__main__':
	main()