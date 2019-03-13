def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    return is_palindrome(middle(word))


def mystery_number(num):
    num = str(num)
    if is_palindrome(num):
        return True


i = 100000
j = 0
count = 0
while i <= 999999:
    j = i
    last_four = str(j)[2:]
    if mystery_number(last_four):
        j += 1
        last_five = str(j)[1:]
        if mystery_number(last_five):
            j += 1
            middle_four = str(j)[1:5]
            if mystery_number(middle_four):
                j += 1
                if mystery_number(str(j)):
                    print(i)
                    count += 1
    i += 1
print("Total:", count)
