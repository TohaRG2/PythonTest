from random import *
from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Графическая программа на Python")
root.wm_attributes("-topmost", 1)

size = 600
canvas = Canvas(root, width=size, height=size)
canvas.pack()
diapason = 0

while diapason < 1000:
    colors = choice(
        ['blue', 'green', 'maroon', 'orange', 'pink', 'purple', 'red', 'yellow', 'violet', 'chartreuse'])
    x0 = randint(0, size)
    y0 = randint(0, size)
    d = randint(0, size / 5)
    canvas.create_oval(x0, y0, x0 + d, y0 + d, fill=colors)
    root.update()
    diapason += 1

root.mainloop()
