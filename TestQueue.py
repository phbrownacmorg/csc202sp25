import unittest
# import the code you want to test here
from CircQ import Queue

class TestQueue(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testIsEmptyTrue(self) -> None:
        self.assertTrue(Queue[str]().isEmpty())

    def testIsEmptyFalse(self) -> None:
        q: Queue[str] = Queue[str]()
        q.add('a')
        self.assertFalse(q.isEmpty())

    def testPeekEmpty(self) -> None:
        with self.assertRaises(AssertionError):
            Queue[str]().peek()

    def testPeekNonEmpty(self) -> None:
        q: Queue[str] = Queue[str]()
        q.add('a')
        self.assertEqual(q.peek(), 'a')
        self.assertFalse(q.isEmpty()) # peek() didn't change the queue
        q.add('b') # Are we looking at the first item?
        self.assertEqual(q.peek(), 'a')

    def testPopEmpty(self) -> None:
        with self.assertRaises(AssertionError):
            Queue[str]().pop()

    def testPopOneItem(self) -> None:
        q: Queue[str] = Queue[str]()
        q.add('a')
        self.assertFalse(q.isEmpty())
        self.assertEqual(q.pop(), 'a')
        self.assertTrue(q.isEmpty()) # pop() should remove the item from the queue

    def testPopTwoItems(self) -> None:
        q: Queue[str] = Queue[str]()
        q.add('a')
        q.add('b')
        self.assertEqual(q.pop(), 'a')
        self.assertFalse(q.isEmpty()) # Still has one item
        self.assertEqual(q.pop(), 'b')
        self.assertTrue(q.isEmpty())

    def testPopFourItems(self) -> None:
        q: Queue[str] = Queue[str]()
        q.add('a')
        q.add('b')
        self.assertEqual(q.pop(), 'a')
        self.assertFalse(q.isEmpty()) # Still has one item
        q.add('c')
        self.assertEqual(q.pop(), 'b')
        q.add('d')
        self.assertEqual(q.pop(), 'c')
        self.assertEqual(q.pop(), 'd')
        self.assertTrue(q.isEmpty())

    def testPop8Items(self) -> None:
        q: Queue[str] = Queue[str]()
        q.add('a')
        q.add('b')
        self.assertEqual(q.pop(), 'a')
        self.assertFalse(q.isEmpty()) # Still has one item
        q.add('c')
        self.assertEqual(q.pop(), 'b')
        q.add('d')
        q.add('e')
        q.add('f')
        q.add('g')
        q.add('h')
        self.assertEqual(q.pop(), 'c')
        self.assertEqual(q.pop(), 'd')
        self.assertEqual(q.pop(), 'e')
        self.assertEqual(q.pop(), 'f')
        self.assertEqual(q.pop(), 'g')
        self.assertEqual(q.pop(), 'h')
        self.assertTrue(q.isEmpty())



if __name__ == '__main__':
    unittest.main()

