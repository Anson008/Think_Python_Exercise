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
    """ Take a list of words as parameter. Count the number of times each word is used
        and return a dictionary with words as keys and number of times as values.
    """
    hist = {}
    for word in t:
        hist[word] = hist.get(word, 0) + 1
    return hist


def total_words(hist):
    """ Take a dictionary of words (key) and frequencies (value) as parameter.
        Count the total number of words, i.e., the sum of values of the dictionary.
    """
    return sum(hist.values())


def num_different_words(hist):
    """ Take a dictionary of words (key) and frequencies (value) as parameter.
        Count the number of different words, i.e., the length of the dictionary.
    """
    return len(hist)


words_in_text = break_into_words('emma.txt')
hist = make_hist(words_in_text)

print("Total number of words:", total_words(hist))
print("Number of different words:", num_different_words(hist))
