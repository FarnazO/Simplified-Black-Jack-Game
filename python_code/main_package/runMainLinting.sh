#!/bin/bash


clear
mains=$(ls *.py | wc -l)
file_names=$(ls -d *.py)
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
