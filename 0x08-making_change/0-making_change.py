#!/usr/bin/python3
""" This module helps make change O(n)"""


def makeChange(coins, total):
    """
        makeChange

        Args:
            coins:  is a list of the values of the coins in your possession
            total: a value greater than the number of coins
    """
    temp_value = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            temp_value += total // coin
            total = total % coin

    return temp_value if total == 0 else -1


if __name__ == '__main__':

    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
