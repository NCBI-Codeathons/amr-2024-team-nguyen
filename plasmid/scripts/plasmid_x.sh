#!/usr/bin/env bash
#
# run_plasmid_x.sh PRED_ALL_DIR FASTA_FILE OUT_DIR
#
# run Xioahui's models
# an edit of runModels.sh
#
SDIR=$1
echo SDIR=$1
#FASTA=$(readlink -f $2)
FASTA=$2
echo FASTA=$FASTA
ODIR=$3
echo ODIR=$ODIR

# add KMC to path                                                                                                                  
PATH=$PATH:$SDIR/kmc/:$SDIR/kmc/bin/

# if output directory doesn't exist, make it                                                                                       
if [ ! -d $ODIR ]; then
        mkdir $ODIR
fi

# if fasta split directory exists, clear it out                                                                                    
#if [ -d $FASTA.split ]; then
#        rm -r $FASTA.split/*
#fi

# echo splitting fasta                                                                                                             
# date                                                                                                                             

# split the fasta file into individual contigs                                                                                     
#python $SDIR/splitFasta.py $FASTA

# echo Xioahui Model                                                                                                       
date                                                                                                                     

cd $SDIR
echo "# activate conda env"
# activate python environment based on GPU existance                                                                       
# if which nvidia-smi > /dev/null; then                                                                                    
#       source zou/conda3/bin/activate root                                                                                
# else                                                                                                                     
#       source zou/conda3_nogpu/bin/activate root                                                                          
# fi                                                                                                                       
source zou/conda3_nogpu/bin/activate root

echo "# subsample each fasta file to 5000 nt"
# echo python $SDIR/zou/subsampleFastas.py $FASTA.split/                                                                   
python $SDIR/zou/subsampleFastas.py $FASTA.split/

# run KMC on all split contigs                                                                                             
for i in $(find $FASTA.split -name "*.sub.fasta"); do
    #echo -e "\tKMC $i"
    #echo -e "\t" kmc.sh 6 $i $i $ODIR/
    kmc.sh 6 $i $i $ODIR/ > /dev/null
    rm $i.kmc_pre $i.kmc_suf
done


echo "# create matrix and matrix order for prediction"

echo python $SDIR/zou/makeMatrix.py $FASTA.split/ $FASTA.zou.sub
python $SDIR/zou/makeMatrix.py $FASTA.split/ $FASTA.zou.sub

echo "# move to zou model directory"
cd zou/zou-plasmid-prediction/
python model_predict.py $FASTA.zou.sub.mat | sed 's/^ *//g' | sed 's/\[//g' | sed 's/\]//g' > $FASTA.zou.sub.pred
cd -

echo # move back to script directory and merge predictions with"contig names"
python zou/mergePreds.py $FASTA.zou.sub.order.lst $FASTA.zou.sub.pred > $ODIR/$(basename $FASTA).zou.pred.tab

date

###                                                                                                                                
# Cleanup                                                                                                                          
###                                                                                                                                

echo "# Cleanup"
#rm -r $FASTA.split
#rm $FASTA.zou.sub.*

