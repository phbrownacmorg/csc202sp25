import unittest
# import the code you want to test here
from Stack import Stack

class TestNothing(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testIsEmptyTrue(self) -> None:
        self.assertTrue(Stack[str]().isEmpty())

    def testIsEmptyFalse(self) -> None:
        st: Stack[str] = Stack[str]()
        st.push('a')
        self.assertFalse(st.isEmpty())

    def testPeekEmpty(self) -> None:
        with self.assertRaises(AssertionError):
            Stack[str]().peek()

    def testPeekNonEmpty(self) -> None:
        st: Stack[str] = Stack[str]()
        st.push('a')
        self.assertEqual(st.peek(), 'a')
        self.assertFalse(st.isEmpty()) # peek() didn't change the stack
        st.push('b') # Are we looking at the top item?
        self.assertEqual(st.peek(), 'b')

    def testPopEmpty(self) -> None:
        with self.assertRaises(AssertionError):
            Stack[str]().pop()

    def testPopOneItem(self) -> None:
        st: Stack[str] = Stack[str]()
        st.push('a')
        self.assertFalse(st.isEmpty())
        self.assertEqual(st.pop(), 'a')
        self.assertTrue(st.isEmpty()) # pop() should remove the item from the stack

    def testPopTwoItems(self) -> None:
        st: Stack[str] = Stack[str]()
        st.push('a')
        st.push('b')
        self.assertEqual(st.pop(), 'b')
        self.assertFalse(st.isEmpty()) # Still has one item
        self.assertEqual(st.pop(), 'a')
        self.assertTrue(st.isEmpty())

if __name__ == '__main__':
    unittest.main()

