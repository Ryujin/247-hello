import tkinter
from tkinter import *

def print_button():
    print('text')
def print_other():
    print('something else')

root = Tk()
frame = Frame(root, borderwidth="7", relief="sunken")
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

tx = Text(root, height=6, width=40, borderwidth=7, bg='lime')
tx.tag_configure("cent", justify="center", font="sans")
tx.tag_add("cent", 1.0, "end")
tx.pack(side = TOP)
tx.insert(END, "Looks like you've configured\nthis program to work with\nyour browser! If you've not\nresized or switched browsers,\njust skip the configuration.", "cent")
          
redbutton = Button(frame, text="Skip the configuration\nthis time", fg="red", command=print_other)
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Hit here if you\nwant to reconfigure", fg="brown", command=print_button)
greenbutton.pack( side = LEFT )
'''
bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black", bg="pink")
blackbutton.pack( side = BOTTOM)
'''
root.mainloop()
