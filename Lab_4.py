import datetime as dt


def plus_days(x: int):
    date = dt.datetime(2022, 9, 5)
    days = []
    for i in range(20):
        date += dt.timedelta(days=x)
        days.append(date)
    print(counter_dictionary(days))
    # for i in days:
    #     print(i)
    return days


def counter_dictionary(array: []):
    dictionary = {str(index): i for index in range(len(array)) for i in array}
    return dictionary


print(plus_days(5))
