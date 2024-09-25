#!/usr/bin/env bash
#
# backup the final results
#
# in case smakemake gets fiesty and deletes them
#
TARGET=./out.bak/
if [ ! -z "$1" ]; then TARGET=$1; fi
echo "rsync  -mhav --include='*.zou.pred.tab' --include='*/' --exclude='*' ./out/  $TARGET"
rsync  -mhav --include='*.zou.pred.tab' --include='*/' --exclude='*' ./out/  $TARGET
