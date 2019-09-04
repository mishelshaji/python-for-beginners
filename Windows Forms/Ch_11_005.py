from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from functools import partial

top = Tk()

def fun():
	s = vartxt.get().strip()
	if(len(s)==0):
		showinfo('Hello','Can''t allow blank')
		return
	s = s.capitalize()
	if(s in cmb_1['values']):
		showinfo('Hello','Duplication not allowed')
		return
	lst = list(cmb_1['values'])
	lst.append(s)
	tup = tuple(lst)
	cmb_1['values'] = tup

top.geometry("500x80")
top.title('Hello World')
lbl_1 = Label(top,text='Item')
vartxt = StringVar()
txt_1 = Entry(top,textvariable=vartxt)
btn_1 = Button(top,text='Add',command= fun)
var_cmb = StringVar()
cmb_1 = Combobox(top,textvariable=var_cmb)
cmb_1['values'] = ('Apple','Orange','Grapes','Mango')
cmb_1.current(0)

lbl_1.pack(side = LEFT,padx=10)
txt_1.pack(side = LEFT,padx=10)
btn_1.pack(side = LEFT,padx=10)
cmb_1.pack(side = LEFT,padx=10)
top.mainloop()