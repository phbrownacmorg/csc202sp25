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
        for rank in UnoCard.RANKS:
            for suit in UnoCard.SUITS:
                if UnoCard._legalCombo(suit, rank):
                    with self.subTest(suit=suit, rank=rank):
                        self.assertEqual(str(UnoCard(suit, rank)), (suit + ' ' + rank).strip())

    def testEq(self) -> None:
        # Make this test all combinations
        for suit1 in UnoCard.SUITS:
            for rank1 in UnoCard.RANKS:
                if UnoCard._legalCombo(suit1, rank1):
                    card1: UnoCard = UnoCard(suit1, rank1)
                    with self.subTest(suit=suit1, rank=rank1):
                        self.assertFalse(card1 == 'not a card')
                    for suit2 in UnoCard.SUITS:
                        for rank2 in UnoCard.RANKS:
                            if UnoCard._legalCombo(suit2, rank2):
                                card2: UnoCard = UnoCard(suit2, rank2)
                                with self.subTest(suit1=suit1, rank1=rank1, suit2=suit2, rank2=rank2):
                                    self.assertEqual(card1 == card2, suit1 == suit2 and rank1 == rank2)

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
        for suit in UnoCard.SUITS:
            for rank in UnoCard.RANKS:
                if UnoCard._legalCombo(suit, rank):
                    with self.subTest(suit=suit, rank=rank):
                        if rank == '0':
                            self.assertEqual(deck.count(UnoCard(suit, rank)), 1)
                        elif suit in UnoCard.WILD_SUITS:
                            self.assertEqual(deck.count(UnoCard(suit, rank)), 4)
                        else:
                            self.assertEqual(deck.count(UnoCard(suit, rank)), 2)

if __name__ == '__main__':
    unittest.main()

