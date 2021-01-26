import turtle

win = turtle.Screen()
alex = turtle.getturtle()
alex.shape("turtle")

for i in range(10):
    for j in range(4):
        alex.forward(100)
        alex.left(90)
    alex.left(10)

win.exitonclick()
