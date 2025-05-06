import unittest
# import the code you want to test here
from MaxHeap import MaxHeap

class TestMaxHeap(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def setUp(self) -> None:
        self._empty = MaxHeap[int]()

        self._one = MaxHeap[str]()
        self._one.insert(40, 'forty')

        self._two = MaxHeap[str]()
        self._two.insert(40, 'forty')
        self._two.insert(11, 'eleven')

        self._two2 = MaxHeap[str]()
        self._two2.insert(11, 'eleven')
        self._two2.insert(40, 'forty')

        self._seven = MaxHeap[str]()
        self._seven.insert(11, 'eleven')
        self._seven.insert(9, 'nine')
        self._seven.insert(7, 'seven')
        self._seven.insert(100, 'one hundred')
        self._seven.insert(10, 'ten')
        self._seven.insert(8, 'eight')
        self._seven.insert(40, 'forty')

    def testEmptyTrue(self) -> None:
        self.assertTrue(self._empty.empty())

    def testLenEmpty(self) -> None:
        self.assertEqual(len(self._empty), 0)

    def testInsertFirst(self) -> None:
        self.assertEqual(len(self._one), 1)

    def testInsertTwoItemsNoSwap(self) -> None:
        self.assertEqual(len(self._two), 2)
        self.assertEqual(self._two._items[0], (40, 'forty'))
        self.assertEqual(self._two._items[1], (11, 'eleven'))

    def testInsertTwoItemsSwap(self) -> None:
        self.assertEqual(len(self._two2), 2)
        self.assertEqual(self._two2._items[0], (40, 'forty'))
        self.assertEqual(self._two2._items[1], (11, 'eleven'))

    def testPeekEmpty(self) -> None:
        with self.assertRaises(AssertionError):
            self._empty.peek()

    def testPeek1(self) -> None:
        self.assertEqual(self._one.peek(), (40, 'forty'))
        self.assertEqual(len(self._one), 1)

    def testPeek2(self) -> None:
        self.assertEqual(self._two.peek(), (40, 'forty'))
        self.assertEqual(len(self._two), 2)

    def testPeek7(self) -> None:
        self.assertEqual(self._seven.peek(), (100, 'one hundred'))
        self.assertEqual(len(self._seven), 7)

    def testPopEmpty(self) -> None:
        with self.assertRaises(AssertionError):
            self._empty.pop()

    def testPopOne(self) -> None:
        self.assertEqual(self._one.pop(), 'forty')
        self.assertTrue(self._one.empty())


if __name__ == '__main__':
    unittest.main()

