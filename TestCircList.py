import unittest
# import the code you want to test here
from CircList import CircList

class TestCircList(unittest.TestCase):

    def setUp(self) -> None:
        self._empty: CircList[int] = CircList[int]()
    
        self._1item: CircList[str] = CircList[str]() # Empty list
        self._1item.add('foo')

        self._2items: CircList[str] = CircList[str]() # Empty list
        self._2items.add('foo')
        self._2items.add('bar')

        self._3items: CircList[str] = CircList[str]() # Empty list
        self._3items.add('foo')
        self._3items.add('bar')
        self._3items.add('baz')

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

    def testStr3Nodes(self) -> None:
        self.assertEqual(str(self._3items), '❬baz❭➞❬bar❭➞❬foo❭➞∅')

    def testLenEmpty(self) -> None:
        self.assertEqual(len(self._empty), 0)

    def testLen1(self) -> None:
        self.assertEqual(len(self._1item), 1)

    def testLen2(self) -> None:
        self.assertEqual(len(self._2items), 2)

    def testLen3(self) -> None:
        self.assertEqual(len(self._3items), 3)

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
    def testPopEmpty(self) -> None:
        # Fails because idx stays negative
        with self.assertRaises(ValueError):
            self._empty.pop()

    def testPop1(self) -> None:
        self.assertEqual(self._1item.pop(), 'foo')
        self.assertTrue(self._1item.empty())

    def testPop2(self) -> None:
        self.assertEqual(self._2items.pop(), 'foo')
        self.assertEqual(str(self._2items), '❬bar❭➞∅')

    def testPop2_0(self) -> None:
        self.assertEqual(self._2items.pop(0), 'bar')
        self.assertEqual(str(self._2items), '❬foo❭➞∅')

    def testPop3(self) -> None:
        self.assertEqual(self._3items.pop(), 'foo')
        self.assertEqual(str(self._3items), '❬baz❭➞❬bar❭➞∅')

    def testPop3_0(self) -> None:
        self.assertEqual(self._3items.pop(0), 'baz')
        self.assertEqual(str(self._3items), '❬bar❭➞❬foo❭➞∅')

    def testPop3_1(self) -> None:
        self.assertEqual(self._3items.pop(1), 'bar')
        self.assertEqual(str(self._3items), '❬baz❭➞❬foo❭➞∅')

    def testPop3_n2(self) -> None:
        self.assertEqual(self._3items.pop(-2), 'bar')
        self.assertEqual(str(self._3items), '❬baz❭➞❬foo❭➞∅')

    def testPop3_n3(self) -> None:
        self.assertEqual(self._3items.pop(-3), 'baz')
        self.assertEqual(str(self._3items), '❬bar❭➞❬foo❭➞∅')

    # Test index()
    def testIndexEmpty(self) -> None:
        with self.assertRaises(ValueError):
            self._empty.index(5)

    def testIndex3NodesAbsent(self) -> None:
        with self.assertRaises(ValueError):
            self._3items.index('xyzzy')

    def testIndex3NodesPresent(self) -> None:
        valueList = ['baz', 'bar', 'foo']
        for i in range(len(valueList)):
            with self.subTest(i=i, value=valueList[i]):
                self.assertEqual(self._3items.index(valueList[i]), i)


if __name__ == '__main__':
    unittest.main()

