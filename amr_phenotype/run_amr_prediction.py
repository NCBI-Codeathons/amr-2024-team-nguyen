import glob
import os,sys
import pandas as pd

'''
parser.add_option('-f', '--fasta_file', help='Fasta file to predict with.', metavar="FILE", default='', dest='fastaFile')
    parser.add_option('-s', '--species', help="Specify the species of genome for the fasta file.  Remember to use quotes.", metavar="SPEC", default='', dest='species')
    parser.add_option('-n', '--threads', help="Number of threads to run with.  Default value is 1.", metavar='INT', default=1, type=int, dest='threads')
    parser.add_option('-t', '--temp_dir', help="Specify the temporary directory to use, default is ./temp/", metavar="DIR", default='./temp/', dest="tDir")
    parser.add_option('-o', '--out_dir', help="Specify the output directory to store all the outupt files.  Defaults to working directory", metavar="DIR", default='./', dest="oDir")

'''

model_dir = '/nfs/ml_lab/projects/ml_lab/mnguyen/AMR_Models/ALL_SPEC/OLD_2024_04_15/models.spcAb.sir.python3'

data_file = pd.read_csv("/nfs/ml_lab/projects/ml_lab/cucinell/amr_codeathon_2024/sciNm_bioAcc_asmAcc.csv",sep='\t')
data_file.columns = ['Species','Biosample','GCA_ID']
predict_script = '/nfs/ml_lab/projects/ml_lab/mnguyen/AMR_Models/ALL_SPEC/OLD_2024_04_15/models.spcAb.sir.python3/predict.py'

threads = '1'    
genomes_path = "/nfs/ml_lab/projects/ml_lab/cucinell/amr_codeathon_2024/fasta_files/*"
count = 0
for fasta_file in glob.glob(genomes_path):
    try:
        gca_id = '_'.join(os.path.basename(fasta_file).split('_')[0:2])
        pdt_id = '_'.join(os.path.basename(fasta_file).split('_')[2:3]) 
        org_data = data_file.loc[data_file.GCA_ID == gca_id]
        if org_data.shape[0] == 0:
            continue
        species = '_'.join(org_data.Species.tolist()[0].split(' ')[0:2])
        space_species = species.replace('_',' ')
        tmp_dir = f'/nfs/ml_lab/projects/ml_lab/cucinell/amr_codeathon_2024/tmp_dir/{gca_id}'
        out_dir = f'/nfs/ml_lab/projects/ml_lab/cucinell/amr_codeathon_2024/output/{gca_id}'  
        model_list = glob.glob(os.path.join(model_dir,species)+'*')
        if len(model_list) > 0:
            count += 1
            cmd = ['python3',predict_script,'--fasta_file',fasta_file,'--species',f'\"{space_species}\"','-n',threads,'-t',tmp_dir,'-o',out_dir]
            #print(' '.join(cmd))
            #if not os.path.exists(tmp_dir):
            #    os.mkdir(tmp_dir)
            #if not os.path.exists(out_dir):
            #    os.mkdir(out_dir)
    except Exception as e:
        import pdb
        pdb.set_trace()
        print('here')
print(f'will run {str(count)}')
