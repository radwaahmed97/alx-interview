#!/usr/bin/python3

from math import floor


def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coin_counter = 0

    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            count = total // coin
            coin_counter += count
            total -= count * coin

    if total > 0:
        return -1

    return coin_counter
