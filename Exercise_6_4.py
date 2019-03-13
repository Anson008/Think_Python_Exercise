def is_power(a, b):
    """ Take parameters a and b and returns True if a is a power of b.

        a, b: floating-point number
    """
    if a / b == 1:
        return True
    elif a / b != 1:
        return False
    else:
        return is_power(a/b, b)


print(is_power(a=1.6, b=3))
