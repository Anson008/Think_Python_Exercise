import time


def look_up_dict(w):
    """ Read the words in words.txt and stores them as keys in a dictionary.
    """
    d = dict()
    fileh = open("words.txt")
    for line in fileh:
        word = line.strip()
        d[word] = d.get(word, 1)
    print(w in d)
    return d


def look_up_list(w):
    t = list()
    fileh = open("words.txt")
    for line in fileh:
        word = line.strip()
        t.append(word)
    print(w in t)
    return t


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


def look_up_bisect(w):
    t = []
    filh = open("words.txt")
    for line in filh:
        word = line.strip()
        t.append(word)
    print(in_bisect(t, w))
    return t


w = "appear"

start_time = time.time()
look_up_dict(w)
elapsed_time = time.time() - start_time
print("Dictionary:", elapsed_time, "seconds")
print("")


start_time = time.time()
look_up_list(w)
elapsed_time = time.time() - start_time
print("List:", elapsed_time, "seconds")
print("")

start_time = time.time()
look_up_bisect(w)
elapsed_time = time.time() - start_time
print("Bisect:", elapsed_time, "seconds")

