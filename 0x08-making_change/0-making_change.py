#!/usr/bin/python3
"""making change module.
"""


def makeChange(coins, total):
    """Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    if type(coins) != list or len(coins) <= 0:
        return -1
    if not all(map(lambda x: type(x) == int and x > 0, coins)):
        return -1
    coins.sort(reverse=True)
    min_coins = 0
    for coin in coins:
        if total <= 0:
            break
        if total >= coin:
            min_coins += total // coin
            total %= coin
    if total > 0:
        return -1
    return min_coins
