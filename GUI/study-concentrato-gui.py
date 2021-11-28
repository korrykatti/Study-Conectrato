from tkinter import *
from tkinter import ttk
import datetime
import time
import random
import webbrowser

root = Tk()
root.title("Study Concentrato")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def func_test_1():
    webbrowser.open("https://www.youtube.com/watch?v=rwSJwzE7lAg")

def func_test_2():
    webbrowser.open("https://www.youtube.com/watch?v=fcZXfoB2f70")

def func_test_3():
    webbrowser.open("https://www.youtube.com/watch?v=tZGpRd-t7jg")

def func_test_4():
    webbrowser.open("https://www.youtube.com/watch?v=ZYzbalQ6Lg8")

def current_position():
    return [root.winfo_pointerx(), root.winfo_pointery()]

pos1 = current_position()

minutes = tk.IntVar()
minutes_entry = ttk.Entry(mainframe, width=7, textvariable=minutes)
minutes_entry.grid(column=2, row=1, sticky=(W, E))

t_end = time.time() + 60 * minutes
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





