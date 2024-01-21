#!/usr/bin/python3
"""This module defines a function `minOperations(n: int)`"""


def minOperations(n):
    """ calculates the fewest number of operations
        (copy, paste) needed to result in exactly
        n H characters
    """
    len_H = 1
    len_dup_H = 0
    total_operations = 0

    while len_H < n:
        if n % len_H == 0:
            total_operations += 2
            len_dup_H = len_H
            len_H *= 2
        else:
            total_operations += 1
            len_H += len_dup_H
    return total_operations
