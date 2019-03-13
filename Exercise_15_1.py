import math
import copy


class Point:
    """ Represents a point in 2D space.

        attributes: x, y
    """

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({:.1f}, {:.1f})".format(self.x, self.y)

    def distance(self, other):
        """ Returns the distance of two points.
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def move_point(self, other):
        """ Moves the original point by a 2D vector.

            other: point(vector)
        """
        self.x += other.x
        self.y += other.y
        return self


class Circle:
    """ Represents a circle.

        attributes: center, radius
    """

    def __init__(self, x=0.0, y=0.0, r=1.0):
        self.center = Point()
        self.center.x = x
        self.center.y = y
        self.r = r

    def __str__(self):
        return "C({:.1f}, {:.1f})\nR = {:.1f}\n".format(self.center.x, self.center.y, self.r)

    def move_circle(self, other):
        """ Shifts the center of a circle by a vector(point object).

            other: point
        """
        self.center.x += other.x
        self.center.y += other.y
        return self

    def enlarge(self, dr):
        """ Increase the radius of the circle by an amount dr."""
        self.r += dr
        return self


class Rectangle:
    """ Represents a rectangle.

        attributes: width, height, corner
    """

    def __init__(self, width=1.0, height=1.0, x=0.0, y=0.0):
        self.width = width
        self.height = height
        self.corner = Point()
        self.corner.x = x
        self.corner.y = y

    def __str__(self):
        return "Width = {:.1f}, Height = {:.1f}, Corner(({:.1f}, {:.1f}))".format(self.width, self.height,
                                                                                  self.corner.x, self.corner.y)


def distance_two_points(p1, p2):
    """ Takes two point objects as parameter and return their distance.

        p1, p2: point objects
    """
    d = math.sqrt((p1.x - p2. x)**2 + (p1.y - p2.y)**2)
    return d


def rect_center(rect):
    """ Takes a rectangle object as parameter and return its center.

    """
    rect.center = Point()
    rect.center.x = rect.corner.x + rect.width / 2
    rect.center.y = rect.corner.y + rect.height / 2
    return rect.center


def point_in_circle(circle, p):
    """ Takes objects 'circle' and 'point' as parameters.
        Return True if the point is in or on the boundary of the circle.

        circle, p: objects
    """
    return distance_two_points(circle.center, p) <= circle.r


def rectangle_in_circle(rect, circle):
    p = copy.copy(rect.corner)
    if not point_in_circle(circle, p):
        return False

    p.x += rect.width
    if not point_in_circle(circle, p):
        return False

    p.y += rect.height
    if not point_in_circle(circle, p):
        return False

    p.x -= rect.width
    if not point_in_circle(circle, p):
        return False

    return True


circle_1 = Circle(r=1, x=0, y=0)
p1 = Point(x=0.5, y=0.5)
print(point_in_circle(circle_1, p1))

rect_1 = Rectangle(width=0.5, height=0.5, x=0, y=0)

print(rectangle_in_circle(rect_1, circle_1))
