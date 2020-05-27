#!/bin/bash


clear
tests=$(ls test_* | wc -l)
file_names=$(ls -d test_*)
declare -a files
files=($file_names)
success=0
for i in ${files[@]}
do
	echo "Linting is running on $i"
	pylint $i

	echo "======================================="
	echo "***************************************"
	echo "======================================="
done
