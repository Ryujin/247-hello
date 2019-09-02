import pyperclip, re, string, keyboard, time, pyautogui, webbrowser, titlecaseMod, pynput, threading, tkinter, configparser, os, sys

text = pyperclip.paste()
pyautogui.FAILSAFE = True
from titlecaseMod import titlecase
from pynput.mouse import Listener
from tkinter import *
configfile_name = "config.ini"
cfg = configparser.ConfigParser()
timenow = 'Huh'
show = '' ; shola1 = '' ; shola2 = ''; shola3 = ''; shola4 = '' ; liban = '' ; sguest = ''
global h3Value, h33Value

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
    global timenow, show, shola1, shola2, shola3, shola4, liban, nameValue, h1Value, h2Value, h3Value, h4Value, h33Value, guest
    cfg.read('config0.ini')
    Nameval = cfg['greet']['libanname']
    timenow = cfg['greet']['timenow']
    h1Value = cfg['greet']['hola1']
    h2Value = cfg['greet']['hola2']
    h33Value = cfg['greet']['hola3']
    h4Value = cfg['greet']['hola4']
    patname = cfg['greet']['guest']   #this will cause problems, below, where 'friend' was assumed, when name IS known
    patnameanon = patname
    offer = 'I\'ll try to help you with that! This will take a few minutes.'  #THIS IS OBSOLETE
            
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
        pyautogui.moveTo(int(xpu), int(ypu)*2.2)       # 23, 421 yari2*2.17   #LOOK CAREFULLY AT THIS; CUT
        pyautogui.PAUSE = 2.7     
        pyautogui.click()
        pyautogui.PAUSE = .1     #need to be on the new patron, and Info tab
        pyautogui.hotkey('ctrl', 'a')     
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
            if patname == patnameanon and words[1] != 'anonymous':
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
    if patname != patnameanon : patname = patname.capitalize()
    if patname == 'Library' : patname = patnameanon
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
    greeting = (h1Value  + " " + patname + h2Value + prefgreeting  + " " + timenow + " " + Nameval + " " + h33Value  + " " + patlibraryX + " " + h4Value)
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
    global window, listener, timenow, show, shola1, shola2, shola3, shola4, liban, h3Value, h2Value, h1Value, h4Value, nameValue, guest
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
    lbl = Label(window, justify=LEFT, text="Now, click just\nbelow the blue bar", font=("Helvetica", 14)).pack(side='left')
    with Listener(on_click=on_click) as listener:
        window.mainloop()
        listener.join()
    listener.stop()
    write_section('paste')
    count = 3
    window = Tk()
    pic3 = PhotoImage(file="tabsH.gif")
    window.title("Final step--3 of 3!")
    window.geometry('800x235+260+25')
    window.configure(background='#00ff00')
    window.lift()
    lblPic3 = Label(window, image=pic3).pack(side="right")
    lbl = Label(window, justify=LEFT, text="Lastly, click inside the\nthe Chat Input Field", font=("Helvetica", 14)).pack(side='right')
    with Listener(on_click=on_click) as listener:
        window.mainloop()
    window = Tk()
    def grab_input():
        global Nameval, timenow, show, shola1, shola2, shola3, shola4, liban, h3Value, h2Value, h1Value, h4Value0, h33Value, g1Value, sguest
        if show != '':
            show.destroy()
        if shola1 != '':    
            shola1.destroy()
        if shola2 != '':    
            shola2.destroy()
        if liban !='':
            liban.destroy()
        if shola3 != '':    
            shola3.destroy()
        if shola4 != '':    
            shola4.destroy()
        if sguest != '':    
            sguest.destroy()
        h1Value=hola1inp.get("1.0","end-1c")
        h2Value=hola2inp.get("1.0","end-1c")
        h3Value=hola3inp.get("1.0","end-1c")
        g1Value = guestinp.get("1.0", "end-1c")
        h33Value = h3Value + ' Anytown Public Library'
        h4Value=hola4inp.get("1.0","end-1c")
        timeValue = timeinp.get("1.0","end-1c")
        nameValue = libaninp.get("1.0","end-1c")
        nameValue = nameValue.strip()
        h4Value = h4Value.lstrip()
        h2Value = h2Value.lstrip()

        timenow = timeValue
        frame = Frame(window)
        frame2 = Frame(window)
        frame.grid(row=11, columnspan=3, rowspan=1, sticky=W+E)
        frame2.grid(row=12, columnspan=3, rowspan=1, sticky=W+E)
        shola1 = Label(frame, text = h1Value)
        shola1.pack(side="left")
        sguest = Label(frame, text=g1Value)
        sguest.pack(side="left")
        shola2 = Label(frame, text = h2Value)
        shola2.configure(text=h2Value)
        shola2.pack(side="left")
        show = Label(frame, text=timenow)
        show.configure(text=timenow)
        show.pack(side="left")
        liban = Label(frame, text = nameValue)
        liban.pack(side="left")
        shola3 = Label(frame2, text = h33Value)
        shola3.pack(side="left")
        shola4 = Label(frame2, text = h4Value)
        shola4.pack(side="left")
        cfig = configparser.ConfigParser()
        cfig.read('config0.ini')
        changreet = cfig['greet']
        changreet['timenow'] = timenow
        changreet['hola1'] = h1Value
        changreet['hola2'] = h2Value
        changreet['hola3'] = h3Value
        changreet['hola4'] = h4Value
        changreet['libanname'] = nameValue
        changreet['guest'] = g1Value
        with open('config0.ini', 'w') as configfile:
            cfig.write(configfile)
     
    cfig = configparser.ConfigParser()
    cfig.read('config0.ini')
    h1 = cfig['greet']['hola1']
    h2 = cfig['greet']['hola2']
    h3 = cfig['greet']['hola3']
    h4 = cfig['greet']['hola4']
    g1 = cfig['greet']['guest']
    libanname = cfig['greet']['libanname']
    thetime = cfig['greet']['timenow']
    window.title("Now, make up a greeting and, if you like, specify the time")
    window.geometry('730x370+220+25')
    window.configure(background='#c0ffee')
    hola1inp = Text(window, width=35, height = 2)
    hola1inp.insert('1.0', h1 )
    guestinp = Text(window, width=22, height=2)
    guestinp.insert('1.0', g1)
    hola2inp = Text(window, width=35, height = 2)
    hola2inp.insert('1.0', h2 )
    hola3inp = Text(window, width=35, height = 2)
    hola3inp.insert('1.0', h3 )
    hola4inp = Text(window, width=35, height = 2)
    hola4inp.insert('1.0', h4 )
    libaninp = Text(window, width=35, height = 1)
    libaninp.insert('1.0', libanname )
    timeinp = Text(window, width=35, height = 2)
    timeinp.insert('1.0', thetime )
    hola1inp.grid(row=1, column=1)
    guestinp.grid(row=2, column=1)
    hola2inp.grid(row=3, column=1)
    timeinp.grid(row=4, column=1)
    libaninp.grid(row=5, column=1)
    hola3inp.grid(row=6, column=1)
    greetHeading = Label(window, text="Here, you craft a greeting", font=("Helvetica", 17), fg='red', justify=CENTER).grid(row=0, column=0, columnspan=3)
    libHolder=Label(window, text="Somewheresville Public or Academic Library", font=("Consolas", 9)).grid(row=7, column=1, pady=2)
    hola4inp.grid(row=8, column=1)
    namePrompt = Label(window, text="Your screen name", font=("Helvetica", 15), fg='orange', bg='#c0ffee', justify=LEFT).grid(row=5, column=2, sticky='W')
    guestPrompt = Label(window, text="The caller's name, if given, goes\nhere. What would you like to call an anon?", font=("Helvetica", 9), fg='orange', bg='#c0ffee', justify=LEFT).grid(row=2, column=2, sticky='W')
    timePrompt = Label(window, text="Time of day, if you like", font=("Helvetica", 15), fg='orange', bg='#c0ffee', justify=LEFT).grid(row=4, column=2, sticky='W')
    buttonPreview=Button(window, height=1, width=17, text="Preview your greeting", bg="yellow",
                    command=grab_input)
    buttonPreview.grid(row=5, column=0)
    buttonCommit = Button(window, height=1, width=17, text="Looks good!", bg="lime", fg="black", command=stroy)
    buttonCommit.grid(row=10, column=1)
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
    window.geometry('650x175+300+225')
    window.configure(background='yellow')
    window.lift()   
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
    window.geometry('600x185+300+225')
    window.configure(background='pink')
    window.lift()
    lbl = Label(window, text="Looks like you have configured the software. Nice!\nIf you're still using the same browser and haven't\nchanged its zoom level, no need to reconfigure!", font=("Helvetica", 16), bg='pink')
    lbl.pack(anchor='n')
    button_yes = Button(window, text="Re-do the\nconfiguration", bg="orange", font=("Helvetica", 11), command=map_it)
   # button_yes = Button(window, text="Re-do the\nconfiguration", bg="orange", font=("Helvetica", 11), command=keyWin)
    button_yes.pack(side = BOTTOM, fill= X, pady = 2, padx = .5)
    button_no = Button(window, text="Skip it and \nrun the program", bg="green", fg="white", command=run_it)
    button_no.pack(side = BOTTOM, fill = X, pady = 2, padx = .5)
    window.mainloop()

