def finger_print(w):
    t = list(w)
    t.sort()
    t = tuple(t)
    return t


def find_anagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = finger_print(word)
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagrams_sets(d):
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagrams_ordered(d):
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))
    t.sort(reverse=True)
    for x in t:
        print(x)


d = find_anagrams("words.txt")
print_anagrams_ordered(d)
