from tkinter import *

window = Tk()
canvas = Canvas(window, width=200, height=200, bg='white')
canvas.pack()
canvas.create_line(50, 50, 100, 100)

window.mainloop()
