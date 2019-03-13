def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    """ Take a string argument and returns True if it is a palindrome and False otherwise.

        word: string
    """
    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    return is_palindrome(middle(word))


word = "refer"
print(is_palindrome(word))
