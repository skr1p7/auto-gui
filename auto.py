#!/usr/bin/python3

from tkinter import *

import os

def git():
	os.system("firefox https://github.com")

def twit():
	os.system("firefox https://twitter.com/home")

def radio():
	os.system("firefox https://www.accuradio.com/heavy-metal/")
	
root = Tk()

root.title("CodeForces Info")

root.geometry("320x260+0+0")


git = Button(root, text="Open GitHub", width = 33, height=2, bg="white", command=git).place(x=12, y=30)

twit = Button(root, text="My Twitter Feed", width = 33, height=2, bg="white", command=twit).place(x=12, y=80)

music = Button(root, text="AccuRadio", width = 33, height=2, bg="white", command=radio).place(x=12, y=130)

quit = Button(root, text="Quit", width = 33, height=2, bg="white", command=root.destroy).place(x=12, y=180)

root.mainloop()