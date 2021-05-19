"""
Power Set: Write a method to return all subsets of a set.
"""

from typing import List


def getPowerSetIteratively(elements: List):
    powerSet = [[]]
    for element in elements:
        tempPowerSet = []
        for pSet in powerSet:
            tempPowerSet.append(pSet + [element])
        powerSet += tempPowerSet
    return powerSet


def getPowerSetRecursively(elements: List):
    if not elements:
        return [[]]
    else:
        lastElement = elements[-1]
        powerSet = []
        powerSet += getPowerSetRecursively(elements[:-1])
        tempPowerSet = []
        for pSet in powerSet:
            tempPowerSet.append(pSet + [lastElement])

        return powerSet + tempPowerSet


if __name__ == '__main__':
    print(getPowerSetIteratively([1, 2, 3]))
    print(getPowerSetRecursively([1, 2, 3]))
