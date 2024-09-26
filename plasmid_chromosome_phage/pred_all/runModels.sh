#! /bin/bash
#
# runModels.sh [fasta file] [out dir]

RUND1=0
RUNX=1
RUND2=0
RUNJ=0

# get script directory
SDIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
# get output directory
ODIR=$(pwd)/$(echo $2 | sed 's/\/$//g')
# get fasta file
FASTA=$(readlink -f $1)

# set old path
PATHOLD=$PATH

# add KMC to path
PATH=$PATH:$SDIR/kmc/:$SDIR/kmc/bin/

# if output directory doesn't exist, make it
if [ ! -d $ODIR ]; then
	mkdir $ODIR
fi

# if fasta split directory exists, clear it out
if [ -d $FASTA.split ]; then
	rm -r $FASTA.split/*
fi

# echo splitting fasta
# date

# split the fasta file into individual contigs
python $SDIR/splitFasta.py $FASTA

# date

###
# RUN DERYA'S MODELS
###

if [ $RUND1 -eq 1 ]; then

	# echo Derya Model
	# date

	# move to aytan directory and run Derya's models then move to script directory
	cd $SDIR/aytan
	source conda3/bin/activate root

	python sourcefinder/SourceFinder/SourceFinder_directory.py -p models/ -n 10 -o $ODIR/ $FASTA.split/
	cd $SDIR

	pwd
	echo $ODIR

	# rename output file from Derya's models 
	mv $ODIR/*_oriclass_srand_n10.tsv $ODIR/$(basename $FASTA).aytan.pred.tab

	# date
fi

###
# RUN XIOAHUI'S MODELS
###

if [ $RUNX -eq 1 ]; then

	# echo Xioahui Model
	# date

	cd $SDIR

	# activate python environment based on GPU existance
	# if which nvidia-smi > /dev/null; then 
	# 	source zou/conda3/bin/activate root
	# else 
	# 	source zou/conda3_nogpu/bin/activate root
	# fi
	source zou/conda3_nogpu/bin/activate root

	# subsample each fasta file to 5000 nt
	# echo python $SDIR/zou/subsampleFastas.py $FASTA.split/
	python $SDIR/zou/subsampleFastas.py $FASTA.split/

	# run KMC on all split contigs
	for i in $FASTA.split/*.sub.fasta; do
		kmc.sh 6 $i $i $ODIR/ > /dev/null
		rm $i.kmc_pre $i.kmc_suf
	done

	# create matrix and matrix order for prediction
	python $SDIR/zou/makeMatrix.py $FASTA.split/ $FASTA.zou.sub

	# move to zou model directory
	cd zou/zou-plasmid-prediction/
	python model_predict.py $FASTA.zou.sub.mat | sed 's/^ *//g' | sed 's/\[//g' | sed 's/\]//g' > $FASTA.zou.sub.pred
	# move back to script directory and merge predictions with 
	#   contig names
	cd $SDIR
	python zou/mergePreds.py $FASTA.zou.sub.order.lst $FASTA.zou.sub.pred > $ODIR/$(basename $FASTA).zou.pred.tab

	# date
fi

###
# RUN AYTAN PLASMID HOST MODELS
###

if [ $RUND2 -eq 1 ]; then

	# echo Derya Model 2
	# date

	source aytan_plasHost/conda2/bin/activate root

	cd $SDIR/aytan_plasHost
	ls $FASTA.split/ | grep '.fasta' | grep -v '.sub.' > $FASTA.split.lst
	python plasmid-host-prediction/plasmid_host_range_pipeline_for_fragments.py -inp $FASTA.split/ -i $FASTA.split.lst -s 1000 -n 5 -p models/ -l genus -t 0.5 -o $FASTA.aytan.host > $FASTA.aytan.host.raw

	# cd $SDIR

	grep "Predicted plasmid host range for" $FASTA.aytan.host.raw | sed 's/\t/ /g' | cut -f6,8 -d' ' > $ODIR/$(basename $FASTA).aytan.host.pred.tab

	# set path back
	PATH=$PATHOLD

	# date

fi

###
# Cleanup
###

# echo Cleanup
# date

rm -r $FASTA.split
# rm $FASTA.split.lst
rm $FASTA.zou.sub.*
# rm -r $FASTA.aytan.host 
# rm -r $FASTA.aytan.host.raw

# date
