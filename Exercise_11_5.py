def rotate_letter(letter, n):
    if letter.islower():
        start = ord('a')
    elif letter.isupper():
        start = ord('A')
    else:
        return letter
    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    rotated = ''
    for letter in word:
        rotated = rotated + rotate_letter(letter, n)
    return rotated


def make_word_dict():
    d = {}
    fileh = open("words.txt")
    for line in fileh:
        word = line.strip()
        d[word] = d.get(word, 0)
    return d


def rotate_pair(word, word_dict):
    total = 0
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print(word, rotated)
            total += 1
    return total


word_dict = make_word_dict()
total = 0
for word in word_dict:
    total += rotate_pair(word, word_dict)
print("Total:", total)
