#!/usr/bin/env python3
import argparse
import os
import sys

try:
    from termcolor import colored
except:
    print("...::: TERMCOLOR dependency does not exist, the program will install it at this moment:::...")
    os.system("sudo apt install python3-pip -y")
    os.system("pip3 install termcolor")
    os.system("pip3 install autopep8")
    os.system("sudo apt install clang-format")
    print("---=== TERMCOLOR INSTALLED SUCCESSFULLY ===---")


def pintar_texto(texto, color="white"):
    return colored(texto, color)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file", help="File you want to check and upload", nargs="*"
    )
    parser.add_argument(
        "-b", "--betty", help="Format the code to betty style", action="store_true"
    )
    parser.add_argument(
        "-p", "--pep", help="Format the code to pep8 style", action="store_true"
    )
    parser.add_argument(
        "-g", "--git", help="This flag is a boolean, use this flag if you want to check and push your file", action="store_true"
    )
    parser.add_argument(
        "-m", "--message", help="You can set a message for commit (you can use this flag without -g flag)", action="store_true"
    )

    return parser.parse_args()


def format_betty(file):
    import getpass
    NAME_SYSTEM_USER = getpass.getuser()

    BETTY_STYLE = """{BasedOnStyle: LLVM, UseTab: Always, IndentWidth: 4, TabWidth: 4, BreakBeforeBraces: Allman,
                   AllowShortIfStatementsOnASingleLine: false, IndentCaseLabels: false, ColumnLimit: 0, AccessModifierOffset: -4}"""

    print(pintar_texto("...::: Formatting file: --> {} <--".format(file), color="green"))
    
    if NAME_SYSTEM_USER == "vagrant":
        print("SOY VAGRANT!!")
    else:
        print("SOY UN SISTEMA OPERATIVO!!")
    os.system('clang-format -i {} -style="{}"'.format(file, BETTY_STYLE))
 

def format_pep(file):
    print(pintar_texto("...::: Formatting file: --> {} <--".format(file), color="yellow"))
    os.system("autopep8 -i {}".format(file))


def push_process(text):

    print(pintar_texto("This is the actual git status", color="yellow"))
    os.system("git status")
    choice = input(pintar_texto(
        "Do you want to save all the changes and commit? Y/n: ", color="yellow"))

    if choice in ["y", "Y", ""]:
        print(pintar_texto("..:: initializing the remote push process", color="green"))
        os.system("git add .")
        os.system("git commit -m {}".format(text))
        os.system("git push")
        print(pintar_texto("push process successfully", color="green"))
    else:
        print("Process canceled by User")


def save_message(message):

    if message in ["q", "Q"]:
        print("Cancel by User")
        sys.exit()

    if message != "":
        print(pintar_texto("Message {} saved!".format( str(message) ), color="green"))
    else:
        message = "commit"
        print(pintar_texto("Message {} saved!".format( str(message) ), color="yellow"))

    return message


def main():
    commit_message = ""
    args = get_args()

    for files in args.file:

        # Checks if the flag exist
        if args.betty != False:
            format_betty(files)
            break

        if args.message != False:
            print("To cancel this line, you can do Ctrl + C or type: q")
            commit_message = save_message(input(
                "Insert message (if you dont put any message, by default, the commit message will be 'commit'): "))

        if args.git != False:
            push_process(commit_message)
            break

        if args.pep != False:
            format_pep(files)
            break

        # Check the extension of the files
        if files.endswith(".c") or files.endswith(".h"):
            format_betty(files)

        elif files.endswith(".py"):
            format_pep(files)

    #Verifying the format
    print(pintar_texto("Checking that all the formats are ok"))
    os.system("betty *.c && betty *.h && pep8 *.py")
    confirm = input("Everything is ok? Y/n: ")
    print(pintar_texto("initializing push process", color="yellow"))
    
    if confirm in ["y", "Y", ""]:
        os.system("git status")
        os.system("git add -A")
        commit_message = save_message(input(
            "Insert message (if you dont put any message, by default, the commit message will be 'commit'): "))
        os.system("git commit -m {} ".format(commit_message))
        os.system("git push")
        print(pintar_texto(
            "Push process finished successfully!", color="green"))
    elif confirm in ["n", "N"]:
        print(pintar_texto(
            "Check the format and when you have finished, run again!", color="red"))
    else:
        print(pintar_texto("Invalid option, ending software", color="red"))
        sys.exit()


if __name__ == "__main__":
    main()
