import os,sys
import pandas as pd

'''
                 0                    1         2            3
0  GCA_007749655.1  Salmonella enterica  amikacin  susceptible
1  GCA_006754985.1  Salmonella enterica  amikacin  susceptible
2  GCA_006811505.1  Salmonella enterica  amikacin  susceptible
'''
pred_data = pd.read_csv('amr_phenotype_summary.txt',sep='\t',header=0)
pred_data.columns = ['GCA_ID','Species','Antibiotic','SR']
pred_data = pred_data.drop(['Species'],axis=1)

'''
GCA_007749655.1	Salmonella enterica	amikacin	susceptible
GCA_006754985.1	Salmonella enterica	amikacin	susceptible
GCA_006811505.1	Salmonella enterica	amikacin	susceptible
GCA_007181875.1	Salmonella enterica	amikacin	susceptible
GCA_007547575.1	Salmonella enterica	amikacin	susceptible
GCA_007472455.1	Salmonella enterica	amikacin	susceptible
'''
asts_data = pd.read_csv('asts_data_unique_v2.tsv',sep='\t',header=0)
asts_data.columns = ['GCA_ID','Antibiotic','SR']
#asts_data.columns = ['GCA_ID','Species','Antibiotic','SR']
#asts_data = asts_data.drop(['Species'],axis=1)

merge_data = pred_data.merge(asts_data,on=['GCA_ID','Antibiotic'],how='left')
merge_data.columns = ['GCA_ID','Antibiotic','SR_pred','SR_asts']

in_asts = merge_data[~merge_data.SR_asts.isna()]
out_asts = merge_data[merge_data.SR_asts.isna()]
out_asts = out_asts.drop('SR_asts',axis=1)

in_asts.to_csv('predictions_with_asts_records.txt',sep='\t',index=None)
out_asts.to_csv('predictions_without_asts_records.txt',sep='\t',index=None)
