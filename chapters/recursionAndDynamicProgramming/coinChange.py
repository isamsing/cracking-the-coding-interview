"""
Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent),
write code to calculate the number of ways of representing n cents.
Hints: #300, #324, #343, #380, #394
"""
from typing import List


def getTotalWaysRecursively(amount: int, coins: List, index: int = 0) -> int:
    if amount == 0:
        return 1
    elif index >= len(coins):
        return 0
    else:
        ways = 0
        numOfCoins = 0
        while coins[index] * numOfCoins <= amount:
            ways += getTotalWaysRecursively(amount - (coins[index] * numOfCoins), coins, index + 1)
            numOfCoins += 1
        return ways


def getTotalWaysDP(amount: int, coins: List):
    DP = [0] * (amount + 1)
    DP[0] = 1
    for coin in coins:
        for index in range(1, len(DP)):
            if index - coin >= 0:
                DP[index] += DP[index - coin]
    return DP[-1]


if __name__ == '__main__':
    print(getTotalWaysRecursively(7, [1, 5, 7]))
    print(getTotalWaysDP(7, [1, 5, 7]))
    print(getTotalWaysRecursively(30, [1, 5, 7]))
    print(getTotalWaysDP(30, [1, 5, 7]))
