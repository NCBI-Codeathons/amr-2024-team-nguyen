import pandas as pd
### Now let's  map to the pathogen data from MicroBiggie ###
contig_df = pd.read_csv("zou_plasmid_results.tsv", sep="\t")

mb_df = pd.read_csv("/path/to/ncbi_pathogen_detect_amr.csv", low_memory=False)

mb_df.rename(
            columns={
                "asm_acc": "Genome ID", 
                "contig_acc": "Contig Name", 
            },
            inplace=True
        )

merged_df = pd.merge(contig_df, mb_df, how='left', on=['Genome ID', 'Contig Name'])
merged_df.to_csv('mapped_zou_plasmid_results.tsv', sep="\t", index=False)

#print(contig_df.columns)
#print(merged_df.columns)
