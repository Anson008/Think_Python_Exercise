import time


def read_words_1():
    fhandle = open("words.txt")
    t = []
    for line in fhandle:
        word = line.strip()
        t.append(word)
    return t


def read_words_2():
    fhandle = open("words.txt")
    t = []
    for line in fhandle:
        word = line.strip()
        t = t + [word]
    return t


start_time = time.time()
t = read_words_1()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

start_time = time.time()
t = read_words_2()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

