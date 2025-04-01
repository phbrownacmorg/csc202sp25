# Program to demonstrate timing code

import timeit

def euler_sum(n: int) -> int:
    """Calculate the sum of the numbers up through the positive integer n.  
    Time should go as O(1)."""
    # Pre:
    assert n > 0, "Failed precondition"
    return n * (n+1) // 2

def sumTo(n: int) -> int:
    """Calculate the sum of the numbers up through the positive integer n.  
    Time should go as O(n)."""
    # Pre:
    assert n > 0, "Failed precondition"
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

def factorial(n: int) -> int:
    """Calculate the factorial of N.  Time should go as O(n)."""
    # Pre:
    assert n > 0, "Failed precondition"
    fact: int = 1
    for i in range(1, n+1): # O(n)
        fact = fact * i
    return fact

def add_trial(results: list[tuple[str, float, float]], stmt: str, time: float) -> list[tuple[str, float, float]]:
    """Add a trial (a tuple of a command, the time it took to run, and the ratio of that time to
    the one before) to a list of trials."""
    ratio: float = 0
    if len(results) > 0:
        ratio = time / results[-1][1]
    results.append((stmt, time, ratio))
    return results

def run_test(cases: list[int]) -> list[tuple[str, float, float]]:
    euler_result: list[tuple[str, float, float]] = []
    loop_result: list[tuple[str, float, float]] = []
    math_result: list[tuple[str, float, float]] = []
    for i in range(len(cases)):
        n: int = cases[i]

        stmt = "euler_sum({0})".format(n)
        time: float = timeit.timeit(stmt=stmt, number=1000, globals=globals())
        euler_result = add_trial(euler_result, stmt, time)

        #stmt = "factorial({0})".format(n)
        stmt = "sumTo({0})".format(n)
        time = timeit.timeit(stmt=stmt, number=1000, globals=globals())
        loop_result = add_trial(loop_result, stmt, time)

        # #stmt = 'math.factorial({0})'.format(n)
        stmt='math.fsum(range({0}+1))'.format(n)
        time = timeit.timeit(stmt=stmt, setup="import math", number=1000, globals=globals())
        math_result = add_trial(math_result, stmt, time)
    return euler_result + loop_result + math_result

def main(args: list[str]) -> int:
    cases: list[int] = [1, 10, 100, 1000, 10000, 100000]
    results: list[tuple[str, float, float]] = run_test(cases)
    for result in results:
        print(result)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))