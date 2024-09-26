import glob
import sys,os
from tqdm import tqdm
import pandas as pd

'''
Genome
Species
Antibiotic
S|R Call
'''

mapping_dict = {}
mapping_file = 'sciNm_bioAcc_asmAcc.csv'
with open(mapping_file,'r') as i:
    for line in i:
        species, accession, gca = line.strip().split('\t')        
        mapping_dict[gca] = species

all_predict_files = glob.glob('output/*/*.sir.pred.tab')
#all_predict_files = glob.glob('/home/ac.cucinell/AMR_Codeathon_2024/amr_predictions/*')
out_data = []
for pred_file in tqdm(all_predict_files):
    data = pd.read_csv(pred_file,sep='\t',header=0) 
    gca_id = '_'.join(os.path.basename(pred_file).split("_")[0:2])
    species = ' '.join(mapping_dict[gca_id].split(' ')[0:2]) 
    for row in data.iterrows():
        row_data = row[1]
        antibiotic = row_data['Antibiotic']
        call = row_data['SR']
        out_data.append([gca_id,species,antibiotic,call]) 

out_df = pd.DataFrame(out_data,columns=['Genome','Species','Antibiotic','SR_Call']) 
out_df.to_csv('amr_phenotype_summary.txt',sep='\t',index=False)
