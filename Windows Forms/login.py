from tkinter import *
from tkinter.messagebox import *

class Login:
	def __init__(self,app):
		#app.geometry('250x120');
		app.title('Login')
		frame = Frame(app,width=250,height=120)
		self.frame = frame
		frame.pack()
		#designing Window
		Label(frame,text = 'User Name').place(x=10,y=10)
		self.uname = Entry(frame)
		self.uname.place(x=100,y=10)
		Label(frame,text = 'Password').place(x=10,y=50)
		self.pwd = Entry(frame,show='?')
		self.pwd.place(x=100,y=50)
		Button(frame,text='Login',command=self.isValid).place(x=180,y=80)
	def isValid(self):
		un 	= self.uname.get()
		pwd = self.pwd.get()
		if(un=='abc' and pwd=='123'):
			self.frame.destroy()
			Welcome(root,un)
		else:
			showinfo('Warning', 'Invalid User !!!')

class Welcome:
	def __init__(self,app,msg):
		#app.geometry('250x120');
		app.title('Welcome')
		frame = Frame(app,width=250,height=120)
		self.frame = frame
		frame.pack()
		#designing Window
		Label(frame,text = 'Welcome '+msg).place(x=10,y=10)

root = Tk()
log = Login(root)
root.mainloop()