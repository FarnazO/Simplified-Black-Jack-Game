#!/bin/bash

clear
cd ../
export PYTHONPATH=$PWD
cd test_package/ 
tests=$(ls test_* | wc -l)
file_names=$(ls -d test_*)
declare -a files
files=($file_names)
success=0
for i in ${files[@]}
do
	echo "$i is running"
	python $i

	if [ $? -eq 0 ]; then
    	echo SUCCESS
    	let "success=success+1" 
	else
    	echo FAIL
	fi
	echo "======================================="
	echo "***************************************"
	echo "======================================="
done
let "failed=tests-success"
echo "Total failed tests: $failed"
echo "Total successful tests: $success"
