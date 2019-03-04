# -*- coding: utf-8 -*-

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from sys import executable, argv
from subprocess import Popen
from random import randint
import time
import webbrowser
import platform

#################################
# Constants                     #
NUM_WINS_OPEN = 5               # how many windows to open per close
SIZE = 250                      # size of the window, in pixels
CLOSE_COMBO = 'hailhydra'       # type this to close the window
IMPATIENCE = 10                  # wait this many seconds before auto-duplication. -1 = don't
RICKROLL = False                 # rickroll the user on close?
TITLE = 'Kernel panic'          # window title
TEXT = "Segmentation fault: \ncore S̶͍̬͇̫͍̬̻̯̣̘̝͚̎̀̿e\n̷̮̟̟̳̭̍̄̾͝g̷͉̀̓͒̄̏͌̈́͜m̶̢̨̤̝̠̠̣̬̟̺͉͈̬̎͊͗͋̏ę̷̠̮̫̯͓̖̪͔̞̻̋̄̈́̕͝ͅn̷̳͖͓̈́͛̉͝t̷̛̻͒̈́̈͒͋͗̇̈́̓͠á̷̧̧̳̝̬̯͚͉̜̆̊̔͊͋ͅͅͅt̵̜̺̟̒̒̈́͛i̶̡̘̲̥͕̘̇o̸͙̺̖̗̞͍̾̇ṅ̵͍͙̀̄̊̇̉̂̋̒͑̓̒̿͘ ̶̢̢̱̲̣͆f̶̟̝͕͈̫̅̅̐̆͝a̶̛͙̺̹̓̔̽̅̓͌͛̀̀̾͗̾͘̚ư̵̛̘̩̻̝̹͍̒̿̍̽̈́̕l̶̪̟͙̱͛̓͋͌̇̌̆̚t̵͍̥̱̹̰̼̮͇͈̬̫̫͋̋͌̄͑̌̽́̄̚͜͠͝͝:̶̆̑́̽̈́ͅ ̸̢̢̡̡̙̯̱̰̞̰̄ć̶͎̈́͌̓̿͝ơ̸̡͓̱͕̭̹͈̫̰̝̠̹̎̊̅̆̆̓͘ř̸̛̤̙͒͆͗͂͑́̓̀̓̌̕͝͝ē̷̫̗̟̪̤͎̟̐̉̀͒́̒͝͠ ̴̧̡̩͚̥̰͓̅̽̆̔́͋̋͌̈́́͊̓̋̕d̶̟̞̬̓̈͌̓ǜ̷͇̻̙͎̮̰͙̣̖͖̹̹͜m̵̧͕̭̬͙̮̦̜̳͖̙̫̱͔͌͌̔̍̀̑̈̅̾̈̀́̈̔ṕ̵͎̯͙̳̠͍̪̼̫̗̭̃̽̓͒͑̄̏́̓̌͘̚͜ē̷̡͉͍̜̭̘̦̜̈͐͌̈́̐̾̉̓̾͝ḑ̷̫̱̝͎̣͔̖͎̘͈̾̇̇̉̑͗̇͘͜͝"" \nA̵͇̰̘̫͊̊́̐̾̈́A̶̳͔̩̼̳̽A̵̯̻̹͛͆̑͐̕͜͜À̴̹͚͕̤̜͉͕̰̊̅͒̿͑̿͑Ḁ̷͇̜͇̝̖̼̯̞̹̪̬̦͠Á̸̢̖̲̭͉̬̳̺̫͈̘͈̘̥̣̏\nA̶̡͚͇͍͇̩͇͇̱̱̻̟̹̮͈̎̈́̉͌̒A̸̢̦͓̤̹̠̺̘͔̘̦̘̔̋̅͐̂́̈́̍͗̊̇̔̚͠Ả̵̡̧̢̞͓͙͍̹̟̙͆͠ͅÂ̴̹̭̦̑͗́̂̄͑̀͊͑͌͐̀͒͝A̷͇̞̋͒̑͌͒̈́͗̓̎̃̚͝A̶̡̡̺̻̰̖͈̩̍͆̈́͆̊̾͝͝A̵̢̨̩̫̦͔̳̼̳͓͖͈̔̀̿͐  \nǪ̸̢̧͖͈̗̩͈̩̮̜̝̺̔͒̀̌̈́̀̀̐̀̀͝I̷͖̳̖̝͋̈͐ȯ̴̡̻̺̜͙͈̯̺̙͆͒͑̿̍́̓̿̂̊͛͑̓ȉ̸̹̤͍͛͑̍̓͋̈́̒̏̚ͅh̵͎͙͕̱̼̹̉́;̵̡̢͇͓̻͕̺̳͆͐̈̓͒̑̏̚͝ͅL̴̢͈̗͖̪͇̪̬̱̘͍͉͎̊̏̍̍̃̊̽̓̔̈̃̄͘K̵̮̦̯͎̺͖̩̬̘̪̟͓͌̿͒̄̏̊́̽̋̐̉̏̈͜͠ͅH̸̡̞͎͖͚͑J̴̧̺͖̱̳̪̺̟̞̻͎̋̓̽̆́͊̄́̀̎͘͠ͅK̶̢͓̩̮͈̬̙̙̟̎͜J̶̍̐̿͑\n̢͔̼̟͔̪̲̠̯̯͉͎͔̽Ḧ̵̞͓́ͅ;̸̢͕̺͍̼͇̘͕̺̲̺̲̦̾͐̋̓̌̽̋͠͠ͅK̷̰͔̰͈̥̈́̋͐͒̑̏̽H̷̹͍͓̺̗̻̪̟̎̀̃͌͜k̶̢̩̞̥͔͖̏j̴̡̙̦̜̯̗̞͕̾̅̆͒̉̾̀́͋̀̕͝ý̵̨̖̆͆͠y̶͙̒͗̓͒͑͐̆͛̌͋̊̄̚̕͠8̴̹̘̣͕̍̅̿̎̏̐͊̀̎͗̚̕9̸̩͔̯̥͈̊͌͘͝7̷̙̱̬̬͈̫̝̘̻̜̗̲͆̂̈̃̀̇̏̉\n7̵̢͕̓̏̌̽̋̏͌̾͗͑̄̐̕̚ͅ6̸̪͛̿̓̈̏̄́̈́̊̆̅̌̈́̑͝9̸̿̊̅̓̔̉͌͌̋̒̀͜2̵̙͉̗̭͓͙̘͚́͌̿̑̅͋͋͋̎̉͝7̷̢̀͂̾̌̽̓̑͛͠7̸̢̺̯̜͔̠̠̙̺̓͛͝͝x̵̨̪̘̬̻͓̰̬̬̭͕̥͚͌́̔̆l̴̡̥̥̺̓̄̒k̸̯͔̯͔̫̲͖̲̖͎̖͇͌̀̔̈́͒̊̚ͅj̶̢̛̫̖͓̘͚̳̣̜̯̠̘̊͐̑̔̒̿̈́̈́̏̑̽̓͠ͅj̴͖̥͙̦͉̗̐͛̔͘f̸̮͍̙͉̰́̑̿̈́̃͆̇͐̄̓̈́̽̕͜ͅl̶̺̜͉̺͕̺͈̫̥͈͚̥̣̈̐ķ̶̢͖̺͎̹͍̋̿̾̂̈̕͝3̸̛͖̲̰͈̗̯̩̱̘̈́̅̚̚  "       # text to appear in the window
# End constants                 #
#################################

