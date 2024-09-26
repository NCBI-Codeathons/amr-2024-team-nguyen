import os,sys
import pandas as pd

data = pd.read_csv('asts_data_augmented.txt',sep='\t',header=0)
#data = pd.read_csv('asts_data_unique_v2.tsv',sep='\t',header=0)

'''
susceptible                   234613
S                             208046
resistant                      65309
not defined (ignore)                   51496
R                              50455
intermediate (susceptible)                    5875
S*                              3707
R*                              2954
nonsusceptible (resistant)                  157
susceptible-dose dependent (susceptible)       62
'''

data_dict = {}
antibiotic_list = data['Antibiotic'].unique().tolist() 
gca_list = data['GCA_ID'].tolist() 
for idx,row in data.iterrows():
    gca_id = row['GCA_ID']
    antibiotic = row['Antibiotic']
    prediction = row['SR_pred']
    if antibiotic not in data_dict:
        data_dict[antibiotic] = {}
    if gca_id in data_dict[antibiotic]:
        if data_dict[antibiotic][gca_id] == prediction:
            continue
        import pdb
        pdb.set_trace()
    data_dict[antibiotic][gca_id] = prediction

outfile = 'asts_augmented_matrix.txt'
#outfile = 'asts_matrix.txt'
with open(outfile,'w') as o:
    o.write('Genome\t')
    o.write('\t'.join(antibiotic_list))
    o.write('\n')
    for gca_id in gca_list:
        o.write(f'{gca_id}')
        for antibiotic in antibiotic_list: 
            if gca_id in data_dict[antibiotic]:
                pred = data_dict[antibiotic][gca_id].lower()
                if pred[0] == 's': 
                    o.write('\t-1')
                elif pred[0] == 'r':
                    o.write('\t1')
                elif pred == 'intermediate': #susceptible
                    o.write('\t-1')
                elif pred == 'nonsusceptible': #resistant
                    o.write('\t1')
                else:
                    o.write('\t')
            else:
                o.write('\t')
        o.write('\n')
