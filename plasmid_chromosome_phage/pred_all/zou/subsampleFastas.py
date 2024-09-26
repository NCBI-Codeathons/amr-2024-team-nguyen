'''
python subsampleFastas.py [fasta dir]
'''

from sys import argv
from glob import glob
import random

if argv[1][-1] != '/':
	argv[1] += '/'

def parseFasta(fNm):
	f = open(fNm)

	gen = ''
	seq = ''
	for i in f:
		i = i.strip('\n')
		if len(i) == 0:
			continue
		if i[0] == '>':
			gen = i
			continue
		seq += i

	f.close()

	return gen, seq

def parseFastas(dNm):
	fLst = glob(dNm + '*.fasta')
	cHsh = {}
	for i in fLst:
		gen, seq = parseFasta(i)
		if len(seq) < 5000:
			continue
		st = random.randint(0, len(seq)-5000)
		seq = seq[st:st+5000]
		cHsh[i] = [gen, seq]

	return cHsh

def printFasta(oNm, gen, seq):
	f = open(oNm, 'w')

	f.write(gen + '\n')
	f.write(seq + '\n')

	f.close()

def printFastas(cHsh):
	for i in cHsh:
		oNm = i[:-1*len('.fasta')] + '.sub.fasta'
		printFasta(oNm, cHsh[i][0], cHsh[i][1])


def main():
	cHsh = parseFastas(argv[1])
	printFastas(cHsh)

if __name__ == '__main__':
	main()