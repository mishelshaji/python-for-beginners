from tkinter import *
window = Tk()

frame = Frame(window, bg="teal", height=500, width=500)
img = PhotoImage(file="default.png")
background = Label(window, image=img)
background.place(x=0, y=0, relwidth=1, relheight=1)
button = Button(window, text='click me', pady=10)
button.place(x=5, y=10, relwidth=1)
frame.pack()
window.mainloop()

# pip install Pillow
# from PIL import Image
# from PIL import ImageTk
# import tkinter
#
# image = Image.open('bll.jpg')
# image = image.resize((20, 20))
# image = ImageTk.PhotoImage(image)
#
# canv = Canvas(root, width=80, height=80, bg='white')
# canv.grid(row=2, column=3)
#
# img = PhotoImage(file=image)
