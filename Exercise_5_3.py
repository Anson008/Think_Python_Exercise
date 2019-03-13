def is_triangle(a, b, c):
    """ Take three integers as arguments, and that prints either “Yes” or “No”, depending on
        whether you can or cannot form a triangle from sticks with the given lengths.

        a, b, c: integer
    """
    if a + b > c and b + c > a and a + c > b:
        print('Yes.')
    else:
        print('No.')


def check_triangle():
    """ Prompt the user to input three stick lengths, converts them to integers,
        and uses is_triangle to check whether sticks with the given lengths can form a triangle.
    """
    a = input("Enter an integer a: ")
    a = int(a)
    b = input("Enter an integer b: ")
    b = int(b)
    c = input("Enter an integer c: ")
    c = int(c)
    return is_triangle(a, b, c)


check_triangle()
