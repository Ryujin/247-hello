import re, string, keyboard, time, pyautogui, webbrowser, pynput, threading, configparser, os
config = configparser.ConfigParser()
configfile_name = "config.ini"
pyautogui.FAILSAFE = True
from pynput.mouse import Listener
from tkinter import *
import tkinter as tk
master = tk.Tk()
master.title("Innovate!")
cfg = configparser.ConfigParser()
count = 3
config_ran = False
lbl = Label(master, text="None")
# from https://stackoverflow.com/questions/4103773/efficient-way-of-having-a-function-only-execute-once-in-a-loop
# maybe learn about decorators

def on_click3(x, y, button, pressed) :
    global xari2, yari2, xari0, yari0, lbl
    count = 3 
    while count > 0:
        if count == 2:
            xari2 = x
            yari2 = y
            write_config3(xari2, yari2)
        count -= 1
    print("Third Coordinates are " + str(x) + " and " + str(y))
    print("long, winding road")

def write_section3(section_name):
    global configfile_name
    c = open(configfile_name, "a", encoding="utf-8")
    c.write('[' + section_name + '] \r')
    c.close()
    print("Okay, that's it!")

def crush3():
    master.title("Third Step 3 3 3 3 3!")
    listener3 = Listener(on_click3=on_click3)
    listener3.start()
    write_section3("pickup")
    listener3.stop() 

def on_click2(x, y, button, pressed) :
    global xari2, yari2, xari0, yari0, lbl
    count = 3 
    while count > 0:
        if count == 2:
            xari2 = x
            yari2 = y
            write_config2(xari2, yari2)
        count -= 1
    print("2nd Coordinates are " + str(x) + " and " + str(y))
    crush3() #sort of wo

def write_config2(x_coord, y_coord):
    global configfile_name
    c = open(configfile_name, "a", encoding="utf-8")
    c.write('x=' + str(x_coord) + '\r')
    c.write('y=' + str(y_coord))
    c.write('This was config2!')
    c.write('\r\n')
    print(str(c))
    c.close()

def write_section2(section_name):
    global configfile_name
    c = open(configfile_name, "a", encoding="utf-8")
    c.write('[' + section_name + '] \r')
    c.close()
    write_config(x,y)
    # Must jump into write_config2 from here
    #crush3() doesn't quite work 

def crush2():
    global lbl   ###no no no no
    #  listener.stop()
    lbl.destroy()
    master.title("Step two!")
    lbl = Label(master, text="Now to click below the linke")
    lbl.pack()
    listener2 = Listener(on_click2=on_click2)
    listener2.start()
    write_section2("pickup")
    #listener2.stop() 

def write_config(x_coord, y_coord):
    global configfile_name, config_ran
    if config_ran:
        return
    c = open(configfile_name, "a", encoding="utf-8")
    c.write('x=' + str(x_coord) + '\r')
    c.write('y=' + str(y_coord))
    c.write('\r\n')
    print(str(c))
    c.close()
    config_ran = True
    crush2()    # NO EFFECT

def matin():
    print("Space Force!")

def on_click(x, y, button, pressed) :
    global xari2, yari2, xari0, yari0, lbl, listener
    count = 3 
    while count > 0:
        if count == 2:
            xari2 = x
            yari2 = y
            write_config(xari2, yari2)
        count -= 1
  #  listener.stop()   # doesn't work here
 #   crush2() #sort of works almost
    # doesn't quite work, either crush3()
#here it needs to write the coordinates ONCE and then move along to next section!   

def write_section(section_name):
    global configfile_name
    c = open(configfile_name, "w", encoding="utf-8")
    c.write('[' + section_name + '] \r')
    c.close()
    #crush2()   DOES NOT WORK!

def write_prelude(v):   
    #with Listener(on_click=on_click) as listener:
    listener = Listener(on_click=on_click)
    listener.start()
        #listener.join()
    write_section(v) 
   # listener.stop()   ### CANNOT WORK HERE

    
def crush():
    frame.destroy()
    tx.destroy()
    redbutton.destroy()
    greenbutton.destroy()
    master.title("Map your screen")
    lbl = Label(master, text="With the QP chat interface screen up,\nclick the 'New' tab at upper left above the blue bar", font=("Helvetica", 14))
    lbl.pack()
    print("label is a " + str(type(lbl)))
    write_prelude('tab')
    #listener.stop()  ## now, it doesn't :-(   ### sort of works here...

    '''
    master.title("Step two")
    lbl2 = Label(master, text="Now, click just below the blue bar", font=("Helvetica", 14))
    lbl2.pack()
    write_prelude('pickup')
'''
def popupmsg(msg):
    global master
    master.destroy
    popup = tk.Tk()
    popup.wm_title("Step one!")
    label = tk.Label(popup, text=msg, font=("Helvetica", 10))
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

if not os.path.isfile('config1.ini'):
    print("In this case, we must run configuration")   
else:
    frame = Frame(master, borderwidth="7", relief="sunken")
    frame.pack()
    bottomframe = Frame(master)
    bottomframe.pack( side = BOTTOM )
    tx = Text(bottomframe, height=6, width=40, borderwidth=7, bg='lime')
    tx.tag_configure("cent", justify="center", font="sans")
    tx.tag_add("cent", 1.0, "end")
    tx.pack(side = TOP)
    tx.insert(END, "Looks like you've configured\nthis program to work with\nyour browser! If you've not\nresized or switched browsers,\njust skip the configuration.", "cent")
    redbutton = Button(frame, text="Skip the configuration\nthis time", fg="red", command=crush)
    redbutton.pack( side = LEFT)
    greenbutton = Button(frame, text="Hit here if you\nwant to reconfigure", fg="brown", command=lambda: popupmsg("This is controversial, but you will need to click a couple things..."))
    greenbutton.pack( side = LEFT )
    master.mainloop()
