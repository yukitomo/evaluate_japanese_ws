#!/bin/sh
# $ bash  eval_japanese_ws.sh ref_file sys_file
ref_file=$1
sys_file=$2

echo "ref_file : ${ref_file}"
echo "sys_file : ${sys_file}"

python scripts/evaluate_japanese_ws/pre_treatment.py ${ref_file} ${result_path} |perl scripts/conlleval.pl -d "\t"

