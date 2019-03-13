def is_abecedarian(word):
    """ Return True if the letters in a word appear in alphabetical order (double letters are okay).
    """
    order = ord('a')
    for letter in word:
        if ord(letter) >= order:
            order = ord(letter)
        else:
            return False
    return True


print(is_abecedarian('abcdea'))

file_word = open('words.txt')
count = 0
for line in file_word:
    word = line.strip()
    if is_abecedarian(word):
        count += 1
print(count)
