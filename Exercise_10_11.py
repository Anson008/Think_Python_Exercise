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


def find_reverse_pair(word_list, word):
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)


word_list = make_word_list()
total = 0
for x in word_list:
    if find_reverse_pair(word_list, x):
        total += 1
        print(x, x[::-1])
print("Total:", total)
