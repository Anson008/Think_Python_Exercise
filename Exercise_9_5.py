def has_letter(word, letter):
    return letter in word


def use_all(word, letters):
    """ Take a word and a string of required letters, and that returns True
        if the word uses all the required letters at least once.
    """
    letters = list(letters)
    for letter in letters:
        if has_letter(word, letter):
            continue
        else:
            return False
    return True


print(use_all("apple", "apld"))

string = "aeiou"
count = 0
file_words = open("words.txt")
for line in file_words:
    word = line.strip()
    if use_all(word, string):
        count += 1
print(count)
