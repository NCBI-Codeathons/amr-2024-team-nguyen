#!/bin/bash

if [ ! -d GeneCorrels ]; then
	mkdir GeneCorrels
fi

for i in GeneMats20/*.tsv; do
	gFT=$(echo $i | rev | cut -f2 -d'.' | cut -f1 -d'_' | rev)
	for j in AMRPhenoMats/*; do
		pFT=NDARO
		if [ $j == "AMRPhenoMats/asts_augmented_matrix.txt" ]; then
			pFT=AUG
		fi
		echo $i $j $gFT $pFT
		python getCorrelsByGene.py $i $j > GeneCorrels/$gFT"_"$pFT.tab
		# break
	done
	# break
done