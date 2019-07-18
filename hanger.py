import pyperclip, re, string, keyboard, time, pyautogui, webbrowser, titlecaseMod, pynput, threading, tkinter, configparser, os

#_WRITES_ CONFIG FILE AND DOES READ FROM IT

text = pyperclip.paste()
pyautogui.FAILSAFE = True
from titlecaseMod import titlecase
from pynput.mouse import Listener
from tkinter import *

configfile_name = "config.ini"
cfg = configparser.ConfigParser()

xari2 = 206 ; yari2 = 207 ; count = 3 ; xari0 = 100 ; yari0 = 100 ; xari3 = 50 ; yari3 = 50

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
        global xari2, yari2, xari0, yari0
        cfg.read('config.ini')
        xtab = cfg['tab']['x']
        ytab = cfg['tab']['y']
        pyautogui.moveTo(int(xtab), int(ytab))    
        pyautogui.click()    #hits the 'New' tab
        pyautogui.PAUSE = .8   #how long does it take to load/switch tabs?
        global xpu, ypu
        xpu = cfg['pickup']['x']
        ypu = cfg['pickup']['y']
        pyautogui.moveTo(int(xpu), int(ypu))   #for 75%  :USE pyautogui.position()  # 23, 241
        pyautogui.click()   #picks up caller

    def grab_deets() :
        global xpu, ypu
        pyautogui.moveTo(int(xpu), int(ypu)*1.5)       # 23, 421 yari2*2.17   #LOOK CAREFULLY AT THIS; CUT
        pyautogui.PAUSE = 2.7     #how long does patron take to load?      
        pyautogui.click()
        pyautogui.PAUSE = .1     #need to be on the new patron, and Info tab
        pyautogui.hotkey('ctrl', 'a')    #(possibly not automatable...)
        pyautogui.hotkey('ctrl', 'c')
        s = pyperclip.paste()
        return s

    def log_stuff(s):
        f = open("openings.txt", "a+", encoding="utf-8")
        s = pyperclip.paste() 
        f.write("\r\n" + s + "\r\n" + "-------------------------------------------------------")
        f.close()

    def split2list(x):
        alist = x.split('\n')
        del alist[0:10] 
        return alist

    def iznta_question() :
        if 'Qwidget:' in words :
            qwposi = words.index('Qwidget:')
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
        cfg.read('config.ini')
        xgreet = cfg['paste']['x'] ; ygreet = cfg['paste']['y']
        pyautogui.moveTo(int(xgreet), int(ygreet))      
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
            pyautogui.moveTo(870, 210) #Closes the 'Already p/u' dialog #USE MATH to adapt this one!!!
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
        mailAlert = Tk()
        mailAlert.title("No mail supplied!")
        mailAlert.geometry('350x120+300+225')
        mailbl = Label(mailAlert, text="Patron gave no email!\nYour clipboard has a\nmessage to ask for it")
        mailbl.grid(column=0, row=0)
        mailAlert.lift()
        mailAlert.deiconify()
        mailAlert.after(3500, mailAlert.destroy)
        mailAlert.mainloop()
if not os.path.isfile('config.ini'):
    print('Importing the configuration script')
    import wmod.hanger0   #TO TIME THE RUNNING OF A MODULE, SIMPLY (Yes, call its functions)
                   # wmod IS NAME OF FOLDER IN ROOT; Wmod.py IS THE FILE AND ALSO NEEDS AN __init__.py
else:
    print('Would you like to REconfigure?')        
if __name__ == "__main__":
    main()
keyboard.add_hotkey('shift+control', main)
keyboard.wait()     #keeps the script alive & ready for the keystrokes in line above
