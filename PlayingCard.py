from AbstractCard import AbstractCard

class PlayingCard(AbstractCard):
    """Class to represent a card of the normal French-suited
    pattern that's common all over the West."""

    SUITS: tuple[str,...] = ('clubs', 'diamonds', 'hearts', 'spades')
    RANKS: tuple[str,...] = ('ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                              'jack', 'queen', 'king')
    
    @classmethod
    def makeDeck(cls) -> list[AbstractCard]:
        """Make a deck of PlayingCards."""
        deck: list[AbstractCard] = []
        for suit in cls.SUITS:
            for rank in cls.RANKS:
                deck.append(PlayingCard(suit, rank))
        return deck