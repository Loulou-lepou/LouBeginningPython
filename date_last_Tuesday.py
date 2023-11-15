"""
get the date of the last Tuesday
"""
from datetime import date, timedelta


def new_date(old_day, old_month, old_year, day_diff):
    """
    return a new date day_diff days before/ after the old day
    day_diff <= 7
    """
    if 0 <= day_diff:
        end_month_day = days_in_month(old_month, old_year)
        if old_day + day_diff < end_month_day:
            # same month, same year
            return date(old_year, old_month, old_day + day_diff)
        else:
            # new month
            new_month, new_year = next_month(old_month, old_year)
            new_day = day_diff + end_month_day - old_day
            return date(new_year, new_month, new_day)
    else:     # 0 < day_diff
        if 1 <= old_day + day_diff:
            # same month, same year
            return date(old_year, old_month, old_day + day_diff)
        else:
            # last month
            month_before, year_ = last_month(old_month, old_year)
            end_month_before = days_in_month(month_before, year_)
            return date(year_, month_before, end_month_before + old_day + day_diff)


def next_month(input_month, input_year):
    """ return the next month """
    if input_month < 12:
        return input_month, input_year
    else:
        return 1, input_year + 1


def last_week(input_day, input_month, input_year):
    """ return the same weekday, last week """

    if 7 < input_day:
        return date(input_year, input_month, input_day - 7)
    else:
        last_week_month = last_month(input_month, input_year)
        return date(last_week_month[1],
                    last_week_month[0],
                    days_in_month(*last_week_month) - 7 + input_day)


def last_month(input_month, input_year):
    """ return the last month of a given month """
    if 1 < input_month:
        return input_month - 1, input_year
    else:
        return 12, input_year - 1


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
    """ return the maximum number of days in the given month, in a given year. """
    max_day = 31
    if input_month in {4, 6, 9, 11}:
        max_day = 30
    elif input_month == 2:
        max_day = 29 if is_leap_year(input_year) else 28
    return max_day


def last_tuesday(given_date):
    """ return the last tuesday of a given date """
    given_month, given_year, given_day = given_date.month, given_date.year, given_date.day

    # [mon, tue, wed, thu, fri, sat, sun] => .weekday() => [0, 1, 2, 3, 4, 5, 6]
    given_date_no, tue_date_no = given_date.weekday(), 1
    day_diff = given_date_no - tue_date_no    # day_diff in [-1, 5]
    if 0 < day_diff:
        tue_same_week = new_date(given_day, given_month, given_year, -day_diff)
        return tue_same_week
    elif day_diff == 0:
        return given_date
    else:
        # back 6 days
        return new_date(given_day, given_month, given_year, -6)


def last_tuesday_2(given_date):
    """
    A simpler method to get the date of the last tuesday
    source: https://www.tutorjoes.in/Python_example_programs/get_date_of_the_last_tuesday_in_python
    """

    offset = (given_date.weekday() - 1) % 7
    return given_date - timedelta(days=offset)


# --- create testcases to test the results -------------

# Generate a range of dates
start_date = date(2011, 1, 1)
end_date = date(2023, 12, 31)
delta = timedelta(days=1)
test_dates = []

while start_date <= end_date:
    test_dates.append(start_date)
    start_date += delta
# Test each date
for date_ in test_dates:
    last_tue = last_tuesday(date_)
    expected_tue = date_
    while expected_tue.weekday() != 1:  # Find the last Tuesday
        expected_tue -= timedelta(days=1)

    if last_tue != expected_tue:
        print(f"Failed: {date_} - Expected: {expected_tue}, Got: {last_tue}")
