'''
python getF1.py [ground truth] [models directory] [Antibiotic Abbr]
'''

from sys import argv
from sklearn.metrics import f1_score

if argv[2][-1] != '/':
	argv[2] += '/'

def getAbbr(fNm):
	f = open(fNm)

	abrHsh = {}
	for i in f:
		i = i.strip('\n').split('\t')
		abrHsh[i[1]] = i[0]

	f.close()

	return abrHsh

def getExpectedF1(dNm, abrHsh):
	f = open(dNm + 'all.f1.tab')
	f.readline()

	expF1Hsh = {}
	for i in f:
		i = i.strip('\n').split('\t')
		spc = i[0].lower().replace('_',' ')
		ab = abrHsh[i[1]].replace('_', ' ', len(abrHsh[i[1]]))
		f1 = i[2]
		ci0 = i[3]
		ci1 = i[4]

		if spc not in expF1Hsh:
			expF1Hsh[spc] = {}
		expF1Hsh[spc][ab] = [f1, ci0, ci1]

	f.close()

	return expF1Hsh

def parsePredsWithASTs(fNm):
	f = open(fNm)
	f.readline()

	trPrHsh = {}

	for i in f:
		i = i.strip('\n').split('\t')
		gid = i[0]
		spc = i[1].lower()
		ab = i[2]
		pr = i[3]
		tr = i[4]

		if tr == 'not defined':
			continue

		# print pr,

		if pr[0].lower() == 's':
			pr = 0
		else:
			pr = 1

		# print pr

		# print tr,

		if tr[0].lower() == 'r':
			tr = 1
		else:
			tr = 0

		# print tr

		if spc not in trPrHsh:
			trPrHsh[spc] = {}
		if ab not in trPrHsh[spc]:
			trPrHsh[spc][ab] = [[],[]]

		trPrHsh[spc][ab][0].append(tr)
		trPrHsh[spc][ab][1].append(pr)

	f.close()

	return trPrHsh

def getF1s(trPrHsh):
	prdF1Hsh = {}

	for i in trPrHsh:
		if i not in prdF1Hsh:
			prdF1Hsh[i] = {}
		for j in trPrHsh[i]:
			tr = trPrHsh[i][j][0]
			pr = trPrHsh[i][j][1]

			prdF1Hsh[i][j] = [f1_score(tr, pr, average = 'macro'),len(tr)]

	return prdF1Hsh

def mergeHshs(prdF1Hsh, expF1Hsh):
	for i in prdF1Hsh:
		for j in prdF1Hsh[i]:
			eF1 = expF1Hsh[i][j]
			prdF1Hsh[i][j] += eF1

def printPrdF1hsh(prdF1Hsh):
	arr = ['', '', 'Ground Truth', '', 'Expected', '', '']
	print('\t'.join(arr))
	arr = ['Species', 'Antibiotic', 'F1 Score', 'Samples', 'F1 Score', '95% CI', '']
	print('\t'.join(arr))
	for i in sorted(prdF1Hsh):
		for j in sorted(prdF1Hsh[i]):
			arr = [i,j] + prdF1Hsh[i][j]
			for k in range(0,len(arr)):
				arr[k] = str(arr[k])
			print('\t'.join(arr))

def main():
	abrHsh = getAbbr(argv[3])
	expF1Hsh = getExpectedF1(argv[2], abrHsh)
	trPrHsh = parsePredsWithASTs(argv[1])
	prdF1Hsh = getF1s(trPrHsh)

	mergeHshs(prdF1Hsh, expF1Hsh)

	printPrdF1hsh(prdF1Hsh)

if __name__ == '__main__':
	main()
