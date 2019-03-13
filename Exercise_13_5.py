import random
import string


def break_into_words(filename, header=False):
    fin = open(filename, encoding="utf-8")
    t = []
    for line in fin:
        if not header:
            if line.startswith("*END*THE SMALL PRINT!"):
                header = True
                continue
            else:
                continue
        line = line.replace("-", " ")
        line = line.replace("！", " ")
        line = line.replace("‘", " ")
        line = line.replace("’", " ")
        line = line.replace("'", " ")
        for word in line.split():
            w = word.strip(string.punctuation + string.whitespace + "“" + "”").lower()
            if len(w) > 1:
                t.append(w)
            else:
                continue
    return t


def make_hist(t):
    """ Take a list of strings as parameter and return a dictionary with strings as the keys
        and frequency as their values.

        t: list of strings
    """
    h = {}
    for x in t:
        h[x] = h.get(x, 0) + 1
    return h


def choose_from_hist(h):
    t = []
    for word, freq in h.items():
        t.extend([word] * freq)
    return random.choice(t)


words_in_book = break_into_words("emma.txt")
hist = make_hist(words_in_book)
print(choose_from_hist(hist))

