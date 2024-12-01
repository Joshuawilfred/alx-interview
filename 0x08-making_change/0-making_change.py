#!/usr/bin/python3
"""Module that defines the makeChange function
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins
    needed to meet total, if possible.
    """
    if total <= 0:
        return 0

    rest = total
    coin_count = 0
    coin_index = 0

    coins_sorted = sorted(coins, reverse=True)
    n = len(coins)

    while rest > 0:
        if coin_index >= n:
            return -1
        if rest - coins_sorted[coin_index] >= 0:
            rest -= coins_sorted[coin_index]
            coin_count += 1
        else:
            coin_index += 1

    return coin_count
