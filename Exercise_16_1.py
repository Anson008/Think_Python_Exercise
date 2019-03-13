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


def mul_time(time, factor):
    assert valid_time(time)
    seconds = time_to_int(time) * factor
    return int_to_time(seconds)


def avg_pace(time, rounds):
    assert valid_time(time)
    factor = 1 / rounds
    return mul_time(time, factor)


t1 = Time()
t1.hour = 1
t1.minute = 12
t1.second = 20

t2 = mul_time(t1, 2)
print("{:d}h {:d}m {:d}s".format(t2.hour, t2.minute, t2.second))

pace = avg_pace(t1, 3)
print("Average pace: {:d}h {:d}m {:.2f}s".format(int(pace.hour), int(pace.minute), pace.second))

