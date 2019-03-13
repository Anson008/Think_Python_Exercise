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


def interlock(t_word, word):
    word1 = word[::2]
    word2 = word[1::2]
    return in_bisect(t_word, word1) and in_bisect(t_word, word2)


t_word = make_word_list()
total = 0
for word in t_word:
    if interlock(t_word, word):
        total += 1
        print(word, word[::2], word[1::2])
print("Total:", total)
