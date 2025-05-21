#!/usr/bin/python3
"""
This module contains the function minOperations which calculates the minimum
number of operations (Copy All and Paste) required to achieve exactly n 'H'
characters in a text file.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations to get
    exactly n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: Minimum number of operations required to reach n 'H' characters.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
