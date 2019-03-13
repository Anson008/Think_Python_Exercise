def has_duplicates(t):
    """Take a list and returns True if there is any element that appears more than once.
    """
    for x in t:
        mun_of_x = t.count(x)
        if mun_of_x > 1:
            return True
    return False


t1 = [1, 2, 3, 4]
t2 = [1, 2, 2, 3]
t3 = ['a', '1', 'a', "da"]
print(has_duplicates(t1))
print(has_duplicates(t2))
print(has_duplicates(t3))

