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

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))