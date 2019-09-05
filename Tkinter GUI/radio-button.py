from tkinter import *

def selection():
    selection = "You selected the option " + str(radio.get())
    label.config(text=selection)

top = Tk()
top.geometry("300x150")
radio = IntVar()
Label(text="Favourite programming language:").pack()
R1 = Radiobutton(top, text="C", variable=radio, value=1, command=selection).pack(anchor=W)
R2 = Radiobutton(top, text="C++", variable=radio, value=2, command=selection).pack(anchor=CENTER)
R3 = Radiobutton(top, text="Java", variable=radio, value=3, command=selection).pack(anchor=E)

label = Label(top)
label.pack()
top.mainloop()