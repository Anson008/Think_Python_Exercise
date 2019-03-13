import turtle


def polygon(t, length, sides):
    degree = 360/sides
    for i in range(sides):
        t.fd(length)
        t.lt(degree)
    turtle.mainloop()


peter = turtle.Turtle()
polygon(peter, length=50, sides=6)
