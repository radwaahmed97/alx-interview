#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins
that needed to meet a given amount total
"""
from math import floor


def makeChange(coins, total):
    """Returns fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    else:
        coins_sum = 0
        coins.sort(reverse=True)
        for i in range(len(coins)):
            coins_sum += coins[i]
            if coins_sum == total:
                return i + 1
            elif coins_sum < total:
                if total % coins_sum == 0:
                    return total // coins_sum
                else:
                    n_coins_i = floor(total / coins_sum)
                    num_coins = n_coins_i + ((total % coins_sum)/coins[i+1])
                    if (total % coins_sum) % coins[i+1] == 0:
                        return int(num_coins)
                    else:
                        return -1
