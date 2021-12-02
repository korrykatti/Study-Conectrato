from tkinter import *
from tkinter import ttk
import webbrowser
import datetime
import time
import random

def lofi():
    webbrowser.open("https://www.youtube.com/watch?v=5qap5aO4i9A")

def testing():
    lol = int(min.get())
    minutes = lol * 60
    print("Starting up in 60 seconds so do whatever you want to and come in a minute and dont u dare move your mouse or the unexpected will happen lol i am not joking i am serious ")
    time.sleep(60)
    print("Haha your time ends less go")
   
    def func_test_1():
        webbrowser.open("https://www.youtube.com/watch?v=rwSJwzE7lAg")

    def func_test_2():
        webbrowser.open("https://www.youtube.com/watch?v=fcZXfoB2f70")

    def func_test_3():
        webbrowser.open("https://www.youtube.com/watch?v=tZGpRd-t7jg")

    def func_test_4():
        webbrowser.open("https://www.youtube.com/watch?v=ZYzbalQ6Lg8")

    root = Tk()

    def current_position():
        return [root.winfo_pointerx(), root.winfo_pointery()]

    pos1 = current_position()

    t_end = time.time() +minutes
    while time.time() < t_end :

        time.sleep(0.5)
        pos2 = current_position()
        if not pos1 == pos2:
       # run a command:
            my_list = [func_test_1, func_test_2, func_test_3, func_test_4]
            random.choice(my_list)()
        
        pos1 = pos2

    else:
        webbrowser.open("https://www.youtube.com/watch?v=Zd9muK2M36c")





root = Tk()
root.title("Study Conectrato")


def clam():
    s = ttk.Style()
    s.theme_use('clam')
def classic():
    s = ttk.Style()
    s.theme_use('classic')
def alt():
    s = ttk.Style()
    s.theme_use('alt')
def default():
    s = ttk.Style()
    s.theme_use('default')


lofi = ttk.Button(root, text="Press To Play LOFI ( choose wisely ) ", default="active", command=lofi).grid(column=1, row=10, sticky=W)

parent = ttk.Frame(root, padding="10 10 10 10")
parent.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(parent, text="Enter Number Of Minutes : ").grid(column=2, row=1, sticky=E)
min = StringVar()
min_entry = ttk.Entry(parent, width=7, textvariable=min)
min_entry.grid(column=4, row=1, sticky=(W, E))

action = ttk.Button(root, text="Click Me To Start", default="active", command=testing).grid(column=3, row=3, sticky=W)
root.bind("<Return>", testing)

ttk.Label(parent, text="Select Theme Or Leave it as it is ").grid(column=1, row=7, sticky=S)
clam = ttk.Button(root, text="Clam", default="active", command=clam).grid(column=4, row=4, sticky=W)
alt = ttk.Button(root, text="Alt", default="active", command=alt).grid(column=5, row=4, sticky=W)
default = ttk.Button(root, text="Default", default="active", command=default).grid(column=6, row=4, sticky=W)
classic = ttk.Button(root, text="Classic", default="active", command=classic).grid(column=7, row=4, sticky=W)

root.mainloop()
