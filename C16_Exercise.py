class Time:
    """ Represents time of the day.

        Attributes: hour, minute, second
    """


def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def print_time(time):
    print("{:02d}:{:02d}:{:02d}".format(time.hour, time.minute, time.second))


def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.second) < (t2.hour, t2.minute, t2.second)


def increment(time, seconds):
    assert valid_time(time)
    time.second += seconds

    if time.second > 60:
        time.minute += time.second // 60
        time.second = time.second % 60

    if time.minute > 60:
        time.hour += time.minute // 60
        time.minute = time.minute % 60


def increment_2(time, seconds):
    """ A pure version of "increment" that creates and returns an new object."""
    assert valid_time(time)
    t2 = Time()
    t2.second = time.second + seconds
    t2.minute = time.minute
    t2.hour = time.hour

    if t2.second > 60:
        t2.minute += t2.second // 60
        t2.second = t2.second % 60

    if t2.minute > 60:
        t2.hour += t2.minute // 60
        t2.minute = t2.minute % 60

    return t2


def time_to_int(time):
    assert valid_time(time)
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def increment_3(time, seconds):
    assert valid_time(time)
    seconds += time_to_int(time)
    return int_to_time(seconds)


t1 = Time()
t1.hour = 14
t1.minute = 35
t1.second = 54

t2 = Time()
t2.hour = 14
t2.minute = 25
t2.second = 36

print_time(t1)
print(is_after(t1, t2))

increment(t1, 68)
print("{:02d}:{:02d}:{:02d}".format(t1.hour, t1.minute, t1.second))

t3 = increment_2(t1, 68)
print("{:02d}:{:02d}:{:02d}".format(t3.hour, t3.minute, t3.second))

t4 = increment_3(t2, 68)
print("{:02d}:{:02d}:{:02d}".format(t4.hour, t4.minute, t4.second))
