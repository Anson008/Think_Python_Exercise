# 1)
def do_twice(f):
    f()
    f()


def print_spam():
    print('spam')


do_twice(print_spam)


# 2)
def do_twice_2(f, v):
    """ Take two arguments, a function object and a value,
        and calls the function twice, passing the value as an argument.
    """
    f(v)
    f(v)


# 3) & 4)
def print_twice(bruce):
    print(bruce)
    print(bruce)


do_twice_2(print_twice, "spa")


# 5)
def do_four(f, v):
    """ takes a function object and a value and calls the function four times,
        passing the value as a parameter. There should be only two statements
        in the body of this function, not four.
    """
    do_twice_2(f, v)
    do_twice_2(f, v)


do_four(print, "star")
