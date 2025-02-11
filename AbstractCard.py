import abc
from functools import total_ordering

@total_ordering
class AbstractCard(abc.ABC):
    """Class to represent a very generic playing card.
    This class basically handles suits and ranks.
    Cards are immutable once created."""

    # Set of possible suits
    SUITS: tuple[str,...] = ()

    # Set of possible ranks (names) of cards
    RANKS: tuple[str,...] = ()

    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = self.suit() in self.SUITS
        assert valid, 'suit() failed: ' + self.suit()
        valid = valid and (self.rank() in self.RANKS)
        assert valid, 'rank() failed: ' + self.rank()
        return valid

    def __init__(self, suit: str, rank: str) -> None:
        """Construct a card with the given suit and rank."""
        # Pre:
        assert suit in self.SUITS and rank in self.RANKS, 'Failed precondition'
        self._suit: str = suit
        self._rank: str = rank
        # Post:
        assert self._invariant(), 'Failed postcondition'

    # Query functions
    def suit(self) -> str:
        """Get the card's suit."""
        return self._suit
    
    def rank(self) -> str:
        """Get the card's rank."""
        return self._rank
    
    def __eq__(self, other: object) -> bool:
        """Test a card for equality with another object.
        If the suits are equal and the ranks are equal,
        the cards are equal."""
        equal: bool = hasattr(other, 'suit') and hasattr(other, 'rank')
        equal = equal and (self.suit() == other.suit()) and \
            (self.rank() == other.rank())
        return equal

    def __lt__(self, other:'AbstractCard') -> bool:
        """Test two cards for ordering.  A card is defined as "less than"
        another card if its rank is less than the other card's rank.
        If the ranks are equal, the order of suits is used instead.
        The cards have to have compatible lists of suits and ranks."""
        # Pre: the cards have to be comparable to each other
        assert (other.suit() in self.SUITS and other.rank() in self.RANKS) \
                or (self.suit() in other.SUITS and self.rank() in other.RANKS), \
                    'Cards are not comparable'
        # Which list of suits and ranks do we use?  Start with self's.
        less_than: bool = False
        suitlist: tuple[str,...] = self.SUITS
        ranklist: tuple[str,...] = self.RANKS
        if other.suit() not in self.SUITS or other.rank() not in self.RANKS:
            suitlist = other.SUITS
            ranklist = other.RANKS
        rank1: int = ranklist.index(self.rank())
        rank2: int = ranklist.index(other.rank())
        less_than = (rank1 < rank2)
        # If the ranks are equal...
        if self.rank() == other.rank():
            suit1: int = suitlist.index(self.suit())
            suit2: int = suitlist.index(other.suit())
            less_than = suit1 < suit2
        return less_than


    @classmethod
    @abc.abstractmethod
    def makeDeck(cls) -> list['AbstractCard']:
        """Make a deck of this kind of Card."""
    

