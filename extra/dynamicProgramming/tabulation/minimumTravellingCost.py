"""
In a country where train travel is popular, you have planned some traveling in advance. The days you will travel are
given in the “days” array. Each day is an integer starting at 1.
Train tickets are sold in 3 different ways, and their prices are given in the “costs” array.
1. 1-day pass is sold for costs[0] dollars;
2. 7-day pass is sold for costs[1] dollars; 3. 30-day pass is sold for costs[2] dollars.
An x-day pass allows x days of consecutive travel.
For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.
Return the minimum cost in dollars needed to travel every day in the given list of days.

Problem Understanding (5 min)
Example 1:
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan: On day 1, you bought a 1-day pass for
costs[0] = $2, which covered day 1.
On day 4, you bought a 7-day pass for costs[1] = $7, which covered days 4,5, ..., 10.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20. In total, you spent $11 and covered all the
days of your travel.
Example 2:
Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan: On day 1, you bought a 30-day pass for
costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31. In total, you spent $17 and covered all the
days of your travel.
"""

from typing import List, Dict


def minimumTravellingCost(days: List, passesLookup: Dict):
    minimumCostForDays = [0] * (max(days) + 1)
    for day in range(1, len(minimumCostForDays)):
        if day in days:
            minimumCostForDays[day] = min(
                [price + minimumCostForDays[max(0, day - validDays)] for validDays, price in passesLookup.items()]
            )
        else:
            minimumCostForDays[day] = minimumCostForDays[day - 1]
    return minimumCostForDays[-1]


if __name__ == '__main__':
    print(minimumTravellingCost([1, 4, 6, 7, 8, 20], passesLookup={1: 2, 7: 7, 30: 15}))