def setstrip(s):
    s = str(s)
    s = s[2:-2]
    s = s.replace("', '", "+")
    return s

def keystates():
    preview = None
    if preview:
        preview.destroy()
    keysts = {} 
    keysts['Ctrl'] = var1.get() ; keysts['Alt']=var2.get() ;  keysts['Up'] = var3.get() ; keysts['Shift']=var4.get() ;  keysts['Enter'] = var5.get() ; keysts['Home']=var6.get() ; keysts['Caps Lock']=var7.get()
    print(keysts)
    keyset = set()
    for key in keysts:
        if keysts[key] == 1:
            print(key)
            keyset.add(key)
    print(keyset)
    global keysetstring
    keysetstring = setstrip(keyset)
    keysetstring = keysetstring.strip()
    print(keysetstring)
    ltr_keys = charBind.get()
    charkeys = set()
    for crctr in ltr_keys:
        charkeys.add(crctr)
    if ltr_keys != '':
        charkeys = setstrip(charkeys)
        charkeys = charkeys.upper()
        keysetstring = keysetstring + '+' + charkeys
    print(keysetstring)
    preview = Label(window, text=keysetstring, fg="red", font=('Helvetica', 12, 'bold')).grid(row=8, column=0)
    Button(window, text='Finalize choices', bg='lime', command=window.destroy).grid(row=10, column=1)
    
