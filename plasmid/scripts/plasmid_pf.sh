#!/usr/bin/env bash
#
# plasmid_pf.sh PLASMID_FINDER_DIR FASTA_FILE OUT_DIR
#
#
SDIR=$1
echo SDIR=$1
FASTA=$2
echo FASTA=$FASTA
ODIR=$3
echo ODIR=$ODIR

# add KMC to path                                                                                                                  
source ~/miniconda3/etc/profile.d/conda.sh 
conda activate $SDIR/conda_pf

# if output directory doesn't exist, make it                                                                                       
if [ ! -d $ODIR ]; then
        mkdir $ODIR
fi

date                                                                                                                     

echo "# run finder -> json"

plasmidfinder.py -i $FASTA -o $ODIR

date

###                                                                                                                                
# Cleanup                                                                                                                          
###                                                                                                                                

echo "# Cleanup"
rm -r $ODIR/tmp
#rm $FASTA.zou.sub.*

