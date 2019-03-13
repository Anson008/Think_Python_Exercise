def is_anagram(word1, word2):
    """Take two strings and returns True if they are anagrams.
    """
    t1 = list(word1)
    t2 = list(word2)
    t1.sort()
    t2.sort()
    if t1 == t2:
        return True
    else:
        return False


word1 = "triangle"
word2 = "integral"
print(is_anagram(word1, word2))
