import turtle
import math


def polygon(t, length, sides):
    degree = 360/sides
    for i in range(sides):
        t.fd(length)
        t.lt(degree)
    turtle.mainloop()


def circle(t, r):
    circumference = 2 * math.pi * r
    sides = int(circumference / 3) + 1
    length = circumference / sides
    polygon(t, length, sides)


charry = turtle.Turtle()
circle(charry, r=50)
