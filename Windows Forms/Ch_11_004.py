from tkinter import *
from tkinter.messagebox import *
from functools import partial

top = Tk()
top.geometry("550x80")
top.title('Hello World')

def fun_chk():
	res = ''
	if(var_chk_1.get()==1): res+='English '
	if(var_chk_2.get()==1): res+='Malayalam '
	if(var_chk_3.get()==1): res+='Hindi '
	var_lbl_1.set(res)
def fun_rd():
	c = rg_col.get()
	lbl_1.config(fg = c)
	#showinfo('Error',c)

var_chk_1 = IntVar()
var_chk_2 = IntVar()
var_chk_3 = IntVar()
chk_1 = Checkbutton(top,text='English',command=fun_chk,variable=var_chk_1)
chk_2 = Checkbutton(top,text='Malayalam',command=fun_chk,variable=var_chk_2)
chk_3 = Checkbutton(top,text='Hindi',command=fun_chk,variable=var_chk_3)

rg_col = StringVar()
rd_1 = Radiobutton(top,text='Red',value='red',variable=rg_col,command=fun_rd)
rd_2 = Radiobutton(top,text='Green',value='green',variable=rg_col,command=fun_rd)
rd_3 = Radiobutton(top,text='Blue',value='blue',variable=rg_col,command=fun_rd)
rd_1.select()

var_lbl_1 = StringVar()
var_lbl_1.set('please select ..')
lbl_1 = Label(top,textvariable=var_lbl_1,fg='red')

chk_1.pack(side = LEFT)
chk_2.pack(side = LEFT)
chk_3.pack(side = LEFT)

rd_1.pack(side = LEFT)
rd_2.pack(side = LEFT)
rd_3.pack(side = LEFT)
lbl_1.pack(side = LEFT)

top.mainloop()