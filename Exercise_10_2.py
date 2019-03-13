def cumsum(t):
    """ Take a list of numbers and returns the cumulative sum; that is, a new list
        where the ith element is the sum of the first i+1 elements from the original list.
    """
    x = []
    for i in range(len(t)):
        x.append(sum(t[:i+1]))
    return x


t = [1, 2, 3]
print(cumsum(t))
