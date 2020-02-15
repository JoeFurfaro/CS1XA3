#!/bin/bash

# Get the intended feature from the first argument
ARGS="'$*'"
RAN="N"

if [ "$#" -eq 0 ] ; then
	# Tell user to include a feature argument
	echo "Please enter one or more arguments that specifies the feature you want to use. Example: ./project_analyze.sh fixme filesize"
	RAN="Y"
fi
if [[ "$ARGS" == *"fixme"* ]] ; then
	# Run FIXME script here
	# Ignore null bytes: https://stackoverflow.com/questions/46163678/get-rid-of-warning-command-substitution-ignored-null-byte-in-input
	echo "Running FIXME..."
	> "fixme.log"
	FILES=$(find .. -type f)
	IFS=$'\n'
	for FILE in $FILES ; do
		LAST=$(tail -n 1 "$FILE" | tr -d '\0')
		if [[ "$LAST" == *"#FIXME"* ]] ; then
			echo "$FILE" >> "fixme.log"
		fi
	done
	echo "Done!"
	IFS=" "
	RAN="Y"
fi
if [[ "$ARGS" == *"filesize"* ]] ; then
	# Run FILESIZE script here
	# Useful stuff found here: https://unix.stackexchange.com/questions/22432/getting-size-with-du-of-files-only
	echo "----------------------"
	echo "Showing the sizes of files in Joe Furfaro's CS1XA3 repo (parent folder to this folder)"
	echo "----------------------"
	find .. -type f -exec du -h {} + | sort -nr
	echo "----------------------"
	RAN="Y"
fi
if [[ "$ARGS" == *"typecount"* ]] ; then
	# Run TYPECOUNT script here
	echo "Enter a file extension: "
	read EXT
	COUNT=$(find .. -type f -name "*.$EXT" | wc -l)
	echo "There are $COUNT files in the repository that have the extension .$EXT."
	RAN="Y"
fi
if [ "$RAN" == "N" ] ; then
	echo "Feature not found. Check out the README.md file to see a list of available features."
fi
