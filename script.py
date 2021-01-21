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
    os.system("pip3 install yapf")
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

    parser.add_argument(
        "-d", "--docs", help="With this flag you can add all the documentation of class, methods and functions automatically", action="store_true"
    )

    return parser.parse_args()


def add_comments_to_python_file(text_file):
    print(pintar_texto("...::: Adding Documentation for file: --> {} <--".format(text_file), color="yellow"))

    comment = '''""" {} {} """'''
    content_file = ""

    # Leemos el archivo y manipulamos el contenido
    with open(text_file, 'r') as file:
        content = file.read().splitlines()
        for n_line, line in enumerate(content):

            # Add Shebang
            if n_line+1 == 1 and "#!/usr/bin/python3" not in line:
                content_file += "#!/usr/bin/python3"+"\n"
                content_file += '\n\n""" Module {}"""'.format(text_file[:-3])+"\n"
            
            #Busca si existe la sintaxis class
            if line.startswith("class") and line.endswith(":"):
                name_of_class = line[line.find("class")+6:line.find("(") or line.find(":")]
                add_class_doc = comment.format("class", name_of_class)
                line = line.rstrip()

                if add_class_doc not in content[n_line+1]:
                    line = line.replace(line, line + "\n{}".format(chr(32)*4) + add_class_doc)
                else:
                    line = line
  
            #Busca si la funcion que encontro es un metodo o una funcion comun
            if line.strip().startswith("def") and line.strip().endswith(":") and "self" in line:
                name_of_def = line[line.find("def")+4:line.find("(") or line.find(":")]
                add_method_doc = comment.format("function", name_of_def)
                line = line.rstrip()

                if add_method_doc not in content[n_line+1]:
                    line = line.replace(line, line + "\n{}".format(chr(32)*8) + add_method_doc)
                else:
                    line = line
            
            #Busca una funcion comun
            if line.strip().startswith("def") and line.strip().endswith(":"):
                name_of_def = line[line.find("def")+4:line.find("(") or line.find(":")]
                add_function_doc = comment.format("function", name_of_def)
                line = line.rstrip()

                if add_function_doc not in content[n_line+1]:
                    line = line.replace(line, line + "\n{}".format(chr(32)*4) + add_function_doc)
                else:
                    line = line


            # Guardamos todo el contenido en la variable para despues, reescribir todo
            content_file += (line+'\n')

    # Escribimos en el archivo todo el contenido del mismo
    with open(text_file, "w") as file:
        file.writelines(content_file)


def format_betty(file):
    BETTY_STYLE = """{BasedOnStyle: LLVM, UseTab: Always, IndentWidth: 4, TabWidth: 4, BreakBeforeBraces: Allman,
                   AllowShortIfStatementsOnASingleLine: false, IndentCaseLabels: false, ColumnLimit: 0, AccessModifierOffset: -4}"""

    print(pintar_texto("...::: Formatting file: --> {} <--".format(file), color="green"))
    os.system('clang-format-3.4 -i {} -style="{}"'.format(file, BETTY_STYLE))
 

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
            add_comments_to_python_file(files)
            format_pep(files)

    #Verifying the format
    print(pintar_texto("Checking that all the formats are ok"))
    os.system("betty *.c")
    os.system("betty *.h")
    os.system("pep8 *.py")
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
