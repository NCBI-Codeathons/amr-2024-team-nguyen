#!/usr/bin/env python3
#
# Convert the AMR Codeathon AST assembly dataset_catalog.json into a DataFrame
#
#print("importing...")
import argparse
import json
import pandas as pd


def parse_ast_catalog(filename):

	#print("opening: "+filename)
	with open(filename) as f:
	    data = json.load(f)

	#print("loaded: "+filename)
	# Prepare the list to store rows
	rows = []

	# Loop over each assembly and extract required information
	for assembly in data.get("assemblies", []):
	    accession = assembly.get("accession", "")
	    #print("accession: "+accession)
	    genomic_nucleotide_fasta = ""
	    gff3 = ""
	    protein_fasta = ""
    
	    # Iterate through the files
	    for file in assembly.get("files", []):
	        if file["fileType"] == "GENOMIC_NUCLEOTIDE_FASTA":
	            genomic_nucleotide_fasta = file["filePath"]
	        elif file["fileType"] == "GFF3":
	            gff3 = file["filePath"]
	        elif file["fileType"] == "PROTEIN_FASTA":
	            protein_fasta = file["filePath"]
	    
	    # Append the row data to the list
	    rows.append({
	        "accession": accession,
	        "FNA": genomic_nucleotide_fasta,
	        "GFF": gff3,
	        "FAA": protein_fasta
	    })

	# Convert the list of rows into a DataFrame
	df = pd.DataFrame(rows)

	# Display the resulting DataFrame
	print("Loaded "+filename+": {0} rows, {1} columns.".format(*df.shape))

	# first line is empty, the JSON just contained a ref to the "assembly_data_report.jsonl" file
	return(df.iloc[1:])
