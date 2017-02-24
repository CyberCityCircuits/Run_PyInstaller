# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 13:16:05 2016

@author: David Ray
"""

#import libraries
import os
import sys
import datetime as dt
from pathlib import Path
from time import sleep
from shutil import copyfile as copy
from shutil import rmtree as rm_dir

#set varibales
application = "Run_PyInstaller"
ver = "0.01.07"
op_code = 0

email = "David@DREAM-Enterprise.com"

package = "pyinstaller"
text1 = "readme.txt"
text2 = "changelog.txt"

#set system varibles
width = 60
lines = 20
cent_width = int(width)-1
currdate = dt.date.today().strftime("%Y%m%d")
currtime = dt.datetime.now().strftime("%H%M")

wait = .5
splash_wait = 2

#define cosole size and color
os.system("mode con: cols=" + str(width) + " lines=" + str(lines))
os.system("color F")
os.system("cls")
os.system("echo off")

#define commands
#logo
def logo():
    init()
    os.system("cls")
    print ()
    print ()
    print ((application + " V" + ver).center(cent_width))
    print ("David A Ray".center(cent_width))
    print ()
    print (("Contact: " + email).center(cent_width))
    print ()
    print ()
    print (("This software will compile your '.py'").center(cent_width))
    print (("scripts using the PyInstaller package.").center(cent_width))
    print (("It will also copy any files named").center(cent_width))
    print (("'readme.txt' or 'changelog.txt' to the").center(cent_width))
    print (("directory your compiled script is put in.").center(cent_width))
    print ()
    print ("  0 - Exit")
    print ()
    print ("  1 - Countinue to Compiler")
    print ("  2 - Install/Upgrade PyInstaller")
    option = input("  Choose your option [0/1/2]: ")
    if option == ("2"):
        install_menu()
    elif option == ("1"):
        user_input()
    elif option == ("0"):
        end()
    else:
        logo()

def delete_file(file):
    if os.path.isfile(file):
        os.remove(file)
        
def delete_dir(dir_name):
    if os.path.exists(dir_name):
        rm_dir(dir_name)
        
def init():
    global app_name, app_py, app_version
    app_name = "null"
    app_py = "null"
    app_version = "null"
        
def complete():
    os.system("cls")
    print ()
    print ()
    print ("...Process Complete...".center(cent_width))
        
def end():
    print ()
    print ()
    print (("...Program Ending...").center(cent_width))
    print ()
    sleep(splash_wait)
    sys.exit()
    

def install_menu():
    os.system('cls')
    print ()
    print ()
    print ((application + " V" + ver).center(cent_width))
    print ()
    print ("  Internet Connection is Required to Install.")
    print ()
    print ()
    print ("  0 - Main Menu")
    print ()
    print ("  1 - New Install of PyInstaller")
    print ("  2 - Install Upgrade of Pyinstaller")
    print ()
    var_install = input("  Choose your option [1/2]: ")
    if var_install == ("1"):
        print ()        
        print ("  Installing...")
        sleep(wait)
        install()
    elif var_install == ("2"):
        print ()        
        print ("  Upgrading...")
        sleep(wait)
        upgrade()
    elif var_install == ("0"):
        logo()
    else:
        logo()
        
#install PyInstaller
def install():
    os.system ("pip install " + package)
    os.system("cls")
    print ()
    print ()
    print ((application + " V" + ver).center(cent_width))
    print ()
    print ()
    print ("  Installation Complete")
    print ()
    print ()
    os.system("pause")
    logo()
    
# upgrade PyInstaller
def upgrade():
    os.system ("pip install --upgrade " + package)
    os.system("cls")
    print ()
    print ()
    print ((application + " V" + ver).center(cent_width))
    print ()
    print ()
    print ("  Upgrade Complete")
    print ()
    print ()
    os.system("pause")
    logo()
    
#ask for input
def user_input():
    global app_py, app_name, app_version
    os.system('cls')
    print ()
    app_name = input("  What is the name of the applicaton?:  ")
    app_version = input("  What version are you compiling?:  ")
    option = input("  Is your script and application named alike? (Y/N):  ")
    if option.lower() == ("y") or option.lower() == ("yes"):
        app_py = (app_name + ".py")
    elif option.lower() == ("n") or option.lower() == ("no"):
        app_py = input("  What is the '.py' file to compile?:  ")
    else:
        print ()
        print ("  Please Check Info and Try Again.")
        print ()
        os.system("pause")
        user_input()
    user_chk()
    
#confirm data from user_input()
def user_chk():
    global op_code
    global filename
    
    print ()
    print ("  File to Compile:          " + app_py)
    print ("  Name of the Application:  " + app_name)
    print ("  Version of Application:   " + app_version)
    print ("  Build Date:               " + currdate)
    print ("  Build Time:               " + currtime)
    print ()
    print ("Option Codes:")
    print ("1 - No Console (Used with GUIs)")
    print ()
    option = input("  Is this correct? (Y/N): ")
    if option.lower() == ("y") or option.lower() == ("yes"):
        print ()
        filename = (app_name + " " + app_version + " - " + currdate + " " + currtime)                
    elif option == "1":
        op_code = 1
        user_chk()
    else:
        print ()
        print ("  Please Check Info and Try Again.")
        print ()
        os.system("pause")
        user_input()
        
def chk_file():
    file = Path(app_py)    
    if not file.is_file():
        os.system('cls')
        print ()
        print ()
        print ()
        print ()
        print ("FILE NOT FOUND".center(cent_width))
        print ()
        print (("Please move your " + app_py + " file to").center(cent_width))
        print (("this directory.").center(cent_width))
        print ()
        print ()
        print ()
        print ()
        print ()
        print ()
        print ()
        os.system("pause")
        logo()

#run pyinstaller
def run_pyinstaller():
    if op_code == str(1):
        os.system('pyinstaller --noconsole ' + app_py + ' -F')
    else:
        os.system('pyinstaller ' + app_py + ' -F')

#rename the 'dist' directory
def ren_dist():
    os.rename('dist', filename)

#copy readme files
def copy_readme():
    test_text1 = Path(text1)
    if test_text1.is_file():
        copy(text1,filename + "/" + text1) 
    test_text2 = Path(text2)    
    if test_text2.is_file():
        copy(text2,filename + "/" + text2)
        
#define main
def main():
    logo()
    chk_file() 
    run_pyinstaller()
    ren_dist()
    copy_readme()
    delete_file(app_name + ".spec")
    delete_dir("__pycache__")
    delete_dir("build")
    
    complete()
    end()

if __name__ == '__main__':
    main()