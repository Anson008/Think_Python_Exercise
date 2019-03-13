import math


def eval_loop():
    """ Iteratively prompts the user, takes the resulting input and evaluates it using eval, and prints the result.
        It should continue until the user enters 'done', and then return the value of the last expression it evaluated.
    """
    while True:
        s = str(input("Enter a string:\n"))
        if s == "done":
            print("Done!")
            print("Last result:", res)
            break
        else:
            res = eval(s)
            print("Result:", res)


eval_loop()
