import unittest
# import the code you want to test here

from palindromeQ import is_palindrome

class TestPalindrome(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testTrue(self) -> None:
        self.assertTrue(is_palindrome(''))

    def test1Char(self) -> None:
        self.assertTrue(is_palindrome('I'))

    def testIgnore(self) -> None:
        self.assertTrue(is_palindrome('I. '))

    def test2CharsPal(self) -> None:
        self.assertTrue(is_palindrome('aa'))

    def test2CharsPalCase(self) -> None:
        self.assertTrue(is_palindrome('Ii'))

    def test2CharsNonPal(self) -> None:
        self.assertFalse(is_palindrome('me'))

    def testEye(self) -> None:
        self.assertTrue(is_palindrome('eye'))

    def testABBA(self) -> None:
        self.assertTrue(is_palindrome('ABBA'))

    def testABB(self) -> None:
        self.assertFalse(is_palindrome('ABB'))

    def testHannah(self) -> None:
        self.assertTrue(is_palindrome('Hannah'))

    def testNathan(self) -> None:
        self.assertFalse(is_palindrome('Nathan'))

    def testMadam(self) -> None:
        self.assertTrue(is_palindrome("Madam, I'm Adam."))

    def testPanama(self) -> None:
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama!'))

if __name__ == '__main__':
    unittest.main()

