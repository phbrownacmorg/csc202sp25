import unittest
# import the code you want to test here
from Hashtable import Hashtable

class TestHashtable(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def setUp(self) -> None:
        self._empty = Hashtable[str, str]()

    def testHashA(self) -> None:
        self.assertEqual(Hashtable.hashval('a'), 1)

    def testHashZelle(self) -> None:
        self.assertEqual(Hashtable.hashval('Zelle'), 60)

    def testHash0(self) -> None:
        self.assertEqual(Hashtable.hashval('0'), 16)

    def testHash40(self) -> None:
        self.assertEqual(Hashtable.hashval('40'), 28)

    def testTableSizeInit(self) -> None:
        self.assertEqual(self._empty.tablesize(), Hashtable.INITIAL_SIZE)

    def testGetZelleEmpty(self) -> None:
        self.assertEqual(self._empty.get('Zelle'), None)

    def testGetZellePresent(self) -> None:
        self._empty.put('Zelle', 'John')
        self.assertEqual(self._empty.get('Zelle'), 'John')



if __name__ == '__main__':
    unittest.main()

