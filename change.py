
def greedy_change(denoms: list[int], amount: int) -> list[int]:
    """Takes a list of coin values DENOMS sorted in decreasing order
    and an AMOUNT for which to make change, and returns a list of
    integers NUMS such that if NUMS[i] is the number of coins of value
    DENOMS[i], the coins will sum to AMOUNT.  The function is recursive,
    using the greedy algorithm."""
    # Pre:
    assert amount >= 0, 'Cannot make change for a negative value'
    assert (len(denoms) == 0) or (amount % denoms[-1] == 0), \
            "Can't make change if the smallest coin doesn't divide the amount"
    # assert DENOMS is sorted in descending order

    # Ensure DENOMS is sorted descending
    #denoms.sort(reverse=True) # Relies on O(n) sorting of an already-sorted list

    # Greedy algorithm
    result: list[int]
    if len(denoms) == 0: # Base case; no more coin denominations to check
        result = []
    else:
        # Take as many as we can of the most valuable coin (this is why it's greedy)
        biggest_coin = amount // denoms[0]
        # Make change for what's left, using the rest of the coin denominations
        result = [biggest_coin] + greedy_change(denoms[1:], amount % denoms[0])
    return result

def main(args: list[str]) -> int:
    # Greedy algorithm gives optimal results
    US_coins: list[int] = [25, 10, 5, 1]
    # Greedy algorithm does not give optimal results
    perverse_coins: list[int] = [25, 10, 5, 4, 1]
    coin_values = perverse_coins
    amount: int = int(input('Please enter an amount for which to make change: '))
    num_coins = greedy_change(coin_values, amount)

    print('Th optimal change (fewest coins) for {0} cents is this:'.format(amount))
    for i in range(len(coin_values)):
        print('\t{0} {1}-cent coins'.format(num_coins[i], coin_values[i]))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))