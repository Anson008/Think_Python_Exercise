def rotate_letter(letter, n):
    """ Take a string and an integer as parameters, and returns a new string that
        contains the letters from the original string rotated by the given amount.

        letter: string
        n: integer
    """
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


print(rotate_word('abc', 1))
