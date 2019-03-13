import string


def make_word_list(filename):
    """ Read a file and return the words in the file as a list.

        filename: string (file directory)
    """
    t = []
    fin = open(filename)
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


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


def diff_words(x1, x2):
    """ Take two sequences x1 and x2 as parameters.
        Return a set of all keys that appear in x1 but not x2.

        x1, x2: lists, dictionaries
    """
    return set(x1) - set(x2)


words_in_book = break_into_words("emma.txt")
words_in_list = make_word_list("words.txt")


t = []
for word in diff_words(words_in_book, words_in_list):
    t.append(word)
t.sort()

for word in t:
    print(word)
