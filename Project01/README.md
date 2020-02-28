# CS1XA3 Project01 - furfaroj

## Getting Started
If authorized to do so, clone the course repository into a local directory of your choice.

    git clone https://github.com/JoeFurfaro/CS1XA3.git
Now make sure the project shell script is executable.

    chmod +x CS1XA3/Project01/project_analyze.sh
    
## Usage
Once you have made the project script executable, it can be executed using the following syntax:

    ./project_analyze.sh [feature_1] <feature_2> <feature_n>
Where features 1 through n can be any of the following case-sensitive feature names:

 - fixme
 - filesize
 - typecount
 - findtag
 - lastmerge
 - backuprestore
 - sshman
 - dunzip

Any number of feature arguments can be specified, however, features that are specified with duplicity will not be run more than once.

## Available Features
The following features are currently included in **project_analyze.sh** and can be specified through the script arguments.
### #FIXME
Argument name: `fixme`
Description: Outputs the name of each file in the CS1XA3 repository whose last line contains the string fragment `#FIXME`
Reference Used:
 - https://stackoverflow.com/questions/46163678/get-rid-of-warning-command-substitution-ignored-null-byte-in-input

### File Size List
Argument name: `filesize`
Description: Outputs a list of all files in the CS1XA3 repository along with a human-readable representation of their respective size. The list is ordered from largest file size to smallest file size.
Reference Used:
 - https://unix.stackexchange.com/questions/22432/getting-size-with-du-of-files-only

### File Type Count
Argument name: `typecount`
Description: Prompts the user to enter a specific file extension. Will output the number of files in the CS1XA3 repository whose extensions match the user's input.

### Find Tag
Argument name: `findtag`
Description: Prompts the user to enter a tag name. Outputs a list of python comments in the repository that contain the user-inputted tag as a sub-string. Saves the outputted list to a file called {TAG_NAME}.log

### Last Merge
Argument name: `lastmerge`
Description: Checks out the last commit whose commit message contains the sub-string "merge" in a detached head state.

### Backup and Restore
Argument name: `backuprestore`
Description: Allows the user to backup, delete, and restore all .tmp files in the repository. Will prompt user to choose a feature (backup or restore)
Usage:

 - Backup mode: Use select feature ID `b` to run backup mode. This mode will delete all .tmp files in the repository from there original location and will move them to a backup folder in the same directory as the project script. It will also save a reference map containing the original locations of each backed-up file.
 - Restore mode: Use the select feature ID `r` to run restore mode. This mode will restore and copy all files from the backup folder to their original location while also keeping them and their backed-up location just in case.

## Custom Features
### SSH Manager
Argument name: `sshman`
Description: Allows the user to store SSH server credentials and associate them with ID aliases to save time when connecting to saved servers that the user wants to use frequently. Available as a shell that prompts the user to enter the sub-commands listed below.

**Sub-command List:**

 - `addhost` Creates a saved host under a custom ID alias. Will prompt the user to enter an ID, hostname, and username
 - `delhost` Deletes a saved host. Will prompt the user to enter a host ID
 - `hosts` Lists all the available saved hosts in a column format
 - `ssh` Opens an SSH session with the specified host ID. Will prompt the user to enter a host ID
 - `scp` Securely copies a file from the local machine to a remote location. Will prompt the user to enter a local path, host ID, and remote path
 - `exit` Exits the SSHMan shell

### Download & Unzip
Argument name: `dunzip`
Description: Prompts the user to enter a remote URL of a file to download and a local path specifying where the downloaded ZIP file should be unzipped. The program then retrieves the file from the remote URL and unzips it in the specified directory, deleting temporary files as it works. A test ZIP file can be found at the URL `http://mac1xa3.ca/u/furfaroj/test/dir.zip`
Reference Used:
 - https://stackoverflow.com/questions/965053/extract-filename-and-extension-in-bash
