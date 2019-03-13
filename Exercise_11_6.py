def look_up_dict(w):
    d = dict()
    fileh = open("words.txt")
    for line in fileh:
        word = line.strip()
        d[word] = d.get(word, 1)
    print(w in d)
    return d