# Program to do nothing, correctly.

from leapyear import is_leap_year

def parseDate(instring: str) -> tuple[int, int, int]:
    """Takes a string INSTRING, split it into month, day, and year,
    and return those three as integers."""
    # Precondition: instring is a string
    parts: list[str] = instring.split('/')
    # Executable assertion
    assert len(parts) == 3, 'Wrong number of parts'
    month: int = int(parts[0])
    day: int = int(parts[1])
    year: int = int(parts[2])
    # Postcondition: month, day, and year are all integers
    return month, day, year

def isValidDate(instring: str) -> bool:
    """Takes a string INSTRING and determines whether it is a valid date
    in m/d/yyyy format."""
    # Precondition: instring is a string
    valid: bool = True
    try:
        month, day, year = parseDate(instring)
    except (AssertionError, ValueError):
        valid = False
    else:
        if (month < 1 or month > 12): # Valid month
            valid = False
        elif (year <= 1582): # Valid year
            valid = False
        elif (day < 1 or day > 31): # Valid day (any month)
            valid = False
        # 30-day months
        elif month in [9, 4, 6, 11] and day > 30:
            valid = False
        # February
        elif month == 2 and day > 29:
            valid = False
        elif month == 2 and day > 28 and not is_leap_year(year):
            valid = False

    # Postcondition: (making this executable would involve repeating the function)
    # valid == true iff instring is a valid Gregorian date
    return valid

def main(args: list[str]) -> int:
    """Reads a date in m/d/yyyy format and determine whether
    it is a valid date."""
    # Precondition: none
    datestring: str = input('Please enter a date in m/d/yyyy format: ')
    print(f"'{datestring}' is", end=' ')

    if not isValidDate(datestring):
        print('NOT', end=' ')
    print('a valid date.')

    # Postcondition:
    # (side effect): printed the correct message indicating
    #                whether the string the user entered was a
    #                valid Gregorian date AND
    # return value == 0 (indicating successful completion)
    return 0 # Conventional return value for completing successfully

if __name__ == '__main__':
    import sys
    main(sys.argv)