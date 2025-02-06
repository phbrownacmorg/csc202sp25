import unittest
# import the code you want to test here
import valid_date

class TestNothing(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def test_2_4_2025(self) -> None:
        self.assertTrue(valid_date.isValidDate('2/4/2025'))

    def test_few_slashes(self) -> None:
        self.assertFalse(valid_date.isValidDate('2/2025'))

    def test_many_slashes(self) -> None:
        self.assertFalse(valid_date.isValidDate('2/4//2025'))

    def test_empty_day(self) -> None:
        self.assertFalse(valid_date.isValidDate('2//2025'))

    def test_month_too_small(self) -> None:
        self.assertFalse(valid_date.isValidDate('0/4/2025'))

    def test_month_too_big(self) -> None:
        self.assertFalse(valid_date.isValidDate('13/4/2025'))

    def test_min_month(self) -> None:
        self.assertTrue(valid_date.isValidDate('1/4/2025'))

    def test_max_month(self) -> None:
        self.assertTrue(valid_date.isValidDate('12/4/2025'))

    def test_day_too_small(self) -> None:
        self.assertFalse(valid_date.isValidDate('2/0/2025'))

    def test_min_day(self) -> None:
        self.assertTrue(valid_date.isValidDate('2/1/2025'))

    def test_day_too_big(self) -> None:
        self.assertFalse(valid_date.isValidDate('3/32/2025'))

    def test_max_day(self) -> None:
        self.assertTrue(valid_date.isValidDate('3/31/2025'))

    def test_day_too_big_30day(self) -> None:
        self.assertFalse(valid_date.isValidDate('4/31/2025'))

    def test_max_day_30day(self) -> None:
        self.assertTrue(valid_date.isValidDate('4/30/2025'))

    def test_day_too_big_Feb_nonleap(self) -> None:
        self.assertFalse(valid_date.isValidDate('2/29/2025'))

    def test_max_day_Feb_nonleap(self) -> None:
        self.assertTrue(valid_date.isValidDate('2/28/2025'))

    def test_day_too_big_Feb_leap(self) -> None:
        self.assertFalse(valid_date.isValidDate('2/30/2024'))

    def test_max_day_Feb_leap(self) -> None:
        self.assertTrue(valid_date.isValidDate('2/29/2024'))

    def test_year_too_small(self) -> None:
        self.assertFalse(valid_date.isValidDate('2/4/1582'))

    def test_min_year(self) -> None:
        self.assertTrue(valid_date.isValidDate('2/4/1583'))

    def test_parse_date(self) -> None:
        self.assertEqual(valid_date.parseDate('2/4/2025'), (2, 4, 2025))

    def test_parse_date_invalid(self) -> None:
        self.assertEqual(valid_date.parseDate('-2/0/-2025'), (-2, 0, -2025))

    def test_parse_date_few_slashes(self) -> None:
        with self.assertRaises(AssertionError):
            valid_date.parseDate('2/2025')

    def test_parse_date_many_slashes(self) -> None:
        with self.assertRaises(AssertionError):
            valid_date.parseDate('2/4/0/2025')

    def test_parse_date_empty_month(self) -> None:
        with self.assertRaises(ValueError):
            valid_date.parseDate('/0/2025')

    def test_parse_date_empty_day(self) -> None:
        with self.assertRaises(ValueError):
            valid_date.parseDate('2//2025')

    def test_parse_date_empty_year(self) -> None:
        with self.assertRaises(ValueError):
            valid_date.parseDate('2/4/')

    def test_parse_date_nonint_month(self) -> None:
        with self.assertRaises(ValueError):
            valid_date.parseDate('Feb/4/2025')

    def test_parse_date_nonint_day(self) -> None:
        with self.assertRaises(ValueError):
            valid_date.parseDate('2/4.3/2025')

    def test_parse_date_nonint_year(self) -> None:
        with self.assertRaises(ValueError):
            valid_date.parseDate('2/4/2025.0')



if __name__ == '__main__':
    unittest.main()

