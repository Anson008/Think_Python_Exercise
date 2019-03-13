import math
from prettytable import PrettyTable


def my_sqrt(a, x):
    """ Find the square root of a by Newton's method.

        x: estimated value of sqrt(a)
    """
    epsilon = 0.000001
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            return y
            break
        x = y


def test_square_root():
    """ Print a table. The first column is a number, a; the second column is the square root
        of a computed with mysqrt; the third column is the square root computed by math.sqrt;
        the fourth column is the absolute value of the difference between the two estimates.
    """
    a = 1
    t = PrettyTable(["a", "my_sqrt(a)", "math.sqrt(a)", "diff"])
    t.align = "l"
    while a <= 9:
        t.add_row([a, my_sqrt(a, a/3), math.sqrt(a), abs(my_sqrt(a, a/3) - math.sqrt(a))])
        a += 1
    print(t)


test_square_root()
