'''
python mergePreds.py [order] [preds]
'''

from sys import argv

def parseFile(fNm, header=False):
	f = open(fNm)

	if header:
		f.readline()

	arr = []
	for i in f:
		arr.append(i.strip('\n'))

	f.close()

	return arr

def printTab(ordr, pred):
	for i in range(0,len(ordr)):
		bPre = float(pred[i])
		if bPre > 0.5:
			bPre = 'PL'
		else:
			bPre = 'CH'
		arr = [ordr[i].replace('.sub.fasta.6.kmrs', ''), pred[i], bPre]
		print('\t'.join(arr))

def main():
	ordr = parseFile(argv[1])
	pred = parseFile(argv[2], True)

	printTab(ordr, pred)
	

if __name__ == '__main__':
	main()

