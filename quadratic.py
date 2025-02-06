import math
# Global constant
EPSILON: float = 0.0000001

def read_quadratic() -> tuple[float, float, float]:
    """Read the coefficients for a quadratic in the form
    a*x**2 + b*x + c = 0, and return them as a tuple."""
    print('Please enter coefficients for a system a*x**2 + b*x + c = 0.')
    a: float = float(input("Please enter a value for a: "))
    b: float = float(input("Please enter a value for b: "))
    c: float = float(input("Please enter a value for c: "))
    return a, b, c

def find_roots(a: float, b: float, c: float) -> tuple[float, float]:
    """Find the roots of a quadratic A*x**2 + B*x + C = 0, and return them
    as a tuple.  If there are no real roots, this function raises an 
    AssertionError with the message 'There are no real roots.'."""
    # Precondition:
    # a, b, and c have to be numbers

    determinant: float = b**2 - 4*a*c
    # Executable assertion
    assert determinant >= 0, "There are no real roots."
    #print(determinant) # for testing
    root1 = (-b + math.sqrt(determinant)) / (2*a)
    root2 = (-b - math.sqrt(determinant)) / (2*a)
    # Postcondition:
    # The roots should solve the system
    # Allow for floating-point imprecision (like using assertAlmostEqual)
    assert abs(a*root1**2 + b*root1 + c) < EPSILON and \
        abs(a*root2**2 + b*root2 + c) < EPSILON, "Failed postcondition"
    return root1, root2

def main(args: list[str]) -> int:
    # Characterize the function as a*x**2 + b*x + c = 0
    # Ask the user for a, b, and c
    try:
        a, b, c = read_quadratic()
    except ValueError:
        print("Values supplied for a, b, and c must all be numbers.")
    else:
        print("System is", a, '*x**2 +', b, '*x +', c, '= 0')

        try:
            # find the root(s)
            root1, root2 = find_roots(a, b, c)
            print('The roots are', root1, 'and', root2)                
        except AssertionError as e:
            print(e)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))