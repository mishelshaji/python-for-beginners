from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('300x200')
window.maxsize(300, 200)

lblusr = Label(text='Username')
lblpass = Label(text='Password')

txtuser = Entry(width='15')
txtpass = Entry(width='15', show='*')

def login():
    username = txtuser.get()
    password = txtpass.get()
    if (username == 'mishel' and password == '0015'):
        messagebox.showinfo('Alert', 'Welcome Mishel')
    else:
        messagebox.showinfo('Alert', 'Invalid User')

btnlogin = Button(text='Login', bg = 'green', fg = 'white', command=login)

lblusr.grid(row=0, column=0)
lblpass.grid(row=1, column=0)

txtuser.grid(row=0, column=1)
txtpass.grid(row=1, column=1)

btnlogin.grid(row=2, column=1)

window.mainloop()