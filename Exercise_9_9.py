def find_mirror(a, b):
    if str(a).zfill(2)[0] == str(b).zfill(2)[1] and str(a).zfill(2)[1] == str(b).zfill(2)[0]:
        return True
    else:
        return False


a = 0   # age of daughter
b = 1   # age of mother
count = 1
while b < 99:
    i = b
    m = a
    n = b
    diff = 0
    while i <= 99:
        if find_mirror(m, n):
            if diff == n - m:
                count += 1
            else:
                count = 1
            diff = n - m
            print(m, n, diff, count)
        m += 1
        n += 1
        i += 1
    b += 1
