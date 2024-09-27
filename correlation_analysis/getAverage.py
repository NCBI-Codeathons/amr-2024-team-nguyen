'''
python getAverage.py [Gene Correl Tab]
'''

from sys import argv
import math
import numpy as np
import scipy.stats

def mean_confidence_interval(data, confidence=0.95):
	a = 1.0 * np.array(data)
	n = len(a)
	m, se = np.mean(a), scipy.stats.sem(a)
	h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
	return [m, m-h, m+h]

f = open(argv[1])

corrs = []
for i in f:
	i = i.strip('\n').split('\t')
	corr = float(i[-1])
	if math.isnan(corr):
		continue
	corrs.append(corr)

f.close()

aci = mean_confidence_interval(corrs)

for i in range(0,len(aci)):
	aci[i] = str(aci[i])

print('\t'.join(aci))

