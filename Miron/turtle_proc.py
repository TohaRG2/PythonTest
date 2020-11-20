import turtle


def module(a):
    if a < 0:
        a = a * -1
    return a


def up():
    turtle.speed(10)
    turtle.fd(20)
    xsize = turtle.window_width() // 2
    ysize = turtle.window_height() // 2
    if module(turtle.xcor()) > xsize:
        win.bye()
    if module(turtle.ycor()) > ysize:
        win.bye()


def left():
    turtle.speed(10)
    turtle.left(90)


def rigth():
    turtle.speed(10)
    turtle.right(90)


def reset():
    turtle.goto(0, 0)
    turtle.clear()


def width1():
    turtle.down()
    turtle.width(1)


def width5():
    turtle.down()
    turtle.width(5)


def width0():
    turtle.up()


win = turtle.Screen()

win.onkey(up, "Up")
win.onkey(rigth, "Right")
win.onkey(left, "Left")
win.onkey(reset, "r")
win.onkey(exit, "Escape")
win.onkey(width0, "0")
win.onkey(width1, "1")
win.onkey(width5, "5")
win.listen()
win.mainloop()

# win.exitonclick()
