import time


def time_since_epoch():
    """ Read the current time and converts it to a time of day in hours,
        minutes, and seconds, plus the number of days since the epoch.
    """
    t = time.time()
    sec_a_day = 24 * 3600
    sec_an_hour = 3600
    sec_a_minute = 60

    days = int(t // sec_a_day)
    sec_left_day = t % sec_a_day

    hours = int(sec_left_day // sec_an_hour)
    sec_left_hour = sec_left_day % sec_an_hour

    minutes = int(sec_left_hour // sec_a_minute)
    seconds = sec_left_hour % sec_a_minute

    print(days, "days", hours, "hours", minutes, "minutes",
          "{:.2f} seconds,".format(seconds), "since the epoch.")


time_since_epoch()
