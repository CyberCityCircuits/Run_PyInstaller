# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:18:16 2017

@author: admin
"""

import var, tasks

import os, sys
import datetime as dt
from pathlib import Path
#from bs4 import BeautifulSoup as bs
import lxml.etree as et

#from tkinter import *
from tkinter import Menu, Frame, BOTH, W
from tkinter import Tk, Label, messagebox


class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        
        
        self.init_window()
        

    def init_window(self):
        self.master.title(var.app_name)
        
        topbar = Menu(self.master)
        self.master.config(menu=topbar)
        
        file_menu = Menu(topbar)
        build_menu = Menu(topbar)
        tools_menu = Menu(topbar)
        help_menu = Menu(topbar)
        
        file_menu.add_command(label="Exit", command=tasks.client_exit)
        topbar.add_cascade(label="File", menu=file_menu)

        
        build_menu.add_command(label="Compile Python Script")
        build_menu.add_command(label="Compile Python Script with No Console")
        topbar.add_cascade(label="Build", menu=build_menu)
        
        tools_menu.add_command(label ="Install PyInstaller")
        tools_menu.add_command(label="Upgrade PyInstaller")
        topbar.add_cascade(label="Tools", menu=tools_menu)
        
        
        help_menu.add_command(label="Directions", command=funct_not_supp)
        help_menu.add_command(label="About", command=show_about)
        topbar.add_cascade(label="Help", menu=help_menu)
        
def funct_not_supp():
    msg_error("Function Not Yet Supported")
    
def msg(text):
    messagebox.showinfo(var.app_name, text)
    
def msg_error(text):
    messagebox.showerror(var.app_name, text)

#command for help > about
def show_about():
    msg(var.name + "\n"
        "Build: " + var.build + "\n\n"
        "By David Ray \n"
        "\n" + var.email + "\n\n"
        "www.DREAM-Enterprise.com")
    
    
    
                
root = Tk()

w = var.width # width for the Tk root
h = var.lines #height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/4) - (w/2)
y = (hs/2.5) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))


    
app = Window(root)    

root.mainloop()

     