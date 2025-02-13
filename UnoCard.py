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

    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = False
        suit: str = self.suit()
        rank: str = self.rank()
        if suit in self.COLOR_SUITS and rank in self.COLOR_RANKS:
            valid = True
        elif suit in self.WILD_SUITS and rank in self.WILD_RANKS:
            valid = True
        return valid
    
    def __init__(self, suit: str, rank: str) -> None:
        """Constructor."""
        # Pre:
        assert (suit in self.COLOR_SUITS and rank in self.COLOR_RANKS) or \
                (suit in self.WILD_SUITS and rank in self.WILD_RANKS), "Failed precondition"
        super().__init__(suit, rank)

    @classmethod
    def makeDeck(cls) -> list[AbstractCard]:
        """Make a deck of UnoCards."""
        deck: list[AbstractCard] = []

        # FILL THIS IN

        return deck