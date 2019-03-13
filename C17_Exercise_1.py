def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


class Time:
    """ Represents time of the day.

        Attributes: hour, minute, second
    """
    def time_to_int(time):
        assert valid_time(time)
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds


class Second:
    """ Represents time in the unit of second.
    """
    def int_to_time(second):
        time = Time()
        minutes, time.second = divmod(second.seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time


time = Time()
time.hour = 2
time.minute = 28
time.second = 49
print(time.time_to_int())

second = Second()
second.seconds = 3611
print("{:02d}:{:02d}:{:02d}".format(second.int_to_time().hour,
                                    second.int_to_time().minute, second.int_to_time().second))