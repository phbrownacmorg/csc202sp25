import unittest
# import the code you want to test here
from Fraction import Fraction

class TestFraction(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testStr_1_2(self) -> None:
        self.assertEqual(str(Fraction(1, 2)), '1/2')

    def testStr_8_16(self) -> None:
        self.assertEqual(str(Fraction(8, 16)), '1/2')

    def testStr_m8_m16(self) -> None:
        self.assertEqual(str(Fraction(-8, -16)), '1/2')

    def testStr_8_m16(self) -> None:
        self.assertEqual(str(Fraction(8, -16)), '-1/2')

    def testStr_162_243(self) -> None:
        self.assertEqual(str(Fraction(162, 243)), '2/3')

    def testStr_81_243(self) -> None:
        self.assertEqual(str(Fraction(81, 243)), '1/3')

    def testStr_0_2(self) -> None:
        self.assertEqual(str(Fraction(0, 2)), '0/1')

    # Test getter methods
    def test_getNum_1_2(self) -> None:
        self.assertEqual((Fraction(1, 2)).getNum(), 1)

    def test_getNum_162_243(self) -> None:
        self.assertEqual((Fraction(162, 243)).getNum(), 2)

    def test_getNum_0(self) -> None:
        self.assertEqual((Fraction(0, 2)).getNum(), 0)

    def test_getNum_m1_2(self) -> None:
        self.assertEqual((Fraction(-1, 2)).getNum(), -1)

    def test_getDenom_1_2(self) -> None:
        self.assertEqual((Fraction(1, 2)).getDenom(), 2)

    def test_getDenom_162_243(self) -> None:
        self.assertEqual((Fraction(162, 243)).getDenom(), 3)

    def test_getDenom_0(self) -> None:
        self.assertEqual((Fraction(0, 2)).getDenom(), 1)

    def test_getDenom_m1_2(self) -> None:
        self.assertEqual((Fraction(-1, 2)).getDenom(), 2)

    # __eq__

    def test_eq_1_2_1_2(self) -> None:
        self.assertTrue(Fraction(1,2) == Fraction(1,2))

    def test_eq_1_2_3_2(self) -> None:
        self.assertFalse(Fraction(1,2) == Fraction(3,2))

    def test_eq_1_2_1_3(self) -> None:
        self.assertFalse(Fraction(1,2) == Fraction(1,3))

    def test_eq_1_2_m1_2(self) -> None:
        self.assertFalse(Fraction(1,2) == Fraction(-1,2))

    # __add__

    def test_add_1_2_1_2(self) -> None:
        self.assertEqual(Fraction(1,2) + Fraction(1,2), Fraction(1,1))

    def test_add_1_2_1_3(self) -> None:
        self.assertEqual(Fraction(1,2) + Fraction(1,3), Fraction(5,6))

    def test_add_1_2_2_3(self) -> None:
        self.assertEqual(Fraction(1,2) + Fraction(2,3), Fraction(7,6))

    def test_add_2_5_2_3(self) -> None:
        self.assertEqual(Fraction(2,5) + Fraction(2,3), Fraction(16,15))

    def test_add_1_6_2_9(self) -> None:
        self.assertEqual(Fraction(1,6) + Fraction(2,9), Fraction(7,18))

    def test_add_5_6_m5_9(self) -> None:
        self.assertEqual(Fraction(5,6) + Fraction(-5,9), Fraction(5,18))

    # __float__
    def test_float_1_2(self) -> None:
        self.assertAlmostEqual(float(Fraction(1,2)), 0.5)

    def test_float_1_3(self) -> None:
        self.assertAlmostEqual(float(Fraction(1,3)), 0.333333333333333)

    def test_float_2_5(self) -> None:
        self.assertAlmostEqual(float(Fraction(2,5)), 0.4)

    def test_float_0_3(self) -> None:
        self.assertAlmostEqual(float(Fraction(0,3)), 0)

    def test_float_16_15(self) -> None:
        self.assertAlmostEqual(float(Fraction(16,15)), 1.0666666666666667)

    def test_float_m5_4(self) -> None:
        self.assertAlmostEqual(float(Fraction(-5,4)), -1.25)


if __name__ == '__main__':
    unittest.main()

