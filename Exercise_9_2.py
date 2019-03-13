def has_no_e(word):
    """Return True if the given word doesn’t have the letter “e” in it.
    """
    result = 'e' not in word
    return result


filh = open('words.txt')
num_words = 0
count_no_e = 0
for line in filh:
    word = line.strip()
    if has_no_e(word):
        print(word)
        count_no_e = count_no_e + 1
    num_words += len(word)
ratio_no_e = count_no_e / num_words
print("Number of words that have no 'e': ", count_no_e)
print("Total number of words: ", num_words)
print("Percentage of words that have no 'e': {:.2%}".format(ratio_no_e))
