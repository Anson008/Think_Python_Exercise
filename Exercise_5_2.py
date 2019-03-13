def check_fermat(a, b, c, n):
    """ Take four parameters — a, b, c and n - and checks to see if Fermat’s theorem holds.
        If n is greater than 2 and a^n + b^n = c^n, the program should print, “Holy smokes, Fermat was wrong!”
        Otherwise the program should print, “No, that doesn’t work.

        a, b, c: positive integer
    """
    if n > 2 and a ** n + b ** n == c ** n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn’t work.')


def prompt_fermat():
    """ Prompt the user to input values for a, b, c and n, converts them to integers,
        and uses check_fermat to check whether they violate Fermat’s theorem.
    """
    a = input('Enter a floating number a: ')
    a = float(a)
    b = input('Enter a floating number b: ')
    b = float(b)
    c = input('Enter a floating number c: ')
    c = float(c)
    n = input('Enter an integer n, which is greater than 2: ')
    n = int(n)
    return check_fermat(a, b, c, n)


prompt_fermat()
