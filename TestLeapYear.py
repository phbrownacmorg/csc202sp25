import unittest
import leapyear
# import the code you want to test here

class TestNothing(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test

    # All four possibilities for divisibility by 4
    def test2025(self) -> None:
        self.assertFalse(leapyear.is_leap_year(2025))

    def test2024(self) -> None:
        self.assertTrue(leapyear.is_leap_year(2024))

    def test2023(self) -> None:
        self.assertFalse(leapyear.is_leap_year(2023))

    def test2022(self) -> None:
        self.assertFalse(leapyear.is_leap_year(2022))

    # Divisible by 400
    def test2000(self) -> None:
        self.assertTrue(leapyear.is_leap_year(2000))

    # Three cases for divisible by 100 but not 400
    def test1900(self) -> None:
        self.assertFalse(leapyear.is_leap_year(1900))

    def test2100(self) -> None:
        self.assertFalse(leapyear.is_leap_year(2100))

    def test2200(self) -> None:
        self.assertFalse(leapyear.is_leap_year(2200))

    # Representative case of a date that's too early
    def test1100(self) -> None:
        with self.assertRaises(AssertionError):
            leapyear.is_leap_year(1100)

    # Top boundary of the dates that are too early
    def test1582(self) -> None:
        with self.assertRaises(AssertionError):
            leapyear.is_leap_year(1582)

    # Bottom bondary of the dates that are not too early
    def test1583(self) -> None:
        self.assertFalse(leapyear.is_leap_year(1583))

    # Representative case from each of the 6 possible cases of the tense
    def testTensePastYes(self) -> None:
        self.assertEqual(leapyear.past_present_future(1924, True), 'was')

    def testTensePastNo(self) -> None:
        self.assertEqual(leapyear.past_present_future(1925, False), 'was NOT')

    def testTensePresentYes(self) -> None:
        self.assertEqual(leapyear.past_present_future(2025, True), 'is')

    def testTensePresentNo(self) -> None:
        self.assertEqual(leapyear.past_present_future(2025, False), 'is NOT')

    def testTenseFutureYes(self) -> None:
        self.assertEqual(leapyear.past_present_future(2124, True), 'will be')

    def testTenseFutureNo(self) -> None:
        self.assertEqual(leapyear.past_present_future(2125, False), 'will NOT be')


if __name__ == '__main__':
    unittest.main()

