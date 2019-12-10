from tkinter import *

root = Tk()
myLabel = Label(root, text="I am the Lorfecks")
myLabel2 = Label(root, text="and I speek for the trez")
myButton = Button(root , text="Click me, now", padx=100)

myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myButton.grid(row=2, column=0)

#def myClick():

root.mainloop()