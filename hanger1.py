import pyperclip, re, string, keyboard, time, pyautogui, webbrowser, titlecaseMod, pynput, threading, tkinter, configparser, os
#ANOTHER THING: SHOULD BE SIMPLE TO SCRAPE LOCATION FROM, E.G. https://www.ip2location.com/demo/172.91.22.94
config = configparser.ConfigParser()
text = pyperclip.paste()
pyautogui.FAILSAFE = True
from titlecaseMod import titlecase
from pynput.mouse import Listener
from tkinter import *
from tkinter import ttk
root = Tk()
count = 0 
cfg = configparser.ConfigParser()

def reconfig():
    print("Reconfigure!")
def main():
    print("Space Force!")

if not os.path.isfile('config.ini'):
    print("In this case, we run configuration")   
else:
    frame = Frame(root, borderwidth="7", relief="sunken")
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack( side = BOTTOM )
    tx = Text(root, height=6, width=40, borderwidth=7, bg='lime')
    tx.tag_configure("cent", justify="center", font="sans")
    tx.tag_add("cent", 1.0, "end")
    tx.pack(side = TOP)
    tx.insert(END, "Looks like you've configured\nthis program to work with\nyour browser! If you've not\nresized or switched browsers,\njust skip the configuration.", "cent")
    redbutton = Button(frame, text="Skip the configuration\nthis time", fg="red", command=main)
    redbutton.pack( side = LEFT)
    greenbutton = Button(frame, text="Hit here if you\nwant to reconfigure", fg="brown", command=reconfig)
    greenbutton.pack( side = LEFT )
    root.mainloop()
