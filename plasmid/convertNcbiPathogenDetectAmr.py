
import argparse
from enum import IntEnum
import pandas as pd


"""

Purpose: Filter and reformat the ncbi_pathogen_detect_amr.csv file and save the results as a TSV file.

The output TSV file will have the following columns from ncbi_pathogen_detect_amr.csv:

- genome ID (asm_acc)
- contig ID (contig_acc)
- Gene/functional name/role (element_name?)
- Added later: plasmid/contig classification


Helpful links:

- https://pandas.pydata.org/pandas-docs/stable/user_guide/enhancingperf.html#enhancingperf
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply

"""

# Column indices
class Column(IntEnum):
   scientific_name = 0
   protein_acc = 1
   biosample_acc = 2
   target_acc = 3
   contig_acc = 4
   start_on_contig = 5
   end_on_contig = 6
   strand = 7
   element_symbol = 8
   element_name = 9
   _type = 10
   scope = 11
   subtype = 12
   _class = 13
   subclass = 14
   amr_method = 15
   pct_ref_coverage = 16
   pct_ref_identity = 17
   taxgroup_name = 18
   strain = 19
   serovar = 20
   element_length = 21
   reference_element_length = 22
   align_length = 23
   hmm_acc = 24
   hmm_description = 25
   geo_loc_name = 26
   isolation_source = 27
   epi_type = 28
   host = 29
   asm_acc = 30
   collection_date = 31
   Run = 32
   closest_reference_acc = 33
   closest_reference_name = 34
   rel_asm_cov = 35
   contig_coverage = 36
   asm_coverage = 37
   amrfinderplus_version = 38
   amrfinderplus_analysis_type = 39
   refgene_db_version = 40
   target_data_id = 41
   contig_url = 42
   protein_url = 43
   hierarchy_node = 44
   bioproject_acc = 45
   creation_date = 46



# Filter and reformat the ncbi_pathogen_detect_amr.csv file and save the results as a TSV file.
def convert(inputFilename, outputFilename):

   # Read the TSV file
   df = pd.read_csv(inputFilename)

   # Create or open the output file.
   with open(outputFilename, "w") as outputFile:

      df.apply(lambda row: convertRow(outputFile,
                                      row.iat[int(Column.asm_acc)], 
                                      row.iat[int(Column.contig_acc)],
                                      row.iat[int(Column.element_name)],
                                      row.iat[int(Column.element_symbol)],
                                      row.iat[int(Column._type)]),
                                      axis=1)


# Format input parameters as a line of TSV and append to the output file.
def convertRow(outputFile, asmAccession, contigAccession, elementName, elementSymbol, type):

   if type != "AMR":
      return
   
   # Replace nan values with an empty string.
   if asmAccession != asmAccession:
      asmAccession = ""
   
   if contigAccession != contigAccession:
      contigAccession = ""
   
   if elementName != elementName:
      elementName = ""
   
   if elementSymbol != elementSymbol:
      elementSymbol = ""
   
   # Append the TSV to the output file.
   outputFile.write(f"{asmAccession}\t{contigAccession}\t{elementName}\t{elementSymbol}\n")


# Trim a string that's possibly null and always return a non-null value.
def safeTrim(text: str):
   if not text:
      return ""
   
   trimmedText = text.strip()
   if len(trimmedText) < 1:
      return ""
   
   return trimmedText




if __name__ == '__main__':

   parser = argparse.ArgumentParser(description="Filter and reformat the ncbi_pathogen_detect_amr.csv file and save the results as a TSV file.")

   parser.add_argument("--input", dest="inputFile", metavar='INPUT_FILE', nargs=1, required=True, help="The TSV input filename")
   parser.add_argument("--output", dest="outputFile", metavar='OUTPUT_FILE', nargs=1, required=True, help="The TSV output filename")

   args = parser.parse_args()

   inputFile = safeTrim(args.inputFile[0])
   if len(inputFile) < 1:
      raise Exception("Invalid inputFile parameter")
   
   outputFile = safeTrim(args.outputFile[0])
   if len(outputFile) < 1:
      raise Exception("Invalid outputFile parameter")

   # Convert the TSV input file.
   convert(inputFile, outputFile)