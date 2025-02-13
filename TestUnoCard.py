import unittest
# import the code you want to test here
from AbstractCard import AbstractCard
from UnoCard import UnoCard

class TestUnoCard(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testSuit(self) -> None:
        for suit in UnoCard.COLOR_SUITS:
            with self.subTest(suit=suit):
                self.assertEqual(UnoCard(suit, '8').suit(), suit)
        for suit in UnoCard.WILD_SUITS:
            with self.subTest(suit=suit):
                self.assertEqual(UnoCard(suit, '').suit(), suit)

    def testRank(self) -> None:
        for rank in UnoCard.COLOR_RANKS:
            with self.subTest(rank=rank):
                self.assertEqual(UnoCard('red', rank).rank(), rank)
        for rank in UnoCard.WILD_RANKS:
            with self.subTest(rank=rank):
                self.assertEqual(UnoCard('wild', rank).rank(), rank)

    def testStr(self) -> None:
        for rank in UnoCard.COLOR_RANKS:
            for suit in UnoCard.COLOR_SUITS:
                with self.subTest(suit=suit, rank=rank):
                    self.assertEqual(str(UnoCard(suit, rank)), suit + ' ' + rank)
        for rank in UnoCard.WILD_RANKS:
            for suit in UnoCard.WILD_SUITS:
                with self.subTest(suit=suit, rank=rank):
                    self.assertEqual(str(UnoCard(suit, rank)), 
                                     (suit + ' ' + rank).strip())

    def testEq(self) -> None:
        self.assertTrue(UnoCard('blue', '4') == UnoCard('blue', '4'))
        # Make this test all combinations

    def testNe(self) -> None:
        self.assertFalse(UnoCard('blue', '4') != UnoCard('blue', '4'))
        # Make this test all combinations
    
    def testLt(self) -> None:
        self.assertFalse(UnoCard('blue', '4') < UnoCard('blue', '4'))
        # Make this test all combinations

    def testLe(self) -> None:
        self.assertTrue(UnoCard('blue', '4') <= UnoCard('blue', '4'))
        # Make this test all combinations

    def testGt(self) -> None:
        self.assertFalse(UnoCard('blue', '4') > UnoCard('blue', '4'))
        # Make this test all combinations

    def testGe(self) -> None:
        self.assertTrue(UnoCard('blue', '4') <= UnoCard('blue', '4'))
        # Make this test all combinations

    def testMakeDeck(self) -> None:
        deck: list[AbstractCard] = UnoCard.makeDeck()
        self.assertEqual(len(deck), 108) # 108 cards total
        # Add checks to make sure each card occurs the correct number of times


if __name__ == '__main__':
    unittest.main()

