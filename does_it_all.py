import pyperclip, re, string, keyboard, time, pyautogui, webbrowser, titlecaseMod, pynput, threading, tkinter, configparser, os

text = pyperclip.paste()
pyautogui.FAILSAFE = True
from titlecaseMod import titlecase
from pynput.mouse import Listener
from tkinter import *
configfile_name = "config.ini"
cfg = configparser.ConfigParser()
val = 'Test'   
timenow = 'Huh'

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

def write_first_section(section_name):
    global configfile_name
    c = open(configfile_name, "w", encoding="utf-8")
    c.write('[' + section_name + '] \r')
    c.close()

xari2 = 206 ; yari2 = 207 ; count = 3 ; xari0 = 100 ; yari0 = 100 ; xari3 = 50 ; yari3 = 50
def on_click(x, y, button, pressed) :
    global xari2, yari2, xari0, yari0, xari3, yari3
    global window, listener
    write_config(str(x), str(y))
    window.after(2000, window.destroy)    
    listener.stop()  # Necessary, or will continue logging clicks for 'tab'
    
def main():
    patname = 'friend'
    patmail = 'Zero'
    patlibrary = 'Stax'
    ipaddress = 'No IP shown'
    gatewayURL = 'placehold'
    quest = 0
    prefgreeting = ''
    global timenow
    # time = ' this evening'

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
               timenow = '' 
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
    #cfg.read('config.ini')
   # patname = cfg['name']['x']
  #  greeting = (prefgreeting + "Hello, " + patname + ", and welcome! It's great to be able to serve you" + time + ". I'm Bruce, part of a network of librarians assisting our " + patlibraryX + " colleagues while they're busy with other things. " + offer)
    greeting = (prefgreeting + "Hello, " + patname + ", and welcome! It's great to be able to serve you" + timenow + ". " + val + " " + patlibraryX + " colleagues while they're busy with other things. " + offer)
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
        mailAlert.after(8500, mailAlert.destroy)
        mailAlert.mainloop()

def map():
    global window, listener, val, timenow
    window = Tk()
    pic = PhotoImage(file="tabsG.gif")
    window.title("Map your screen--Step 1 of 3")
    window.geometry('725x240+300+325')
    window.configure(background='blue')
    window.lift()
    write_first_section('tab')
    lblPic = Label(window, image=pic).pack(side="right")
    lbl = Label(window, justify=LEFT, text="On the actual QP\nchat interface screen,\nclick the 'New' tab at upper\nleft above the blue bar", font=("Helvetica", 14)).pack(side='right')
    with Listener(on_click=on_click) as listener:
        window.mainloop()
        listener.join()
    listener.stop()
    write_section('pickup')
    count = 3
    window = Tk()
    pic2 = PhotoImage(file="tabsP.gif")
    window.title("Step two of three!")
    window.geometry('650x260+210+225')
    window.configure(background='pink')
    window.lift()
    lblPic2 = Label(window, image=pic2).pack(side="left")
    lbl = Label(window, justify=RIGHT, text="Now, click just\nbelow the blue bar", font=("Helvetica", 14)).pack(side='left')
    with Listener(on_click=on_click) as listener:
        window.mainloop()
        listener.join()
    listener.stop()
    write_section('paste')
    count = 3
    window = Tk()
    pic3 = PhotoImage(file="tabsH.gif")
    window.title("Final step--3 of 3!")
    window.geometry('800x235+210+25')
    window.configure(background='#00ff00')
    window.lift()
    lblPic3 = Label(window, image=pic3).pack(side="right")
    lbl = Label(window, justify=LEFT, text="Lastly, click inside the\nthe Chat Input Field", font=("Helvetica", 14)).pack(side='right')
    #lbl.grid(column=0, row=0)
    #lbl.pack(side = TOP)
    with Listener(on_click=on_click) as listener:
        window.mainloop()
    window = Tk()
    def grab_input():
        global val, timenow
        inputValue=inp.get("1.0","end-1c")
        timeValue = timeinp.get("1.0","end-1c")
        val = inputValue
        timenow = timeValue
        print('val is ' + val)
        print ('time is ' + timenow + ' inside the grab function.')
    window.title("Now, make up a greeting")
    window.geometry('520x315+210+25')
    window.configure(background='#0fff00')
    timeinp = Text(window, width=20, height = 1)
    timeinp.insert('1.0', 'When izzitnow?')
    timeinp.pack(side=LEFT)
    inp = Text(window, width=60, height=12)
    inp.insert('1.0', 'Go ahead and type a greeting--use your name, and some\nfriendly badinage.')
    inp.pack(side=BOTTOM)
    buttonCommit=Button(window, height=1, width=10, text="Commit", 
                    command=grab_input)
    buttonCommit.pack(side=LEFT)
    print('And now, val is ' + val)
    window.mainloop()
    
def stroy():
    window.destroy()

def map_it(evt=None):    # What is the evt=None doing here?
    stroy()
    map()

def run_it(evt=None):
    stroy()
    main()

if not os.path.isfile('config.ini'):
    print("In this case, we must run configuration")
    window = Tk()
    window.title("Giving you a chance to configure the software just for you!")
    window.geometry('650x170+300+225')
    window.configure(background='yellow')
    window.lift()
	# need a button with command=map_it()   
    lbl = Label(window, text="Let's customize the program to fit you and your\ncomputer. We need to map your screen, and you will\nalso get to make a greeting script using your name.", font=("Helvetica", 16), bg='yellow')
    lbl.pack(anchor='n')
    lbl2 = Label(window, text="Click the green bar to begin!", font=("Helvetica", 16), bg='yellow')
    lbl.pack(anchor='s')
    button_yes = Button(window, text="Click the Green Bar to Configurate Me!", bg="lime", font=("Helvetica", 11), command=map_it)
    button_yes.pack(side = BOTTOM, fill= X, pady = 2, padx = .5)
    window.mainloop()
else:
    window = Tk()
    window.title("Choose what to do at launch")
    window.geometry('600x170+300+225')
    window.configure(background='pink')
    window.lift()
    lbl = Label(window, text="Looks like you have configured the software. Nice!\nIf you're still using the same browser and haven't\nchanged its zoom level, no need to reconfigure!", font=("Helvetica", 16), bg='pink')
    lbl.pack(anchor='n')
    button_yes = Button(window, text="Re-do the\nconfiguration", bg="orange", font=("Helvetica", 11), command=map_it)
    button_yes.pack(side = BOTTOM, fill= X, pady = 2, padx = .5)
    button_no = Button(window, text="Skip it and \nrun the program", bg="green", fg="white", command=run_it)
    button_no.pack(side = BOTTOM, fill = X, pady = 2, padx = .5)
    window.mainloop()

if __name__ == "__main__":
    main()
keyboard.add_hotkey('shift+control', main)
keyboard.wait()     #keeps the script alive & ready for the keystrokes in line above
