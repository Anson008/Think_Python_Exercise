def has_letter(word, letter):
    return letter in word


def find_letter(word, letters):
    for letter in letters:
        if has_letter(word, letter):
            continue
        else:
            return False
    return True


def use_only(word, letters):
    """ Take a word and a string of letters, and that
        returns True if the word contains only letters in the list.
    """
    letters_in_word = list(word)
    letters_in_string = list(letters)
    print("Letters in word:", letters_in_word)
    print("Letters in string:", letters_in_string)
    return find_letter(letters, letters_in_word)


print(use_only("apple", "apue"))
