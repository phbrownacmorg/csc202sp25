import unittest
# import the code you want to test here
from match_delims import match_delims

class TestDelims(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testEmpty(self) -> None:
        self.assertTrue(match_delims(""))

    def testSimpleBalance(self) -> None:
        self.assertTrue(match_delims("([{}])"))

    def testCloseBeforeOpenParentheses(self) -> None:
        self.assertFalse(match_delims(')('))

    def testWrongCloseOrder(self) -> None:
        self.assertFalse(match_delims('({[])}'))

    def testDistractors(self) -> None:
        self.assertTrue(match_delims("( { xyzzy [ plugh ] foo } bar )"))

    def testMismatchInside(self) -> None:
        self.assertFalse(match_delims("( { xyzzy [ plugh } foo } bar )"))

if __name__ == '__main__':
    unittest.main()

