import string


def read_into_words(filename):
    """ Read a file, breaks each line into words, strips whitespace and punctuation from the words,
        and converts them to lowercase.
    """
    fin = open(filename)
    for line in fin:
        line = line.replace("-", " ")
        for word in line.split():
            w = word.strip(string.punctuation + string.whitespace).lower()
            print(w)


read_into_words('emma.txt')
