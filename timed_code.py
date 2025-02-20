# Program to demonstrate timing code

import timeit

def factorial(n: int) -> int:
    """Calculate the factorial of N.  Time should go as O(n)."""
    fact: int = 1
    for i in range(1, n+1): # O(n)
        fact = fact * i
    return fact

def run_test(cases: list[int]) -> list[tuple[str, float, float]]:
    result: list[tuple[str, float, float]] = []
    for i in range(len(cases)):
        n: int = cases[i]
        stmt = "factorial({0})".format(n)
        time: float = timeit.timeit(stmt=stmt, number=10000, globals=globals())
        ratio: float = 0
        if i > 0:
            ratio = time / result[-2][1]
        trial: tuple[str, float, float] = (stmt, time, ratio)
        result.append(trial)
        stmt = 'math.factorial({0})'.format(n)
        time = timeit.timeit(stmt=stmt, setup="import math", number=10000, globals=globals())
        ratio = 0
        if i > 0:
            ratio = time / result[-2][1]
        result.append((stmt, time, ratio))
    return result

def main(args: list[str]) -> int:
    cases: list[int] = [1, 10, 100]
    results: list[tuple[str, float, float]] = run_test(cases)
    results.sort()
    for result in results:
        print(result)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))