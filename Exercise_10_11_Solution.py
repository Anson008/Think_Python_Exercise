from __future__ import print_function, division

def in_bisect(t, word):
    if len(t) == 0:
        return False
    i = len(t) // 2
    if t[i] == word:
        return True
    if t[i] > word:
        return in_bisect(t[:i], word)
    else:
        return in_bisect(t[i+1:], word)


def make_word_list():
    t = []
    filh = open("words.txt")
    for line in filh:
        word = line.strip()
        t.append(word)
    return t


def reverse_pair(word_list, word):
    """Checks whether a reversed word appears in word_list.

    word_list: list of strings
    word: string
    """
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)


if __name__ == '__main__':
    word_list = make_word_list()

    for word in word_list:
        if reverse_pair(word_list, word):
            print(word, word[::-1])