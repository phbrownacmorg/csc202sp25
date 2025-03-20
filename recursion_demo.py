from LList import LList

def make_numlist() -> LList[float]:
    result: LList[float] = LList[float]()
    for num in [5, 7, 1, 3, 3, 6, 9, 2, -6]:
        result.add(num)
    return result

def sumlist(numlist: LList[float]) -> float:
    """Sum a list of numbers, recursively."""
    total: int = 0 # Handles the base case (empty list)
    if not numlist.empty():
        total = numlist.data() + sumlist(numlist.rest())
    return total

def reverse(s: str) -> str:
    """Reverse a string, recursively."""
    result: str
    if len(s) < 2: # Base case
        result = s
    else: # Recursive case, len(s) >= 2
        result = s[-1] + reverse(s[1:-1]) + s[0]
    return result

def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of A and B, using Euclid's algorithm."""
    result: int
    if b == 0:
        result = abs(a)
    else:
        result = gcd(b, a % b)
    return result

def expt(a: float, b: int) -> float:
    """Raise A to the integer power B.   This approach is O(n) for n=b."""
    result: float
    if b == 0: # Base case
        result = 1
    elif b < 0: # Recursive case #1: b < 0
        result = 1.0 / expt(a, -b)
    else: # Recursive case: b > 0
        result = a * expt(a, b-1)
    return result

def fastexpt(a: float, b: int) -> float:
    """Raise A to the integer power B.   This approach is O(lg n) for n=b."""
    result: float
    if b == 0: # Base case
        result = 1
    elif b < 0: # Recursive case #1: b < 0
        result = 1.0 / fastexpt(a, -b)
    elif b % 2 == 0: # Recursive case #2: b > 0, b is even
        half: float = fastexpt(a, b // 2)
        result = half * half # (a ** (b // 2)) ** 2
    else:            # Recursive case #3: b > 0, b is odd
        half: float = fastexpt(a, b // 2)
        result = half * half * a # ((a ** (b // 2)) ** 2) * a
    return result

def baseconvert(a: int, b: int) -> str:
    """Express the integer A in base B, and return the result as a string."""
    digits: str = '0123456789abcdefghijklmnopqrstuvwxyz'
    # Pre:
    assert len(digits) > b > 1, \
        "Base must be at least 2 and less than the number of digits available"
    assert a >= 0, 'A must be non-negative'

    result: str = ''
    if a < b: # Base case
        result = digits[a]
    else: # a >= b
        result = baseconvert(a // b, b) + digits[a % b]
    return result

def main(args: list[str]) -> int:
    # Sum of a list
    numlist: LList[float] = make_numlist()
    print("{0} sums to {1}".format(numlist, sumlist(numlist)))

    # String reversal
    s: str = "Madam, I'm Adam."
    print('"{0}", "{1}"'.format(s, reverse(s)))
    s = 'hannah'
    print('"{0}", "{1}"'.format(s, reverse(s)))
    s = 'na\u03b8an'
    print('"{0}", "{1}"'.format(s, reverse(s)))

    # GCD
    print('gcd({0}, {1}) = {2}'.format(4, -2, gcd(4, -2)))
    print('gcd({0}, {1}) = {2}'.format(5, 10, gcd(5, 10)))
    print('gcd({0}, {1}) = {2}'.format(10, 5, gcd(10, 5)))
    print('gcd({0}, {1}) = {2}'.format(-81, 270, gcd(-81, 270)))
    print('gcd({0}, {1}) = {2}'.format(-81, -270, gcd(-81, -270)))

    # expt
    print('{0} ** {1} = {2}'.format(33.3, 0, expt(33.3, 0)))
    print('{0} ** {1} = {2}'.format(-12, 3, expt(-12, 3)))
    print('{0} ** {1} = {2}'.format(3, 4, expt(3, 4)))
    print('{0} ** {1} = {2}'.format(-2, -3, expt(-2, -3)))

    # fastexpt
    print('{0} ** {1} = {2}'.format(33.3, 0, fastexpt(33.3, 0)))
    print('{0} ** {1} = {2}'.format(-12, 3, fastexpt(-12, 3)))
    print('{0} ** {1} = {2}'.format(3, 4, fastexpt(3, 4)))
    print('{0} ** {1} = {2}'.format(-2, -3, fastexpt(-2, -3)))

    # baseconvert
    print('{0} in base {1} = {2}'.format(426, 2, baseconvert(426, 2)))
    print('{0} in base {1} = {2}'.format(426, 10, baseconvert(426, 10)))
    print('{0} in base {1} = {2}'.format(426, 16, baseconvert(426, 16)))
    print('{0} in base {1} = {2}'.format(13, 2, baseconvert(13, 2)))
    print('{0} in base {1} = {2}'.format(13, 16, baseconvert(13, 16)))
    print('{0} in base {1} = {2}'.format(4, 2, baseconvert(4, 2)))
    print('{0} in base {1} = {2}'.format(4, 10, baseconvert(4, 10)))
    print('{0} in base {1} = {2}'.format(4, 16, baseconvert(4, 16)))
    print('{0} in base {1} = {2}'.format(255, 2, baseconvert(255, 2)))
    print('{0} in base {1} = {2}'.format(255, 10, baseconvert(255, 10)))
    print('{0} in base {1} = {2}'.format(255, 16, baseconvert(255, 16)))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))