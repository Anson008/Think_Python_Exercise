def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def print_histo(h):
    for c in h:
        print(c, h[c])


hist = histogram("parrot")
print(hist)
print(invert_dict(hist))
