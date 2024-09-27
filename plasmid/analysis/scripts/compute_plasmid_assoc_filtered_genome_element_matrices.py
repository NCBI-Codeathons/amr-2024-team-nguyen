#!/usr/bin/env python3
#
# compute_plasmid_assoc_filtered_genome_element_matrices.py \
#   --contig_plasmidcall_elem_tab   contig_denovo-plasmid-element_5perc.tsv \
#   --low_pl_perc 10 \
#   --high_pl_perc 90 \
#   --out_elem_stats     element_stats.all.tsv \
#   --out_all_pl_matrix  out_all_pl_matrix.tsv \
#   --out_high_pl_matrix out_high_pl_matrix.tsv \
#   --out_low_pl_matrix  out_low_pl_matrix.tsv
#
# reads in the table associating contig plasmid calls and AMRFinderPlus contig AMR elements
# 
# generate_genome_elem_matrix_from_table():
#
#    Takes a table with columns [genome_acc, contig_acc, element_symbol].
#    Creates a matrix where each row is a unique genome_acc and each column is a unique element_symbol.
#    The matrix contains 1 if there is a corresponding element_symbol for a genome_acc, and -1 otherwise.
#
# Processing:
#
# element_symbol stats:
#    The program calculates total_calls, total_pl_calls, and pl_call_perc for each element_symbol.
#    The plasmid_assoc column is determined based on the thresholds low_pl_perc and high_pl_perc.
#
# Matrix generation (N=3):
#    All elements matrix: Written to out_all_genome_elem.
#    High plasmid_assoc matrix: Contains elements where plasmid_assoc=1.
#    Low plasmid_assoc matrix: Contains elements where plasmid_assoc=-1.

import argparse
import pandas as pd

def generate_genome_elem_matrix_from_table(all_genome_acc, df):
    """Generates a matrix of genome_acc vs. element_symbol, with 1 if the genome contains the element_symbol, -1 if not."""

    # Ignore rows with empty element_symbol
    # this causes us to lose all contigs that have no AMR elements
    #df = df.dropna(subset=['element_symbol'])  

    # default is no association
    # NOTE: this only creates rows for genome_acc values that also have a non-empty element_symbol value.
    matrix = pd.pivot_table(df, index='genome_acc', columns='element_symbol', aggfunc='size', fill_value=-1)


    # expand the pivot table to ensure all unique genome_acc values are included, filling missing rows with -1
    matrix = matrix.reindex(all_genome_acc.unique(), fill_value=-1)

    # mark all observed associations
    matrix[matrix > 0] = 1  # Convert all counts to 1 for presence

    return matrix

