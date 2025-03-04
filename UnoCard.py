from AbstractCard import AbstractCard

class UnoCard(AbstractCard):
    """Class to represent an Uno card.  This class represents the pre-2018
    classic Uno cards."""

    # Class attributes
    COLOR_SUITS: tuple[str,...] = ('red', 'yellow', 'green', 'blue')
    WILD_SUITS: tuple[str] = ('wild',) # 1-item tuple needs a comma
    SUITS: tuple[str,...] = COLOR_SUITS + WILD_SUITS
    COLOR_RANKS: tuple[str,...] = ('0', '1', '2', '3', '4', '5', '6', '7', '8',
                                   '9', 'skip', 'reverse', 'draw 2')
    WILD_RANKS: tuple[str,...] = ('', 'draw 4')
    RANKS: tuple[str, ...] = COLOR_RANKS + WILD_RANKS

    @classmethod
    def _legalCombo(cls, suit: str, rank: str) -> bool:
        return (suit in cls.COLOR_SUITS and rank in cls.COLOR_RANKS) or \
                (suit in cls.WILD_SUITS and rank in cls.WILD_RANKS)

    @classmethod
    def makeDeck(cls) -> list[AbstractCard]:
        """Make a deck of UnoCards."""
        deck: list[AbstractCard] = []
        for suit in cls.SUITS:
            for rank in cls.RANKS:
                if cls._legalCombo(suit, rank):
                    deck.append(UnoCard(suit, rank)) # At least one of every legal card
                    if rank != '0':
                        deck.append(UnoCard(suit, rank)) # At least two of all non-0's
                        if suit in cls.WILD_SUITS:
                            deck.append(UnoCard(suit, rank))
                            deck.append(UnoCard(suit, rank)) # Four of each wild card

        return deck