window = Tk()
window.title("This last bit sets key binding")
window.geometry('950x315+210+25')
window.configure(background='#face0f')
chkLabel = Label(window, text="Choose two or three keys you'll press at the same time to awaken the program.\nWhen you hear a call come in, hitting these keys together will grab the call and generate\na greeting. Avoid key combos that already trigger commonly used shortcuts.\nFor example, Ctrl + P, or Ctrl + Alt + Del would be bad choices!", font=("Helvetica", 14))
# https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
chkLabel.grid(row=0, columnspan=3)
var1=IntVar(); var2=IntVar(); var3=IntVar(); var4=IntVar(); var5=IntVar(); var6=IntVar(); var7=IntVar()
Checkbutton(window, text='CTRL key', variable=var1).grid(row=2, column=0)
Checkbutton(window, text='ALT key', variable=var2).grid(row=2, column=1)
Checkbutton(window, text='UP ARROW key', variable=var3).grid(row=2, column=2)
Checkbutton(window, text='SHIFT key', variable=var4).grid(row=3, column=0)
Checkbutton(window, text='ENTER key', variable=var5).grid(row=3, column=1)
Checkbutton(window, text='HOME key', variable=var6).grid(row=3, column=2)
Checkbutton(window, text='CAPS LOCK key', variable=var7).grid(row=4, column=0)
charBind = Entry(window)
charLabel = Label(window, text="Choose letter, number, or symbol keys if you like")
genlTip = Label(window, text="Tip: Use a pair of neighboring keys, and don't include combos that already trigger an\naction when pressed together!")
genlTip.grid(row=7, column=0, columnspan=3)
charLabel.grid(row=5, column=0, columnspan=2, sticky=E)
charBind.grid(row=5, column=2, sticky=W)
Button(window, text='Show choices', bg='orange', command=keystates).grid(row=10, column=0)
#Button(window, text='Finalize choices', bg='lime', command=window.destroy).grid(row=10, column=1)
# ADD A try/except to prevent empty~no choice situations
window.lift()
window.mainloop()

window = Tk()
window.title("Here's what happens next")
window.geometry('650x315+210+25')
window.configure(background='#deface')
splainlabel = Label(window, text="Here's what will happen next:", font=("Helvetica", 17), bg='#deface', fg='blue')
splain2 = Label(window, text="When you close this window, the program will\ncycle through the clicks you mapped, plus\none slightly lower down after the 2nd, with brief time\nintervals between the clicks.", font=("Helvetica", 14), bg='#deface', fg='blue')
wakelabel = Label(window, text=keysetstring, font=("Helvetica", 14), bg='#deface', fg='purple')
wakesplain = Label(window, text="Hit these keys, together, to launch\nthe pickup cycle: When you\nhear a new call, have your QP screen up.", font=("Helvetica", 14), bg='#deface', fg='blue')
splainlabel.grid(row=0, column=0, sticky=EW)
splain2.grid(row=1, column=0, sticky=EW)
wakelabel.grid(row=3, column=0, sticky=EW)
wakesplain.grid(row=4, column=0, sticky=EW)
close_it = Button(window, text="Close\nwindow", command=window.destroy)
close_it.configure(height=4, width=8, bg='#feeb1e', relief=RAISED)  #emboss it too!
close_it.grid(row=3, column=1)
window.lift()
window.mainloop()
# user needs to be able to close, restart program somehow (not from CLI)
#import the sys module and use sys.exit()  -- alternatively, Python has a quit() function built in
#possibly they both work?
keysetstring = keysetstring.lower()

def killit():
    print("Shutting down!")
    window = Tk()
    window.title("Exiting the program")
    window.geometry('500x120+240+30')
    window.configure(background = '#f00dee')
    lastlabel = Label(window, text="Exiting...", font=("Helvetica", 28), bg='#f00dee', fg='red').pack()
    window.lift()
    window.after(2300, window.destroy)
    window.mainloop()
    time.sleep(3.5)
    sys.exit()

if __name__ == "__main__":
    main()
keyboard.add_hotkey(keysetstring, main)
keyboard.add_hotkey('alt+shift+x', killit)
keyboard.wait()     #keeps the script alive & ready for the keystrokes in line above
