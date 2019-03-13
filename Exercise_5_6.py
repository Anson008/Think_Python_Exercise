import turtle


def koch(t, length):
    if length < 60:
        t.fd(length)
        return
    m = length / 3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snow_flake(t, n):
    for i in range(3):
        koch(t, n)
        t.rt(120)


t_koch = turtle.Turtle()
t_koch.pu()
t_koch.goto(-150, 100)
t_koch.pd()
snow_flake(t_koch, 600)
turtle.mainloop()
