from tkinter import *
from tkinter.messagebox import *

top = Tk()

def fun():
	showinfo('Python','Hello World!')

photo=PhotoImage(file="1.gif")
#photo=photo.subsample(4, 4)
b = Button(top,text="Hello",command=fun)
b.config(image=photo)
b.pack()
top.mainloop()

'''
	Button
	======
	bg='blue',fg='white',activebackground='#A0AF00',
	activeforeground='yellow',height='2',width='10',
	wraplength='30',image=photo
'''