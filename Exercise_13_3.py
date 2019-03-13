import string


def break_into_words(filename, header=True):
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


def most_frequent(t):
    """ Take a list of words as parameter. Count the frequency of each word
        and return a word list in frequency-descending order.
    """
    d = make_hist(t)
    t = []
    for word, freq in d.items():
        t.append((freq, word))
        t.sort(reverse=True)
    return t


def print_most_freq(t, num=10):
    """ Take a list of words as parameter. Print the top n most frequent words.

        t: list of words
        num: the number of most frequent words to print
    """
    t_freq = most_frequent(t)
    print("Top", num, "most frequent words:")
    count = 1
    for freq, word in t_freq[:num]:
        print(count, word, freq, sep="\t")
        count += 1


words_book = break_into_words("emma.txt", header=False)
print_most_freq(words_book, num=15)
