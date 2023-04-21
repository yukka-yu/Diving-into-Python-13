'''Программа определяет, является ли введённая строка датой'''

class DateException(Exception):
    pass

class YearError(DateException):
    def __init__(self, year):
        self.year = year

    def __str__(self):
        return f'Year must be integer from 1 to 9999, here you have value {self.year}'


class MonthError(DateException):
    def __init__(self, month_number):
        self.month_number = month_number

    def __str__(self):
        return f'Month number must be integer from 1 to 12, here you have value {self.month_number}'


class DayError(DateException):
    def __init__(self, day_number):
        self.day_number = day_number
    def __str__(self):
        return f'Day number must be more than 1 and cannot be more than 31, here you have value {self.day_number}'



def is_date(date):
    date_list = list(map(int, date.split(".")))
    if date_list[2] > 9999 or date_list[2] < 1:
        raise YearError(date_list[2])
    if date_list[1] > 12:
        raise MonthError(date_list[1])
    if date_list[0] > 31:
        raise DayError(date_list[0])
    elif (date_list[1] in [4, 6, 9, 11]) and date_list[0] > 30:
        return False
    elif date_list[1] == 2 and _is_leap(date_list[2]) and date_list[0] > 29:
        return False
    elif date_list[1] == 2 and not _is_leap(date_list[2]) and date_list[0] > 28:
        return False
    else:
        return True
    


def _is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


# print(is_date("29.02.2004"))

if __name__ == "__main__":

    print(is_date("32.02.2004"))