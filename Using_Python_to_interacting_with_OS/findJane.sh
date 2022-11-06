#!/bin/bash

> oldFiles.txt
for file in $(grep " jane " list.txt | cut -d " " -f 3); do
	if test -e "..${file}"; then 
		echo $file >> oldFiles.txt;
	fi
done