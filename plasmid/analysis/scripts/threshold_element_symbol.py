#!/usr/bin/env python3
#
# filter AMR-element:contig table
#
# compute number of unique genomes for each element_symbol.
# remove all records for elment_symbols below the threshold percentage of genomes
# save a table of the counts
#
import argparse
import pandas as pd

# Define the function that will perform the task
def process_tsv(input_file, output_file, min_perc, elem_genome_counts_file):
    # Load the select columns [1,2,4] from the TSV file
    column_mapping = {1: 'genome_acc', 2: 'contig_acc', 3: 'element_name', 4: 'element_symbol'}
    print("Reading "+input_file)
    df = pd.read_csv(input_file, sep='\t', usecols=[0, 1, 3], header=None, names=[column_mapping[1], column_mapping[2], column_mapping[4]])
    print("Read "+input_file+": {0} rows, {1} columns.".format(*df.shape))

    # Count how many distinct values there are in genome_acc
    distinct_genome_acc_count = df['genome_acc'].nunique()

    # Calculate the min_threshold based on min_perc
    min_threshold = (min_perc / 100) * distinct_genome_acc_count

    # For each value in element_symbol, count how many distinct genome_acc values it is associated with
    element_counts = df.groupby('element_symbol')['genome_acc'].nunique()

    # Write element_symbol and its unique genome_acc counts to a separate TSV file
    #print("Write "+elem_genome_counts_file+":{0} rows, {1} columns.".format(*element_counts.shape))
    print("Write "+elem_genome_counts_file)
    element_counts.to_csv(elem_genome_counts_file, sep='\t', header=['unique_genome_acc_count'])

    # Filter out rows where element_symbol is not associated with at least min_threshold unique genome_acc values
    valid_elements = element_counts[element_counts >= min_threshold].index
    filtered_df = df[df['element_symbol'].isin(valid_elements)]

    # Write the remaining rows to the output TSV file
    print("Write "+output_file+":{0} rows, {1} columns.".format(*filtered_df.shape))
    filtered_df.to_csv(output_file, sep='\t', index=False)

# Set up argparse
def main():
    parser = argparse.ArgumentParser(
        description="Process AMR_element_symbol to contig_acc TSV file and filter rows based on unique genome_acc counts per element_symbol.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter  # Use this formatter to show defaults in help
    )
    parser.add_argument('--input', type=str, default="convertedNPDA.tsv", help="Input TSV file")
    parser.add_argument('--output', type=str, required=True, help="Output TSV file")
    parser.add_argument('--min_perc', type=float, default=5,
                        help="Minimum percentage of unique genome_accs required for element_symbol filtering")
    parser.add_argument('--elem_genome_counts', type=str, default="convertedNPDA.hist.element_symbol_uniq_genome_counts.tsv",
                        help="Output TSV file for element_symbol and their unique genome_acc counts")

    args = parser.parse_args()

    # Call the function to process the TSV
    process_tsv(args.input, args.output, args.min_perc, args.elem_genome_counts)

if __name__ == "__main__":
    main()
