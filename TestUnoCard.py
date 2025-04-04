import unittest
# import the code you want to test here
from AbstractCard import AbstractCard
from UnoCard import UnoCard

class TestUnoCard(unittest.TestCase):

    # Called before each new test
    def setUp(self) -> None:
        self._green4 = UnoCard('green', '4')
        self._red4 = UnoCard('red', '4') # Same rank, suit is less: less
        self._blue3 = UnoCard('blue', '3') # Suit is greater, rank is less: less
        self._red5 = UnoCard('red', '5') # Suit is less, rank is greater: greater
        self._green4_2 = UnoCard('green', '4') # Different objects, same value

        return super().setUp()

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
                                with self.subTest(suit1=suit1, rank1=rank1, 
                                                  suit2=suit2, rank2=rank2):
                                    self.assertEqual(card1 == card2, 
                                                     suit1 == suit2 and rank1 == rank2)
        # Check defined combinations, to verify that my loops test what I think they test
        self.assertFalse(self._green4 == self._red4)
        self.assertFalse(self._green4 == self._blue3)
        self.assertFalse(self._green4 == self._red5)
        self.assertTrue(self._green4 == self._green4_2)

    def testNe(self) -> None:
        # Make this test all combinations
        for suit1 in UnoCard.SUITS:
            for rank1 in UnoCard.RANKS:
                if UnoCard._legalCombo(suit1, rank1):
                    card1: UnoCard = UnoCard(suit1, rank1)
                    with self.subTest(suit=suit1, rank=rank1):
                        self.assertTrue(card1 != 'not a card')
                    for suit2 in UnoCard.SUITS:
                        for rank2 in UnoCard.RANKS:
                            if UnoCard._legalCombo(suit2, rank2):
                                card2: UnoCard = UnoCard(suit2, rank2)
                                with self.subTest(suit1=suit1, rank1=rank1, 
                                                  suit2=suit2, rank2=rank2):
                                    self.assertEqual(card1 != card2, 
                                                     suit1 != suit2 or rank1 != rank2)
        # Check defined combinations, to verify that my loops test what I think they test
        self.assertTrue(self._green4 != self._red4)
        self.assertTrue(self._green4 != self._blue3)
        self.assertTrue(self._green4 != self._red5)
        self.assertFalse(self._green4 != self._green4_2)
    
    def testLt(self) -> None:
        # Make this test all combinations
        for suit1 in UnoCard.SUITS:
            for rank1 in UnoCard.RANKS:
                if UnoCard._legalCombo(suit1, rank1):
                    card1: UnoCard = UnoCard(suit1, rank1)
                    st1: int = UnoCard.SUITS.index(suit1)
                    rnk1: int = UnoCard.RANKS.index(rank1)
                    for suit2 in UnoCard.SUITS:
                        for rank2 in UnoCard.RANKS:
                            if UnoCard._legalCombo(suit2, rank2):
                                card2: UnoCard = UnoCard(suit2, rank2)
                                st2: int = UnoCard.SUITS.index(suit2)
                                rnk2: int = UnoCard.RANKS.index(rank2)
                                with self.subTest(suit1=suit1, rank1=rank1, 
                                                  suit2=suit2, rank2=rank2):
                                    self.assertEqual(card1 < card2, 
                                                     rnk1 < rnk2 or (rank1 == rank2
                                                                     and st1 < st2))
        # Check defined combinations, to verify that my loops test what I think they test
        self.assertFalse(self._green4 < self._red4)
        self.assertFalse(self._green4 < self._blue3)
        self.assertTrue(self._green4 < self._red5)
        self.assertFalse(self._green4 < self._green4_2)

    def testLe(self) -> None:
        # Make this test all combinations
        for suit1 in UnoCard.SUITS:
            for rank1 in UnoCard.RANKS:
                if UnoCard._legalCombo(suit1, rank1):
                    card1: UnoCard = UnoCard(suit1, rank1)
                    st1: int = UnoCard.SUITS.index(suit1)
                    rnk1: int = UnoCard.RANKS.index(rank1)
                    for suit2 in UnoCard.SUITS:
                        for rank2 in UnoCard.RANKS:
                            if UnoCard._legalCombo(suit2, rank2):
                                card2: UnoCard = UnoCard(suit2, rank2)
                                st2: int = UnoCard.SUITS.index(suit2)
                                rnk2: int = UnoCard.RANKS.index(rank2)
                                with self.subTest(suit1=suit1, rank1=rank1, 
                                                  suit2=suit2, rank2=rank2):
                                    self.assertEqual(card1 <= card2, 
                                                     rnk1 < rnk2 or (rank1 == rank2
                                                                     and st1 <= st2))
        # Check defined combinations, to verify that my loops test what I think they test
        self.assertFalse(self._green4 <= self._red4)
        self.assertFalse(self._green4 <= self._blue3)
        self.assertTrue(self._green4 <= self._red5)
        self.assertTrue(self._green4 <= self._green4_2)

    def testGt(self) -> None:
        # Make this test all combinations
        for suit1 in UnoCard.SUITS:
            for rank1 in UnoCard.RANKS:
                if UnoCard._legalCombo(suit1, rank1):
                    card1: UnoCard = UnoCard(suit1, rank1)
                    st1: int = UnoCard.SUITS.index(suit1)
                    rnk1: int = UnoCard.RANKS.index(rank1)
                    for suit2 in UnoCard.SUITS:
                        for rank2 in UnoCard.RANKS:
                            if UnoCard._legalCombo(suit2, rank2):
                                card2: UnoCard = UnoCard(suit2, rank2)
                                st2: int = UnoCard.SUITS.index(suit2)
                                rnk2: int = UnoCard.RANKS.index(rank2)
                                with self.subTest(suit1=suit1, rank1=rank1, 
                                                  suit2=suit2, rank2=rank2):
                                    self.assertEqual(card1 > card2, 
                                                     rnk1 > rnk2 or (rank1 == rank2
                                                                     and st1 > st2))
        # Check defined combinations, to verify that my loops test what I think they test
        self.assertTrue(self._green4 > self._red4)
        self.assertTrue(self._green4 > self._blue3)
        self.assertFalse(self._green4 > self._red5)
        self.assertFalse(self._green4 > self._green4_2)

    def testGe(self) -> None:
        for suit1 in UnoCard.SUITS:
            for rank1 in UnoCard.RANKS:
                if UnoCard._legalCombo(suit1, rank1):
                    card1: UnoCard = UnoCard(suit1, rank1)
                    st1: int = UnoCard.SUITS.index(suit1)
                    rnk1: int = UnoCard.RANKS.index(rank1)
                    for suit2 in UnoCard.SUITS:
                        for rank2 in UnoCard.RANKS:
                            if UnoCard._legalCombo(suit2, rank2):
                                card2: UnoCard = UnoCard(suit2, rank2)
                                st2: int = UnoCard.SUITS.index(suit2)
                                rnk2: int = UnoCard.RANKS.index(rank2)
                                with self.subTest(suit1=suit1, rank1=rank1, 
                                                  suit2=suit2, rank2=rank2):
                                    self.assertEqual(card1 >= card2, 
                                                     rnk1 > rnk2 or (rank1 == rank2
                                                                     and st1 >= st2))
        # Check defined combinations, to verify that my loops test what I think they test
        self.assertTrue(self._green4 >= self._red4)
        self.assertTrue(self._green4 >= self._blue3)
        self.assertFalse(self._green4 >= self._red5)
        self.assertTrue(self._green4 >= self._green4_2)
        # self.assertTrue(UnoCard('blue', '4') <= UnoCard('blue', '4'))
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

