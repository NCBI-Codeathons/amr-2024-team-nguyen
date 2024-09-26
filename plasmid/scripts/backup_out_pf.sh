#!/usr/bin/env bash
#
# backup the final results: plasmidfinder.py (pf)
#
# in case smakemake gets fiesty and deletes them
#
rsync  -mhav --include='results_tab.tsv' --include='*/' --exclude='*' ./out/  ./out.bak/
