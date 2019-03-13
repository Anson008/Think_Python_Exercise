import turtle
import math


class Point:
    """ Represents a point in 2D space.

        Attributes: x, y
    """


class Rectangle:
    """ Represents a rectangle in 2D space.

        Attributes: width, height, corner
    """


class Circle:
    """ Represents a circle in 2D space.

        Attributes: center, radius
    """


def polygon(t, length, sides):
    degree = 360/sides
    for i in range(sides):
        t.fd(length)
        t.lt(degree)


def turtle_circle(t, r):
    circumference = 2 * math.pi * r
    sides = int(circumference / 3) + 1
    length = circumference / sides
    polygon(t, length, sides)


def draw_rect(t, rect):
    """ Takes a turtle object and rectangle object as parameters.
        Use the turtle to draw the rectangle.

        t: turtle
        rect: rectangle
    """
    t.pu()
    t.goto(rect.corner.x, rect.corner.y)
    t.setheading(0)
    t.pd()

    for length in rect.width, rect.height, rect.width, rect.height:
        t.fd(length)
        t.lt(90)


def draw_circle(t, circle):
    t.pu()
    t.goto(circle.center.x, circle.center.y)
    t.fd(circle.radius)
    t.lt(90)
    t.pd()

    turtle_circle(t, circle.radius)


anson = turtle.Turtle()

# Draw the axes
length = 200
anson.fd(length)
anson.bk(length)
anson.lt(90)
anson.fd(length)
anson.bk(length)

# Draw a rectangle
rect = Rectangle()
rect.width = 60
rect.height = 90
rect.corner = Point()
rect.corner.x = 10
rect.corner.y = 30

draw_rect(anson, rect)

# Draw a circle
circle = Circle()
circle.center = Point()
circle.center.x = 70
circle.center.y = 80
circle.radius = 60

draw_circle(anson, circle)



# wait for the user to close window
turtle.mainloop()
