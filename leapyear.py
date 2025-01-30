# Program to take a year from the user and print out whether
# the year is a leap year.

from datetime import datetime

def is_leap_year(year: int) -> bool:
    """Returns a Boolean indicating whether the given YEAR is a leap year,
    using the rules for the Gregorian calendar."""
    # Precondition: year is late enough that the Gregorian calendar
    #   actually existed
    assert year > 1582, "Year is pre-Gregorian"
    # Gregorian leap-year rules:
    #   - If a year is evenly divisible by 400, it's a leap year.
    #   - If it's evenly divisible by 100 but not by 400, it's not a leap year.
    #   - If it's evenly divisible by 4 but not by 100, it's a leap year.
    #   - If it's not evenly divisible by 4, it's not a leap year.
    leap: bool = False # True basically 3/4 of the time
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 100 == 0 and year % 400 != 0:
        leap = False
    elif year % 400 == 0:
        leap = True
    # Postcondition:
    # return value is True iff year is a leap year in the Gregorian
    #   calendar
    return leap

def past_present_future(year: int, positive: bool) -> str:
    """Returns the proper form of the verb "to be" for the given YEAR, couched
    positively or negatively according to the value of POSITIVE.  That is,
    for a year in the past, couched positively, it returns 'was'; for the
    current year, couched positively, it returns 'is'; and for a year in the
    future, couched positively, it returns 'will be'.  Couched in the negative,
    the function returns 'was NOT', 'is NOT', and 'will NOT be' for past, 
    current, and future years respectively."""
    now: datetime = datetime.now()
    result = ''
    if year < now.year and positive: # Year is in the past
        result = 'was'
    elif year < now.year: # and not positive
        result = 'was NOT'
    elif year > now.year and positive: # Year is in the future
        result = 'will be'
    elif year > now.year: # and not positive
        result = 'will NOT be'
    elif positive: # and year == now.year
        result = 'is'
    else: # year == now.year and not positive
        result = 'is NOT'
    return result

def main(args: list[str]) -> int:
    year: int = int(input('Please enter a Gregorian year (i.e., year > 1581): '))
    print('The year', year, past_present_future(year, is_leap_year(year)), 
          'a leap year.')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))