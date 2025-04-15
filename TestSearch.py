import unittest
# import the code you want to test here
from search import contains, index

class TestSearch(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test

    def setUp(self) -> None:
        self._empty = []
        self._one = ['a']
        self._odd = ['a', 'c', 'e', 'g', 'i']
        self._even = ['a', 'c', 'e', 'g', 'i', 'k']

    def testContainsFalse(self) -> None:
        self.assertFalse(contains('a', self._empty))

    def testContainsTrue(self) -> None:
        self.assertTrue(contains('a', self._one))

    def testContainsStart(self) -> None:
        self.assertTrue(contains('a', self._even))

    def testContainsEnd(self) -> None:
        self.assertTrue(contains('k', self._even))

    def testContainsMiddle(self) -> None:
        self.assertTrue(contains('e', self._even))

    def testContainsAbsentNonEmptySeq(self) -> None:
        self.assertFalse(contains('x', self._even))

    def testIndexAbsent(self) -> None:
        with self.assertRaises(ValueError):
            index('a', self._empty)

    def testIndexAbsentNonEmptySeq(self) -> None:
        with self.assertRaises(ValueError):
            index('a', self._empty)

    def testIndexPresentOne(self) -> None:
        self.assertEqual(index('a', self._one), 0)

    def testIndexPresentStart(self) -> None:
        self.assertEqual(index('a', self._even), 0)

    def testIndexPresentEnd(self) -> None:
        self.assertEqual(index('k', self._even), 5)

    def testIndexPresentMiddle(self) -> None:
        self.assertEqual(index('g', self._even), 3)

if __name__ == '__main__':
    unittest.main()

