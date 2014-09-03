#!/usr/bin/env python

from Tkinter import *
import tkMessageBox

def show_alert():
    root.bell()
    tkMessageBox.showinfo("Ready!", "DING!")
    quit()

def start_timer():
    root.after(scale.get() * 1000, show_alert)

root = Tk()

minutes = Label(root, text="Minute:")
minutes.grid(row=0, column=0)

scale = Scale(root, from_=1, to=60, orient=HORIZONTAL, length=600)
scale.grid(row=0, column=1)

button = Button(root, text="Start timing", command=start_timer)
button.grid(row=1, column=1, pady=5, sticky=E)

root.mainloop()
