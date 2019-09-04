from tkinter import *
from tkinter.messagebox import *

top = Tk()
top.geometry("270x80")
top.title('Hello World')

def fun():
	a = e1.get()
	showinfo('Python','Hello '+a)


lbl1 = Label(top, text="User Name",bd = 5)
e1 = Entry(top)
b = Button(top,text="Hello",command=fun)

lbl1.pack( side = LEFT)
e1.pack(side = LEFT,padx=10)
b.pack(side = LEFT)

top.mainloop()