def process_files(contig_plasmidcall_elem_tab, low_pl_perc, high_pl_perc, out_elem_stats,
                  out_all_pl_matrix, out_high_pl_matrix, out_low_pl_matrix):

    # Read the contig_plasmidcall_elem_tab file
    print(f"Reading {contig_plasmidcall_elem_tab}...")
    df = pd.read_csv(contig_plasmidcall_elem_tab, sep='\t')
    print(f"Read {contig_plasmidcall_elem_tab}: {df.shape[0]} rows x {df.shape[1]} columns.")

    # QC: number of unique genome_acc
    n_uniq_genome_acc = df['genome_acc'].nunique()
    print(f"\tNumber of unique genome_acc: {n_uniq_genome_acc}")

    # Create element_plasmid_tab with unique element_symbol and required statistics
    print("Processing element symbols...")
    element_plasmid_tab = df.groupby('element_symbol').agg(
        total_calls=('plasmid_call', 'size'),
        total_pl_calls=('plasmid_call', lambda x: (x == 'PL').sum())
    ).reset_index()

    # Calculate pl_call_perc
    element_plasmid_tab['pl_call_perc'] = (element_plasmid_tab['total_pl_calls'] / element_plasmid_tab['total_calls']) * 100

    # Compute plasmid_assoc column based on thresholds
    element_plasmid_tab['plasmid_assoc'] = 0
    element_plasmid_tab.loc[element_plasmid_tab['pl_call_perc'] < low_pl_perc, 'plasmid_assoc'] = -1
    element_plasmid_tab.loc[element_plasmid_tab['pl_call_perc'] > high_pl_perc, 'plasmid_assoc'] = 1

    print(f"Writing {out_elem_stats}...")
    element_plasmid_tab.to_csv(out_elem_stats, sep='\t')
    print(f"Wrote {out_elem_stats}: {element_plasmid_tab.shape[0]} rows x {element_plasmid_tab.shape[1]} columns.")

    # Generate genome-element matrix for all element_symbols
    print("Generating genome-element matrix for all elements...")
    genome_elem_all = generate_genome_elem_matrix_from_table(df['genome_acc'],df)
    print(f"Writing {out_all_pl_matrix}...")
    genome_elem_all.to_csv(out_all_pl_matrix, sep='\t')
    print(f"Wrote {out_all_pl_matrix}: {genome_elem_all.shape[0]} rows x {genome_elem_all.shape[1]} columns.")
    # QC: number of unique genome_acc
    print(f"\tNumber of unique genome_acc: {genome_elem_all.index.nunique()}")

    # Filter rows with element_symbol classified as plasmid_assoc=1
    high_assoc_elements = element_plasmid_tab[element_plasmid_tab['plasmid_assoc'] == 1]['element_symbol']
    high_pl_df = df[df['element_symbol'].isin(high_assoc_elements)]

    # Generate genome-element matrix for high plasmid_assoc elements
    print("Generating genome-element matrix for plasmid_assoc=1 elements...")
    genome_elem_high = generate_genome_elem_matrix_from_table(df['genome_acc'],high_pl_df)
    print(f"Writing {out_high_pl_matrix}...")
    genome_elem_high.to_csv(out_high_pl_matrix, sep='\t')
    print(f"Wrote {out_high_pl_matrix}: {genome_elem_high.shape[0]} rows x {genome_elem_high.shape[1]} columns.")
    # QC: number of unique genome_acc
    print(f"\tNumber of unique genome_acc: {genome_elem_high.index.nunique()}")

    # Filter rows with element_symbol classified as plasmid_assoc=-1
    low_assoc_elements = element_plasmid_tab[element_plasmid_tab['plasmid_assoc'] == -1]['element_symbol']
    low_pl_df = df[df['element_symbol'].isin(low_assoc_elements)]

    # Generate genome-element matrix for low plasmid_assoc elements
    print("Generating genome-element matrix for plasmid_assoc=-1 elements...")
    genome_elem_low = generate_genome_elem_matrix_from_table(df['genome_acc'],low_pl_df)
    print(f"Writing {out_low_pl_matrix}...")
    genome_elem_low.to_csv(out_low_pl_matrix, sep='\t')
    print(f"Wrote {out_low_pl_matrix}: {genome_elem_low.shape[0]} rows x {genome_elem_low.shape[1]} columns.")
    # QC: number of unique genome_acc
    print(f"\tNumber of unique genome_acc: {genome_elem_low.index.nunique()}")

# Set up argparse
def main():
    parser = argparse.ArgumentParser(
        description="Process a table of contig_plasmidcall_elem_tab and generate genome-element matrices.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument('--contig_plasmidcall_elem_tab', type=str, default="contig_denovo-plasmid-element_5perc.tsv",
                        help="Input TSV file with columns: genome_acc, contig_acc, element_symbol, plasmid_call [%(default)s]")
    
    parser.add_argument('--low_pl_perc', type=float, default=10, help="Low plasmid call percentage threshold [%(default)s]")
    parser.add_argument('--high_pl_perc', type=float, default=90, help="High plasmid call percentage threshold [%(default)s]")
    
    parser.add_argument('--out_elem_stats', type=str, default="element_stats.all.tsv",
                        help="Output TSV file for stats on all amr elements [%(default)s]")
    
    parser.add_argument('--out_all_pl_matrix', type=str, default="out_all_pl_matrix.tsv",
                        help="Output TSV file for genome-element matrix for all elements [%(default)s]")

    parser.add_argument('--out_low_pl_matrix', type=str, default="out_low_pl_matrix.tsv",
                        help="Output TSV file for genome-element matrix for plasmid_assoc=-1 elements [%(default)s]")

    parser.add_argument('--out_high_pl_matrix', type=str, default="out_high_pl_matrix.tsv",
                        help="Output TSV file for genome-element matrix for plasmid_assoc=1 elements [%(default)s]")
    
    
    args = parser.parse_args()

    # Call the function to process the files
    process_files(args.contig_plasmidcall_elem_tab, args.low_pl_perc, args.high_pl_perc, 
                  args.out_elem_stats,
                  args.out_all_pl_matrix, args.out_high_pl_matrix, args.out_low_pl_matrix)

if __name__ == "__main__":
    main()
