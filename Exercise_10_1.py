def nested_sum(t):
    """ Take a list of lists of integers and adds up the elements from all of the nested lists.
    """
    total = 0
    for x in t:
        total = total + sum(x)
    return total


t = [[1, 2], [3, 4], [5, 6]]
print(nested_sum(t))
