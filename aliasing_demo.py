from copy import copy, deepcopy
from AbstractCard import AbstractCard
from PlayingCard import PlayingCard
from UnoCard import UnoCard

def print_comparison(obj1: object, label1: str, obj2: object, label2: str) -> None:
    print('{0}@{1}\t{2}@{3}\tis: {4}\t==: {5}'.format(label1, id(obj1), 
                                                     label2, id(obj2),
                                                     obj1 is obj2, obj1 == obj2))


def show_copying(deck1: list[AbstractCard]) -> None:
    print('Copying...')
    deck2 = deck1 # Two names for a single object
    print_comparison(deck1, 'deck1', deck2, 'deck2')
    print_comparison(deck1[0], 'deck1[0]', deck2[0], 'deck2[0]')
    print()

    deck3 = deck1[:] # Shallow copy
    print_comparison(deck1, 'deck1', deck3, 'deck3')
    print_comparison(deck1[0], 'deck1[0]', deck3[0], 'deck3[0]')
    print()

    deck4 = copy(deck1) # Shallow copy
    print_comparison(deck1, 'deck1', deck4, 'deck4')
    print_comparison(deck1[0], 'deck1[0]', deck4[0], 'deck4[0]')
    print()

    deck5 = deepcopy(deck1) # Shallow copy
    print_comparison(deck1, 'deck1', deck5, 'deck5')
    print_comparison(deck1[0], 'deck1[0]', deck5[0], 'deck5[0]')
    print()

def show_aliasing(decklist: list[list[AbstractCard]]) -> None:
    decklist2 = decklist[:] # Shallow copy
    print('Aliasing...')
    print_comparison(decklist[0], 'decklist[0]', decklist2[0], 'decklist2[0]')
    print('First card of each: ', decklist[0][0], decklist2[0][0])

    decklist3 = deepcopy(decklist)
    print_comparison(decklist[0], 'decklist[0]', decklist3[0], 'decklist3[0]')

    print('First card of each: ', decklist[0][0], decklist2[0][0])

    decklist[0][0] = UnoCard('green', '5')
    print('\ndecklist2[0][0] changed! Aliasing...')
    print_comparison(decklist[0], 'decklist[0]', decklist2[0], 'decklist2[0]')
    print('First card of each: ', decklist[0][0], decklist2[0][0])

    print('\ndecklist3 (deep copy) was unaffected')
    print_comparison(decklist[0], 'decklist[0]', decklist3[0], 'decklist3[0]')
    print('First card of each: ', decklist[0][0], decklist3[0][0])


def main(args: list[str]) -> int:
    deck: list[AbstractCard] = PlayingCard.makeDeck()
    show_copying(deck)

    unodeck: list[AbstractCard] = UnoCard.makeDeck()

    list1: list[list[AbstractCard]] = [deck, unodeck]
    show_aliasing(list1)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))