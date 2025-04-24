import unittest
from BinTree import BinTree
# import the code you want to test here

class TestBinTree(unittest.TestCase):

    def setUp(self) -> None:
        self._empty = BinTree[str]()

        self._1item = BinTree[str]('garbage')

        self._L1tree = BinTree[str]('five')
        self._L1tree._left = self._1item

        self._R1tree = BinTree[str]('five')
        self._R1tree._right = self._1item

        self._bothSidesNow = BinTree[str]('infinity')
        self._bothSidesNow._left = self._R1tree
        self._bothSidesNow._right = BinTree[str]('left')

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testEmptyTrue(self) -> None:
        self.assertTrue(self._empty.empty())

    def testEmptyFalse(self) -> None:
        self.assertFalse(self._1item.empty())

    def testContainsEmpty(self) -> None:
        self.assertFalse('garbage' in self._empty)

    def testContainsWrongData(self) -> None:
        self.assertFalse('trash' in self._1item)

    def testContainsRoot(self) -> None:
        self.assertTrue('garbage' in self._1item)

    def testContainsWrongDataL(self) -> None:
        self.assertFalse('trash' in self._L1tree)

    def testContainsLChild(self) -> None:
        self.assertTrue('garbage' in self._L1tree)

    def testContainsWrongDataR(self) -> None:
        self.assertFalse('trash' in self._R1tree)

    def testContainsLChild(self) -> None:
        self.assertTrue('garbage' in self._R1tree)

    def testLen(self) -> None:
        self.assertEqual(len(self._empty), 0)
        self.assertEqual(len(self._1item), 1)
        self.assertEqual(len(self._L1tree), 2)
        self.assertEqual(len(self._R1tree), 2)
        self.assertEqual(len(self._bothSidesNow), 4)

    def testHeight(self) -> None:
        self.assertEqual(self._empty.height(), 0)
        self.assertEqual(self._1item.height(), 1)
        self.assertEqual(self._L1tree.height(), 2)
        self.assertEqual(self._R1tree.height(), 2)
        self.assertEqual(self._bothSidesNow.height(), 3)

    def testIter(self) -> None:
        self.assertEqual(list(iter(self._empty)), [])
        self.assertEqual(list(iter(self._1item)), ['garbage'])
        self.assertEqual(list(iter(self._L1tree)), ['garbage', 'five'])
        self.assertEqual(list(iter(self._R1tree)), ['five', 'garbage'])
        self.assertEqual(list(iter(self._bothSidesNow)), ['five', 'garbage', 'infinity', 'left'])


if __name__ == '__main__':
    unittest.main()

