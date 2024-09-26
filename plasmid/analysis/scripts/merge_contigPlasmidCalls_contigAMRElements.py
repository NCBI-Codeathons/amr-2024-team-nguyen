#!/usr/bin/env python3
#
# Mergethe
#    contig plasmid classifier calls
# with the
#   (filtered) table of contig-AMR_elements (precomputed from AMRFinderPlus)
#

import argparse
import pandas as pd

def process_files(contig_elements, contig_plasmid_calls, output):
    # Read in the TSV files as DataFrames
    print(f"Reading {contig_plasmid_calls}...")
    contig_plasmid_df = pd.read_csv(contig_plasmid_calls, sep='\t', header=None, 
                                    names=['genome_acc', 'contig_acc', 'asm_type', 'plasmid_call', 'plasmid_score'])
    print(f"Read {contig_plasmid_calls}: {contig_plasmid_df.shape[0]} rows x {contig_plasmid_df.shape[1]} columns.")

    print(f"Reading {contig_elements}...")
    contig_elements_df = pd.read_csv(contig_elements, sep='\t')
    print(f"Read {contig_elements}: {contig_elements_df.shape[0]} rows x {contig_elements_df.shape[1]} columns.")

    # Perform the left outer join using [genome_acc, contig_acc] as the compound key
    print("Merging DataFrames...")
    merged_df = pd.merge(contig_plasmid_df, contig_elements_df, on=['genome_acc', 'contig_acc'], how='left')
    print(f"Merged DataFrame: {merged_df.shape[0]} rows x {merged_df.shape[1]} columns.")

    # Write the resulting DataFrame to the output file
    print(f"Writing {output}...")
    merged_df.to_csv(output, sep='\t', index=False)
    print(f"Wrote {output}: {merged_df.shape[0]} rows x {merged_df.shape[1]} columns.")

# Set up argparse
def main():
    parser = argparse.ArgumentParser(
        description="Perform a left outer join between contig_plasmid_calls and contig_elements files.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--contig_elements', type=str, default="convertedNPDA.5perc.tsv", 
                        help="Input TSV file with columns: genome_acc, contig_acc, and element_symbol [%(default)s]")
    parser.add_argument('--contig_plasmid_calls', type=str, default="../merge_clean_zou_pred.denovo.via_find_awk.tsv", 
                        help="Input TSV file with columns: genome_acc, contig_acc, asm_type, plasmid_call, plasmid_score [%(default)s]")
    parser.add_argument('--output', type=str, default="contig-plasmid-element_5perc.tsv", 
                        help="Output TSV file [%(default)s]")
    
    args = parser.parse_args()

    # Call the function to process the files
    process_files(args.contig_elements, args.contig_plasmid_calls, args.output)

if __name__ == "__main__":
    main()
