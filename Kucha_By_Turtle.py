import turtle
import random

# kucha = random.randint(5, 25)
kucha = 10
win = turtle.Screen()
alex = turtle.Turtle()
alex.speed("fastest")
row_count = 1
max_in_kucha = 1

while kucha > max_in_kucha:
    row_count = row_count + 1
    max_in_kucha = max_in_kucha + row_count

alex.write(str(kucha))
alex.penup()
alex.right(90)
alex.fd(row_count * 40)
alex.right(90)
alex.fd(row_count * 20)
alex.left(180)

alex.pendown()
output_count = 0
while output_count < kucha:
    output_in_row = 0
    while output_in_row < row_count and output_count < kucha:
        alex.pendown()
        alex.circle(20)
        alex.penup()
        alex.fd(40)
        output_in_row += 1
        output_count += 1
    row_count -= 1
    alex.left(90)
    alex.fd(36)
    alex.left(90)
    alex.fd(20)
    alex.fd(40 * row_count)
    alex.left(180)
    alex.pendown()

win.exitonclick()
