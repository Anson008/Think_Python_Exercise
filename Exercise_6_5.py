def gcd(a, b):
    """Take parameters a and b and returns their greatest common divisor.

        a, b: integer
    """
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)


print(gcd(6, 8))
