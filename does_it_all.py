import pyperclip, re, string, keyboard, time, pyautogui, webbrowser, titlecaseMod, pynput, threading, tkinter, configparser, os

text = pyperclip.paste()
pyautogui.FAILSAFE = True
from titlecaseMod import titlecase
#from pynput.mouse import Listener
from pynput import *
from tkinter import *
configfile_name = "config.ini"
cfg = configparser.ConfigParser()
val = 'Test'   
timenow = 'Huh'
show = '' ; shola1 = '' ; shola2 = ''; shola3 = ''; shola4 = '' ; liban = ''
global h3Value
keychoice = 'Hit the button & choose a key!'
keys_label = 'ditto'

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
    global timenow, show, shola1, shola2, shola3, shola4, liban, nameValue, h1Value, h2Value, h3Value, h4Value
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
    greeting = (prefgreeting + "Hello, " + patname + ", and welcome! It's great to be able to serve you " + timenow + ". " + val + " " + patlibraryX + " colleagues while they're busy with other things. " + offer)
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

def choose_keys():
    with pynput.keyboard.Listener(
        on_press=on_press) as glistener:
        glistener.join()

def on_press(key):
        global keychoice, keys_label
        print (type(keys_label))
        print('{0} pressed'.format(key))
        while keychoice != '':
            print('{0} pressed'.format(key))
          #  keys_label.destroy()
            print('okay so far')
            keychoiced = (str('{0} chosen'.format(key)))
            print(keychoiced)
            keys_label2 = Label(window, text=keychoiced)
            keys_label2.pack(side=LEFT)
            #keys_label.configure(keychoiced)
            print('the key choice is ' + keychoiced)
            #window.mainloop()
            
