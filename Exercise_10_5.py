def is_sorted(t):
    """ Take a list as a parameter and returns True if the list is sorted in ascending order and False otherwise.
    """
    if t == sorted(t):
        return True
    else:
        return False


t1 = [2, 1, 3]
t2 = [1, 2, 3]
print(is_sorted(t1))
print(is_sorted(t2))
