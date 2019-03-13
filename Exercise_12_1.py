def make_hist(string):
    hist = {}
    for letter in string:
        hist[letter] = hist.get(letter, 0) + 1
    return hist


def most_frequent(string):
    """ Take a string and prints the letters in decreasing order of frequency.
    """
    hist = make_hist(string)

    t = []
    for letter, freq in hist.items():
        t.append((freq, letter))
    t.sort(reverse=True)

    res = []
    for freq, letter in t:
        res.append(letter)

    return res


string = open('emma.txt').read()
letter_seq = most_frequent(string)
for letter in letter_seq:
    print(letter)

