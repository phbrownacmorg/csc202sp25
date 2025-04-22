import unittest
# import the code you want to test here
from Hashtable import Hashtable

class TestHashtable(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def setUp(self) -> None:
        self._empty = Hashtable[str, str]()

        self._1item = Hashtable[str, str]()
        self._1item['Zelle'] = 'John'

        self._6items = Hashtable[str, str]()
        self._6items['Barrera'] = 'Joseph'
        self._6items['Brown'] = 'Peter'
        self._6items['Mangum'] = 'Amanda'
        self._6items['Nasiri'] = 'Moloud'
        self._6items['Sorrells'] = 'Jessica'
        self._6items['Zelle'] = 'John'

    def testHashA(self) -> None:
        self.assertEqual(Hashtable.hashval('a'), 1)

    def testHashZelle(self) -> None:
        self.assertEqual(Hashtable.hashval('Zelle'), 60)

    def testHash0(self) -> None:
        self.assertEqual(Hashtable.hashval('0'), 16)

    def testHash40(self) -> None:
        self.assertEqual(Hashtable.hashval('40'), 28)

    def testHashBarrera(self) -> None:
        self.assertEqual(Hashtable.hashval('Barrera'), 63)

    def testHashBrown(self) -> None:
        self.assertEqual(Hashtable.hashval('Brown'), 72)

    def testHashMangum(self) -> None:
        self.assertEqual(Hashtable.hashval('Mangum'), 69)

    def testHashNasiri(self) -> None:
        self.assertEqual(Hashtable.hashval('Nasiri'), 70)

    def testHashSorrells(self) -> None:
        self.assertEqual(Hashtable.hashval('Sorrells'), 118)

    def testTableSizeInit(self) -> None:
        self.assertEqual(self._empty.tablesize(), Hashtable.INITIAL_SIZE)
        self.assertEqual(self._1item.tablesize(), Hashtable.INITIAL_SIZE)
        self.assertEqual(self._6items.tablesize(), Hashtable.INITIAL_SIZE)

    def testGetitemZelleEmpty(self) -> None:
        with self.assertRaises(KeyError):
            self._empty['Zelle']

    def testGetZelleEmpty(self) -> None:
        self.assertEqual(self._empty.get('Zelle'), None)

    def testGetZellePresent(self) -> None:
        self.assertEqual(self._1item.get('Zelle'), 'John')

    def testGetZellePresentBrackets(self) -> None:
        self.assertEqual(self._1item['Zelle'], 'John')

    def testGet5Items(self) -> None:
        keys: list[str] = ['Barrera', 'Brown', 'Mangum', 'Nasiri', 'Sorrells', 'Zelle']
        values: list[str] = ['Joseph', 'Peter', 'Amanda', 'Moloud', 'Jessica', 'John']
        for i in range(len(keys)):
            with self.subTest(key=keys[i]):
                self.assertEqual(self._6items[keys[i]], values[i])
        with self.assertRaises(KeyError):
            self._6items['Hopkins']

    def testReplacement(self) -> None:
        self.assertEqual(self._6items['Brown'], 'Peter')
        self._6items['Brown'] = 'Laura'
        self.assertEqual(self._6items['Brown'], 'Laura')

    def testChaining(self) -> None:
        self.assertEqual(Hashtable.hashval('Barrera') % self._6items.tablesize(), 3)
        self.assertEqual(Hashtable.hashval('Brown') % self._6items.tablesize(), 0)
        self.assertEqual(Hashtable.hashval('Mangum') % self._6items.tablesize(), 1)
        self.assertEqual(Hashtable.hashval('Nasiri') % self._6items.tablesize(), 2)
        self.assertEqual(Hashtable.hashval('Sorrells') % self._6items.tablesize(), 2)
        self.assertEqual(Hashtable.hashval('Zelle') % self._6items.tablesize(), 0)

    def testBinIdx(self) -> None:
        self.assertEqual(self._6items._bin_idx('Barrera', 0), -1)
        self.assertEqual(self._6items._bin_idx('Barrera', 1), -1)
        self.assertEqual(self._6items._bin_idx('Barrera', 2), -1)
        self.assertEqual(self._6items._bin_idx('Barrera', 3), 0)

        self.assertEqual(self._6items._bin_idx('Brown', 0), 1)  # Same chain as Zelle
        self.assertEqual(self._6items._bin_idx('Brown', 1), -1)
        self.assertEqual(self._6items._bin_idx('Brown', 2), -1)
        self.assertEqual(self._6items._bin_idx('Brown', 3), -1)

        self.assertEqual(self._6items._bin_idx('Mangum', 0), -1)
        self.assertEqual(self._6items._bin_idx('Mangum', 1), 0)
        self.assertEqual(self._6items._bin_idx('Mangum', 2), -1)
        self.assertEqual(self._6items._bin_idx('Mangum', 3), -1)

        self.assertEqual(self._6items._bin_idx('Nasiri', 0), -1)
        self.assertEqual(self._6items._bin_idx('Nasiri', 1), -1)
        self.assertEqual(self._6items._bin_idx('Nasiri', 2), 1) # Same chain as Sorrells
        self.assertEqual(self._6items._bin_idx('Nasiri', 3), -1)

        self.assertEqual(self._6items._bin_idx('Sorrells', 0), -1)
        self.assertEqual(self._6items._bin_idx('Sorrells', 1), -1)
        self.assertEqual(self._6items._bin_idx('Sorrells', 2), 0)
        self.assertEqual(self._6items._bin_idx('Sorrells', 3), -1)

        self.assertEqual(self._6items._bin_idx('Zelle', 0), 0)
        self.assertEqual(self._6items._bin_idx('Zelle', 1), -1)
        self.assertEqual(self._6items._bin_idx('Zelle', 2), -1)
        self.assertEqual(self._6items._bin_idx('Zelle', 3), -1)

    # Test mixins
    def testKeys(self) -> None:
        self.assertEqual(list(self._empty.keys()), [])
        self.assertEqual(list(self._1item.keys()), ['Zelle'])
        self.assertEqual(list(self._6items.keys()), ['Zelle', 'Brown', 'Mangum', 'Sorrells', 'Nasiri', 'Barrera'])

    def testContains(self) -> None:
        keys = ['Zelle', 'Brown', 'Mangum', 'Sorrells', 'Nasiri', 'Barrera']
        for key in keys:
            with self.subTest(key=key):
                self.assertFalse(key in self._empty)
                self.assertTrue(key in self._6items)
        self.assertTrue('Zelle' in self._1item)
        for key in keys[1:]:
            with self.subTest(key=key):
                self.assertFalse(key in self._1item)

if __name__ == '__main__':
    unittest.main()

