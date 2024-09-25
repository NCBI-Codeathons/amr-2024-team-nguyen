#!/usr/bin/env bash
#
# install plasmidFinder via conda
#

echo <<EOF 
#
# create env
#
EOF
conda create --prefix conda_pf -f plasmid_finder.yml

echo <<EOF 
#
# activate
#
EOF
conda activate ./conda_pf

echo <<EOF 
#
# download db
#
EOF
download-db.sh

echo <<EOF 
#
# usage example
#
EOF
echo  plasmidfinder.py \
      -i /home/nbowers/bvbrc-dev/dev_container/NCBI_AMR_Codeathon/all-ast/GCA_904866355.1/GCA_904866355.1_KSB1_6F_genomic.denovo.fna \
      -o ./output
echo "# view output"
echo "cat output/data.json | jq "
