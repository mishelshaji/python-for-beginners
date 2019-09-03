from tkinter import *

window = Tk()
window.geometry('700x500')

txtbox = Entry(window, width='20')
txtbox.grid(row=0, column=0)

def clicked():
    txt = txtbox.get()
    btn.configure(text=txt)
btn = Button(window, text='Click Me', command=clicked)
btn.grid(row=0, column=1)

window.mainloop()