def chop(t):
    """ Takes a list, modifies it by removing the first and last elements, and returns None.
    """
    del t[0]
    del t[-1]


t = [1, 2, 3, 4, 5, 6]
s = chop(t)
print(t)
print(s)
