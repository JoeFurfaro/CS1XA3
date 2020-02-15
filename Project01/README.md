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


## Future Custom Features
### SSH Manager
Argument name: `sshman`
Description: Allows the user to create and store SSH server credentials and associate them with a certain ID to save time when connecting to saved servers that the user wants to use frequently. The user can add and delete hosts using the "add" and "del" commands, and can list all saved hosts using the "list" command. The user can also connect to one of there hosts or scp to one of their hosts using the "ssh" and "scp" commands and following the prompt asking which host they want to connect to.

### Download & Unzip
Argument name: `dunzip`
Description: Prompts the user to enter a remote URL of a file to download and a local path specifying where the downloaded ZIP file should be unzipped. The program then retrieves the file from the remote URL and unzips it in the specified directory, deleting temporary files as it works.
