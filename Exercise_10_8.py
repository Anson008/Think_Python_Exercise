import random


def gen_birthday():
    i = 1
    t = []
    while i <= 23:
        birthday = random.randint(1, 366)
        t.append(birthday)
        i += 1
    return t


def has_duplicates(t):
    for x in t:
        mun_of_x = t.count(x)
        if mun_of_x > 1:
            return True
    return False


total = 2000
i = 0
count = 0
t = []
while i <= total:
    t = gen_birthday()
    if has_duplicates(t):
        count += 1
    i += 1
prob_same_birthday = count / total
print("The probability of having the same birthday: {:.2%}".format(prob_same_birthday))
