#!/usr/bin/python3

""" 
Script Installer 
Author: Nicolas Ribeiro
"""
import os

LOCATION_LANGUAGE = "es_UY.UTF-8"

# Installing main dependences
print("...:::/// Installing all the neccessary dependences ///:::...")
os.system("sudo apt install python3-pip -y")
os.system("sudo pip3 install termcolor")
os.system("sudo pip3 install autopep8")
os.system("sudo pip3 install pycodestyle")
os.system("sudo pip3 install yapf")
os.system("sudo pip3 install black")
os.system("sudo apt-get install clang-format-3.4")
os.system("sudo apt-get install clang-format")
os.system("sudo locale-gen {}".format(LOCATION_LANGUAGE))
os.system("sudo dpkg-reconfigure locales")
os.system("cat script.py > up && sudo mv up /usr/local/bin && sudo chmod +x /usr/local/bin/up")

print("...:::/// Holberton Script AutoFormatter was installed successfully ///:::...")
print("Testing the script")
os.system("up -h")
print("If the commands shows: 'up: command not found, means that the install dont work' ")
print("If not shows that, congratulations! you have your own autoformatter :)")
