def right_justify(s):
    """ prints the string with enough leading spaces so that
        the last letter of the string is in column 70 of the display.

        s: string
    """
    space = ' ' * (70 - len(s))
    length = len(' ' * (70 - len(w)) + w)
    print(space, s)
    print("Length:", length)


word = input('Enter a word:\n')
w = str(word)
right_justify(w)
