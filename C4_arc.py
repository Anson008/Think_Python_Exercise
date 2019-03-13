import turtle
import math


def polyline(t, length, sides, degree):
    for i in range(sides):
        t.fd(length)
        t.lt(degree)
    turtle.mainloop()


def arc(t, r, angle):
    arc_length = (angle / 360) * (2 * math.pi * r)
    sides = int(arc_length / 3) + 1
    degree = angle / sides
    length = arc_length / sides
    polyline(t, length, sides, degree)


abe = turtle.Turtle()
arc(abe, 50, 260)
