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
xari = 206 ; yari = 207  
#Then these get set & saved as 'constants', but it's only happening below, not above!
def on_click(x, y, button, pressed) :
    global xari2, yari2, xari0, yari0, count
    while count != 1:
        print(count)
        print('Clicked: ' + str(x) + ' and ' + str(y))
        count = count + 1
        print(count)
        break
    xari2 = x ; yari2 = y
    #window.after(2000, window.destroy)    
   # listener.stop()

def main():
    global xari
    print(xari)
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
        global xari, yari, xari2, yari2, xari0, yari0
        cfg.read('config.ini')
        xtab = cfg['tab']['x']
        ytab = cfg['tab']['y']
        print('xtab is ' + str(xtab))
        pyautogui.moveTo(int(xtab), int(ytab))    
        pyautogui.click()    #hits the 'New' tab
        pyautogui.PAUSE = .8   #how long does it take to load/switch tabs?
        global xpu, ypu
        xpu = cfg['pickup']['x']
        ypu = cfg['pickup']['y']
        print('ypu is ' + str(ypu))
        pyautogui.moveTo(int(xpu), int(ypu))   #for 75%  :USE pyautogui.position()  # 23, 241
        pyautogui.click()   #picks up caller

    def grab_deets() :
        xpu, ypu
        pyautogui.moveTo(int(xpu), int(ypu)*1.7)       # 23, 421 yari2*2.17   #LOOK CAREFULLY AT THIS; CUT
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

    # def greeting() :

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
        xgreet = cfg['greet']['x'] ; ygreet = cfg['greet']['y']
        print('ygreet is ' + str(ygreet))
        pyautogui.moveTo(int(xgreet), int(ygreet))      
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'v')

def reconfig() :
    frame.after(200, frame.destroy)
    tx.after(200, tx.destroy)
    window = Tk()
    window.title("Step one!")
    window.geometry('350x80+300+225')
    window.lift()
    lbl = Label(window, text="Hit the 'New' tab above the blue bar")
    lbl.grid(column=0, row=0)
    with Listener(on_click=on_click) as listener:
        window.mainloop()
        print('1rd: ' + str(xari2) + ' ' + str(yari2))
        x0 = xari2  ;   y0 = yari2
        print('x0 is ' + int(x0))
        cfg['tab'] = {'x': x0, 'y': y0}
        print('cfg is ' + cfg['tab'])
        listener.join()
        window.after(2000, window.destroy)
        listener.stop()
    window = Tk()
    window.title("Step two!")
    window.geometry('350x80+300+225')
    window.lift()
    lbl = Label(window, text="Now, click just below the blue bar")
    lbl.grid(column=0, row=0)
    with Listener(on_click=on_click) as listener:
        window.mainloop()
        print('2nd: ' + str(xari2) + ' ' + str(yari2))
        x1 = xari2  ;   y1 = yari2
        cfg['pickup'] = {'x': x1, 'y': y1}
        window.after(2000, window.destroy)    
        listener.join()
        print(str(xari2) + ', ' + str(yari2) + ' the second')
        listener.stop()
    window = Tk()
    window.title("Step three!")
    window.geometry('350x80+300+225')
    window.lift()
    lbl = Label(window, text="Now, inside the chat box")
    lbl.grid(column=0, row=0)
    with Listener(on_click=on_click) as listener:
        window.mainloop()
        print('3rd: ' + str(xari2) + ' ' + str(yari2))
        x2 = xari2  ;   y2 = yari2
        cfg['greet'] = {'x': x2, 'y': y2}
        with open('config.ini', 'w') as configfile:
            cfg.write(configfile)
        listener.join()
        print(str(xari2) + ', ' + str(yari2) + ' the thirnd')
        listener.stop()
        window.after(2000, window.destroy)
        listener.stop()
    
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
            patmail = patmail[1:-1]   #TRIMS PARENTHESES OFF BOTH ENDS 
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
        mailAlert.after(5500, mailAlert.destroy)
        mailAlert.mainloop()
if not os.path.isfile('config.ini'):
    reconfig()    
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

if __name__ == "__main__":
    main()
keyboard.add_hotkey('ctrl+alt+.', main)
keyboard.wait()     #keeps the script alive & ready for the keystrokes in line above
