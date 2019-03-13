import string


def in_bisect(t, word):
    """ Take a sorted list and a target value and returns the index of the value
        in the list if it’s there, or None if it’s not.
    """
    if len(t) == 0:
        return False
    i = len(t) // 2
    if t[i] == word:
        return True
    if t[i] > word:
        return in_bisect(t[:i], word)
    else:
        return in_bisect(t[i+1:], word)


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


def diff_words(w_book, w_list):
    """ Take a list of words in a book and a word list as parameters.
        Return the words that are in the book but not in the words list.

        w_book, w_list: lists
    """
    t = []
    for key in make_hist(w_book):
        if in_bisect(w_list, key):
            continue
        else:
            t.append(key)
    return t


words_in_book = break_into_words("emma.txt", header=False)
words_in_list = make_word_list("words.txt")
print("The words in the book that aren't in the word list are:")
t = diff_words(words_in_book, words_in_list)
t.sort()
for word in t:
    print(word)
