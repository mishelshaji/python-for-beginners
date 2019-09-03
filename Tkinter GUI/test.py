from tkinter import *
window = Tk()

frame = Canvas(window, bg="teal", height=500, width=500)
img = PhotoImage(file="default.png")
background = Label(window, image=img)
background.place(x=0, y=0, relwidth=1, relheight=1)

lbluser = Label(text='Username')
lbluser.place(x=100, y=300, relwidth=0.8)
button = Button(window, text='click me', pady=10)
button.place(x=5, y=10, relwidth=1)
frame.pack()
window.mainloop()
