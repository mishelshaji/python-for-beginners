from tkinter import *
from tkinter.messagebox import *
import Ch_11_008

class App_1:
	def __init__(self, master):
		frame = Frame(master)
		self.win = frame
		frame.pack()
		master.title('First Window')
		self.button = Button(frame, text="QUIT", fg="green", command=frame.quit)
		self.button.pack(side=LEFT)
		self.hi_there = Button(frame, text="Hello", command=self.say_hi)
		self.hi_there.pack(side=LEFT)

	def say_hi(self):
		self.win.destroy()
		app = Ch_11_008.App_2(root)

root = Tk()
root.geometry("270x80")
app = App_1(root)

root.mainloop()
root.destroy() # optional; 