import unittest
# import the code you want to test here
from AbstractCard import AbstractCard
from PlayingCard import PlayingCard

class TestPlayingCard(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testSuit(self) -> None:
        for suit in PlayingCard.SUITS:
            with self.subTest(suit=suit):
                self.assertEqual(PlayingCard(suit, 'jack').suit(), suit)

    def testVal(self) -> None:
        for rank in PlayingCard.RANKS:
            with self.subTest(rank=rank):
                self.assertEqual(PlayingCard('diamonds', rank).rank(), rank)

    def testEq(self) -> None:
        for suit1 in PlayingCard.SUITS:
            for rank1 in PlayingCard.RANKS:
                for suit2 in PlayingCard.SUITS:
                    for rank2 in PlayingCard.RANKS:
                        with self.subTest(suit1=suit1,rank1=rank1,suit2=suit2,rank2=rank2):
                            card1: PlayingCard = PlayingCard(suit1, rank1)
                            card2: PlayingCard = PlayingCard(suit2, rank2)
                            if suit1 == suit2 and rank1 == rank2:
                                self.assertTrue(card1 == card2)
                            else:
                                self.assertFalse(card1 == card2)
                            self.assertFalse(card1 == 'not a card')

    def testLt(self) -> None:
        for suit1 in PlayingCard.SUITS:
            for rank1 in PlayingCard.RANKS:
                for suit2 in PlayingCard.SUITS:
                    for rank2 in PlayingCard.RANKS:
                        with self.subTest(suit1=suit1,rank1=rank1,suit2=suit2,rank2=rank2):
                            card1: PlayingCard = PlayingCard(suit1, rank1)
                            card2: PlayingCard = PlayingCard(suit2, rank2)
                            val1: int = PlayingCard.RANKS.index(card1.rank())
                            val2: int = PlayingCard.RANKS.index(card2.rank())
                            if val1 != val2:
                                self.assertEqual(card1 < card2, val1 < val2)
                            else: # val1 == val2 => card1.rank() == card2.rank()
                                # Comparison should be based on suits
                                s1: int = PlayingCard.SUITS.index(card1.suit())
                                s2: int = PlayingCard.SUITS.index(card2.suit())
                                self.assertEqual(card1 < card2, s1 < s2)

    def testMakeDeck(self) -> None:
        deck: list[AbstractCard] = PlayingCard.makeDeck()
        self.assertEqual(len(deck), 52)

if __name__ == '__main__':
    unittest.main()

