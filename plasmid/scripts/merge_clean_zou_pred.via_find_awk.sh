#!/usr/bin/env bash
#
# merge all sample-specific plasmid_x calling files
#
# this simple awk approach runs in ~ 30-40 seconds
# orders of magnitude faster than the python approaches tried previously
#
# run from "plasmid" directory
#
# we use "find -exec" because there are too many files to fit on the command line
# infect, find runs the script 12 times, resulting in 12 copies of header line,
# which that awk bit at the end cleans up!

cat <<EOF 
#
# denovo ASM contigs
#
# real	0m27.349s
# user	0m25.734s
# sys	0m3.213s
EOF
time find out -name "*.denovo.fna.zou.pred.tab" -exec awk -v ASM_TYPE=denovo -f scripts/merge_clean_zou_pred.awk {} + | awk 'BEGIN{FS = OFS = "\t"}(NR>1&&$1!="genome_acc"){print $0}' > merge_clean_zou_pred.denovo.via_find_awk.tsv 


cat  <<EOF 
#
# guided ASM contigs
#
# real	0m6.235s
# user	0m3.498s
# sys	0m2.761s
EOF
time find out -name "*.guided.fna.zou.pred.tab" -exec awk -v ASM_TYPE=guided -f scripts/merge_clean_zou_pred.awk {} + | awk 'BEGIN{FS = OFS = "\t"}(NR>1&&$1!="genome_acc"){print $0}' > merge_clean_zou_pred.guided.via_find_awk.tsv 


echo "done"
