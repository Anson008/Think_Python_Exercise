def print_plus_minus():
    print('+', '- - - -', '+', '- - - -', '+', '- - - -', '+')


def print_vertical():
    print('|', ' ' * 7, '|', ' ' * 7, '|', ' ' * 7, '|')


def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_grid():
    print_plus_minus()
    do_four(print_vertical)
    print_plus_minus()
    do_four(print_vertical)
    print_plus_minus()
    do_four(print_vertical)
    print_plus_minus()


print_grid()
