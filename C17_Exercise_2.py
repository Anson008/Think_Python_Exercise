class Point:
    """ Represents a point in 2D space.
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_point(self):
        print("({:.1f}, {:.1f})".format(self.x, self.y))

    def add_point(self, other):
        np = Point()
        np.x = self.x + other.x
        np.y = self.y + other.y
        return np

    def add_tuple(self, other):
        np = Point()
        np.x = self.x + other[0]
        np.y = self.y + other[1]
        return np

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def __str__(self):
        return "({:.1f}, {:.1f})".format(self.x, self.y)

    def __radd__(self, other):
        return self.__add__(other)


p = Point(5, 3)
q = Point(-9, 1)
t = (1, 3,)
p.print_point()
print("Point q:", q)
(p+q).print_point()
print("Point (p+q):", p+q)
print("Point (p+t):", p+t)
print("Point (t+p):", t+p)
