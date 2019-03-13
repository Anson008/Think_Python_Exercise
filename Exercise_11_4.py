def has_duplicates_dict(t):
    d = dict()
    for x in t:
        d[x] = d.get(x, 0) + 1
        if d[x] >= 2:
            return True
    return False


t1 = [1, 2, 3, 4]
t2 = [1, 2, 2, 3]
t3 = ['a', '1', 'a', "da"]
print(has_duplicates_dict(t1))
print(has_duplicates_dict(t2))
print(has_duplicates_dict(t3))