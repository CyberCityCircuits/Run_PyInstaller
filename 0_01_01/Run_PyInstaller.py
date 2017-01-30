# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 13:16:05 2016

@author: David Ray
"""

#import libraries
import os
import datetime as dt
from pathlib import Path
from time import sleep
from shutil import copyfile as copy

#set console size and color
os.system('mode con: cols=50 lines=20')
os.system('color F')
os.system('cls')
os.system('echo off')

#set varibales
ver = ("0.01.01")
wait = (2)
currdate = dt.date.today().strftime("%Y%m%d")
currtime = dt.datetime.now().strftime("%H%M")
package = ("pyinstaller")
text1 = ("readme.txt")
text2 = ("changelog.txt")

#define commands
#logo
def logo():
    os.system("cls")
    print ("")
    print ("")
    print ("             Run_PyInstaller " + ver)
    print ("                   David A Ray")
    print ("")
    print ("")
    print ("      This software will compile your '.py'")
    print ("      scripts using the PyInstaller package.")
    print ("        It will also copy any files named")
    print ("      'readme.txt' or 'changelog.txt' to the")
    print ("     directory your compiled script is put in.")
    print ("")
    print ("  1 - Countinue to Compiler")
    print ("  2 - Install/Upgrade PyInstaller")
    print ("  3 - Exit")
    confirm = raw_input("  Choose your option [1/2/3]: ")
    if confirm == ("2"):
        install_menu()
    elif confirm == ("1"):
        user_input()
    elif confirm == ("3"):
        exit()
    else:
        logo()

def install_menu():
    os.system('cls')
    print ("")
    print ("")
    print ("")
    print ("  Internet Connection is Required to Install.")
    print ("")
    print ("")
    print ("  1 - New Install of PyInstaller")
    print ("  2 - Install Upgrade of Pyinstaller")
    print ("")
    var_install = raw_input("  Choose your option [1/2]: ")
    if var_install == ("1"):
        print ("")        
        print ("  Installing...")
        sleep(.5)
        install()
    elif var_install == ("2"):
        print ("")        
        print ("  Upgrading...")
        sleep(.5)
        upgrade()
    else:
        logo()
        
#install PyInstaller
def install():
    os.system ("pip install " + package)
    print ("")
    print ("")
    print ("  Installation Complete")
    print ("")
    print ("")
    os.system("pause")
    logo()
    
# upgrade PyInstaller
def upgrade():
    os.system ("pip install --upgrade " + package)
    print ("")
    print ("")
    print ("  Installation Complete")
    print ("")
    print ("")
    os.system("pause")
    logo()
    
#ask for input
def user_input():
    global app_py, app_name, app_version
    os.system('cls')
    print ("")
    app_py = raw_input("  What is the '.py' file to compile?:  ")
    app_name = raw_input("  What is the name of the applicaton?: ")
    app_version = raw_input("  What version are you compiling?:     ")
    confirm()
    
#confirm data from user_input()
def confirm():
    global filename
    print ("")
    print ("  File to Compile:          ") + app_py
    print ("  Name of the Application:  ") + app_name
    print ("  Version of Application:   ") + app_version
    print ("  Build Date:               ") + currdate
    print ("  Build Time:               ") + currtime
    print ("")
    confirm = raw_input("  Is this correct? (Y/N): ")
    if confirm == 'y' or confirm == 'Y':
        print ("")
        filename = (app_name + " " + app_version + " - " + currdate + " " + currtime)                
    else:
        print ("")
        print ("  Please Check Info and Try Again.")
        print ("")
        os.system("pause")
        user_input()
        
def chk_file():
    file = Path(app_py)    
    if not file.is_file():
        os.system('cls')
        print ("")
        print ("")
        print ("")
        print ("")
        print ("                 FILE NOT FOUND")
        print ("")
        print ("        Please move your " + app_py + " file to")
        print ("        this directory.")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        os.system("pause")
        exit()

#run pyinstaller
def run_pyinstaller():
    os.system('pyinstaller ' + app_py + ' -F')

#rename the 'dist' directory
def ren_dist():
    os.rename('dist', filename)

#copt readme files
def copy_readme():
    test_text1 = Path(text1)
    if test_text1.is_file():
        copy(text1,filename + "/" + text1) 
    test_text2 = Path(text2)    
    if test_text2.is_file():
        copy(text2,filename + "/" + text2)
        
#run commands
logo()
chk_file() 
run_pyinstaller()
ren_dist()
copy_readme()