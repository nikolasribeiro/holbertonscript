import argparse
import os

try:
    from termcolor import colored
except:
    print("...::: No se encontro la dependencia TERMCOLOR, el programa procedera a instalarlo a continuacion :::...")
    os.system("sudo apt install python3-pip -y")
    os.system("pip3 install termcolor")
    print("---=== TERMCOLOR INSTALADO ===---")


def pintar_texto(texto, color="white"):
    return colored(texto, color)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b","--betty", help="Betty checks your code for correct format")
    parser.add_argument("-g","--git", help="This flag is a boolean, use this flag if you want to check and push your file", action="store_true")
    parser.add_argument("-m","--message", help="You can set a message for commit (you can use this flag without -g flag)")

    return parser.parse_args()

def check_betty(file):
    os.system(f"betty {file}")


def main():
    commit_message = ""
    args = get_args()

    if args.betty != None:
        check_betty(args.betty)

    if args.message != None:
        commit_message = args.message
        if args.git:
            print(f"Commit Message: {commit_message}")
        else:
            print(f"Commit Message saved successfully")
    
    if args.git:
        print( pintar_texto("This is the actual git status", color="yellow") )
        os.system("git status")
        choice = input( pintar_texto("Do you want to save all the changes and commit? Y/n: ", color="yellow") )

        if choice in ["y","Y"]:
            print( pintar_texto("..:: Inicializing the remote push process", color="green") )
            os.system("git add .")
            os.system(f"git commit -m {commit_message}")
            os.system("git push")
            print( pintar_texto("push process successfully", color="green") )
        else:
            print("Process canceled by User")





if __name__ == "__main__":
    main()