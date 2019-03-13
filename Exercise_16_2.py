import datetime


def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def print_date():
    date = datetime.date.today()
    print("Current date:", date)
    day_of_week = datetime.date.isoweekday(date)
    print("Day of the week:", day_of_week)


def input_date_of_birth():
    user_input = input("Enter your date of birth (yyyymmdd):\n")
    birthday = datetime.datetime.strptime(user_input, "%Y%m%d")
    return birthday


def age(birthday):
    today = datetime.datetime.today()
    age = (today - birthday).days // 365
    return age


def days_until_next_birthday(birthday):
    today = datetime.datetime.today()
    next_birthday = datetime.datetime(today.year, birthday.month, birthday.day)

    if today > next_birthday:
        next_birthday = datetime.datetime(today.year + 1, birthday.month, birthday.day)

    delta = next_birthday - today
    return delta


def double_day(birthday1, birthday2):
    if birthday1 > birthday2:
        diff = birthday1 - birthday2
        double = birthday1 + diff
    else:
        diff = birthday2 - birthday1
        double = birthday2 + diff
    return double


def n_times_day(birthday1, birthday2, factor):
    if birthday1 > birthday2:
        diff = birthday1 - birthday2
        f_times = birthday1 + diff / (factor - 1)
    else:
        diff = birthday2 - birthday1
        f_times = birthday2 + diff / (factor - 1)
    return f_times


birthday = input_date_of_birth()
age = age(birthday)
days_next_birth = days_until_next_birthday(birthday)
print("Your birthday is:", birthday)
print("Your age is:", age)
print("Days until your next birthday:", days_next_birth)

b1 = input_date_of_birth()
b2 = input_date_of_birth()
print(double_day(b1, b2))
print(n_times_day(b1, b2, factor=2))
