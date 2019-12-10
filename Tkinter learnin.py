from tkinter import *

root = Tk()
root.title('Image Matching')
#root.iconbitmap('C:/Users/S1840085/Pictures/Rando trash/Icon.ico')

def myClick():
    myLabel = Label(root, text="You clicked a button, nice.")
    myLabel.pack()

#myLabel = Label(root, text="I am the Lorfecks")
myLabel2 = Label(root, text="and I speek for the trez")
myButton = Button(root , text="Click me, now", padx=100, command= myClick)

#myLabel.grid(row=0, column=0)
#myLabel2.grid(row=1, column=0)
#myButton.grid(row=2, column=0)
#myLabel.pack()
myLabel2.pack()
myButton.pack()

root.mainloop()