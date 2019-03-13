import random
import bisect
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


def random_word(h):
    """ Chooses a random word from a histogram. The probability of each word is proportional to its frequency.

        hist: dictionary, map from word to frequency
    """
    words = []
    freq = []
    total_freq = 0
    for key, value in h.items():
        words.append(key)
        total_freq += value
        freq.append(total_freq)

    x = random.randint(0, total_freq - 1)
    index = bisect.bisect_left(freq, x)
    return words[index]


words_in_book = break_into_words("emma.txt")
hist = make_hist(words_in_book)
print(random_word(hist))
