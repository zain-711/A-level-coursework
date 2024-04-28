from tkinter import *

root = Tk()
e = Entry(root, width = 30)
e.pack()
e.get()
e.insert(0,"Enter your name")

def myclick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()
    
nextButton = Button(root, text="Next", padx=20, pady=10, command = myclick,)#Creates a button, padx and pady are the dimentions, changing these values changes the size of the button 
nextButton.pack()

root.mainloop()
