from tkinter import *
import tkinter.messagebox

var = Tk()
tkinter.messagebox.showinfo('Message', 'hi')
ans = tkinter.messagebox.askquestion('quiz', 'do you like python')
if ans == 'yes':
   print("You clicked yes")

var.mainloop()