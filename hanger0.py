import pyperclip, re, string, keyboard, time, pyautogui, webbrowser, titlecaseMod, pynput, threading, tkinter, configparser, os
from pynput.mouse import Listener
from tkinter import *
configfile_name = "config.ini"
cfg = configparser.ConfigParser()

def write_config(x_coord, y_coord):
    global configfile_name
    c = open(configfile_name, "a", encoding="utf-8")
    c.write('x=' + x_coord + '\r')
    c.write('y=' + y_coord)
    c.write('\r\n')
    c.close()
def write_section(section_name):
    global configfile_name
    c = open(configfile_name, "a", encoding="utf-8")
    c.write('[' + section_name + '] \r')
    c.close()
count = 3
def on_click(x, y, button, pressed) :
    global xari2, yari2, xari0, yari0, xari3, yari3
    global count
    while count > 0:
        if count == 2:
            xari2 = x
            yari2 = y
        count -= 1
    write_config(str(x), str(y))
    window.after(2000, window.destroy)    
    listener.stop()

window = Tk()
window.title("Map your screen")
window.geometry('350x80+300+225')
window.lift()
ws = window.winfo_screenwidth()
write_section('tab')
lbl = Label(window, text="With the QP chat interface screen up,\nclick the 'New' tab at upper left above the blue bar")
lbl.grid(column=0, row=0)
with Listener(on_click=on_click) as listener:
    window.mainloop()
    listener.join()
listener.stop()
write_section('pickup')
count = 3
window = Tk()
window.title("Step two!")
window.geometry('350x80+300+225')
window.lift()
lbl = Label(window, text="Now, click just below the blue bar")
lbl.grid(column=0, row=0)
with Listener(on_click=on_click) as listener:
    window.mainloop()
    listener.join()
listener.stop()
write_section('paste')
count = 3
window = Tk()
window.title("Step three!")
window.geometry('350x80+300+225')
window.lift()
lbl = Label(window, text="Lastly, click in the text box")
lbl.grid(column=0, row=0)
with Listener(on_click=on_click) as listener:
    window.mainloop()
