from tkinter import *
window = Tk()
window.maxsize(500, 500)
window.minsize(400, 400)
lbl = Label(window, text="Hello world",
            bg='red', fg='yellow',
            height='5', width='20',
            font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
window.mainloop()