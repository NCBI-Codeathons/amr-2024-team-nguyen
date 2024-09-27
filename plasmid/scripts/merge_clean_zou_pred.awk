#!/usr/bin/awk -f
BEGIN {
    FS = OFS = "\t"  # Set input and output field separators to tab
    # column names
    CONTIG_ACC=1
    SCORE=2
    CALL=3
    # parameter checkes
    if( ASM_TYPE == "" ) {
	print( "ERROR: ASM_TYPE unset!!")
	exit
    }
    # new headers
    print "genome_acc","contig_acc","asm_type","call","score"
}
{
    # Extract the second level directory name from FILENAME
    match(FILENAME, /\/([^\/]+)\/[^\/]+$/, arr)
    second_level_dir = arr[1]

    # Strip the "_split_seq_[0-9]+" suffix from the first column
    gsub(/_split_seq_[0-9.sub]+$/, "", $1)

    # Print the second-level directory as the new first column, followed by the rest of the line
    print second_level_dir, $CONTIG_ACC, ASM_TYPE, $CALL, $SCORE
}
