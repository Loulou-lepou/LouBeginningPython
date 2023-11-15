"""
validate a gregorian date
"""
from datetime import date


def valid_format(input_date):
    """
    input_date = input_date_str.strip()
    valid format: yyyy-mm-dd
    where yyyy, mm, dd are integers
          1 <= yyyy <= 32767, 1 <= mm <= 12,  1<= dd <= 31
    """
    if input_date[4] == "-" and input_date[7] == "-":
        try:
            year_, month_, day_ = list(map(int, input_date.split("-")))
            if 1 <= month_ <= 12 and 1 <= day_ <= 31 and 1 <= year_ <= 32767:
                return year_, month_, day_
        except ValueError:
            return False
    else:
        return False


def is_leap_year(input_year):
    """ check whether the given year is a leap year """
    if input_year % 4 == 0:
        if input_year % 100 == 0 and input_year % 400 == 0:
            return False
        else:
            return True
    else:
        return False


def days_in_month(input_month, input_year):
    """ return the maxinum number of days in the given input_month, input_year"""
    max_day = 31
    if input_month in {4, 6, 9, 11}:
        max_day = 30
    elif input_month == 2:
        max_day = 29 if is_leap_year(input_year) else 28
    return max_day


if __name__ == '__main__':
    """
    validate Gregorian date
    """
    while True:
        input_date_str = input("Enter a valid Gregorian date in the form 'yyyy-mm-dd':\n")
        if valid_format(input_date_str):
            given_year, given_month, given_day = valid_format(input_date_str)
            # if given_day <= days_in_month(given_month, given_year):
            #     print("Valid input")
            #     print(date(given_year, given_month, given_day))
            #     break
            # else:
            #     print("Invalid input.")
            try:
                valid_date = date(given_year, given_month, given_day)
                print("Valid input:", valid_date)
                break
            except ValueError:
                print("Invalid input.")
        else:
            print("Invalid input.")
