#!/usr/bin/python3

import argparse
import os
import sys

try:
    from termcolor import colored
except:
    print("...::: TERMCOLOR dependency does not exist, the program will install it at this moment:::...")
    os.system("sudo apt install python3-pip -y")
    os.system("pip3 install termcolor")
    print("---=== TERMCOLOR INSTALLED SUCCESSFULLY ===---")


def pintar_texto(texto, color="white"):
    return colored(texto, color)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="File you want to check with betty")
    parser.add_argument("-b","--betty", help="Betty checks your code for correct format", action="store_true")
    parser.add_argument("-g","--git", help="This flag is a boolean, use this flag if you want to check and push your file", action="store_true")
    parser.add_argument("-m","--message", help="You can set a message for commit (you can use this flag without -g flag)", action="store_true")

    return parser.parse_args()

def check_betty(file):
    os.system(f"betty {file}")

def push_process(text):

    print( pintar_texto("This is the actual git status", color="yellow") )
    os.system("git status")
    choice = input( pintar_texto("Do you want to save all the changes and commit? Y/n: ", color="yellow") )

    if choice in ["y","Y",""]:
        print( pintar_texto("..:: initializing the remote push process", color="green") )
        os.system("git add .")
        os.system(f"git commit -m {text}")
        os.system("git push")
        print( pintar_texto("push process successfully", color="green") )
    else:
        print("Process canceled by User")

def save_message(message):

    if message in ["q","Q"]:
        print("Cancel by User")
        sys.exit()

    if message != "":
        print( pintar_texto(f"Message {str(message)} saved!", color="green") )
    else:
        message = "commit"
        print( pintar_texto(f"Message {str(message)} saved!", color="yellow") )

    return message

def main():
    commit_message = ""
    args = get_args()

    if args.betty == False and args.git == False and args.message == False:
        
        print( pintar_texto("initializing push process", color="yellow") )
        os.system(f"betty {args.file}")
        confirm = input("Betty is ok? y/n: ")
        if confirm in ["y","Y"]:
            os.system("git status")
            os.system("git add .")
            os.system("git commit -m 'commit' ")
            os.system("git push")
            print( pintar_texto("Push process finished successfully!", color="green") )
        elif confirm in ["n","N"]:
            print( pintar_texto("Check betty and when you have finished, run again!", color="red") )
        else:
            print( pintar_texto("Invalid option, ending software", color="red") )
            sys.exit()
        
    else:
        if args.betty != False:
            check_betty(args.file)

        if args.message != False:
            print("To cancel this line, you can do Ctrl + C or type: q")
            commit_message = save_message( input("Insert message (if you dont put any message, by default, the commit message will be 'commit'): ") )
            

        if args.git != False:
            push_process(commit_message)

if __name__ == "__main__":
    main()