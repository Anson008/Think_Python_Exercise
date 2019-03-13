def find_triple_double(word):
    i = 0
    code = ""
    while i < len(word) - 1:
        if word[i+1] == word[i]:
            code = code + "1"
        else:
            code = code + "0"
        i += 1
    if "0101010" in code:
        return True
    else:
        return False


file_words = open("words.txt")
count = 0
for line in file_words:
    word = line.strip()
    if find_triple_double(word):
        print(word)
        count += 1
print("Total:", count)
