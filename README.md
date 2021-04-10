# Holberton Script Auto-format Files (HSAF)

In this project, I create a script that auto-format all the files to Betty Style and Pep8.
<img src="img/script.png"/>
## How to Install :floppy_disk:

### USE THE INSTALLER
Execute the INSTALLER.py in your terminal and grab a coffee while INSTALLER works.

 
### The old way to install HolbertonScript
1. Clone this repository in your terminal
` git clone https://github.com/nikolasribeiro/holbertonscript `
2. Make a new file with the script code like this: 
` cat script.py > up `
3. Move the file "up" to a PATH directory that you can use, in my case i have a directory named "custom_path" added to my PATH env
`mv up ~/custom_path`
4. Add execution permission to up file
`chmod +x up`
5. Type in your terminal: up -h
```
$ up -h

usage: up [-h] [-b] [-p] [-g] [-m] [file [file ...]]

positional arguments:
  file           File you want to check and upload

optional arguments:
  -h, --help     show this help message and exit
  -b, --betty    Format the code to betty style
  -p, --pep      Format the code to pep8 style
  -g, --git      This flag is a boolean, use this flag if you want to check and push your file
  -m, --message  You can set a message for commit (you can use this flag without -g flag)
```
## How it Works? :page_with_curl:

This script identifies the type of file that it reads and based on the file extension (.c, .h, .py) it begins to format with the specific recommendations for each type of file.
Then, when the script had finished of format, checks again if the files are ok with the standards of Betty style or Pep8, the push decision relay on you. If you think that any file are not correct formated, you can cancel the push to your github repository. 

This script was tested with my own holberton's repository and works excellent, feel free to try it and i hope you like it!

### Authors
*Nicolas Ribeiro* - [Github](https://github.com/nikolasribeiro) - nikolas.sebastian.ribeiro@gmail.com
