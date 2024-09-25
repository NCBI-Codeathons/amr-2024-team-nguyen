#!/bin/bash

if (( $# < 4 )); then
	echo usage: "$0 [k] [file in] [file out] [temp dir] <threads>"
	echo "Uses kmc to get kmers and kmc_dump to print"
	echo "Outputs readable file to [file out].[k].kmrs"
	echo $# args supplied
	exit
fi

k=$1
fin=$2
fout=$3
dir=$4
threads=1
if (( $# > 4 )); then
	threads=$5
fi

kmc -t8 -k$k -fm -ci1 -cs1677215 -t$threads $fin $fout $dir
kmc_dump $fout $fout.$k.kmrs
