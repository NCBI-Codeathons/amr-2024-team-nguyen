import pandas as pd
import os,sys

out_asts = pd.read_csv('predictions_without_asts_records.txt',sep='\t',header=0)
asts_data = pd.read_csv('asts_data_unique_v2.tsv',sep='\t')
#asts_data = asts_data.drop(['Species'],axis=1)

aug_data = pd.concat([out_asts,asts_data],ignore_index=True)

aug_data.to_csv('asts_data_augmented.txt',sep='\t',index=False)
