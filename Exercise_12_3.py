def finger_print(w):
    t = list(w)
    t.sort()
    t = tuple(t)
    return t


def find_anagrams(filename):
    fin = open(filename)
    d = {}
    for line in fin:
        word = line.strip().lower()
        t = finger_print(word)
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def metathesis_signature(t):
    d = {}
    for word in t:
        i = 0
        while i < len(word):
            if word[i:i+2] not in d:
                d[word[i:i+2]] = [word]
            else:
                d[word[i:i+2]].append(word)
            i += 1
    return d


def find_metathesis(d):
    for key in d:
        t = d[key]
        