def map():
    global window, listener, val, timenow, show, shola1, shola2, shola3, shola4, liban, h3Value, h2Value, h1Value, h4Value, nameValue, keychoice
    window = Tk()
    pic = PhotoImage(file="tabsG.gif")
    window.title("Map your screen--Step 1 of 3")
    window.geometry('725x240+300+325')
    window.configure(background='blue')
    window.lift()
    write_first_section('tab')
    lblPic = Label(window, image=pic).pack(side="right")
    lbl = Label(window, justify=LEFT, text="On the actual QP\nchat interface screen,\nclick the 'New' tab at upper\nleft above the blue bar", font=("Helvetica", 14)).pack(side='right')
    with pynput.mouse.Listener(on_click=on_click) as listener:
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
    with pynput.mouse.Listener(on_click=on_click) as listener:
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
    with pynput.mouse.Listener(on_click=on_click) as listener:
        window.mainloop()
    window = Tk()
    def grab_input():
        global val, timenow, show, shola1, shola2, shola3, shola4, liban, h3Value, h2Value, h1Value, h4Value
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
        h1Value=hola1inp.get("1.0","end-1c")
        h2Value=hola2inp.get("1.0","end-1c")
        h3Value=hola3inp.get("1.0","end-1c")
        h33Value = h3Value + ' Anytown Public Library '
        h4Value=hola4inp.get("1.0","end-1c")
        timeValue = timeinp.get("1.0","end-1c")
        nameValue = libaninp.get("1.0","end-1c")
        val = h1Value
        timenow = timeValue
        frame = Frame(window)
        frame2 = Frame(window)
        frame.grid(row=8, columnspan=3, rowspan=1, sticky=W+E)
        frame2.grid(row=9, columnspan=3, rowspan=1, sticky=W+E)
        shola1 = Label(frame, text = val)
        shola1.configure(text=val)
        shola1.pack(side="left")
        #shola1.grid(row=0, column=0)
        show = Label(frame, text=timenow)
        show.configure(text=timenow)
        show.pack(side="left")
        #show.grid(row=0, column=1)
        shola2 = Label(frame, text = h2Value)
        shola2.configure(text=h2Value)
        shola2.pack(side="left")
        #shola2.grid(row=0, column=2)
        liban = Label(frame, text = nameValue)
        #liban.configure(text = nameValue)
        liban.pack(side="left")
        #liban.grid(row=0, column = 3)
        shola3 = Label(frame2, text = h33Value)
        #shola3.configure(text=h3Value)
        shola3.pack(side="left")
        #shola3.grid(row=1, column=0)
        shola4 = Label(frame2, text = h4Value)
        #shola4.configure(text=h4Value)
        shola4.pack(side="left")
        #shola4.grid(row=1, column=1)
        print('val in grab_input() is ' + val)
        print ('time is ' + timenow + ' inside the grab function.')
        cfig = configparser.ConfigParser()
        cfig.read('config0.ini')
        changreet = cfig['greet']
        changreet['timenow'] = timenow
        changreet['hola1'] = h1Value
        changreet['hola2'] = h2Value
        changreet['hola3'] = h3Value
        changreet['hola4'] = h4Value
        changreet['libanname'] = nameValue
        with open('config0.ini', 'w') as configfile:
            cfig.write(configfile)
     
    cfig = configparser.ConfigParser()
    cfig.read('config0.ini')
    h1 = cfig['greet']['hola1']
    h2 = cfig['greet']['hola2']
    h3 = cfig['greet']['hola3']
    h4 = cfig['greet']['hola4']
    libanname = cfig['greet']['libanname']
    thetime = cfig['greet']['timenow']
    window.title("Now, make up a greeting and, if you like, specify the time")
    window.geometry('660x346+210+25')
    window.configure(background='#c0ffee')
    hola1inp = Text(window, width=35, height = 2)
    hola1inp.insert('1.0', h1 )
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
    timeinp.grid(row=2, column=1)
    hola2inp.grid(row=3, column=1)
    libaninp.grid(row=4, column=1)
    hola3inp.grid(row=5, column=1)
    greetHeading = Label(window, text="Here, you craft a greeting", font=("Helvetica", 17), fg='red', bg='#c0ffee', justify=LEFT).grid(row=0, column=0, columnspan=3)
    libHolder=Label(window, text="Somewheresville Public or Academic Library", font=("Consolas", 9)).grid(row=6, column=1, pady=2)
    hola4inp.grid(row=7, column=1)
    namePrompt = Label(window, text="Your screen name", font=("Helvetica", 12), fg='orange', bg='#c0ffee', justify=LEFT).grid(row=4, column=2, sticky='W')
    timePrompt = Label(window, text="Time of day, if you like", font=("Helvetica", 12), fg='orange', bg='#c0ffee', justify=LEFT).grid(row=2, column=2, sticky='W')
    buttonPreview=Button(window, height=1, width=17, text="Preview your greeting", bg="yellow",
                    command=grab_input)
    buttonPreview.grid(row=1, column=0)
    buttonCommit = Button(window, height=1, width=17, text="Looks good!", bg="lime", fg="black", command=window.destroy)
    buttonCommit.grid(row=10, column=1)
   # print('And now, h33Value is ' + h33Value)
    window.mainloop()

    global keychoice, keys_label
    window = Tk()
    window.title("Set the wake-up keystrokes!")
    window.geometry('560x325+210+25')
    window.configure(background='#c0ffee')
    bindPrompt = Label(window, text = "Now decide which key combination\nshould trigger a pickup", font=("Helvetica", 14), fg='green').pack(side = TOP)
    #181.5  #Albrigt Rd (one) , CSA pickup bldg. (three)  Hilltop Rd. (four)
    choobutton = Button(window, text="start the thing", command=choose_keys).pack(side=LEFT)
    killbutton = Button(window, text="i'm done here", command=stroy).pack(side=LEFT)
    #keychoice = tkinter.StringVar()
    keychoice = 'Okay, pick some keys'
    keys_label = Label(window, text=keychoice)
    keys_label.pack(side=LEFT)
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
    window.geometry('600x182+300+225')
    window.configure(background='pink')
    window.lift()
    lbl = Label(window, text="Looks like you have configured the software. Nice!\nIf you're still using the same browser and haven't\nchanged its zoom level, no need to reconfigure!", font=("Helvetica", 16), bg='pink')
    lbl.pack(anchor='n')
    button_yes = Button(window, text="Re-do the\nconfiguration", bg="orange", font=("Helvetica", 11), command=map_it)
    button_yes.pack(side = BOTTOM, fill= X, pady = 2, padx = .5)
    button_no = Button(window, text="Skip it and \nrun the program", bg="green", fg="white", command=run_it)
    button_no.pack(side = BOTTOM, fill = X, pady = 2, padx = .5)
    # seems this might be a good place to offer _just_ config of key binding, or greeting -- ?
    window.mainloop()

if __name__ == "__main__":
    main()
pynput.keyboard.add_hotkey('shift+control', main)
pynput.keyboard.wait()     #keeps the script alive & ready for the keystrokes in line above
