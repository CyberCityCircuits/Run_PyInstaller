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

#set console size and color
os.system('mode con: cols=50 lines=20')
os.system('color F')
os.system('cls')
os.system('echo off')

#set varibales
ver = ("0.01.00")
wait = (2)
currdate = dt.date.today().strftime("%Y%m%d")
currtime = dt.datetime.now().strftime("%H%M")

#define commands
#logo
def logo():
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("")
    print ("             Run_PyInstaller " + ver)
    print ("                   David A Ray")
    sleep(wait)

#ask for input
def user_input():
    global app_py, app_name, app_version
    os.system('cls')
    print ("")
    app_py = raw_input("  What is the '.py' file to compile?: ")
    app_name = raw_input("  What is the name of the applicaton?: ")
    app_version = raw_input("  What version are you compiling?: ")
    
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
        filename = (app_name + " " + app_version + " " + currdate + " " + currtime)                
    else:
        print ("")
        print ("  Please Check Info and Try Again.")
        print ("")
        os.system("pause")
        exit()
        
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

def ren_dist():
    os.rename('dist', filename)

#run commands
logo()
user_input()
confirm()
chk_file() 
run_pyinstaller()
ren_dist()
