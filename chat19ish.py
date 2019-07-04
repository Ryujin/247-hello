import pyperclip, re, string, time, pyautogui, webbrowser, titlecaseMod, pynput, threading, tkinter
#TODO: Make a module that massages the library names -> Tacked this into titlecaseMod
#CAN main() BE KICKED OFF BY A KEYBOARD COMMAND, PROGRAM 'SLEEPS' B/N INVOCATIONS, VARS DEFINED IN HEAD SECTION?
text = pyperclip.paste()
pyautogui.FAILSAFE = True
from titlecaseMod import titlecase
from pynput.mouse import Listener
from tkinter import *

xari = 6 ; yari = 7 ; count = 3
#def fix_coordinates(): Need an interface to prompt when/where to click
#Then these get set & saved as 'constants'
def on_click(x, y, button, pressed) :
    global xari, yari
    global count
    while count > 0:
        print('Clicked: ' + str(x) + ' and ' + str(y))
        count -= 1
        if count == 1 and yari != 7:
           break
        xari = x ; yari = y
    window.after(2000, window.destroy)    
    listener.stop()
'''
---Goes into pickup()---
with Listener(on_click=on_click) as listener:
    listener.join()
pyautogui.moveTo(xari, yari)
pyautogui.moveTo(xari, yari*1.364)
---In grab_deets---
pyautogui.moveTo(xari, yari*3.6)
---In paste_greeting---
pyautogui.moveTo(yari*6.061, yari*2.73)
'''


def main():
    patname = 'friend'
    patmail = 'Zero'
    patlibrary = 'Stax'
    ipaddress = 'No IP shown'
    gatewayURL = 'placehold'
    quest = 0
    prefgreeting = ''
    time = ' this evening'
    offer = 'I\'ll try to help you with that! This will take a few minutes.'
            
    def pickup() :
        pyautogui.moveTo(732, 165)    #for 75% on Folio
        pyautogui.click()    #hits the 'New' tab
        pyautogui.PAUSE = .8   #how long does it take to load/switch tabs?
        pyautogui.moveTo(732, 225)   #for 75%  :USE pyautogui.position()
        pyautogui.click()   #picks up caller

    def grab_deets() :
        pyautogui.moveTo(732, 600)
    #  pyautogui.click()
        pyautogui.PAUSE = 2.7     #how long does patron take to load?
        pyautogui.click()
        pyautogui.PAUSE = .1     #need to be on the new patron, and Info tab
        pyautogui.hotkey('ctrl', 'a')    #(possibly not automatable...)
        pyautogui.hotkey('ctrl', 'c')
        s = pyperclip.paste()
        return s

    def log_stuff(s):
        f = open("openings.txt", "a+")
        s = pyperclip.paste() 
        f.write("\r\n" + s + "\r\n" + "-------------------------------------------------------")
        f.close()

    # def greeting() :

    def split2list(x):
        alist = x.split('\n')
        del alist[0:10] 
        return alist

    def iznta_question() :
        if 'Qwidget:' in words :
            qwposi = words.index('Qwidget:')
          #  print (qwposi)
          #  print(len(words) - qwposi - 1)
            if (len(words) - qwposi) <= 4 :
                return True
            else :
                return False

    def emailask():
        if patmail != 'They gave us no address' :
            return ''
        else:
            return " And though you're not obliged to give an email address, which we certainly <b><i>never</i></b> use to track or to spam anyone, it does help us serve you better. Is there an address where we can reach you in case we're disconnected and another librarian needs to follow up?"

    def pastegreeting() :
        pyautogui.moveTo(900, 85)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'v')

    pickup()
    text = grab_deets()
    log_stuff(text)
    mylist = split2list(text)
    for lines in reversed(mylist):
        words = lines.split()
        if len(words) == 0 : continue
        if  words[0] == 'Close' : 
            pyautogui.moveTo(870, 210) #Closes the 'Already p/u' dialog 
            pyautogui.click()
            return    #stops script upon 'Already p/u' message
        if words[0] == 'Name:' :
            patname = words[1]  #ASHFORD. KICK IN TO A DIFFT FUNCTION!  
        if words[0] == 'Queue:' :
            if 'UK' in words :
                time = '' 
        if words[0] == 'Patron:' :
            if patname == 'friend' and words[1] != 'anonymous':
                patname = words[1]
            patmail = words[-1]
            if patmail == 'provided' :
                patmail = 'They gave us no address'
            patmail = patmail[1:-1]   #TRIMS PARENTHESES OFF BOTH ENDS, or does it????
        if words[0] == "Patron\'s" :
            patlibrary = (words[2: ])   #IF THIS CONTAINS 'ASHFORD' LOOK FOR NAME & EMAIL BELOW
            if 'Ashford' in patlibrary:
                prefgreeting = "Hi, welcome to Ashford University's 24/7 Library Chat service! " 
        if iznta_question() :
            offer = 'What can I help you with?'
            continue
    patname = patname.capitalize()
    if patname == 'Library' : patname = 'friend'
    if patmail == 'rovided' : patmail = 'They gave us no address'
    patlibraryX = '' 
    for kotoba in patlibrary:
        brack = '('
        if brack in kotoba :
            indx = patlibrary.index(kotoba)
            print(indx)
            patlibraryX = patlibrary[ : indx ]
            patlibraryX = ' '.join(patlibraryX)
            patlibraryX = str(patlibraryX)
            patlibraryX = titlecase(patlibraryX)
            break
        else:
            patlibraryX = patlibraryX + ' ' + kotoba
            patlibraryX = titlecase(patlibraryX)
    patlibraryX = patlibraryX.lstrip()
    addAsk = emailask()
    greeting = (prefgreeting + "Hello, " + patname + ", and welcome! It's great to be able to serve you" + time + ". I'm Bruce, part of a network of librarians assisting our " + patlibraryX + " colleagues while they're busy with other things. " + offer)
    pyperclip.copy(greeting)
    log_stuff(greeting)
    pastegreeting()
    print(greeting)
    if addAsk != '' :
        pyperclip.copy(addAsk)

window = Tk()
window.title("Map your screen")
window.geometry('350x80+300+225')
window.lift()
ws = window.winfo_screenwidth()
#hs = window.winfo_screenheight()
print(ws)
lbl = Label(window, text="With the QP chat interface screen up,\nclick the 'New' tab at upper left above the blue bar")
lbl.grid(column=0, row=0)
#window.after(7000, window.destroy) #TODO: DESTROY AFTER VALID CLICK, W/ CALLBACK (or Iterator, or Generator?)
with Listener(on_click=on_click) as listener:
    window.mainloop()
    #window.wait_variable(xari)
    print('2nd: ' + str(xari))
    listener.join()
print(str(xari) + ', ' + str(yari) + ' the third')
listener.stop()

#window.after(3000, on_click(xari, yari, 'button', 'pressed'))
print('Finish line!')
if __name__ == "__main__":
    main()
