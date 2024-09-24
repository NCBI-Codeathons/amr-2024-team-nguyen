#!/usr/bin/env python3
#
from parse_dataset_catalog import parse_ast_catalog

DATASET_DIR="/home/nbowers/bvbrc-dev/dev_container/NCBI_AMR_Codeathon/all-ast"
CAT_FILENAME="dataset_catalog.json"

df = parse_ast_catalog(DATASET_DIR+"/"+CAT_FILENAME)

print("   Read {0} rows, {1} columns.".format(*df.shape))
