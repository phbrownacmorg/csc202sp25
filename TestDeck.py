import unittest
# import the code you want to test here
from AbstractCard import AbstractCard
from Deck import Deck
from PlayingCard import PlayingCard
from UnoCard import UnoCard
import random

class TestDeck(unittest.TestCase):

    # Every method that starts with the string "test"
    # will be executed as a unit test
    def testEmptyAtStart(self) -> None:
        deck: Deck = Deck()
        self.assertTrue(deck.isEmpty())
        self.assertEqual(len(deck), 0)

    def testAddCards(self) -> None:
        # Also checks isEmpty (when False) and __len__
        deck: Deck = Deck()
        self.assertTrue(deck.isEmpty())
        deck.addCards(PlayingCard.makeDeck())
        self.assertEqual(len(deck), 52)
        self.assertFalse(deck.isEmpty())
        deck.addCards(UnoCard.makeDeck())
        self.assertEqual(len(deck), 160)
        self.assertFalse(deck.isEmpty())

    def testDeal(self) -> None:
        deck: Deck = Deck()
        deck.addCards(PlayingCard.makeDeck())
        self.assertEqual(len(deck), 52)
        card: AbstractCard = deck.deal()
        self.assertEqual(len(deck), 51)
        self.assertEqual(card, PlayingCard('spades', 'king'))
    
    def testStrEmpty(self) -> None:
        self.assertEqual(str(Deck()), """Deck:\n""")

    def testStrCards(self) -> None:
        deck = Deck()
        cards: list[AbstractCard] = PlayingCard.makeDeck()
        expected: str = 'Deck:\n'
        for card in cards:
            expected += '\t' + str(card) + '\n'
        deck.addCards(cards)
        self.assertEqual(str(deck), expected)

        cards = UnoCard.makeDeck()
        for card in cards:
            expected += '\t' + str(card) + '\n'
        deck.addCards(cards)
        #print(deck)
        self.assertEqual(str(deck), expected)

    def testShuffle(self) -> None:
        random.seed(5628) # doesn't matter what the number is, as long as it's constant
        deck = Deck()
        deck.addCards(PlayingCard.makeDeck())
        # deck is pretty thoroughly ordered
        inorder: int = 0
        for i in range(51):
            if deck._cards[i] < deck._cards[i+1]:
                inorder += 1
        self.assertEqual(inorder, 48)
        deck.shuffle()
        self.assertEqual(len(deck), 52)
        for suit in PlayingCard.SUITS:
            for rank in PlayingCard.RANKS:
                self.assertEqual(deck._cards.count(PlayingCard(suit, rank)), 1)
        inorder = 0
        for i in range(51):
            if deck._cards[i] < deck._cards[i+1]:
                inorder += 1
        self.assertEqual(inorder, 25)
        # seed 144000 gives 25 in order
        # seed 37 gives 27 in order
        # seed 4935 gives 27 in order
        # seed 5628 gives 25 in order

        print(deck)

if __name__ == '__main__':
    unittest.main()

