from tkinter import *
from tkinter import ttk

def testing():
    lol = int(min.get())
    minutes = lol * 60
    print(minutes)

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
