import math


def estimate_pi():
    """ Use Srinivasa Ramanujan formula to compute and return an estimate of π.
    """
    k = 0
    epsilon = 1e-15
    total = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        mun = math.factorial(4 * k) * (1103 + 26390 * k)
        den = math.factorial(k) ** 4 * 396 ** (4 * k)
        term = factor * mun / den
        total = total + term
        if abs(term) < epsilon:
            break
        k = k + 1
    my_pi = 1 / total
    return my_pi


a = estimate_pi()
b = math.pi
print('My pi:', a)
print('math.pi: ', b)
print('Difference: ', abs(a - b))
