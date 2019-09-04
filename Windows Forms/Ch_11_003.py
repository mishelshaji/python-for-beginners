from tkinter import *
from tkinter.messagebox import *
from functools import partial

top = Tk()
top.geometry("240x150")
top.title('Hello World')
top.config(bg='white')

def fun(x):
	flg = 0
	try:
		a = float(e1.get())
		flg = 1
		b = float(e2.get())
		c = 0
		if(x==1): c = a + b
		elif(x==2): c = a - b
		elif(x==3): c = a * b
		else: c = a / b
		ans.set(c)
	except (Exception) as e:
		showinfo('Error',e)
		if(flg==0): e1.focus_set();e1.select_to(END)
		else: e2.focus_set();e2.select_to(END)

Label(top, text="First No: ",bg='white').place(x=10,y=10)
Label(top, text="Second No: ",bg='white').place(x=10,y=40)
Label(top, text="Result: ",bg='white').place(x=10,y=70)

e1 = Entry(top,justify=RIGHT)
e2 = Entry(top,justify=RIGHT)
ans = DoubleVar()
e3 = Entry(top,justify=RIGHT, textvariable=ans, state='readonly')
e1.focus_set()
e1.place(x=100,y=10)
e2.place(x=100,y=40)
e3.place(x=100,y=70)

Button(top,text="  +  ",command=partial(fun,1)).place(x=95,y=100)
Button(top,text="  -  ",command=partial(fun,2)).place(x=130,y=100)
Button(top,text="  X  ",command=partial(fun,3)).place(x=165,y=100)
Button(top,text="  /  ",command=partial(fun,4)).place(x=200,y=100)

top.mainloop()