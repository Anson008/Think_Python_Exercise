import bisect


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
    t = []
    fin = open(filename)
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def in_bisect_cheat(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


word_list = make_word_list("words.txt")
word = "apple"
print(in_bisect(word_list, word))
