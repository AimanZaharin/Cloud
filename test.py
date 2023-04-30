import sys
from tkinter import *

def assign(value):
    global x
    x = value
    mGui.destroy()

mGui = Tk()
mGui.geometry("500x100+500+300")
mGui.title("Attribute Selection Window")

frame1 = Frame(mGui)
frame1.pack()

mLabel = Label(frame1, text = "Please select one of the following attributes to assign to the selected Convwks feature:").grid(row=0, column=0)

frame2 = Frame(mGui)
frame2.pack()


mButton = Button(frame2, text = "CON", command = lambda: assign("CON")).grid(row=0, column=0, padx=10)
mButton = Button(frame2, text = "MS", command = lambda: assign("MS")).grid(row=0, column=1, padx=10)
mButton = Button(frame2, text = "DRN", command = lambda: assign("DRN")).grid(row=0, column=2, padx=10)
mGui.mainloop()     #FOR WINDOWS ONLY