from tkinter import *
from tkinter.messagebox import *

class App_2:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		master.title('Second Window')
		self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
		self.button.pack(side=LEFT)
		self.hi_there = Button(frame, text="Hello", command=self.say_hi)
		self.hi_there.pack(side=LEFT)

	def say_hi(self):
		showinfo('Python','Hello World!')