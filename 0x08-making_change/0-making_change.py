#!/usr/bin/python3
"""making_change module"""


def makeChange(coins, total):
    """makeChange function"""
    if total == 0:
        return 0
    remainder = total
    coins_counter = 0
    coins_index = 0
    coins.sort(reverse=True)
    length = len(coins)

    while remainder > 0:
        if coins_index >= length:
            return -1
        if remainder - coins[coins_index] >= 0:
            remainder -= coins[coins_index]
            coins_counter += 1
        else:
            coins_index += 1
    return coins_counter
