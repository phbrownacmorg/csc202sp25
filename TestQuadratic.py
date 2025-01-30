import unittest
# import the code you want to test here
import quadratic
import math

class TestQuadratic(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test

    # Simplest possible quadratic
    def test1_0_0(self) -> None:
        roots: tuple[float, float] = quadratic.find_roots(1, 0, 0)
        self.assertAlmostEqual(roots[0], 0)
        self.assertAlmostEqual(roots[1], 0)

    # Make c non-zero
    def test1_0_m2(self) -> None:
        roots: tuple[float, float] = quadratic.find_roots(1, 0, -2)
        self.assertAlmostEqual(roots[0], math.sqrt(2))
        self.assertAlmostEqual(roots[1], -math.sqrt(2))

    # Make all three non-zero
    def test1_m1_m2(self) -> None:
        roots: tuple[float, float] = quadratic.find_roots(1, -1, -2)
        self.assertAlmostEqual(roots[0], 2)
        self.assertAlmostEqual(roots[1], -1)

    # Make a > 1
    def test2_m1_m2(self) -> None:
        roots: tuple[float, float] = quadratic.find_roots(2, -1, -2)
        self.assertAlmostEqual(roots[0], 1.2807764064044151)
        self.assertAlmostEqual(roots[1], -0.7807764064044151)

    # Negative determinant
    def test2_1_2(self) -> None:
        with self.assertRaises(ValueError):
            roots: tuple[float, float] = quadratic.find_roots(2, 1, 2)

if __name__ == '__main__':
    unittest.main()

