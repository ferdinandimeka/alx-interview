#!/usr/bin/python3
"""
    module that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
        calculates the fewest number of operations
    """
    if n == 1:
        return 0  # base case: already have 1 H

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
