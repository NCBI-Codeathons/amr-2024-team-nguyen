import glob
import os
import pandas as pd
from multiprocessing import Pool
import subprocess

model_dir = '/nfs/ml_lab/projects/ml_lab/mnguyen/AMR_Models/ALL_SPEC/OLD_2024_04_15/models.spcAb.sir.python3'
data_file = pd.read_csv("/nfs/ml_lab/projects/ml_lab/cucinell/amr_codeathon_2024/sciNm_bioAcc_asmAcc.csv", sep='\t')
data_file.columns = ['Species', 'Biosample', 'GCA_ID']
predict_script = '/nfs/ml_lab/projects/ml_lab/mnguyen/AMR_Models/ALL_SPEC/OLD_2024_04_15/models.spcAb.sir.python3/predict.py'
threads = '1'
genomes_path = "/nfs/ml_lab/projects/ml_lab/cucinell/amr_codeathon_2024/fasta_files/*"

def run_command(cmd):
    """Run the command using subprocess"""
    try:
        #print(cmd)
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(cmd)}")

def process_file(fasta_file):
    """Process each fasta file, construct the command, and run it using subprocess"""
    try:
        gca_id = '_'.join(os.path.basename(fasta_file).split('_')[0:2])
        org_data = data_file.loc[data_file.GCA_ID == gca_id]
        if org_data.shape[0] == 0:
            return  # Skip this entry if there's no matching GCA_ID
        
        species = '_'.join(org_data.Species.tolist()[0].split(' ')[0:2])
        space_species = species.replace('_', ' ')
        tmp_dir = f'/nfs/ml_lab/projects/ml_lab/cucinell/amr_codeathon_2024/tmp_dir/{gca_id}'
        out_dir = f'/nfs/ml_lab/projects/ml_lab/cucinell/amr_codeathon_2024/output/{gca_id}'
        model_list = glob.glob(os.path.join(model_dir, species) + '*')
        
        if len(model_list) > 0:
            cmd = ['python3', predict_script, '--fasta_file', fasta_file, '--species', f'{space_species}', '-n', threads, '-t', tmp_dir, '-o', out_dir]
            
            # Run the command
            run_command(cmd)
    
    except Exception as e:
        print(f"Exception occurred: {e}")

def main():
    all_fasta_files = glob.glob(genomes_path)

    # Use Pool to manage multiple processes
    with Pool(processes=128) as pool:
        pool.map(process_file, all_fasta_files)

if __name__ == "__main__":
    main()

