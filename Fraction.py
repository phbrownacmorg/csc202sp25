def gcd(a: int, b: int) -> int:
    """Returns the greatest common divisor of A and B.
    The return value is never negative, even if A 
    and/or B is negative."""
    # Pre: none
    m, n = a, b
    while m % n != 0:
        m, n = n, m % n
    # Post:
    assert a % abs(n) == 0 and b % abs(n) == 0
    # and there is no greater n for which this is true
    return abs(n)

class Fraction:
    """Class to represent a fraction (rational number).
    Fractions are immutable once created, and are always
    in lowest terms."""

    def _invariant(self) -> bool:
        """Class invariant."""
        # Pre: none
        # Post: return True iff self is a legitimate Fraction
        return self._denom > 0 and gcd(self._num, self._denom) == 1

    def __init__(self, num: int, denom: int) -> None:
        """Make a Fraction from a numerator and a denominator."""
        # Pre:
        assert denom != 0, "Denominator cannot be zero"
        # Make the denominator positive
        if denom < 0:
            denom = -denom
            num = -num
        # Next, reduce to lowest terms
        factor: int = gcd(num, denom)
        if factor > 1:
            num = num // factor
            denom = denom // factor
        # Assign the attributes
        self._num = num
        self._denom = denom
        # Post: the class invariant is true
        assert self._invariant()

    # Query methods

    def __str__(self) -> str:
        """Returns a string representation of a Fraction."""
        # Pre:
        assert self._invariant()
        # Post: return value is the numerator, "/", and the denominator
        return str(self._num) + '/' + str(self._denom)
        
    
    def getNum(self) -> int:
        """Returns the numerator of the Fraction."""
        # Pre:
        assert self._invariant()
        # Post: return value is the numerator
        return self._num
    
    def getDenom(self) -> int:
        """Returns the denominator of the Fraction."""
        # Pre:
        assert self._invariant()
        # Post: return value is the denominator
        return self._denom
    
    def __eq__(self, other: object) -> bool:
        """Compares self to OTHER and returns True iff they're both equal."""
        # Pre:
        assert self._invariant() # No precondition for other
        equal: bool = True
        if (not hasattr(other, 'getNum')) or (not hasattr(other, 'getDenom')):
            equal = False
        elif (self._num != other.getNum()) or (self._denom != other.getDenom()):
            equal = False
        return equal
    
    def __add__(self, other: object) -> 'Fraction':
        """Adds two fractions together and returns a new Fraction with the sum."""
        # Pre:
        assert self._invariant() and \
            hasattr(other, 'getNum') and hasattr(other, 'getDenom') \
            and other.getDenom != 0, 'Failed precondition'
        denom: int = self._denom * other.getDenom()
        num = self._num * other.getDenom() + other.getNum() * self._denom
        # Post: returned Fraction == self + other
        return Fraction(num, denom)

    def __float__(self) -> float:
        """Convert a Fraction to a floating-point number."""
        # Pre:
        assert self._invariant()
        # Post: return value is the float equivalent of this Fraction
        return self._num / self._denom