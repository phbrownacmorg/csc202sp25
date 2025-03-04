import unittest
# import the code you want to test here
from LList import LList

class TestLList(unittest.TestCase):

    def setUp(self) -> None:
        self._empty: LList[int] = LList[int]()
    
        self._1item: LList[str] = LList[str]() # Empty list
        self._1item.add('foo')

        self._2items: LList[str] = LList[str]() # Empty list
        self._2items.add('foo')
        self._2items.add('bar')

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testEmpty(self) -> None:
        self.assertTrue(self._empty.empty())

    def testEmptyFalse(self) -> None:
        self.assertFalse(self._1item.empty())

    def testStrEmpty(self) -> None:
        self.assertEqual(str(self._empty), '∅')

    def testStr1Node(self) -> None:
        self.assertEqual(str(self._1item), '❬foo❭➞∅')

    def testStr2Nodes(self) -> None:
        self.assertEqual(str(self._2items), '❬bar❭➞❬foo❭➞∅')

    def testLenEmpty(self) -> None:
        self.assertEqual(len(self._empty), 0)

    def testLen1(self) -> None:
        self.assertEqual(len(self._1item), 1)

    def testLen2(self) -> None:
        self.assertEqual(len(self._2items), 2)

    def testContainsEmpty(self) -> None:
        self.assertFalse(500 in self._empty)

    def testContains1(self) -> None:
        self.assertTrue('foo' in self._1item)
        self.assertFalse('bar' in self._1item)

    def testContains2(self) -> None:
        self.assertTrue('foo' in self._2items)
        self.assertTrue('bar' in self._2items)
        self.assertFalse('baz' in self._2items)

    # Need tests for pop

if __name__ == '__main__':
    unittest.main()

