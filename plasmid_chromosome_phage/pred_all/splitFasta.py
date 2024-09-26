'''
python splitFasta.py [fasta file]
'''

from sys import argv
import os

def addSeq(fHsh, cGen, cSeq):
	if len(cSeq) < 5000:
		return
	if cGen != '' and cSeq != '':
		fHsh[cGen[1:-1]] = cSeq

def parseFasta(fNm):
	f = open(fNm)

	currGen = ""
	currSeq = ""
	fHsh = {}
	for i in f:
		i = i
		if i[0] == '>':
			addSeq(fHsh, currGen, currSeq)
			currGen = i
			currSeq = ''
			continue
		currSeq += i

	addSeq(fHsh, currGen, currSeq)

	f.close()

	return fHsh

def printFasta(fHsh, fNm):
	pref = fNm + '.split/'
	if not os.path.exists(pref):
		os.mkdir(pref)
	cnt = 0
	repLst = "\\/:*?\"<>|\n"
	for i in fHsh:
		nm = i.split(' ')[0] + '_split_seq_' + str(cnt)
		for j in repLst:
			nm = nm.replace(j, '_', len(nm))
		f = open(pref + nm + '.fasta', 'w')
		f.write('>' + i + '\n' + fHsh[i])
		cnt += 1

def main():
	fHsh = parseFasta(argv[1])
	printFasta(fHsh, argv[1])

if __name__ == '__main__':
	main()
