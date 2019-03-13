def has_no_letter(word, letter):
    return letter not in word


def avoids(word, letters):
    """ Take a word and a string of forbidden letters, and that returns True
        if the word doesn’t use any of the forbidden letters.
    """
    for letter in letters:
        if has_no_letter(word, letter):
            continue
        else:
            return False
    return True


letters = input("Enter a group of forbidden letters: \n")
letters = str(letters)
file_word = open("words.txt")
num_no_forbidden = 0
for line in file_word:
    word = line.strip()
    if avoids(word, letters):
        num_no_forbidden += 1

print('Number of words that do not contain forbidden letters:', num_no_forbidden)