RICKROLL_URL = "http://www.youtube.com/watch?v=oHg5SJYRHA0"

FIRST_RUN = not bool(len(argv) - 1)

def make_new(old):
    old.root.destroy()
    for _ in range(NUM_WINS_OPEN):
        Popen([executable, 'Hydra.py', '1'])
    if RICKROLL:
        webbrowser.open(RICKROLL_URL, new=1)

class MainWindow (object):

    def __init__(self):
        self.keys_pressed = []
        self.mouse_state = False
        self.birthday = time.time()
        
        self.root = tk.Tk()
        self.root.title(TITLE)
        if not FIRST_RUN and (IMPATIENCE > 0):
            self.root.after(1000 * IMPATIENCE, make_new, self)

        self.root.protocol('WM_DELETE_WINDOW', lambda: make_new(self))
        
        self.root.bind('<Unmap>', lambda e: self.unminimize())
        #self.root.bind('<Map>', lambda e: self.unminimize())
        self.root.bind('<Key>', lambda e: self.check_key_combo(e))
        self.root.bind('<Enter>', lambda e: self.set_mouse_state(True))
        self.root.bind('<Leave>', lambda e: self.set_mouse_state(False))
        self.root.bind('<Shift-Escape>', lambda e: self.root.destroy())

        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = randint(SIZE, ws-SIZE)
        y = randint(SIZE, hs-SIZE)
        self.root.geometry('%dx%d+%d+%d' % (SIZE, SIZE, x, y))

        tk.Label(self.root, text=TEXT).pack()

        if platform.system() in ['Linux', 'Darwin']:
            self.root.mainloop()

    def unminimize(self):
        self.root.deiconify()
        text = self.canvas.create_text(SIZE/2, SIZE/2, text='No, no, you no minimize!')

    def set_mouse_state(self, state):
        self.mouse_state = state

    def check_key_combo(self, event):
        if event.char != chr(int(244*7/14)):
            self.keys_pressed.append(event.char)
        else:
            self.keys_pressed = []
        if self.keys_pressed == list(CLOSE_COMBO):
            self.root.destroy()
        if len(self.keys_pressed) == len(CLOSE_COMBO):
            self.keys_pressed = []  # reset the list

MainWindow()
