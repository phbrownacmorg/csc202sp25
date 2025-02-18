from AbstractCard import AbstractCard
from typing import Iterable
import random

class Deck:
    """Class to represent a deck of cards.  The deck is
    implemented as a list of AbstractCards.  The end of
    the list is the top of the deck."""

    # class invariant
    def _invariant(self) -> bool:
        """Class invariant: all the cards are AbstractCards."""
        valid: bool = True
        for card in self._cards:
            valid = valid and isinstance(card, AbstractCard)
        return valid
    
    def __init__(self) -> None:
        """Construct an empty Deck."""
        self._cards: list[AbstractCard] = []
        # Post
        assert self._invariant()

    # Query methods
    def __len__(self) -> int:
        """Size of the deck."""
        return len(self._cards)

    def isEmpty(self) -> bool:
        """Return True iff the deck is empty."""
        return len(self) == 0
    
    # Demonstrates polymorphism
    def __str__(self) -> str:
        """Make a string representation of the deck."""
        result: str = """Deck:\n"""
        for card in self._cards:
            result += '\t{0}\n'.format(str(card))
        return result

    # Mutator methods
    def shuffle(self) -> None:
        """Shuffle the deck."""
        random.shuffle(self._cards)
        # One slightly less opaque way way to do shuffling.  There exist plenty of others.
        # oldcards: list[AbstractCard] = self._cards[:] # make a copy
        # self._cards = [] # Empty out the deck itself
        # while len(oldcards) > 0:
        #     self._cards.append(oldcards.pop(random.randrange(0, len(oldcards))))


    def deal(self) -> AbstractCard:
        """Deal a card from the top of the deck."""
        # Pre:
        assert not self.isEmpty()
        return self._cards.pop()
        # Post: the deck got one card smaller,
        #        AND the return value is the old
        #        top of the deck.

    def addCards(self, newCards: Iterable[AbstractCard]) -> None:
        # Pre: nothing in NEWCARDS that isn't an AbstractCard
        self._cards.extend(newCards)
        # Post: size of deck is the old size plus len(newCards) AND
        assert self._invariant()