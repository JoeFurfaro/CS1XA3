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
	find .. -type f -exec du -h "{}" + | sort -nr
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
if [[ "$ARGS" == *"findtag"* ]] ; then
	echo "Enter a tag: "
	read TAG
	> "$TAG.log";
	find .. -type f -name "*.py" -exec cat "{}" + | grep "#.*$TAG.*" >> "$TAG.log"
	echo "Done"
	RAN="Y"
fi
if [[ "$ARGS" == *"lastmerge"* ]] ; then
	ID=$(git log --oneline | grep "merge" -m 1 | cut -c 1-7)
	git checkout "$ID"
	echo "Done"
	RAN="Y"
fi
if [[ "$ARGS" == *"backuprestore"* ]] ; then
	echo "Would you like to Backup or Restore? (b/r)"
	read ACTION
	if [ "$ACTION" == "b" ] ; then
		echo "Backing up..."
		if [ -d "backup" ] ; then
			rm -R "backup"
		fi
		mkdir "backup"
		find .. -type f -name "*.tmp" >> "backup/restore.log"
		find .. -type f -name "*.tmp" -not -path "*/backup/*" -exec mv "{}" "./backup" \;
		echo "Done"
	elif [ "$ACTION" == "r" ] ; then
		if [ -f "backup/restore.log" ] ; then
			echo "Restoring..."
			FILES=$(cat "backup/restore.log")
			IFS=$'\n'
			for FILE in $FILES ; do
				BASENAME=$(basename "$FILE")
				cp "backup/$BASENAME" "$FILE"
			done
			IFS=" "
			echo "Done"
		else
			echo "ERROR: There is not restore.log file to restore your data from!"
		fi
	else
		echo "Invalid action"
	fi
	RAN="Y"
fi
if [[ "$ARGS" == *"sshman"* ]] ; then
	echo "--------------------------------"
	echo "REMOTES MANAGER - HELP IN README"
	echo "--------------------------------"

	if [ ! -d "hosts" ] ; then
	    mkdir "hosts"
	fi

	CMD=""
	while [ ! "$CMD" == "exit" ] ; do
	    read CMD
	    if [ "$CMD" == "ssh" ] ; then
	        echo "Enter target ID..."
	        read ID
	        if [ -f "hosts/$ID" ] ; then
	            HOST=$(sed '2q;d' "hosts/$ID")
	            USERNAME=$(sed '3q;d' "hosts/$ID")
	            echo "Opening connection to '$ID' ($USERNAME@$HOST)"
	            ssh "$USERNAME@$HOST"
	            echo "--------------------"
	        else
	            echo "Host with ID '$ID' not found"
	        fi
	    elif [ "$CMD" == "addhost" ] ; then
	        echo "Enter new ID..."
	        read ID
	        echo "Enter host address..."
	        read HOST
	        echo "Enter user..."
	        read USERNAME
	        # Create host here
	        > "hosts/$ID"
	        echo "$ID" >> "hosts/$ID"
	        echo "$HOST" >> "hosts/$ID"
	        echo "$USERNAME" >> "hosts/$ID"
	        echo "Host added successfully"
	    elif [ "$CMD" == "hosts" ] ; then
			FILES=$(find "hosts" -type f)
		    CONTENTS=""
		    IFS=$'\n'
		    > "tmp_list"
		    echo "HOST ID|HOST ADDRESS|USER NAME" >> tmp_list
		    echo "-------|------------|---------" >> tmp_list
		    for FILE in $FILES ; do
		        CUR_CONTENTS=$(cat "$FILE" | tr "\n" "|")
		        echo $CUR_CONTENTS >> "tmp_list"
		    done
		    column -t -s '|' tmp_list
		    rm "tmp_list"
		    IFS=" "
	    elif [ "$CMD" == "delhost" ] ; then
	        echo "Enter id..."
	        read ID
	        if [ -f "hosts/$ID" ] ; then
	            rm "hosts/$ID"
	            echo "Host deleted successfully"
	        else
	            echo "Host not found"
	        fi
	    elif [ "$CMD" == "scp" ] ; then
	        echo "Enter file path..."
	        read LPATH
	        echo "Enter target ID..."
	        read ID
	        echo "Enter target path..."
	        read TPATH
	        if [ -f "hosts/$ID" ] ; then
	            HOST=$(sed '2q;d' "hosts/$ID")
	            USERNAME=$(sed '3q;d' "hosts/$ID")
	            echo "Attempting to copy file to '$ID' ($USERNAME@$HOST)"
	            scp "$LPATH" "$USERNAME@$HOST:$TPATH"
	            echo "--------------------"
	        else
	            echo "Host with ID '$ID' not found"
	        fi
	    else
			if [ ! "$CMD" == "exit" ] ; then
	        	echo "Command not found"
			fi
	    fi
	done

	echo "Goodbye"
	RAN="Y"

fi
# https://stackoverflow.com/questions/965053/extract-filename-and-extension-in-bash
if [[ "$ARGS" == *"dunzip"* ]] ; then
	echo "Enter remote file URL"
	read RURL
	RBNAME=$(basename RURL)
	REXT="${filename##*.}"
	if [ "$REXT" == "zip" ] ; then
		wget "$RURL"
	else
		echo "ERROR: The requested file is not a ZIP file"
	fi
	RAN="Y"
fi
if [ "$RAN" == "N" ] ; then
	echo "Feature not found. Check out the README.md file to see a list of available features."
fi
