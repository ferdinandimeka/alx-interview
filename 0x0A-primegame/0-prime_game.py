#!/usr/bin/python3
"""Prime game module
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with 'x' rounds.
    """
    if x < 1 or not nums:
        return None
    maria_wins, ben_wins = 0, 0
    # generate a list of primes up to the max value in nums
    primes = [1] * (max(nums) + 1)
    primes[0], primes[1] = 0, 0
    for i in range(2, len(primes)):
        if primes[i] == 1:
            for j in range(i * i, len(primes), i):
                primes[j] = 0
    # calculate the winner of each round
    for round in range(x):
        prime_count = sum(primes[:nums[round] + 1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    # calculate the overall winner
    if maria_wins == ben_wins:
        return None
    return "Maria" if maria_wins > ben_wins else "Ben"
