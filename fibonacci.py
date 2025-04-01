def fast_fib(n: int) -> tuple[int, int]:
    """Calculate the Nth and N-1st terms of the Fibonacci sequence,
        recursively.  This implementation returns a tuple (fib(N), fib(n-1)),
        so that further terms of the sequence can be calculated with just a
        single recursion.  This approach uses a single recursion, so it runs
        in O(n) time."""
    # Pre:
    assert n >= 0, 'fib({0}) is not defined'.format(n)
    
    result: tuple[int, int] = (0, 0) # Handles base case of n = 0
    if n == 1: # Base case
        result = (1, 0) # fib(1), fib(0)
    elif n > 1: # Recursive case
        previous_terms: tuple[int, int] = fast_fib(n - 1) # Sole recursion
        fib_n_minus_1: int = previous_terms[0]
        fib_n_minus_2: int = previous_terms[1]
        fib_n: int = fib_n_minus_1 + fib_n_minus_2
        result = (fib_n, fib_n_minus_1)
    return result

def fibonacci(n: int) -> int:
    """Calculate the Nth term of the Fibonacci sequence, using fast_fib."""
    return fast_fib(n)[0]

def slow_fibonacci(n: int) -> int:
    """Calculate the Nth term of the Fibonacci sequence, recursively.
        This is coded straight from the definition, but the double
        recursion makes it unusably slow except for the first few terms.
        This naive implementation runs in O(2**n) time (actually O(Φ**n)
        ≈ O(1.618**n), but that's still bad enough to be impractical.)"""
    # Pre:
    assert n >= 0, 'fib({0}) is not defined'.format(n)
    result: int = n # Handles the base case of n < 2
    if n > 1: # Recursive case
        result = slow_fibonacci(n - 1) + slow_fibonacci(n - 2)
    return result

def main(args: list[str]) -> int:
    n: int = int(input('Enter an integer n to see fib(n): '))
    print('fib({0}) = {1}'.format(n, fibonacci(n)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))