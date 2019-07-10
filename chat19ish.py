import pyperclip, re, string, keyboard, time, pyautogui, webbrowser, titlecaseMod, pynput, threading, tkinter
#NOW main() IS KICKED OFF BY A KEYBOARD COMMAND, PROGRAM 'SLEEPS' B/N INVOCATIONS, VARS DEFINED IN HEAD SECTION
#NOW THAT WE CAN CAPTURE MOUSE CLICKS & WRITE THEM TO pyautogui/pyperclip FUNCTIONS, HOW TO STORE THOSE THROUGH
#MULTIPLE RUNS OF THE PROGRAM?
#MOUSE MAPPING AS AN *OPTIONAL* STEP UPON LAUNCH--NEED TO
#SAVE 'CONFIG' FILE/FUNCTION' TO DISK
#ANOTHER THING: SHOULD BE SIMPLE TO SCRAPE LOCATION FROM, E.G. https://www.ip2location.com/demo/172.91.22.94

text = pyperclip.paste()
pyautogui.FAILSAFE = True
from titlecaseMod import titlecase
from pynput.mouse import Listener
from tkinter import *
configfile_name = "config.ini"

def write_config(x_coord, y_coord):
     #   configfile_name = "config.ini"
        #if not os.path.isfile(configfile_name):
    # Create the configuration file as it doesn't exist yet
    global configfile_name
    c = open(configfile_name, "a", encoding="utf-8")
    #c.write('[' + section_name + '] \r')
    c.write('x=' + x_coord + '\r')
    c.write('y=' + y_coord)
    c.write('\r\n')
    c.close()
def write_section(section_name):
    global configfile_name
    c = open(configfile_name, "a", encoding="utf-8")
    c.write('[' + section_name + '] \r')
    c.close()

'''
import cfg_load
fig = cfg_load.load('config.ini')
print(type(config))
for section in fig:
    print(section)
print(fig['pickup'])
'''

count = 5
xari2 = 206 ; yari2 = 207 ; count = 5 ; xari0 = 100 ; yari0 = 100 ; xari3 = 50 ; yari3 = 50
#Then these get set & saved as 'constants', but it's only happening below, not above!
def on_click(x, y, button, pressed) :
    global xari2, yari2, xari0, yari0, xari3, yari3
    global count
    while count > 0:
        if count == 4 and yari2 != 207:
            xari0 = x
            yari0 = y
            continue
        print('Clicked: ' + str(x) + ' and ' + str(y) + ' and xari2 is ' + str(xari2))
        print(count)
        count -= 1
    write_config(str(x), str(y))
    window.after(2000, window.destroy)    
    listener.stop()
'''
        if count == 3 and yari2 != 207:
           xari2 = x ; yari2 = y
           break
        if count == 1 and yari2 != 207:
            xari3 = x ; yari3 = y
            break
        '''
 #       count -= 1
 #   window.after(2000, window.destroy)    
  #  listener.stop()
'''
TODO: TEST THESE COORDS, LOOK AT USE OF SCREEN SIZE
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
        global xari2, yari2, xari0, yari0
        pyautogui.moveTo(xari0, yari0)    #for Practice gui: 23, 194
        pyautogui.click()    #hits the 'New' tab
        pyautogui.PAUSE = .8   #how long does it take to load/switch tabs?
        pyautogui.moveTo(xari2, yari2)   #for 75%  :USE pyautogui.position()  # 23, 241
        pyautogui.click()   #picks up caller

    def grab_deets() :
        global xari2, yari2
        pyautogui.moveTo(xari2, yari2+100)       # 23, 421 yari2*2.17
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
        pyautogui.moveTo(xari3, yari3)     # (xari*6.061, yari*2.73)       # 700, 360
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
        mailAlert.after(8500, mailAlert.destroy)
        mailAlert.mainloop()
        
window = Tk()
window.title("Map your screen")
window.geometry('350x80+300+225')
window.lift()
ws = window.winfo_screenwidth()
write_section('tab')
#hs = window.winfo_screenheight()
print(ws)
lbl = Label(window, text="With the QP chat interface screen up,\nclick the 'New' tab at upper left above the blue bar")
lbl.grid(column=0, row=0)
with Listener(on_click=on_click) as listener:
    window.mainloop()
    listener.join()
listener.stop()
write_section('pickup')
print('Now for Window 2')
window = Tk()
window.title("Step two!")
window.geometry('350x80+300+225')
window.lift()
lbl = Label(window, text="Now, click just below the blue bar")
lbl.grid(column=0, row=0)
with Listener(on_click=on_click) as listener:
    window.mainloop()
    print('3rd: ' + str(xari2) + ' ' + str(yari2))
    listener.join()
print(str(xari2) + ', ' + str(yari2) + ' the third')
listener.stop()
write_section('paste')
window = Tk()
window.title("Step three!")
window.geometry('350x80+300+225')
window.lift()
lbl = Label(window, text="Lastly, click in the text box")
lbl.grid(column=0, row=0)
with Listener(on_click=on_click) as listener:
    window.mainloop()

print('Finish line!')
if __name__ == "__main__":
    main()
keyboard.add_hotkey('shift+control', main)
keyboard.wait()     #keeps the script alive & ready for the keystrokes in line above
